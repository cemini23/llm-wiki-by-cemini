---
title: "BISECT — spectral starvation in low-rank continual learning"
type: source
tags: [source, arxiv, lora, continual-learning, vision-transformer, rank]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-03
updated: 2026-11-03
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | BISECT: Bilevel Spectral Decomposition for Low-Rank Continual Learning |
| Authors | Tom Saliencro, Wen-Hsuan Liu, Rohan Desai, Amara Okonkwo, Maya Lindqvist (UC Irvine, University of Washington) |
| arXiv | 2611.03574 |
| Pages | 18 |
| Read status | skimmed (abstract) |

## Narrative

Exemplar-free continual learning on pretrained Vision Transformers usually means LoRA, and current methods manage the low-rank update space by **strict subspace isolation** — projecting each new task into the approximate null space of historical activations.

That treats *any* cross-task feature overlap as catastrophic interference. The paper argues the orthogonality premise creates a **structural bottleneck they name spectral starvation**: when down-projection bases are locked before task optimisation, the gradient norm reaching the update is starved.

BISECT replaces isolation with a **bilevel spectral decomposition**, so the basis is not frozen before the task is seen.

### Why it is a useful reframe

The orthogonality assumption is intuitive and wrong in a specific way: tasks that genuinely share features are punished for sharing them. The failure is not interference, it is **refusing available capacity**.

For LoRA fine-tuning in general — not just continual learning — the lesson transfers: **a rank budget locked before you see the task allocates capacity by guess rather than by need.**

**Caveat.** Abstract only. No accuracy table reproduced.

## Snippets

> "We show that this orthogonality premise induces a structural bottleneck we term spectral starvation: when down-projection bases are locked before task optimization, the gradient norm reaching t…" [Source: arxiv-2611.03574 p.1]

## Dead Ends

- **Citing an accuracy number.** Abstract only.
