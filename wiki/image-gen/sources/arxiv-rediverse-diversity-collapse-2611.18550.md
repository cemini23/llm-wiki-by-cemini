---
title: "Restoring Diversity in Distilled Image and Video Generators by Probing Activations (2611.18550)"
type: source
maturity: draft
related:
  - concepts/diversity-collapse-in-distilled-generators.md
  - sources/arxiv-jvt-pixel-space-video-diffusion-2611.18549.md
updated: 2026-11-16
---

## Raw Concept

- **Title:** Restoring Diversity in Distilled Image and Video Generators by Probing Activations
- **Authors:** Furkan Horoz, Ozgur Kara, Kaan Oktay et al. (UIUC, fal, Johns Hopkins)
- **Type:** arXiv preprint, cs.CV
- **Location:** `cemini-egress-fi:/opt/cemini-bulk/research/image-gen/arxiv-2611.18550-restoring-diversity-in-distilled-image-and-video.pdf`
- **Retrieved:** 2026-11-16
- **arXiv:** 2611.18550
- **Read status:** full — 42 pages extracted 2026-11-16

## Narrative

Few-step distillation cuts sampling latency and costs diversity: different seeds produce nearly the same image for a fixed prompt.

The paper locates the cause. Probing student activations against the teacher's shows total activation variance is comparable, but it is concentrated into substantially fewer directions. The collapse is localised to an identifiable intermediate block at the initial denoising step. So the failure is a misallocation of variance, not a loss of generative capacity.

The fix follows from the diagnosis: restore the missing directions. ReDiverse-FT fine-tunes a lightweight adapter that regresses student activations onto the teacher's at training time; ReDiverse-TF does the inference-time counterpart.

Demonstrated on SDXL, SD3, Wan 2.1 and MiniMax-H3, with visibly broader variation across seeds for the same prompt.

Relevance to any distilled or LoRA-merged pipeline in this wiki: a dropdown in output variety after distillation is a known, diagnosable artefact rather than an unavoidable trade.

[Source: arxiv-2611.18550-restoring-diversity-in-distilled-image-and-video.pdf]

## Snippets

> "distilled students maintain total activation variance comparable to their teachers, but concentrate it into substantially fewer directions."

## Dead Ends

- **Full-read note (2026-11-16):** Discussion: diversity is lost at a single collapsed block, where the student's features lose the teacher's principal directions of variation that downstream blocks could still render. [Source: arxiv-rediverse-diversity-collapse-2611.18550.md full text, 42pp]
