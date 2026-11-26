---
title: "FlavorOrigins cartridge #3 (Coffee and Tea) — organic search and launch blueprint"
type: source
related:
  - concepts/atlas-engine.md
  - sources/atlas-coffee-specification-2026-11-26.md
  - sources/atlas-coffee-geospatial-inventory-2026-11-26.md
  - sources/atlas-spice-growth-strategy-2026-11-26.md
updated: 2026-11-26
read_status: skimmed
maturity: draft
---

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Organic Search and Launch Blueprint for FlavorOrigins Cartridge #3: Coffee and Tea |
| Author | Operator document, no named author |
| Type | Operator document, .docx, SEO and launch plan |
| Location | `research to be indexed/osint/Coffee & Tea SEO Blueprint.docx` |
| Retrieved | 2026-11-26 |
| Pages | 254 blocks, 6 tables |
| Read status | skimmed (positioning, tools, taxonomy and cluster sections) |

## Narrative

### What it is

The go-to-market plan for `flavororigins.com/coffee-tea/`. It is the third of the three cartridge plans and the most technical of them. [Source: Coffee & Tea SEO Blueprint.docx]

### Position

Existing specialty beverage sites split agronomy, chemistry and palate training into separate silos:

- **Roaster maps** (Moustache, Maillard, Morning Fix) give introductory pins and narrative, and one of them states that static origin atlases age quickly.
- **World Coffee Research** publishes the primary botanical reference — 55 Arabica and 47 Robusta varieties — plus Sensory Lexicon 2.0, but it is built for farmers and breeders, not for search.
- **Tea atlases** (Tealytics with 52 countries, 158 regions and 313 places) document provenance without modelling how elevation, shading or oxidation creates flavour.
- **Brew loggers** (Beanconqueror, Filtru, Beanie with 40,000+ coffees) hold the telemetry inside native apps that search engines cannot index.
- **Credentials** cost $900 to $3,225 for tea programmes, and the SCA took over the Q Grader programme on 1 October 2025.

The gap is a free, indexed, interactive reference that joins all five.

### Three interactive tools, all crawlable

- **Dual-rendered elevation and terroir maps.** Semantic HTML elevation tables first, then D3 and MapLibre hydration. Every region node is an `<a href>`, so a crawler and a keyboard user can traverse it.
- **Cultivar-to-chemistry matrices.** Coffee: WCR lineages (Typica, Bourbon, Ethiopian landraces, Catimor and Sarchimor introgressions, F1 hybrids such as Centroamericano H1) against altitude, leaf-tip colour and rust resistance. Tea: propagation biology against volatile mechanism — steaming locks in cis-3-hexenol, shading raises S-methylmethionine which converts to dimethyl sulfide in gyokuro, roasting forms pyrazines in hojicha.
- **Browser-based FSRS study decks.** `ts-fsrs` v6, drill on the nine Evolved Q Grader assessments and the Agtron 63 roast standard.

### Search reality as of November 2026

The document records a policy timeline that matters for any programmatic site:

| Change | Effective date |
|---|---|
| HowTo rich results retired | 2023 |
| CourseInfo, LearningVideo, PracticeProblem phased out | 2025–2026 |
| Commercial FAQPage rich results discontinued | 7 May 2026 |
| Scaled Content Abuse policy update | 28 August 2026 |

Consequence: JSON-LD must match visible DOM text and must not chase retired rich-result types. Visibility now comes from proprietary data tables, named attribution and engagement.

### Cross-cartridge linking

Same rule as the spice plan: inline body links only, where a shared volatile compound or infusion physics justifies the jump. Footer link farms and repetitive anchors are prohibited. Where the compound data does not exist for a target, the pipeline must not emit the link.

### Rollout

Programmatic publishing is gated on row uniqueness, not URL volume. The document cites Google's John Mueller from September 2026: thin legacy pages can weigh on a site's perception long after edits begin. One intent, one owner URL. Route taxonomy covers regions, varieties, comparisons, chemistry, history, quiz and study tools.

### Discrepancy to resolve

The document again says a 21 November 2026 domain index listed `flavororigins.com` as available for registration. The verified build records v1 live at that domain on 25 November 2026. [OPEN QUESTION 2026-11-26] Resolve registrar and DNS state before staging.

### Honest limits

Keyword-level search volume and confirmed live slugs inside `/spirits/` and `/spices/` were absent. The 40 clusters are ranked by intent and differentiation, not by volume. Cross-cartridge links need pre-launch route validation, because the target pages are not yet verified to exist.
