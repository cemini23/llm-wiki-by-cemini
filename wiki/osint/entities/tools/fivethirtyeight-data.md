---
title: FiveThirtyEight data (fivethirtyeight/data)
type: entity
tags: [tool, dfs, prediction-markets, k175, extract]
keywords: [tidy data, sports datasets, political polling, CeminiDFS]
related:
  - sources/eval-url-revenue-and-project-analysis-2026-07-20.md
  - concepts/active-project-research-routing.md
maturity: draft
created: 2026-07-20
updated: 2026-07-20
---

## Relations

- @sources/eval-url-revenue-and-project-analysis-2026-07-20.md — K175 Extract
- @concepts/active-project-research-routing.md — CeminiDFS + PM canary routing

## Raw Concept

Curated CSV/R/Python datasets (sports + politics) in tidy format. Eval: historical baselines for CeminiDFS projections and PM LP canary backtests — not a live feed.

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | [fivethirtyeight/data](https://github.com/fivethirtyeight/data) |
| **License** | CC-BY-4.0 [CONFIRMED 2026-07-20] |
| **Stars / push** | ~17.4k★ · pushed 2025-02 [CONFIRMED] |
| **Verdict** | **GO (extract)** — tidy schema discipline + historical tables |
| **Routing** | CeminiDFS (primary) · pm-canary (polling histories) |
| **Risk** | Static / low-frequency updates — structure > live P&L |

### Phase-0 (2026-07-20)

| Field | Value |
|-------|-------|
| **Clone** | `/tmp/k175-fivethirtyeight-data-audit` (422 MB; under 500 MB cap) |
| **SPDX** | CC-BY-4.0 [CONFIRMED] |
| **Verdict** | **GO (extract)** |
| **Risk** | Static CSVs — CC-BY attribution required on redistribution |

Report: `.local/reports/k175-phase0-2026-07-20.md`.

## Snippets

> Tidy snake_case datasets eliminate normalization friction for projection matrices. [Source: @sources/eval-url-revenue-and-project-analysis-2026-07-20.md]
