---
title: Playground S11 TAG widen (no gin)
type: brief
created: 2026-08-02
updated: 2026-08-02
target: agents/devfun-poker-arena
---

## Target

Raise VPIP/PFR toward halloran-class TAG (~20–26% / ~10–12%) on Playground S11 without re-enabling gin.

## Summary

v1 fixed permanent KO survival (min stack 1500) but VPIP stayed ~8% — BB/SB broadway auto-folds and chart raise→fold killed defends (KQo/AJo folded). v2: steal-sized TAG BB/SB defend before those guards; stronger margins; MP/CO open extras. Gin still hard-killed.

## Regime disclosure

Comparisons in this brief are **single-regime** (HU Researcher sandbox and/or 6-max Playground chip-qual only). Not a multi-regime leaderboard claim; no free cross-regime superiority asserted.

## Changes

| Knob | Value |
|------|--------|
| `CEMINI_TAG_WIDEN` | 1 |
| `CEMINI_KO_SURVIVAL_MIN_STACK` | 700 |
| `CEMINI_KO_SURVIVAL_HANDS` | 40 |
| `CEMINI_COLD_START_NO_STEAL` | 0 |
| Gin | still killed |

## Do not

- Set `CEMINI_GIN_KILL=0`
- Widen under short-stack / qual protect

## Sources

- Live S11 stats (~9–11% VPIP nit)
- `examples/tag_widen.py`
