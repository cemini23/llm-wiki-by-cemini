## Target

`agents/devfun-poker-arena/` — Poker Arena operator brief (2026-07-21_super-audit-hard-policy.md).

# Super-audit — texas_solver hard policy ship

READONLY. Do not edit code. Report only.


## Summary

Operator brief: 2026-07-21 super-audit-hard-policy. `agents/devfun-poker-arena/` — Poker Arena operator brief (2026-07-21_super-audit-hard-policy.md).

## Regime disclosure

Comparisons in this brief are **single-regime** (HU Researcher sandbox and/or 6-max Playground chip-qual only). Not a multi-regime leaderboard claim; no free cross-regime superiority asserted.
## Mission
Review whether Active `bf18eac0` (`CEMINI_SOLVER_HARD=1` sampling texas_solver_v1 bake mix) is a sound competitive step vs soft-bias, and list blocking bugs before we claim ladder progress.

## Context
- Prior Active e3574bb4 soft-bias μ≈−37.6 @8.2k rank~204
- Fable: tops play σ from blueprint; we previously only soft-biased equity bars
- Densify to 90 spots deferred (TexasSolver hang on new boards)
- Engine cemini; no gin/DeepCFR/opponent-modes

## Required output format
```
VERDICT: SHIP | REWORK | REJECT
BLOCKERS: (bullets or none)
RISKS: (bullets)
PATCH BACKLOG: (ordered, if any)
ONE-LINE SUMMARY:
```

## Focus
1. Flag-off soft path identity
2. Hard sample fail-open when freqs empty/illegal
3. Facing-bet path: overcommit guard before hard sample — correct?
4. Will hard sampling on 90 coarse keys OOS like DeepCFR-lite?
5. What must densify before μ can exit bottom third?

## Sources

- Internal Arena ops briefs / escalate packages in `agents/devfun-poker-arena/briefs/`
- Related references under `agents/devfun-poker-arena/references/`
