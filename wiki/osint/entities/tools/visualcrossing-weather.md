---
title: "Visual Crossing Weather API"
type: entity
tags: [tool, weather-api, vendor, cemini-prod-candidate, k37]
keywords: [visualcrossing, weather, adopt, three-surface-eval]
related:
  - sources/evaluating-urls-system-integration.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-05-11
updated: 2026-05-11
---

## Relations
- `@sources/evaluating-urls-system-integration.md` — source evaluation brief (URL 3)
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied
- `@concepts/cemini-license-posture.md` — license posture context

## Raw Concept

- **Repo / URL**: `visualcrossing.com/weather-api`
- **Tier (per source brief)**: **Adopt**
- **License**: Free tier permits commercial use (per source brief; verify before prod commit)

## Narrative

Enterprise-grade meteorological API with unified RESTful endpoint covering realtime + multi-day forecasts + ~50-year history. Delivers ~100 distinct meteorological elements.

### Integration vector

Adopt as the baseline weather ingestion in Cemini. Free tier permits commercial use; 50yr historical depth supports multi-decade backtesting. Implement as an MCP tool for analyst nodes.

### Risks

Cost-scaling: exceeding 1,000 records/day triggers $0.0001/record. Strict rate-limiting + Redis caching required if LangGraph polls multiple markets simultaneously.

[Source: Evaluating Urls System Integration.docx, URL 3]
