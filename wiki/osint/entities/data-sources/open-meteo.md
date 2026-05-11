---
title: Open-Meteo
type: entity
tags: [data-source, weather, ensemble-forecasting]
keywords: []
related:
  - sources/3-17-competition-research.md
  - sources/3-19-ip-sale-research.md
  - sources/3-19-kalshi-trading-strategy-research.md
  - concepts/ensemble-weather-forecasting.md
  - entities/platforms/kalshi.md
  - entities/data-sources/nws-weather-gov.md
  - entities/tools/visualcrossing-weather.md
maturity: validated
created: 2026-04-23
updated: 2026-05-11
---

## Relations

- @sources/3-17-competition-research.md
- @sources/3-19-ip-sale-research.md — zero-vendor-lock-in data-source posture (no API key, no rate limit) cited as IP-portability advantage at acquirer transfer
- @sources/3-19-kalshi-trading-strategy-research.md
- @concepts/ensemble-weather-forecasting.md
- @entities/platforms/kalshi.md
- @entities/data-sources/nws-weather-gov.md — companion / complement: Open-Meteo gives the global multi-model ensemble (ECMWF + GFS + ICON + MetNo + JMA); NWS gives the single US-government authoritative forecast and observation feed — use as the resolution-truth source when settling US-locality Kalshi weather contracts
- @entities/tools/visualcrossing-weather.md — K37 Adopt (CONDITIONAL-GO 2026-05-11); paid 50-yr historical depth complementing Open-Meteo's free shallower reanalysis. Both serve the backtesting role; choose by depth/freshness need

## Raw Concept

Synthesized from 2 source(s) referencing this entity across the Cemini research corpus. Category: data-sources.

## Narrative

Open-Meteo is an open, no-API-key weather forecasting service aggregating
multiple numerical weather prediction (NWP) ensembles — ECMWF IFS, GFS,
ICON, MetNo, JMA. Cemini uses it as the primary input to the ensemble-
weather forecasting concept that feeds Kalshi weather event-contract
strategies.

Documented integration: hourly pulls of the ensemble forecast at specific
lat/lon points corresponding to Kalshi contract locations (e.g., NYC/LAX/
Chicago temperature contracts), fit into a Gumbel extreme-value
distribution to produce a probability distribution over the contract's
resolution bucket, then converted to a fair-value price that drives
Avellaneda-Stoikov market-making quotes in logit space. No API key + no
rate limit at the volumes Cemini uses = another zero-vendor-risk data
source, consistent with the IP-sale-readiness posture.

## Snippets

*(populate as source stubs are deep-read.)*
