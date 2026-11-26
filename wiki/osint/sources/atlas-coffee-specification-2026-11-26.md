---
title: "Atlas Engine cartridge #3 (Coffee and Tea) — domain specification"
type: source
related:
  - concepts/atlas-engine.md
  - sources/atlas-coffee-geospatial-inventory-2026-11-26.md
  - sources/atlas-coffee-seo-blueprint-2026-11-26.md
updated: 2026-11-26
read_status: skimmed
maturity: draft
---

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Atlas Engine Cartridge 3 Coffee and Tea Domain Specification |
| Author | Operator document, no named author |
| Type | Operator document, .docx, technical specification |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/coffee specs.docx` |
| Retrieved | 2026-11-26 |
| Pages | 321 blocks, 7 tables |
| Read status | skimmed (schema, scope and calibration sections; sample records not read line by line) |

## Narrative

### What it is

The `CoffeeTeaExtension` schema and content plan for Cartridge #3. It keeps the six universal primitives and adds a provenance-tagged payload for two crops that cannot share fields: `coffea` and `camellia_sinensis`. [Source: coffee specs.docx]

### Scope

| Item | Count |
|---|---|
| Regional expressions | 60 |
| Cup and blend compositions | 30 |
| Historical diffusion arcs | 30 |
| Automated factual accuracy guardrails | 15 |
| Coffee expressions | 35 |
| Tea expressions | 25 |

### The discriminated union

Coffee and tea are modelled as two branches of one type. Botanical, processing and sensory fields never coerce across genera, so a tea cannot inherit a coffee process enum.

Two live taxonomic disputes are preserved rather than flattened:

- **Liberica.** A 2006 Kew review merged `Coffea excelsa` and `C. dewevrei` into `C. liberica` var. `dewevrei`. A 2025 phylogenomic study splits broad-sense Liberica into three species and raises recognized `Coffea` species from 131 to 133. The schema keeps `excelsa` as the operational key, `Coffea dewevrei` as the binomial, and a `taxonomicVintageNote` that records both positions.
- **Cambodiensis.** Agronomic practice recognises `var. lasiocalyx` as a third tea variety. Kew POWO lists it as a synonym under `var. assamica`. The schema keeps `cambodiensis` as a first-class key with a `powoCanonicalSynonym` pointer.

This is the correct pattern for any catalogue that outlives a taxonomy revision: keep the working key, store the binomial, and record the vintage.

### Provenance instead of defaults

A ten-value `ProvenanceStatus` enum covers the whole record: `VERIFIED_PRIMARY`, `VERIFIED_LAB_PANEL`, `FAMILY_ANCHOR_BASELINE`, `TRADITIONAL_ATTRIBUTION`, `SECONDARY_TRADE_REPORT`, and four pending states, including `PENDING_SENSORY_PANEL`, `PENDING_HARVEST_DATA`, `PENDING_BREW_CALIBRATION` and `PENDING_COMPOSITION_AUDIT`.

The consequence is visible in the data. All unbenchmarked numeric sensory vectors are null, not estimated. Anaerobic fermentation is a supported enum value with zero verified lots in v1. Five of the 30 compositions (Masala Chai, Earl Grey, Jasmine Pearl, Cà Phê Sữa Đá, Cuban Cortadito) are declared cross-cartridge stubs because the doses do not exist in the evidence base.

### Sensory calibration crosswalk

The sweetener in the design is a normalisation layer. Three protocols are mapped onto one 0–10 intensity axis while keeping quality separate from intensity:

- SCA 103-2024 rates section intensity on 0–15 and uses Check-All-That-Apply over 110+ WCR Lexicon attributes.
- CQI's 2019 Fine Robusta protocol rates quality on 0–10 in quarter-point steps from 6.
- Tea QDA studies use 0–10 intensity for taste and aroma.

Brewing reference anchors are family-level, not estate-level: green tea about 1:50 at 80–85 °C, black tea about 1:75 at 85–90 °C, oolong at 1:15 gongfu, pu-erh at 1:30 Western.

### Honest limits

The document flags its own error rate. A Darjeeling Terai coordinate printed in one micromorphology paper, 24.9742 N 78.4716 E, is called out as a source anomaly because it falls outside West Bengal. City and estate coordinates stay `PENDING_GEOCODING_LOOKUP` across the timeline.

### Count note

The specification counts 60 expressions as 35 coffee plus 25 tea. The same cartridge's geospatial inventory counts 63 origin entries as 36 coffee plus 27 tea. These are different units: expressions are catalogue records, origins are boundary units. Both can be true. Do not reconcile them into one number.
