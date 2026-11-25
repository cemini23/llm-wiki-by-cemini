---
title: "World Spirits Atlas — open geospatial architecture and static build pipeline"
type: source
related:
  - concepts/atlas-engine.md
  - sources/world-spirits-atlas-specification-2026-11-25.md
  - sources/world-spirits-atlas-growth-strategy-2026-11-25.md
updated: 2026-11-25
read_status: skimmed
maturity: draft
---

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Open-Source World Spirits Atlas: Verified Permissive Geospatial Inventory, Regulatory Extraction Architecture, and Sub-15MB Static Build Pipeline |
| Author | Operator document, no named author |
| Type | Operator document, .docx, technical architecture |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/Open World Spirits Atlas Architecture.docx` |
| Retrieved | 2026-11-25 |
| Pages | 245 paragraphs, 5 tables |
| Read status | skimmed (sections 1–3, pipeline and byte budget) |

## Narrative

### What it is

The data and build layer for a World Spirits Atlas: where the geographic boundaries come from, how legal standards of identity are extracted, and how the whole thing compiles into a static site under 15 MB. It is written as a design document, with a citation for almost every claim. [Source: Open World Spirits Atlas Architecture.docx]

This is one of three documents for the same new product. The others are the technical and pedagogical specification, and the growth and monetization playbook. See `concepts/atlas-engine.md`.

### The core constraint: zero-copyleft data

The document opens by rejecting five mainstream GIS defaults because they silently add share-alike or non-commercial terms:

- Eurostat GISCO NUTS/LAU, non-commercial only; commercial rights sit with EuroGeographics.
- GADM, non-commercial, no redistribution.
- Overture Maps divisions and base themes, which inherit ODbL from OpenStreetMap.
- Selected geoBoundaries sub-national layers that inherit ODbL from upstream contributors.
- GADM-derived UN OCHA HDX COD-AB packages, notably Barbados.

The replacements are public-domain, CC0, CC BY 4.0, Open Government Licence v3.0, Licence Ouverte, OGDL-Taiwan and INEGI free-use national datasets. A licensing gate in the build aborts on any deny-list match. That is the single most reusable idea in the document: licence checking is code, not review.

**Licence decision (2026-11-25):** CC BY 4.0 governs the curated data. That is this document's term and it matches the zero-copyleft constraint. The caveat sits with the tiles: this document also lists Overture Maps and selected geoBoundaries layers, both of which **inherit ODbL — a share-alike licence — from OpenStreetMap**. A derived tile database containing that geometry carries the obligation, so the map download cannot be labelled CC BY 4.0 on the strength of this document alone. Check tile provenance before release. `[OPEN QUESTION 2026-11-25]`

### Consuming structured law instead of scraping prose

Almost no jurisdiction outside France publishes vector polygons for spirit geographical indications. So the architecture pairs deterministic administrative dissolves, driven by versioned municipal and ward lookup tables, with parsers against machine-readable government APIs: EUR-Lex CELLAR SPARQL, the EU eAmbrosia API, the US eCFR Versioner XML API, and UK legislation.gov.uk XML. The Scotland example shows why this needs care: the five statutory whisky regions are defined partly by 2006 council wards, so the build must match those ward boundaries, not current ones.

### Build pipeline and byte budget

The repository is cartridge-generic. Domain recipes live in `cartridges/<domain>/`, and the same compiler builds Spirits, Wine, Coffee or Spice atlases with no code change. The compiler stages are fetch, licence gate, dissolve, standards extraction. Geometry is simplified and stripped to six thin tile keys. Output is z0-to-z10 PMTiles plus Brotli-compressed legal JSON shards, with an ODbL-free Natural Earth basemap.

The estimated payload is 6.7 to 11.6 MB, under the 15 MB ceiling. Runtime fetches individual tiles by HTTP range request, so a visitor downloads only what is in view. The front end is MapLibre GL JS.

### Honest limits

This is an engineering estimate, not a measured build. The byte budget is explicitly a table of allowances, not a benchmark. Toolchain caveats are stated: Tippecanoe does not run natively on Windows, so GDAL's PMTiles driver is the fallback, and two auxiliary Open Maps for Europe utilities are GPL-3.0 and must not be bundled into an MIT repository.

### Reuse value

High for any geospatial product in the workspace. The licence-gate-as-code pattern, the cartridge layout and the thin-tile-key discipline transfer directly. Treat the numbers as targets to verify, not facts.
