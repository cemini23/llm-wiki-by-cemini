---
title: Market memory and Hurst regime — trend vs mean-reversion before model choice
type: concept
tags: [concept, quant, regime, hurst, mean-reversion, trend-following, k67, phosphenq]
keywords: [hurst-exponent, market-memory, regime-classification, trend-vs-mean-reversion, phosphenq]
related:
  - sources/trading-posts-compilation-38-2026-05-26.md
  - sources/posts-prediction-markets-quant-frameworks-2026-05-21.md
  - concepts/monte-carlo-permutation-test-mcpt.md
  - concepts/koroushak-discretionary-trading-curriculum.md
  - entities/people/phosphenq.md
  - sources/arxiv-2608.16749-rough-volatility-across-assets-2026-08-18.md
maturity: draft
created: 2026-05-26
updated: 2026-05-26
---

## Relations

- @sources/trading-posts-compilation-38-2026-05-26.md — Post 27 primary
- @concepts/monte-carlo-permutation-test-mcpt.md — **after** backtest validation; this is **before** model selection
- @entities/people/phosphenq.md — author
- @concepts/koroushak-discretionary-trading-curriculum.md — discretionary regime heuristics

## Raw Concept

Before fitting Kalman filters, running MCPT, or choosing Poisson/KL on a market: classify whether the series' **memory** supports **trend-following** or **mean-reversion**. @phosphenq (K67 Post 27) advocates a single statistic (Hurst-style framing) computable in ~40 lines of Python, with live examples on VIX, SPX, BTC.

## Narrative

### Failure mode

Running mean-reversion in a trend regime (and vice versa) destroys months of gains in weeks — both strategies can be "correct" architecturally but wrong on **memory**.

### Workflow position

```
Regime (Hurst/memory) → strategy family → backtest → MCPT validation
```

Complements @concepts/monte-carlo-permutation-test-mcpt.md (is this backtest real?) — does not replace it.

### Cemini relevance

- Optional pre-filter on any systematic sleeve (crypto, vol indices, prediction-market price paths **per event**).
- Pairs with Koroush discretionary **environment checklist** — one formal, one heuristic.

## Snippets

> "Before you pick a model, before you run a backtest, there is a question almost nobody measures: does this market even have the kind of memory your strategy assumes it has?" [Source: Posts.docx K67 Post 27, @phosphenq]
