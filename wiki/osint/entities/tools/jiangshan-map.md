---
title: jiangshan-map — historical jurisdiction cartography (GPL-3.0)
type: entity
tags: [tool, cartography, genealogy, atto, gpl]
keywords: [jiangshan-map, semantic URL router, historical boundaries, polygon]
related:
  - concepts/historical-jurisdiction-atlas.md
  - sources/eval-multi-wiki-link-revenue-v10.9-2026-10-25.md
maturity: draft
created: 2026-10-25
updated: 2026-10-25
phase_0_verdict: CONDITIONAL-GO — pattern only, no code
wire_status: wont_wire
wire_note: GPL-3.0. Re-implement the ?year=&place= contract over ISTAT data. Never copy code or GeoJSON into Atto.
---

## Raw Concept

Phase-0 on [DeanChensj/jiangshan-map](https://github.com/DeanChensj/jiangshan-map), 2026-10-25. Triggered by the v10.9 multi-wiki link evaluation (URL 10), which scored it Extract for Atto and family-tree.

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | https://github.com/DeanChensj/jiangshan-map |
| **Stack** | JavaScript, HTML, CSS. Canvas/Parchment Casing border rendering. |
| **Stars** | 1.3k (155 forks), per report |
| **Last commit** | 2026-10-25 (verified by clone) |
| **Size** | 43 MB / 82 files |
| **License** | **GPL-3.0** — verified 2026-10-25. The source report recorded "NOT FOUND". |
| **Verdict** | CONDITIONAL-GO — take the URL contract and interaction pattern only |

### What it does

An interactive map of Chinese dynastic territories from 403 BCE to present. Two features carry the value:

- **Trace Place** — a genealogical panel showing which jurisdiction held a place, in which era.
- **Modern X-Ray Lens** — historical boundaries drawn over modern ones.

### The reusable contract

```
?year=1845&place=Napoli,Avellino
```

The agent emits a year and a place name, both taken from the record. The client resolves coordinates and boundaries. **The agent never formats a latitude.** That removes a whole class of hallucination from FIND deep-links.

### Why it is CONDITIONAL-GO and not GO

The licence is GPL-3.0. Atto vendors nothing copyleft. So this is a **design reference**: read the interaction, re-implement the contract over ISTAT administrative data. No code, no assets, no GeoJSON.

Known defect: issue #158 reports rendering lag with heavy polygons loaded at once. Any Atto implementation must lazy-load boundaries by era and region.

### Where it lands

Atto Access share (20/mo) and Concierge (>=$2,500) deliverables; family-tree dogfood. Methodology page: @concepts/historical-jurisdiction-atlas.md.

## Snippets

> "its semantic URL router (?year=1079,1080&place=...) eliminates LLM coordinate hallucination by allowing the agent to pass only extracted dates and place names" — source report, URL 10

## Dead Ends

- Copying the map renderer. GPL-3.0.
- Loading all province polygons on one frame. Issue #158 says it lags.
