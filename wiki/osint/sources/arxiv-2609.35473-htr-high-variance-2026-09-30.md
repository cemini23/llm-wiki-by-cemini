---
title: "HTR lives in the high-pixel-variance subspace (2609.35473)"
type: source
tags: [source, k276, atto, htr, self-supervised]
keywords: [k276, htr, mae, pretraining, no-weights]
related:
  - concepts/k276-atto-htr-wave.md
maturity: draft
created: 2026-09-30
updated: 2026-09-30
read_status: skimmed
---

## Relations

- @concepts/k276-atto-htr-wave.md

## Raw Concept

| File | `arxiv-2609.35473-handwritten-text-recognition-lives-in-the-high-p.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2609.35473-handwritten-text-recognition-lives-in-the-high-p.pdf` |
| Archive | egress-fi 2026-09-30 |
| Retrieved | 2026-09-30 |
| Dual-ID | **OSINT K276** |
| sha256 | `8303cdcd227c0dec33935169701f7ee0cc79f3fde63ba7980cd7e20f8b649ef4` |
| arXiv | 2609.35473 |
| Authors | Carlos Garrido-Munoz, Jorge Calvo-Zaragoza (University of Alicante) |

## Narrative

The paper makes a distribution claim. The discriminative signal in a handwritten line image lives in the high-variance pixel subspace. That is the inverse of natural-image classification, where the signal sits in low-variance directions. If true, pixel reconstruction is the right pretraining objective for HTR.

The authors probe the input with pixel-PCA, top-K against bottom-K projections, read by a BiLSTM-CTC probe. They adapt I-JEPA and V-JEPA-2 to HTR and compare six self-supervised methods under one matched ViT-B encoder.

Real-data mean character error rate: MAE 5.5%, SimMIM 8.7%, V-JEPA-2 10.6%, SigLIP 14.5%, I-JEPA 14.7%, MoCo-v3 19.2%. Only the two pixel-grounded methods beat their baselines. Full fine-tuning gives MAE 4.5% against TrOCR-B at 4.7%. At 10% of labels MAE reaches 8.8%.

The benchmarks are Latin-script and historical: Bentham, Rodrigo, Parzival, LAM, IAM, RIMES. That is our document class.

The authors admit the study uses one encoder scale and one seed per experiment. Non-Latin scripts are untested.

Result for Atto: a method signal, not a product. No checkpoint and no code are released. Transkribus stays the only product HTR. Do not swap the HTR path on this paper alone.
