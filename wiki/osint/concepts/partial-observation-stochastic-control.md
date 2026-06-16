---
title: Partial-observation stochastic control — particle + DeepSets pattern
type: concept
tags: [concept, stochastic-control, partial-observation, deep-learning, execution]
keywords: [particle-filter, deep-sets, latent-drift, filtering-distribution, deep-bsde]
related:
  - sources/arxiv-particle-methods-partial-observation-2606.09055-2026-06-15.md
  - concepts/stochastic-calculus-foundations.md
  - concepts/quant-finance.md
  - sources/arxiv-tt-dac-ps-optimal-execution-2606.08379-2026-06-10.md
  - concepts/time-inconsistent-stochastic-control.md
  - sources/arxiv-dpg-time-inconsistent-equilibrium-2606.11798-2026-06-16.md
maturity: draft
created: 2026-06-15
updated: 2026-06-16
---

## Relations

- @sources/arxiv-particle-methods-partial-observation-2606.09055-2026-06-15.md — primary source (K117)
- @concepts/stochastic-calculus-foundations.md — measure-valued filtering background
- @concepts/quant-finance.md — corpus cluster
- @sources/arxiv-tt-dac-ps-optimal-execution-2606.08379-2026-06-10.md — fully observed execution RL contrast
- @concepts/time-inconsistent-stochastic-control.md — K118: time-inconsistent objectives break naive DP
- @sources/arxiv-dpg-time-inconsistent-equilibrium-2606.11798-2026-06-16.md — K118 DPG equilibrium learner

## Raw Concept

K117 arXiv 2606.09055 — when controllers observe noisy signals but state is latent (unobserved drift, hidden factors), the Bellman state becomes a **filtering distribution**. Particle methods + symmetric NNs make this finite-dimensional and trainable.

## Narrative

### Problem shape

Fully observed control → HJB on physical state `x`. Partial observation → HJB on **conditional law** `P(X_t | G_t)` — infinite-dimensional. Finance instances: portfolio optimization under **unobserved drift**, liquidation with latent liquidity factors, trading from price-only signals.

### Particle surrogate

Reference-probability reformulation maps observations to **common noise**; N weighted particles `(X^k, L^k)` approximate the filtering state with proved convergence (under Lipschitz + compact-action assumptions). Time discretization yields a **finite-dimensional Markov control problem** solvable by RL-style methods.

### Why DeepSets matter

Particle cloud is **permutation-invariant**. Generic MLPs over `2N` inputs over-parameterize; DeepSets (`Φ₂(mean_k Φ₁(x^k))`) exploit symmetry — same pattern as population-distribution networks in mean-field RL literature.

### Solvers (paper)

| Method | When |
|--------|------|
| Direct symmetric feedback | General; optimize expected cost via Adam + path sampling |
| Deep BSDE | Uncontrolled diffusion; BSDE characterization of value |
| RNN baseline | Path-dependent controls |

### Cemini steal-from (REFERENCE only)

1. **Name the partial-observation gap** in equity execution briefs — TT-DAC-PS assumes observable state; latent drift / microstructure states are not.
2. **Particle + symmetric NN** as research harness template if Cemini adds filtering-state execution sim on laptop Arctic.
3. **Do not prod-deploy** without replication — paper uses synthetic + benchmark LQ; no open production codebase.

## Snippets

> "The particle reformulation is high-dimensional but permutation-invariant, a structure that can be exploited by symmetric neural network architectures." [Source: arxiv-2606.09055-particle-methods-with-deep-learning-for-stochast.pdf abstract]
