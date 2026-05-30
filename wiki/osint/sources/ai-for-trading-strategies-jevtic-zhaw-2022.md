---
title: "Artificial Intelligence for Trading Strategies (Jevtic et al. 2022)"
type: source
tags: [source, academic, machine-learning, crude-oil, zhaw, k84]
keywords: [lstm, random-forest, svm, knn, arma-garch, cross-signal-trading, market-regimes, volatility-phases]
related:
  - concepts/time-series-arima-garch-framework.md
  - concepts/markov-regime-switching-models.md
  - concepts/lo-mackinlay-variance-ratio-test.md
  - sources/ssrn-5140015-time-series-quant-finance-2025.md
maturity: draft
read_status: skimmed
created: 2026-05-30
updated: 2026-05-30
---

## Relations

- @concepts/time-series-arima-garch-framework.md — ARMA-GARCH baseline compared in thesis
- @concepts/markov-regime-switching-models.md — regime-phase performance analysis parallel
- @sources/ssrn-5140015-time-series-quant-finance-2025.md — academic time-series canon (K56)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Artificial Intelligence for Trading Strategies |
| **Author** | Danijel Jevtic, Romain Délèze, Joerg Osterrieder (ZHAW) |
| **Type** | Bachelor thesis preprint |
| **Location** | `cemini-librarian:/opt/cemini-bulk/research/AI_for_trading_strategies.pdf` |
| **arXiv** | 2208.07168 |
| **Date** | 2022-08-16 |
| **Read status** | skimmed (abstract + methods list) |

## Narrative

Empirical comparison on **crude oil**: ML models (LSTM, Random Forest, SVM regression, k-NN) vs classical **Cross Signal Trading** and **ARMA-GARCH**. Performance sliced by **market phase / volatility regime** — Random Forest showed strongest recall in high-volatility periods; k-NN failed to detect COVID shock.

**Wiki fit:** reference baseline for “ML vs classical” and **regime-conditioned backtest** discipline — not novel enough for prod brief unless ArcticDB equity/oil sleeve adds regime labels. Pairs with K58 GMM regime stress-test concept.

## Snippets

> "Random Forest, on average, made better decisions in highly volatile market periods than ordinary statistical models such as ARMA-GARCH." [Source: AI_for_trading_strategies.pdf abstract]
