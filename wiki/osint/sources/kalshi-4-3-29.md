---
title: "PredictionMarketBench: A SWE-bench-Style Framework for Backtesting Trading Agents on Prediction Markets"
type: source
tags: [pdf, llm-agents, time-series, crypto, prediction-markets]
clusters: [llm-agents, time-series, crypto, prediction-markets]
related:
  - entities/platforms/kalshi.md
  - entities/platforms/polymarket.md
maturity: validated
created: 2026-04-23
updated: 2026-04-23
---

## Relations

- @entities/platforms/kalshi.md
- @entities/platforms/polymarket.md

## Raw Concept

- Original title: PredictionMarketBench: A SWE-bench-Style Framework for Backtesting Trading Agents on Prediction Markets
- Authors: Avi Arora, Malpani (co-author — full name in paper)
- Affiliation: arXiv preprint (academic team)
- Type: PDF, research paper (arXiv preprint)
- Location: research for cemini/kalshi 4 3:29.pdf
- Length: ~20+ pages
- Retrieved: 2026-04-23
- Publication date: 2025 (arXiv preprint)
- Read status: deep-read
- Primary cluster: time-series
- All clusters: llm-agents, time-series, crypto, prediction-markets

## Narrative

The authors build a SWE-bench-style evaluation harness for LLM trading agents on prediction markets. A task is a historical Kalshi/Polymarket contract; the agent receives the contract description plus a cutoff time's information set (news, past price history, public data) and must produce a position. Ground truth is contract resolution. The paper reports baselines: GPT-4.1-nano, a Bollinger-bands price-rule baseline, and several LLM configurations with tool-use (news retrieval, search).

Core finding is that *vanilla* LLMs underperform a naive Bollinger baseline on most categories — they either chase momentum or produce uninformative medians near 50%. With tool-use for news retrieval, performance improves materially on news-driven contracts (politics, events) but not on weather/sports. The paper emphasizes that PredictionMarketBench is intended to be a shared benchmark, not a proof of LLM alpha; it is explicit that current LLMs are below the bar on most markets.

This is a useful benchmark artifact more than a trading discovery. Its value for the Cemini suite is (a) a ready-made eval harness format that can be adopted, (b) quantified baselines showing where LLMs fail, (c) a reminder that LLM-driven prediction-market bots should be evaluated on a frozen historical set, not ad-hoc live trading logs.

## Key findings

- SWE-bench-style harness: historical prediction-market contracts as agent tasks, resolution as ground truth.
- Vanilla GPT-4.1-nano underperforms a Bollinger-bands price baseline on most contract categories.
- Tool-use (news retrieval) helps materially on news-driven contracts, not on weather/sports.
- The benchmark is presented as a standard, not as evidence that LLMs have alpha.
- Reusable harness format for any LLM trading agent evaluation (applicable to Cemini agent evals).

## Snippets

- **abstract** — "We present a SWE-bench-style framework for backtesting trading agents on prediction markets" — the artifact is the benchmark, not a new model.
- **baselines** — Bollinger-bands beat GPT-4.1-nano on most contract categories — strong null-result reminder.
- **discussion** — "Current LLMs do not show alpha on prediction markets in our setup" — clean, honest limitation statement.
