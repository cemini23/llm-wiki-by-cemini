---
title: "Windy — High-Fidelity Weather Forecast API"
type: entity
tags: [tool, weather-api, vendor, kalshi-relevant, defer, k38]
keywords: [windy, com, defer, three-surface-eval]
related:
  - sources/link-evaluation-brief-trading-stack.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-05-11
updated: 2026-05-11
---

## Relations
- `@sources/link-evaluation-brief-trading-stack.md` — source evaluation brief (URL 13)
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied
- `@concepts/cemini-license-posture.md` — license posture context

## Raw Concept

- **Repo / URL**: `windy.com`
- **Tier (per source brief)**: **Defer**
- **License**: Proprietary vendor API; commercial pricing tier

## Narrative

Machine-readable weather forecast API. Map Forecast overlays + Point Forecast endpoints. 20+ meteorological parameters (wind gusts, temperature, CAPE, convective precipitation, wave heights) aggregated across multiple models. Professional tier €990/yr, 10,000 req/day cap.

### Integration vector

Defer adoption until projected Kalshi-weather trading volume + expected edge justifies the €990/yr subscription. High value for Kalshi weather markets when economics justify.

### Risks

10,000 req/day hard ceiling must be managed by LangGraph orchestrator. Proprietary vendor data terms — legal review before redistribution.

[Source: Link Evaluation Brief Trading Stack.docx, URL 13]
