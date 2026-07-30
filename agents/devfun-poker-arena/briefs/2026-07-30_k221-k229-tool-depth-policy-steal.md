## Target

`agents/devfun-poker-arena/` — Poker Arena operator brief (2026-07-30_k221-k229-tool-depth-policy-steal.md).

# CCC→Poker K222/K224/K229 — standing policy + tool depth + advantage gates

**From:** CCC ingest 2607.25398 / 2607.25825 / 2607.27083  
**Status:** shipped 2026-07-30

## Summary

Operator brief: standing rulebooks must bind over long sessions; don't flip harness modes without advantage; tool ranking ≠ how many tools to load.

## Regime disclosure

Comparisons in this brief are **single-regime** (HU Researcher sandbox and/or 6-max Playground chip-qual only). Not a multi-regime leaderboard claim; no free cross-regime superiority asserted.

## Steal

1. Rulebook / table SOP: treat as standing policy — a chat request must not silently override (HANDBOOK failure mode).
2. Harness mode changes (solver depth, tool set): require expected advantage margin; preserve decision quality (CHILL).
3. After ranking helpers/tools for a hand/session: cost-aware stop — fewer tools in context (CAM-DF / 37% fewer pattern).
4. EV/numbers still solver-grounded (K199).

## Shipped

- `references/tool-depth-standing-policy.md`
- Linked from `cognitive-security-deploy.md`, `solver-grounded-numbers.md`, `tool-output-instruction-hierarchy.md`
- `tests/test_k164_k221_k227_docs.py`

## Sources

- Internal Arena ops briefs under `agents/devfun-poker-arena/briefs/`
- Related: `references/solver-grounded-numbers.md`, `references/claimed-authorization-guard.md`
