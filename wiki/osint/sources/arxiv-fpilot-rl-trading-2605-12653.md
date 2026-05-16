---
title: "Plan Before You Trade: Inference-Time Optimization for RL Trading Agents (arXiv:2605.12653)"
type: source
tags: [source, arxiv, reinforcement-learning, trading-agents, inference-time-optimization, mpc, k48]
keywords: [fpilot, inference-time-optimization, rl-trading-agent, model-predictive-control, price-forecast, portfolio-management, trademaster-dj30]
related:
  - concepts/rl-marl-research.md
maturity: validated
read_status: skimmed
created: 2026-05-15
updated: 2026-05-15
---

## Relations

- @concepts/rl-marl-research.md — RL-for-trading research; FPILOT is an inference-time-optimization technique applicable to a trained RL trading policy without retraining

## Raw Concept

- **Title**: Plan Before You Trade: Inference-Time Optimization for RL Trading Agents
- **Authors**: Eun Go, Rohan Deb, Arindam Banerjee (UIUC, per the 2026-05-15 sweep)
- **Type**: arXiv preprint — arXiv:2605.12653
- **Submitted**: 2026-05-12
- **Retrieved**: 2026-05-15 (Tier-2 arXiv sweep `@sweeps/2026-05-15.md`, Q3 #1)
- **Read status**: skimmed (abstract-level)

## Narrative

RL portfolio-management agents are normally trained then deployed as static policies with no way to use price forecasts at decision time. **FPILOT** is an inference-time optimization framework, inspired by Model Predictive Control, that folds a price forecaster into a *pre-trained* RL agent **without retraining**.

Key idea: future prices are largely independent of an individual agent's allocations, so a multi-step price trajectory can be predicted without action-conditioned rollouts — making the MPC-style planning step cheap. FPILOT is policy-agnostic (works with any policy-learning algorithm).

**Results** (TradeMaster DJ30 benchmark): consistent gains in total return, Sharpe, Sortino, and Calmar; stochastic policies benefit more than deterministic ones; gains scale with forecaster quality.

**Why it matters here**: CeminiSuite runs an RL trading stack. FPILOT is an "add a planning layer at inference" pattern — a retraining-free upgrade path. The forecaster-quality scaling result means it compounds with any improvement in the forecasting side.

## Snippets

> "Reinforcement learning agents for portfolio management are typically trained and deployed as static policies, with no mechanism for using price forecasts at inference time. We propose FPILOT [...] The framework adapts policies to forecaster predictions without retraining and demonstrates consistent improvements across multiple algorithms."
> — [Source: https://arxiv.org/abs/2605.12653 (retrieved 2026-05-15)]
