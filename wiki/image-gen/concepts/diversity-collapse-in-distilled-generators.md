---
title: Diversity collapse in distilled image and video generators
type: concept
maturity: draft
related:
  - sources/arxiv-rediverse-diversity-collapse-2611.18550.md
updated: 2026-11-16
---

## Raw Concept

Question this page answers: why do few-step distilled generators produce nearly the same image for every seed, and can it be undone?

From arXiv 2611.18550 (ReDiverse).

## Narrative

The symptom is familiar to anyone running a distilled or aggressively merged checkpoint: two seeds, one prompt, one picture.

The diagnosis is specific. Comparing student activations to the teacher's shows the total variance is about the same, but it occupies far fewer directions. The compression is localised to one intermediate block at the first denoising step. The model has not lost the ability to generate variety; it has stopped spreading its variance across the directions that produce it.

The repair has two forms. At training time, a lightweight adapter is fine-tuned to regress student activations back onto the teacher's. At inference time, a correction reinstates the missing variance directions without retraining the whole model.

What to check when output variety drops: not the sampler settings, and not the prompt, but whether the checkpoint is distilled and whether an activation-space correction is available.

[OPEN QUESTION 2026-11-16] Whether the correction holds under heavy LoRA stacking, where multiple adapters each shift the activation distribution, is untested in the abstract.

## Snippets

> "diversity collapse stems from a misallocation of activation variance rather than an inherent loss of generative capability."
