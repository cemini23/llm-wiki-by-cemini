---
title: Atlas Engine — multi-vertical geospatial atlas, cartridge #1 spirits
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

From three operator documents dated 2026-11-25: an architecture document, a technical and pedagogical specification, and a growth and monetization playbook. No code repository exists in this workspace at ingest time.

**Status: NEW PROJECT. Not on the roadmap yet.** No page in `wiki/osint/` described an Atlas Engine before this ingest. `concepts/historical-jurisdiction-atlas.md` shares the word "atlas" and nothing else, and there is no evidence this is related to Comuni Atlas.

## Narrative

### What it is

A multi-vertical atlas engine: one rendering and data engine, plus per-domain "cartridges". Cartridge #1 is the World Spirits Atlas. Cartridge #2 and later are named as Wine, Coffee and Spice or Tea. The engine is domain-agnostic; the cartridge supplies the content, the legal rules and the sensory taxonomy. [Source: World Spirits Atlas Specification.docx]

### Three layers

**Data.** Zero-copyleft geographic boundaries, sourced from public-domain and permissively licensed national datasets. A licence gate runs in code and aborts the build on any ODbL, share-alike, non-commercial or GADM source. Legal standards of identity are pulled from machine-readable government APIs, not scraped prose. [Source: Open World Spirits Atlas Architecture.docx]

**Schema.** Six universal typed interfaces, shared by every vertical: `OriginRegion`, `BaseMaterial`, `ProcessMethod`, `Expression`, `TimelineEvent`, `Composition`. A vertical-specific extension carries the rest. Validation is part of the schema: dual ABV thresholds, contested-GI versioning, and a mandatory pedagogical sibling for every expression. [Source: World Spirits Atlas Specification.docx]

**Delivery.** A static build: PMTiles vector tiles plus Brotli-compressed JSON shards, rendered in MapLibre. The estimated payload is 6.7 to 11.6 MB against a 15 MB ceiling. A generic repository layout puts domain recipes in `cartridges/<domain>/` so a new vertical needs no code change.

### Content scope at launch

65 flagship regional expressions across six families: whisk(e)y, agave, cane and rum, botanicals and amari, grape and orchard brandies, and Asian and grain spirits. 35 multi-region cocktails under a "Map Your Glass" feature. 35 timeline milestones. Fifteen validator unit tests. [Source: World Spirits Atlas Specification.docx]

### Brand and monetization

Two brands: a consumer umbrella hosting all atlases as subdirectories, and a separate developer brand for the open-source engine. The split avoids a site-wide "built with" footer badge, which Google's link-spam policy names as a spam signal. Monetization is museum-shop style: giclée map prints, FSRS study packs for spirits certification, disclosed affiliates, and privacy-first sponsorship. No programmatic display ads. [Source: World Spirits Atlas Growth Strategy.docx]

### Why it may matter here

It is a clean example of a domain-agnostic product with typed primitives and licence gates built into the pipeline. That pattern transfers to any structured-catalogue product. The spirits content itself is outside the current trading and genealogy lanes.

### Open questions

- [OPEN QUESTION 2026-11-25] No repository, build or measurement exists. The byte budget is an allowance, not a measured build.
- [NEEDS VERIFICATION 2026-11-25] License conflict: the architecture document says curated data is CC BY 4.0, while the growth document labels the free map download CC BY-SA. Resolve before any public release.
- [OPEN QUESTION 2026-11-25] Whether the operator wants this on `ROADMAP.md`. That file is outside this ingest's scope.

### Routing

Roadmap candidate. Not routed to Atto, GuruWatcher, Basgiath, CeminiDFS or CeminiParlays. No trading or betting link.
