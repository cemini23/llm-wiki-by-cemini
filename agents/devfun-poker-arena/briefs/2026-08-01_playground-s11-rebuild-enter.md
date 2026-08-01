---
title: Playground S11 enter — gin killed + short-stack rebuild
type: brief
tags: [brief, poker, playground, s11, postmortem]
created: 2026-08-01
target: agents/devfun-poker-arena
---

## Target

Leave Tournament S10 (busted / 250 MON rebuy). Enter Playground S11 chip-qual with a frozen control arm.

## Summary

Gin is hard-killed (`CEMINI_GIN_KILL=1`). Short-stack push/fold (<20bb) overrides chase. Rebuys capped at 2 and max 5 MON. Posture is Playground chip-qual TAG — not tournament chase.

## Changes

| Item | Action |
|------|--------|
| Gin / V008 / V2 | Killed at master switch |
| Short-stack | `examples/short_stack.py` push/fold |
| Rebuy | `CEMINI_MAX_REBUYS=2`, `CEMINI_REBUY_MAX_MON=5` |
| Chase margins | Mild only; off when short |
| S11 enter | `playground_chip_qual_enter.sh 11` |

## Do not

- Fund 250 MON T10 rebuy
- Set `CEMINI_GIN_KILL=0` without offline A/B proof
- Flip placement_chase on Playground

## Sources

- `briefs/2026-08-01_tournament-s10-postmortem.md`
- Prod journal T10 bust sequence
