---
title: Lo–MacKinlay variance ratio test — random-walk specification check
type: concept
tags: [concept, quant-finance, market-efficiency, variance-ratio, random-walk, backtest-hygiene, k68]
keywords: [variance-ratio, lo-mackinlay, market-efficiency, autocorrelation, random-walk, heteroskedasticity-consistent, crsp, backtest-sanity]
related:
  - sources/lo-mackinlay-1988-variance-ratio.md
maturity: validated
created: 2026-05-26
updated: 2026-05-26
clusters: [quant-finance, market-microstructure]
---

## Relations

- @sources/lo-mackinlay-1988-variance-ratio.md — canonical source (Lo & MacKinlay 1988)

## Raw Concept

What prompted this page: K68 ingest of `LoMacKinlay1988.pdf` — the standard reference for variance-ratio market-efficiency testing, needed as an explicit wiki primitive for backtest discipline and agent-evaluation alignment.

## Narrative

The **variance ratio test** compares multi-period return variance to scaled one-period variance. Under a random walk with i.i.d. increments, **VR(q) = 1** for every horizon **q**. Empirical VR **> 1** indicates positive serial correlation (momentum); **< 1** indicates mean reversion.

Lo and MacKinlay (1988) showed widespread rejection of the random walk for U.S. equities—especially smaller stocks—using weekly CRSP data. The test remains the workhorse **specification check** because it is simpler than estimating full autocorrelation vectors and has well-studied asymptotic distributions (including heteroskedasticity-robust forms).

### Operational recipe (Cemini)

1. Compute log returns \(r_t\) on the series under test (strategy PnL, factor portfolio, or single-name benchmark).
2. For horizons \(q \in \{2,4,8,13,26\}\) (weeks) or trading-day analogues, compute **VR(q)** with the paper's overlap convention (document which variant in backtest logs).
3. If VR departs from 1 at conventional significance, **do not** describe the strategy as "unpredictable noise"; document the autocorrelation structure or adjust benchmarks.
4. Pair with **unit-root / stationarity** checks in @concepts/time-series-arima-garch-framework.md before fitting predictive models.

### Prediction-market caveat

Polymarket and Kalshi prices are bounded probabilities with event resolution. VR on **probability changes** is still informative for **autocorrelation in belief updates** but does not map 1:1 to CRSP equity results—always label venue and horizon.

## Snippets

> VR(q) = Var(r_t^{(q)}) / (q · Var(r_t)); under a random walk, VR(q) = 1 for all q. [Source: LoMacKinlay1988.pdf — Lo & MacKinlay 1988]

> Use VR as a mandatory pre-live diagnostic on any equity signal stream before promoting backtest Sharpe to prod briefs. [CONFIRMED — Cemini K68 ingest policy]
