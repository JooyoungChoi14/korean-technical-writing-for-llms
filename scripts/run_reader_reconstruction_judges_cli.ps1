param(
    [ValidateSet('claude-fable-5','codex-gpt-5.6-sol')]
    [string[]]$Judges=@('claude-fable-5','codex-gpt-5.6-sol'),
    [string]$ClaudeModel='claude-fable-5',
    [Parameter(Mandatory=$true)][string]$OutputRoot,
    [string]$BatchRoot='',
    [ValidateRange(1,60)][int]$ChunkSize=20,
    [ValidateRange(1,3)][int]$Concurrency=2,
    [switch]$SkipFinished
)
$ErrorActionPreference='Stop'
$repoRoot=Split-Path -Parent $PSScriptRoot
$experimentRoot=Join-Path $repoRoot 'evals\reader-reconstruction-v6'
if([string]::IsNullOrWhiteSpace($BatchRoot)){$BatchRoot=Join-Path $experimentRoot 'batches'}elseif(-not [IO.Path]::IsPathRooted($BatchRoot)){$BatchRoot=Join-Path $repoRoot $BatchRoot}
$BatchRoot=[IO.Path]::GetFullPath($BatchRoot)
$schemaPath=Join-Path $experimentRoot 'judge-output-schema.json'
$mcpConfigPath=Join-Path $experimentRoot 'empty-mcp.json'
$schemaText=Get-Content $schemaPath -Raw -Encoding UTF8
if(-not [IO.Path]::IsPathRooted($OutputRoot)){$OutputRoot=Join-Path $repoRoot $OutputRoot}
$OutputRoot=[IO.Path]::GetFullPath($OutputRoot)
New-Item -ItemType Directory -Path $OutputRoot -Force|Out-Null
$profiles=@(
    [pscustomobject]@{agent='claude';model=$ClaudeModel;judge='claude-fable-5'},
    [pscustomobject]@{agent='codex';model='gpt-5.6-sol';judge='codex-gpt-5.6-sol'}
)|Where-Object{$Judges -contains $_.judge}
$instruction=@'
당신은 문장 선호도가 아니라 명시적 의미 포함 여부만 판정하는 평가자입니다.
각 항목에서 revision 문장 자체가 proposition을 직접 진술하거나 모호하지 않게 바꾸어 말했을 때만 explicitly_entailed를 true로 두세요.
명제 목록을 단서로 빠진 주체, 동작, 대상, 조건, 결과를 추론하거나 보충하지 마세요. revision이 비어 있으면 모두 false입니다.
actor_and_action_explicit는 revision만 읽고 누가 또는 무엇이 어떤 핵심 동작을 하는지 둘 다 알 수 있을 때만 true입니다.
입력의 모든 item_id와 proposition id를 빠짐없이 한 번씩 반환하세요.
'@
$jobs=[Collections.Generic.List[object]]::new()
foreach($profile in $profiles){
    $judgeDir=Join-Path $BatchRoot $profile.judge
    foreach($batch in Get-ChildItem $judgeDir -Filter 'batch-*.json'|Sort-Object Name){
      $batchPayload=Get-Content $batch.FullName -Raw -Encoding UTF8|ConvertFrom-Json
      for($startIndex=0;$startIndex -lt $batchPayload.items.Count;$startIndex+=$ChunkSize){
        [int]$part=1+[Math]::Floor($startIndex/$ChunkSize);$partItems=@($batchPayload.items|Select-Object -Skip $startIndex -First $ChunkSize)
        while(($jobs|Where-Object State -eq Running).Count -ge $Concurrency){$done=Wait-Job $jobs -Any -Timeout 5;if($done){Receive-Job $done|Out-Host}}
        $dir=Join-Path $OutputRoot $profile.judge;New-Item -ItemType Directory -Path $dir -Force|Out-Null
        $base="$([IO.Path]::GetFileNameWithoutExtension($batch.Name))-part-$($part.ToString('D2'))"
        $out=Join-Path $dir "$base.output.json";$meta=Join-Path $dir "$base.meta.json"
        if($SkipFinished -and (Test-Path -LiteralPath $meta)){if((Get-Content $meta -Raw -Encoding UTF8|ConvertFrom-Json).transport_status -eq 'completed'){continue}}
        $batchText=[ordered]@{judge=$batchPayload.judge;items=$partItems}|ConvertTo-Json -Depth 12
        $batchCount=$partItems.Count
        $prompt="$instruction`n반드시 아래 JSON Schema와 일치하는 JSON 객체 하나만 출력하세요. 설명이나 코드 펜스를 추가하지 마세요.`n`n[JSON Schema]`n$schemaText`n`n[판정 대상]`n$batchText"
        $jobs.Add((Start-Job -ArgumentList $profile.agent,$profile.model,$profile.judge,$batch.FullName,$batchCount,$prompt,$schemaPath,$mcpConfigPath,$out,$meta -ScriptBlock{
            param($agent,$model,$judge,$batchFile,$batchCount,$prompt,$schemaPath,$mcpConfigPath,$out,$meta)
            $OutputEncoding=[Text.UTF8Encoding]::new($false);[Console]::OutputEncoding=[Text.UTF8Encoding]::new($false)
            $start=[DateTimeOffset]::UtcNow;$stderrPath=[IO.Path]::ChangeExtension($meta,'.stderr.txt');$rawDebugPath=$null
            $record=[ordered]@{judge=$judge;agent=$agent;model=$model;batch_file=$batchFile;started_at=$start.ToString('o');completed_at=$null;elapsed_seconds=$null;transport_status='failed';error=$null;output=[IO.Path]::GetFileName($out)}
            try{
                if($agent -eq 'claude'){
                    $args=@('-p','--model',$model,'--tools','','--permission-mode','dontAsk','--no-session-persistence','--no-chrome','--strict-mcp-config','--mcp-config',$mcpConfigPath,'--output-format','text')
                    $raw=($prompt|& claude @args 2> $stderrPath|Out-String);$rawDebugPath=[IO.Path]::ChangeExtension($out,'.raw.txt');Set-Content $rawDebugPath $raw -Encoding UTF8
                    if($LASTEXITCODE -ne 0){throw ((Get-Content $stderrPath -Raw -ErrorAction SilentlyContinue)+$raw)}
                    $value=$raw.Trim();if($value.StartsWith('```json')){$value=$value.Substring(7)}elseif($value.StartsWith('```')){$value=$value.Substring(3)};if($value.EndsWith('```')){$value=$value.Substring(0,$value.Length-3)};Set-Content $out $value.Trim() -Encoding UTF8
                }else{
                    $args=@('exec','--model',$model,'--sandbox','read-only','--ephemeral','--ignore-rules','--color','never','--skip-git-repo-check','--output-schema',$schemaPath,'-')
                    $raw=($prompt|& codex @args 2> $stderrPath|Out-String);if($LASTEXITCODE -ne 0){throw ((Get-Content $stderrPath -Raw -ErrorAction SilentlyContinue)+$raw)};Set-Content $out $raw.Trim() -Encoding UTF8
                }
                $parsed=Get-Content $out -Raw -Encoding UTF8|ConvertFrom-Json
                if($null -eq $parsed.judgments){throw 'judgments 배열이 없습니다.'}
                if(@($parsed.judgments).Count -ne $batchCount){throw "judgments 수가 입력 항목 수와 다릅니다: $(@($parsed.judgments).Count)/$batchCount"}
                $record.transport_status='completed'
            }catch{$record.error=$_.Exception.Message}
            finally{$end=[DateTimeOffset]::UtcNow;$record.completed_at=$end.ToString('o');$record.elapsed_seconds=[Math]::Round(($end-$start).TotalSeconds,3);$record|ConvertTo-Json -Depth 10|Set-Content $meta -Encoding UTF8;if($record.transport_status -eq 'completed' -and (Test-Path -LiteralPath $stderrPath)){Remove-Item -LiteralPath $stderrPath -Force};if($record.transport_status -eq 'completed' -and $rawDebugPath -and (Test-Path -LiteralPath $rawDebugPath)){Remove-Item -LiteralPath $rawDebugPath -Force};[pscustomobject]@{judge=$judge;batch=[IO.Path]::GetFileName($batchFile);status=$record.transport_status;seconds=$record.elapsed_seconds}}
        }))
      }
    }
}
while(($jobs|Where-Object State -eq Running).Count){$done=Wait-Job $jobs -Any -Timeout 5;if($done){Receive-Job $done|Out-Host}}
$jobs|Where-Object State -ne Running|ForEach-Object{Receive-Job $_ -ErrorAction SilentlyContinue|Out-Host;Remove-Job $_ -Force}
"Completed CLI judge batches."
