## Target

`agents/devfun-poker-arena/` — Poker Arena operator brief (2026-07-21_k199-k201-solver-prune-steal.md).

# CCC→Poker K199/K201 — solver-grounded numbers + tool-dump prune

**From:** CCC ingest 2607.18147 + 2607.18213
**For:** devfun-poker-arena agents / review bots


## Summary

Operator brief: 2026-07-21 k199-k201-solver-prune-steal. `agents/devfun-poker-arena/` — Poker Arena operator brief (2026-07-21_k199-k201-solver-prune-steal.md).

## Regime disclosure

Comparisons in this brief are **single-regime** (HU Researcher sandbox and/or 6-max Playground chip-qual only). Not a multi-regime leaderboard claim; no free cross-regime superiority asserted.
## Steal

1. **Solver-grounded:** EV, pot odds, solver outputs — report only from trusted tool; LLM narrates, does not invent numbers.
2. **Tool dumps:** cap/summarize verbose tool output in long multi-hand threads (K115 N/W for closed models); don't re-feed full solver logs every turn.
3. No swe-pruner-pro install (no SPDX); open-weight internal-prune is WATCH only.

## Why poker

Sparse terminal PnL + fat tool traces = classic invent-numbers + context-bloat failure modes.

## Sources

- Internal Arena ops briefs / escalate packages in `agents/devfun-poker-arena/briefs/`
- Related references under `agents/devfun-poker-arena/references/`
