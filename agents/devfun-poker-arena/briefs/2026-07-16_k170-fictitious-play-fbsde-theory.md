---
title: K170 — fictitious-play FBSDE convergence (theory steal)
type: brief
target: Poker Arena
created: 2026-07-16
updated: 2026-07-16
---

## Target

`agents/devfun-poker-arena/` — MAFP / fictitious-play chart bake track.

## Summary

arXiv 2607.08861: first convergence analysis of fictitious play for fully coupled FBSDEs in finite-player stochastic differential games (geometric → super-exponential under structure). Theory shelf for MAFP — do not port FBSDE numerics onto Arena clock.

## Body

### P0

1. Cite as theoretical backing that FP iteration can converge even when coupled — supports continuing MAFP chart bake (solver-bake track).
2. Do **not** add online FBSDE solves to `decide()` hot path.

### Out of scope

- Tumor phylogenetics, Shor/Lean, handwriting attacks

## Sources

- wiki/sources/arxiv-2607.08861-fictitious-play-fbsde-stochastic-games-2026-07-16.md
