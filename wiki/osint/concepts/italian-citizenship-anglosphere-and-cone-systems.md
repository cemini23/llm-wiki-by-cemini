---
title: Italian citizenship — US · CA · AU · CL · UY admin matrices for Atto
type: concept
tags: [concept, genealogy, citizenship, atto, k204, usa, canada, australia, chile, uruguay]
keywords: [jus soli cutoff, DFAT, GAC, SRCeI, DGREC, e-Apostille, DOC_FOREIGN_IUS_SOLI_TITLE, auth regime]
related:
  - sources/us-records-italian-citizenship-2026-07-29.md
  - sources/canada-apostille-citizenship-research-2026-07-29.md
  - sources/australia-nationality-law-research-2026-07-29.md
  - sources/chile-civil-records-reference-pack-2026-07-29.md
  - sources/uruguay-italian-emigrant-reference-pack-2026-07-29.md
  - concepts/italian-citizenship-latam-audience-systems.md
  - concepts/italian-citizenship-pathways-document-pipelines.md
  - concepts/italian-citizenship-primary-law-lock.md
  - concepts/italian-citizenship-youtube-soft-flags.md
  - concepts/gpuology-genealogy-agent-kit.md
  - sources/cassazione-minor-issue-pdf-pack-2026-07-28.md
maturity: draft
created: 2026-07-29
updated: 2026-07-29
---

## Relations

- @sources/us-records-italian-citizenship-2026-07-29.md — US vital + apostille + USCIS matrices
- @sources/canada-apostille-citizenship-research-2026-07-29.md — post-2024 GAC / provincial split
- @sources/australia-nationality-law-research-2026-07-29.md — 1986 *jus soli* cutoff + DFAT
- @sources/chile-civil-records-reference-pack-2026-07-29.md — SRCeI / RUN / e-Apostille
- @sources/uruguay-italian-emigrant-reference-pack-2026-07-29.md — ciudadanía vs nacionalidad
- @concepts/italian-citizenship-latam-audience-systems.md — BR/AR/VE/DO GTM + CL/UY sequencing
- @concepts/italian-citizenship-pathways-document-pipelines.md — DOC_* / pathway IDs
- @concepts/italian-citizenship-primary-law-lock.md — Clock A/B
- @concepts/italian-citizenship-youtube-soft-flags.md — soft-flags
- @concepts/gpuology-genealogy-agent-kit.md — product hub
- @sources/cassazione-minor-issue-pdf-pack-2026-07-28.md — primary PDFs

## Raw Concept

Inbox country packs (2026-07-29) for five high-signal jurisdictions beyond the K203 LatAm core four. Goal: encode **foreign-title** + **authentication** + **consular** traps into Atto Research checklists — never auto-eligibility.

**Not legal advice.** Full matrices live in `.local/research/atto-latam-audience-systems/{USA,CANADA,AUSTRALIA,CHILE,URUGUAY}.md`.

## Narrative

### Auth-regime defaults (see also AUTH-REGIMES.md)

| Country | Default regime | Overlay |
|---------|----------------|---------|
| US | `hague_apostille` | State vs federal authentications; e-Apostille acceptance uneven at IT seats |
| CA | `hague_apostille` (from **2024-01-11**) | **Bifurcated** GAC vs AB/BC/ON/QC/SK — wrong office = 20-day burn |
| AU | `hague_apostille` | **DFAT only**; paper seal; no e-apostille |
| CL | `hague_apostille` | Native **e-Apostille** PDFs; seat “original” rule unverified |
| UY | `hague_apostille` | Manuscript → in-person MRREE; gestor/Carta Poder for diaspora |

EU 2016/1191 / CIEC 16/34 do **not** apply to these five as issuance countries for Italy-bound packs (CH/FR/BE stay on separate EU/CIEC tracks).

### Soil-title false-positive leaders

1. **Australia post-20-Aug-1986** — birth ≠ citizenship without parent citizen/PR or Form 119 acquisition date = DOB.
2. **US N-560 / CRBA** — citizenship ≠ soil; Circ. 43347 minor-issue exposure.
3. **Chile transeúnte** annotation (pre-2014 practice) — birth may not have conferred Chilean nationality.
4. **Uruguay ciudadanía legal** — Corte Electoral positive ≠ settled Italian-law naturalization theory; counsel path.
5. **Canada wallet citizenship certificate** — does not prove *jus soli*; need long-form birth + IRCC search for naturalization timeline.

### DOC_* mapping (parked code)

Reuse pathways ontology: `DOC_FOREIGN_BIRTH_TITLE`, `DOC_FOREIGN_NATURALISATION_OR_NONE`, `DOC_FOREIGN_IUS_SOLI_TITLE`, marriage/death, ID corroboration. Per-country issuer + apostille authority from source tables. Translation modes: US seat-fork (Boston apostille-on-translator); CA often dual apostille or translate-in-Italy; AU NAATI after DFAT; CL embassy list vs MINREL; UY Traductor Público + consular conformity.

### Sequencing vs K203

Keep **US** as GTM beachhead + deepest checklist. Ship **CA/AU** Research branches next (English, shared anglosphere UX). **CL/UY** after BR/AR locale scaffolding (Spanish Cone). Do not wait on Brazilian GitHub civic APIs — they do not issue certidões.

## Dead Ends

- Treating e-Apostille existence in issuing state as Italian-seat acceptance.
- Assuming registrocivil.cl / gub.uy digital portals work without local national ID.
- Encoding Uruguay *ciudadanía legal* as automatic eligibility win or automatic loss without counsel soft-flag.
