---
title: Diaspora-press IIIF geocoding pipeline (Atto steal)
type: concept
tags: [genealogy, iiif, geocoding, atto, k226]
keywords: [IIIF, diaspora press, VLM bootstrap, geocode]
related:
  - sources/arxiv-2608.05911-armenian-paris-geocoding-2026-08-07.md
  - entities/tools/semantica.md
  - concepts/computational-genealogy-archival-automation.md
maturity: draft
created: 2026-08-07
updated: 2026-08-07
---

## Relations

- @sources/arxiv-2608.05911-armenian-paris-geocoding-2026-08-07.md
- @entities/tools/semantica.md
- @concepts/computational-genealogy-archival-automation.md

## Raw Concept

Pattern from Armenian Paris mapping paper (2608.05911) for Atto productization of press/ad geocoding — not Barone-private digs.

## Narrative

1. IIIF page → detect commercial ads → VLM/OCR bootstrap for under-resourced scripts → structured records → geocode → map.
2. Atto: reuse for Italian/diaspora newspapers and town directories; **Transkribus** remains sole product HTR; Magika + PII strip; no unattended portal scrape.
3. Pair with semantica / sie for entity index — human-gated merges.

## Snippets

> End-to-end, IIIF-based pipeline that turns digitised diaspora press into an interactive map of commercial community. [Source: arXiv:2608.05911]
