---
title: "aisuite"
type: entity
tags: [tool, xsp, llm-routing, k195, extract]
keywords: [aisuite, Andrew Ng, multi-provider, MIT]
related:
  - sources/eval-revenue-opportunity-analysis-2026-07-25.md
  - concepts/xsp-lane-trading-framework.md
  - concepts/wiki-tooling-evaluation.md
maturity: draft
created: 2026-07-25
updated: 2026-07-25
---

## Relations

- @sources/eval-revenue-opportunity-analysis-2026-07-25.md
- @concepts/xsp-lane-trading-framework.md
- @concepts/wiki-tooling-evaluation.md

## Raw Concept

Phase-0 K195 Extract. https://github.com/andrewyng/aisuite

## Narrative

| Field | Value |
|-------|-------|
| **License** | MIT `[CONFIRMED]` |
| **Tier** | Extract |
| **Local** | `.local/adopts/aisuite` (~11MB) |
| **Fit** | Unified provider API for XSP/PM signal eval hot-swap (rate-limit / latency failovers) |

Do not rewrite CeminiSuite LLM clients wholesale — extract routing pattern into existing adapters.
