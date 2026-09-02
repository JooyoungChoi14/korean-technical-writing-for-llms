param(
    [ValidateSet('baseline','candidate')][string[]]$Variants=@('baseline','candidate'),
    [ValidateSet('claude-fable-5','claude-sonnet','claude-haiku-4-5','codex-gpt-5.6-sol','codex-gpt-5.4-mini','codex-gpt-5.3-codex-spark')]
    [string[]]$ProfileKeys=@('claude-fable-5','claude-sonnet','claude-haiku-4-5','codex-gpt-5.6-sol','codex-gpt-5.4-mini','codex-gpt-5.3-codex-spark'),
    [ValidateRange(1,5)][int]$Runs=3,
    [Parameter(Mandatory=$true)][string]$OutputRoot,
    [ValidateRange(1,3)][int]$Concurrency=2,
    [switch]$SkipFinished
)
$ErrorActionPreference='Stop'
$repoRoot=Split-Path -Parent $PSScriptRoot
$experimentRoot=Join-Path $repoRoot 'evals\naturalness-tuning-v5'
$skillRoot=Join-Path $repoRoot 'plugins\korean-technical-writing-review\skills\korean-technical-writing-review'
$tasks=Get-Content (Join-Path $experimentRoot 'tasks.json') -Raw -Encoding UTF8|ConvertFrom-Json
$schemaPath=Join-Path $experimentRoot 'output-schema.json'
$schemaText=Get-Content $schemaPath -Raw -Encoding UTF8
$referenceFiles=@((Join-Path $skillRoot 'references\rubric.ko.md'),(Join-Path $skillRoot 'references\semantic-fidelity.ko.md'),(Join-Path $skillRoot 'references\output-formats.ko.md'))
$references=($referenceFiles|ForEach-Object{"`n--- $([IO.Path]::GetFileName($_)) ---`n"+(Get-Content $_ -Raw -Encoding UTF8)}) -join "`n"
$variantInstructions=@{
    baseline=("`n--- SKILL.md ---`n"+(Get-Content (Join-Path $skillRoot 'SKILL.md') -Raw -Encoding UTF8)+$references)
    candidate=("`n--- SKILL.md ---`n"+(Get-Content (Join-Path $experimentRoot 'candidate-SKILL.md') -Raw -Encoding UTF8)+$references)
}
if(-not [IO.Path]::IsPathRooted($OutputRoot)){$OutputRoot=Join-Path $repoRoot $OutputRoot}
$OutputRoot=[IO.Path]::GetFullPath($OutputRoot);New-Item -ItemType Directory -Path $OutputRoot -Force|Out-Null
$profiles=@(
    [pscustomobject]@{agent='claude';model='claude-fable-5';key='claude-fable-5'},
    [pscustomobject]@{agent='claude';model='sonnet';key='claude-sonnet'},
    [pscustomobject]@{agent='claude';model='claude-haiku-4-5';key='claude-haiku-4-5'},
    [pscustomobject]@{agent='codex';model='gpt-5.6-sol';key='codex-gpt-5.6-sol'},
    [pscustomobject]@{agent='codex';model='gpt-5.4-mini';key='codex-gpt-5.4-mini'},
    [pscustomobject]@{agent='codex';model='gpt-5.3-codex-spark';key='codex-gpt-5.3-codex-spark'}
)|Where-Object{$ProfileKeys -contains $_.key}
$blocks=@($tasks.cases|ForEach-Object{"### $($_.id)`n[문맥]`n$($_.context)`n`n[검토 대상 문장]`n$($_.target)"})
$prompt="아래 문서 조각마다 검토 대상 문장이 자연스럽고 명확한 한국어 기술 문장인지 평가하세요. 문맥에는 뜻을 확정하는 데 필요한 정보가 들어 있습니다. 고칠 필요가 있으면 문맥의 사실을 유지한 수정문을 제안하고, 이미 자연스럽고 명확하면 통과시키고 suggested_revision을 null로 두세요.`n`n$($blocks -join "`n`n")`n`n반드시 아래 JSON Schema와 정확히 일치하는 JSON 객체 하나만 출력하세요. 다른 필드, 설명, 마크다운 코드 펜스를 추가하지 마세요. 모든 ID를 한 번씩 포함하세요.`n`n$schemaText"
$jobs=[Collections.Generic.List[object]]::new()
foreach($run in 1..$Runs){foreach($variant in $Variants){foreach($profile in $profiles){
    while(($jobs|Where-Object State -eq Running).Count -ge $Concurrency){$done=Wait-Job $jobs -Any -Timeout 5;if($done){Receive-Job $done|Out-Host}}
    $dir=Join-Path $OutputRoot (Join-Path $variant $profile.key);New-Item -ItemType Directory -Path $dir -Force|Out-Null;$out=Join-Path $dir "run-$run.md";$meta=Join-Path $dir "run-$run.json"
    if($SkipFinished -and (Test-Path -LiteralPath $meta)){if((Get-Content $meta -Raw -Encoding UTF8|ConvertFrom-Json).transport_status -eq 'completed'){continue}}
    $instructions=$variantInstructions[$variant]
    $jobs.Add((Start-Job -ArgumentList $profile.agent,$profile.model,$profile.key,$variant,$run,$prompt,$instructions,$schemaPath,$out,$meta -ScriptBlock{
        param($agent,$model,$key,$variant,$run,$prompt,$instructions,$schemaPath,$out,$meta)
        $OutputEncoding=[Text.UTF8Encoding]::new($false);[Console]::OutputEncoding=[Text.UTF8Encoding]::new($false)
        $start=[DateTimeOffset]::UtcNow;$record=[ordered]@{agent=$agent;model=$model;key=$key;variant=$variant;delivery='system_or_developer_instructions';run=$run;started_at=$start.ToString('o');completed_at=$null;elapsed_seconds=$null;transport_status='failed';error=$null;output="run-$run.md"}
        try{
            $stderrPath=[IO.Path]::ChangeExtension($meta,'.stderr.txt');$rawDebugPath=$null
            if($agent -eq 'claude'){
                $args=@('-p',$prompt,'--model',$model,'--tools','','--permission-mode','dontAsk','--no-session-persistence','--no-chrome','--strict-mcp-config','--mcp-config','{"mcpServers":{}}','--output-format','text','--append-system-prompt',$instructions)
                $raw=(& claude @args 2> $stderrPath|Out-String);$rawDebugPath=[IO.Path]::ChangeExtension($out,'.raw.json');Set-Content $rawDebugPath $raw -Encoding UTF8;if($LASTEXITCODE -ne 0){throw ((Get-Content $stderrPath -Raw -ErrorAction SilentlyContinue)+$raw)};$value=$raw.Trim();if($value.StartsWith('```json')){$value=$value.Substring(7)};if($value.EndsWith('```')){$value=$value.Substring(0,$value.Length-3)};Set-Content $out $value.Trim() -Encoding UTF8
            }else{
                $args=@('exec','--model',$model,'--sandbox','read-only','--ephemeral','--ignore-rules','--color','never','--skip-git-repo-check','--output-schema',$schemaPath,'-c',("developer_instructions="+$instructions),$prompt)
                $raw=(& codex @args 2> $stderrPath|Out-String);if($LASTEXITCODE -ne 0){throw ((Get-Content $stderrPath -Raw -ErrorAction SilentlyContinue)+$raw)};Set-Content $out $raw.Trim() -Encoding UTF8
            }
            $record.transport_status=if([string]::IsNullOrWhiteSpace((Get-Content $out -Raw -Encoding UTF8))){'empty'}else{'completed'}
        }catch{$record.error=$_.Exception.Message}
        finally{$end=[DateTimeOffset]::UtcNow;$record.completed_at=$end.ToString('o');$record.elapsed_seconds=[Math]::Round(($end-$start).TotalSeconds,3);$record|ConvertTo-Json -Depth 10|Set-Content $meta -Encoding UTF8;if($record.transport_status -eq 'completed' -and (Test-Path -LiteralPath $stderrPath)){Remove-Item -LiteralPath $stderrPath -Force};if($record.transport_status -eq 'completed' -and $rawDebugPath -and (Test-Path -LiteralPath $rawDebugPath)){Remove-Item -LiteralPath $rawDebugPath -Force};[pscustomobject]@{key=$key;variant=$variant;run=$run;status=$record.transport_status;seconds=$record.elapsed_seconds}}
    }))
}}}
while(($jobs|Where-Object State -eq Running).Count){$done=Wait-Job $jobs -Any -Timeout 5;if($done){Receive-Job $done|Out-Host}}
$jobs|Where-Object State -ne Running|ForEach-Object{Receive-Job $_ -ErrorAction SilentlyContinue|Out-Host;Remove-Job $_ -Force}
$summary=@(Get-ChildItem $OutputRoot -Filter 'run-*.json' -Recurse|ForEach-Object{Get-Content $_.FullName -Raw -Encoding UTF8|ConvertFrom-Json});$summary|ConvertTo-Json -Depth 10|Set-Content (Join-Path $OutputRoot 'transport-summary.json') -Encoding UTF8;"Completed $($summary.Count) CLI records."
