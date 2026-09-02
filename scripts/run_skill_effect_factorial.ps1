param(
    [Parameter(Mandatory = $true)]
    [string[]]$Models,

    [ValidateSet('development', 'holdout')]
    [string]$TaskSet = 'development',

    [ValidateSet('none', 'baseline', 'certainty', 'conflict', 'combined')]
    [string[]]$Variants = @('none', 'baseline', 'certainty', 'conflict', 'combined'),

    [ValidateRange(1, 10)]
    [int]$RunCount = 3,

    [Parameter(Mandatory = $true)]
    [string]$OutputRoot,

    [ValidateRange(1024, 131072)]
    [int]$MaxOutputTokens = 32768,

    [ValidateRange(1, 12)]
    [int]$Concurrency = 4
)

$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path -Parent $PSScriptRoot
$experimentRoot = Join-Path $repoRoot 'evals\skill-effect-v2'
$skillRoot = Join-Path $repoRoot 'plugins\korean-technical-writing-review\skills\korean-technical-writing-review'
$taskPath = Join-Path $experimentRoot ("tasks\{0}.json" -f $TaskSet)
$secretPath = Join-Path $env:USERPROFILE '.codex\secrets\ollama-cloud-api-key.txt'

$token = $env:OLLAMA_API_KEY
if ([string]::IsNullOrWhiteSpace($token) -and (Test-Path -LiteralPath $secretPath)) {
    $token = (Get-Content -LiteralPath $secretPath -Raw -Encoding UTF8).Trim()
}
if ([string]::IsNullOrWhiteSpace($token)) {
    throw 'OLLAMA_API_KEY 또는 Codex 비밀 파일에서 Ollama Cloud API 키를 찾지 못했습니다.'
}

$taskDocument = Get-Content -LiteralPath $taskPath -Raw -Encoding UTF8 | ConvertFrom-Json
$caseLines = foreach ($case in $taskDocument.cases) {
    "- $($case.id): $($case.text)"
}
$prompt = @"
다음 한국어 기술 문장을 각각 검토하고 수정 필요 여부를 판정하세요.

$($caseLines -join "`n")

JSON만 출력하세요. 스키마는 다음과 같습니다.
{"cases":[{"id":"DEV-A01","decision":"통과|구체화 필요|의미 확인 필요","reader_must_infer":"문자열 또는 null","suggested_revision":"문자열 또는 null","verification_question":"문자열 또는 null"}]}
입력된 모든 ID를 한 번씩 포함하고, 입력에 없는 ID는 추가하지 마세요.
"@

$instructionFiles = @(
    (Join-Path $skillRoot 'SKILL.md'),
    (Join-Path $skillRoot 'references\rubric.ko.md'),
    (Join-Path $skillRoot 'references\semantic-fidelity.ko.md'),
    (Join-Path $skillRoot 'references\output-formats.ko.md')
)
$baselineInstructions = ($instructionFiles | ForEach-Object {
    "`n--- $([IO.Path]::GetFileName($_)) ---`n" + (Get-Content -LiteralPath $_ -Raw -Encoding UTF8)
}) -join "`n"
$certainty = Get-Content -LiteralPath (Join-Path $experimentRoot 'candidates\certainty.md') -Raw -Encoding UTF8
$conflict = Get-Content -LiteralPath (Join-Path $experimentRoot 'candidates\conflict.md') -Raw -Encoding UTF8

function Get-VariantInstructions([string]$Variant) {
    switch ($Variant) {
        'none' { return '당신은 한국어 기술 문서 편집자입니다.' }
        'baseline' { return $baselineInstructions }
        'certainty' { return $baselineInstructions + "`n`n" + $certainty }
        'conflict' { return $baselineInstructions + "`n`n" + $conflict }
        'combined' { return $baselineInstructions + "`n`n" + $certainty + "`n`n" + $conflict }
    }
}

if (-not [IO.Path]::IsPathRooted($OutputRoot)) {
    $OutputRoot = Join-Path $repoRoot $OutputRoot
}
$OutputRoot = [IO.Path]::GetFullPath($OutputRoot)
$setRoot = Join-Path $OutputRoot $TaskSet
New-Item -ItemType Directory -Path $setRoot -Force | Out-Null

$jobs = [Collections.Generic.List[object]]::new()
foreach ($variant in $Variants) {
    $instructions = Get-VariantInstructions $variant
    $sha256 = [Security.Cryptography.SHA256]::Create()
    try {
        $hashBytes = $sha256.ComputeHash([Text.Encoding]::UTF8.GetBytes($instructions))
        $instructionHash = ($hashBytes | ForEach-Object { $_.ToString('x2') }) -join ''
    }
    finally {
        $sha256.Dispose()
    }
    foreach ($model in $Models) {
        foreach ($run in 1..$RunCount) {
            while (($jobs | Where-Object State -eq 'Running').Count -ge $Concurrency) {
                $done = Wait-Job -Job $jobs -Any -Timeout 5
                if ($done) { Receive-Job -Job $done | Out-Host }
            }

            $safeModel = $model -replace '[:/]', '-'
            $outputDir = Join-Path $setRoot (Join-Path $variant $safeModel)
            New-Item -ItemType Directory -Path $outputDir -Force | Out-Null
            $outputPath = Join-Path $outputDir ("run-{0}.md" -f $run)
            $metadataPath = Join-Path $outputDir ("run-{0}.json" -f $run)

            $jobs.Add((Start-Job -ArgumentList @(
                $model, $run, $variant, $TaskSet, $instructions, $instructionHash,
                $prompt, $token, $MaxOutputTokens, $outputPath, $metadataPath
            ) -ScriptBlock {
                param($model, $run, $variant, $taskSet, $instructions, $instructionHash, $prompt, $token, $maxOutputTokens, $outputPath, $metadataPath)
                $startedAt = [DateTimeOffset]::UtcNow
                $record = [ordered]@{
                    model = $model
                    variant = $variant
                    task_set = $taskSet
                    delivery = 'inline_instructions'
                    native_skill_loaded = $false
                    instruction_sha256 = $instructionHash
                    run = $run
                    started_at = $startedAt.ToString('o')
                    completed_at = $null
                    elapsed_seconds = $null
                    transport_status = 'failed'
                    response_status = $null
                    incomplete_details = $null
                    response_output_types = $null
                    usage = $null
                    error = $null
                    output = $null
                }
                try {
                    $body = @{
                        model = $model
                        instructions = $instructions
                        input = $prompt
                        stream = $false
                        temperature = 0
                        max_output_tokens = $maxOutputTokens
                        truncation = 'disabled'
                    } | ConvertTo-Json -Depth 12
                    $response = Invoke-RestMethod `
                        -Method Post `
                        -Uri 'https://ollama.com/v1/responses' `
                        -Headers @{ Authorization = "Bearer $token" } `
                        -ContentType 'application/json; charset=utf-8' `
                        -Body ([Text.Encoding]::UTF8.GetBytes($body)) `
                        -TimeoutSec 900

                    $parts = foreach ($item in $response.output) {
                        foreach ($content in $item.content) {
                            if ($content.type -eq 'output_text') { $content.text }
                        }
                    }
                    $text = ($parts -join "`n").Trim()
                    Set-Content -LiteralPath $outputPath -Value $text -Encoding UTF8
                    $record.transport_status = if ([string]::IsNullOrWhiteSpace($text)) { 'empty' } else { 'completed' }
                    $record.response_status = $response.status
                    $record.incomplete_details = $response.incomplete_details
                    $record.response_output_types = @($response.output | ForEach-Object {
                        $item = $_
                        [pscustomobject]@{
                            type = $item.type
                            content_types = @($item.content | ForEach-Object { $_.type })
                        }
                    })
                    $record.usage = $response.usage
                    $record.output = [IO.Path]::GetFileName($outputPath)
                }
                catch {
                    $record.error = $_.Exception.Message -replace 'Bearer\s+\S+', 'Bearer [REDACTED]'
                }
                finally {
                    $finishedAt = [DateTimeOffset]::UtcNow
                    $record.completed_at = $finishedAt.ToString('o')
                    $record.elapsed_seconds = [Math]::Round(($finishedAt - $startedAt).TotalSeconds, 3)
                    $record | ConvertTo-Json -Depth 12 | Set-Content -LiteralPath $metadataPath -Encoding UTF8
                    [pscustomobject]@{
                        model = $model
                        variant = $variant
                        task_set = $taskSet
                        run = $run
                        status = $record.transport_status
                        elapsed_seconds = $record.elapsed_seconds
                    }
                }
            }))
        }
    }
}

while (($jobs | Where-Object State -eq 'Running').Count -gt 0) {
    $done = Wait-Job -Job $jobs -Any -Timeout 5
    if ($done) { Receive-Job -Job $done | Out-Host }
}
$jobs | Where-Object State -ne 'Running' | ForEach-Object {
    Receive-Job -Job $_ -ErrorAction SilentlyContinue | Out-Host
    Remove-Job -Job $_ -Force
}

$summary = @(Get-ChildItem -LiteralPath $setRoot -Filter 'run-*.json' -Recurse | ForEach-Object {
    Get-Content -LiteralPath $_.FullName -Raw -Encoding UTF8 | ConvertFrom-Json
})
$summary | ConvertTo-Json -Depth 12 | Set-Content -LiteralPath (Join-Path $setRoot 'transport-summary.json') -Encoding UTF8
Write-Output ("Completed {0} records for task set '{1}'." -f $summary.Count, $TaskSet)
