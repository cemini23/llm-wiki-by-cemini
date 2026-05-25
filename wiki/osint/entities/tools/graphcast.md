---
title: GraphCast — DeepMind ML weather forecasting (Apache-2.0)
type: entity
tags: [entity, tool, weather-ml, defer, k63]
keywords: [graphcast, google-deepmind, weather-forecasting, neural, apache-2]
related:
  - sources/multi-wiki-tool-eval-36url-wiki-ingestion-2026-05-24.md
  - concepts/ensemble-weather-forecasting.md
  - concepts/polymarket-weather-trading-strategy.md
  - concepts/ensemble-weather-forecasting.md
  - concepts/nwp-model-stack-polymarket-weather.md
maturity: draft
created: 2026-05-24
updated: 2026-05-25
---

## Relations

- @sources/multi-wiki-tool-eval-36url-wiki-ingestion-2026-05-24.md — K63 URL 21 Defer
- @concepts/ensemble-weather-forecasting.md — complements ICON/GFS/ECMWF deterministic stack
- @concepts/polymarket-weather-trading-strategy.md — forecast precision bar for narrow bins

## Raw Concept

DeepMind GraphCast neural weather model (~6.7k★, Apache-2.0). K63 **Defer** — heavy GPU inference; evaluate vs Open-Meteo ensemble path before cemini-prod integration.

## Narrative

### Verdict: **Defer (Phase-0)**

Potential lift: bias-corrected global fields for station-level 1°C bin markets. Blocker: ops cost + librarian Ollama is not H100-class training/inference farm.

## Snippets

> "Defer… DeepMind weather ML." [Source: K63 eval, URL 21]
