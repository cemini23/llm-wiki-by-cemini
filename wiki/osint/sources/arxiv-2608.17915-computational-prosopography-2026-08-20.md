---
title: "Computational prosopography across a millennium (arXiv 2608.17915)"
type: source
tags: [arxiv, genealogy, atto, k243]
keywords: [prosopography, Fields-Medal, Wikidata, mentor-student, entity-resolution]
related:
  - concepts/atto-genealogy-agent-kit.md
  - concepts/computational-genealogy-archival-automation.md
  - entities/tools/lore.md
  - entities/tools/google-timeline-visualizer.md
  - entities/tools/whisperlivekit.md
  - sources/eval-repository-revenue-2026-08-20.md
maturity: draft
created: 2026-08-20
updated: 2026-08-20
read_status: read
---

## Relations

- @concepts/atto-genealogy-agent-kit.md — lineage/entity-resolution steal; Transkribus sole HTR
- @concepts/computational-genealogy-archival-automation.md — mentor–student graph as FIND prior
- @entities/tools/lore.md — narrative schema sibling; no living-person vitals
- @entities/tools/google-timeline-visualizer.md — maps without GPS fixtures
- @entities/tools/whisperlivekit.md — STT is not HTR
- @sources/eval-repository-revenue-2026-08-20.md — same-day Lore/timeline Extract

## Raw Concept

| Field | Value |
|-------|--------|
| Paper | arXiv:2608.17915, "Computational Prosopography across a Millennium: Mathematically Oriented Lineages Traced from the Fields Medalists" |
| Authors | Hiroyuki Chuma, Kanji Otsuka, Yoichi Sato |
| Retrieved | 2026-08-20 |
| File | `arxiv-2608.17915-computational-prosopography-across-a-millennium.pdf` |
| sha256 | `779bc7d91842fc4536a08a3c035c7c4d03185b189be7dbff0b476595dc076f6f` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.17915-computational-prosopography-across-a-millennium.pdf` |
| Type | physics.soc-ph preprint |
| Dual-ID | **OSINT K243**. Atto methodology. **No Barone names.** |

## Narrative

The authors reconstruct a mentor–student DAG from Wikidata (Mathematics Genealogy Project + MacTutor): ~470,000 assertions → 372,853 persons. Using all 64 historical Fields Medalists as a fixed tracer set, backward traversal enumerates ~25.5 million distinct paths across 57 generations.

**Concrete claim `[TENTATIVE]`:** genealogical traffic through Leibniz is an hourglass — thin upstream (5.3 paths/node) and thick downstream (53.4), ~10:1 — while Newton lies on only four of the 64 lineages. 54 of 64 lineages converge on five twelfth- and thirteenth-century Islamic and Byzantine scholars before an eleventh-century documentary boundary they call the Monastery Wall. The traversal engine is algebraically reversible: ranking decisions can be reconstructed after the fact, so tool criticism is part of the argument rather than a footnote.

Atto steal: treat entity-resolution and path enumeration as a **human-gated FIND prior**, not an auto-merge into `truth.ged`. Absence of an edge can be evidence of recording practice, not proof that a relationship never existed. Never put private pedigree, living-person vitals, or family GPS into git or Atto fixtures. Transkribus remains sole product HTR; this paper is graph methodology, not OCR.

## Snippets

> "The traversal engine is algebraically reversible, so every ranking decision it makes can be reconstructed afterward." [Source: arxiv-2608.17915 abstract]
