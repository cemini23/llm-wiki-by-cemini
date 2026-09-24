---
title: "Matryoshka Attribution: Learning to Attribute Language Model Outputs to Representations and Weights"
type: source
tags: [arxiv, source, k270, interpretability, harness]
keywords: [k270, MAttr, attribution, mask-learning, MuBench]
related:
  - concepts/k270-harness-evolution-wave.md
maturity: draft
created: 2026-09-23
updated: 2026-09-23
read_status: skimmed
---

## Relations

- @concepts/k270-harness-evolution-wave.md

## Raw Concept

| Paper | arXiv:2609.25518 |
| File | `arxiv-2609.25518-matryoshka-attribution-learning-to-attribute-lan.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2609.25518-matryoshka-attribution-learning-to-attribute-lan.pdf` |
| Authors | Aryaman Arora, Kirill Acharya, Nathan Hu, Yanzhe Zhang, Noah Goodman, Dan Jurafsky, Christopher Potts (Stanford University) |
| Retrieved | 2026-09-23 |
| Pages | 58 |
| Dual-ID | **OSINT K270** |
| sha256 | `9c49093f719aaace3f2c3dbe2ce5a9af80660f699f5ef579cc437460873cb8ca` |

## Narrative

This page records the **attribution method only**. The PDF reports a finetuning case study as a downstream application. This page does not describe that case study.

**Problem framing.** Attribution asks which internal computations cause a language model output. Existing methods use causal interventions, gradients, or learnable masks. The paper says these methods are either infeasibly expensive or fail to identify actual causally-important internal computations.

**Proposed framing.** The paper frames attribution as the problem of identifying **nested subsets** of internal components that minimise a downstream loss. The nested structure is the "matryoshka" property: a subset at one sparsity contains the subset at the next sparsity.

**Method — Matryoshka Attribution (MAttr).** MAttr is a mask learning method. It parametrises the mask with a simple **differentiable sigmoid top-k operator**. Training supervises all sparsities at the same time by **randomising k** over training. The result is a learned ordering of components by attribution score.

**Reported result.** MAttr reaches number 1 on the official leaderboard of the Mechanistic Interpretability Benchmark (Mueller et al., 2025). The method identifies sparse and task-transferrable circuits across varying circuit bases.

**Release status.** The PDF has **no code release**. No clone. **FILE only. 0 product Integrate GO.**
