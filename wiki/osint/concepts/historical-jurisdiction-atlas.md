---
title: Historical jurisdiction atlas — zero-coordinate place resolution
type: concept
tags: [concept, genealogy, cartography, atto, gazetteer]
keywords: [historical jurisdiction, semantic URL router, gazetteer, ISTAT, comune, Atto]
related:
  - sources/eval-multi-wiki-link-revenue-v10.9-2026-10-25.md
  - entities/tools/jiangshan-map.md
maturity: draft
created: 2026-10-25
updated: 2026-10-25
---

## Raw Concept

The question this page answers: **how does an agent show a historical place on a map without inventing coordinates?**

Source: [Source: Multi-Wiki Link Revenue Evaluation v10.9, URL 10 (DeanChensj/jiangshan-map), 2026-10-25]. Related to Atto's in-flight Atlas work and Atto K246 (geospatial computation).

## Narrative

### The failure this fixes

A genealogical record says a person was born in a village in the Kingdom of the Two Sicilies in 1845. The village was a *comune* then. It may be a *frazione* now. The province name changed. The borders changed twice.

If the agent tries to place this, it will produce a plausible latitude and longitude. **That number will be invented.** LLMs are unreliable at recall of coordinates, and a wrong point on a map is worse than no point, because it looks authoritative.

### The contract

[jianshan-map](https://github.com/DeanChensj/jiangshan-map) solves this by removing coordinates from the agent's job entirely.

```
atto-mcp emits:   ?year=1845&place=Napoli,Avellino
client resolves:  jurisdiction boundaries for 1845 at that place
client renders:   historical outline vs modern outline
```

The agent passes only what it read from the record: a year and a place name. The client owns the gazetteer. **The agent never formats a coordinate.**

Three parts make this work:

1. **Semantic URL router.** `?year=&place=` is the whole API. No lat/long, no bounding box, no map ID. Multiple years are allowed (`?year=1079,1080`) so the client can animate a boundary change.
2. **Historical-to-modern overlay.** The client draws the historical jurisdiction and the modern one on the same frame, so the user sees the change rather than being told about it.
3. **Place genealogy panel.** A lineage view: which province held this comune, under which state, in which era.

### Mapping to Italian records

The report's translation of this pattern onto Italian civil records is the useful part:

| jiangshan-map concept | Italian equivalent |
|---|---|
| Dynastic territory | Kingdom of the Two Sicilies, Papal States, Kingdom of Italy |
| Prefecture / county | Provincia, circondario |
| County subdivision | Mandamento |
| Village | Comune, frazione, suppressed comune |
| Boundary change | Unification 1861, provincial redraws, comune mergers |

The data source for the modern side is ISTAT administrative boundaries. The historical side needs a separate gazetteer of suppressed comuni and pre-unification provinces.

### Licence constraint — the blocking fact

**jiangshan-map is GPL-3.0.** Phase-0 confirmed this on 2026-10-25; the source report recorded the licence as "NOT FOUND".

Consequence: Atto takes the **URL contract and the interaction pattern**, not the code, not the assets, not the GeoJSON. Atto's own policy is anti-copyleft vendoring. Re-implement over ISTAT data.

### Performance constraint

Issue #158 on jiangshan-map reports client-side rendering degradation when heavy polygon snapshots load together. Atto must **lazy-load provincial boundary slices by era and by region.** Loading the whole country's boundaries for every query will not hold.

### What this buys

- Removes coordinate hallucination from FIND deep-links.
- Makes the Access share (20/mo) and Concierge (>=$2,500) deliverables visually differentiated.
- Gives the truth gate something checkable: a place name from a record is a fact; a coordinate is a guess.

## Snippets

> "Crucially, its semantic URL router (?year=1079,1080&place=...) eliminates LLM coordinate hallucination by allowing the agent to pass only extracted dates and place names from civil records while the client atlas resolves coordinates." — report, URL 10

> "License: NOT FOUND — do not copy raw map code or assets; re-implement the semantic ?year=&place= URL resolver and historical-to-modern Italian comune gazetteer overlay cleanly inside /Users/claudiobarone/Projects/atto using ISTAT / historical Italian administrative boundary data." — report, URL 10 (licence since confirmed GPL-3.0)

## Dead Ends

- **Copying the map rendering code.** GPL-3.0. Not available to Atto under its vendoring policy.
- **Asking the agent for coordinates.** The whole point of the contract is that it does not.
