---
title: "theatre.js — keyframe animation studio/core split (Apache-2.0 core, AGPL studio)"
type: entity
tags: [tool, animation, javascript, licence-split, game-time]
keywords: [theatre js, keyframe, studio, core, apache-2.0, agpl, timeline, dom animation]
related:
  - "@osint-wiki/sources/eval-multi-wiki-link-revenue-v10.11-2026-11-03.md"
maturity: draft
created: 2026-11-03
updated: 2026-11-03
---

## Raw Concept

Surfaced by @osint-wiki/sources/eval-multi-wiki-link-revenue-v10.11-2026-11-03.md, URL 8, **Extract** tier. Routed to game-time for UI micro-interactions and cutscene timelines.

The question this page answers: **can you get a designer-grade animation editor without shipping a copyleft licence?**

## Narrative

### What it is

A JavaScript animation library split into two packages:

| Package | Role | Licence |
|---------|------|---------|
| `@theatre/core` | The **runtime**. Playback of keyframe state in a shipped bundle. | **Apache-2.0** |
| `@theatre/studio` | The **editor**. The timeline UI a developer uses to author. | **AGPL-3.0** |

The idea is that you author in the studio and ship only the core — keyframes become JSON, and the runtime plays them back.

### Phase-0, 2026-11-03

Verified at the package manifest: `@theatre/core` `package.json` declares `"license": "Apache-2.0"`, version **0.7.0**. The split the report describes is real.

**But the split is a discipline, not a guarantee.** Nothing in npm prevents a build from pulling `@theatre/studio` into a shipped bundle. AGPL's network clause is triggered by *use over a network*, so a browser game that shipped studio code would be in scope.

That means the licence safety of this choice depends on a build-time check, not on the package names. If it is adopted, enforce it:

- `@theatre/studio` restricted to `devDependencies`.
- A bundle assertion that fails the build if studio code is present.
- A note in the project's licence policy gate.

Without those three, the Apache-2.0 story is a hope.

### Why it fits game-time

The design brief describes a browser strategy game with era transitions and a semantic-zoom map. Those are precisely the things that look cheap when hand-animated with CSS transitions and expensive when they need a timeline. A keyframe editor plus a small runtime is the right shape.

### Caveats

- **0.7.0** is pre-1.0. Pin the version.
- The studio is a React application. It is a development tool, not a dependency of the game.
- The authoring workflow is only as good as the person using it; a timeline editor does not produce good motion by itself.

### Status

Extract, **conditional on the build gate**. Adopt the pattern only with the studio exclusion enforced.

## Snippets

> `@theatre/core` `package.json`: `"license": "Apache-2.0"`, version `0.7.0`. [fetched 2026-11-03]

> "Apache-2.0 for @theatre/core (shipped bundle); AGPL-3.0 for @theatre/studio (design/dev editor only)" — report, URL 8

## Dead Ends

- **Treating "core is Apache-2.0" as sufficient.** The guarantee comes from the build check, not the package metadata.
