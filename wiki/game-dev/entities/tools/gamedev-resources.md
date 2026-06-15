---
title: GameDev-Resources — curated asset index (reference-only)
type: entity
tags: [entity, tool, assets, reference, cc0]
keywords: [gamedev-resources, opengameart, polyhaven, assets]
related:
  - concepts/art-pipeline-v0-requirements.md
  - concepts/tool-evaluation-cross-wiki-batch-2026-06-13.md
  - sources/tool-evaluation-cross-wiki-routing-2026-06-13.md
maturity: validated
created: 2026-06-13
updated: 2026-06-13
cross-wiki-stub: @image-gen-wiki
---

## Relations

- @image-gen-wiki — ComfyUI generation (this repo is **static asset links only**)

## Raw Concept

[`Kavex/GameDev-Resources`](https://github.com/Kavex/GameDev-Resources) — CC0-1.0 curated markdown list of free game dev assets, tools, and audio (~2.7k★).

## Narrative

### Posture

**Reference-only** — no executable logic. Use as link index when sourcing v0 placeholders.

### Priority links for castle-sim v0

| Resource | Use |
|----------|-----|
| [OpenGameArt](https://opengameart.org/) | 2D sprites, tilesets (Kenney-style placeholders) |
| [Poly Haven](https://polyhaven.com/) | PBR textures (if 3D props later) |
| Free sound/music sections in list | UI + ambient (verify per-asset license) |

Handoff: @concepts/art-pipeline-v0-requirements.md placeholder checklist.

### Verdict

**GO** for bookmarking — CC0 list itself is safe to cite; **verify each downstream asset license** before shipping in castle-sim.

## Snippets

v0 placeholder sourcing order:

```
1. Kenney / OpenGameArt (explicit CC0/CC-BY)
2. Procedural color tiles in-engine (zero IP)
3. @image-gen-wiki generation when art milestone starts
```
