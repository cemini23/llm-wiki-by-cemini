---
title: "Evolution Strategies at the Hyperscale — EGGROLL (Sarkar et al., Oxford/MILA/NVIDIA, 2026)"
type: source
tags: [paper, evolution-strategies, rl-marl, llm-training, black-box-optimization, low-rank, es]
keywords: [eggro, evolution-strategies, black-box-optimization, low-rank-perturbations, llm-pretraining, grpo, rwkv, int8-training, zeroth-order, gaussian-es, neural-tangent-kernel]
related:
  - sources/matching-accuracy-different-geometry-es-grpo.md
  - sources/sakana-conductor-rl-orchestration.md
  - sources/sakana-trinity-llm-coordinator.md
  - concepts/rl-marl-research.md
maturity: validated
read_status: deep-read
created: 2026-05-15
updated: 2026-05-15
clusters: [rl-marl, ml-methods]
---

## Relations
- @ccc-wiki/briefs/2026-05-15_2026-05-15_eggro-evolution-strategies-llm-fine-tuning.md  (cross-wiki brief)

- @sources/matching-accuracy-different-geometry-es-grpo.md — companion paper comparing ES vs GRPO training geometry; EGGROLL provides the scalable ES implementation
- @sources/sakana-conductor-rl-orchestration.md — Conductor uses GRPO; EGGROLL offers an ES alternative for non-differentiable reward functions
- @sources/sakana-trinity-llm-coordinator.md — Trinity uses sep-CMA-ES; EGGROLL's low-rank structuring could accelerate it
- @concepts/rl-marl-research.md — corpus hub for RL/MARL papers; EGGROLL adds the black-box optimization perspective

## Raw Concept

- **Title**: Evolution Strategies at the Hyperscale
- **Authors**: Bidipta Sarkar, Mattie Fellows, Juan Agustin Duque, Alistair Letcher, et al. (FLAIR / WhiRL — University of Oxford; MILA — Québec AI Institute; NVIDIA AI Technology Center; NormaCore.dev)
- **Type**: Academic paper
- **Date**: 2026
- **Retrieved**: 2026-05-15
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/Evolution Strategies at the Hyperscale.pdf`
- **Pages**: 76
- **Read status**: deep-read

## Narrative

EGGROLL (Evolution Guided GeneRal Optimisation via Low-rank Learning) solves a critical bottleneck: naive Evolution Strategies (ES) becomes prohibitively expensive at scale on GPUs because batched matrix multiplications with unstructured random perturbations have low arithmetic intensity.

### Core contribution

Instead of sampling full d-dimensional perturbation vectors, EGGROLL structures each perturbation as a **rank-r matrix** E_i = (1/√r) A_i B_i^T, where A_i ∈ R^{m×r} and B_i ∈ R^{n×r}. This improves arithmetic intensity by orders of magnitude, achieving **up to 91% of pure batch inference throughput** — a ~100× speedup at billion-parameter scale and large population sizes.

### Key theoretical results

1. **High-dimensional convergence**: Proves a critical noise scaling σ_d = o(d^{-1/2}) under which the ES update linearises and converges to the first-order derivative. Three regimes identified: linearisation, critical, divergence.

2. **EGGROLL consistency**: Even fixed rank-1 updates converge to the true ES gradient as dimension grows. The overall update rank is min(N·r, m, n) — not restricted to low-rank.

3. **Gaussian recovery**: As rank r increases, the EGGROLL perturbation distribution converges to Gaussian via CLT, recovering the standard ES score function.

### Three empirical demonstrations

1. **Pure integer pretraining**: Trains an int8 RNN language model from scratch, reaching 3.40 bits/byte vs 3.58 for a fp32 Transformer trained with backprop SGD — *ES beats backprop on a language modeling task*.

2. **LLM post-training**: Competitive with GRPO on reasoning tasks, using RWKV7 models.

3. **Tabula rasa RL**: No performance compromise vs full ES despite being dramatically faster.

### Relevance to Cemini

EGGROLL enables **gradient-free training of trading models** where the objective (PnL, Sharpe, max drawdown) is non-differentiable. The low-rank structuring maps naturally to financial models where parameter matrices (e.g., attention weights, factor loadings) already have low effective rank. For the Cemini RL-for-trading stack, EGGROLL offers a path to optimize directly against terminal portfolio metrics rather than surrogate loss functions. The LLM post-training results also suggest applicability to fine-tuning Cemini's internal LLM components on reasoning-heavy market analysis tasks.

## Snippets

> "We introduce Evolution Guided GeneRal Optimisation via Low-rank Learning (EGGROLL), which improves arithmetic intensity by structuring individual perturbations as rank-r matrices, resulting in a hundredfold increase in training speed for billion-parameter models at large population sizes, achieving up to 91% of the throughput of pure batch inference." (p.1)

> "ES does not require taking derivatives directly through the fitness function; instead the Monte Carlo update only requires evaluation of f(x_i) for each mutation x_i to estimate ∇J(θ)." (p.4)

> "EGGROLL enables the stable pretraining of nonlinear recurrent language models that operate purely in integer datatypes." (p.1)

> "we prove that even fixed low-rank updates (including rank-1) converge to the true ES gradient as dimension grows, despite heavier-tailed perturbations." (p.3)
