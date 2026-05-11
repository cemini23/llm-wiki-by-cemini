---
title: "Wethr.net — Polymarket / Kalshi Weather Analytics"
type: entity
tags: [tool, weather-analytics, kalshi, polymarket, prediction-markets, cemini-prod-candidate, k38]
keywords: [wethr, net, adopt, three-surface-eval]
related:
  - sources/link-evaluation-brief-trading-stack.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-05-11
updated: 2026-05-11
---

## Relations
- `@sources/link-evaluation-brief-trading-stack.md` — source evaluation brief (URL 28)
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied
- `@concepts/cemini-license-posture.md` — license posture context

## Raw Concept

- **Repo / URL**: `wethr.net`
- **Tier (per source brief)**: **Adopt**
- **License**: Proprietary vendor API; pricing pending

## Narrative

Analytics platform tailored for weather prediction-market participants (Kalshi, Polymarket). Programmable API. Mathematically computes temperature probability boundaries (high/orange, max/red, public/white, min/blue curves) for prediction markets specifically.

### Integration vector

Adopt — integrate API endpoints directly into Cemini's Kalshi automated execution path. Service is mathematically optimized for prediction-market temperature probabilities = immediate algorithmic alpha that cannot be replicated internally.

### Risks

Data reliability disclaimer ("not guaranteed accurate, complete, or up-to-date") → automated trading must implement circuit breakers + fail-safes for anomalous or stale feeds. Pricing tiers obscure.

[Source: Link Evaluation Brief Trading Stack.docx, URL 28]
