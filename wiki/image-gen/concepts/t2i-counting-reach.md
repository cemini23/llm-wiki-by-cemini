---
title: T2I counting reach (how far a number word in a prompt still works)
type: concept
tags: [concept, t2i, prompt-engineering, evaluation, counting]
keywords: [counting, reach, number word, same-noise test, layout preservation, fine-scale noise, exact-match metric, SD3.5, FLUX.1-dev, FLUX.2 klein, Qwen-Image, SDXL]
related:
  - sources/arxiv-number-words-past-ten-t2i-2611.06840.md
  - entities/models/flux-1-dev.md
  - entities/models/flux-2-klein.md
  - entities/models/qwen-image-2512.md
  - concepts/prompt-engineering-uncensored.md
created: 2026-11-10
updated: 2026-11-10
---

## Raw Concept

The question this page answers: for which count ranges can a prompt operator rely on a number word, and what replaces it past that range? Synthesized from arXiv:2611.06840.

## Narrative

**Definition.** A model's *reach* is the range of requested counts over which it still follows the number word. The measurement holds the object type and the starting noise fixed, changes only the number, and asks whether the larger request produced more objects in the same-noise pair.

A single-number summary is the *effective scatter* — the noise level of a simulated loose estimator that orders crowds as well as the model does. A model whose order falls to 0.5 has no finite scatter and is not following the number at all.

**Measured reach, five open models.**

| Model | Follows 2–8 | Follows 12–25 | Exact at 12–30 |
|---|---|---|---|
| SDXL | yes (.89) | partly (.65) | 3% |
| SD3.5-Medium | yes (.80) | weakly (.57) | 4% |
| FLUX.1-dev | yes (.90) | no (.47) | 0% |
| FLUX.2 Klein 4B | yes (.89) | loosely (.73) | 13% |
| Qwen-Image | yes (.99) | loosely (.78) | 21% |

All five are covered as entities in this wiki. The ordering is stable: Qwen-Image and FLUX.2 Klein hold the number furthest.

**Two separate things fail past the reach.** This is the part worth remembering.

- The **layout** survives. Thumbnail correlation stays about .70 when only the number changes.
- The **count** does not. It moves about as much as under a fresh seed, with no consistent direction.

The coarse part of the starting noise fixes the composition of the picture but not how many objects sit in it. A redraw of only the noise finer than an eighth of the image keeps the layout just as well, and already moves a large crowd's count two-thirds as far as a new number does.

**Why this matters for measurement.** Past ten, exact-match barely separates a model that follows loosely from one that ignores the number. A relative-error score can prefer a constant guess of sixteen. Use a same-noise order test instead when comparing models or LoRAs.

**The workaround that works.** Put the count into the noise, not the prompt. Starting SD3.5-Medium from a noised grid of the target object raises human-read correct counts from 4% to 59%. The planted count survives a conflicting number word, and a different object word repaints the grid.

**Practical rules for this wiki's persona and product work.**

1. Up to about eight objects, write the number. It works.
2. Past ten, a number word is decoration. Use a layout control, a composite, or a count-aware noise start.
3. Do not tune a LoRA against an exact-count metric above ten. The metric cannot see the effect you want.
4. When comparing two models on crowds, hold the seed and compare order, not exact hits.

**Scope limit.** All measurements are off-the-shelf open models with plain "a photo of c Xs" prompts. Few-step distilled variants and fine-tuned community checkpoints were not tested [OPEN QUESTION 2026-11-10].

## Snippets

[Source: arxiv-2611.06840 p.1 — "Past SD3.5-M's reach, the coarse part of the starting noise fixes the composition of the picture but not how many objects it holds."]
