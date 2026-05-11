---
title: "Wethr.net — Polymarket / Kalshi Weather Analytics"
type: entity
tags: [tool, weather-analytics, kalshi, polymarket, prediction-markets, cemini-prod-candidate, k38, phase-0-go]
keywords: [wethr, net, adopt, three-surface-eval, contract-resolution, nws-logic, wu-logic, station-direct]
related:
  - sources/link-evaluation-brief-trading-stack.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
  - entities/data-sources/nws-weather-gov.md
  - entities/tools/visualcrossing-weather.md
maturity: validated
created: 2026-05-11
updated: 2026-05-11
phase_0_audit: GO 2026-05-11 (live Kalshi/Polymarket-resolution path; vendor-age risk via circuit breakers)
adoption_status: DEFERRED 2026-05-11 (no spend now; reactivate when first Kalshi weather strategy reaches paper-trade phase OR $24.99/mo budget cleared)
---

## Relations
- `@sources/link-evaluation-brief-trading-stack.md` — source evaluation brief (URL 28)
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied
- `@concepts/cemini-license-posture.md` — license posture context
- `@entities/data-sources/nws-weather-gov.md` — ultimate resolution-truth source; cross-validation + circuit-breaker fallback
- `@entities/tools/visualcrossing-weather.md` — paired Adopt for backtesting role

## Raw Concept

- **Repo / URL**: `wethr.net`
- **Tier (per source brief)**: **Adopt**
- **License** [VERIFIED 2026-05-11]: Proprietary vendor API. Open beta launched 2025-05-14 (≤12 mo operating).
- **Phase-0 audit** [VERIFIED 2026-05-11]: API v2 docs comprehensive. 30 US + international airport stations (KNYC/KLGA/KMIA/KLAX/KMDW/KDCA/KBOS confirmed — full Kalshi roster covered). **Explicit `logic=nws` vs `logic=wu` parameter** for Kalshi-mode vs Polymarket-mode resolution. Sources raw METAR + CLI/DSM + 6-hour station highs/lows — **station-direct, not interpolated**. T-group precision validation for ASOS rounding edge case. Pricing tiers verified: Pro $24.99/mo (60 req/min, 5K req/day — API access starts here), Developer $99/mo (300 req/min, 50K req/day, + Push API + Model Accuracy API). Self-declared "data not guaranteed accurate" disclaimer.

## Narrative

Analytics platform built explicitly for Kalshi + Polymarket weather contracts. Programmable API exposes `lowest_probable` / `highest_probable` bounds and contract-resolution-aligned high/low calculation logic. **Phase-0 verdict: GO** — adopt for live-trading path.

### Integration vector

**GO 2026-05-11** — integrate API endpoints directly into Cemini's Kalshi automated execution path. Use `logic=nws` for Kalshi resolution; `logic=wu` for Polymarket. **Getting this parameter wrong = silent strategy bias** (the two modes differ on rounding + time convention). Cost: Professional $24.99/mo covers 5 airports × 15-min poll cadence (480 req/day, well under Pro 5K/day limit). Scales to all 28 US stations × 15-min = 2,688 req/day (still Pro tier). Defer Developer $99/mo tier until Push streaming or Model Accuracy logic becomes part of a strategy.

### Critical implementation guidance

1. **Logic parameter is non-optional**: set `logic=nws` for every Kalshi-resolution-path call; `logic=wu` for Polymarket. Wrap in helper that fails-closed if parameter missing.
2. **Circuit breakers required** per vendor disclaimer: staleness check on `inserted_at` field + cross-validate against `lowest_probable`/`highest_probable` envelope before trading.
3. **NWS fallback**: parallel-poll `@entities/data-sources/nws-weather-gov.md` for cross-validation; fail-over to NWS if wethr.net stale or absent.

### Risks

1. **Vendor immaturity** — ≤12 mo operating; no published SLA; no status page found; single-product company. Concentration risk if vendor folds mid-trading-day.
2. **Bus factor** — Small operator (no team page, single email contact); migration burden if vendor disappears.
3. **Beta endpoints** — Precipitation API, Push API, NWS Forecasts API still marked BETA — accuracy + stability not yet guaranteed.

[Source: Link Evaluation Brief Trading Stack.docx, URL 28; Phase-0 audit 2026-05-11]
