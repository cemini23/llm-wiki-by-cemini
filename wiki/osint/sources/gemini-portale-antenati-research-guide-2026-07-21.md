---
title: Portale Antenati Research Guide (Gemini DR — deep-link grammar)
type: source
tags: [source, docx, genealogy, antenati, iiif, k180, italy]
keywords: [search-registry, ARK, localita, tipologia, IIIF, AWS WAF, dual-original, lang=it]
clusters: [k180-ingest]
related:
  - concepts/antenati-deep-link-grammar.md
  - concepts/computational-genealogy-archival-automation.md
  - concepts/italian-regional-genealogy-archive-playbook.md
  - concepts/gpuology-genealogy-agent-kit.md
  - entities/tools/gcerretani-antenati.md
  - sources/gemini-italian-civil-register-extraction-2026-07-21.md
  - sources/gemini-italian-genealogy-research-tools-2026-07-21.md
  - sources/gemini-automated-deep-genealogy-research-2026-07-09.md
maturity: draft
read_status: read
created: 2026-07-21
updated: 2026-07-21
---

## Relations

- @concepts/antenati-deep-link-grammar.md — synthesized URL + checklist rules for Atto find layer
- @entities/tools/gcerretani-antenati.md — IIIF downloader; WAF/manifest hybrid workflow
- @concepts/computational-genealogy-archival-automation.md — era ladder hub
- @concepts/gpuology-genealogy-agent-kit.md — product = browser browse, local organize
- @sources/gemini-italian-civil-register-extraction-2026-07-21.md — act layout + ARK/DGS citation companion
- @sources/gemini-italian-genealogy-research-tools-2026-07-21.md — competitive tooling around Antenati friction
- @sources/gemini-automated-deep-genealogy-research-2026-07-09.md — prior IIIF/Antenati methodology (K153)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Architectural Analysis and Methodological Framework of Portale Antenati (2025–2026) |
| **Author / origin** | Gemini Deep Research (Atto research prompt → inbox) |
| **Type** | Word docx |
| **Filename** | `Portale Antenati Research Guide.docx` |
| **sha256** | `6021cef07a109c364ed0f7c5db467c502ef07ee41c62843fc00d9e595644b1ab` |
| **Size** | 2,990,776 bytes |
| **Retrieved** | 2026-07-21 (inbox) |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/Portale Antenati Research Guide.docx` |
| **read_status** | read |

## Narrative

Architecture memo for Portale Antenati as of 2025–2026: SPA + AWS WAF, IIIF Presentation manifests on `dam-antenati` / `iiif-antenati`, Mirador viewer, and **stable browse deep links** via `search-registry` query params (`localita`, `anno`, `tipologia`, `archivio`, `fondo`, `serie`, `descrizione`, `lang`). Canonical citations use **ARK** (`/ark:/12657/…`), not ephemeral `s_id`. Prefer `lang=it` (EN UI can lag / undercount). Nominative “Index of published names” is incomplete — null ≠ absent; always fall through to volume browse. Dual-original doctrine: Antenati digitizes State Archive *seconda copia*; gaps → Comune *prima copia* / *copia integrale* (portal images are **not** legal certificates). Upcoming authenticated download area may obsolete third-party bulk IIIF tools.

**Wiki scope:** URL grammar, operator checklist, WAF/ops notes. No scrape recipes for CDN tile farms; no private pedigree.

## Snippets

> Stable browse: `https://antenati.cultura.gov.it/search-registry/?localita=Milano&tipologia=Nati&anno=1890&lang=it` [Source: Portale Antenati Research Guide.docx]

> Persistent cite: `https://antenati.cultura.gov.it/ark:/12657/{item_id}` — not `detail-registry/?s_id=…` [Source: Portale Antenati Research Guide.docx]

> Nominative index incomplete — absence means “not transcribed,” not “not registered.” [Source: Portale Antenati Research Guide.docx]

> Antenati = tribunal/State Archive copy; Comune retains the twin. WWII gaps (e.g. Napoli) → write the municipality. [Source: Portale Antenati Research Guide.docx]
