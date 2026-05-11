---
title: "BettingOnWeather — Prediction Market Strategy Hub"
type: entity
tags: [tool, prediction-markets-strategy, kalshi, polymarket, reference-only, k38]
keywords: [bettingonweather, reference-only, three-surface-eval]
related:
  - sources/link-evaluation-brief-trading-stack.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-05-11
updated: 2026-05-11
---

## Relations
- `@sources/link-evaluation-brief-trading-stack.md` — source evaluation brief (URL 29)
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied
- `@concepts/cemini-license-posture.md` — license posture context

## Raw Concept

- **Repo / URL**: `bettingonweather.com`
- **Tier (per source brief)**: **Reference-only**
- **License**: Educational website / reference content

## Narrative

Educational + strategic hub for weather-prediction-market participants. Details mechanics, fee structures, and settlement sources (NOAA feeds) for Kalshi + Polymarket. Web calculators for net-profit modeling accounting for platform fees.

### Integration vector

Reference-only — essential reading for defining the hard mathematical limits of the algorithmic trading risk engine. No executable software integration available.

### Risks

Fee structures change frequently — hardcoding 7% Kalshi cap or 1.5% Polymarket withdrawal fee guarantees eventual orchestrator failure. Verify dynamically via exchange APIs in prod.

[Source: Link Evaluation Brief Trading Stack.docx, URL 29]
