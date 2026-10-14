---
title: Deferred engine candidates — post Phase-0 shelf
type: concept
tags: [concept, engine, phase-0, defer]
keywords: [libgdx, duality, java, csharp, engine-eval]
related:
  - entities/engines/godot-4.md
  - concepts/game-dev-wiki-scope.md
  - sources/tool-evaluation-cross-wiki-routing-2026-06-13.md
  - concepts/tool-evaluation-cross-wiki-batch-2026-06-13.md
maturity: draft
created: 2026-06-13
updated: 2026-06-15
---

## Relations

- @entities/engines/godot-4.md — **CONDITIONAL-GO** active choice for castle-sim

## Raw Concept

Engines **deferred** from active Phase-0 (Godot / Unity / Bevy) after 56-target tool eval — revisit in 30–90 days if Godot path fails.

## Narrative

| Engine | Stack | License | Stars | Why defer |
|--------|-------|---------|-------|-----------|
| [libGDX](https://github.com/libgdx/libgdx) | Java | Apache-2.0 | ~25k | Mature cross-platform; expands scope to JVM; no RTS slice investment yet |
| [Duality](https://github.com/AdamsLair/duality) | C# / OpenTK | MIT | ~1.4k | Plugin-based 2D editor + engine; viable if Unity eval deprioritized |

**Re-eval trigger:** Godot vertical slice blocked on 2D tooling for >2 milestones, or operator explicitly requests Java/C# alt.

## Dead Ends

- jMonkeyEngine — 3D Java; out of Stronghold 2D isometric lane
- MonoGame link lists — no license on aggregates; not engines themselves
