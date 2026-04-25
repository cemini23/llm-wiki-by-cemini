---
title: Kalshi
type: entity
tags: [platform, prediction-markets, exchange, cemini-venue]
keywords: []
related:
  - sources/3-10-cryptographic-research.md
  - sources/3-17-competition-research.md
  - sources/3-19-alternative-data-for-prediction-markets-research.md
  - sources/3-19-compliance-research.md
  - sources/3-19-ip-sale-research.md
  - sources/3-19-kalshi-trading-strategy-research.md
  - sources/3-29-research-4.md
  - sources/3-9-pm-research.md
  - sources/kalshi-2-3-29.md
  - sources/kalshi-3-3-29.md
  - sources/kalshi-4-3-29.md
  - sources/osint-prediction-markets-trading-architecture.md
  - concepts/favorite-longshot-bias.md
  - concepts/macro-weather-regime.md
  - concepts/ip-sale-readiness.md
  - entities/platforms/polymarket.md
  - entities/data-sources/open-meteo.md
  - concepts/ensemble-weather-forecasting.md
maturity: validated
created: 2026-04-23
updated: 2026-04-23
---

## Relations

- @sources/3-10-cryptographic-research.md
- @sources/3-17-competition-research.md
- @sources/3-19-alternative-data-for-prediction-markets-research.md
- @sources/3-19-compliance-research.md
- @sources/3-19-ip-sale-research.md
- @sources/3-19-kalshi-trading-strategy-research.md
- @sources/3-29-research-4.md
- @sources/3-9-pm-research.md
- @sources/kalshi-2-3-29.md
- @sources/kalshi-3-3-29.md
- @sources/kalshi-4-3-29.md
- @sources/osint-prediction-markets-trading-architecture.md
- @concepts/favorite-longshot-bias.md
- @concepts/macro-weather-regime.md
- @concepts/ip-sale-readiness.md
- @entities/platforms/polymarket.md
- @entities/data-sources/open-meteo.md
- @concepts/ensemble-weather-forecasting.md

## Raw Concept

Synthesized from 12 source(s) referencing this entity across the Cemini research corpus. Category: platforms.

## Narrative

Kalshi is a CFTC-regulated designated contract market (DCM) for event
contracts — US-domiciled yes/no prediction markets on outcomes ranging from
weather and macroeconomic prints to elections and regulatory events. Within
Cemini it occupies three roles:

1. **Execution venue** — the Kalshi API (REST + WebSocket) is wired through
   the LangGraph scatter-gather topology alongside Alpaca and Hyperliquid;
   position sizing flows through the Kelly/CVaR risk engine.
2. **Alternative-data generator** — intraday price series on weather and
   event contracts provide a forward-looking signal layer that's fused with
   GDELT, FRED, and Open-Meteo ensembles before being dispatched to equity
   and crypto strategies.
3. **Compliance leverage point** — Kalshi's DCM status means event-contract
   trading sits under CFTC jurisdiction, which is structurally cleaner for
   an IP-sale-to-institutional-buyer story than operating on an unregistered
   offshore exchange.

Key microstructure facts documented across the corpus: the 2024 election-
contract ruling cemented Kalshi's regulatory moat; tick sizes are \$0.01 on
binary contracts; settlement is cash-only at \$1.00/\$0.00 on resolution;
the venue exhibits a strong favorite-longshot bias that several Cemini
strategies explicitly monetize via Avellaneda-Stoikov market-making in logit
space.

## Snippets

*(populate as source stubs are deep-read.)*
