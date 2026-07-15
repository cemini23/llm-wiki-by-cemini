---
title: K139 — DeepSearch scaffold + staged reflection delta (poker sandbox)
type: brief
target: Poker Arena
created: 2026-07-15
updated: 2026-07-15
---

## Target

`agents/devfun-poker-arena/` — HL analyst loop / Researcher Round HU sandbox.

## Summary

**Delta only** on top of shipped K161 DeepSearch trajectory filter (`config/hu_deepsearch_trajectory_filter.json`). SEO K139 re-read of arXiv **2607.07820** adds two steals K161 left advisory-thin: (1) **scaffold → ReAct** conversion shape for HL briefs, (2) **staged reflection strength** after repeated same-spot fails.

Core generate→filter→mix remains Watch / already shipped — do not re-implement.

## Body

### P0 — scaffold fields before mix (advisory)

When a failure unit is tagged eligible, require HL brief memory to expose the paper's four scaffold fields (rename OK):

| Scaffold field | Arena analog |
|----------------|--------------|
| `completed_list` | Verified facts this spot (stack, board class, HUD tag) |
| `todo_list` | Next decide() checks / regression spot |
| `experience` | Lessons from prior losses in same spot class |
| `information` | Evidence tokens cited (cards/street/action) |

Drop units that only have free-form ungrounded reflection (already in K161 drop rules) **or** lack `experience` after ≥2 same-spot failures.

### P1 — staged reflection strength

Mirror DeepSearch's soft→stronger failure hints:

1. **First fail** in spot class → generic reformulation note ("recheck sizing vs HUD").
2. **Repeated fail** (≥2) → stronger grounded hint required (cite concrete board/street leak or veto).

Do not inject "teacher" gold actions from a stronger model — keep self-generated, filter-verified.

### Out of scope

- Vendoring DeepSearch-World Wikipedia env / 420K pool / 9B weights (not released; >> size budget)
- TipDrop / David persona (no image-gen path)
- Prod cemini-prod scp (wiki-only default for this paper)

### Operator checklist

- [ ] Add scaffold four-field block to next HL failure-mix brief template
- [ ] Gate: repeated same-spot fail requires stronger `experience` string
- [ ] Leave K161 filter config as source of truth for required tags
- [ ] Revisit Adopt only when authors publish SPDX code + small eval subset

## Sources

- arXiv [2607.07820](https://arxiv.org/abs/2607.07820)
- `briefs/2026-07-13_k161-hierarchical-memory-deepsearch-steal.md`
- `references/deepsearch-trajectory-filter.md`
- SEO companion: seo-wiki sources/arxiv-geng-2026-deepsearch-world-self-distillation-2607.07820-2026-07-15.md
