---
title: "flint-chart (Microsoft) — MCP chart language for AI agents"
type: entity
tags: [tool, k231, guruwatcher, mcp, visualization]
keywords: [flint-chart, flint, Vega-Lite, ECharts, Discord charts, MCP server]
related:
  - sources/eval-url-revenue-opportunity-2026-08-11.md
  - concepts/wiki-tooling-evaluation.md
  - sources/eval-project-evaluation-revenue-2026-08-11.md
maturity: draft
created: 2026-08-11
updated: 2026-08-11
phase_0_verdict: "GO Extract 2026-08-11 (MIT, ~26MB)"
---

## Relations

- @sources/eval-project-evaluation-revenue-2026-08-11.md

- @sources/eval-url-revenue-opportunity-2026-08-11.md — GO Extract (GuruWatcher)
- @concepts/wiki-tooling-evaluation.md

## Raw Concept

- **Repo**: `github.com/microsoft/flint-chart`
- **License**: MIT [gh api override; eval flagged verify — confirmed]
- **Tier**: Extract
- **Primary fit**: GuruWatcher — Discord chart MCP
- **Phase-0**: `.local/adopts/flint-chart` ~80MB

## Narrative

Flint is a visualization intermediate language letting AI agents reliably generate polished charts from simple text specs. `flint-chart-mcp` server turns raw financial data into native static PNG/SVG charts for GuruWatcher Discord alert channels — eliminating manual charting on Macro Charts and ledger reconciliations.

**Constraints:** **alert-only, never orders**; never auto-rewrite `watches.json`; latency budget — chart generation must not stall time-sensitive price/level webhook dispatch.
