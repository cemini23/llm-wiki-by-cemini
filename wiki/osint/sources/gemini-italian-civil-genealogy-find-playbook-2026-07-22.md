---
title: Italian Civil Genealogy FIND Playbook (Gemini DR — deep links / Belfiore / do-not-automate)
type: source
tags: [source, docx, genealogy, antenati, find, atto, civil-records, k185]
keywords: [search-registry, Belfiore, ISTAT, Liste di Leva, Albo d'Oro, FIND.md, frazione, 70-year privacy]
clusters: [k185-ingest]
related:
  - concepts/antenati-deep-link-grammar.md
  - concepts/italian-regional-genealogy-archive-playbook.md
  - concepts/us-italy-hometown-reveal-ladder.md
  - concepts/computational-genealogy-archival-automation.md
  - concepts/gpuology-genealogy-agent-kit.md
  - sources/gemini-portale-antenati-research-guide-2026-07-21.md
  - sources/gemini-italian-place-name-resolution-2026-07-21.md
maturity: draft
read_status: read
created: 2026-07-22
updated: 2026-07-22
---

## Relations

- @concepts/antenati-deep-link-grammar.md — FIND deep-link templates (updated from this DR)
- @concepts/italian-regional-genealogy-archive-playbook.md — military / privacy / comune custody pivots
- @concepts/us-italy-hometown-reveal-ladder.md — feeds Step 1 geographic normalization
- @concepts/computational-genealogy-archival-automation.md — HTR / evidence packet constraints
- @concepts/gpuology-genealogy-agent-kit.md — FIND layer product surface
- @sources/gemini-portale-antenati-research-guide-2026-07-21.md — K180 Antenati guide
- @sources/gemini-italian-place-name-resolution-2026-07-21.md — K180 Belfiore PK

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Strategic Architecture and Topological Resolution in Italian Civil Record Genealogy: A Playbook for Deep-Link Systems |
| **Author / origin** | Gemini Deep Research (Atto FIND / civil-genealogy prompt → inbox) |
| **Type** | Word docx |
| **Filename** | `Italian Civil Genealogy Research Plan.docx` |
| **sha256** | `335939074628f6a524ac057c9b632206dfae9f4646e60813f73911b1ec34f429` |
| **Size** | 2,991,081 bytes |
| **Retrieved** | 2026-07-22 (inbox) |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/Italian Civil Genealogy Research Plan.docx` |
| **read_status** | read |

## Narrative

FIND-layer playbook: Antenati + FamilySearch entry points, frazione→comune / Belfiore temporal normalization, civil vs parish eras, military backdoors (*Liste di Leva* / *Ruoli Matricolari* / Albo d'Oro), and explicit **do-not-automate** constraints.

**Deliverable pipeline (A):** normalize place → nominative links (low yield) → registry browse links (high yield) → military backdoor if male ~1850–1920 → optional cassette/HTR → emit `FIND.md`.

**Deep-link templates (B):** Antenati `search-registry/?localita=` preferred; nominative secondary; FS catalog `q.filmNumber=` durable; Albo d'Oro often no deep-link (route to search UI).

**Comune checklist (C):** frazione vs comune · temporal validity / mergers · civil vs baptism · 70-year privacy closure copy bank (D).

**Do not automate (E):** CDN/IIIF scrape · auto tree merge · server-side HTR on scraped images · bypass paywalls / auto PEC · blind POST into portal forms.

**Citation quality:** Antenati URLs + FS wiki + secondary blogs. Nominative “<15% hit” claim is anecdotal — treat as UX framing, not a measured KPI. [TENTATIVE]

**Wiki scope:** FIND routing. Operator doctrine still: browser-first; no Antenati CDN product.

## Snippets

> Prefer registry browse deep links over nominative search; nominative framed as low-probability rapid-pass. [Source: Italian Civil Genealogy Research Plan.docx]

> Template: https://antenati.cultura.gov.it/search-registry/?localita={COMUNE} — highest success rate. [Source: Italian Civil Genealogy Research Plan.docx]

> Never write truth.ged without human verification — Italian naming conventions collide cousins. [Source: Italian Civil Genealogy Research Plan.docx]

> Do not: CDN scrape · unauthorized server HTR · bypass Comune/Archivio paywalls · blind POST form injection. [Source: Italian Civil Genealogy Research Plan.docx]
