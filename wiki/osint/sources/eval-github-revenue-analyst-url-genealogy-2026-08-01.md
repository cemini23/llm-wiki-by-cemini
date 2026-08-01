---

title: "Eval — Revenue Analyst URL Evaluation (genealogy OS / GEDCOM / Antenati) 2026-08-01"
type: source
tags: [tool-eval, genealogy, atto, k216]
keywords: [webtrees, FamilyGem, kingraph, gedcom, AncestryLLM, Antenati]
related:
  - concepts/gpuology-genealogy-agent-kit.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/cemini-license-posture.md
  - entities/tools/tmcw-gedcom.md
  - entities/tools/ancestryllm.md
maturity: draft
created: 2026-08-01
updated: 2026-08-01
---

## Relations

- @concepts/gpuology-genealogy-agent-kit.md
- @concepts/wiki-tooling-evaluation.md
- @concepts/cemini-license-posture.md
- @entities/tools/tmcw-gedcom.md
- @entities/tools/ancestryllm.md

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Revenue Analyst URL Evaluation.docx |
| Type | tool-eval v5 |
| Retrieved | 2026-08-01 |
| sha256 | a8093e2fe7ff2089… (full in preingest) |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/osint/Revenue Analyst URL Evaluation.docx |
| read_status | deep-read |

## Narrative

20-URL genealogy OS / GEDCOM / Antenati batch. **Never trust eval SPDX** — `gh api` overrides.

| Repo | Eval tier | SPDX (gh) | Cemini verdict |
|------|-----------|-----------|----------------|
| tmcw/gedcom | Integrate | **ISC** | **GO Extract** — Phase-0 clone |
| sodejm/AncestryLLM | Integrate | **MIT** | **GO Extract** — Phase-0; human-gated Ancestry ToS |
| tomnlydhill8439/antenati-toolkit-pro-v3-app | Integrate | **GPL-3.0** | **Watch** — GPL isolate; Antenati ToS; no auto-book |
| michelesalvador/FamilyGem | Extract | **GPL-3.0** | **Watch** — GPL isolate; mobile render patterns only |
| rstacruz/kingraph | Extract | null / no LICENSE | **NO-GO** clone |
| lesnik571-lab/GenealogyDB | Extract | null | **NO-GO** |
| Gitvijay36/heritage-mender-revived | Integrate | null | **NO-GO** |
| Majsan-T/PastPaths | Extract | null / ~890MB | **NO-GO** size |
| fisharebest/webtrees | Watch | (prior GPL isolate) | Watch Access-share UI |
| Others | Pass/Context | — | Aggregate Rejects on this page |

Phase-0: `scripts/adopt_k216_phase0.sh` (gedcom, AncestryLLM, …).

## Snippets

> Tier Integrate: tmcw/gedcom — Python GEDCOM parser aligned with Atto stack. [Source: Revenue Analyst URL Evaluation.docx]
