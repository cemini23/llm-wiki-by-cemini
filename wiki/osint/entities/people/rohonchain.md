---
title: "@RohOnChain (Roan) — Backend developer, quant-framework series author"
type: entity
tags: [entity, person, quant-trader, polymarket, hft-execution, prediction-markets, time-series, markov-chains, k55]
keywords: [rohonchain, roan, backend-developer, hft-execution, quant-framework-series, markov-chain-trading, time-series-arima-garch, neural-network-signals, polymarket-systems]
related:
  - sources/trading-posts-2-time-series-openhuman-conflict-detector-lp-tactics-2026-05.md
  - sources/trading-posts-ai-workflow-polymarket-markov-2026-05.md
  - sources/posts-prediction-markets-quant-frameworks-2026-05-21.md
  - concepts/time-series-arima-garch-framework.md
  - concepts/markov-regime-switching-models.md
maturity: draft
created: 2026-05-20
updated: 2026-05-21
---

## Relations

- @sources/trading-posts-2-time-series-openhuman-conflict-detector-lp-tactics-2026-05.md — K55 Post 1 (Time Series ARIMA/GARCH)
- @sources/trading-posts-ai-workflow-polymarket-markov-2026-05.md — K49 ingest source (Markov chain trading framework)
- @sources/posts-prediction-markets-quant-frameworks-2026-05-21.md — K56 Post 8 is a re-share of @RohOnChain's time-series article already ingested in K55 (cross-referenced for source-handle completeness; no new content)
- @concepts/time-series-arima-garch-framework.md — synthesized concept (this batch)
- @concepts/markov-regime-switching-models.md — synthesized concept (K49)

## Raw Concept

Backend developer / quantitative trader publishing a "Quant Framework" series on prediction-market trading. Two ingested posts (K49 Markov chains, K55 time-series ARIMA/GARCH) with a planned third (neural networks for signal generation). High-quality, code-included, mathematically literate. Author of the **32-tool cheat sheet for Polymarket bots** referenced by other K55 creators (Posts.docx Post 2 cross-reference).

## Narrative

### Handle

X / Twitter: **@RohOnChain** (first name "Roan", per his own bio)

### Stated background

> "I'm Roan, a backend developer working on system design, HFT-style execution, and quantitative trading systems. My work focuses on how prediction markets actually behave under load. For any suggestions, thoughtful collaborations, partnerships DMs are open." [Source: Posts 2.docx — Post 1]

### Quant Framework series

| Topic | Status | Wiki concept |
|---|---|---|
| **Markov Chains for regime detection** | Published, K49 ingested | @concepts/markov-regime-switching-models.md |
| **Neural Networks for signal generation** | Published (referenced; not yet ingested) | — |
| **Time Series ARIMA + GARCH** | Published, K55 ingested | @concepts/time-series-arima-garch-framework.md |

The three layers are **designed to compose**: regime detection (Markov) + signal generation (NN) + position sizing on volatility regime (GARCH). Closing prompt of Post 1 (K55) explicitly explores GARCH × Markov agreement/disagreement as a multi-model orchestration pattern.

### Other public output

- **32-tool cheat sheet for Polymarket bots** — referenced by @MatiasScalbi in K55 Posts.docx Post 2; @LunarResearcher 2-week mass-built bot tooling thread also lifts from this list. → Worth ingesting separately if the source thread is retrievable.

### Why Cemini cares

- **Recurring high-quality source**: the three-part quant-framework series is internally cross-referenced and complete. Each post anchors a real Cemini-applicable concept.
- **Genuine technical depth**: unlike many Polymarket creators, the code in his posts is runnable (verified — `yfinance` + `statsmodels` + `arch` for the time-series post; `numpy` + `hmmlearn` for the Markov post).
- **Multi-model orchestration pattern**: the GARCH × Markov agreement test is a portable insight, not a Polymarket-specific tactic.

### Cemini fit

- **Reference**, like other K49 / K55 author entities. Content is the value, not the person; but recording the author as an entity makes cross-batch attribution clean.
- **Neural Networks signal-generation post** is the missing third piece; worth tracking for a future ingest.
