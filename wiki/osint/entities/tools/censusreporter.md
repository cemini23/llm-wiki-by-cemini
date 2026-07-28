---
title: Census Reporter (censusreporter)
type: entity
tags: [tool, genealogy, census, k175, extract]
keywords: [ACS, PostgreSQL schema, US census, demographic staging]
related:
  - sources/gemini-gpuology-genealogy-business-analysis-2026-07-20.md
  - concepts/gpuology-genealogy-agent-kit.md
  - sources/eval-url-revenue-and-project-analysis-2026-07-20.md
  - sources/eval-github-revenue-journalism-geo-2026-07-28.md
  - concepts/computational-genealogy-archival-automation.md
  - entities/tools/steve-morse-census-tools.md
maturity: draft
created: 2026-07-20
updated: 2026-07-28
---

## Relations
- @concepts/gpuology-genealogy-agent-kit.md — product strategy (K176)

- @sources/eval-url-revenue-and-project-analysis-2026-07-20.md — K175 Extract
- @sources/eval-github-revenue-journalism-geo-2026-07-28.md — K202 Extract reaffirm (FIND geo xref)
- @concepts/computational-genealogy-archival-automation.md — US census staging module
- @entities/tools/steve-morse-census-tools.md — address → ED browse; Census Reporter = schema/API patterns

## Raw Concept

Open stack (originally Knight News Challenge) for wrangling ACS / census aggregates — PostgreSQL schemas + Python wrappers. Eval: blueprint for family-tree **US census staging**, not a replacement for NARA image browse.

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | [censusreporter/censusreporter](https://github.com/censusreporter/censusreporter) |
| **License** | MIT [CONFIRMED 2026-07-20] |
| **Stars / push** | ~821★ · pushed 2026-07-05 [CONFIRMED] |
| **Verdict** | **GO (extract)** — ingestion schemas / API patterns for demographic staging |
| **Routing** | family-tree · GPUOLOGY US pack |
| **Not for** | Proving a specific ancestor alone — still need ED images + vitals |

### Phase-0 (2026-07-20)

| Field | Value |
|-------|-------|
| **Clone** | `/tmp/k175-censusreporter-audit` (111 MB) |
| **SPDX** | MIT [CONFIRMED] |
| **Verdict** | **GO (extract)** |
| **Risk** | Full web app stack — steal schemas/API patterns only; do not run as genealogy SaaS |

Complements Steve Morse ED Finder: Morse finds the page; Census Reporter patterns help structure tables once extracted. Report: `.local/reports/k175-phase0-2026-07-20.md`.

## Snippets

> PostgreSQL schemas + Python wrappers for ACS/historical census aggregation. [Source: @sources/eval-url-revenue-and-project-analysis-2026-07-20.md]
