---
title: GDELT (Global Database of Events, Language, and Tone)
type: entity
tags: [data-source, alt-data, news, events]
keywords: []
related:
  - sources/3-17-git-research-pt2.md
  - sources/3-19-compliance-research.md
  - sources/3-19-ip-sale-research.md
  - sources/3-19-kalshi-trading-strategy-research.md
  - sources/3-19-langgraph-scatter-gather-financial-analysis.md
  - sources/3-29-research-4.md
  - sources/gdelt-1-3-29.md
  - sources/gdelt-4-3-29.md
  - concepts/cameo-codes.md
  - concepts/goldstein-scale.md
  - entities/frameworks/finbert.md
  - entities/data-sources/fred.md
  - entities/data-sources/finnhub.md
maturity: validated
created: 2026-04-23
updated: 2026-04-26
---

## Relations

- @sources/3-17-git-research-pt2.md
- @sources/3-19-compliance-research.md
- @sources/3-19-ip-sale-research.md — open alt-data sources (no commercial-license entanglement) cited as IP-portability advantage at acquirer transfer
- @sources/3-19-kalshi-trading-strategy-research.md — GDELT cited as adverse-shock signal that triggers Kalshi BatchCancelOrders inventory withdrawal (the 0.2x token weighting makes 100-orders/sec liquidity pull feasible on Basic tier)
- @sources/3-19-langgraph-scatter-gather-financial-analysis.md
- @sources/3-29-research-4.md
- @sources/gdelt-1-3-29.md
- @sources/gdelt-4-3-29.md — interpretable ML for macro alpha using GDELT news-sentiment features (D′ 2026-04-26)
- @concepts/cameo-codes.md
- @concepts/goldstein-scale.md
- @entities/frameworks/finbert.md
- @entities/data-sources/fred.md
- @entities/data-sources/finnhub.md

## Raw Concept

Synthesized from 5 source(s) referencing this entity across the Cemini research corpus. Category: data-sources.

## Narrative

GDELT is an open dataset cataloging global news events in near-real-time,
with rich schema covering actor identities, CAMEO event codes, Goldstein
scale intensity, and tone scores. Cemini consumes GDELT 2.0 v2 tables via
Google BigQuery exports and streams incremental updates into TimescaleDB.

Primary uses in the stack:
- **Country-instability prediction** — aggregate Goldstein deltas per
  country over rolling windows feed a Bayesian deep-learning model
  flagged in the 3-29-research-4 paper.
- **Event-driven signal overlay** — high-Goldstein-intensity events
  matched to ticker entity lists generate short-window volatility
  forecasts consumed by the options and prediction-market strategies.
- **FinBERT input corpus** — tone-tagged headlines tied to specific
  tickers are re-scored by FinBERT to produce a sentiment feature
  orthogonal to GDELT's own tone score.

## Snippets

*(populate as source stubs are deep-read.)*
