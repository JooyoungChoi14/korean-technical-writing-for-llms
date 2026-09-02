param(
    [Parameter(Mandatory = $true)]
    [string[]]$Models,

    [ValidateSet('baseline', 'self-check', 'counterexample', 'cross-boundary', 'task-specific')]
    [string]$Variant = 'baseline',

    [ValidateRange(1, 10)]
    [int]$RunCount = 3,

    [Parameter(Mandatory = $true)]
    [string]$OutputRoot,

    [ValidateRange(1024, 131072)]
    [int]$MaxOutputTokens = 16384,

    [ValidateRange(1, 10)]
    [int]$Concurrency = 3
)

$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path -Parent $PSScriptRoot
$skillRoot = Join-Path $repoRoot 'plugins\korean-technical-writing-review\skills\korean-technical-writing-review'
$promptPath = Join-Path $repoRoot 'evals\cli-smoke\prompt.ko.txt'
$secretPath = Join-Path $env:USERPROFILE '.codex\secrets\ollama-cloud-api-key.txt'

$token = $env:OLLAMA_API_KEY
if ([string]::IsNullOrWhiteSpace($token) -and (Test-Path -LiteralPath $secretPath)) {
    $token = (Get-Content -LiteralPath $secretPath -Raw -Encoding UTF8).Trim()
}
if ([string]::IsNullOrWhiteSpace($token)) {
    throw 'OLLAMA_API_KEY 또는 Codex 비밀 파일에서 Ollama Cloud API 키를 찾지 못했습니다.'
}

$instructionFiles = @(
    (Join-Path $skillRoot 'SKILL.md'),
    (Join-Path $skillRoot 'references\rubric.ko.md'),
    (Join-Path $skillRoot 'references\semantic-fidelity.ko.md'),
    (Join-Path $skillRoot 'references\output-formats.ko.md')
)
$instructions = ($instructionFiles | ForEach-Object {
    "`n--- $([IO.Path]::GetFileName($_)) ---`n" + (Get-Content -LiteralPath $_ -Raw -Encoding UTF8)
}) -join "`n"

$variantInstructions = switch ($Variant) {
    'baseline' { '' }
    'self-check' {
@'

답변을 제출하기 전에 다음 두 항목을 자체 점검하세요.
1. 같은 문장을 요약에서는 통과시키고 표에서는 문제로 판정하는 등 답변 내부의 판정이 충돌하지 않아야 합니다.
2. 원문에서 확정할 수 없는 구현체·자료 구조·정책을 수정안에 사실처럼 추가하지 말고, 필요한 최소 확인 질문을 남기세요.
'@
    }
    'counterexample' {
@'

답변을 제출하기 전에 다음 세 항목을 자체 점검하세요.
1. 같은 문장을 요약에서는 통과시키고 표에서는 문제로 판정하는 등 답변 내부의 판정이 충돌하지 않아야 합니다.
2. 원문에서 확정할 수 없는 구현체·자료 구조·정책을 수정안에 사실처럼 추가하지 말고, 필요한 최소 확인 질문을 남기세요.
3. 여러 규칙의 적용 순서와 일반적인 우선 원칙이 함께 제시되면, 서로 다른 범주의 규칙 두 개가 동시에 성립하는 반례를 만들어 최종 결과가 하나로 결정되는지 검사하세요. 결정할 수 없다면 그 구체적인 규칙 조합을 확인 질문에 명시하세요.
'@
    }
    'cross-boundary' {
@'

답변을 제출하기 전에 다음 세 항목을 자체 점검하세요.
1. 같은 문장을 요약에서는 통과시키고 표에서는 문제로 판정하는 등 답변 내부의 판정이 충돌하지 않아야 합니다.
2. 원문에서 확정할 수 없는 구현체·자료 구조·정책을 수정안에 사실처럼 추가하지 말고, 필요한 최소 확인 질문을 남기세요.
3. 서로 다른 출처나 범주의 규칙이 우선순위로 나열되고 허용·거부처럼 반대 결과가 섞여 있으면, 앞선 범주의 허용과 뒤 범주의 거부가 동시에 성립하는 조합을 반드시 대입하세요. 나열 순서와 일반 우선 원칙이 서로 다른 결과를 만들면 그 조합과 최종 결과를 확인 질문에 명시하세요.
'@
    }
    'task-specific' {
@'

답변을 제출하기 전에 다음 세 항목을 자체 점검하세요.
1. 같은 문장을 요약에서는 통과시키고 표에서는 문제로 판정하는 등 답변 내부의 판정이 충돌하지 않아야 합니다.
2. 원문에서 확정할 수 없는 구현체·자료 구조·정책을 수정안에 사실처럼 추가하지 말고, 필요한 최소 확인 질문을 남기세요.
3. 권한 규칙을 검토할 때 사용자에게 직접 부여된 허용과 역할에서 부여된 거부가 동시에 성립하는 경우를 대입해 최종 결과가 무엇인지 확인하세요. 원문으로 결정할 수 없다면 이 조합을 그대로 질문으로 남기세요.
'@
    }
}
$instructions += $variantInstructions
$prompt = Get-Content -LiteralPath $promptPath -Raw -Encoding UTF8
$prompt = $prompt -replace '^\$korean-technical-writing-review\s*', ''

$variantRoot = Join-Path $OutputRoot $Variant
New-Item -ItemType Directory -Path $variantRoot -Force | Out-Null

$jobs = [Collections.Generic.List[object]]::new()
foreach ($model in $Models) {
    foreach ($run in 1..$RunCount) {
        while (($jobs | Where-Object State -eq 'Running').Count -ge $Concurrency) {
            $done = Wait-Job -Job $jobs -Any -Timeout 5
            if ($done) { Receive-Job -Job $done | Out-Host }
        }

        $safeModel = $model -replace '[:/]', '-'
        $outputDir = Join-Path $variantRoot $safeModel
        New-Item -ItemType Directory -Path $outputDir -Force | Out-Null
        $outputPath = Join-Path $outputDir ("run-{0}.md" -f $run)
        $metadataPath = Join-Path $outputDir ("run-{0}.json" -f $run)

        $jobs.Add((Start-Job -ArgumentList @(
            $model, $run, $Variant, $instructions, $prompt, $token,
            $MaxOutputTokens, $outputPath, $metadataPath
        ) -ScriptBlock {
            param($model, $run, $variant, $instructions, $prompt, $token, $maxOutputTokens, $outputPath, $metadataPath)
            $startedAt = [DateTimeOffset]::UtcNow
            $record = [ordered]@{
                model = $model
                variant = $variant
                run = $run
                started_at = $startedAt.ToString('o')
                completed_at = $null
                elapsed_seconds = $null
                status = 'failed'
                response_status = $null
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
                    -TimeoutSec 600

                $parts = foreach ($item in $response.output) {
                    foreach ($content in $item.content) {
                        if ($content.type -eq 'output_text') { $content.text }
                    }
                }
                $text = ($parts -join "`n").Trim()
                Set-Content -LiteralPath $outputPath -Value $text -Encoding UTF8
                $record.status = if ([string]::IsNullOrWhiteSpace($text)) { 'empty' } else { 'completed' }
                $record.response_status = $response.status
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
                    run = $run
                    status = $record.status
                    elapsed_seconds = $record.elapsed_seconds
                    output = $outputPath
                }
            }
        }))
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

$summary = Get-ChildItem -LiteralPath $variantRoot -Filter 'run-*.json' -Recurse | ForEach-Object {
    Get-Content -LiteralPath $_.FullName -Raw -Encoding UTF8 | ConvertFrom-Json
}
$summary | ConvertTo-Json -Depth 12 | Set-Content -LiteralPath (Join-Path $variantRoot 'summary.json') -Encoding UTF8

Write-Output ("Completed {0} records for variant '{1}'." -f $summary.Count, $Variant)
