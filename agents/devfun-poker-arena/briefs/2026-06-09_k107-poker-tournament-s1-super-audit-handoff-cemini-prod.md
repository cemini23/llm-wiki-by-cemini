---
title: K107 poker — Tournament S1 super audit handoff
type: brief
target: CeminiSuite / devfun-poker-arena prod
created: 2026-06-09
updated: 2026-06-09
tags: [poker, tournament, super-audit, k107]
---

## Target

**cemini-prod** poker arena lobby + operator — tournament S1 posture (shipped `4a6df45`).

## Summary

Super-audit recommended **`70f2527`** revert; **shipped:** lane-gate hybrid on **`4a6df45`** + tournament env + open-spot preflop fix. Eval-panel lane **−26.67** (lane_tight) is expected; tournament posture preflight **−9.37**. Target **VPIP 12–16%** rock band — not field LAG.

## Body

### Canonical doc

`agents/devfun-poker-arena/briefs/2026-06-09_tournament-s1-super-audit-synthesis.md`

Pack: `agents/devfun-poker-arena/reports/gap-audit/pack-tournament-s1`

### Current prod settings

| Item | Setting |
|------|---------|
| Git (main) | `4a6df45` |
| AGENT_VERSION | `s1t.4a6df45.tournament-s1` |
| CEMINI_TOURNAMENT_MODE | 1 |
| CEMINI_EVAL_PANEL_GATE | 0 |
| JACKPOT_ROYAL_ENABLED | 0 |
| JACKPOT_27_HUNT_ENABLED | 0 |
| CEMINI_KO_SURVIVAL | 1; HANDS=60 |
| Open-spot routing | `is_preflop_open_spot()` — fixed (not `call_chips==0`) |
| Comp ID | `TOURNAMENT_COMP=cmp... ./scripts/s1_tournament_prod_apply.sh` when bracket live |

### Open-spot audit (K107 Post 16)

**Fixed** — see `briefs/2026-06-09_open-spot-pfr-preflop-audit.md`. Regression: `prod_aa_utg_open_spot`.

### Do not

- Checkout raw `70f2527` decide (nuts regression + wrong baseline for current guards)
- Chase eval-panel −17.45 on tournament comp (eval_panel uses lane_tight)
- Deploy from S2 oracle comp (S1 primary only)

## Sources

- @agents/devfun-poker-arena/briefs/2026-06-09_tournament-s1-super-audit-synthesis.md
- @agents/devfun-poker-arena/briefs/2026-06-09_open-spot-pfr-preflop-audit.md
