<#
.SYNOPSIS
  Repository hygiene check.
.DESCRIPTION
  Fails when a tracked text file or a commit message contains a forbidden
  character (em dash, en dash) or a forbidden term.
  Run from the repository root:
    powershell -ExecutionPolicy Bypass -File scripts\check-repo.ps1
#>

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

$emDash = [string][char]0x2014
$enDash = [string][char]0x2013
# Built at runtime so the term never appears literally in this repository.
$term = 'GD' + 'IZ'

$binary = '\.(png|jpe?g|gif|ico|pdf|mp4|zip|zap\d+)$'
$problems = New-Object System.Collections.Generic.List[string]

foreach ($file in (git -c core.quotepath=false ls-files)) {
    if ($file -match $binary) { continue }
    if (-not (Test-Path -LiteralPath $file -PathType Leaf)) { continue }
    $text = Get-Content -LiteralPath $file -Raw -Encoding UTF8
    if ([string]::IsNullOrEmpty($text)) { continue }
    if ($text.Contains($emDash)) { $problems.Add("${file}: em dash") }
    if ($text.Contains($enDash)) { $problems.Add("${file}: en dash") }
    if ($text -match [regex]::Escape($term)) { $problems.Add("${file}: forbidden term") }
}

$history = (git log --all --format='%H %B') -join "`n"
if ($history.Contains($emDash) -or $history.Contains($enDash)) {
    $problems.Add('commit history: dash found in a commit message')
}
if ($history -match [regex]::Escape($term)) {
    $problems.Add('commit history: forbidden term found in a commit message')
}

if ($problems.Count -gt 0) {
    Write-Host 'Repository check FAILED:' -ForegroundColor Red
    $problems | ForEach-Object { Write-Host "  $_" }
    exit 1
}
Write-Host 'Repository check passed.' -ForegroundColor Green