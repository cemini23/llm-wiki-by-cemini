---
title: NWP bias correction via ML — error-target models for prediction-market weather
type: concept
tags: [concept, weather-trading, polymarket, kalshi, nwp, xgboost, machine-learning, k66]
keywords: [bias correction, xgboost, metar, ecmwf, gfs, model spread, station-level, prediction error]
related:
  - sources/alterego-eth-xgboost-nwp-polymarket-models-2026-05-25.md
  - entities/tools/aruneshdev-kalshi-weather-xgboost.md
  - concepts/polymarket-weather-trading-strategy.md
  - concepts/ensemble-weather-forecasting.md
  - concepts/nwp-model-stack-polymarket-weather.md
  - entities/data-sources/open-meteo.md
  - entities/people/coldmath-polymarket.md
  - sources/alterego-eth-coldmath-weather-deconstruction-2026-05-24.md
  - concepts/polymarket-weather-bot-methodology-taxonomy.md
  - sources/alterego-eth-five-weather-methodologies-2026-05-27.md
maturity: draft
created: 2026-05-25
updated: 2026-05-27
---

## Relations

- @sources/alterego-eth-xgboost-nwp-polymarket-models-2026-05-25.md — K66 Post 1
- @entities/tools/aruneshdev-kalshi-weather-xgboost.md — reference implementation (CONDITIONAL-GO)
- @concepts/polymarket-weather-trading-strategy.md — Gamma + station mapping + Kelly
- @sources/alterego-eth-coldmath-weather-deconstruction-2026-05-24.md — top wallet likely uses similar multi-model + bias correction [TENTATIVE]

## Raw Concept

Predict **NWP error** (observed − forecast) with gradient-boosted trees using station, season, synoptic, model-spread, and recent METAR — then apply correction before mapping to Polymarket temperature bins.

## Narrative

### Why not raw ECMWF → probability

Naive bots pipe a single NWP run into a bucket probability. That ignores **systematic biases** (summer afternoon warm bias in city X, day-of-week drift, model spread signal). @AlterEgo_eth argues narrow **1°C bins** need corrected means, not raw globals.

### Feature families (K66)

- Per-station / season historical bias
- **Model spread** across ECMWF/GFS/HRRR (disagreement as uncertainty feature)
- Calendar / diurnal time features
- **Recent METAR** for nowcasting correction

### Training data bar

≥**2 years** METAR per station + archived NWP (ECMWF/GFS/HRRR). NOAA ISD is free; alignment is the engineering cost. Cemini Track C already has Open-Meteo harvest — gap is **labeled error dataset + offline trainer**, not another scraper.

### Prod posture

- **Steal-from** (clean-room), not pip-install AruneshDev (no license).
- Complements @entities/tools/suislanchez-polymarket-kalshi-weather-bot.md ensemble edge and @entities/tools/polyweather.md calibration theory.
- Pairs with @concepts/nwp-model-stack-polymarket-weather.md for which NWP feeds enter the error model.

## Snippets

> "Treat NWP models as a baseline and uses XGBoost to predict their error." [Source: @AlterEgo_eth.docx, K66]
