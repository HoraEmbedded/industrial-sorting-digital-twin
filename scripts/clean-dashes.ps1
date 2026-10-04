<#
.SYNOPSIS
  Replaces em dashes and en dashes by a plain hyphen in the given files.
.EXAMPLE
  powershell -ExecutionPolicy Bypass -File scripts\clean-dashes.ps1 electrical\industrial-sorting-line.qet
#>
param(
    [Parameter(Mandatory = $true, ValueFromRemainingArguments = $true)]
    [string[]]$Path
)

$emDash = [string][char]0x2014
$enDash = [string][char]0x2013
$utf8 = New-Object System.Text.UTF8Encoding $false

foreach ($p in $Path) {
    $full = (Resolve-Path -LiteralPath $p).Path
    $text = [System.IO.File]::ReadAllText($full, $utf8)
    $clean = $text.Replace($emDash, '-').Replace($enDash, '-')
    if ($clean -ne $text) {
        [System.IO.File]::WriteAllText($full, $clean, $utf8)
        Write-Host "Cleaned: $p"
    } else {
        Write-Host "Nothing to clean: $p"
    }
}