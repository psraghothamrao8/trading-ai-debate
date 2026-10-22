param(
  [Parameter(Mandatory)][string]$Question,
  [int]$Rounds = 3
)

$claudeExe = "$env:USERPROFILE\.local\bin\claude.exe"
$out = Join-Path $PSScriptRoot "debate-log.md"

function Ask-Claude($p) { (& $claudeExe -p $p) -join "`n" }
function Ask-Agy($p)    { (& agy -p $p --print-timeout 300s) -join "`n" }

$log = "# Question`n$Question`n"
$c = Ask-Claude "You are Claude. Answer concisely and take a clear position: $Question"
$log += "`n## Claude R1`n$c`n"

for ($i = 1; $i -le $Rounds; $i++) {
  $g = Ask-Agy "You are Gemini debating Claude. Do not edit any files. Transcript so far:`n$log`nCritique Claude's position, then give your recommendation. If you fully agree, include the word AGREE."
  $log += "`n## Gemini R$i`n$g`n"
  Write-Host "Gemini R$i done"
  if ($g -match "\bAGREE\b") { break }

  $c = Ask-Claude "You are Claude debating Gemini. Transcript so far:`n$log`nRespond to the critique and revise your position. If you fully agree, include the word AGREE."
  $log += "`n## Claude R$($i+1)`n$c`n"
  Write-Host "Claude R$($i+1) done"
  if ($c -match "\bAGREE\b") { break }
}

$final = Ask-Claude "Debate transcript:`n$log`nWrite the final decision: the choice, the reasons, and any unresolved disagreements."
$log += "`n## DECISION`n$final`n"
$log | Set-Content -Path $out -Encoding utf8
Write-Host "`n$final`n`nFull transcript: $out"
