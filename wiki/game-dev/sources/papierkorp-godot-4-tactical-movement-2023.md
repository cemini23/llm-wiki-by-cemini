---
title: papierkorp — grid tactical movement in Godot 4.2 (2023)
type: source
tags: [source, godot, tilemap, movement, tutorial]
keywords: [papierkorp, tilemap, range, hover-layer, godot-4]
related:
  - concepts/godot-pathfinding-patterns.md
  - sources/kobold-tactics-tilemap-pathfinding-2023.md
  - sources/shaggydev-udd-navigation-2025.md
read_status: read
source_type: tutorial
source_url: https://papierkorp.github.io/blog/posts/godot-4-tactical-movement
maturity: validated
created: 2026-06-13
updated: 2026-06-13
---

## Relations

- @concepts/godot-pathfinding-patterns.md — Pattern 2 reachable-area preview (simpler variant)

## Raw Concept

Beginner Godot 4.2 tutorial: **Manhattan range** move highlighting on multi-layer TileMap with custom data (`water`, `tree` obstacles).

## Narrative

### Techniques [CONFIRMED]

- TileSet custom data layers for terrain rules
- Separate TileMap layers: `floor`, `obstacle`, `hover`, `hoverTemp`
- Move range = nested loops `abs(i)+abs(j) <= range` — **not A\***; instant UI preview
- `local_to_map` / `map_to_local` for click-to-move snap
- Illegal move feedback via temp hover tile + 2s timer

### castle-sim relevance

| Tutorial | castle-sim v0 |
|----------|---------------|
| Turn-based range highlight | Defer — real-time job assign |
| Custom data on tiles | **Use** for wall/tree/passable |
| Multi-layer hover paint | Optional "peasant reach" debug overlay |
| No pathfinding around walls | **Do not copy** — use AStarGrid2D + @sources/shaggydev-udd-navigation-2025.md |

Good **UI/debug** reference; path logic is weaker than spike requirements.

### Quality note [TENTATIVE]

First-project tutorial — architecture is monolithic (player script owns tilemap ops). Prefer Navigation service pattern for castle-sim.

## Snippets

Nearest texture filter for pixel art: `Project Settings → Rendering → Textures → Default Texture Filter: Nearest`

## Dead Ends

- Manhattan range without obstacle path — fails M0 "path around wall" requirement
