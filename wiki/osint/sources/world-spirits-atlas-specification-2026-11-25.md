---
title: "Atlas Engine cartridge #1 (World Spirits) — schema and pedagogical specification"
type: source
related:
  - concepts/atlas-engine.md
  - sources/world-spirits-atlas-architecture-2026-11-25.md
  - sources/world-spirits-atlas-growth-strategy-2026-11-25.md
updated: 2026-11-25
---

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Cartridge #1 (World Spirits): Master Atlas Engine Technical and Pedagogical Specification |
| Author | Operator document, no named author |
| Type | Operator document, .docx, technical specification |
| Location | `research to be indexed/osint/World Spirits Atlas Specification.docx` |
| Retrieved | 2026-11-25 |
| Pages | 272 paragraphs, 9 tables |
| Read status | read (schema section in full; family lists and checklist) |

## Narrative

### What it is

The data model for the first atlas cartridge, written as typed TypeScript and JSON interfaces. It binds six domain-agnostic primitives to a spirits-specific extension, and it fixes the content scope: 65 launch expressions, 35 cocktails and 35 timeline milestones. [Source: World Spirits Atlas Specification.docx]

### The six universal primitives

The same interfaces serve every future vertical, whether Wine, Coffee or Tea:

| Primitive | Role |
|---|---|
| `OriginRegion` | Nested region with centroid, boundary reference, climate zone and GI protection status |
| `BaseMaterial` | Botanical taxon, material class, sugar or starch type, conversion requirement |
| `ProcessMethod` | Stage, apparatus, temperature or pressure regime, chemical impact |
| `Expression` | The product, as region times material times process, plus tasting notes and benchmarks |
| `TimelineEvent` | Dated milestone with coordinates and migration arcs |
| `Composition` | A cocktail, with each ingredient's measured volume and historical origin |

Two design choices are worth copying. Coordinates are stored as explicit WGS84 `lat`/`lng` objects and converted to GeoJSON `[lng, lat]` tuples only at the rendering boundary, which prevents coordinate-inversion bugs. Years are integers and may be negative for BCE.

### Domain extension

`SpiritsExtension` attaches to every expression. It carries a botanical taxonomy, legal compliance fields and a mandatory seven-axis sensory profile on a 0 to 10 scale, plus cocktail provenance. The extension is where vertical-specific logic lives, so the core graph stays clean.

### Validation, not prose

The specification encodes legal constraints as machine checks rather than notes:

- **Dual ABV thresholds.** `origin_min_abv` and `us_import_min_abv` are separate, because Mexican domestic bottling permits 35% while US import rules require 40%. A single threshold would reject compliant bottles.
- **Contested-GI versioning.** Regions under litigation or delayed registration are tagged `contested_gi` with a `last_verified_date`, so a statutory change triggers an audit alert.
- **Referential integrity.** Every expression must name a pedagogical sibling, enforced as a foreign key, so each page renders a side-by-side comparison.

Fifteen validator unit tests are specified. The paper states the regulatory baselines in force through 2025–2026: the TTB American Single Malt final rule effective January 2025, the JSLMA labelling standard enforced April 2024, India's FSSAI single malt definition effective March 2024, and EU Regulation 2019/787.

### The legal asymmetry caveat

The document is careful about what a geographical indication means. Scotch, Cognac, Tequila and Martinique Rhum Agricole sit on binding statutory protection. The Japanese Whisky standard is a voluntary industry code, and Plymouth Gin's EU GI lapsed in 2015. Several GIs are contested. It also separates legal provenance from sensory claim: a "100% de Agave" Tequila may still carry up to 1 percent undisclosed additives by weight.

### Honest limits

The 65 expressions are a launch list, not a complete corpus. The document is a specification; no validator code ships with it. The unit-test list is a requirement, not a passing suite.

### Reuse value

This is the reusable core of the project: a typed, vertical-agnostic schema with validation rules attached. Any future atlas vertical can reuse the six primitives unchanged.
