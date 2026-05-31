---
title: "RMATS — recursive multi-agent portfolio under geopolitical uncertainty (arXiv:2605.25311)"
type: source
tags: [source, arxiv, multi-agent, portfolio, geopolitical-risk, drawdown, k87]
keywords: [rmats, recursive-coordination, cvar, hmm-regime, kalman-filter, geopolitical-risk-score, etf-universe, drawdown-control]
clusters: [rl-marl, portfolio-strategy]
related:
  - concepts/marl-trading-architecture.md
  - concepts/portfolio-strategy.md
  - concepts/rl-marl-research.md
  - concepts/llm-agent-systems.md
  - sources/tradingagents.md
  - sources/arxiv-drl-portfolio-sac-2605.17307.md
maturity: validated
read_status: skimmed
created: 2026-05-30
updated: 2026-05-30
---

## Relations

- @concepts/marl-trading-architecture.md — typed AgentMessage recursive coordination vs fixed sequential pipelines (TradingAgents contrast)
- @concepts/portfolio-strategy.md — monthly ETF rebalancing with explicit drawdown objective
- @concepts/rl-marl-research.md — multi-agent + RL reward shaping cluster
- @sources/tradingagents.md — cited baseline architecture; RMATS claims convergence-guaranteed recursion as differentiator
- @sources/arxiv-drl-portfolio-sac-2605.17307.md — sibling RL portfolio WFO study (return-maximizing vs RMATS capital-preservation posture)

## Raw Concept

- **Title**: Recursive Multi-Agent Trading System: Iterative Optimized Portfolio Strategy Under Geopolitical Uncertainty
- **Authors**: Jing Yang, Yichao Wu, Jianan Liu, Penghao Liang, Mengwei Yuan, Xianyou Li, Weiran Yan — APAM 2026 (5-page ACM format)
- **Type**: arXiv preprint — arXiv:2605.25311
- **Submitted**: 2026-05-25
- **Retrieved**: 2026-05-30 (Tier-2 sweep `@sweeps/2026-05-30.md`, Tier-B)
- **Pages**: 5 (conference short paper)
- **Read status**: skimmed (full paper)
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/2605.25311_rmats-geopolitical-multi-agent-trading.pdf`

## Narrative

**RMATS** (Recursive Multi-Agent Trading System) coordinates Sentiment, Report, Analysis, and Risk agents via **typed message passing** until portfolio weights converge (median **2 rounds**, 74.1% within r ≤ 2). Analysis agent uses HMM regime classification + Kalman signal fusion; Risk agent uses CVaR estimation, geopolitical stress tests, and circuit-breaker overrides. Monthly rebalance on **24 ETFs** (US sectors, intl equity, fixed income, commodities) + SPY benchmark; 10 bps costs.

**Test window Jan 2023–Mar 2025 (561 days)** — strong bull market (SPY ≈ +60%). RMATS: **MDD 9.62%** vs MVO 15.49% and FinBERT proxy 15.28%; **lowest event-period loss in 3/5** geopolitical stress windows (Israel-Hamas +1.15% only positive). Trade-off: **Sharpe −0.297**, ann. return 0.22% — defensive architecture penalized in AI-bull regime. Authors report limitations honestly: sentiment agent uses **market proxies not live FinBERT**; short test period.

**Cemini relevance:** Pattern for **macro/geopolitical risk gating** on portfolio sleeves — recursive agent debate with formal convergence criterion vs `@sources/tradingagents.md` fixed debate rounds. Steal-from for RiskAgent CVaR + circuit-breaker wiring into conductor macro regime. Not deployable as-is (ETF toy universe, proxy sentiment).

## Snippets

> "RMATS achieves a maximum drawdown of 9.62%, lower than MVO (15.49%) and FinBERT Sentiment (15.28%), and exhibits the lowest event-period drawdown in 3 of 5 geopolitical stress scenarios tested."
> — [Source: 2605.25311_rmats-geopolitical-multi-agent-trading.pdf p.1]

> "The recursive protocol achieves a median convergence of 2 rounds, with 74.1% of steps completing within r ≤ 2 … aggregate weight delta decreases from 0.165 at r = 1 to 0.007 at r = 2, a 95.9% reduction."
> — [Source: 2605.25311_rmats-geopolitical-multi-agent-trading.pdf p.4]

> "The negative Sharpe ratio (−0.297) deserves direct discussion. The 2023–2025 test period was characterized by unusually strong equity market performance … an environment where defensive architectures are systematically penalized."
> — [Source: 2605.25311_rmats-geopolitical-multi-agent-trading.pdf p.4]
