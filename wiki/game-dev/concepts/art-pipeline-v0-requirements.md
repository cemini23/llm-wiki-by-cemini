---
title: Art pipeline v0 — placeholder requirements (Godot import)
type: concept
tags: [concept, art, godot, isometric, image-gen]
keywords: [isometric, tiles, sprites, tileset, placeholder, comfyui]
related:
  - concepts/vertical-slice-v0.md
  - meta/sibling-wiki-inventory.md
  - entities/engines/godot-4.md
  - entities/projects/castle-sim.md
  - entities/tools/gamedev-resources.md
  - sources/gamedev-resources-phase-0-audit-2026-06-13.md
  - sources/tool-evaluation-cross-wiki-routing-2026-06-13.md
maturity: draft
created: 2026-06-13
updated: 2026-06-13
---

## Relations

- @image-gen-wiki/index.md — **primary** for generation technique (ComfyUI, LoRA)
- @image-gen-wiki/entities/uis/comfyui.md
- @image-gen-wiki/concepts/two-pass-generation-workflow.md
- @concepts/vertical-slice-v0.md — v0 needs no final art

## Raw Concept

Minimum art spec for Tier 1 vertical slice — placeholders acceptable; final pipeline owned by image-gen-wiki.

## Narrative

### v0 art bar (playtest gate)

Vertical slice v0 does **not** require Stronghold-quality pre-rendered isometric art. Accept:

- Flat-color or Kenney-style placeholder tiles
- [OpenGameArt](https://opengameart.org/) CC0/CC-BY assets — index via @entities/tools/gamedev-resources.md
- [Poly Haven](https://polyhaven.com/) — PBR reference if 3D props added later
- Single wall segment, tree, peasant, archer silhouettes
- 32×16 or 64×32 isometric cell (match `TileSet` tile shape)

### Godot import target

| Asset | Godot node | Notes |
|-------|------------|-------|
| Ground + walls | `TileMapLayer` + isometric `TileSet` | Y-sort enabled |
| Units | `Sprite2D` or `AnimatedSprite2D` | 8-dir optional later |
| Buildings | Tile or scene instance | Stockpile = 1×1 tile minimum |

Import path: PNG tilesheet → TileSet atlas → assign collision + custom data layer for “blocks pathfinding”.

### Generation handoff (when ready)

Route to @image-gen-wiki for:

1. Isometric tile sheet prompt / LoRA style lock
2. Two-pass workflow for wall crenellation variants
3. Batch export with consistent light direction (Stronghold uses fixed NW lighting on pre-rendered assets [TENTATIVE])

**Stub only here** — do not duplicate ComfyUI runbooks.

### Sibling pages to read first

See @meta/sibling-wiki-inventory.md § image-gen-wiki.

## Snippets

```
v0 placeholder checklist:
[x] 1 ground tile
[x] 1 wall segment (+ optional crenellation variant)
[x] 1 tree resource node
[x] 1 peasant walk cycle (4 frames OK)
[x] 1 archer + projectile sprite
```
