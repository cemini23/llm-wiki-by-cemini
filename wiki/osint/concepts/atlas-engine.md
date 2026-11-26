---
title: Atlas Engine - multi-vertical geospatial atlas, cartridge #1 spirits
type: concept
maturity: draft
related:
  - sources/world-spirits-atlas-architecture-2026-11-25.md
  - sources/world-spirits-atlas-specification-2026-11-25.md
  - sources/world-spirits-atlas-growth-strategy-2026-11-25.md
updated: 2026-11-25
---

## Raw Concept

Question this page answers: what is the Atlas Engine, what is in cartridge #1, and is this a new project?

From three operator documents dated 2026-11-25: an architecture document, a technical and pedagogical specification, and a growth and monetization playbook. At ingest time no code repository existed. A working build now exists at `~/Projects/Atlas101`, remote `github.com/cemini23/flavororigins`.

**Status: BUILT - v1 live at flavororigins.com/spirits/ (verified 2026-11-25).** No page in `wiki/osint/` described an Atlas Engine before this ingest. `concepts/historical-jurisdiction-atlas.md` shares the word "atlas" and nothing else, and there is no evidence this is related to Comuni Atlas.

## Narrative

### What it is

A multi-vertical atlas engine: one rendering and data engine, plus per-domain "cartridges". Cartridge #1 is the World Spirits Atlas. Cartridge #2 and later are named as Wine, Coffee and Spice or Tea. The engine is domain-agnostic; the cartridge supplies the content, the legal rules and the sensory taxonomy. [Source: World Spirits Atlas Specification.docx]

### Three layers

**Data.** Zero-copyleft geographic boundaries, sourced from public-domain and permissively licensed national datasets. A licence gate runs in code and aborts the build on any ODbL, share-alike, non-commercial or GADM source. Legal standards of identity are pulled from machine-readable government APIs, not scraped prose. [Source: Open World Spirits Atlas Architecture.docx]

**Schema.** Six universal typed interfaces, shared by every vertical: `OriginRegion`, `BaseMaterial`, `ProcessMethod`, `Expression`, `TimelineEvent`, `Composition`. A vertical-specific extension carries the rest. Validation is part of the schema: dual ABV thresholds, contested-GI versioning, and a mandatory pedagogical sibling for every expression. [Source: World Spirits Atlas Specification.docx]

**Delivery.** A static build: PMTiles vector tiles plus Brotli-compressed JSON shards, rendered in MapLibre. Measured 2026-11-25: the basemap PMTiles is 2.1 MB, the spirits GeoJSON fallback is 56 KB, and the shards are 156 KB. The full static build is 11 MB against a 15 MiB ceiling. A generic repository layout puts domain recipes in `cartridges/<domain>/` so a new vertical needs no code change.

### Content scope at launch

65 flagship regional expressions across six families: whisk(e)y, agave, cane and rum, botanicals and amari, grape and orchard brandies, and Asian and grain spirits. 35 multi-region cocktails under a "Map Your Glass" feature. 35 timeline milestones. Fifteen validator unit tests. [Source: World Spirits Atlas Specification.docx]

### Brand and monetization

Two brands: a consumer umbrella hosting all atlases as subdirectories, and a separate developer brand for the open-source engine. The split avoids a site-wide "built with" footer badge, which Google's link-spam policy names as a spam signal. Monetization is museum-shop style: giclee map prints, FSRS study packs for spirits certification, disclosed affiliates, and privacy-first sponsorship. No programmatic display ads. [Source: World Spirits Atlas Growth Strategy.docx]

### Why it may matter here

It is a clean example of a domain-agnostic product with typed primitives and licence gates built into the pipeline. That pattern transfers to any structured-catalogue product. The spirits content itself is outside the current trading and genealogy lanes.

### Verified build state (2026-11-25)

- 60 regions, 0 fallback. 65 expressions, 35 cocktails, 35 timeline milestones.
- 103 pilot URLs across 5 segmented sitemaps; all 103 returned HTTP 200 with a canonical tag. The static build has 222 pages; 118 remain `noindex, follow`.
- 15 accuracy guardrails in `packages/data-validator/tests/accuracy.test.ts`. 20/20 data and accuracy tests pass, 35/35 compiler tests pass, 6/6 browser smoke tests pass.
- The licence gate has 20 deny patterns, including MPL-2.0. 12 sources approved; 26 pinned files verified.
- 455 npm packages pass the dependency audit. Astro `^6.4.8`, Tailwind `^3.4.17`.
- Code is MIT. Curated data is CC BY 4.0 (`LICENSE`, `DATA_LICENSE`).
- Mexico: 181 Tequila, 35 Bacanora and 17 Raicilla municipalities, dissolved from HDX ADM2 with INEGI upstream.

### Open questions

- [OPEN QUESTION 2026-11-25] Whether the operator wants this on `ROADMAP.md`.
- **Decision 2026-11-25:** the repo stays private until launch. Flip it to public on 2026-12-01, before the article drops.
- [OPEN QUESTION 2026-11-25] `terroirkit.dev` does not resolve.

### Licence conflict - resolved for curated data, open for tiles

**Decision 2026-11-25: CC BY 4.0 governs the curated data.** That covers the expressions, cocktails, and dated milestones. It is the architecture document's term, and it matches the project's own zero-copyleft constraint. The growth document's CC BY-SA label is the outlier and should be corrected upstream.

**The tiles are a separate question and cannot be settled the same way.** The architecture lists Overture Maps divisions and selected geoBoundaries layers as inputs, and both **inherit ODbL from OpenStreetMap**. ODbL is share-alike. If the published tile set contains Overture- or OSM-derived geometry, a share-alike obligation attaches to the derived database, and CC BY-SA is then closer to correct than CC BY 4.0 for that download.

So the growth document may not be simply wrong. It may be describing the tiles rather than the data.

**Before any public release, one check decides it:** list which source dataset each published tile layer derives from, and confirm whether any is ODbL. If none is, publish CC BY 4.0 throughout. If any is, label that layer share-alike and keep the curated data at CC BY 4.0 - the two can differ, because they are different works.

This is `[OPEN QUESTION 2026-11-25]`, not a verified fact: no build exists, so there is nothing to inspect yet.

**Resolved on inspection 2026-11-25.** `cartridges/spirits/dist/attribution.json` lists 14 upstream licences. No layer is ODbL. The basemap is Natural Earth (Public Domain); the other layers are OGL v3.0, Licence Ouverte 2.0, CC BY 4.0, CC0/Public Domain, CC BY-IGO 3.0 and MLIT. All 60 features carry `license_id`, and the six tile keys include it. The tile share-alike question is closed for v1.

**One wording risk remains.** `DATA_LICENSE` applies a blanket CC BY 4.0 to files under `cartridges/*/data/` and `cartridges/*/dist/`. The compiled `dist/` geometry includes OGL, CC BY-IGO and Licence Ouverte material. A compilation can carry CC BY 4.0 while upstream layers keep their terms, but the licence text should say that explicitly. `[OPEN QUESTION 2026-11-25]`

### Routing

Roadmap candidate. Not routed to Atto, GuruWatcher, Basgiath, CeminiDFS or CeminiParlays. No trading or betting link.
