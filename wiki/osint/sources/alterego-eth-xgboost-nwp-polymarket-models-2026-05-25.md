---
title: "@AlterEgo_eth — XGBoost NWP bias correction + regional model stack (2 posts)"
type: source
tags: [source, alterego_eth, polymarket, weather-trading, nwp, xgboost, k66]
keywords: [aruneshdev, kalshi weather model, ecmwf, gfs, hrrr, icon, metar, bias correction, gamma api, station resolution]
related:
  - entities/people/alteregoeth.md
  - entities/tools/aruneshdev-kalshi-weather-xgboost.md
  - concepts/nwp-bias-correction-ml-weather-trading.md
  - concepts/nwp-model-stack-polymarket-weather.md
  - concepts/polymarket-weather-trading-strategy.md
  - concepts/ensemble-weather-forecasting.md
  - entities/data-sources/open-meteo.md
  - sources/alterego-eth-coldmath-weather-deconstruction-2026-05-24.md
  - entities/people/coldmath-polymarket.md
  - concepts/polymarket-weather-bot-methodology-taxonomy.md
  - sources/alterego-eth-five-weather-methodologies-2026-05-27.md
maturity: validated
read_status: deep-read
created: 2026-05-25
updated: 2026-05-27
clusters: [polymarket, weather-trading]
---

## Relations

- @entities/people/alteregoeth.md — author (sixth artifact; weather ML + NWP catalog)
- @entities/tools/aruneshdev-kalshi-weather-xgboost.md — Post 1 reference repo
- @concepts/nwp-bias-correction-ml-weather-trading.md — Post 1 synthesized pattern
- @concepts/nwp-model-stack-polymarket-weather.md — Post 2 regional model matrix
- @concepts/polymarket-weather-trading-strategy.md — parent strategy corpus
- @sources/alterego-eth-coldmath-weather-deconstruction-2026-05-24.md — prior drop used same filename (K61 ColdMath); **different posts**
- @entities/people/coldmath-polymarket.md — K61 subject; K66 bias-correction stack plausibly explains ColdMath edge [TENTATIVE]

## Raw Concept

- **Title**: `@AlterEgo_eth.docx` — 2 posts (no `Next Post:` delimiter in export; sequential @AlterEgo_eth headers)
- **Type**: X long-form posts
- **Location**: `research to be indexed/@AlterEgo_eth.docx` → `cemini-librarian:/opt/cemini-bulk/research/@AlterEgo_eth.docx` (**supersedes** K61 librarian copy)
- **Retrieved**: 2026-05-25
- **Read status**: deep-read

## Narrative

### Post 1 — XGBoost NWP error correction (Kalshi → Polymarket)

**Repo:** [AruneshDev/Automated-Trading-System-Kalshi-Weather-Model](https://github.com/AruneshDev/Automated-Trading-System-Kalshi-Weather-Model) — Phase-0: **~7★**, last push **2025-04-08**, **no LICENSE file** [CONFIRMED 2026-05-25].

**Idea:** treat ECMWF/GFS (etc.) as baseline; **XGBoost regressor predicts temperature error** per station/season/synoptic regime — not raw NWP → probability.

**Features cited:** model spread, historical bias, time features, recent METAR.

**Polymarket port (author):** swap Kalshi API → **Gamma** (`GET /markets` + details); map **resolution station** per city (KLAX, KATL, …); output bias-corrected probs → Kelly sizing.

**Hard part:** ≥2y METAR + archived ECMWF/GFS/HRRR per station; NOAA ISD free but alignment labor-intensive.

→ @concepts/nwp-bias-correction-ml-weather-trading.md, @entities/tools/aruneshdev-kalshi-weather-xgboost.md

### Post 2 — 11-model regional stack for Polymarket cities

**Workflow:** ECMWF anchor → add **regional best** model → use **ensemble** (e.g. ICON-D2 EPS) when market is binary near threshold.

| Region | Models (author list) |
|--------|----------------------|
| Global | ECMWF, ECMWF AIFS, GFS, ICON-Global |
| US/Canada | HRRR (hourly, 3km), GEM, GFS |
| Europe | ICON-EU, AROME, UKMO, ECMWF |
| Central EU | ICON-D2, ICON-D2 EPS |
| Asia | JMA-GSM, JMA-MSM, ECMWF + ICON-Global |
| MENA/Africa | ECMWF, GFS |

**Key distinction:** deterministic = point; **ensemble = distribution** — distribution drives binary threshold markets.

→ @concepts/nwp-model-stack-polymarket-weather.md

## Snippets

> "Instead of blindly trusting raw NWP outputs, the model learns how much and in which direction different models are wrong for each specific station, season and synoptic situation." [Source: @AlterEgo_eth.docx Post 1, 2026-05-25]

> "A single deterministic forecast tells you the expected value. An ensemble tells you the distribution. For binary threshold markets, the distribution is what actually matters." [Source: @AlterEgo_eth.docx Post 2, 2026-05-25]

> "You need at least 2 years of historical METAR observations per station + archived forecasts from ECMWF/GFS/HRRR." [Source: @AlterEgo_eth.docx Post 1, 2026-05-25]
