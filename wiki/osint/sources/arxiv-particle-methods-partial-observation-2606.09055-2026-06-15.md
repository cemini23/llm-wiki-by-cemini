---
title: "Particle Methods with Deep Learning for Stochastic Control under Partial Observation (arXiv 2606.09055, 2026)"
type: source
tags: [source, stochastic-control, partial-observation, deep-learning, execution, k117]
keywords: [particle-filter, deep-sets, deep-bsde, mean-field-control, portfolio-liquidation, latent-drift]
related:
  - concepts/partial-observation-stochastic-control.md
  - concepts/stochastic-calculus-foundations.md
  - concepts/quant-finance.md
  - sources/arxiv-tt-dac-ps-optimal-execution-2606.08379-2026-06-10.md
maturity: draft
read_status: read
created: 2026-06-15
updated: 2026-06-15
clusters: [quant-finance, rl-marl, ml-methods]
---

## Relations

- @concepts/partial-observation-stochastic-control.md — synthesis page
- @concepts/stochastic-calculus-foundations.md — filtering / measure-valued state background
- @concepts/quant-finance.md — corpus cluster
- @sources/arxiv-tt-dac-ps-optimal-execution-2606.08379-2026-06-10.md — sibling equity execution RL lane

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Particle Methods with Deep Learning for Stochastic Control under Partial Observation |
| **Authors** | Laurière, Tan, Yang (NYU Shanghai / CUHK) |
| **arXiv** | 2606.09055 |
| **sha256** | `b61c38e68ec25bc3…` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2606.09055-particle-methods-with-deep-learning-for-stochast.pdf` |
| **Retrieved** | 2026-06-15 |
| **Read status** | read (abstract + §2–3 + financial application pointers) |

## Narrative

Under partial observation the dynamic-programming state is the **conditional distribution** of hidden variables — infinite-dimensional. Laurière et al. replace it with a **weighted N-particle system** using common-noise-adapted mean-field control limit theory ([6]); prove convergence of the fully discretized particle approximation to the continuous-time problem.

**Computational hooks:**

1. **Permutation invariance** — particle states `(X^k, L^k)` are symmetric → **DeepSets** architectures keep parameter count tractable vs generic high-D nets.
2. **Two solvers** — direct symmetric feedback optimization (Adam) and **Deep BSDE** when diffusion is uncontrolled.
3. **Financial demos** — portfolio **liquidation** and **asset allocation** under unobserved drift / latent factors.

**Cemini posture:** **REFERENCE** — steal the *problem framing* (latent drift, filtering-as-state) for equity execution research; do not port particle+Deep BSDE stack to prod without Arctic replication harness. Complements TT-DAC-PS (fully observed execution RL) by naming the partial-observation gap.

## Snippets

> "Under partial observation, the relevant state is the conditional distribution of the hidden state given the observations. This filtering distribution is measure-valued." [Source: arxiv-2606.09055-particle-methods-with-deep-learning-for-stochast.pdf §1]

> "The system is invariant under permutations of the particles. This symmetry is essential for computation: it allows us to use symmetric neural network architectures, such as DeepSets-type architectures." [Source: arxiv-2606.09055-particle-methods-with-deep-learning-for-stochast.pdf §1]

> "Numerical experiments on a linear–quadratic benchmark, a nonlinear partially observed mean-field control problem, and two financial applications, portfolio liquidation and asset allocation." [Source: arxiv-2606.09055-particle-methods-with-deep-learning-for-stochast.pdf abstract]
