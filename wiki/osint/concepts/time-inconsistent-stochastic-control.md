---
title: Time-inconsistent stochastic control — equilibrium via deterministic policy gradient
type: concept
tags: [concept, stochastic-control, reinforcement-learning, time-inconsistency, quant-finance, k118]
keywords: [extended-hjb, subgame-perfect-nash, mean-variance, hyperbolic-discounting, dpg, continuous-time-rl]
related:
  - sources/arxiv-dpg-time-inconsistent-equilibrium-2606.11798-2026-06-16.md
  - concepts/stochastic-calculus-foundations.md
  - concepts/partial-observation-stochastic-control.md
  - concepts/markov-regime-switching-models.md
  - sources/arxiv-tt-dac-ps-optimal-execution-2606.08379-2026-06-10.md
maturity: draft
created: 2026-06-16
updated: 2026-06-16
---

## Relations

- @sources/arxiv-dpg-time-inconsistent-equilibrium-2606.11798-2026-06-16.md — K118 primary source
- @concepts/stochastic-calculus-foundations.md — continuous-time machinery
- @concepts/partial-observation-stochastic-control.md — K117 latent-state control sibling
- @concepts/markov-regime-switching-models.md — regime breaks time-consistency in practice

## Raw Concept

K118 arXiv 2606.11798 — when objectives are time-inconsistent (mean-variance, hyperbolic discounting, state-dependent risk aversion), classical dynamic programming fails. Standard fix: intra-personal game → **subgame-perfect Nash equilibrium** characterized by **extended HJB** (coupled PDE family, model coefficients required).

## Narrative

### Failure modes of stochastic-policy continuous RL here

| Issue | Why it blocks naive extension |
|-------|------------------------------|
| Coupled extended exploratory HJB | Not a simple time-consistent HJB + entropy term |
| Continuous-time sampling | Gibbs-measure stochastic policies hard to sample |
| Entropy regularization | Alters problem; poor approximation for diffusion control in finance examples |

### DPG two-stage reformulation (steal-from)

1. Introduce auxiliary functions capturing future selves' preferences → modified running reward.
2. **Stage 1:** time-consistent auxiliary problem → **deterministic policy gradient**.
3. **Stage 2:** fixed-point on auxiliary functions given policy (martingale characterizations).
4. Outer loop repeats until equilibrium.

**Finance demos:** mean-variance portfolio; optimal tracking with non-exponential discounting.

**Cemini use:** vocabulary for why **vol-scaling / turnover controls** (K117) matter more than pretending a single global optimum exists across rebalance horizons. REFERENCE only — no code drop.

## Snippets

> "A policy deemed optimal at current time might be disagreed at a future date." [Source: arxiv-2606.11798-deterministic-policy-gradient-for-learning-equil.pdf §1]
