---
title: "Deterministic Policy Gradient for Learning Equilibrium in Time-Inconsistent Control (arXiv 2606.11798)"
type: source
tags: [source, arxiv, reinforcement-learning, stochastic-control, time-inconsistency, quant-finance, k118]
keywords: [2606.11798, deterministic-policy-gradient, extended-hjb, mean-variance, non-exponential-discounting, continuous-time-rl]
related:
  - concepts/time-inconsistent-stochastic-control.md
  - concepts/stochastic-calculus-foundations.md
  - concepts/partial-observation-stochastic-control.md
  - sources/arxiv-tt-dac-ps-optimal-execution-2606.08379-2026-06-10.md
  - concepts/markov-regime-switching-models.md
maturity: draft
read_status: read
created: 2026-06-16
updated: 2026-06-16
clusters: [quant-finance, rl-marl, ml-methods]
---

## Relations

- @concepts/time-inconsistent-stochastic-control.md — equilibrium-as-game framing + two-stage DPG algorithm
- @concepts/stochastic-calculus-foundations.md — continuous-time control background
- @concepts/partial-observation-stochastic-control.md — sibling K117 execution/control research lane
- @sources/arxiv-tt-dac-ps-optimal-execution-2606.08379-2026-06-10.md — fully observed execution RL contrast

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Deterministic Policy Gradient for Learning Equilibrium in Time-Inconsistent Control Problems |
| **Authors** | Guo, Huang, Yu (Berkeley / HK PolyU) |
| **arXiv** | 2606.11798 |
| **sha256** | `7b95e3b7b925cd2fe4d1e90a9ae23835232c4bf62719cdc26c7bb38b8769ff85` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2606.11798-deterministic-policy-gradient-for-learning-equil.pdf` |
| **Retrieved** | 2026-06-16 |
| **Read status** | read (abstract + §1 motivation + two-stage reformulation sketch) |

## Narrative

Continuous-time **model-free RL** for **subgame-perfect Nash equilibrium** in time-inconsistent control — mean-variance portfolio, non-exponential discounting, state-dependent risk aversion.

**Why stochastic policies fail here:** extended exploratory HJB is coupled; Gibbs-measure sampling is hard in continuous time; entropy regularization alters the targeted problem (approximation error for diffusion control).

**Core move:** reformulate via extended HJB into an equivalent **two-stage fixed-point** problem:

| Stage | Task |
|-------|------|
| 1 | Given auxiliary functions → learn optimal policy in auxiliary **time-consistent** problem via **deterministic policy gradient (DPG)** |
| 2 | Given policy → inner fixed-point / martingale characterization to update auxiliary functions |

Repeat actor-critic style across stages → unified equilibrium learner without entropy regularization.

**Theory:** mild assumptions + convergence of inner fixed-point iterations. **Empirics:** mean-variance portfolio management + optimal tracking under non-exponential discounting.

**Cemini posture:** **REFERENCE** — no public code. Steal **problem framing** for equity execution research (time-inconsistent objectives vs naive dynamic programming). Pairs with K117 partial-observation control and K110 TT-DAC-PS execution RL as a **control-theory vocabulary** layer, not a prod install.

## Snippets

> "We develop a continuous-time model-free reinforcement learning algorithm to learn deterministic equilibrium policies in general time-inconsistent control problems." [Source: arxiv-2606.11798-deterministic-policy-gradient-for-learning-equil.pdf abstract]

> "The choice of deterministic policy seems a suitable alternative in general time-inconsistent control problems… we can circumvent the previous technical gaps stemming from entropy regularization." [Source: arxiv-2606.11798-deterministic-policy-gradient-for-learning-equil.pdf §1]

> "Prominent examples include the nonlinear functional of expectations such as the mean-variance criterion for portfolio management, the subjective non-exponential discounting adopted by the decision maker…" [Source: arxiv-2606.11798-deterministic-policy-gradient-for-learning-equil.pdf §1]
