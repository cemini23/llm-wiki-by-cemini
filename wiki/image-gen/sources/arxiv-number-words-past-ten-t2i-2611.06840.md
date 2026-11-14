---
title: "Same Layout, Different Count — what number words do past ten in T2I models (arXiv:2611.06840)"
type: source
tags: [source, arxiv, t2i, counting, prompt-engineering, evaluation, flux, qwen, sd3]
keywords: [number words, counting, reach, same-noise test, SD3.5-Medium, FLUX.1-dev, FLUX.2 klein, Qwen-Image, SDXL, layout preservation, fine-scale noise]
related:
  - concepts/t2i-counting-reach.md
  - entities/models/flux-1-dev.md
  - entities/models/flux-2-klein.md
  - entities/models/qwen-image-2512.md
  - concepts/prompt-engineering-uncensored.md
read_status: read
created: 2026-11-10
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Same Layout, Different Count: What Number Words Do Past Ten in Text-to-Image Models |
| Author | Liang Yue, Eric A. Vance (University of Colorado Boulder) |
| Type | arXiv:2611.06840 [cs.CV], 43 pages |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/image-gen/arxiv-2611.06840-same-layout-different-count-what-number-words-do.pdf` |
| Retrieved | 2026-11-10 |
| File | `arxiv-2611.06840-same-layout-different-count-what-number-words-do.pdf` |
| Read status | read (abstract, methods, result tables) |

## Narrative

A careful measurement paper on one narrow question: past about ten objects, does the number word in a prompt still control the count?

**The method.** Hold the object type and the starting noise fixed. Change one thing at a time: the number, the seed, the digit spelling of the number, an unrelated word, or only the fine-scale part of the noise. Then compare. Human counters, who never saw the prompt, counted 3,088 images.

**The finding — a reach per model.** Every model follows small counts. From two to eight objects, a larger request gives more objects in 80–99% of same-noise pairs that differ. Past ten the models split.

| Model | Same-noise order, requests 2–8 | Same-noise order, requests 12–25 | Exact match, 12–30 |
|---|---|---|---|
| SDXL (CLIP) | .89 | .65 | 3% |
| SD3.5-Medium (CLIP, T5) | .80 | .57 | 4% |
| FLUX.1-dev (T5, CLIP) | .90 | .47 | 0% |
| FLUX.2 [klein] 4B (Qwen3) | .89 | .73 | 13% |
| Qwen-Image (Qwen2.5-VL) | .99 | .78 | 21% |

Order 1.0 means the larger request always gives more objects. Order 0.5 means no direction.

**Two distinct failures.** SD3.5-Medium and FLUX.1-dev stop following the number soon after ten. FLUX.2 [klein] and Qwen-Image follow it loosely up to twenty-five, about as well as a noisy estimator would.

**The layout-and-count split.** Past SD3.5-Medium's reach, a new number from the same noise keeps the picture layout (thumbnail correlation about .70) but not the count. The count moves about as much as under a new seed, and in no consistent direction. The coarse part of the starting noise fixes the composition of the picture, but not how many objects it holds.

**The number arrives but has no direction.** The number can be read off the condition in order, and the number word acts in the first denoising steps. Nothing the authors tried gives a large number a clear direction. This includes amplifying the number and fine-tuning on counted crowds.

**A count can be supplied through the noise instead.** Start SD3.5-Medium from a noised grid of the target object. People then find the requested count in 59% of images, against 4% when the count is only written in the prompt. A planted count survives a conflicting number word, while a different object word repaints the grid.

**Measurement warning.** Past ten, an exact-match score barely separates a model that follows loosely from one that ignores the number. A relative-error score can even prefer a constant guess of sixteen. The same-noise order test separates them.

**Practical read for this wiki.** The usable lesson is negative and cheap: do not write "twelve candles" or "twenty-five bottles" in a prompt and expect twelve or twenty-five. Use a layout control, a composite, or a count-aware noise start. For small counts up to about eight, the number word works and is worth writing. Four of the five models tested are in the wiki as entities.

## Snippets

> "Past ten, an exact-match score barely separates a model that follows the number loosely from one that ignores it, and a relative-error score can even prefer a constant guess of sixteen." [Source: arxiv-2611.06840 p.1]

> "SD3.5-M and FLUX.1-dev stop following it soon after ten, while FLUX.2 [klein] and Qwen-Image follow it loosely up to twenty-five." [Source: arxiv-2611.06840 p.1]

> "Shown instead as a noised grid in the starting latent, the count is drawn: people find it in 59% of images, against 4% when it is only told." [Source: arxiv-2611.06840 p.1]

## Dead Ends

- **A prompt-only fix for large counts.** The paper tried amplification, fine-tuning on counted crowds, and spelling changes. None gave the number a direction past the reach.
