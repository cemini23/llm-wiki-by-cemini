---
title: Automated Deep Genealogy Research (Gemini roadmap)
type: source
tags: [source, docx, genealogy, archival, k153, methodology]
keywords: [Antenati, IIIF, FamilySearch API, GEDCOM, Transkribus, HTR, Double Metaphone, stato civile, parish, Trent]
clusters: [k153-ingest]
related:
  - concepts/computational-genealogy-archival-automation.md
  - concepts/italian-regional-genealogy-archive-playbook.md
  - sources/gemini-italian-ancestry-deep-research-2026-07-09.md
  - sources/gemini-portale-antenati-research-guide-2026-07-21.md
  - entities/tools/gcerretani-antenati.md
  - entities/tools/transkribus.md
  - entities/tools/familysearch-platform-api.md
maturity: draft
read_status: read
created: 2026-07-09
updated: 2026-07-09
---

## Relations

- @concepts/computational-genealogy-archival-automation.md — synthesized 3-era Italian archival ladder + IDE automation stack
- @concepts/italian-regional-genealogy-archive-playbook.md — K154 town/archive companion
- @sources/gemini-italian-ancestry-deep-research-2026-07-09.md — family-prompt Deep Research (methodology-only wiki extract)
- @entities/tools/gcerretani-antenati.md — Portale Antenati IIIF downloader cited in source
- @entities/tools/transkribus.md — HTR platform + REST API for parish/notarial scripts
- @entities/tools/familysearch-platform-api.md — REST kinship / places API (prefer over UI scrape)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Computational Genealogy and Archival Architecture: A Technical Roadmap for Tracing European Ancestry to the 16th Century |
| **Author / origin** | Gemini deep-research export (operator drop) |
| **Type** | Word docx methodology roadmap |
| **Filename** | `Automated Deep Genealogy Research.docx` |
| **sha256** | `a3a656eb70711bca7ae7178ce48868938f4928f1a7a211a43600c8af39e7a116` |
| **Size** | 2,995,322 bytes |
| **Retrieved** | 2026-07-09 (inbox) |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/Automated Deep Genealogy Research.docx` |
| **read_status** | read |

## Narrative

Gemini-authored technical roadmap (not a specific pedigree). Argues that ~500-year European genealogy is an **archival + software** problem: civil → parish → notarial layers, then IDE automation (FamilySearch REST API, GEDCOM, graph/SQLite kinship stores, IIIF bulk image pull from Antenati, HTR via Transkribus or multimodal LLMs, Double Metaphone entity resolution).

Primary model is **Italy**: Napoleonic/stato civile (~1809+), Catholic parish registers (systematic after Council of Trent mandate ~1563), and notarial protocols for earlier or sparse vital chains. Marks the mid-1500s Trent “brick wall” and Reformation migration as the main demographic/geographic discontinuity.

Strengths for Cemini: clean era table, cites real tools (gcerretani/antenati, FamilySearch developer API, Transkribus, IIIF), and correctly pushes API over fragile FamilySearch UI scraping (Shadow DOM). Weaknesses: synthesis prose (secondary citations); Phase-0 still required before adopting any tool; no substitute for town-specific register survival.

**Out of wiki scope:** private family trees / DNA / named living people. Use this page for methodology only.

## Snippets

> Italian stato civile forms are “highly structured, pre-printed demographic forms” often naming occupations and grandparents — suitable for automated entity extraction. [Source: Automated Deep Genealogy Research.docx]

> Pre-1563 work “requires transitioning entirely away from standardized demographic datasets and relying almost exclusively on fragmented notarial deeds, feudal tax rolls, and university matriculation records.” [Source: Automated Deep Genealogy Research.docx]

> Prefer FamilySearch REST API with OAuth over BeautifulSoup/Selenium against Shadow DOM UI elements. [Source: Automated Deep Genealogy Research.docx]

> Portale Antenati exposes IIIF manifests; tools such as `gcerretani/antenati` automate registry download for offline HTR. [Source: Automated Deep Genealogy Research.docx; https://github.com/gcerretani/antenati]
