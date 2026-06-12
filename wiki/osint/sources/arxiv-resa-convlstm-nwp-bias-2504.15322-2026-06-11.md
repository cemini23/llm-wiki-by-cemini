---
title: ReSA-ConvLSTM — systematic NWP bias correction (arXiv 2504.15322)
type: source
tags: [source, arxiv, weather, nwp, bias-correction, machine-learning]
keywords: [2504.15322, ReSA-ConvLSTM, ECMWF, ERA5, bias-correction, weather-forecasting]
related:
  - concepts/ensemble-weather-forecasting.md
  - concepts/polymarket-weather-bot-methodology-taxonomy.md
  - sources/trading-posts-compilation-9-2026-06-12.md
maturity: draft
read_status: skimmed
created: 2026-06-11
updated: 2026-06-11
---

## Relations

- @concepts/ensemble-weather-forecasting.md — ML bias-correction layer in NWP stack
- @concepts/polymarket-weather-bot-methodology-taxonomy.md — weather PM bot research chain

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | How to systematically develop an effective AI-based bias correction model? |
| **arXiv** | 2504.15322 |
| **sha256** | `61dea6723c18ab00957f20d8a265fc081be306028e819192b066778264277a7c` |
| **Location** | `cemini-librarian:/opt/cemini-bulk/research/2504.15322v1.pdf` |
| **Retrieved** | 2026-06-11 |
| **Read status** | skimmed — abstract, architecture components |

## Narrative

**ReSA-ConvLSTM** maps ECMWF forecasts → ERA5 reanalysis for T2m, U10/V10, SLP using: dynamic climatological normalization, ConvLSTM with temporal causality, residual self-attention. **41 years** global data; up to **~20% RMSE reduction** vs operational ECMWF at 1–7 day horizons. Lightweight (**10.6M** params); cross-variable retraining ~85% faster.

**Cemini mapping:** REFERENCE for **Polymarket weather bot** bias-correction research — complements ensemble-weather concept; not wired to prod weather quoter. No code adoption in K111.

## Snippets

> "Achieving up to 20% RMSE reduction over 1–7 day forecasts compared to operational ECMWF outputs."

> — [Source: 2504.15322v1.pdf Abstract, retrieved 2026-06-11]
