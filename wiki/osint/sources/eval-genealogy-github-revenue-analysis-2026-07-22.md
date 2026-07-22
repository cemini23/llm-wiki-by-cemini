---
title: "Genealogy GitHub Revenue Analysis (2026-07-22)"
type: source
tags: [source, tool-eval, genealogy, atto, k190]
keywords: [revenue-eval, Atto, GEDCOM, license-override]
related:
  - concepts/wiki-tooling-evaluation.md
  - concepts/gpuology-genealogy-agent-kit.md
  - concepts/computational-genealogy-archival-automation.md
  - concepts/active-project-research-routing.md
  - entities/tools/betty.md
  - entities/tools/kekule-html.md
  - entities/tools/go-geni.md
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
- @entities/tools/betty.md
- @entities/tools/kekule-html.md
- @entities/tools/go-geni.md

## Raw Concept

| Field | Value |
|-------|-------|
| **Filename** | `Genealogy GitHub Revenue Analysis.docx` |
| **sha256** | `e24751cf68fd3aaaa561a76429df263df87633b0c8c219ddf86d0fe363b0b232` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/Genealogy GitHub Revenue Analysis.docx` |
| **Theme** | Methodology / viz / static site / historical index parsers for Atto |

## Narrative

Tool-eval batch (v10.3 Atto/genealogy lens). **Never trust eval license claims** — `gh api` overrides below. Pass/Context/UNAVAILABLE aggregated here (no stub farm).

### Integrate (post-override)

| Repo | Confirmed license | Posture |
|------|-------------------|---------|
| bartfeenstra/betty | GPL-3.0 | **Watch** — GPL product friction (eval Integrate overturned) |

### Extract

| Repo | Confirmed license | Posture |
|------|-------------------|---------|
| LondonRain/KekuleHtml | AGPL-3.0 | **Watch** — AGPL (eval Extract overturned) |
| 06Games/Historical-Record-Indexes | ODbL-1.0 | Watch data license — no product embed without counsel |

### Watch / overturn

| Repo | Confirmed license | Posture |
|------|-------------------|---------|
| dmalch/go-geni | Apache-2.0 | Watch Geni API connector — local clone kept |

12 UNAVAILABLE + Pass/Context folded. Leaflet/lifespan ideas from KekuleHtml are **methodology only** under AGPL.

## Snippets

License report: `.local/reports/k190-license-gh-2026-07-22.txt`. Phase-0: `scripts/adopt_k190_phase0.sh`.
