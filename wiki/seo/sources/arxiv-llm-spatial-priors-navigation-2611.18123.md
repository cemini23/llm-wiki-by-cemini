---
title: "Evaluating Language Models as Spatial Priors for Object-Goal Navigation (2611.18123)"
type: source
maturity: draft
related:
  - concepts/llm-spatial-priors-limits.md
updated: 2026-11-16
read_status: read
---

## Raw Concept

- **Title:** Evaluating Language Models as Spatial Priors for Object-Goal Navigation
- **Author:** Jun Miura (Toyohashi University of Technology)
- **Type:** arXiv preprint, robotics
- **Location:** `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2611.18123-evaluating-language-models-as-spatial-priors-for.pdf`
- **Retrieved:** 2026-11-16
- **arXiv:** 2611.18123
- **Read status:** full — 96 pages extracted 2026-11-16

## Narrative

Instead of asking a model for a scalar object-room affinity, this work asks for a spatial prior: a distribution over where the target object sits in a room. Two open-weight models, Qwen3.5-27B and Gemma-4-31B-it, are tested on real layouts from CubiCasa5K and ScanNet.

What holds: generated rooms reproduce object frequencies and room sizes for the room type. What fails: object proximity to walls does not follow the real per-room-type differences. On movable furniture, the models assign higher likelihood to layouts with everything piled at room centre than to the real layouts.

When given a target object, the models place related objects near it and move others away. When given each object's wall, they place most objects against it but do not keep everything inside the room rectangle.

The search-cost result is the decision-relevant one: generated placements reduce searched area relative to a uniform prior, but by less than a third of the reduction from a prior built on real layouts; after spatial smoothing the fraction stays below two thirds, and the real-layout prior wins in every room type.

Conclusion: use models for object-room association and for writing coordinates under an external constraint, followed by a geometric check — not as a placement prior where real layouts exist.

No SEO lane. Recorded because it was dropped in the seo inbox.

[Source: arxiv-2611.18123-evaluating-language-models-as-spatial-priors-for.pdf]

## Snippets

> "the real-layout prior gives the lower search cost in every room type."

## Dead Ends

- **Full-read note (2026-11-16):** Generated placements reduce search area by less than a third of the real-layout prior; after smoothing the fraction stays below two thirds, and the real-layout prior wins in every room type. [Source: arxiv-llm-spatial-priors-navigation-2611.18123.md full text, 96pp]
