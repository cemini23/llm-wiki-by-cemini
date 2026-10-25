---
title: gcerretani/antenati (Portale Antenati IIIF downloader)
type: entity
tags: [tool, genealogy, antenati, iiif, python, draft]
keywords: [IIIF, Portale Antenati, Italian civil registers, offline archival]
related:
  - concepts/gpuology-genealogy-agent-kit.md
  - sources/gemini-gpuology-genealogy-business-analysis-2026-07-20.md
  - sources/gemini-automated-deep-genealogy-research-2026-07-09.md
  - sources/gemini-italian-ancestry-deep-research-2026-07-09.md
  - sources/gemini-portale-antenati-research-guide-2026-07-21.md
  - sources/gemini-italian-genealogy-research-tools-2026-07-21.md
  - sources/gemini-italian-civil-register-extraction-2026-07-21.md
  - concepts/antenati-deep-link-grammar.md
  - concepts/computational-genealogy-archival-automation.md
  - concepts/italian-regional-genealogy-archive-playbook.md
  - entities/tools/transkribus.md
  - sources/gemini-sellia-calabria-archive-routing-2026-07-11.md
maturity: draft
created: 2026-07-09
updated: 2026-10-25
---

## Relations
- @sources/gemini-gpuology-genealogy-business-analysis-2026-07-20.md — K176 GPUOLOGY business DR
- @concepts/gpuology-genealogy-agent-kit.md — product strategy concept
- @sources/gemini-portale-antenati-research-guide-2026-07-21.md — K180 WAF + ARK + upcoming auth download
- @sources/gemini-italian-genealogy-research-tools-2026-07-21.md — K180 hybrid browser→manifest→CLI workflow
- @sources/gemini-italian-civil-register-extraction-2026-07-21.md — K180 HTR image source path
- @concepts/antenati-deep-link-grammar.md — prefer deep links over bulk scrape

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
| **K176 commercial posture** | Download to **user’s local machine** for personal/research use (Italian Ministry decrees cited in DR). Central commercial hosting of Antenati images → concession fees / ToS risk. AWS WAF challenges common. Legal review required before kit ships IIIF agent. [Source: @sources/gemini-gpuology-genealogy-business-analysis-2026-07-20.md] |
| **K180 ops note** | Typical hybrid: solve AWS WAF in browser → pass IIIF manifest URL to CLI. Ministry has signaled authenticated high-res download for registered users — may obsolete third-party bulk tools; Atto stays browser-first + local vault. [Source: @sources/gemini-portale-antenati-research-guide-2026-07-21.md · @sources/gemini-italian-genealogy-research-tools-2026-07-21.md] |

Cited in @sources/gemini-automated-deep-genealogy-research-2026-07-09.md alongside generic IIIF downloaders.

## Snippets

> “Open-source Python command-line tools, such as antenati (developed specifically to interface with the Italian Ministry of Culture's architecture)” [Source: @sources/gemini-automated-deep-genealogy-research-2026-07-09.md]
