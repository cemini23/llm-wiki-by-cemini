---
title: K282 — level editors and tile tooling (routed brief, landed 2026-10-05)
type: source
tags: [source, triage, briefs, tooling, tilemap, cross-wiki]
keywords: [tiled, sprytile, axial, better-tile-editor, fabricmoddingconventions, tilemap]
related:
  - concepts/rts-pathfinding-approaches.md
  - concepts/godot-pathfinding-patterns.md
  - concepts/minecraft-data-driven-content-patterns.md
  - entities/projects/castle-sim.md
  - sources/cross-wiki-routed-briefs-2026-10-05.md
  - meta/cross-wiki-routing.md
  - sources/k284-k285-basgiath-clip-tooling-2026-10-08.md
read_status: read
source_type: operator-triage
maturity: validated
created: 2026-10-05
updated: 2026-10-07
---

## Raw Concept

Cross-wiki brief from OSINT batch K282, routed 2026-10-05 and landed here. Of a 20-row eval, **11 rows are level-editor, tilemap, or 2D-engine tooling**. None touches a revenue project, and this wiki's castle-sim is a 3D Godot effort, so the brief was filed as **reference only: 0 Integrate, no install, zero clones.** Recorded now so the routing is auditable.

## Narrative

### Rows worth a stub

| Repo | Why it is noted |
|------|-----------------|
| [`mapeditor/tiled`](https://github.com/mapeditor/tiled) | Canonical TMX and JSON 2D tilemap schema; autotiling and Wang brushes. The reference for orthogonal, hex, and isometric coordinate grids |
| [`Sprytile/Sprytile`](https://github.com/Sprytile/Sprytile) | Blender low-poly UV-paint workflow — paint 2D pixel tiles straight onto 3D meshes |
| [`mateoltd/axial`](https://github.com/mateoltd/axial) | Rust Minecraft client launcher: memory tuning, integrity validation, runtime sandbox management |
| [`cidwel/better-tile-editor`](https://store.godotengine.org/asset/cidwel/better-tile-editor/) | Godot 4.6+ tilemap suite — patch terrains, multi-tile stamping, autotile cliffs, slope tools |

**The one row that matters for castle-sim** is `better-tile-editor`. It targets **Godot 4.6+** and covers terrains, multi-tile stamping, autotile cliffs, and slope tools — the exact surface a Stronghold-style map needs. It is a Godot Asset Store listing, so licence and version support must be checked at the asset page before any use. [TENTATIVE — not audited]

`mapeditor/tiled` matters as a **schema reference**, not a tool to run. Its TMX and JSON map formats are the most widely implemented 2D tilemap interchange format, and the orthogonal/hex/isometric coordinate conventions are worth reading before inventing castle-sim's own map format. See @concepts/rts-pathfinding-approaches.md and @concepts/godot-pathfinding-patterns.md for how grid choice interacts with pathfinding here.

### The instructive rejection

**`brainage04/FabricModdingConventions`** does a real and useful thing — **headless GameTest regression CI** for Minecraft entities and block states — but it is **Java Fabric**, which cannot compile to the Bedrock runtime. Goal match, stack mismatch. This is the second such mismatch recorded in two days (the K283 batch hit the same pattern). The Bedrock equivalent of this capability wants `@minecraft/server` scripting, not Fabric. Recorded as a **pattern worth having**, not a repo to take. Relevant context: @concepts/minecraft-data-driven-content-patterns.md.

### Rows rejected

Seven passes — `Seanba/Tiled2Unity`, `UnityPatterns/TileEditor`, `mapeditor/rs-tiled`, `vnen/godot-tiled-importer`, `RoryDungan/HexTiles`, `paspallas/bonesmith` — all legacy or stack-mismatched. Six rows were **404**.

### Eval-quality warning

**6 of 20 URLs return 404**, several of them `*-Community-2026` repos that read as generated. That is a second wave in two days with a high dead-link rate. Treat the row metrics as leads, not findings. The same warning was raised in K281.

### Boundary

No clones, no install. These notes are reference only.

## Dead Ends

- Installing any of these for castle-sim before the 3D asset pipeline is chosen. Fork B is Godot 3D and the tile lane is a placeholder path.
- Taking `FabricModdingConventions` as a Bedrock tool. It is Java-only.
- Trusting the eval's row metrics. A third of the URLs are dead.
