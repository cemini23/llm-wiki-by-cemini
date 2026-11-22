---
title: "Embedding-gap ideation — a pre-registered null result"
type: concept
related:
  - sources/arxiv-embedding-map-distances-llm-ideation-2611.21408.md
  - concepts/generation-verification-gap-agent-artifacts.md
updated: 2026-11-22
---

## Raw Concept

Question this page answers: does "pick a far point in embedding space" produce good new ideas?

Synthesised from one source: `@sources/arxiv-embedding-map-distances-llm-ideation-2611.21408.md` (2611.21408). Weak fit for CCC; filed as a caution.

## Narrative

The recipe is widely circulated: embed existing work, choose a point far from its neighbours, and decode that point into a new idea. The author calls it **gap-based ideation** and tests four versions against what appeared later.

Results, all negative or null:

1. **Far random directions are not text.** No later item reaches raw cosine above about 0.10 with one. An LLM decoder shown a target's neighbours reproduces those neighbours in all six target sets.
2. **Hole scores track size.** On k-means cells, the registered hole score mostly follows cell size and position. Three density-based gap scores forecast growth at or below chance (AUC 0.30 to 0.66) and add nothing to momentum.
3. **Continuations cluster.** LLM continuations of arXiv papers stay closer to the source than real citing papers do.
4. **No inverted U.** No inverted-U relation was detected for inspiration graded by distance.

Tests were pre-registered; follow-ups from two AI reviews came after the main results.

### Reading

The value is as a caution for tool adoption. A novelty tool built on embedding distances has no evidence of working, and the failure mode is invisible: it produces text, and the text looks new. Distance is not novelty, and novelty is not quality.

For Cemini the rule is general: a tool that claims to find "gaps" needs an outcome test, not a demo. [TENTATIVE] single author, honest null.

## Snippets

> "Far random directions are not text: no later item reaches a raw cosine above about 0.10 with one." [Source: arxiv-2611.21408-do-embedding-map-distances-guide-llm-ideation-fo.pdf p.1]

> "Three density-based gap scores forecast which cells grow fastest at or below chance (AUC 0.30 to 0.66) and add nothing to momentum." [Source: arxiv-2611.21408-do-embedding-map-distances-guide-llm-ideation-fo.pdf p.1]
