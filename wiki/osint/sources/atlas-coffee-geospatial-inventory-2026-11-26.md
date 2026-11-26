---
title: "World Coffee and Tea Atlas — permissive geospatial and origin source inventory"
type: source
related:
  - concepts/atlas-engine.md
  - sources/atlas-coffee-specification-2026-11-26.md
  - sources/atlas-coffee-seo-blueprint-2026-11-26.md
updated: 2026-11-26
read_status: read
maturity: draft
---

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Permissive Geospatial and Origin Source Inventory for World Coffee and Tea Atlas |
| Author | Operator document, no named author |
| Type | Operator document, .docx, source inventory |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/coffee inventory.docx` |
| Retrieved | 2026-11-26 |
| Pages | 239 blocks, 8 tables |
| Read status | read (summary, licence gate, tier tables and country rules) |

## Narrative

### What it is

The licence and boundary plan for Cartridge #3. It covers 63 origin entries — 36 coffee and 27 tea — across 24 producing countries and territories. [Source: coffee inventory.docx]

### The licence statement

The opening summary states the build terms directly: **"MIT code, CC BY 4.0 curated data"**, on MapLibre GL JS plus PMTiles, with a runtime payload of 15 MiB or less.

This matters beyond Cartridge #3. It is an independent statement of the same licence split that `concepts/atlas-engine.md` records as a decision, and it goes against the earlier CC BY-SA label in the 2026-11-25 spirits growth document. The corroboration is for curated data only. The document does not audit every upstream tile layer, so the ODbL caveat on the concept page still applies.

### The core finding

No verified global or national registry distributes open-licensed vector polygons for coffee or tea appellations. Statutory bodies publish other things:

| Authority | Publishes | Not |
|---|---|---|
| Colombia SIC/FNC | departmental denomination resolutions | shapefiles |
| Brazil INPI | GI registrations | polygons |
| India GI Registry | certificates | polygons |
| Sri Lanka Tea Board | agro-climatic zone definitions and estate counts | boundaries |

So the build cannot use GI registries as a geometry source. It must synthesise origins from administrative polygons and mask them with crop and elevation data.

### Approved and conditional boundary sources

| Source | Licence | Gate status |
|---|---|---|
| FAO GAUL 2024/2025 | CC BY 4.0 | Approved, inspect per-country metadata |
| World Bank Official Boundaries | CC BY 4.0 | Approved, audit `GEOM_SRCE` for SALB lineage |
| Natural Earth 1:10m | Public Domain | Approved, ADM1 only |
| HDX COD-AB | CC BY-IGO 3.0 | Conditional, audit for SALB and OSM |
| Brazil IBGE MMD | CC BY 4.0 | Approved |
| Mexico INEGI | Libre Uso MX | Conditional, verify inside the ZIP |
| Taiwan NLSC | OGDL-Taiwan-1.0 | Approved, village level |
| Japan MLIT N03 | PDL 1.0 | Conditional, plus an edit-disclosure string |
| South Korea KOSTAT SGIS | CC BY 4.0 | Conditional, verify repo provenance |

### Disqualified sources

The reject list is broader than Cartridge #2's and includes terrain inputs: Survey of India and Nakshe, ISRO Bhuvan, China Tianditu, raw UN SALB, Copernicus DEM (bespoke third-party notices), unfiltered geoBoundaries composites, and any input whose metadata mentions ODbL, CC BY-SA, non-commercial, GADM, OpenStreetMap, Wambacher, DataMeet or Tianditu.

Two rules are stricter than a simple allow-list:

- **The gate reads metadata, not licences by reputation.** Copernicus DEM is scientifically good and still rejected, because a bespoke notice breaks the eight-licence allowlist.
- **Provenance can be inherited.** GAUL and World Bank are approved on their own terms, but individual rows can trace back to UN SALB, so the gate checks per country.

### Boundary engineering for tea

Tea exposes the weakness of administrative geometry. Sri Lanka classifies tea by seven agro-climatic elevation and monsoon zones, not by province. Darjeeling spans 600–2,000 m and Nilgiri 1,000–2,500 m, while the surrounding districts include the plains. Mainland China prohibits cross-border export of map data. Taiwan publishes village-level boundaries. The build therefore masks administrative units with MapSPAM crop density and NASADEM elevation, and dissolves where an origin spans many units.

### Runtime

The 15 MiB cap forces spatial subsetting. FAO GAUL 2024 Level 2 alone holds 45,523 global districts. The plan extracts only target ADM units at z3–z9, dissolves multi-unit GIs, applies elevation and crop masks at z5–z10, and carries `src_id`, `src_url`, `src_license`, `src_vintage` and `modified` on every exported feature so MapLibre can render a live attribution bar.

### Read

Together with the spice inventory, this gives the project a repeatable geodata licence audit. The rule "no verified GI polygon registry exists" is the load-bearing claim, and it is stated for two crops and 24 countries.
