---
title: Italian Genealogy Software Data (Gemini DR — place / toponymy)
type: source
tags: [source, docx, genealogy, toponymy, istat, belfiore, k180, italy]
keywords: [comuni soppressi, Codice Belfiore, SISTAT, frazione, dialect phonetics, BeWeB, SIUSA, Friuli in prin]
clusters: [k180-ingest]
related:
  - concepts/italian-regional-genealogy-archive-playbook.md
  - concepts/us-italy-hometown-reveal-ladder.md
  - concepts/computational-genealogy-archival-automation.md
  - entities/tools/codice-fiscale-js.md
  - concepts/gpuology-genealogy-agent-kit.md
  - sources/gemini-italian-american-genealogy-sources-2026-07-21.md
  - sources/gemini-italian-civil-genealogy-find-playbook-2026-07-22.md
maturity: draft
read_status: read
created: 2026-07-21
updated: 2026-07-22
---

## Relations

- @entities/tools/codice-fiscale-js.md — K175 comuni/soppressi extract; Belfiore-adjacent
- @concepts/italian-regional-genealogy-archive-playbook.md — regional exception portals
- @concepts/us-italy-hometown-reveal-ladder.md — produces the messy place string this resolves
- @concepts/computational-genealogy-archival-automation.md — place → archive routing
- @concepts/gpuology-genealogy-agent-kit.md — Atto extract.comune soft priors
- @sources/gemini-italian-american-genealogy-sources-2026-07-21.md — US string inputs
- @sources/gemini-italian-civil-genealogy-find-playbook-2026-07-22.md — K185 FIND Step 1 Belfiore/ISTAT normalize

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Architectural Specifications for Italian Genealogical Place Name Resolution Systems |
| **Author / origin** | Gemini Deep Research (Atto research prompt → inbox) |
| **Type** | Word docx |
| **Filename** | `Italian Genealogy Software Data.docx` |
| **sha256** | `7e6e5ec2f7e3bf7795b1c6b4be3eb94b0b95203b21ff1da67fcec3aeb82f1f3a` |
| **Size** | 2,989,597 bytes |
| **Retrieved** | 2026-07-21 (inbox) |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/Italian Genealogy Software Data.docx` |
| **read_status** | read |

## Narrative

Engineering memo for resolving oral / US-phonetic place strings into historical *comuni*. Hierarchy: *frazione* → *comune* → *provincia* (State Archive). Temporal graph for *comuni soppressi* (esp. Fascist 1927–28 mergers), provincial suppressions (Caserta), Fascist renames (Littoria→Latina), Sardinia 2021–25 province recodes. **Codice Belfiore** as stable PK (survives province moves; embedded in Codice Fiscale); ISTAT/SISTAT for history + shapefiles; OSM/Wikidata for *frazioni* + successor links (license-aware). Homonyms (many San Giorgio); Southern dialect lenition (B↔V, schwa endings) need Italian→English phonetic engine, not plain Levenshtein. Regional exceptions when Antenati is weak: Trentino indexes, Friuli-in-prin, BeWeB ecclesiastical, SIUSA / SAN discovery.

**Wiki scope:** data model + pitfalls + open-dataset pointers. Do not vendor CC-BY-SA lista-comuni into proprietary git without license plan (Atto already fetch-caches).

## Snippets

> Codice Belfiore is the durable birthplace key; ISTAT codes churn when provinces reorganize. [Source: Italian Genealogy Software Data.docx]

> Immigrants often name the *frazione*; civil acts live at the governing *comune*. [Source: Italian Genealogy Software Data.docx]

> “Buccino” ↔ “Vuccino” / “Vuccin” — Southern B→V lenition breaks naive string match. [Source: Italian Genealogy Software Data.docx]

> 1927–28 Fascist consolidations create replaces/replaced-by edges that must be date-valid. [Source: Italian Genealogy Software Data.docx]
