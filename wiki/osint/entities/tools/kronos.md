---
title: "Kronos — financial time-series foundation model (Watch: licence unstated, Qlib assumption)"
type: entity
tags: [tool, model, forecasting, time-series, watch, guruwatcher]
keywords: [kronos, financial foundation model, ohlcv tokenization, qlib, autoregressive forecasting]
related:
  - sources/eval-multi-wiki-link-revenue-v10.10-batch-c-2026-11-02.md
maturity: draft
created: 2026-11-02
updated: 2026-11-02
---

## Raw Concept

Surfaced by @sources/eval-multi-wiki-link-revenue-v10.10-batch-c-2026-11-02.md, URL 8, **Watch** tier. Routed to GuruWatcher and xsp-killer.

The question this page answers: **is a pretrained candlestick model worth pointing at a watch list?**

## Narrative

### What it is

`shiyu-coder/Kronos` — a two-stage financial foundation model pretrained on **45+ global exchanges**.

The mechanism is the interesting part: it **quantises continuous multi-dimensional OHLCV candlesticks into hierarchical discrete tokens**, then forecasts autoregressively with a Transformer. Treating a candlestick as a token rather than as five numbers is what lets a language-model architecture apply to price data at all.

### Why it is in Watch, not Extract

Three blockers, all from the report:

1. **Qlib daily-equity assumptions.** The pipeline is built around a daily equity panel. GuruWatcher watches newsletters and filings; xsp-killer trades options. Neither is a daily equity cross-section, and adopting the model means adopting its data shape.
2. **Licence SPDX not stated.** Unverified.
3. **The demo pipeline has been stale since 2026-07-04.** A demonstration that is not maintained is not evidence the model still runs.

The report's condition is correct: **XSP shadow backtesting before any routing.** Run it against the actual instrument and horizon, offline, and compare to the incumbent — not against its own paper.

### What would change the verdict

- A stated licence.
- A maintenance signal on the demo pipeline.
- A shadow result on XSP or on the actual watch targets that beats the current baseline.

Nothing else. Popularity on a leaderboard is not on that list.

### The honest framing

A pretrained model over candlestick tokens has no access to the thing a newsletter watch is actually about — what a person wrote. It is a price-path model. Pointing it at GuruWatcher would be solving a different problem than the one GuruWatcher has.

Its natural home, if it has one here, is xsp-killer: a price-path question on an instrument xsp-killer already trades.

### Status

Watch. Nothing installed, nothing run.

## Snippets

> "Introduces a two-stage financial foundation model (pre-trained on 45+ global exchanges) that quantizes continuous multi-dimensional OHLCV candlesticks into hierarchical discrete tokens before autoregressive Transformer forecasting." — report, URL 8

> "License: NOT FOUND — license SPDX is not explicitly stated in the retrieved repository metadata." — report, URL 8

## Dead Ends

- **Pointing a price-path model at a text-watch problem.** GuruWatcher asks what a person wrote. Kronos answers what a price did.
- **Trusting an unmaintained demo.** The pipeline has been stale since 2026-07-04.
