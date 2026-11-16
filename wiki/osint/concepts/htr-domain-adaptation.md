---
title: Domain adaptation for historical handwritten text recognition
type: concept
maturity: draft
related:
  - sources/arxiv-domain-adaptation-htr-2611.17952.md
  - sources/arxiv-dra-htr-2611.18143.md
updated: 2026-11-16
---

## Raw Concept

Question this page answers: how do you make a handwriting recogniser work on a new archive when you have few labels for it?

From two 2026 preprints by the same Luleå group (2611.17952, 2611.18143).

## Narrative

The shared recipe has three steps. Pretrain on labelled source data. Adapt to unlabelled target data so the feature distributions align. Retrain task-specific layers on source data rendered in the target's style.

Why it fits archive work: historical registers come with large unlabelled scans and almost no transcriptions. The method uses the unlabelled scans directly.

Reported results. On character classification, 76.17% macro F1 on Safran-MNIST-DLS. On line recognition across seven datasets in four languages with one configuration, state of the art on four and competitive on three, with an average 13.52-point CER reduction over DRANet and run-to-run spread falling from 7.23 to 1.11 points.

A second stage is worth separating: post-OCR correction with a language model adds 2.16 CER points. That is a language fix applied after the visual model, and it is optional.

Cost note. The adaptation compute is a training cost, not an inference cost.

[TENTATIVE] Both figures come from the papers' own abstracts. The underlying experiments were not reproduced here.

## Snippets

> "The unsupervised training increases the computation time only during training not in inference."
