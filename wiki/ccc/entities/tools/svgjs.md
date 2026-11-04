---
title: "svg.js — modular SVG runtime: path morphing, polygon sampling, constrained select (MIT)"
type: entity
tags: [tool, svg, javascript, game-time, atto, geometry]
keywords: [svg.js, pathmorphing, topoly, svg.select, svg.resize, polygon sampling, map overlay]
related:
  - "@osint-wiki/sources/eval-multi-wiki-link-revenue-v10.11-2026-11-03.md"
maturity: draft
created: 2026-11-03
updated: 2026-11-03
---

## Raw Concept

Surfaced by @osint-wiki/sources/eval-multi-wiki-link-revenue-v10.11-2026-11-03.md, URL 11, **Extract** tier. Routed to game-time and Atto.

The question this page answers: **what does a browser need to animate a border and hit-test a shape?**

## Narrative

### What it is

**MIT.** A modular SVG library for the browser, where each capability is a separate plugin. The report names three that matter:

| Plugin | What it does | Use |
|--------|--------------|-----|
| `svg.pathmorphing.js` | Interpolate one path into another | Animated territory borders |
| `svg.topoly.js` | Convert a path to a polygon and sample points along it | Hit-testing an irregular region |
| `svg.select.js` + `svg.resize.js` | Constrained bounding-box selection and resize | Annotating a scanned record, or a card's centering overlay |

### Why these three, not the library

The interesting property is that each is independently loadable. A project that needs polygon hit-testing does not have to take the animation engine, and one that needs the editor controls does not have to take either.

That matters more than it sounds. SVG libraries have a habit of being taken whole, and then a shipped bundle carries a path-morphing engine that is never called.

### The game-time fit

A strategy map with changing borders is exactly a path-morphing problem, and clicking a province is exactly a polygon hit-test. Both are the kind of thing that is easy to specify and slightly wrong to hand-roll — the naive hit-test uses the bounding box and gets the corners wrong.

If game-time is ever started, these are two small, MIT-licensed pieces that each solve one well-defined geometry problem.

### The Atto fit — narrower than the report implies

The report suggests `svg.select.js` and `svg.resize.js` for "constrained bounding-box selectors" over civil-record scans.

That is a UI control, and Atto already treats the record image as local and never shipped anywhere. A resize handle in a local UI is fine. The thing to avoid is letting a generic crop-box control become a *measurement* — a box drawn by hand is an annotation, not a calibrated reading. If a box is ever used to extract a value, it needs to be a fact about the record, not a gesture.

### Caveats

- Plugin licenses can differ from the core. Check the plugin, not just the repo.
- Path morphing requires compatible path structures — differing node counts produce awkward interpolation unless normalised first.

### Status

Extract. Two plugins, both small, both MIT-verifiable.

## Snippets

> "Pulls modular SVG path morphing, path-to-polygon sampling (toPoly), and constrained resize handlers into /Users/claudiobarone/Projects/game-time/briefs/ and /Users/claudiobarone/Projects/atto" — report, URL 11

## Dead Ends

- **Taking the whole library for one plugin.** The modular split is the point.
- **Treating a hand-drawn crop box as a measurement.** It is an annotation.
