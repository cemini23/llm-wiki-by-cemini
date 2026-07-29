---
title: Foreign civil-doc authentication regimes — Hague / EU / CIEC enum
type: concept
tags: [concept, genealogy, citizenship, atto, apostille, ciec, eu-2016-1191, k206]
keywords: [hague_apostille, eu_2016_1191, ciec_16_34, INFOSTAR, multilingual form, auth-regime enum]
related:
  - sources/switzerland-nationality-civil-registry-2026-07-29.md
  - sources/france-nationality-registry-2026-07-29.md
  - sources/belgium-civil-registry-2026-07-29.md
  - sources/peru-civil-record-retrieval-2026-07-29.md
  - sources/mexico-civil-records-2026-07-29.md
  - sources/argentina-consular-rules-deepening-2026-07-29.md
  - sources/brazil-jure-sanguinis-deepening-2026-07-29.md
  - sources/venezuela-italian-citizenship-deepening-2026-07-29.md
  - sources/dominican-nationality-document-deepening-2026-07-29.md
  - concepts/italian-citizenship-anglosphere-and-cone-systems.md
  - concepts/italian-citizenship-latam-audience-systems.md
  - concepts/italian-citizenship-pathways-document-pipelines.md
  - concepts/gpuology-genealogy-agent-kit.md
  - concepts/italian-citizenship-primary-law-lock.md
maturity: draft
created: 2026-07-29
updated: 2026-07-29
---

## Relations

- @sources/switzerland-nationality-civil-registry-2026-07-29.md — force CIEC 16; EU N/A
- @sources/france-nationality-registry-2026-07-29.md — eu_2016_1191 + copie intégrale
- @sources/belgium-civil-registry-2026-07-29.md — EU/CIEC; copie not extrait
- @sources/peru-civil-record-retrieval-2026-07-29.md — Hague after RENIEC PDF
- @sources/mexico-civil-records-2026-07-29.md — state Hague; e-Apostille ≠ civil
- @sources/argentina-consular-rules-deepening-2026-07-29.md — seat×province Hague overlays
- @sources/brazil-jure-sanguinis-deepening-2026-07-29.md — Hague + SP/BH digital-reject overlay
- @sources/venezuela-italian-citizenship-deepening-2026-07-29.md — SAREN e-apostille + comuni friction
- @sources/dominican-nationality-document-deepening-2026-07-29.md — MIREX + PGR-before-translation
- @concepts/italian-citizenship-anglosphere-and-cone-systems.md — US/CA/AU/CL/UY + CH/FR/BE
- @concepts/italian-citizenship-latam-audience-systems.md — BR/AR/VE/DO/PE/MX
- @concepts/italian-citizenship-pathways-document-pipelines.md — DOC_* consumers
- @concepts/gpuology-genealogy-agent-kit.md — product hub
- @concepts/italian-citizenship-primary-law-lock.md — Clock A foreign-title

## Raw Concept

Should Atto replace `apostille: bool` with an authentication-regime enum so Research checklists do not ship FR/BE packs under a false “needs apostille” default, or CH packs under CIEC Form 34?

**Not legal advice.** Operator pack: `.local/research/atto-latam-audience-systems/AUTH-REGIMES.md`.

## Narrative

### Enum (product)

| Value | When |
|-------|------|
| `hague_apostille` | Issuing state party to Hague; Italian seat expects apostille (US/CA/AU/CL/UY/PE/MX/AR/… and CH nat/judgments) |
| `eu_2016_1191` | Public docs issued in EU member for use in another EU member — multilingual standard form; apostille often unnecessary |
| `ciec_16_34` | CIEC multilanguage civil-status forms — **force Convention 16** when Italy is destination (IT not party to 34) |
| `consular_or_bilateral` | Overlay: IT–AR 1987 / seat-specific QR digital acceptance / counsel legalization paths |

### Defaults by issuance country (2026-07-29 snapshot)

| Country | Default | Critical overlay |
|---------|---------|------------------|
| CH | `ciec_16_34` + Hague for nat | **Force Conv. 16**; EU form N/A (EFTA) |
| FR | `eu_2016_1191` | Hague if IT filing **outside** EU |
| BE | `eu_2016_1191` / CIEC | copie not extrait; eLegalisation later |
| PE / MX / AR / US / CA / AU / CL / UY | `hague_apostille` | MX state not federal civil; PE after PDF; AR seat×province; CA GAC vs provincial |

### Never

- Boolean apostille as sole auth gate.
- Treat e-Apostille existence in issuing state as Italian-seat acceptance.
- Default INFOSTAR NG Form 34 for Italy-bound CH extracts.

## Dead Ends

- Encoding “Europe = EU multilingual floor” (breaks CH).
- Assuming SIDEA / MiConsulado prints satisfy Amb CDMX.
