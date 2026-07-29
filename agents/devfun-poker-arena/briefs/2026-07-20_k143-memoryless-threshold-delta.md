---
title: K143 — memoryless threshold delta (poker sandbox)
type: brief
target: Poker Arena
created: 2026-07-20
updated: 2026-07-20
---

## Target

`agents/devfun-poker-arena/` — HL analyst loop / Researcher Round HU sandbox.

## Summary

Thin steal from the **memoryless best-choice** problem (arXiv 2607.16145): when the agent cannot retain relative-rank history (rejected offers erased), optimal policy collapses to **threshold strategies** — equivalent to imperfect-observation models. Contrast with full-information best-choice (running record / Gilbert–Mosteller).

For poker: when spot-class memory is intentionally compressed (or intentionally memoryless for a drill), prefer calibrated **absolute thresholds** over relative-rank / "best so far" heuristics.

## Body

### P0 — memoryless vs full-info decide() modes

| Mode | State | Policy shape |
|------|-------|--------------|
| Full-info | Running best / relative ranks | Classic optimal-stopping / record rules |
| Memoryless | No past values retained | Threshold on absolute signal only |

Do not mix: if hierarchical memory (K161) is off or spot history is wiped, do not apply relative-rank sizing logic.

### P1 — balance-at-boundary intuition

Paper emphasizes balance equations at the acceptance boundary under PPP heavy traffic. Mirror: when using a memoryless threshold for call/fold or bet-size bins, audit that the threshold is solved against the **remaining horizon** (stack depth / streets left), not a static EV cutoff copied from full-history sims.

### Out of scope

- TipDrop / David / ComfyUI
- Prod scp
- Warehouse / SEO operator playbooks

### Operator checklist

- [ ] Tag drills that intentionally wipe relative-rank history as `memoryless_threshold`
- [ ] Keep full-info record rules behind hierarchical memory path
- [ ] Advisory only — no hard submit gate

## Sources

- arXiv [2607.16145](https://arxiv.org/abs/2607.16145)
- SEO: `@seo-wiki/sources/arxiv-gnedin-2026-memoryless-best-choice-2607.16145-2026-07-20.md`
