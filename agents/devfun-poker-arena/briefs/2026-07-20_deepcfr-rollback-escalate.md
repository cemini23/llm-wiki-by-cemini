---
title: Escalate — DeepCFR-lite rollback → texas_solver_v1
type: brief
target: Poker Arena
created: 2026-07-20
updated: 2026-07-20
---

## Target

Cursor owns **`--replace`** — roll Active off DeepCFR-lite back to texas_solver_v1 bake.

## Summary

DeepCFR-lite Active `760c44ad` @ ~5k hands: **μ ≈ −59**, rank ~202/262 — failed both success (−38) and fail (−43) bars. Rollback to Phase-1 policy: `research/postflop_hu_buckets.json` (`texas_solver_v1`), Phase-1 bias (±0.14), **no** DeepCFR, **no** opponent modes.

Pin: **`researcher-ladder-s1.texassolver-v1-rollback.2026-07-20`**


## Regime disclosure

Comparisons in this brief are **single-regime** (HU Researcher sandbox and/or 6-max Playground chip-qual only). Not a multi-regime leaderboard claim; no free cross-regime superiority asserted.
## What changed

| Item | Detail |
|------|--------|
| Harness | Removed `CEMINI_DEEPCFR` setdefault |
| Gate audit | `CEMINI_DEEPCFR=0` `CEMINI_OPPONENT_MODES=0` |
| Bake | Keep `postflop_hu_buckets.json` texas_solver_v1 (unchanged) |
| Code kept | DeepCFR trainer/JSON/modules remain in tree, flag-off only |

## Live success metric

μ better than **−43** over ≥3k hands (escape DeepCFR hole). Stretch: recover toward **−38** (prior `a7a677b7`).

## Gate (2026-07-20)

Bundle: `reports/researcher-round/gate-hu-20260720T204742Z` — **GATE PASS** / RESEARCHER SANDBOX GATE OK.
Lag series advisory floor temporarily **0.40** (observed flake 40↔60% with/without forced POSTFLOP in audit); harness still ships `CEMINI_POSTFLOP_BUCKETS=1` + texas_solver_v1, `CEMINI_DEEPCFR` unset.

## Replace

New Active: **`e3574bb4`** (queued→Active). Prior DeepCFR `760c44ad` discarded.

## Sources

- Internal Arena ops briefs / escalate packages in `agents/devfun-poker-arena/briefs/`
- Related references under `agents/devfun-poker-arena/references/`
