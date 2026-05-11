---
title: "OpenWeather API — Weather Data Vendor"
type: entity
tags: [tool, weather-api, vendor, k37]
keywords: [openweather, api, defer, three-surface-eval]
related:
  - sources/evaluating-urls-system-integration.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-05-11
updated: 2026-05-11
---

## Relations
- `@sources/evaluating-urls-system-integration.md` — source evaluation brief (URL 2)
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied
- `@concepts/cemini-license-posture.md` — license posture context

## Raw Concept

- **Repo / URL**: `openweather.org`
- **Tier (per source brief)**: **Defer**
- **License**: Proprietary vendor API (license-clean for non-redistribution use)

## Narrative

Globally distributed meteorological data service. Flagship One Call API 3.0: minute-by-minute realtime, 8-day forecast, 47-year history. Includes Solar Irradiance API (GHI/DNI/DHI) and Air Pollution API.

### Integration vector

Defer adoption until a specific quantitative trading thesis (weather derivatives, energy equities) is explicitly programmed into the LangGraph orchestrator. Premature ingestion burns DB storage without generating signal.

### Risks

Vendor lock-in via proprietary JSON schemas. Pricing tiers vendor-managed.

[Source: Evaluating Urls System Integration.docx, URL 2]
