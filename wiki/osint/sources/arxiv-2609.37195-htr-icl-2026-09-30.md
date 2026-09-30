---
title: "In-context learning for handwritten text recognition (2609.37195)"
type: source
tags: [source, k276, atto, htr, in-context-learning]
keywords: [k276, htr, icl, vlm, few-shot]
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

| File | `arxiv-2609.37195-exploring-in-context-learning-for-handwritten-te.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2609.37195-exploring-in-context-learning-for-handwritten-te.pdf` |
| Archive | egress-fi 2026-09-30 |
| Retrieved | 2026-09-30 |
| Dual-ID | **OSINT K276** |
| sha256 | `1d91ea138120a0cfbb9ec3935ddaf48396ca0bce5d744f82b954b9fd7f1d816f` |
| arXiv | 2609.37195 |
| Authors | Eric Ayllon, Abel Gandia, Jorge Calvo-Zaragoza (University of Alicante) |

## Narrative

The paper transcribes handwriting with general vision-language models and no parameter updates. The pipeline is an instruction, k image-and-transcript demonstrations, then a query image.

Error is reported as global character error rate. IAM falls from 17.68% with no context to 5.36% at 16 examples. RIMES falls from 8.81% to 5.56%. SaintGall falls from 32.98% to 18.54%. Most of the gain appears at context size 2 to 4. Qwen3 is the best model in most settings.

Cross-domain results stay close to in-domain. That is the interesting part for archival work, where the target hand differs from the demonstration hand.

Two failure modes are admitted: verbose non-transcriptions, and generation loops. The early-modern German set ICFHR16 fails badly at 378% zero-shot.

Result for Atto: a possible in-house option, not a win. The paper does not test Transkribus. Best-case historical numbers, about 18 to 21% error on SaintGall and LAM, do not beat a trained product system. The useful property is few-shot setup with no training run.

No author code. The method runs on public checkpoints: Qwen2.5-VL-7B, Qwen3-VL-8B, Gemma-4-E4B, Kimi-VL-A3B. No clone. Transkribus stays the only product HTR.
