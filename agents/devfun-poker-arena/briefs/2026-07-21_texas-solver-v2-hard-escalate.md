## Target

`agents/devfun-poker-arena/` — Poker Arena operator brief (2026-07-21_texas-solver-v2-hard-escalate.md).

# Escalate — texas_solver_v2 hard


## Summary

Operator brief: 2026-07-21 texas-solver-v2-hard-escalate. `agents/devfun-poker-arena/` — Poker Arena operator brief (2026-07-21_texas-solver-v2-hard-escalate.md).

## Regime disclosure

Comparisons in this brief are **single-regime** (HU Researcher sandbox and/or 6-max Playground chip-qual only). Not a multi-regime leaderboard claim; no free cross-regime superiority asserted.
## Active

- Competition: `cmr3n8tft01nilecm1u5jlny7`
- Pin: `researcher-ladder-s1.texas-solver-v2-hard.2026-07-21`
- Gate: `gate-hu-20260721T134218Z` PASS (lag series **60%**)
- Replace: `e4fa997e-5cfb-4ee2-94c3-7e36ed99f134` (Queued → Running smoke → expect Continuous Active)
- Bundle SHA: `ec5d954b4e605c681230a03223171e839b5d08e2b0756c7a0664141e933ac790`

## What fixed densify

TexasSolver v0.2.0 **SIGABRT (exit 134)** on new boards with `thread_num≥8` + `use_isomorphism=1`.
Not a hang — a crash. Fix:

- Grid defaults: `thread_num=1`, `use_isomorphism=0`
- Bake: `run_solver_with_fallback` retries crash → 1/0
- Foreground presolve (background jobs were getting killed mid-solve)

## Policy

- `CEMINI_SOLVER_HARD=1` — sample σ from bake freqs
- Free: hard before Gin; Facing: after leak-fold library
- Engine: `cemini`

## Bars

| Bar | μ |
|-----|---|
| Success | better than **−37.6** @ ≥3k |
| Stretch | ≤ **−28** |
| Rollback | ≤ **−43** |

## Known residual

- `size_pot_frac` still ≈0.5 everywhere (single bet-size tree); action mix is the competitive lever this ship.

## Sources

- Internal Arena ops briefs / escalate packages in `agents/devfun-poker-arena/briefs/`
- Related references under `agents/devfun-poker-arena/references/`
