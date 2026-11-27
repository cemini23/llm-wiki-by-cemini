---
title: Atlas Engine - three-cartridge geospatial atlas (spirits, spice, coffee and tea)
type: concept
maturity: draft
related:
  - sources/world-spirits-atlas-architecture-2026-11-25.md
  - sources/world-spirits-atlas-specification-2026-11-25.md
  - sources/world-spirits-atlas-growth-strategy-2026-11-25.md
  - sources/atlas-spirits-expansion-2026-11-26.md
  - sources/atlas-spice-specification-2026-11-26.md
  - sources/atlas-spice-geospatial-inventory-2026-11-26.md
  - sources/atlas-spice-growth-strategy-2026-11-26.md
  - sources/atlas-coffee-specification-2026-11-26.md
  - sources/atlas-coffee-geospatial-inventory-2026-11-26.md
  - sources/atlas-coffee-seo-blueprint-2026-11-26.md
updated: 2026-11-26
---

## Raw Concept

Question this page answers: what is the Atlas Engine, what is in cartridge #1, and is this a new project?

From three operator documents dated 2026-11-25: an architecture document, a technical and pedagogical specification, and a growth and monetization playbook. At ingest time no code repository existed. A working build now exists at `~/Projects/Atlas101`, remote `github.com/cemini23/flavororigins`.

**Status: BUILT - v1 live at flavororigins.com/spirits/ (expanded build verified 2026-11-26).** No page in `wiki/osint/` described an Atlas Engine before this ingest. `concepts/historical-jurisdiction-atlas.md` shares the word "atlas" and nothing else, and there is no evidence this is related to Comuni Atlas.

## Narrative

### What it is

A multi-vertical atlas engine: one rendering and data engine, plus per-domain "cartridges". Cartridge #1 is the World Spirits Atlas. Cartridge #2 and later are named as Wine, Coffee and Spice or Tea. The engine is domain-agnostic; the cartridge supplies the content, the legal rules and the sensory taxonomy. [Source: World Spirits Atlas Specification.docx]

### Three layers

**Data.** Zero-copyleft geographic boundaries, sourced from public-domain and permissively licensed national datasets. A licence gate runs in code and aborts the build on any ODbL, share-alike, non-commercial, GADM or MPL source. Legal standards of identity are pulled from machine-readable government APIs, not scraped prose. [Source: Open World Spirits Atlas Architecture.docx]

**Schema.** Six universal typed interfaces, shared by every vertical: `OriginRegion`, `BaseMaterial`, `ProcessMethod`, `Expression`, `TimelineEvent`, `Composition`. A vertical-specific extension carries the rest. Validation is part of the schema: dual ABV thresholds, contested-GI versioning, and a mandatory pedagogical sibling for every expression. [Source: World Spirits Atlas Specification.docx]

**Delivery.** A static build: PMTiles vector tiles plus Brotli-compressed JSON shards, rendered in MapLibre. Measured 2026-11-26: `spirits.pmtiles` is 13.04 MB, the basemap is 1.71 MB, the shards total 235.9 KB, and `attribution.json` is 20.3 KB. The active payload is 15,013,255 bytes, with 715 KB of headroom under the 15 MiB cap. The GeoJSON fallback is 1.48 MB and never loads on a normal visit. A generic repository layout puts domain recipes in `cartridges/<domain>/` so a new vertical needs no code change.

### Content scope at launch

300 regional expressions across six families: whisk(e)y, agave, cane and rum, botanicals and amari, grape and orchard brandies, and Asian and grain spirits. 112 multi-region cocktails under a "Map Your Glass" feature. 35 timeline milestones. Fifteen validator unit tests. [Sources: World Spirits Atlas Specification.docx; verified build 2026-11-26]

### Cartridge architecture (three cartridges, one engine)

The product family is now defined as three cartridges, all served by one engine:

| Cartridge | Route | Domain | State |
|---|---|---|---|
| #1 World Spirits | `/spirits/` | flavororigins.com | Built and live (expanded build verified 2026-11-26) |
| #2 World Spice and Chili | `/spices/` | flavororigins.com | Specified, not built |
| #3 Coffee and Tea | `/coffee-tea/` | flavororigins.com | Specified, not built |

The engine brand is `terroirkit.dev`. The consumer brand is `flavororigins.com`. The stack is Astro SSG plus MapLibre GL JS plus PMTiles, with a runtime payload cap of 15 MiB per cartridge. [Sources: coffee specs.docx, World Spice Atlas Specification.docx, Coffee & Tea SEO Blueprint.docx]

**Shared primitives.** All three cartridges keep the same six universal interfaces: `OriginRegion`, `BaseMaterial`, `ProcessMethod`, `Expression`, `TimelineEvent`, `Composition`. A cartridge adds one typed extension payload and does not change core fields. Cartridge #2 adds `SpiceExtension`. Cartridge #3 adds `CoffeeTeaExtension`, which is a discriminated union over the `coffea` and `camellia_sinensis` genera. [Sources: World Spice Atlas Specification.docx, coffee specs.docx]

**Shared gate.** Each cartridge runs the same pipeline: `compiler/fetch.py` -> `license_gate.py` -> `dissolve.py` -> `tippecanoe` -> `pmtiles`. The gate aborts the build on any ODbL, share-alike, non-commercial, GADM or MPL input. [Source: Global Spice GI Geospatial Inventory.docx]

**Shared rule - provenance over completeness.** Cartridge #2 and #3 both separate corpus-verified records from placeholders. Cartridge #2 uses `PENDING_SOURCING` and a `data_readiness` enum. Cartridge #3 uses a ten-value `ProvenanceStatus` enum, including `PENDING_SENSORY_PANEL` and `PENDING_COMPOSITION_AUDIT`. Unverified records stay out of the index. [Sources: World Spice Atlas Specification.docx, coffee specs.docx]

### Cartridge #2 - World Spice and Chili, scale

The specification fixes the catalogue counts. Only the geospatial inventory states the region total, and it gives a range. [Sources: World Spice Atlas Specification.docx, Global Spice GI Geospatial Inventory.docx]

| Item | Count | Source |
|---|---|---|
| Regional expressions | 65 | Specification |
| Regional blends, pastes and seasonings ("Map Your Blend") | 35 | Specification |
| Diffusion milestones | 35 | Specification |
| Automated validation rules | 15 | Specification |
| Flagship spice and chili regions (polygon assembly) | 55-62 | Geospatial inventory |

The geospatial inventory gives a regional split: Europe 12-13, Asia 22-23, Americas 12-14, Middle East and Africa 9-12. The counts are ranges because some regions are still contested at polygon level. [Source: Global Spice GI Geospatial Inventory.docx]

Readiness is not uniform. Of the 65 expressions, 30 have botanical, analytical, processing or GI records in the current evidence base. The other 35 are expansion slots marked `PENDING_SOURCING`. Of the 35 blends, ingredient links and regulatory flags are mapped, but percentage ratios and coordinates are placeholders. Of the 35 milestones, 18 modern events carry verified dates. Of the 15 validator rules, 7 are fully grounded, 4 partly grounded and 4 are structural invariants. [Source: World Spice Atlas Specification.docx]

Two 2025-2026 analytical standards drive the chemistry layer. ISO 3632-1:2025 adds an Extra Class tier above Category I for saffron. ASTA Method 21.3 (2026) revises capsaicinoid response factors and shifts calculated Scoville heat by a factor of 0.9431 against 2004 values. [Source: World Spice Atlas Specification.docx]

### Cartridge #3 - Coffee and Tea, scale

| Item | Count | Source |
|---|---|---|
| Regional expressions | 60 | Specification |
| Cup and blend compositions | 30 | Specification |
| Historical diffusion arcs | 30 | Specification |
| Automated factual accuracy guardrails | 15 | Specification |
| Origin entries | 63 | Geospatial inventory |
| Producing countries and territories | 24 | Geospatial inventory |
| Coffee origins | 36 | Geospatial inventory |
| Tea origins | 27 | Geospatial inventory |

The two documents agree on the origin totals: 63 entries over 24 countries, split 36 coffee and 27 tea. The inventory counts 19 coffee-producing countries in its coffee section. [Source: coffee inventory.docx]

Cartridge #3 splits one crop-level question from Cartridge #1 and #2. Coffee and tea origins are mostly not statutory GI polygons. Colombia, Brazil, India and Sri Lanka publish resolutions, municipality rosters or agro-climatic definitions, not redistributable shapefiles. The build therefore assembles ADM1-ADM3 polygons from FAO GAUL 2024/2025, World Bank Official Boundaries, Natural Earth 1:10m, audited HDX COD-AB, Brazil IBGE, Mexico INEGI and Taiwan NLSC. Non-administrative terroirs (Sri Lanka's seven agro-climatic tea zones, Darjeeling at 600-2,000 m, Nilgiri at 1,000-2,500 m) are masked with MapSPAM crop allocation and elevation data. [Source: coffee inventory.docx]

### Cartridge #1 - spirits expansion (shipped)

The 2026-11-25 expansion document proposed 185 expressions and 120 cocktails. The live build on 2026-11-26 exceeds that: 300 expressions and 112 cocktails. The earlier caution not to cite 185 and 120 as current is retired. Cite the verified build numbers instead. [Source: World Spirits Atlas Expansion.docx; verified 2026-11-26]

### Brand and monetization

Two brands: a consumer umbrella hosting all atlases as subdirectories, and a separate developer brand for the open-source engine. The split avoids a site-wide "built with" footer badge, which Google's link-spam policy names as a spam signal. Monetization is museum-shop style: giclee map prints, FSRS study packs for spirits certification, disclosed affiliates, and privacy-first sponsorship. No programmatic display ads. [Source: World Spirits Atlas Growth Strategy.docx]

### Why it may matter here

It is a clean example of a domain-agnostic product with typed primitives and licence gates built into the pipeline. That pattern transfers to any structured-catalogue product. The spirits content itself is outside the current trading and genealogy lanes.

### Verified build state (2026-11-26)

- 313 tile features: 285 statutory, 18 cultural regions, 10 generic. 261 statutory features are EU spirit GIs, plus 7 country ring fallbacks and 17 feature references. The EU register total is 265.
- 300 expressions, 112 cocktails, 35 timeline milestones.
- 160 pilot URLs across 5 segmented sitemaps; all 160 returned HTTP 200 with a trailing-slash canonical. The static build has 588 routes; 429 remain `noindex`.
- 15 accuracy guardrails in `packages/data-validator/tests/accuracy.test.ts`; 15 tests present.
- Legal layer: 643 clause records (581 unique verbatim quotes) in a 32.7 KB Brotli shard, from 162 of 165 specification PDFs.
- Distilleries: 5,578 TTB rows, 5,572 geocoded (99.89%), in a 107 KB Brotli shard.
- 17 attribution licences: 16 upstream plus `atlas-derived-ccby4`. No ODbL layer.
- The licence gate has 20 deny patterns, including MPL-2.0.
- Dependency audit: 455 packages passed on 2026-11-25. Astro `^6.4.8`, Tailwind `^3.4.17`.
- Code is MIT. Curated data is CC BY 4.0 (`LICENSE`, `DATA_LICENSE`).
- Mexico: 181 Tequila, 35 Bacanora and 17 Raicilla municipalities, dissolved from HDX ADM2 with INEGI upstream.

### Open questions

- [OPEN QUESTION 2026-11-25] Whether the operator wants this on `ROADMAP.md`.
- **Decision 2026-11-25:** the repo stays private until launch. Flip it to public on 2026-12-01, before the article drops.
- [OPEN QUESTION 2026-11-25] `terroirkit.dev` does not resolve.

### Licence conflict - resolved for curated data, open for tiles

**Decision 2026-11-25: CC BY 4.0 governs the curated data.** That covers the expressions, cocktails, and dated milestones. It is the architecture document's term, and it matches the project's own zero-copyleft constraint. The growth document's CC BY-SA label is the outlier and should be corrected upstream.

**Corroborated 2026-11-26.** The Cartridge #3 geospatial inventory states the whole build as "MIT code, CC BY 4.0 curated data". That is an independent second document. So two documents now agree on CC BY 4.0 for the curated data, against one earlier CC BY-SA label. The finding is strengthened, and it now covers a cartridge, not just the spirits data. Note the scope limit: the inventory states the build licence in its opening summary. It does not audit the licence of every upstream layer. [Source: coffee inventory.docx]

**The tiles are a separate question and cannot be settled the same way.** The architecture lists Overture Maps divisions and selected geoBoundaries layers as inputs, and both **inherit ODbL from OpenStreetMap**. ODbL is share-alike. If the published tile set contains Overture- or OSM-derived geometry, a share-alike obligation attaches to the derived database, and CC BY-SA is then closer to correct than CC BY 4.0 for that download.

So the growth document may not be simply wrong. It may be describing the tiles rather than the data.

**Before any public release, one check decides it:** list which source dataset each published tile layer derives from, and confirm whether any is ODbL. If none is, publish CC BY 4.0 throughout. If any is, label that layer share-alike and keep the curated data at CC BY 4.0 - the two can differ, because they are different works.

This is `[OPEN QUESTION 2026-11-25]`, not a verified fact: no build exists, so there is nothing to inspect yet.

**Resolved on inspection 2026-11-26.** `cartridges/spirits/dist/attribution.json` lists 17 licences: 16 upstream plus `atlas-derived-ccby4`. No layer is ODbL. The basemap is Natural Earth (Public Domain); the other layers are OGL v3.0, Licence Ouverte 2.0, CC BY 4.0, CC0/Public Domain, CC BY-IGO 3.0 and MLIT. All 313 features carry `license_id`, and the six tile keys include it. The tile share-alike question is closed for v1.

**One wording risk remains.** `DATA_LICENSE` applies a blanket CC BY 4.0 to files under `cartridges/*/data/` and `cartridges/*/dist/`. The compiled `dist/` geometry includes OGL, CC BY-IGO and Licence Ouverte material. A compilation can carry CC BY 4.0 while upstream layers keep their terms, but the licence text should say that explicitly. `[OPEN QUESTION 2026-11-25]`

### Routing

Roadmap candidate, filed as "Atlas Engine (candidate)" in `ROADMAP.md`. Not routed to Atto, GuruWatcher, Basgiath, CeminiDFS or CeminiParlays. No trading or betting link.

The scope grew on 2026-11-26 from one cartridge to three, plus a 120-expression spirits expansion. The engine and its licence gate are still the transferable part. The spice, coffee and spirits content is still outside the trading and genealogy lanes.
