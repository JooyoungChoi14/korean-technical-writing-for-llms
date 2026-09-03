param(
    [string]$Model='kimi-k3',
    [Parameter(Mandatory=$true)][string]$OutputRoot,
    [ValidateRange(1,60)][int]$ChunkSize=20,
    [ValidateRange(0,5)][int]$RetryCount=2,
    [switch]$SkipFinished
)
$ErrorActionPreference='Stop'
$repoRoot=Split-Path -Parent $PSScriptRoot;$experimentRoot=Join-Path $repoRoot 'evals\reader-reconstruction-v6';$batchRoot=Join-Path $experimentRoot 'batches\ollama-kimi-k3'
$schemaText=Get-Content (Join-Path $experimentRoot 'judge-output-schema.json') -Raw -Encoding UTF8
$secretPath=Join-Path $env:USERPROFILE '.codex\secrets\ollama-cloud-api-key.txt';$token=$env:OLLAMA_API_KEY
if([string]::IsNullOrWhiteSpace($token) -and (Test-Path -LiteralPath $secretPath)){$token=(Get-Content $secretPath -Raw -Encoding UTF8).Trim()}
if([string]::IsNullOrWhiteSpace($token)){throw 'Ollama Cloud API 키를 찾지 못했습니다.'}
if(-not [IO.Path]::IsPathRooted($OutputRoot)){$OutputRoot=Join-Path $repoRoot $OutputRoot};$OutputRoot=[IO.Path]::GetFullPath($OutputRoot)
$dir=Join-Path $OutputRoot 'ollama-kimi-k3';New-Item -ItemType Directory -Path $dir -Force|Out-Null
$instructions='문장 선호도가 아니라 명시적 의미 포함 여부만 판정하는 평가자입니다. revision 문장 자체가 proposition을 직접 진술하거나 모호하지 않게 바꾸어 말했을 때만 true로 판정하세요. 명제 목록을 단서로 빠진 내용을 추론하거나 보충하지 마세요. actor_and_action_explicit는 문장만으로 주체와 핵심 동작을 둘 다 알 수 있을 때만 true입니다. JSON 객체 외에는 출력하지 마세요.'
foreach($batch in Get-ChildItem $batchRoot -Filter 'batch-*.json'|Sort-Object Name){
  $batchPayload=Get-Content $batch.FullName -Raw -Encoding UTF8|ConvertFrom-Json
  for($startIndex=0;$startIndex -lt $batchPayload.items.Count;$startIndex+=$ChunkSize){
    $part=1+[Math]::Floor($startIndex/$ChunkSize);$partItems=@($batchPayload.items|Select-Object -Skip $startIndex -First $ChunkSize)
    $chunkPayload=[ordered]@{judge=$batchPayload.judge;items=$partItems}|ConvertTo-Json -Depth 12
    $base="$([IO.Path]::GetFileNameWithoutExtension($batch.Name))-part-$('{0:D2}' -f $part)";$out=Join-Path $dir "$base.output.json";$meta=Join-Path $dir "$base.meta.json"
    if($SkipFinished -and (Test-Path -LiteralPath $meta)){if((Get-Content $meta -Raw -Encoding UTF8|ConvertFrom-Json).transport_status -eq 'completed'){continue}}
    $prompt="입력의 모든 item_id와 proposition id를 빠짐없이 한 번씩 반환하세요. 반드시 아래 JSON Schema와 일치하는 JSON 객체 하나만 출력하세요.`n`n[JSON Schema]`n$schemaText`n`n[판정 대상]`n$chunkPayload"
    $start=[DateTimeOffset]::UtcNow;$record=[ordered]@{judge='ollama-kimi-k3';agent='ollama-cloud';model=$Model;batch_file=$batch.FullName;part=$part;item_count=$partItems.Count;started_at=$start.ToString('o');completed_at=$null;elapsed_seconds=$null;transport_status='failed';response_status=$null;usage=$null;error=$null;output=[IO.Path]::GetFileName($out)}
    try{
        $body=@{model=$Model;instructions=$instructions;input=$prompt;stream=$false;temperature=0;max_output_tokens=20000;truncation='disabled'}|ConvertTo-Json -Depth 16
        $response=$null;foreach($attempt in 0..$RetryCount){try{$response=Invoke-RestMethod -Method Post -Uri 'https://ollama.com/v1/responses' -Headers @{Authorization="Bearer $token"} -ContentType 'application/json; charset=utf-8' -Body ([Text.Encoding]::UTF8.GetBytes($body)) -TimeoutSec 900;break}catch{if($_.Exception.Message -notmatch '429' -or $attempt -ge $RetryCount){throw};Start-Sleep -Seconds (15*($attempt+1))}}
        $record.response_status=$response.status;$record.usage=$response.usage
        $parts=foreach($item in $response.output){foreach($content in $item.content){if($content.type -eq 'output_text'){$content.text}}};$text=($parts -join "`n").Trim();if($text.StartsWith('```json')){$text=$text.Substring(7)}elseif($text.StartsWith('```')){$text=$text.Substring(3)};if($text.EndsWith('```')){$text=$text.Substring(0,$text.Length-3)};Set-Content $out $text.Trim() -Encoding UTF8
        $parsed=Get-Content $out -Raw -Encoding UTF8|ConvertFrom-Json;if($null -eq $parsed.judgments){throw 'judgments 배열이 없습니다.'};if(@($parsed.judgments).Count -ne $partItems.Count){throw "judgments 수가 입력 항목 수와 다릅니다: $(@($parsed.judgments).Count)/$($partItems.Count)"};$record.transport_status='completed'
    }catch{$record.error=$_.Exception.Message -replace 'Bearer\s+\S+','Bearer [REDACTED]'}
    finally{$end=[DateTimeOffset]::UtcNow;$record.completed_at=$end.ToString('o');$record.elapsed_seconds=[Math]::Round(($end-$start).TotalSeconds,3);$record|ConvertTo-Json -Depth 12|Set-Content $meta -Encoding UTF8;[pscustomobject]@{judge='ollama-kimi-k3';batch=$batch.Name;status=$record.transport_status;seconds=$record.elapsed_seconds}|Format-Table -AutoSize}
  }
}
"Completed Ollama judge batches."
