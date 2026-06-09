---
title: Open-spot preflop detection audit
type: brief
tags: [poker, preflop, pfr, bug, k107]
created: 2026-06-09
status: FIXED — is_preflop_open_spot() in opponent_target + cemini_decide routing
---

## Target

Operator — **devfun-poker-arena** `examples/cemini_decide.py`

## Summary

External report (@3d64r_89): `call_chips == 0` misclassifies non-blind first-to-act opens → limp path → **PFR 6% / VPIP 23%**. Use **`current_bet <= big_blind`** for open spots.

## Body

### Repro logic

| Spot | call_chips | current_bet | Old branch | Correct |
|------|------------|-------------|------------|---------|
| UTG open | BB | BB | vs_bet (limp) | open raise |
| Unraised pot | 0 | 0 | open | open |

### Fix (shipped)

`examples/opponent_target.py`: `is_preflop_open_spot()` — blinds-only pot (`pot <= sb+bb+2`, `max_bet <= bb`) or `call_chips==0`; excludes vs-raise and multiway limp (`btn_q9o_vs_limp` pot=70).

`examples/cemini_decide.py`: preflop routing + EP trash / lane_tight open guards use `is_preflop_open_spot(table, allowed, call_chips)` instead of `call_chips == 0`.

Regression: `prod_aa_utg_open_spot` — AA UTG first-in must `bet`.

### Validation

1. `uv run pytest tests/ -q`
2. Selfplay 500 hands — log VPIP/PFR; gap should shrink toward ≤8pp
3. Cross-check with tournament super-audit VPIP 10–16% target

## Sources

- OSINT K107 Post 16 via @briefs/2026-06-09_k107-gambling-poker-open-spot-from-osint.md
