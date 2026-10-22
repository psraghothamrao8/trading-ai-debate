# trading-ai-debate

Scripts that make Claude Code and Gemini (Antigravity `agy`) debate intraday short-only strategy ideas for Indian equities (NSE), then converge on a final, audited report.

- `debate.ps1` - simple N-round two-model debate with a final decision.
- `discover.ps1` - multi-phase pipeline: idea generation -> cull -> deep analysis -> converge -> final report -> adversarial audit -> revision.
- `seed_ideas.md` - first batch of ~40 ideas used to seed the pipeline.
- `runs/<timestamp>/` - outputs of a run. `6_AUDITED_FINAL.md` is the final report.

**Nothing here is backtested or proven.** AI conviction is not evidence of profitability. This is research, not financial advice.
