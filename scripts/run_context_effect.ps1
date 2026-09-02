param(
    [Parameter(Mandatory = $true)][string[]]$Models,
    [ValidateSet('underspecified', 'sufficient', 'irrelevant', 'conflicting')]
    [string[]]$Conditions = @('underspecified', 'sufficient', 'irrelevant', 'conflicting'),
    [ValidateSet('none', 'baseline')][string[]]$Variants = @('none', 'baseline'),
    [ValidateRange(1, 5)][int]$RunCount = 2,
    [Parameter(Mandatory = $true)][string]$OutputRoot,
    [ValidateRange(2048, 65536)][int]$MaxOutputTokens = 16384,
    [ValidateRange(1, 12)][int]$Concurrency = 3,
    [ValidateRange(1, 8)][int]$RetryCount = 5,
    [switch]$SkipFinished
)

$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path -Parent $PSScriptRoot
$experimentRoot = Join-Path $repoRoot 'evals\context-effect-v3'
$skillRoot = Join-Path $repoRoot 'plugins\korean-technical-writing-review\skills\korean-technical-writing-review'
$taskDocument = Get-Content -LiteralPath (Join-Path $experimentRoot 'tasks.json') -Raw -Encoding UTF8 | ConvertFrom-Json
$secretPath = Join-Path $env:USERPROFILE '.codex\secrets\ollama-cloud-api-key.txt'
$token = $env:OLLAMA_API_KEY
if ([string]::IsNullOrWhiteSpace($token) -and (Test-Path -LiteralPath $secretPath)) {
    $token = (Get-Content -LiteralPath $secretPath -Raw -Encoding UTF8).Trim()
}
if ([string]::IsNullOrWhiteSpace($token)) { throw 'Ollama Cloud API 키를 찾지 못했습니다.' }

$instructionFiles = @(
    (Join-Path $skillRoot 'SKILL.md'),
    (Join-Path $skillRoot 'references\rubric.ko.md'),
    (Join-Path $skillRoot 'references\semantic-fidelity.ko.md'),
    (Join-Path $skillRoot 'references\output-formats.ko.md')
)
$baselineInstructions = ($instructionFiles | ForEach-Object {
    "`n--- $([IO.Path]::GetFileName($_)) ---`n" + (Get-Content -LiteralPath $_ -Raw -Encoding UTF8)
}) -join "`n"

if (-not [IO.Path]::IsPathRooted($OutputRoot)) { $OutputRoot = Join-Path $repoRoot $OutputRoot }
$OutputRoot = [IO.Path]::GetFullPath($OutputRoot)
New-Item -ItemType Directory -Path $OutputRoot -Force | Out-Null

$jobs = [Collections.Generic.List[object]]::new()
foreach ($condition in $Conditions) {
    $cases = @($taskDocument.cases | Where-Object context_condition -eq $condition)
    $caseBlocks = foreach ($case in $cases) {
@"
### $($case.id)
[문맥]
$($case.context)

[검토 대상 문장]
$($case.target)
"@
    }
    $prompt = @"
아래 문서 조각마다 문맥과 검토 대상 문장을 함께 읽고 판정하세요. 문맥에 근거가 있으면 근거를 사용하고, 없거나 서로 충돌하면 임의로 확정하지 마세요.

$($caseBlocks -join "`n`n")

JSON만 출력하세요.
{"cases":[{"id":"PERM-U","decision":"통과|구체화 필요|의미 확인 필요","evidence_quote":"문맥의 짧은 직접 인용 또는 null","suggested_revision":"문자열 또는 null","verification_question":"문자열 또는 null"}]}
모든 ID를 한 번씩 포함하세요. `evidence_quote`는 반드시 제공된 문맥에서 그대로 복사한 짧은 구절이어야 합니다. 뜻이 확정되지 않거나 문맥이 충돌하면 `suggested_revision`은 null로 두세요.
"@

    foreach ($variant in $Variants) {
        $instructions = if ($variant -eq 'baseline') { $baselineInstructions } else { '당신은 한국어 기술 문서 편집자입니다.' }
        $sha256 = [Security.Cryptography.SHA256]::Create()
        try {
            $hashBytes = $sha256.ComputeHash([Text.Encoding]::UTF8.GetBytes($instructions))
            $instructionHash = ($hashBytes | ForEach-Object { $_.ToString('x2') }) -join ''
        } finally { $sha256.Dispose() }

        foreach ($model in $Models) {
            foreach ($run in 1..$RunCount) {
                while (($jobs | Where-Object State -eq 'Running').Count -ge $Concurrency) {
                    $done = Wait-Job -Job $jobs -Any -Timeout 5
                    if ($done) { Receive-Job -Job $done | Out-Host }
                }
                $safeModel = $model -replace '[:/]', '-'
                $outputDir = Join-Path $OutputRoot (Join-Path $condition (Join-Path $variant $safeModel))
                New-Item -ItemType Directory -Path $outputDir -Force | Out-Null
                $outputPath = Join-Path $outputDir ("run-{0}.md" -f $run)
                $metadataPath = Join-Path $outputDir ("run-{0}.json" -f $run)
                if ($SkipFinished -and (Test-Path -LiteralPath $metadataPath)) {
                    $existing = Get-Content -LiteralPath $metadataPath -Raw -Encoding UTF8 | ConvertFrom-Json
                    if ($existing.transport_status -in @('completed','empty')) { continue }
                }
                $jobs.Add((Start-Job -ArgumentList @(
                    $model,$run,$variant,$condition,$instructions,$instructionHash,$prompt,$token,$MaxOutputTokens,$outputPath,$metadataPath,$RetryCount
                ) -ScriptBlock {
                    param($model,$run,$variant,$condition,$instructions,$instructionHash,$prompt,$token,$maxOutputTokens,$outputPath,$metadataPath,$retryCount)
                    $startedAt = [DateTimeOffset]::UtcNow
                    $record = [ordered]@{ model=$model; variant=$variant; context_condition=$condition; run=$run; delivery='inline_instructions'; native_skill_loaded=$false; instruction_sha256=$instructionHash; started_at=$startedAt.ToString('o'); completed_at=$null; elapsed_seconds=$null; transport_status='failed'; response_status=$null; incomplete_details=$null; usage=$null; error=$null; output=$null }
                    try {
                        $body = @{ model=$model; instructions=$instructions; input=$prompt; stream=$false; temperature=0; max_output_tokens=$maxOutputTokens; truncation='disabled' } | ConvertTo-Json -Depth 12
                        $response = $null
                        foreach ($attempt in 0..$retryCount) {
                            try {
                                $response = Invoke-RestMethod -Method Post -Uri 'https://ollama.com/v1/responses' -Headers @{Authorization="Bearer $token"} -ContentType 'application/json; charset=utf-8' -Body ([Text.Encoding]::UTF8.GetBytes($body)) -TimeoutSec 900
                                break
                            } catch {
                                if ($_.Exception.Message -notmatch '429' -or $attempt -ge $retryCount) { throw }
                                Start-Sleep -Seconds ([Math]::Min(120, 15 * ($attempt + 1) + (Get-Random -Minimum 0 -Maximum 11)))
                            }
                        }
                        $parts = foreach($item in $response.output){ foreach($content in $item.content){ if($content.type -eq 'output_text'){$content.text} } }
                        $text = ($parts -join "`n").Trim()
                        Set-Content -LiteralPath $outputPath -Value $text -Encoding UTF8
                        $record.transport_status = if([string]::IsNullOrWhiteSpace($text)){'empty'}else{'completed'}
                        $record.response_status=$response.status; $record.incomplete_details=$response.incomplete_details; $record.usage=$response.usage; $record.output=[IO.Path]::GetFileName($outputPath)
                    } catch { $record.error=$_.Exception.Message -replace 'Bearer\s+\S+','Bearer [REDACTED]' }
                    finally {
                        $finishedAt=[DateTimeOffset]::UtcNow; $record.completed_at=$finishedAt.ToString('o'); $record.elapsed_seconds=[Math]::Round(($finishedAt-$startedAt).TotalSeconds,3)
                        $record|ConvertTo-Json -Depth 12|Set-Content -LiteralPath $metadataPath -Encoding UTF8
                        [pscustomobject]@{model=$model;variant=$variant;condition=$condition;run=$run;status=$record.transport_status;seconds=$record.elapsed_seconds}
                    }
                }))
            }
        }
    }
}

while (($jobs | Where-Object State -eq 'Running').Count -gt 0) {
    $done=Wait-Job -Job $jobs -Any -Timeout 5; if($done){Receive-Job -Job $done|Out-Host}
}
$jobs|Where-Object State -ne 'Running'|ForEach-Object{Receive-Job -Job $_ -ErrorAction SilentlyContinue|Out-Host;Remove-Job -Job $_ -Force}
$summary=@(Get-ChildItem -LiteralPath $OutputRoot -Filter 'run-*.json' -Recurse|ForEach-Object{Get-Content $_.FullName -Raw -Encoding UTF8|ConvertFrom-Json})
$summary|ConvertTo-Json -Depth 12|Set-Content -LiteralPath (Join-Path $OutputRoot 'transport-summary.json') -Encoding UTF8
Write-Output ("Completed {0} context-effect records." -f $summary.Count)
