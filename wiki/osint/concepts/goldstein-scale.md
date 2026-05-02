---
title: Goldstein scale
type: concept
tags: [concept, alt-data, events, intensity-metric]
keywords: [goldstein-scale, conflict-cooperation, event-intensity, gdelt, cameo, macro-regime]
related:
  - entities/data-sources/gdelt.md
  - concepts/cameo-codes.md
maturity: validated
created: 2026-04-23
updated: 2026-05-02
---

## Relations

- @entities/data-sources/gdelt.md
- @concepts/cameo-codes.md — CAMEO event codes form the taxonomy to which Goldstein intensity scores attach. Bidirectional: cameo-codes references this page for intensity scoring.

## Raw Concept

Stub created during Phase 3 lint to close dangling ref from an entity page. Expand on deep-read.

## Narrative

The **Goldstein scale** is a -10 to +10 conflict/cooperation intensity
metric assigned to each CAMEO-coded event in GDELT. It was originally
developed by Joshua Goldstein (1992) for the KEDS project to quantify
event data for quantitative international relations research, building
on the WEIS event taxonomy that CAMEO later extended.

### Scale anchors

| Score | Interpretation |
|-------|----------------|
| +10 | Formal alliance, unification, voluntary merger |
| +7 to +9 | High cooperation: military aid, strategic partnership |
| +3 to +6 | Moderate cooperation: diplomatic visit, economic agreement |
| +1 to +2 | Low cooperation: public statement of support, expression of optimism |
| 0 | Neutral event or observation |
| -1 to -2 | Low conflict: mild criticism, diplomatic protest |
| -3 to -5 | Moderate conflict: sanctions, troop mobilization, border violation |
| -6 to -8 | High conflict: artillery/missile attack, assassination |
| -9 to -10 | Extreme conflict: full-scale military assault, mass casualties |

Each CAMEO event code maps to a fixed Goldstein score. For example,
CAMEO 0251 ("Appeal for easing of administrative sanctions") maps to a
moderate positive value; CAMEO 193 ("Armed battle") maps to -10. The
mapping is maintained by the GDELT project.

### Goldstein severity

GDELT also computes **Goldstein severity** = `abs(Goldstein scale)`,
used as a 25% weight in the Event Significance formula (alongside
CAMEO+ magnitude, systemic importance, propagation potential, market
sensitivity, fatality counts, article evidence, and confidence). Severity
treats extreme cooperation and extreme conflict symmetrically — both
are "high impact" events.

### CAMEO+ scope

In GDELT 2.0 / CAMEO+, the Goldstein scale is present for all Conflict
events and for CAMEO+ Political domain events. It is null for
non-political CAMEO+ domains (Economic, Corporate, Technology, etc.)
where the cooperation/conflict axis is not meaningful.

### Cemini usage

Cemini computes rolling per-country Goldstein aggregates (mean,
min, max, and volatility over 7/30/90-day windows) as:
- A country-instability predictor feeding the Macro Weather regime
  classifier
- A feature in the 3-29-research-4 Bayesian deep-learning model for
  macro-regime classification
- An adverse-shock trigger: when a country's 7-day mean Goldstein drops
  below -5, the Kalshi strategy executes BatchCancelOrders for that
  country's event contracts

## Snippets

- "Goldstein scale from -10 conflict to +10 cooperation" — [Source: https://docs.gdeltcloud.com/ (retrieved 2026-05-02)]
- "Event significance combines Goldstein severity where meaningful, CAMEO+ magnitude/systemic/propagation/market metrics where present, fatality presence for Conflict Events, article evidence volume, and confidence" — [Source: https://docs.gdeltcloud.com/api-reference (retrieved 2026-05-02)]
- "Goldstein scale is present for all Conflict Events. Present for CAMEO+ POLITICAL Events. Null for non-political CAMEO+ domains." — [Source: https://docs.gdeltcloud.com/api-reference (retrieved 2026-05-02)]
