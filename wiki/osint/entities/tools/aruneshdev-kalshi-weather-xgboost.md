---
title: AruneshDev Kalshi weather XGBoost — NWP error-correction reference
type: entity
tags: [entity, tool, weather-trading, kalshi, polymarket, xgboost, steal-from, k66]
keywords: [aruneshdev, automated-trading-system-kalshi-weather-model, xgboost, metar, ecmwf, gfs, bias correction]
related:
  - sources/alterego-eth-xgboost-nwp-polymarket-models-2026-05-25.md
  - sources/multi-wiki-tool-eval-22url-2026-05-26.md
  - concepts/nwp-bias-correction-ml-weather-trading.md
  - concepts/polymarket-weather-trading-strategy.md
  - concepts/cross-venue-arbitrage-pattern.md
  - entities/tools/suislanchez-polymarket-kalshi-weather-bot.md
  - entities/data-sources/open-meteo.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-05-25
updated: 2026-05-26
---

## Relations

- @sources/alterego-eth-xgboost-nwp-polymarket-models-2026-05-25.md — K66 @AlterEgo_eth endorsement
- @sources/multi-wiki-tool-eval-22url-2026-05-26.md — K68 duplicate listing (URL 22) confirming no-license posture unchanged
- @concepts/nwp-bias-correction-ml-weather-trading.md — ML-on-NWP pattern host
- @entities/tools/suislanchez-polymarket-kalshi-weather-bot.md — higher-maturity dual-venue weather steal-from (~403★)

## Raw Concept

GitHub: `AruneshDev/Automated-Trading-System-Kalshi-Weather-Model`. XGBoost predicts **forecast error** (not temperature directly) with station/season features + METAR. K60 v4 cluster listed as **thin/stale**; K66 @AlterEgo_eth reframes as best public **bias-correction** reference for narrow Polymarket bins.

## Narrative

### Phase-0 (2026-05-25)

| Signal | Value |
|--------|-------|
| Stars | ~7 |
| Last push | 2025-04-08 |
| License | **None** (no LICENSE file) |
| Structure | data collection / features / train / inference + notebooks |

**Verdict: CONDITIONAL-GO (steal-from patterns only)** — do not vendor the repo until license clarified. Clean-room: XGBoost error target, METAR short-term correction, model-spread features, Kalshi→Gamma swap per @concepts/polymarket-weather-trading-strategy.md.

**vs suislanchez:** suislanchez = ensemble + Brier + cross-venue scan; AruneshDev = **supervised bias correction** on deterministic NWP — complementary steal-from axes.

### Cemini integration sketch

1. Harvest METAR + Open-Meteo historical NWP (@entities/data-sources/open-meteo.md).
2. Train per-station error models (batch offline on laptop/librarian — not prod hot path).
3. At inference: corrected μ/σ → bin probabilities for Gamma weather markets → existing Kelly path.

## Snippets

> "XGBoost regressor trained to predict temperature error" [Source: @AlterEgo_eth.docx via K66, 2026-05-25]
