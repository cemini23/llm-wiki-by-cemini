---
title: "World Spice and Chili Atlas — geospatial and regulatory inventory"
type: source
related:
  - concepts/atlas-engine.md
  - sources/atlas-spice-specification-2026-11-26.md
  - sources/atlas-spice-growth-strategy-2026-11-26.md
updated: 2026-11-26
read_status: read
maturity: draft
---

## Raw Concept

| Field | Value |
|-------|--------|
| Title | World Spice and Chili Atlas Geospatial and Regulatory Inventory |
| Author | Operator document, no named author |
| Type | Operator document, .docx, source inventory |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/Global Spice GI Geospatial Inventory.docx` |
| Retrieved | 2026-11-26 |
| Pages | 171 blocks, 7 tables |
| Read status | read |

## Narrative

### What it is

A licence audit and polygon plan for 55–62 flagship spice and chili regions in Cartridge #2. It answers one question: which boundary sources can enter a zero-copyleft build, and which must abort it. [Source: Global Spice GI Geospatial Inventory.docx]

### Two-tier assembly

**Tier one — direct national vectors,** used only where an official open portal is verified:

| Country | Source | Status |
|---|---|---|
| France | INAO SIQO delimited areas, 84.9 MB | Conditional pass, confirm Licence Ouverte 2.0 |
| Spain | CNIG/IGN BDLJE, 63–222 MB by format | Pass, CC BY 4.0 |
| Italy | ISTAT statistical boundaries | Hold, verify the CC BY version |
| Mexico | INEGI Marco Geoestadístico | Hold, verify Libre Uso MX inside the ZIP |
| Japan | MLIT KSJ N03 | Hold, per-dataset terms vary |

**Tier two — global fallback,** where no national portal is verified: FAO GAUL 2025 Level 2 (CC BY 4.0, published 28 May 2026), World Bank Official Boundaries Admin-2 (CC BY 4.0, updated 21 October 2026), and Natural Earth 1:10m (Public Domain). [Source: Global Spice GI Geospatial Inventory.docx]

### The deny list

Five source families abort the build:

| Source | Reason |
|---|---|
| Eurostat GISCO | Non-commercial, verified against its own primary terms |
| Overture Maps Divisions | ODbL 1.0 via OpenStreetMap conflation |
| geoBoundaries | Mixed ODbL, DataMeet and CC BY |
| DataMeet India | CC BY 2.5 India, 2011 boundaries |
| GADM | Non-commercial |

The document makes a sharper point than a simple deny list. Catalogue badges cannot be trusted. One commercial connector lists Eurostat GISCO as reusable under Decision 2011/833/EU, which contradicts Eurostat's own download terms. The gate must read upstream metadata, not the aggregator's label.

### Regional split

Europe 12–13 regions, Asia 22–23, Americas 12–14, Middle East and Africa 9–12. Europe and Asia are the best covered, because France and Spain publish GI polygons and India and Japan publish national municipal layers. Middle East and Africa have no verified national portal in the audited set, so every one of those regions routes through GAUL, World Bank or Natural Earth.

### Runtime budget

The 15 MiB cap does not survive unfiltered input. Single upstream archives are larger than the whole budget: Spanish CNIG at 156.96 MB as shapefile or 222.71 MB as GeoPackage, the French INAO bundle at 84.9 MB, World Bank ADM0 GeoJSON at 165.78 MB, the Survey of India ABDB at 193.14 MB, and Natural Earth Admin-1 alone at 14.22 MB zipped. The plan filters to the target polygons and dissolves before tiling, and enforces a CI size assertion on `spices.pmtiles` plus the basemap plus the MapLibre bundle. [Source: Global Spice GI Geospatial Inventory.docx]

### Elevation bands

No audited source carries elevation-band geometry. Nine upland terroirs may need clipping inside broad Admin-2 districts: Kashmir saffron, Himachal kala jeera, Coorg and Alleppey cardamom, Wakayama sansho, Sichuan peppercorn, Cobán cardamom, Peruvian rocoto, Taliouine saffron and Ethiopian korarima. Candidate elevation inputs are SRTM v4 and Japan GSI, both pending licence verification. [Source: Global Spice GI Geospatial Inventory.docx]

### What remains unverified

The document is explicit about its own gaps. ISO 676, the India Spices Board GI registry, Mexican IMPI and NOM records, the Sri Lanka Ceylon Cinnamon PGI specification, Codex standard identifiers beyond the existence of CCSCH7, and peer-reviewed HPLC capsaicinoid datasets were not retrieved. No Scoville or grade metadata can publish until they are.

### Read

This is the most reusable document in the set. The deny list and the "verify upstream, not the badge" rule apply to any geodata build, not just a spice atlas.
