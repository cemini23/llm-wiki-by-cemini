---
title: CAMEO codes (Conflict and Mediation Event Observations)
type: concept
tags: [concept, alt-data, events, schema, taxonomy]
keywords: [cameo, cameo-plus, event-coding, gdelt, quadclass, conflict-mediation, taxonomy]
related:
  - entities/data-sources/gdelt.md
  - concepts/goldstein-scale.md
maturity: validated
created: 2026-04-23
updated: 2026-05-02
---

## Relations

- @entities/data-sources/gdelt.md
- @concepts/goldstein-scale.md — Goldstein scale assigns -10 to +10 intensity values to each CAMEO-coded event. Bidirectional: goldstein-scale references this page for the taxonomy.

## Raw Concept

Stub created during Phase 3 lint to close dangling ref from an entity page. Expand on deep-read.

## Narrative

**CAMEO** (Conflict and Mediation Event Observations) is the event-type
taxonomy used by GDELT to classify news events. It was originally
developed as an extension of the WEIS (World Event/Interaction Survey)
coding scheme, adding mediation- and conflict-specific subcategories.
The taxonomy has been adopted with modifications by ICEWS and forms
the backbone of GDELT 1.0 and 2.0 event coding.

### Hierarchical structure

CAMEO uses a three-level numeric coding system:

| Level | Example | Description |
|--------|---------|-------------|
| Root (2 digits) | `02` | "Appeal" |
| Base (3 digits) | `025` | "Appeal to yield" |
| Full (4 digits) | `0251` | "Appeal for easing of administrative sanctions" |

The hierarchy enables aggregation at multiple resolutions: root-level
for broad trend analysis, full-code for granular event tracking.

### QuadClass — top-level aggregation

All CAMEO events fall under four primary classifications:

| QuadClass | Code | Description |
|-----------|------|-------------|
| Verbal Cooperation | 1 | Public statements of support, diplomatic consultation |
| Material Cooperation | 2 | Aid provision, military cooperation, economic agreements |
| Verbal Conflict | 3 | Criticism, threats, diplomatic protest |
| Material Conflict | 4 | Armed conflict, sanctions enforcement, property seizure |

### Root categories (2-digit)

The 20 root categories span from cooperative to conflictual:

- **01** — Make public statement
- **02** — Appeal
- **03** — Express intent to cooperate
- **04** — Consult
- **05** — Engage in diplomatic cooperation
- **06** — Engage in material cooperation
- **07** — Provide aid
- **08** — Yield
- **09** — Investigate
- **10** — Demand
- **11** — Disapprove
- **12** — Reject
- **13** — Threaten
- **14** — Protest / Demonstrate
- **15** — Exhibit force posture
- **16** — Reduce relations
- **17** — Coerce
- **18** — Assault
- **19** — Fight
- **20** — Engage in unconventional mass violence

Each category branches into 3-digit and 4-digit subcategories with
specific behavioral descriptions. The codebook includes formal
descriptions and extensive examples for each code. [Source: CAMEO
Manual 1.1b3, retrieved 2026-05-02]

### CAMEO+ domain expansion

GDELT 2.0 extends CAMEO beyond political events with **CAMEO+** — nine
domains that code non-political events alongside traditional CAMEO:

| Domain | Scope |
|--------|-------|
| POLITICAL | CAMEO 01–17 diplomatic, cooperative, and non-violent coercive events |
| ECONOMIC | Monetary policy, fiscal policy, trade, currency events, sovereign debt |
| CORPORATE | M&A, bankruptcies, leadership changes, supply chain shocks |
| TECHNOLOGY | AI capability, cyber operations, space, strategic tech controls |
| INFRASTRUCTURE | Energy, transport, communications infrastructure disruptions |
| ENVIRONMENT | Geophysical, meteorological, climate, pollution events |
| HEALTH | Disease outbreaks, pandemics, health policy crises |
| DEMOGRAPHIC | Refugee flows, migration, population crises, labor events |
| INFORMATION | Disinformation campaigns, information controls, major leaks |

Each CAMEO+ event carries four AI-derived latent scores: magnitude
(0–10 domain-specific intensity), systemic importance (0–1),
propagation potential (0–1), and market sensitivity (0–1).

### Cemini usage

Cemini aggregates CAMEO event counts per country-window, filtered by
QuadClass and root category, and correlates with asset-price moves to
generate macro-regime features. Combined with the Goldstein scale for
intensity, CAMEO codes form the event-structure backbone of
GDELT-derived signals. The CAMEO+ Economic and Corporate domains are
of particular interest for financial-event surveillance.

## Snippets

- "CAMEO event codes are defined in a three-level taxonomy... EventBaseCode yields its level two leaf root node... EventRootCode defines the root-level category." — [Source: GDELT 2.0 Events Column Labels, https://github.com/linwoodc3/gdelt2HeaderRows (retrieved 2026-05-02)]
- "The entire CAMEO event taxonomy is ultimately organized under four primary classifications: Verbal Cooperation, Material Cooperation, Verbal Conflict, and Material Conflict." — [Source: GDELT 2.0 QuadClass documentation (retrieved 2026-05-02)]
- "Three principles underlie the CAMEO actor coding system. First, codes are composed of one or more three-character elements... Second, the codes are interpreted hierarchically... Third, we are basing our work on standardized codes." — [Source: CAMEO Manual 1.1b3, http://data.gdeltproject.org/documentation/CAMEO.Manual.1.1b3.pdf (retrieved 2026-05-02)]
