param(
    [ValidateSet('underspecified','sufficient','irrelevant','conflicting')]
    [string[]]$Conditions=@('underspecified','sufficient','irrelevant','conflicting'),
    [ValidateSet('none','baseline')][string[]]$Variants=@('none','baseline'),
    [ValidateSet('claude-opus-5','claude-sonnet','codex-gpt-5.6-sol','codex-gpt-5.3-codex-spark')]
    [string[]]$ProfileKeys=@('claude-opus-5','claude-sonnet','codex-gpt-5.6-sol','codex-gpt-5.3-codex-spark'),
    [Parameter(Mandatory=$true)][string]$OutputRoot,
    [ValidateRange(1,4)][int]$Concurrency=2,
    [switch]$SkipFinished
)
$ErrorActionPreference='Stop'
$repoRoot=Split-Path -Parent $PSScriptRoot
$experimentRoot=Join-Path $repoRoot 'evals\context-effect-v3'
$skillRoot=Join-Path $repoRoot 'plugins\korean-technical-writing-review\skills\korean-technical-writing-review'
$tasks=Get-Content (Join-Path $experimentRoot 'tasks.json') -Raw -Encoding UTF8|ConvertFrom-Json
$schemaPath=Join-Path $experimentRoot 'output-schema.json'
$schemaText=Get-Content $schemaPath -Raw -Encoding UTF8
$userProfile=[Environment]::GetFolderPath('UserProfile')
$codexHome=Join-Path $userProfile '.codex'
$files=@((Join-Path $skillRoot 'SKILL.md'),(Join-Path $skillRoot 'references\rubric.ko.md'),(Join-Path $skillRoot 'references\semantic-fidelity.ko.md'),(Join-Path $skillRoot 'references\output-formats.ko.md'))
$instructions=($files|%{"`n--- $([IO.Path]::GetFileName($_)) ---`n"+(Get-Content $_ -Raw -Encoding UTF8)}) -join "`n"
if(-not [IO.Path]::IsPathRooted($OutputRoot)){$OutputRoot=Join-Path $repoRoot $OutputRoot};$OutputRoot=[IO.Path]::GetFullPath($OutputRoot);New-Item -ItemType Directory -Path $OutputRoot -Force|Out-Null
$profiles=@(
    [pscustomobject]@{agent='claude';model='claude-opus-5';key='claude-opus-5'},
    [pscustomobject]@{agent='claude';model='sonnet';key='claude-sonnet'},
    [pscustomobject]@{agent='codex';model='gpt-5.6-sol';key='codex-gpt-5.6-sol'},
    [pscustomobject]@{agent='codex';model='gpt-5.3-codex-spark';key='codex-gpt-5.3-codex-spark'}
) | Where-Object { $ProfileKeys -contains $_.key }
$jobs=[Collections.Generic.List[object]]::new()
foreach($condition in $Conditions){
    $blocks=@($tasks.cases|? context_condition -eq $condition|%{"### $($_.id)`n[문맥]`n$($_.context)`n`n[검토 대상 문장]`n$($_.target)"})
    $prompt="아래 문서 조각마다 문맥과 검토 대상 문장을 함께 읽고 판정하세요. 문맥에 근거가 있으면 사용하고, 없거나 충돌하면 임의로 확정하지 마세요.`n`n$($blocks -join "`n`n")`n`n반드시 아래 JSON Schema와 정확히 일치하는 JSON 객체 하나만 출력하세요. 다른 필드, 설명, 마크다운 코드 펜스를 추가하지 마세요. evidence_quote는 제공된 문맥의 짧은 직접 인용이어야 합니다. 뜻이 확정되지 않거나 문맥이 충돌하면 suggested_revision은 null로 두세요. 모든 ID를 한 번씩 포함하세요.`n`n$schemaText"
    foreach($variant in $Variants){foreach($profile in $profiles){
        while(($jobs|? State -eq Running).Count -ge $Concurrency){$d=Wait-Job $jobs -Any -Timeout 5;if($d){Receive-Job $d|Out-Host}}
        $dir=Join-Path $OutputRoot (Join-Path $condition (Join-Path $variant $profile.key));New-Item -ItemType Directory -Path $dir -Force|Out-Null;$out=Join-Path $dir 'run-1.md';$meta=Join-Path $dir 'run-1.json'
        if($SkipFinished -and (Test-Path $meta)){if((Get-Content $meta -Raw -Encoding UTF8|ConvertFrom-Json).transport_status -eq 'completed'){continue}}
        $jobs.Add((Start-Job -ArgumentList $profile.agent,$profile.model,$profile.key,$variant,$condition,$prompt,$instructions,$schemaPath,$schemaText,$out,$meta,$repoRoot,$userProfile,$codexHome -ScriptBlock{
            param($agent,$model,$key,$variant,$condition,$prompt,$instructions,$schemaPath,$schemaText,$out,$meta,$repoRoot,$userProfile,$codexHome)
            $env:USERPROFILE=$userProfile
            $env:HOME=$userProfile
            $env:CODEX_HOME=$codexHome
            $OutputEncoding=[Text.UTF8Encoding]::new($false)
            [Console]::OutputEncoding=[Text.UTF8Encoding]::new($false)
            $start=[DateTimeOffset]::UtcNow;$r=[ordered]@{agent=$agent;model=$model;key=$key;variant=$variant;context_condition=$condition;delivery=if($variant -eq 'baseline'){'system_or_developer_instructions'}else{'none'};run=1;started_at=$start.ToString('o');completed_at=$null;elapsed_seconds=$null;transport_status='failed';error=$null;output='run-1.md'}
            try{
                $stderrPath=[IO.Path]::ChangeExtension($meta,'.stderr.txt')
                $rawDebugPath=$null
                if($agent -eq 'claude'){
                    $args=@('-p',$prompt,'--model',$model,'--tools','','--permission-mode','dontAsk','--no-session-persistence','--no-chrome','--strict-mcp-config','--mcp-config','{"mcpServers":{}}','--output-format','text')
                    if($variant -eq 'baseline'){$args+=@('--append-system-prompt',$instructions)}
                    $raw=(& claude @args 2> $stderrPath|Out-String)
                    $rawDebugPath=[IO.Path]::ChangeExtension($out,'.raw.json')
                    Set-Content $rawDebugPath $raw -Encoding UTF8
                    if($LASTEXITCODE -ne 0){throw ((Get-Content $stderrPath -Raw -ErrorAction SilentlyContinue)+$raw)}
                    $value=$raw.Trim()
                    if($value.StartsWith('```json')){$value=$value.Substring(7)}
                    if($value.EndsWith('```')){$value=$value.Substring(0,$value.Length-3)}
                    $value=$value.Trim()
                    Set-Content $out $value -Encoding UTF8
                }else{
                    $args=@('exec','--model',$model,'--sandbox','read-only','--ephemeral','--ignore-rules','--color','never','--skip-git-repo-check','--output-schema',$schemaPath)
                    if($variant -eq 'baseline'){$args+=@('-c',("developer_instructions="+$instructions))};$args+=$prompt
                    $raw=(& codex @args 2> $stderrPath|Out-String);if($LASTEXITCODE -ne 0){throw ((Get-Content $stderrPath -Raw -ErrorAction SilentlyContinue)+$raw)};Set-Content $out $raw.Trim() -Encoding UTF8
                }
                $r.transport_status=if([string]::IsNullOrWhiteSpace((Get-Content $out -Raw -Encoding UTF8))){'empty'}else{'completed'}
            }catch{$r.error=$_.Exception.Message}
            finally{
                $end=[DateTimeOffset]::UtcNow
                $r.completed_at=$end.ToString('o')
                $r.elapsed_seconds=[Math]::Round(($end-$start).TotalSeconds,3)
                $r|ConvertTo-Json -Depth 10|Set-Content $meta -Encoding UTF8
                if($r.transport_status -eq 'completed' -and (Test-Path $stderrPath)){Remove-Item -LiteralPath $stderrPath -Force}
                if($r.transport_status -eq 'completed' -and $rawDebugPath -and (Test-Path $rawDebugPath)){Remove-Item -LiteralPath $rawDebugPath -Force}
                [pscustomobject]@{key=$key;variant=$variant;condition=$condition;status=$r.transport_status;seconds=$r.elapsed_seconds}
            }
        }))
    }}
}
while(($jobs|? State -eq Running).Count){$d=Wait-Job $jobs -Any -Timeout 5;if($d){Receive-Job $d|Out-Host}}
$jobs|? State -ne Running|%{Receive-Job $_ -ErrorAction SilentlyContinue|Out-Host;Remove-Job $_ -Force}
$summary=@(Get-ChildItem $OutputRoot -Filter 'run-1.json' -Recurse|%{Get-Content $_.FullName -Raw -Encoding UTF8|ConvertFrom-Json});$summary|ConvertTo-Json -Depth 10|Set-Content (Join-Path $OutputRoot 'transport-summary.json') -Encoding UTF8;"Completed $($summary.Count) CLI records."
