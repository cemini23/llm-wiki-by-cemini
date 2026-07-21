---
title: CodiceFiscaleJS (lucavandro)
type: entity
tags: [tool, genealogy, italy, k175, extract]
keywords: [codice fiscale, comuni soppressi, municipality matrix, jure sanguinis]
related:
  - sources/gemini-gpuology-genealogy-business-analysis-2026-07-20.md
  - concepts/gpuology-genealogy-agent-kit.md
  - sources/eval-url-revenue-and-project-analysis-2026-07-20.md
  - sources/gemini-italian-place-name-resolution-2026-07-21.md
  - concepts/computational-genealogy-archival-automation.md
  - concepts/italian-regional-genealogy-archive-playbook.md
maturity: draft
created: 2026-07-20
updated: 2026-07-21
---

## Relations
- @concepts/gpuology-genealogy-agent-kit.md — product strategy (K176)
- @sources/gemini-italian-place-name-resolution-2026-07-21.md — K180 Belfiore PK / soppressi temporal model

- @sources/eval-url-revenue-and-project-analysis-2026-07-20.md — K175 Extract
- @concepts/computational-genealogy-archival-automation.md — geo entity resolution
- @concepts/italian-regional-genealogy-archive-playbook.md — comune / province validation

## Raw Concept

JS/TS library for Italian fiscal-code calculation that embeds a municipality matrix including **comuni soppressi** — useful for validating historical birthplaces on acts vs modern maps.

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | [lucavandro/CodiceFiscaleJS](https://github.com/lucavandro/CodiceFiscaleJS) |
| **License** | CC-BY-SA-4.0 [CONFIRMED 2026-07-20] |
| **Stars / push** | ~217★ · pushed 2026-02 [CONFIRMED] |
| **Verdict** | **GO (extract)** — geo/comune validation logic + data for regional playbook |
| **Routing** | family-tree private sprint; GPUOLOGY kit only after sharealike review |
| **NEEDS VERIFICATION 2026-07-20** | Accuracy of soppressi / border changes ~1861–1920 vs Archivio di Stato place authorities |

### Phase-0 (2026-07-20)

| Field | Value |
|-------|-------|
| **Clone** | `/tmp/k175-codice-fiscale-js-audit` (5 MB) → `~/Desktop/family/research/tools/codice-fiscale-js/` |
| **SPDX** | CC-BY-SA-4.0 [CONFIRMED] |
| **Verdict** | **GO (extract)** |
| **Risk** | `lista-comuni.js` present (~13k lines); CC-BY-SA sharealike if redistributing matrix in commercial kit |

Do **not** treat fiscal-code generation as proof of identity for living people. Use municipality tables as a **lookup**, with human confirm against the act. Report: `.local/reports/k175-phase0-2026-07-20.md`.

## Snippets

> Complete matrix of Italian municipalities including suppressed/reassigned comuni. [Source: @sources/eval-url-revenue-and-project-analysis-2026-07-20.md]
