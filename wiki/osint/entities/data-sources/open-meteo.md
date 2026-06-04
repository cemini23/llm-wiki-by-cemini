---
title: Open-Meteo
type: entity
tags: [data-source, weather, ensemble-forecasting]
keywords: [open-meteo, bias-correction-parameter, icon-gfs-ecmwf-ensemble, no-api-key-data-source]
related:
  - sources/3-17-competition-research.md
  - sources/3-19-ip-sale-research.md
  - sources/3-19-kalshi-trading-strategy-research.md
  - sources/x2-docx-polymarket-theparuchh-2026.md
  - concepts/ensemble-weather-forecasting.md
  - concepts/polymarket-weather-trading-strategy.md
  - entities/platforms/kalshi.md
  - entities/data-sources/nws-weather-gov.md
  - entities/tools/visualcrossing-weather.md
  - entities/tools/polyweather.md
  - concepts/nwp-model-stack-polymarket-weather.md
  - sources/alterego-eth-xgboost-nwp-polymarket-models-2026-05-25.md
  - concepts/nwp-bias-correction-ml-weather-trading.md
  - entities/tools/aruneshdev-kalshi-weather-xgboost.md
  - sources/stanford-avellaneda-stoikov-hf-mm-gr5-2018.md
maturity: validated
created: 2026-04-23
updated: 2026-05-29
---

## Relations

- @sources/3-17-competition-research.md
- @sources/3-19-ip-sale-research.md — zero-vendor-lock-in data-source posture (no API key, no rate limit) cited as IP-portability advantage at acquirer transfer
- @sources/3-19-kalshi-trading-strategy-research.md
- @concepts/ensemble-weather-forecasting.md
- @entities/platforms/kalshi.md
- @entities/data-sources/nws-weather-gov.md — companion / complement: Open-Meteo gives the global multi-model ensemble (ECMWF + GFS + ICON + MetNo + JMA); NWS gives the single US-government authoritative forecast and observation feed — use as the resolution-truth source when settling US-locality Kalshi weather contracts
- @entities/tools/visualcrossing-weather.md — K37 Adopt (CONDITIONAL-GO 2026-05-11); paid 50-yr historical depth complementing Open-Meteo's free shallower reanalysis. Both serve the backtesting role; choose by depth/freshness need
- @sources/x2-docx-polymarket-theparuchh-2026.md — K41 retail-bot operator's operational guide; documents `bias_correction=true` parameter claim (+30-40% accuracy) and station-vs-city-center coordinate discovery
- @entities/tools/polyweather.md — K60; also ingests Open-Meteo alongside METAR/TAF/official obs networks (AGPL product — methodology reference only)
- @concepts/polymarket-weather-trading-strategy.md — K41 strategy concept page (parallel Polymarket application of the same data source)

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

### K41 addition: `bias_correction=true` parameter — `[RETRACTED 2026-05-29]`

The K41-ingested @sources/x2-docx-polymarket-theparuchh-2026.md documents a parameter **`bias_correction=true`** on Open-Meteo's API claiming **+30-40% temperature-forecast accuracy**. Exa + official docs check (2026-05-29): the standard **Forecast API** (`/v1/forecast`) has **no** `bias_correction` query param in [Open-Meteo openapi.yml](https://raw.githubusercontent.com/open-meteo/open-meteo/main/openapi.yml); forecast output is intended for user-built post-processing pipelines. The **Climate API** exposes **`disable_bias_correction`** (boolean, default bias correction *on* against ERA5-Land) — inverse naming, different product. The +30-40% magnitude remains author-asserted and unverified. **Revenue implication:** weather bots must implement explicit bias correction (Historical Forecast archive + station truth), not flip a forecast-API toggle.

Also documented: 5 of 11 city queries had wrong default coordinates (city-center geocode vs the weather station the resolution market uses). Mitigation: pin coordinates to the resolution-truth station, not the city geocode.

## Snippets

*(populate as source stubs are deep-read.)*
