---
title: 'Deep Hedging with Reinforcement Learning: A Practical Framework for Option Risk Management'
type: source
tags: [pdf, rl-marl, deep-hedging, options-derivatives]
keywords: [deep-hedging, reinforcement-learning, actor-critic, GAE, option-overlay, transaction-costs, SPX, SPY, Sharpe]
related:
  - concepts/rl-marl-research.md
  - concepts/options-derivatives.md
maturity: validated
read_status: deep-read
created: 2026-04-27
updated: 2026-05-16
---

## Relations

- @concepts/rl-marl-research.md — cluster hub for RL/MARL research in the Cemini corpus
- @concepts/options-derivatives.md — RL deep-hedging applied to equity-index option exposure; option-surface features (ATM IV, term-structure slope, 25-delta skew) used as state

## Raw Concept

- **Original title**: Deep Hedging with Reinforcement Learning: A Practical Framework for Option Risk Management
- **Author(s)**: Travon Lucius (BlackRock), Christian (Chip) Koch Jr, Jacob Starling, Julia Zhu, Miguel Urena (Emory), Carrie Hu (Emory). November 2025. arXiv:2512.12420v1 [q-fin.PM], 13 Dec 2025
- **Type**: PDF
- **Location**: research for cemini/Deep Hedging with Reinforcement Learning.pdf
- **Retrieved**: 2026-04-27
- **Length**: 9p
- **Read status**: deep-read
- **Cluster**: rl-marl

## Narrative

This paper builds a reproducible "deep hedging" stack in which an RL agent learns to size an equity-index option-overlay position under realistic frictions, extending the deep-hedging paradigm of Buehler et al. (2019) but emphasizing auditability over a black-box policy. The agent hedges a normalized option-implied equity exposure (one unit of underlying delta, offset via SPY) by trading the index ETF; the option surface and macro variables enter only as **state information**, not as a pricing engine.

**Method.** A deterministic `HedgingEnv` builds a daily SPX/SPY panel from 2005 onward (18,018 trading days, IV fields populated on 96% of rows). State is a `window x features` matrix of economically motivated, interpretable features — ATM IV at 30d/91d, term-structure slope, 25-delta skew, VIX, 10-year yield, and realized/historical volatilities — normalized using train-split statistics only. Forward returns are aligned to the action timestamp to eliminate look-ahead bias. The reward is cost-aware and scaled to basis points: per-step PnL is `p_t = a_t R_{t+1} - c_t` with proportional cost `c_t = kappa|a_t - a_{t-1}|`, plus an Almgren-Chriss-style slippage hook (linear-quadratic price impact) kept available but with nonlinear terms zeroed in the reported runs. The policy is a compact two-layer 256-unit MLP outputting a squashed-Gaussian action, trained with an entropy-regularized actor-critic using generalized advantage estimation (GAE), gamma=0.99, gradient clipping, cosine LR schedule.

**Results.** On a fixed walk-forward split (train <= 2017, validation 2018-19, test >= 2020) the GAE policy posts deterministic Sharpe of 0.48 / 0.77 / 0.50 (train/valid/test), with standalone overlay-equity test drawdown inside roughly -3% and controlled turnover. Only the GAE overlay has a 95% (Newey-West + block-bootstrap) test-Sharpe interval strictly above zero; the authors stop short of claiming statistical dominance over long SPY since confidence bands overlap. A 50/50 GAE-plus-long-SPY blend lifts test Sharpe to ~0.65 (vs ~0.22 for SPY alone) while cutting annualized volatility from ~14.6% to ~10%. The overlay adds the most value in high-VIX regimes and the COVID/post-2022 test windows.

**Relevance to Cemini.** A directly transferable blueprint for a RL hedging overlay on an existing equity allocation: leak-free environment design, basis-point cost-aware rewards, surface/macro features instead of Greeks, and an explicitly auditable compact policy. The reward module is designed to be swapped for drawdown- or CVaR-penalized objectives — a natural fit for the Kelly/CVaR risk engine. Open-source code: github.com/tlucius16/deep-hedging-rl.

## Snippets

> "Per-step PnL is `p_t = a_t R_{t+1} - c_t` and we scale the reward as `r_t = 10^4 p_t` (basis points) to keep gradients well behaved." [Source: Deep Hedging with Reinforcement Learning.pdf p.3]

> "Across the 2005–2023 walk-forward split the trained policy keeps post-cost Sharpe positive, keeps the standalone overlay-equity test drawdown within roughly -3%, and achieves the best trade-off when 50% of capital is allocated to the agent and 50% to long SPY." [Source: Deep Hedging with Reinforcement Learning.pdf p.1]

> "Only the GAE overlay has an interval that sits entirely above zero; all rule-based baselines and the ML surrogate have confidence bands that straddle zero. Although the GAE interval lies entirely above zero, it still overlaps with that of the long-SPY benchmark, so we interpret the evidence as supporting a reliable positive Sharpe for the overlay rather than formal statistical dominance over long SPY." [Source: Deep Hedging with Reinforcement Learning.pdf p.6]
