---
title: K157 — FBSDE fictitious-play theory shelf (poker)
type: brief
target: Poker Arena
created: 2026-07-16
updated: 2026-07-16
---

**Shelf (done)** — folded into `references/mafp-fbsde-theory-shelf.md` (K170 + K157). Do not re-implement; do not import continuous-time rates into MAFP loop budgets.

## Target

`agents/devfun-poker-arena/` — MAFP / fictitious-play literature shelf only.

## Summary

arXiv 2607.08861 proves geometric (sometimes super-exponential) convergence of fictitious play for fully coupled continuous-time Nash FBSDE systems. **Shelf only** — do not change discrete MAFP / HL iteration budgets from these rates.

## Body

### Do

- Link under MAFP reading list as continuous-time FP theory advance (Han–Hu–Long extension).

### Do not

- Import geometric rates into sandbox self-play / MAFP loop schedules
- Attempt deep FBSDE solvers for Arena decide()
- Prod scp / FOSS adopt (none)

## Sources

- arXiv 2607.08861
- `@gambling-wiki/sources/arxiv-2607.08861-fictitious-play-coupled-fbsde-2026-07-16.md`
- `@gambling-wiki/sources/arxiv-2606.19308-mafp-multi-agent-fictitious-play-2026-06-21.md`
