---
title: "Atlas Engine cartridge #2 (World Spice and Chili) — technical specification"
type: source
related:
  - concepts/atlas-engine.md
  - sources/atlas-spice-geospatial-inventory-2026-11-26.md
  - sources/atlas-spice-growth-strategy-2026-11-26.md
updated: 2026-11-26
read_status: read
maturity: draft
---

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Cartridge 2 World Spice and Chili Atlas Technical Specification |
| Author | Operator document, no named author |
| Type | Operator document, .docx, technical specification |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/World Spice Atlas Specification.docx` |
| Retrieved | 2026-11-26 |
| Pages | 269 blocks, 6 tables |
| Read status | read (schema, counts, readiness and validator sections) |

## Narrative

### What it is

The data model and content plan for Cartridge #2 on the terroirkit Atlas Engine. It keeps the six universal primitives and puts every spice-specific field inside a typed `SpiceExtension` payload, so Cartridge #1 records are not changed. [Source: World Spice Atlas Specification.docx]

The document states its own rules of evidence at the top. Every section separates corpus-verified data from structural placeholders marked `PENDING_SOURCING`. Each expression also carries a `data_readiness` value: `CORPUS_VERIFIED`, `PARTIAL_VERIFIED` or `PENDING_SOURCING`.

### Scope

65 regional expressions, 35 regional blends, 35 diffusion milestones and 15 automated validation rules.

Readiness across those records:

| Record set | Verified | Partial | Awaiting sourcing |
|---|---|---|---|
| 65 expressions | 30 | — | 35 |
| 35 blends | ingredient links and flags | ratios and coordinates | — |
| 35 milestones | 18 modern events with dates | 5 pre-modern | 12 early |
| 15 validator rules | 7 grounded | 4 partial | 4 structural |

[Source: World Spice Atlas Specification.docx]

### The extension

`SpiceExtension` carries six spice families, ten plant parts, six pungency mechanisms, method-versioned Scoville intervals, aroma compounds with assay wavelengths, a solubility profile, `/spirits/` botanical backlink IDs, a seven-axis sensory model and a compliance block.

Four design choices are worth copying:

- **The extension is a payload, not a subclass.** `Expression<TExt>` is generic. Cartridge #2 adds a payload and never mutates core fields.
- **Every coordinate carries provenance.** `GeoPoint.provenance` is either `VERIFIED_COORDINATE` or `PENDING_SOURCING`. A placeholder cannot pass as a measurement.
- **Method versioning is a field.** `ScovilleRange.analytical_method` names the assay, and `normalized_2026_typical` holds the rescaled value.
- **Compliance is data.** Coumarin limits, EU mycotoxin caps and saffron grades are typed fields with numbers, not prose.

### Analytical standards

Two 2025–2026 revisions drive the chemistry layer.

**ISO 3632-1:2025**, published 7 July 2025, replaces the 2011 saffron standard. It adds an Extra Class above Category I. Extra Class requires crocin at 440 nm of at least 230, picrocrocin at 257 nm of at least 80, and safranal at 330 nm between 30 and 50. Category I raises the crocin floor from 190 to 200.

**ASTA Method 21.3 (2026)** updates capsaicinoid response factors and shifts calculated Scoville heat units by a factor of 0.9431 against 2004 values. The 2004 method phases out over five years, to April 2031. On a benchmark mixture the same lot reads about 5.6 to 5.8 percent lower after recalibration, with no change in sensory heat.

The document is careful about the limit of each assay. UV-Vis cannot detect water-soluble adulterants such as tartrazine. Crocin isomers co-absorb at 330 nm, so a safranal reading near 42 can sit over an actual content of 0.17 mg/g. The compliance block therefore enforces certificate-of-analysis date tracking instead of treating a grade label as permanent.

### Regulatory layer

Three constraints attach to blends automatically:

- **Coumarin.** Cassia-based blends trigger an EFSA/BfR alert at a tolerable daily intake of 0.1 mg/kg body weight. At an average cassia level of 3,000 mg/kg, a 70 kg adult reaches the limit at about 2.33 g per day. Ceylon cinnamon at 15 mg/kg shifts that threshold to about 467 g per day.
- **Solvent polarity.** Aqueous steeping keeps coumarin low. Ethanolic extraction of cassia, as in vermouth or liqueur infusion, extracts far above the daily threshold.
- **Contaminants and allergens.** EU Regulation 2023/915 limits attach to any dried Capsicum blend. Pink peppercorn carries a cashew and pistachio cross-reactivity flag.

### Honest limits

This is a specification, not a build. The TypeScript is described as an idiomatic reconstruction, because the Cartridge #1 source files were not available to the author. No validator code ships. All 35 expansion slots stay `PENDING_SOURCING`, including the four that carry a narrow partial anchor, and most blend ratios are empty.

### Reuse value

The pattern is the point: a generic join entity, a typed payload, and readiness flags on every field. Any catalogue product with mixed evidence quality can copy it.
