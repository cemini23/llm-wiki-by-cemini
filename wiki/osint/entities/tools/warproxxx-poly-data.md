---
title: warproxxx poly_data — Polymarket historical trades dataset (GPL-3.0)
type: entity
tags: [entity, tool, polymarket, dataset, wallet-analytics, reference-only, gpl, k64]
keywords: [poly_data, warproxxx, trades-csv, polars, wallet-screening, gpl-3]
related:
  - sources/trading-posts-farxxxxx-hermes-koroush-2026-05-24.md
  - sources/gemini-dr-wave5b-osint-2026-04-30.md
  - concepts/polymarket-wallet-alpha-pipeline.md
  - concepts/prediction-market-historical-analysis.md
  - concepts/cemini-license-posture.md
  - entities/platforms/polymarket.md
maturity: draft
created: 2026-05-24
updated: 2026-05-24
---

## Relations

- @sources/trading-posts-farxxxxx-hermes-koroush-2026-05-24.md — K64 Post 1 walkthrough
- @sources/gemini-dr-wave5b-osint-2026-04-30.md — Wave 5B Reject (GPL-3.0; MIT pyproject metadata drift)
- @concepts/polymarket-wallet-alpha-pipeline.md — wallet screen pattern
- @concepts/cemini-license-posture.md — license-metadata-discrepancy example

## Raw Concept

Open dataset of Polymarket trades (~86M rows cited K64). **GPL-3.0** [CONFIRMED 2026-05-24, ~1.9k★]. Cemini: **reference / clean-room patterns only** — wallet aggregation logic, not codebase import.

## Narrative

### K64 usage pattern (@farxxxxx1)

Polars `scan_csv` → per-`maker` aggregates (count, win rate, sum PnL) → filter → export top wallets for “whale check” in agent loop.

### Verdict: **Reference-only (Reject Adopt)**

Same posture as Wave 5B. Replicate analytics on Cemini-owned data (pmxt orderbook history, Data-API) under MIT/Apache tooling.

## Snippets

> "Every trade ever made on Polymarket. Every wallet." [Source: K64 posts.docx, 2026-05-24]
