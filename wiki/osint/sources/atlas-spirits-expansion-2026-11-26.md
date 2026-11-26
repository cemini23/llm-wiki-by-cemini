---
title: "World Spirits Atlas expansion — 120 net-new expressions and 85 cocktails"
type: source
related:
  - concepts/atlas-engine.md
updated: 2026-11-26
read_status: skimmed
maturity: draft
---

## Raw Concept

| Field | Value |
|-------|--------|
| Title | World Spirits Atlas Expansion Catalog: 120 Net-New Regional Expressions and 85 Map Your Glass Cocktails |
| Author | Operator document, no named author |
| Type | Operator document, .docx, content catalogue |
| Location | `research to be indexed/osint/World Spirits Atlas Expansion.docx` |
| Retrieved | 2026-11-26 |
| Pages | 467 blocks, 12 tables |
| Read status | skimmed (method, family counts and legal baselines; individual rows sampled) |

## Narrative

### What it is

A data package that doubles and then some the Cartridge #1 catalogue. Spirits expressions rise from 65 to 185, an addition of 120. Cocktails rise from 35 to 120, an addition of 85. The output is JSON-ready Markdown tables, not a built site. [Source: World Spirits Atlas Expansion.docx]

### Expression additions by family

| Family | Added | Running total |
|---|---|---|
| Whisk(e)y | +24 | — |
| Agave and desert | +18 | — |
| Cane and rum | +20 | — |
| Botanicals, amari and liqueurs | +28 | — |
| Grape and orchard brandies | +16 | — |
| Asian and grain spirits | +14 | — |
| **Total** | **+120** | **185** |

### Cocktail additions by family

Whiskey 20, cane and tiki 18, agave 7, gin and botanical 14, brandy and pisco 11, aperitivo and low-ABV 15. Total 85, bringing the catalogue to 120. The set is designed to complete the IBA 2024 official list of 102 cocktails plus modern craft benchmarks.

### Why the entries are narrow

The author could not inspect the live 65-expression spine. Every new entry therefore targets a sub-regional micro-terroir, a single-still marque or a protected sub-appellation. Generic anchors are deliberately excluded: Kentucky Bourbon, London Dry Gin, generic Espadín mezcal, Martinique AOC rhum agricole, and the eleven core cocktails (Negroni, Manhattan, Dry Martini, Sazerac, Daiquiri, Margarita, Mai Tai, Pisco Sour, Caipirinha, Penicillin, Paper Plane). This is the right fix for an unreadable baseline. It also means the package cannot confirm that no duplicate exists.

### Schema conventions

- ID prefixes carry meaning: `exp_` net-new expression, `reg_` origin, `spine_` baseline anchor, `mod_` vermouth, liqueur or bitter, `pantry_` juice and syrup.
- `SensoryProfile7Axis` is seven slash-delimited integers on 0–10: sweetness, fruit-floral, herbal-botanical, spice-pepper, oak-wood, smoke-peat, intensity-body.
- Cocktail ingredients are `ingredient_id|measure_ml|role|(lat,lon)`, with WGS84 origin coordinates per ingredient.

### Legal corrections worth keeping

The document corrects several commercial tasting-chart errors:

- **Scotland has five protected designations, not six.** Regulation 10 of the Scotch Whisky Regulations 2009 defines three regions (Highland, Lowland, Speyside) and two localities (Islay, Campbeltown). "Islands" is not statutory. Skye, Orkney, Jura, Arran and Mull fall in Highland.
- **Mezcal smoke is a process variable, not a category.** NOM-070-SCFI-2016 defines three production categories and six maturation classes. Clay-pot distillation gives texture without automatically more smoke.
- **Rum taxonomy turns on esters and still architecture.** Jamaica codifies four marques from Common Clean to Continental Flavoured. Guyana's EU-protected GI covers three wooden heritage stills at Diamond.
- **Peru and Chile make different spirits.** Peru's INDECOPI DO bans rectification, dilution and wood ageing. Chile's Decreto 521 permits all three.

### Honest limits

Statutory detail not verified in primary legal texts is marked `[UNVERIFIED: ...]` in place, which is the correct handling. Cocktail provenance that rests on standard historiography rather than bar records is marked `c.` or `(disputed)`. The spine baseline was not inspected, so duplicate risk is unmeasured.

### Read

Use this page for the family counts and for the legal corrections. Treat the records themselves as unreviewed drafts until they pass the existing validator.
