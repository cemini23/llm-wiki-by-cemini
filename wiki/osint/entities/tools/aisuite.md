---
title: "aisuite"
type: entity
tags: [tool, xsp, llm-routing, k195, k198, extract, atto]
keywords: [aisuite, Andrew Ng, multi-provider, MIT]
related:
  - sources/eval-revenue-opportunity-analysis-2026-07-25.md
  - sources/eval-revenue-stack-url-evaluation-2026-07-28.md
  - concepts/xsp-lane-trading-framework.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/gpuology-genealogy-agent-kit.md
  - entities/tools/book-to-skill.md
  - entities/tools/agent-governance-toolkit.md
maturity: draft
created: 2026-07-25
updated: 2026-07-28
---

## Relations

- @sources/eval-revenue-opportunity-analysis-2026-07-25.md — K195 Extract
- @sources/eval-revenue-stack-url-evaluation-2026-07-28.md — K198 re-Extract → Atto/GuruWatcher
- @concepts/xsp-lane-trading-framework.md
- @concepts/wiki-tooling-evaluation.md
- @concepts/gpuology-genealogy-agent-kit.md
- @entities/tools/book-to-skill.md
- @entities/tools/agent-governance-toolkit.md

## Raw Concept

Phase-0 K195 Extract (still local). https://github.com/andrewyng/aisuite — MIT.

## Narrative

| Field | Value |
|-------|-------|
| **License** | MIT `[CONFIRMED]` |
| **Tier** | Extract (K195 XSP; K198 Atto/GuruWatcher failover) |
| **Local** | `.local/adopts/aisuite` (~11MB) |
| **Fit** | Unified provider API — HTR cost routing (Atto) + Discord alert reliability (GuruWatcher) + XSP signal eval hot-swap |

Do not rewrite CeminiSuite LLM clients wholesale — extract routing pattern into existing adapters. MCP support noted in K198 eval.
