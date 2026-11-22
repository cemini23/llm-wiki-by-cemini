---
title: "Dataset distillation for handwritten text recognition — a negative result"
type: source
maturity: draft
related:
  - concepts/htr-segmentation-generalization.md
  - concepts/gpuology-genealogy-agent-kit.md
updated: 2026-11-22
---

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Dataset Distillation for Handwritten Text Recognition: An Empirical Study |
| Author | Félix Fuentes-Hurtado, Eric Ayllón, Juan C. Alfaro |
| Type | arXiv preprint, computer vision |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2611.21054-dataset-distillation-for-handwritten-text-recogn.pdf` |
| Retrieved | 2026-11-22 |
| arXiv | 2611.21054v1 |
| Pages | 10 |
| Read status | read |

## Narrative

Dataset distillation replaces a large training set with a small synthetic set. It works well for image classification, where each sample has one class label. This paper asks whether it works for line-level handwritten text recognition (HTR), where the label is an unaligned character sequence from a nearly infinite output space. [Source: arxiv-2611.21054-dataset-distillation-for-handwritten-text-recogn.pdf p.1]

To adapt the methods, the authors cluster transcriptions by character n-grams and call the clusters "text pseudo-classes". They apply gradient matching (GM), distribution matching (DM) and trajectory matching (MTT) to a CRNN trained with CTC. Synthetic line images are made by optimising only the pixels of real starting lines, while the transcription stays fixed.

The result is negative and clear. Across four datasets (IAM, George Washington, READ 2016, LAM) and three budgets (1% to 10% of the training lines), no distilled set beats its real starting lines. Random starting lines beat medoid starting lines. Further optimisation only degrades recognition. DM lowers its objective without a gain. GM and MTT barely move their objectives. [Source: arxiv-2611.21054-dataset-distillation-for-handwritten-text-recogn.pdf p.1]

Why this matters for the genealogy workstream: HTR models are retrained per collection, per hand and per period. A working distillation method would cut that cost. This paper says the classification-era distillation recipes do not transfer. A practical pipeline should keep a small curated real sample, not a synthetic one.

## Snippets

> "Across four datasets ... no distilled set outperforms its real initialisation lines." [Source: arxiv-2611.21054-dataset-distillation-for-handwritten-text-recogn.pdf p.1]
