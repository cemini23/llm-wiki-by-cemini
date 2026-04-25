---
title: FRED (Federal Reserve Economic Data)
type: entity
tags: [data-source, macro, central-bank]
keywords: []
related:
  - sources/3-19-compliance-research.md
  - sources/3-19-kalshi-trading-strategy-research.md
  - sources/3-19-langgraph-scatter-gather-financial-analysis.md
  - concepts/macro-weather-regime.md
  - entities/data-sources/gdelt.md
maturity: validated
created: 2026-04-23
updated: 2026-04-23
---

## Relations

- @sources/3-19-compliance-research.md
- @sources/3-19-kalshi-trading-strategy-research.md
- @sources/3-19-langgraph-scatter-gather-financial-analysis.md
- @concepts/macro-weather-regime.md
- @entities/data-sources/gdelt.md

## Raw Concept

Synthesized from 3 source(s) referencing this entity across the Cemini research corpus. Category: data-sources.

## Narrative

FRED is the Federal Reserve Bank of St. Louis's open data portal — ~800K
US and international macro time series. Cemini consumes FRED via the
official Python client (fredapi) with daily incremental pulls persisted to
TimescaleDB. Key series used across the corpus: DFF (effective fed funds),
DGS10 (10y treasury), VIXCLS (CBOE VIX), DCOILWTICO (WTI spot), DEXUSEU,
UNRATE, CPIAUCSL.

FRED series are the backbone of the **Macro Weather regime** classifier:
SPY vs its 21-EMA / 50-SMA gates are evaluated in the context of the
current Fed stance (DFF regime) and yield-curve shape (DGS10 - DGS2). The
compliance research also highlights FRED as a zero-vendor-risk data source
— open, redistributable, with no API-terms entanglement that would
complicate the IP-sale handoff.

## Snippets

*(populate as source stubs are deep-read.)*
