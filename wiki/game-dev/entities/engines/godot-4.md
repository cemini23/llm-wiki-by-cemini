---
title: Godot 4 — hobby engine candidate
type: entity
tags: [entity, engine, godot, phase-0]
keywords: [godot, godot-4, isometric, rts, grid-building, mit-license, astargrid2d]
related:
  - concepts/vertical-slice-v0.md
  - concepts/scope-tiers.md
  - concepts/stronghold-deconstruction.md
  - entities/tools/claude-code-game-studios.md
  - concepts/godot-3d-sh2-architect-spike-plan.md
  - concepts/operator-vision-sh2-personal-clone.md
  - entities/projects/castle-sim.md
  - sources/godot-4-phase-0-audit-2026-06-13.md
  - concepts/art-pipeline-v0-requirements.md
  - concepts/deferred-engine-candidates.md
  - concepts/godot-pathfinding-patterns.md
  - concepts/rts-pathfinding-approaches.md
  - entities/tools/hi-godot-ai.md
  - entities/tools/gamedevbench.md
  - sources/gamedevbench-phase-0-audit-2026-06-21.md
  - sources/kobold-tactics-tilemap-pathfinding-2023.md
  - sources/liquid-fire-godot-tactics-pathfinding-2024.md
  - sources/morinaga-shin-koikoi-claude-godot-2026.md
  - sources/pchojecki-catvivors-claude-code-steam-2026.md
  - sources/vav-labs-godot-flow-fields-2026.md
  - sources/vav-labs-astargrid2d-gotchas-2026-06-22.md
  - sources/gdquest-pathfinding-glossary-2026-06-23.md
  - sources/godot-rts-rpg-youtube-watchlist-2026-06-23.md
maturity: validated
created: 2026-06-13
updated: 2026-06-23
---

## Relations

- @concepts/godot-3d-sh2-architect-spike-plan.md — **Fork B** 3D SH2 line (2026-06-13)
- @concepts/operator-vision-sh2-personal-clone.md — fork locked
- @concepts/vertical-slice-v0.md — 2D slice gate (historical); 3D spike supersedes presentation
- @concepts/stronghold-deconstruction.md — pathfinding flagged high risk; mitigated below
- @image-gen-wiki/index.md — sprite/tile art pipeline
- @sources/godot-4-phase-0-audit-2026-06-13.md — audit trail (clone + kit scan)

## Raw Concept

Phase-0 **CONDITIONAL-GO** — 2D spike validated; **3D SH2 clone** is active presentation target (Fork B).

## Narrative

### Why Godot for this project

- MIT license, Mac-native editor (Apple Silicon universal)
- **3D (Fork B):** `NavigationAgent3D`, CSG/instanced walls, orthographic architect camera — SH2 build fantasy
- **2D (legacy):** `AStarGrid2D` + TileMap — sim logic prototype; do not extend presentation
- Agent codegen corpus strong for GDScript
- RTS MP not built-in — defer

### Phase-0 audit (2026-06-13)

Audit method: clone `godotengine/godot` @ `4.5.2-stable` to `/tmp/godot-audit/`, download Mac universal editor, scan grid-building kits for hardcoded paths, cross-read navigation docs.

#### 1. License — GO

| Check | Result |
|-------|--------|
| SPDX | **MIT** [CONFIRMED] — `LICENSE.txt` in tag `4.5.2-stable` |
| Commercial / hobby | Permitted, no royalty |
| Export | No runtime fee; export templates same license |

#### 2. Mac editor — GO

| Check | Result |
|-------|--------|
| Latest stable (Jun 2026) | **4.6.3** on [godotengine.org/download/macos](https://godotengine.org/download/macos/) (May 2026); audited binary **4.5.2-stable** |
| Apple Silicon | Universal **arm64 + x86_64** binary [CONFIRMED] — `file` on downloaded `.app` |
| Smoke test | `Godot --version` → `4.5.2.stable.official`; headless `--quit-after 1` exits clean on operator Mac [CONFIRMED 2026-06-13] |
| Distribution | Code-signed & notarized (Prehensile Tales B.V.) per official download page |
| Failure modes | Third-party macOS window managers (Magnet, Swish) reported to cause editor input lag — disable if seen [TENTATIVE] |
| Pin recommendation | **4.5.2-stable** (audited) or **4.6.x stable**; avoid preview builds for slice |

Use **standard** (GDScript) build, not .NET, unless C# is explicitly chosen.

#### 3. Grid-building kits — CONDITIONAL (no drop-in for v0)

Scanned kits in `/tmp/godot-audit/kits/` (primarily [MarkoDM/GodotInGameBuildingSystemGDS](https://github.com/MarkoDM/GodotInGameBuildingSystemGDS)).

| Kit | Dims | License | Stars | Updated | Hardcoded paths | v0 fit |
|-----|------|---------|-------|---------|-----------------|--------|
| MarkoDM GDS | 3D | MIT | 28 | 2024-05 | **None** — only portable `res://` refs | **Poor** — 3D survival demo, not isometric 2D walls |
| MarkoDM C# | 3D | MIT | 76 | 2024-05 | Same | **Poor** — requires .NET build |
| CityCrafter3D | 3D proc | MIT | 86 | 2025-12 | Addon path only | **NO-GO** — procedural city gen, not player wall draw |
| Maaack/A-Star-Grid-Map | 2D | MIT | 2 | 2026-03 | AssetLib install | **Maybe** — bridges TileMap → `AStarGrid2D`; evaluate in spike |

**Finding:** No mature, maintained **2D isometric wall-draw** kit found. MarkoDM grid-cell occupancy pattern is useful reference logic but wrong dimensionality for `@concepts/vertical-slice-v0.md`.

**Slice approach (recommended):**

1. `TileMapLayer` with isometric `TileSet` for walls/ground
2. Custom placement controller (~100–200 LOC) — snap mouse via `local_to_map`, validate occupancy
3. Mirror placed wall cells into `AStarGrid2D` via `set_point_solid` (do **not** call `update()` after toggles — it resets solids [CONFIRMED docs issue #8893])

Optional: borrow MarkoDM **grid cell occupancy** ideas; do not vendor the 3D project wholesale.

#### 4. Pathfinding risk — CONDITIONAL-GO (architecture chosen, spike required)

Stronghold-style dynamic walls are the highest engineering risk in v0 (@concepts/stronghold-deconstruction.md). Godot offers two stacks:

| Approach | Dynamic walls | v0 unit count (~10) | Risk |
|----------|---------------|---------------------|------|
| **`AStarGrid2D` + grid sync** | `set_point_solid` per cell — O(1), no rebuild | Excellent | **LOW** if walls stay gridded |
| **`NavigationRegion2D` rebake** | Rebake on each wall segment | Poor — tile-heavy meshes slow queries | **HIGH** — avoid for v0 |
| **`NavigationAgent2D` RVO avoidance** | Soft obstacles only; does not affect pathfind | Overkill for peasants | **MEDIUM** perf cost if enabled on all agents |

**Recommended v0 stack:** `AStarGrid2D` aligned to wall `TileMapLayer`; peasants request `get_id_path` / `get_point_path` on job assign and when a wall changes (local invalidation, not global rebake). Before committing a wall segment, speculatively set cell solid and verify a path still exists from spawn to trees (maze-seal prevention) [TENTATIVE — pattern from community writeups].

**Known failure modes:**

- Unreachable target → full polygon search; expensive if navmesh over-tiled — mitigated by small grid + grid A*
- Calling `AStarGrid2D.update()` after `set_point_solid()` → **clears all solids** [CONFIRMED]
- Using avoidance agents for every peasant every frame → documented perf cliff

**Spike gate (before feature work):** 20×20 grid, draw/remove walls, 5 peasants path to trees — must hold 60 fps on operator Mac for 10 minutes.

#### 5. Engine comparison (brief)

| Engine | Verdict for Tier 1 |
|--------|-------------------|
| **Godot 4** | **CONDITIONAL-GO** — best fit for 2D isometric hobby slice |
| Unity | Heavier install; Personal license OK but less aligned with wiki/agent GDScript corpus |
| Bevy | Rust ECS; no editor parity for tile art — **NO-GO** for art-heavy isometric slice |

### Adoption posture

| Verdict | **CONDITIONAL-GO** |
|---------|----------------------|
| Unblocks `castle-sim` repo? | **Yes** — meets vertical-slice gate |
| Conditions | (1) Pin 4.5.2 or 4.6.x stable; (2) custom TileMap + `AStarGrid2D`, no kit dependency; (3) pass pathfinding spike above |

## Snippets

### Pin version in new project

```ini
# project.godot
config/features=PackedStringArray("4.5", "Forward Plus")
```

### Isometric grid snap (TileMapLayer)

```gdscript
var cell: Vector2i = wall_layer.local_to_map(wall_layer.to_local(get_global_mouse_position()))
var snapped: Vector2 = wall_layer.map_to_local(cell)
```

### Wall → pathfinding sync

```gdscript
func set_wall_solid(cell: Vector2i, blocked: bool) -> void:
    astar.set_point_solid(cell, blocked)
    # Do NOT call astar.update() here — resets all solids
```

### Phase-0 clone command

```bash
git clone --depth 1 --branch 4.5.2-stable https://github.com/godotengine/godot.git /tmp/godot-audit/godot
```

## Dead Ends

- **MarkoDM building system as dependency** — 3D-only, stale (2024), no pathfinding hook; reference patterns only.
- **NavigationRegion2D rebake per wall** — documented perf trap for tile-dense maps; defer unless unit count jumps to RTS scale.
