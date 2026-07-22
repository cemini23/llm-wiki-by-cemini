---
title: "Genealogy Tools Revenue Analysis (2026-07-22)"
type: source
tags: [source, tool-eval, genealogy, atto, k190]
keywords: [revenue-eval, Atto, GEDCOM, license-override]
related:
  - concepts/wiki-tooling-evaluation.md
  - concepts/gpuology-genealogy-agent-kit.md
  - concepts/computational-genealogy-archival-automation.md
  - concepts/active-project-research-routing.md
  - entities/tools/claude-family-history-research-skill.md
  - entities/tools/ancestry-tools.md
  - entities/tools/lineage.md
maturity: draft
read_status: read
created: 2026-07-22
updated: 2026-07-22
clusters: [k190-ingest]
---

## Relations

- @concepts/wiki-tooling-evaluation.md
- @concepts/gpuology-genealogy-agent-kit.md
- @concepts/computational-genealogy-archival-automation.md
- @concepts/active-project-research-routing.md
- @entities/tools/claude-family-history-research-skill.md
- @entities/tools/ancestry-tools.md
- @entities/tools/lineage.md

## Raw Concept

| Field | Value |
|-------|-------|
| **Filename** | `Genealogy Tools Revenue Analysis.docx` |
| **sha256** | `a7e5741d1a64c19aa86a3ec3ab957a6eb73d885de6c2e8fefcc0035ec258dbd0` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/Genealogy Tools Revenue Analysis.docx` |
| **Theme** | Python/Ruby Ancestry tooling + Claude skill |

## Narrative

Tool-eval batch (v10.3 Atto/genealogy lens). **Never trust eval license claims** — `gh api` overrides below. Pass/Context/UNAVAILABLE aggregated here (no stub farm).

### Integrate (post-override)

| Repo | Confirmed license | Posture |
|------|-------------------|---------|
| emaynard/claude-family-history-research-skill | MIT | **Integrate GO** |
| cdhorn/ancestry-tools | Apache-2.0 | **Integrate GO** (stale 2022 — still useful CSV/GEDCOM helpers) |

### Extract

| Repo | Confirmed license | Posture |
|------|-------------------|---------|
| Thimxx/pyGenealogical-Tools | GPL-3.0 | Watch GPL |
| bengarvey/lineage | MIT | **Extract GO** — D3 pedigree viz adopted |
| lrf1/ancestry_scripts | NOASSERTION | Watch |

### Watch / overturn

| Repo | Confirmed license | Posture |
|------|-------------------|---------|
| stefankroes/ancestry | MIT | Watch — Rails tree gem; not Atto stack |

Pass majority (9). Claude skill pairs with autoresearch-genealogy vault patterns.

## Snippets

License report: `.local/reports/k190-license-gh-2026-07-22.txt`. Phase-0: `scripts/adopt_k190_phase0.sh`.
