---
title: Time Magazine Labs babynames (SSA)
type: entity
tags: [tool, genealogy, entity-resolution, k175, extract]
keywords: [SSA baby names, name frequency, fuzzy match priors]
related:
  - sources/gemini-gpuology-genealogy-business-analysis-2026-07-20.md
  - concepts/gpuology-genealogy-agent-kit.md
  - sources/eval-url-revenue-and-project-analysis-2026-07-20.md
  - concepts/computational-genealogy-archival-automation.md
maturity: draft
created: 2026-07-20
updated: 2026-07-20
---

## Relations
- @concepts/gpuology-genealogy-agent-kit.md — product strategy (K176)

- @sources/eval-url-revenue-and-project-analysis-2026-07-20.md — K175 Extract
- @concepts/computational-genealogy-archival-automation.md — entity resolution priors (alongside Double Metaphone)

## Raw Concept

Node scripts + SSA historical baby-name frequencies. Eval: year/state name-probability priors to weight ambiguous OCR / spelling variants during entity resolution.

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | [TimeMagazineLabs/babynames](https://github.com/TimeMagazineLabs/babynames) |
| **License** | MIT [CONFIRMED 2026-07-20] |
| **Stars / push** | ~654★ · last push 2022-12 [CONFIRMED] |
| **Verdict** | **GO (extract)** — frequency tables as soft priors only |
| **Routing** | family-tree · GPUOLOGY entity-resolution pack |
| **Caveat** | US SSA bias — weak for Italian given names / Latin parish forms; combine with Italian onomastic lists separately |

### Phase-0 (2026-07-20)

| Field | Value |
|-------|-------|
| **Clone** | `/tmp/k175-babynames-audit` (169 MB) → `~/Desktop/family/research/tools/babynames/` |
| **SPDX** | MIT [CONFIRMED] |
| **Verdict** | **GO (extract)** |
| **Risk** | US SSA bias — soft priors only; weak for Italian/Latin parish names |

Never auto-merge on name frequency alone — tag `[TENTATIVE]` until a primary act confirms. Report: `.local/reports/k175-phase0-2026-07-20.md`.

## Snippets

> Aggregate decennial naming frequencies → probability matrix for ambiguous transcriptions. [Source: @sources/eval-url-revenue-and-project-analysis-2026-07-20.md]
