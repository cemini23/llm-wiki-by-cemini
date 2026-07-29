---
title: K144 — MaRA segment-select delta (poker sandbox)
type: brief
target: Poker Arena
created: 2026-07-22
updated: 2026-07-22
---

## Target

`agents/devfun-poker-arena/` — HL analyst loop / Researcher Round HU sandbox.

## Summary

Thin steal from **MaRA** (arXiv 2607.19326): before generating an answer, **rank and keep** only query-relevant input segments. Token-level adapters cannot fix paragraph-level irrelevance.

For poker HL: when assembling a decide()/GenomeDiff brief from multiple traces, spot reports, and prior briefs — **select segments** (failure units, recent stigmergy scores, relevant streets) before the long synthesis call.

## Body

### P0 — select-then-synthesize

1. Gather candidate snippets (K161 tags, stigmergy top-N, last-N hand notes)
2. Score relevance to the current spot question (cheap ranker / keyword+tag filter is enough without MaRA code)
3. Cap context; then run HL generation

### Out of scope

- Installing MaLoRA/MaRA weights
- TipDrop / David / prod scp

### Operator checklist

- [ ] Add optional `segment_select_cap` before HL brief expansion
- [ ] Log which segments were dropped (audit)
- [ ] Advisory — no hard submit gate

## Sources

- arXiv [2607.19326](https://arxiv.org/abs/2607.19326)
- SEO: `@seo-wiki/sources/arxiv-dokme-2026-malora-mara-state-space-adapters-2607.19326-2026-07-22.md`
