---
title: OANDA
type: entity
tags: [platform, forex, cfd, cemini-venue]
keywords: []
related:
  - sources/3-19-compliance-research.md
  - sources/3-19-ip-sale-research.md
  - sources/3-19-langgraph-scatter-gather-financial-analysis.md
  - sources/forex-research-3-18.md
  - concepts/carry-trade.md
  - concepts/macro-weather-regime.md
maturity: validated
created: 2026-04-23
updated: 2026-04-23
---

## Relations

- @sources/3-19-compliance-research.md
- @sources/3-19-ip-sale-research.md
- @sources/3-19-langgraph-scatter-gather-financial-analysis.md
- @sources/forex-research-3-18.md
- @concepts/carry-trade.md
- @concepts/macro-weather-regime.md

## Raw Concept

Synthesized from 4 source(s) referencing this entity across the Cemini research corpus. Category: platforms.

## Narrative

OANDA is a retail-and-institutional forex broker used by Cemini as the
primary FX execution venue. The forex research documents the full
integration: v20 REST + streaming API, tick-level price feeds persisted to
TimescaleDB hypertables, and order submission through the scatter-gather
LangGraph topology with per-pair risk limits enforced by the Kelly/CVaR
engine.

OANDA's role in the IP-sale thesis is notable: unlike Alpaca (equities-
only) or Hyperliquid (crypto-only), OANDA provides **24/5 FX coverage** on
majors and crosses, which the compliance research flags as a requirement
for the intended institutional-buyer archetype. Documented strategies
include EUR/USD carry-trade variants, GBP/JPY mean-reversion in specific
regime windows, and a Macro-Weather-gated dispersion overlay on G10
crosses.

## Snippets

*(populate as source stubs are deep-read.)*
