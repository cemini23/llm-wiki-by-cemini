---
title: gcerretani/antenati (Portale Antenati IIIF downloader)
type: entity
tags: [tool, genealogy, antenati, iiif, python, draft]
keywords: [IIIF, Portale Antenati, Italian civil registers, offline archival]
related:
  - sources/gemini-automated-deep-genealogy-research-2026-07-09.md
  - sources/gemini-italian-ancestry-deep-research-2026-07-09.md
  - concepts/computational-genealogy-archival-automation.md
  - concepts/italian-regional-genealogy-archive-playbook.md
  - entities/tools/transkribus.md
maturity: draft
created: 2026-07-09
updated: 2026-07-09
---

## Relations

- @sources/gemini-automated-deep-genealogy-research-2026-07-09.md — cited as Antenati automation path
- @sources/gemini-italian-ancestry-deep-research-2026-07-09.md — reaffirmed Priority-2 in K154 tool matrix
- @concepts/computational-genealogy-archival-automation.md — IIIF bulk-fetch step
- @concepts/italian-regional-genealogy-archive-playbook.md — town-locked civil image pull
- @entities/tools/transkribus.md — typical next hop after offline images

## Raw Concept

Open-source Python CLI aimed at Italy’s Portale Antenati IIIF image delivery — download whole civil-register books for local browsing / HTR. Repo: [gcerretani/antenati](https://github.com/gcerretani/antenati).

## Narrative

| Field | Value |
|-------|-------|
| **Role** | Offline extract of digitized *stato civile* / Napoleonic packs |
| **Fit** | Town-locked deep research when name indexes are empty and page browse is required |
| **Verdict** | **Watch / conditional Phase-0** — useful pointer; confirm license + Antenati usage terms before production scripts |
| **Not for** | Creating pedigree facts without reading images; FamilySearch Shadow-DOM scraping |

Cited in @sources/gemini-automated-deep-genealogy-research-2026-07-09.md alongside generic IIIF downloaders.

## Snippets

> “Open-source Python command-line tools, such as antenati (developed specifically to interface with the Italian Ministry of Culture's architecture)” [Source: @sources/gemini-automated-deep-genealogy-research-2026-07-09.md]
