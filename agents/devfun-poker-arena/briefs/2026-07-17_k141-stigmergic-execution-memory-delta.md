---
title: K141 — stigmergic execution memory delta (poker sandbox)
type: brief
target: Poker Arena
created: 2026-07-17
updated: 2026-07-17
---

## Target

`agents/devfun-poker-arena/` — HL analyst loop / Researcher Round HU sandbox.

## Summary

Thin steal from **SGM** (arXiv 2607.15182): decaying **environment** memory that ranks which candidate goals enter the planner. Mirror for poker: recent execution traces on spot-classes should bias which drills / decide() candidates enter the next HL epoch — not only how you play after the spot is chosen.

Complements shipped K161 hierarchical memory + DeepSearch trajectory filter (do not re-implement).

## Body

### P0 — spot-class stigmergy (advisory)

Maintain a bounded decaying score per spot class (e.g. BTN vs BB river, 3bet pots):

| Channel | Update on |
|---------|-----------|
| `pressure` | Recent losses / veto fails in class |
| `completion` | Recent wins / clean folds that matched plan |
| `block` | Spots that caused planner/HL thrash |

Decay each epoch: `M ← ρM + Δ`. Prefer high-pressure / high-block classes when shortlisting the next regression unit **before** writing a full HL brief.

### P1 — goal instantiation vs play

SGM's lesson: shape **which** goals enter the planner. For arena:

1. Filter eligible failure units (K161 DeepSearch tags)
2. **Then** rank by stigmergic spot-class scores
3. Only then expand scaffold / GenomeDiff brief

### Out of scope

- Warehouse MAPF / PBS code
- TipDrop / David
- Prod scp

### Operator checklist

- [ ] Add optional `stigmergy_spot_scores` JSON (cap + ρ) next to hierarchical memory config
- [ ] Rank K161-eligible units by score before mix
- [ ] Keep advisory — no hard submit gate

## Sources

- arXiv [2607.15182](https://arxiv.org/abs/2607.15182)
- `briefs/2026-07-13_k161-hierarchical-memory-deepsearch-steal.md`
- SEO: `@seo-wiki/sources/arxiv-dutta-2026-stigmergic-graph-memory-mapd-2607.15182-2026-07-17.md`
