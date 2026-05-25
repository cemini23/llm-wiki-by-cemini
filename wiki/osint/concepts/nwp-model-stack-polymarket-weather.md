---
title: NWP model stack by region — Polymarket weather market selection
type: concept
tags: [concept, weather-trading, polymarket, nwp, ecmwf, hrrr, icon, operational-meteorology, k66]
keywords: [ecmwf, gfs, hrrr, icon-d2, arome, ukmo, gem, jma, ensemble, regional models, polymarket cities]
related:
  - sources/alterego-eth-xgboost-nwp-polymarket-models-2026-05-25.md
  - concepts/nwp-bias-correction-ml-weather-trading.md
  - concepts/ensemble-weather-forecasting.md
  - concepts/polymarket-weather-trading-strategy.md
  - entities/data-sources/open-meteo.md
  - entities/tools/graphcast.md
maturity: draft
created: 2026-05-25
updated: 2026-05-25
---

## Relations

- @sources/alterego-eth-xgboost-nwp-polymarket-models-2026-05-25.md — K66 Post 2 catalog
- @concepts/ensemble-weather-forecasting.md — ensemble → distribution for bucket markets
- @entities/data-sources/open-meteo.md — practical API for many listed models

## Raw Concept

Operational playbook: **ECMWF anchor** + **regional best model** per Polymarket city geography; prefer **ensemble** (ICON-D2 EPS) when resolving binary threshold markets near the strike.

## Narrative

### Regional matrix [TENTATIVE — @AlterEgo_eth single source]

| Region | Primary adds | Notes |
|--------|--------------|-------|
| **Global** | ECMWF, ECMWF AIFS, GFS, ICON-Global | Baseline for any city |
| **US/Canada** | HRRR, GEM, GFS | HRRR hourly 3km short-range |
| **Europe** | ICON-EU, AROME, UKMO | UKMO for London/N Europe |
| **Central EU** | ICON-D2, ICON-D2 EPS | EPS for threshold binaries |
| **Asia** | JMA-GSM, JMA-MSM | MSM for Japan vicinity |
| **MENA/Africa** | ECMWF + GFS | Weak regional alt |

### Decision rule

1. Start **ECMWF** (5–10d skill leader per author).
2. Layer **regional** model for city (e.g. HRRR for US metros).
3. If ensemble available and market is **binary near threshold** → use **distribution**, not deterministic point.

### Cemini mapping

Open-Meteo already multiplexes many NWPs — this concept is the **selection policy** atop harvesters, not a new data vendor. Wire into weather analyst prompts + offline bias-correction features (@concepts/nwp-bias-correction-ml-weather-trading.md).

**GraphCast / neural NWPs** (@entities/tools/graphcast.md) are out of scope for this post but may supersede regional deterministic models long-term [NEEDS VERIFICATION 2026-05-25].

## Snippets

> "Always start with ECMWF as your anchor. Then layer in the regional model that covers your city." [Source: @AlterEgo_eth.docx, K66]
