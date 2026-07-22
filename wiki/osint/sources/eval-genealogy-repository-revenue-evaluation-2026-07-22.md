---
title: "Genealogy Repository Revenue Evaluation (2026-07-22)"
type: source
tags: [source, tool-eval, genealogy, atto, k190]
keywords: [revenue-eval, Atto, GEDCOM, license-override]
related:
  - concepts/wiki-tooling-evaluation.md
  - concepts/gpuology-genealogy-agent-kit.md
  - concepts/computational-genealogy-archival-automation.md
  - concepts/active-project-research-routing.md
  - entities/tools/genea-app.md
  - entities/tools/open-genealogy.md
  - entities/tools/wikitree-dynamic-tree.md
  - entities/tools/topola-viewer.md
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
- @entities/tools/genea-app.md
- @entities/tools/open-genealogy.md
- @entities/tools/wikitree-dynamic-tree.md
- @entities/tools/topola-viewer.md

## Raw Concept

| Field | Value |
|-------|-------|
| **Filename** | `Genealogy Repository Revenue Evaluation.docx` |
| **sha256** | `026e964f24d0d2e79b217dc33aa89927c3360ee8b199b40e85bb1975f5668323` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/Genealogy Repository Revenue Evaluation.docx` |
| **Theme** | GEDCOM parsers, WikiTree, visualization, OSINT genealogy frameworks |

## Narrative

Tool-eval batch (v10.3 Atto/genealogy lens). **Never trust eval license claims** — `gh api` overrides below. Pass/Context/UNAVAILABLE aggregated here (no stub farm).

### Integrate (post-override)

| Repo | Confirmed license | Posture |
|------|-------------------|---------|
| genea-app/genea-app | MIT | **Integrate GO** — browser GEDCOM app |
| DigitalArchivst/Open-Genealogy | CC-BY-NC-SA-4.0 | **Watch** — NC blocks commercial Atto (eval Integrate overturned) |
| PeWu/topola-viewer | Apache-2.0 | Reinforce existing entity (eval claimed MIT — wrong) |

### Extract

| Repo | Confirmed license | Posture |
|------|-------------------|---------|
| RobPavey/wikitree-sourcer | MIT | Extract — large; entity only this batch (no clone >40MB git) |
| wikitree/wikitree-dynamic-tree | MIT | **Extract GO** — adopted |
| rootsdev/roots-search | MIT | Watch stale 2017 |
| sedelmeyer/family-genealogy-database | NOASSERTION | Watch — no SPDX |
| trasta298/keifu | MIT | Watch — ~125MB skip clone |
| The-Osint-Toolbox/Ancestry-Genealogy-OSINT | NOASSERTION | Watch OSINT checklist |

### Watch / overturn

| Repo | Confirmed license | Posture |
|------|-------------------|---------|
| wikitree/wikitree-browser-extension | MIT | Watch |
| oh-kay-blanket/family-plot | GPL-3.0 | Watch GPL |

GeneGenie.Gedcom C# Context only. Prefer genea-app + topola for Atto viz.

## Snippets

License report: `.local/reports/k190-license-gh-2026-07-22.txt`. Phase-0: `scripts/adopt_k190_phase0.sh`.
