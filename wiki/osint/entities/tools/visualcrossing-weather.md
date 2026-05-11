---
title: "Visual Crossing Weather API"
type: entity
tags: [tool, weather-api, vendor, cemini-prod-candidate, k37, phase-0-conditional-go]
keywords: [visualcrossing, weather, adopt, three-surface-eval, kalshi, polymarket, interpolation]
related:
  - sources/evaluating-urls-system-integration.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
  - entities/data-sources/nws-weather-gov.md
  - entities/data-sources/open-meteo.md
  - entities/tools/wethr-net.md
maturity: validated
created: 2026-05-11
updated: 2026-05-11
phase_0_audit: CONDITIONAL-GO 2026-05-11 (backtesting-only role; interpolation gap on contract-resolution path)
adoption_status: DEFERRED 2026-05-11 (no spend now; Free tier is $0/mo so adoption gate is workstream-readiness, not budget — reactivate when Kalshi weather-contract backtest scope opens)
---

## Relations
- `@sources/evaluating-urls-system-integration.md` — source evaluation brief (URL 3)
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied
- `@concepts/cemini-license-posture.md` — license posture context
- `@entities/data-sources/nws-weather-gov.md` — ultimate Kalshi-resolution-truth source; complementary
- `@entities/data-sources/open-meteo.md` — pre-existing free backtesting alternative; less depth
- `@entities/tools/wethr-net.md` — paired Adopt for live-resolution path

## Raw Concept

- **Repo / URL**: `visualcrossing.com/weather-api`
- **Tier (per source brief)**: **Adopt**
- **License** [VERIFIED 2026-05-11]: Commercial-use rights explicitly confirmed across all four plans (Free / Metered / Professional / Enterprise) via vendor docs. Free tier = 1,000 records/day. Overage on Metered at $0.0001/record.
- **Phase-0 audit** [VERIFIED 2026-05-11]: Vendor founded 2003 (Reston VA, ~23 yrs operating); 99.9% SLA quoted across paid plans. 50+ yr historical depth confirmed; sub-hourly history paid-tier only. Source attribution = ISD + MADIS (METAR/ASOS/AWOS) + ERA5 + MERRA-2 + GHCN-D. Unified Timeline API (past/present/future), ~100 elements, 2km forecast resolution.

## Narrative

Enterprise-grade meteorological API with unified RESTful endpoint covering realtime + multi-day forecasts + ~50-year history. Delivers ~100 distinct meteorological elements. **Phase-0 verdict: CONDITIONAL-GO** — adopt with role-restricted scope.

### Integration vector

**CONDITIONAL-GO 2026-05-11** — adopt for **backtesting + climatology only**. Free tier suffices for v1 at Cemini's likely cadence (5 airports × 15-min poll = 480 records/day, under 1,000/day free cap). One-shot historical backfill (5 airports × 1 yr hourly = 43,800 records) = **~$4.38** as Metered overage. Live operation = $0/mo at this cadence.

### Critical role restriction — interpolation gap

Visual Crossing's historical data is **grid-interpolated from station proximity**, NOT station-direct (per vendor's own docs). For Kalshi/Polymarket temperature contracts that resolve on specific airport METARs (KLGA / KJFK / KMIA / etc.), interpolated history will **silently diverge** from contract-resolution truth. Do NOT use Visual Crossing on the live contract-resolution path. Use `@entities/tools/wethr-net.md` (station-direct, `logic=nws`/`wu` parameter) for live; `@entities/data-sources/nws-weather-gov.md` as ultimate resolution-truth.

### Risks

1. **Interpolation gap** — historical data is grid-interpolated, not station-direct → backtests will diverge from Kalshi resolution if used naively.
2. **Reanalysis revisions** — ERA5 + MERRA-2 sources reissue observations periodically; historical query results are not strictly reproducible.
3. **Sub-hourly paywall** — sub-hourly history (needed for intraday analysis) requires Metered plan, not Free.
4. **Cost-scaling** — 1,000 records/day Free cap; overage at $0.0001/record. Strict rate-limiting + Redis caching required if LangGraph polls multiple markets simultaneously.

[Source: Evaluating Urls System Integration.docx, URL 3; Phase-0 audit 2026-05-11]
