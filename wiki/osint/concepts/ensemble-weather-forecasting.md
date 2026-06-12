---
title: Ensemble weather forecasting
type: concept
tags: [concept, alt-data, weather, methodology]
keywords: []
related:
  - sources/3-17-competition-research.md
  - sources/3-19-alternative-data-for-prediction-markets-research.md
  - sources/3-19-kalshi-trading-strategy-research.md
  - entities/data-sources/open-meteo.md
  - entities/platforms/kalshi.md
  - concepts/polymarket-weather-trading-strategy.md
  - entities/tools/polyweather.md
  - entities/tools/suislanchez-polymarket-kalshi-weather-bot.md
  - entities/tools/graphcast.md
  - sources/alterego-eth-xgboost-nwp-polymarket-models-2026-05-25.md
  - concepts/nwp-model-stack-polymarket-weather.md
  - concepts/nwp-bias-correction-ml-weather-trading.md
  - concepts/polymarket-lp-weather-market-discovery.md
  - sources/arxiv-resa-convlstm-nwp-bias-2504.15322-2026-06-11.md
  - sources/trading-posts-compilation-9-2026-06-12.md
maturity: validated
created: 2026-04-23
updated: 2026-06-11
---

## Relations

- @sources/3-17-competition-research.md
- @sources/3-19-alternative-data-for-prediction-markets-research.md
- @sources/3-19-kalshi-trading-strategy-research.md
- @entities/data-sources/open-meteo.md
- @entities/platforms/kalshi.md
- @concepts/polymarket-weather-trading-strategy.md — K60 weather PM strategy
- @entities/tools/polyweather.md — EMOS/DEB calibration reference (AGPL, methodology only)
- @entities/tools/suislanchez-polymarket-kalshi-weather-bot.md — 31-member GFS ensemble implementation reference
- @concepts/nwp-model-stack-polymarket-weather.md — K66: when to use ICON-D2 EPS etc. for threshold binaries
- @sources/alterego-eth-xgboost-nwp-polymarket-models-2026-05-25.md — K66: distribution vs deterministic for PM weather
- @concepts/polymarket-lp-weather-market-discovery.md — LP on temperature bins (orthogonal to ensemble edge)
- @sources/arxiv-resa-convlstm-nwp-bias-2504.15322-2026-06-11.md — K111 ReSA-ConvLSTM ECMWF→ERA5 bias correction (~20% RMSE gain)

## Raw Concept

Synthesized across 3 source(s) in the Cemini research corpus that reference this concept directly or by equivalent terminology.

## Narrative

**Ensemble weather forecasting** is the practice of combining outputs
from multiple numerical weather prediction (NWP) models to produce a
probability distribution over the forecast variable, rather than a
point forecast. Cemini uses it as the primary signal for Kalshi
weather event contracts (temperature buckets, precipitation
thresholds, hurricane landfall).

**[TENTATIVE — 2026-04-24 Track C audit]** Only step 1 (Open-Meteo ingestion) is real; the statistical pipeline from step 2 onward is not built. Gumbel fit: 0 hits. Multi-model ensemble (ECMWF/GFS/ICON/MetNo/JMA with per-model weights): 0 hits. No evidence Kalshi weather contracts are actually quoted from Gumbel-fit probabilities. `WEATHER_ALPHA_LIVE=true` env gate means weather signals default to neutral/gated off. Ticket (**P2**): *Ship the ensemble-fit + Gumbel + Kalshi weather-contract quoting loop* — only the first link of the chain is built. Gap memo: `briefs/track-c-walk-results.md`.

### The pipeline per the 3-19 Kalshi strategy research
1. **Open-Meteo ingestion** `[CONFIRMED 2026-04-24]` — Pull ECMWF IFS, GFS, ICON, MetNo, JMA forecasts for the target
   lat/lon at each Kalshi contract's resolution time via Open-Meteo. *Real: `scrapers/open_meteo_harvester.py`, `scrapers/open_meteo_client.py`, `tests/test_open_meteo_harvester.py`, `docker/Dockerfile.weather`. Step 24 (Visual Crossing Weather) completed per `CLAUDE.md`. Note: harvester pulls Open-Meteo, which internally serves forecasts — but code does not explicitly ensemble multiple NWP models with per-model weights.*
2. **Gumbel fit** `[RETRACTED 2026-04-24]` — ~~Fit a **Gumbel extreme-value distribution** to the ensemble
   values — preferred over Gaussian because extreme-temp and
   precipitation-threshold contracts resolve on tail events.~~ *0 hits in code.*
3. **Per-contract probability integration** `[RETRACTED 2026-04-24]` — ~~Compute the Kalshi-contract-specific probability by integrating
   the Gumbel fit over the contract's resolution bucket.~~ *Depends on step 2; not built.*
4. **AS-logit weather quotes** `[RETRACTED 2026-04-24]` — ~~Pass through an Avellaneda-Stoikov market-making model in logit
   space to produce bid/ask quotes.~~ *Generic logit_pricing engine exists but is not wired to weather-contract Gumbel fits.*
5. **Kelly-fractional + CVaR sizing** `[TENTATIVE 2026-04-24]` — Size via Kelly-fractional + CVaR cap. *Kelly real; CVaR cap not enforced as a gate — see @concepts/game-of-attrition-doctrine.md.*

### Why Gumbel, not Gaussian
Kalshi contracts bucket at 5°F or precipitation-in-quarter-inch
granularity; at the resolution edges the ensemble distribution is
skewed and Gaussian tails underweight the actual resolution
probability. Gumbel captures the right-tail reasonably well with only
two parameters, which keeps the fit stable on 30–50 ensemble members.

## Snippets

*(populate as source stubs are deep-read.)*
