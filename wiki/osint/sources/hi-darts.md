---
title: 'Hi-DARTS: Hierarchical Dynamically Adapting Reinforcement Trading System'
type: source
tags: [pdf, rl-marl, k49]
keywords: [Hi-DARTS, Hierarchical, Dynamically, Adapting, Reinforcement, Trading, System, PPO, multi-agent, adaptive-frequency]
clusters: [rl-marl]
related:
  - concepts/rl-marl-research.md
  - concepts/marl-trading-architecture.md
maturity: validated
read_status: deep-read
created: 2026-04-27
updated: 2026-05-16
---

## Relations

- @concepts/rl-marl-research.md — RL/MARL research cluster hub for the Cemini corpus
- @concepts/marl-trading-architecture.md — synthesis concept: Hi-DARTS anchors the hierarchical volatility-gated-execution pattern

## Raw Concept

- **Original title**: Hi-DARTS: Hierarchical Dynamically Adapting Reinforcement Trading System
- **Author(s)**: Hoon Sagong (Hongik University), Heesu Kim (Sungkyunkwan University), Hanbeen Hong (Hankuk University of Foreign Studies)
- **Type**: PDF (arXiv 2509.12048)
- **Location**: research for cemini/Hi-DARTS.pdf
- **Retrieved**: 2026-04-27
- **Length**: 6p
- **Read status**: deep-read
- **Cluster**: rl-marl

## Narrative

Conventional automated trading systems run at a fixed operating frequency, which is computationally wasteful during calm markets and too slow to react during volatile ones. Hi-DARTS proposes a two-layer hierarchical multi-agent RL architecture that adapts its decision frequency to market conditions. The top layer — a "Time Frame Allocator" meta-agent — reads real-time market data plus reward feedback and selects which specialized lower-layer "Time Frame Agent" (trained at 1-minute, 10-minute, or 1-hour resolution) should trade. Each agent is a PPO policy with a 2-hidden-layer MLP; the allocator receives a log-return reward `R = ln(V_current / V_previous)` while individual agents receive a `tanh`-bounded normalized-profit reward. Agents are trained independently on same-resolution data only, so each specializes to its timescale.

Training used AAPL data (2013–2022 train, 2023 validation, Jan 2024–May 2025 test) from WRDS, on a single V100. In back-testing Hi-DARTS produced a 25.17% cumulative return with a 0.75 Sharpe ratio and -25.49% max drawdown — beating AAPL buy-and-hold (12.19%, Sharpe 0.35), SPY (20.01%, Sharpe 0.58), and every single-frequency agent in isolation (the standalone 1-minute agent lost 8.06%). Volatility-quartile analysis confirmed the allocator learned the intended behavior: 1-minute agent usage rose from ~0% in the calmest quartile to 1.4% in the most volatile, while 1-hour usage fell from ~13.7% to ~7.5%. The work is a proof-of-concept; the planned third "Stock Selector" layer and a high-frequency override mechanism are future work.

**Cemini relevance**: Hi-DARTS is a directly relevant RL trading architecture for Cemini's MAPPO/RL stack — a concrete worked example of hierarchical multi-agent PPO with a meta-agent that gates execution frequency on volatility, plus a reusable reward-shaping pair (bounded per-trade profit + log-return portfolio reward).

## Snippets

> "Hi-DARTS utilizes a meta-agent to analyze market volatility and dynamically activate specialized Time Frame Agents for high-frequency or low-frequency trading as needed." [Source: Hi-DARTS.pdf p.1]

> "During back-testing on AAPL stock from January 2024 to May 2025, Hi-DARTS yielded a cumulative return of 25.17% with a Sharpe Ratio of 0.75. This performance surpasses standard benchmarks, including a passive buy-and-hold strategy on AAPL (12.19% return) and the S&P 500 ETF (SPY) (20.01% return)." [Source: Hi-DARTS.pdf p.1]

> "when the market moved from the least volatile quartile to the most fluctuating quartile, the allocation of 1 minute agents was increased from 0% to 1.4%, while the 1 hour agent deployment decreased from 13.7% to 7.5%." [Source: Hi-DARTS.pdf p.4]
