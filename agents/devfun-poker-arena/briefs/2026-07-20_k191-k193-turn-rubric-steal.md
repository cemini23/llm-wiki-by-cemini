# CCC→Poker K191/K193 — turn scores + expert rubrics

**From:** CCC ingest 2607.15660 + 2607.16057
**For:** devfun-poker-arena agents / review writeups

## Target

Poker arena — long-horizon decide chains and strategy QA


## Summary

Operator brief: 2026-07-20 k191-k193-turn-rubric-steal. **From:** CCC ingest 2607.15660 + 2607.16057

## Regime disclosure

Comparisons in this brief are **single-regime** (HU Researcher sandbox and/or 6-max Playground chip-qual only). Not a multi-regime leaderboard claim; no free cross-regime superiority asserted.
## Steal

1. **Turn-aware scoring:** log per-hand / per-street success signals, not only session PnL, when diagnosing agent trajectories (ToolVerse credit-assignment steal — pattern only).
2. **Dependency unlock:** treat memory → opponent model → solver tool as an unlock graph for multi-step evals.
3. **Rubric-from-expert:** when LLM judges strategy writeups, explode a solver/expert reference into checklist criteria; report partial vs all-criteria; human-gate money decisions.
4. No ToolVerse / BusinessCaseBench installs — methodology only.

## Why poker

Multi-street decisions are long-horizon with sparse terminal reward — same failure mode the paper attacks. Subjective “good play” writeups need expert-anchored rubrics, not vibe judges.

## Sources

- Internal Arena ops briefs / escalate packages in `agents/devfun-poker-arena/briefs/`
- Related references under `agents/devfun-poker-arena/references/`
