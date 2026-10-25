---
title: "Prediction markets — efficiency and contract design (Wolfers–Zitzewitz)"
type: concept
tags: [concept, prediction-markets, market-efficiency, contract-design]
keywords: [prediction-market-efficiency, winner-takes-all-probability, index-mean-contract, spread-median, conditional-markets, risk-neutral-probability]
related:
  - sources/substack-rss-moontower-2026-07-08-betting-as-a-tax-on-bullshit.md
  - concepts/proper-betting-clob-prediction-markets.md
  - sources/nber-w10504-wolfers-zitzewitz-prediction-markets-2004.md
  - entities/platforms/polymarket.md
  - entities/platforms/kalshi.md
  - concepts/polymarket-microstructure-findings.md
  - concepts/prediction-market-statistical-arbitrage.md
  - concepts/instrumental-probability-learnable-alpha.md
  - sources/arxiv-instrumental-probability-hard-to-predict-2606.08209-2026-06-10.md
  - concepts/kalshi-implied-macro-belief-distributions.md
  - sources/arxiv-kalshi-macroeconomic-beliefs-2606.30040-2026-07-02.md
  - sources/arxiv-prophets-profit-prediction-markets-2607.06166-2026-07-09.md
  - sources/substack-rss-klement-2026-07-10-iran-news-bias.md
maturity: core
created: 2026-05-27
updated: 2026-10-25
---

## Relations

- @sources/nber-w10504-wolfers-zitzewitz-prediction-markets-2004.md — canonical citation
- @entities/platforms/polymarket.md — modern implementation
- @entities/platforms/kalshi.md — regulated US PM
- @concepts/polymarket-microstructure-findings.md — execution layer
- @concepts/prediction-market-statistical-arbitrage.md — when efficiency breaks

## Raw Concept

Academic grounding for **why prediction-market prices are treated as forecasts** in the wiki and Cemini stack — synthesized from NBER w10504 (K72).

## Narrative

### Efficiency prior

Liquid, well-designed PMs **aggregate dispersed information** into prices that **beat simple benchmarks** [CONFIRMED] — Wolfers & Zitzewitz (2004) meta-evidence across IEM, corporate, and sports contexts. Cemini's edge hypotheses assume **local** inefficiencies (latency, niche markets, microstructure), not global irrationality of all PM prices.

### Contract → statistic map

- **Binary / winner-take-all** (Polymarket YES mid): interpret as **P(event)** only if risk-neutral and stakes small vs wealth; correlated macro shocks break pure probability read.
- **Index-style** payoffs: **mean** forecast.
- **Spread / line markets**: **median** via even-money structure.
- **Families** of related binaries: approximate **full distribution** + uncertainty.

### Design implications for Cemini

- Backtests that treat mid as probability should document **risk-premium** and **liquidity** caveats.
- **Conditional** PM structures (if deployed) can encode regression beliefs — separate correlation from causation in narrative.
- **DARPA PAM** failure: political/compliance risk is independent of statistical efficiency — document for institutional buyers.

## Snippets

> "Market-generated forecasts are typically fairly accurate, and outperform most moderately sophisticated benchmarks." [Source: w10504.pdf abstract]
