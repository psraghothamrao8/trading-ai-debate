param(
  [string]$SeedFile = "",
  [int]$DivergeTurns = 8,   # each turn = one model adds ~6-7 ideas (alternating Claude / Gemini) -> ~40 ideas
  [int]$CullRounds   = 2,
  [int]$ConvergeRounds = 2
)

$claudeExe = "$env:USERPROFILE\.local\bin\claude.exe"
$run = Join-Path $PSScriptRoot ("runs\" + (Get-Date -Format "yyyyMMdd-HHmmss"))
New-Item -ItemType Directory -Force $run | Out-Null
Set-Location $run

$MaxArg = 100000000   # long prompts go to Gemini via file now, so no compression is needed

# Claude: high by default, xhigh ("extra") only for the key analysis/final steps. Gemini: high (its max available level).
function Ask-Claude($p, $effort = "high") { ($p | & $claudeExe -p --effort $effort) -join "`n" }

function Ask-Agy($p) {
  # Long prompts go through a file Gemini reads in full (needs read_file rule for this folder in ~\.gemini\config\config.json)
  if ($p.Length -gt 12000) {
    $f = Join-Path $run ("prompt_" + [guid]::NewGuid().ToString('N').Substring(0,6) + ".txt")
    Set-Content -Path $f -Value $p -Encoding utf8
    $p = "Use your built-in file reading/viewing tool (NOT a shell command) to open $f and read it to the very end, then follow the instructions in it exactly. Reply with text only. Do not create or edit any files."
  }
  $arg = $p -replace '"', '\"'   # PowerShell 5.1 does not escape embedded quotes for native exes
  for ($try = 1; $try -le 2; $try++) {
    $out = (& agy -p $arg --effort high --print-timeout 1800s) -join "`n"
    if ($out.Trim().Length -gt 200) { return $out }
    Write-Host "  agy returned too little ($($out.Length) chars), try $try"
  }
  throw "agy returned no usable output: $out"
}

# Shrink a long text with Claude so it fits inside agy's argument limit
function Squash($text, $max) {
  if ($text.Length -le $max) { return $text }
  Write-Host "  (compressing $($text.Length) -> ~$max chars for Gemini)"
  Ask-Claude "Compress the text below to at most $max characters. Keep every idea ID (like C3, G5), each idea's core mechanism, every score/conviction rating, and every substantive argument or objection. Drop filler. Output only the compressed text.`n`n$text"
}

# Build a Gemini prompt: fixed head + (possibly squashed) bulky sections
function Gem($head, [string[]]$bulk, $tail) {
  $room = $MaxArg - $head.Length - $tail.Length - 200
  $each = [math]::Max(3000, [int]($room / [math]::Max(1, $bulk.Count)))
  $body = ($bulk | ForEach-Object { Squash $_ $each }) -join "`n`n"
  "$head`n`n$body`n`n$tail"
}

$context = @"
CONTEXT:
- Market: Indian equities (NSE), INTRADAY ONLY, SHORT SELLING ONLY (cash-segment MIS shorts or futures shorts). Flat by ~15:15 IST. Hours 09:15-15:30 IST.
- Must be a rules-based algorithm that can run every trading day, unattended.
- Real costs: brokerage, STT on the sell side, exchange charges, GST, SEBI fees, slippage. A short-only book fights the market's upward drift, so edges must come from intraday structure, not from 'stocks go down'.
- DAILY OPERATION: the strategy must generate tradable signals on most trading days (not only on rare event days), so it can run every day and be validated on a large sample. Event-driven ideas are fine only if the event recurs frequently (e.g. daily/weekly flows, expiries, every-session patterns).
- Retail-scale capital. Data available: 1-minute OHLCV for NSE stocks, previous-day data, optionally index/option-chain data and news timestamps.

THE BAR (this is the whole point):
- GROUND-BREAKING. Aim for ideas that would make an experienced quant say 'huh, that's actually clever, why isn't everyone doing it?'. Anything found in a retail trading book or a YouTube strategy video is REJECTED: gap fade, VWAP rejection, RSI overbought, simple breakdowns, moving-average crosses, supertrend, standard pivot rules.
- Every idea needs a NON-OBVIOUS MECHANISM: name who is forced or predictably wrong on the other side of the trade (forced sellers/buyers, stop clusters, hedgers, auction/expiry mechanics, circuit-limit psychology, index rebalancing flows, order-book vacuums, cross-stock lead-lag, etc.) and WHY they cannot stop being wrong.
- THEME: take money from institutions, big operators, prop desks and HFT/algo firms that exploit Indian retail. Find where they are predictable, forced, or exploitable, and short against them. Think freely and originally; do not limit yourself to any list.
- Ideas must be genuine trades placed with ordinary orders (no deceptive or fake orders).
- Be honest about novelty: if it is a variant of something known, say so. 'Never tried before' is unverified.
- CONVICTION: you are not a neutral committee. Back only ideas you personally BELIEVE in and would be excited to see tested first. Rate each idea with CONVICTION 1-5 (5 = 'I would bet my own time on this'). Weak ideas you don't believe in should not be listed.
- Nothing is guaranteed profitable. Everything must be falsifiable by backtest.
"@

$fmt = "IDEA FORMAT (max 70 words each, numbered with your prefix): Name | Mechanism: who is on the other side and why they lose | Entry | Exit/stop | Data needed | Main failure mode | Known-variant? | CONVICTION n/5"

# ---------- PHASE 1: DIVERGE ----------
$ideas = ""
if ($SeedFile -and (Test-Path $SeedFile)) { $ideas = Get-Content $SeedFile -Raw }
for ($t = 1; $t -le $DivergeTurns; $t++) {
  $isClaude = ($t % 2 -eq 1)
  $who = if ($isClaude) { "C" } else { "G" }
  $head = "$context`n`nYou are collaborating with another AI to invent intraday SHORT-ONLY strategies for NSE. Add 6-7 NEW, genuinely original ideas not duplicating the list below. Only include ideas you have high conviction in. THINK DEEPLY before answering: for each candidate, mentally simulate the counterparty's behaviour, check the cost math (expected gross move per trade must clearly exceed the round-trip cost), consider how the edge would decay once known, and DISCARD anything that fails; only list ideas that survive your own scrutiny.`n$fmt`nUse prefix $who (${who}1, ${who}2...) continuing your numbering after the HIGHEST existing number for your prefix in the list (if none, start at 1)."
  Write-Host "Diverge turn $t/$DivergeTurns ($who)..."
  if ($isClaude) { $r = Ask-Claude "$head`n`nEXISTING IDEAS:`n$ideas" }
  else { $r = Ask-Agy (Gem $head @("EXISTING IDEAS:`n$ideas") "") }
  $ideas += "`n$r`n"
  Set-Content -Path "1_ideas.md" -Value $ideas -Encoding utf8
}

# ---------- PHASE 2: CULL ----------
$cull = ""
for ($r = 1; $r -le $CullRounds; $r++) {
  foreach ($who in "Gemini","Claude") {
    $head = "$context`n`nBelow is a pool of candidate strategies. Cull ruthlessly. Score EVERY idea 1-5 on: edge plausibility, testability with the data above, survival after Indian costs+slippage, novelty. Then CHAMPION the 3 ideas you personally believe in most and explain in 3-4 sentences each why you feel they will work (be specific about the mechanism). Name your TOP 10, kill the rest with one line each. Disagree with the other AI where it is wrong; merge or upgrade ideas where that makes them stronger and more original."
    Write-Host "Cull round $r ($who)..."
    if ($who -eq "Claude") { $resp = Ask-Claude "$head`n`nIDEAS:`n$ideas`n`nDISCUSSION SO FAR:`n$cull" }
    else { $resp = Ask-Agy (Gem $head @("IDEAS:`n$ideas", "DISCUSSION SO FAR:`n$cull") "") }
    $cull += "`n### $who (cull round $r)`n$resp`n"
    Set-Content -Path "2_cull.md" -Value $cull -Encoding utf8
  }
}

$shortlist = Ask-Claude @"
$context

From the ideas and cull discussion below, produce the SHORTLIST of exactly 8 ideas. Prefer ideas BOTH AIs championed or rated highly; merge/upgrade where the discussion suggested. Max 90 words each in the idea format, with both AIs' conviction. Output only the list.

IDEAS:
$ideas

CULL DISCUSSION:
$cull
"@
Set-Content -Path "3_shortlist.md" -Value $shortlist -Encoding utf8

# ---------- PHASE 2b: DEEP ANALYSIS OF THE SHORTLIST ----------
$deep = ""
foreach ($who in "Claude","Gemini") {
  $head = "$context`n`nDEEP ANALYSIS. For EACH of the 8 shortlisted strategies below, do a rigorous quantitative analysis: (1) a precise falsifiable hypothesis; (2) exactly how to measure the signal from 1-minute OHLCV (and any extra public data) with formulas; (3) estimated number of trades per day and sample size needed to validate; (4) cost model: estimate round-trip cost for an Indian intraday short (STT on sell side, brokerage, exchange/GST/SEBI charges, slippage) and the BREAKEVEN gross edge per trade; (5) capacity and how fast the edge decays once crowded; (6) the single most likely reason it fails and a cheap test that would reveal that failure early; (7) one concrete improvement that makes it sharper or more original. Be specific and critical; if the other AI's analysis (if present) is wrong, say so and correct it. End with your ranking of the 8 and your conviction (1-5) for each."
  Write-Host "Deep analysis ($who)..."
  if ($who -eq "Claude") { $resp = Ask-Claude "$head`n`nSHORTLIST:`n$shortlist`n`nANALYSIS SO FAR:`n$deep" "xhigh" }
  else { $resp = Ask-Agy (Gem $head @("SHORTLIST:`n$shortlist", "ANALYSIS SO FAR:`n$deep") "") }
  $deep += "`n### $who deep analysis`n$resp`n"
  Set-Content -Path "3b_deep.md" -Value $deep -Encoding utf8
}

# ---------- PHASE 3: CONVERGE ----------
$conv = ""
for ($r = 1; $r -le $ConvergeRounds; $r++) {
  foreach ($who in "Claude","Gemini") {
    $head = "$context`n`nDebate toward the best 2-3 strategies to actually build and run daily. Finalists must be ones BOTH AIs are genuinely enthusiastic about (conviction 4+ from each); if you cannot get there, say who is unconvinced and why. Stress-test with concrete failure scenarios: circuit limits, expiry days, budget/RBI days, low-liquidity stocks, gap-up squeezes, short-eligibility, slippage in fast moves. You may modify or combine ideas to make them bolder. State clearly which 2-3 you back and how strongly you believe in each."
    Write-Host "Converge round $r ($who)..."
    if ($who -eq "Claude") { $resp = Ask-Claude "$head`n`nSHORTLIST:`n$shortlist`n`nDEEP ANALYSIS:`n$deep`n`nDISCUSSION SO FAR:`n$conv" "xhigh" }
    else { $resp = Ask-Agy (Gem $head @("SHORTLIST:`n$shortlist", "DEEP ANALYSIS:`n$deep", "DISCUSSION SO FAR:`n$conv") "") }
    $conv += "`n### $who (converge round $r)`n$resp`n"
    Set-Content -Path "4_converge.md" -Value $conv -Encoding utf8
  }
}

$final = Ask-Claude @"
$context

SHORTLIST:
$shortlist

DEEP ANALYSIS:
$deep

DEBATE:
$conv

Write the FINAL REPORT with the 2-3 chosen strategies. For each: the core insight in plain words (why it's original), exact rules (universe filter, entry trigger with time window, stop-loss, target/time exit, position sizing), who is on the other side and why they lose, Claude's and Gemini's conviction with their reasons, expected failure regimes, a precise BACKTEST PLAN (data, period, cost model, metrics, out-of-sample split, kill criteria such as 'abandon if net profit factor < 1.2 after costs'), and a paper-trading plan. Note remaining disagreements. State plainly that AI conviction is not evidence of profitability; only the backtest and paper trading are. No guarantees.
"@
Set-Content -Path "5_FINAL.md" -Value $final -Encoding utf8

# ---------- PHASE 4: INDEPENDENT AUDIT, THEN REVISION ----------
Write-Host "Audit (Gemini)..."
$audit = Ask-Agy ((@"
$context

You are an adversarial auditor. Below is a FINAL REPORT proposing intraday short-only NSE strategies. Try hard to break it: find logic holes, hidden look-ahead bias or survivorship bias in the backtest plan, cost-model errors, unrealistic fill assumptions, regimes where it loses badly, edge-decay risks, and anything vague that could not be coded unambiguously. For each strategy give: VERDICT (build / fix first / drop), the top 3 flaws, and exact fixes. Be specific and unsparing.

FINAL REPORT:
$final
"@))
Set-Content -Path "5b_audit.md" -Value $audit -Encoding utf8

Write-Host "Revision (Claude)..."
$revised = Ask-Claude @"
$context

Below are a FINAL REPORT and an adversarial AUDIT of it. Produce the AUDITED FINAL REPORT: keep strategies the audit supports, fix or drop those it breaks (explain each change in one line), make every rule unambiguous and codeable (exact formulas, time windows, thresholds with starting values and the range to test), and finish with a prioritized build order (which to backtest first and why) and the first week's concrete steps. Keep the plain statement that AI conviction is not evidence of profitability. No guarantees.

FINAL REPORT:
$final

AUDIT:
$audit
"@ "xhigh"
Set-Content -Path "6_AUDITED_FINAL.md" -Value $revised -Encoding utf8
Write-Host "`nDONE. See $run\6_AUDITED_FINAL.md"

