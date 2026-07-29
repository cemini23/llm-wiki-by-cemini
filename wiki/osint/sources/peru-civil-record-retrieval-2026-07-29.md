---
title: Peru civil-record retrieval — RENIEC proxy-first for Atto
type: source
tags: [source, genealogy, citizenship, atto, peru, reniec, k206, docx]
keywords: [RENIEC, Copia Certificada, Págalo.pe, Yape, e-apostille, OREC, DNI firewall]
related:
  - concepts/foreign-civil-doc-authentication-regimes.md
  - concepts/italian-citizenship-latam-audience-systems.md
  - concepts/italian-citizenship-pathways-document-pipelines.md
  - concepts/italian-citizenship-primary-law-lock.md
  - concepts/gpuology-genealogy-agent-kit.md
maturity: validated
created: 2026-07-29
updated: 2026-07-29
read_status: deep-read
---

## Relations

- @concepts/foreign-civil-doc-authentication-regimes.md — hague_apostille after source PDF
- @concepts/italian-citizenship-latam-audience-systems.md — LatAm expansion card
- @concepts/italian-citizenship-pathways-document-pipelines.md — DOC_*
- @concepts/italian-citizenship-primary-law-lock.md — Clock A
- @concepts/gpuology-genealogy-agent-kit.md — product hub

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Peru Civil Record Retrieval (Gemini DR-08) |
| Filename | `Peru Civil Record Retrieval.docx` |
| sha256 | `eb62403952750c0b331041e46d1a560abba04c2e0159da71eac9ff18b1cbdd7f` |
| Retrieved | 2026-07-29 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/Peru Civil Record Retrieval.docx` |
| Laptop extract | `.local/research/atto-latam-audience-systems/PERU.md` |

**Not legal advice.**

## Narrative

Digitization looks end-to-end, but the **RENIEC DNI firewall** blocks non-residents from self-serve issuance — Atto posture must be **proxy-first**, not “fully online for diaspora.” Issue **Copia Certificada** (not certificado/extracto). Coverage probe via `apps.reniec.gob.pe/actasregistrales` distinguishes portal hit vs OREC fallback.

Apostille is remote-capable (`portal.rree.gob.pe`, foreign passport OK, S/ 31 e-apostille) **after** an e-signed PDF exists; source issuance is not. **Págalo.pe** accepts foreign cards; **Yape** is Peru-only — do not recommend for abroad payments. Soil-title mapping uses Constitución + birth acta frames (1933/1979/1993 differ on loss rules).

## Snippets

> “Fully online for diaspora” hypothesis fails at the DNI wall.

[Source: Peru Civil Record Retrieval.docx]
