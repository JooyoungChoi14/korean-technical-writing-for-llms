param(
    [Parameter(Mandatory = $true)]
    [string]$ExperimentRoot,

    [Parameter(Mandatory = $true)]
    [string]$OutputPath
)

$ErrorActionPreference = 'Stop'
$variants = @('baseline', 'self-check', 'counterexample', 'cross-boundary', 'task-specific')
$variantSummary = [ordered]@{}
$modelMap = [ordered]@{}

foreach ($variant in $variants) {
    $variantRoot = Join-Path $ExperimentRoot $variant
    $judgmentPath = Join-Path $ExperimentRoot ("{0}-judgment.json" -f $variant)
    $records = Get-ChildItem -LiteralPath $variantRoot -Filter 'run-*.json' -Recurse | ForEach-Object {
        Get-Content -LiteralPath $_.FullName -Raw -Encoding UTF8 | ConvertFrom-Json
    }
    $judgments = (Get-Content -LiteralPath $judgmentPath -Raw -Encoding UTF8 | ConvertFrom-Json).runs
    $elapsed = @($records.elapsed_seconds | Sort-Object)
    $median = if ($elapsed.Count) { $elapsed[[Math]::Floor($elapsed.Count / 2)] } else { $null }

    $variantSummary[$variant] = [ordered]@{
        total = $records.Count
        completed = @($records | Where-Object status -eq 'completed').Count
        empty = @($records | Where-Object status -eq 'empty').Count
        passed = @($judgments | Where-Object passed_count -eq 3).Count
        failed = @($judgments | Where-Object { $null -ne $_.c1 -and $_.passed_count -lt 3 }).Count
        median_elapsed_seconds = $median
        input_tokens = ($records | ForEach-Object { if ($_.usage) { [long]$_.usage.input_tokens } } | Measure-Object -Sum).Sum
        output_tokens = ($records | ForEach-Object { if ($_.usage) { [long]$_.usage.output_tokens } } | Measure-Object -Sum).Sum
    }

    foreach ($group in ($judgments | Group-Object model)) {
        if (-not $modelMap.Contains($group.Name)) {
            $modelMap[$group.Name] = [ordered]@{
                model = $group.Name
                variants = [ordered]@{}
            }
        }
        $modelRecords = @($records | Where-Object {
            ($_.model -replace '[:/]', '-') -eq $group.Name
        })
        $modelMap[$group.Name].variants[$variant] = [ordered]@{
            passed = @($group.Group | Where-Object passed_count -eq 3).Count
            failed = @($group.Group | Where-Object { $null -ne $_.c1 -and $_.passed_count -lt 3 }).Count
            empty = @($group.Group | Where-Object { $null -eq $_.c1 }).Count
            median_elapsed_seconds = if ($modelRecords.Count) {
                (@($modelRecords.elapsed_seconds | Sort-Object))[[Math]::Floor($modelRecords.Count / 2)]
            }
            else {
                $null
            }
        }
    }
}

$summary = [ordered]@{
    date = '2026-09-02'
    design = [ordered]@{
        models = $modelMap.Count
        runs_per_model_per_variant = 3
        variants = $variants
        total_runs = [int](($variantSummary.GetEnumerator() | ForEach-Object {
            $_.Value.total
        } | Measure-Object -Sum).Sum)
        judge = 'Codex gpt-5.6-sol, reasoning effort high; representative pass and fail outputs manually checked'
        acceptance = '../../cli-smoke/expected.json'
    }
    variants = $variantSummary
    models = @($modelMap.Values)
}

$summary | ConvertTo-Json -Depth 12 | Set-Content -LiteralPath $OutputPath -Encoding UTF8
Write-Output ("Wrote {0}" -f $OutputPath)
