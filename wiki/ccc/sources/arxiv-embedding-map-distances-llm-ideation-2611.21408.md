---
title: "Do embedding-map distances guide LLM ideation? A pre-registered null result"
type: source
related:
  - concepts/embedding-gap-ideation-null-result.md
  - concepts/generation-verification-gap-agent-artifacts.md
updated: 2026-11-22
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Do Embedding-Map Distances Guide LLM Ideation? Four Tests Against What Came Next |
| Author | Javier Aguilar Martín (AGILabs) |
| Type | arXiv paper (cs.LG), 2611.21408 |
| Location | `research to be indexed/ccc/arxiv-2611.21408-do-embedding-map-distances-guide-llm-ideation-fo.pdf` |
| Retrieved | 2026-11-22 |
| Pages | 48 |
| Read status | read |

## Narrative

The paper tests a popular ideation recipe: embed existing work, pick a point far from its neighbours, and decode that point into a new idea. The author calls this **gap-based ideation** and tests four ways the distances could help, against what actually appeared later.

Four results, all negative or null:

1. **Far random directions are not text.** No later item reaches raw cosine above about 0.10 with one. An LLM decoder shown a target's neighbours writes those neighbours in all six target sets.
2. **Hole scores track cell size.** On k-means cells of a past-only map, the registered hole score mostly follows size and position. Three density-based gap scores forecast cell growth at or below chance (AUC 0.30 to 0.66) and add nothing to momentum.
3. **LLM continuations stay close to the source.** Continuations of arXiv papers stay closer to the source than real citing papers do.
4. **No inverted U.** For inspiration graded by distance, no inverted-U relation was detected.

Original tests were pre-registered. Follow-ups requested in two AI reviews were run after the main results, and are dated only by local git commits.

This is a weak fit for CCC. Its value is as a caution, not a harness finding: the same instinct that produces "pick a far point in embedding space" produces unverified novelty tooling. The result is a null, and it is reported honestly. [TENTATIVE] single author; the null result is the claim.

## Snippets

> "A neighbour-free search writes coherent text at median cosine 0.57 and 0.47 to interior gaps, beating the nearest existing item on 15 and 14 of 20, but only 0.07 and 0.06 to far points." [Source: arxiv-2611.21408-do-embedding-map-distances-guide-llm-ideation-fo.pdf p.1]
