---
title: "@AlterEgo_eth — ECMWF/GFS bias map across Polymarket weather cities"
type: source
tags: [source, alterego_eth, polymarket, weather-trading, nwp, bias-correction, k74]
keywords: [ecmwf, gfs, ukmo, cmc, gem, systematic-bias, london, paris, nyc, houston]
related:
  - entities/people/alteregoeth.md
  - concepts/nwp-bias-correction-ml-weather-trading.md
maturity: validated
read_status: deep-read
created: 2026-05-28
updated: 2026-05-28
clusters: [polymarket, weather-trading]
---

## Relations

- @entities/people/alteregoeth.md — author; eighth ingested weather artifact
- @concepts/nwp-bias-correction-ml-weather-trading.md — reinforces station/model-specific correction thesis with concrete city bias examples

## Raw Concept

- **Title**: The Complete Map of ECMWF and GFS Biases Across Major Cities on Polymarket Weather Markets
- **Author**: @AlterEgo_eth (X)
- **Type**: single long-form X post / docx export
- **Location**: `research to be indexed/@AlterEgo_eth.docx` (K74)
- **Retrieved**: 2026-05-28
- **Read status**: deep-read

## Narrative

This post argues edge in 1-degree weather binaries comes from exploiting persistent model error patterns, not trusting a single "best model" output. It frames systematic bias as directionally stable enough to price around by city and season.

### Key bias claims (single-source; treat as provisional)

- **ECMWF** often underestimates daytime heat by about 1-2 C in sunny high-pressure setups (Europe and US southwest examples).
- **GFS** often overestimates by about 0.5-1 C in the southeastern US.
- **UKMO** often underestimates by about 1-2 C in northern regions.
- **CMC/GEM** often overestimates temperatures in northern US conditions tied to snow-cover handling.

### Cemini relevance

- Supports the existing thesis that narrow-bin weather markets require station-level bias correction before sizing.
- Adds practical city examples (London, Paris, NYC, Houston) to guide where correction priors should be tested first.
- Reiterates why ensemble smoothing alone is insufficient without explicit model/station calibration.

## Snippets

> "ECMWF ... frequently underestimates daytime heat ... 1-2 C lower than reality." [Source: @AlterEgo_eth.docx, 2026-05-28]

> "GFS ... regularly overestimates temperature ... 0.5-1 C warmer than actual." [Source: @AlterEgo_eth.docx, 2026-05-28]

> "If you trade without this correction, you are every day fighting against a built-in 0.5-2 C systematic error." [Source: @AlterEgo_eth.docx, 2026-05-28]
