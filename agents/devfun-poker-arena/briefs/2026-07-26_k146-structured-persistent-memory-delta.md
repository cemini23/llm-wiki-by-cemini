---
title: K146 — structured persistent memory delta (poker sandbox)
type: brief
target: Poker Arena
created: 2026-07-26
updated: 2026-07-26
---

## Target

`agents/devfun-poker-arena/` — HL analyst loop / Researcher Round HU sandbox.

## Summary

Thin steal from sequential EQA memory (arXiv 2607.21571): multi-query-in-same-scene needs **structured persistent memory** of visual/semantic evidence — not occupancy-only maps and not raw episode transcripts. Complements K161 hierarchical memory + K144 MaRA select-then-synthesize.

## Body

### P0 — session vs episode

| Mode | Behavior |
|------|----------|
| Episodic | Wipe spot memory between HL briefs |
| Sequential | Carry structured spot-class / table-state evidence across related decide() queries |

Prefer sequential when drilling the same table/session. Store evidence tokens (street, action line, failure unit IDs), not only “explored spots.”

### Out of scope

- Robot navigation code
- TipDrop / David / prod scp

### Operator checklist

- [x] Tag multi-query HL sessions as `sequential_memory` (documented in `references/hierarchical-session-memory.md`)
- [ ] Persist structured evidence alongside stigmergy scores (still advisory / HL ops)
- [x] Advisory — no hard submit gate

## Sources

- arXiv [2607.21571](https://arxiv.org/abs/2607.21571)
- SEO: `@seo-wiki/sources/arxiv-cai-2026-sequential-eqa-memory-bottlenecks-2607.21571-2026-07-26.md`
