---
title: Godot 4 RTS RPG — YouTube watchlist — 2026-06-23
type: source
tags: [source, godot, rts, youtube, watchlist]
keywords: [godot, rts, rpg, tutorial, youtube, transcript]
related:
  - concepts/godot-pathfinding-patterns.md
  - concepts/rts-pathfinding-approaches.md
  - concepts/scope-tiers.md
  - entities/engines/godot-4.md
  - entities/projects/castle-sim.md
  - sources/sh2-kingmaker-youtube-watchlist-2026-06-19.md
  - sources/shaggydev-tactics-engine-devlog-2023.md
  - sources/inbox-arxiv-reject-batch-2026-06-25.md
  - sources/inbox-arxiv-reject-batch-2026-06-23.md
  - meta/cross-wiki-routing.md
read_status: read
source_type: operator-watchlist
source_url: https://www.youtube.com/watch?v=9TVAnK6bRPs
maturity: validated
created: 2026-06-23
updated: 2026-06-25
---

## Raw Concept

Optional Godot 4 RTS/RPG long-form tutorial (**~11h**, KIMS MAKING GAMES) for **camera, selection, building input, and NavigationAgent2D** patterns — not SH2 parity. EN transcript fetched 2026-06-25: **11,786 segments**, ~653 min.

## Narrative

### Videos

| ID | Title | Channel | Transcript | Status |
|----|-------|---------|------------|--------|
| 9TVAnK6bRPs | Build a Complete RTS RPG in Godot 4 \| Full Game Tutorial 11h | KIMS MAKING GAMES | ✅ | **11,786 segments** — sampled; archive `/tmp/godot-rts-yt-transcripts.json` |

### `[OBSERVED-YT]` steal candidates (timestamp samples)

| # | Pattern | Timestamp | Notes |
|---|---------|-----------|-------|
| 1 | **Input map actions** — `confirm_build`, `cancel_build`, pause | ~03:53–04:58 | Maps to castle-sim architect confirm/cancel wall placement |
| 2 | **Grid snap** for building placement | ~07:42 | Enable grid on build preview — adjacency to Fork B wall snap |
| 3 | **NavigationAgent2D** on units | ~64:52, 65:23, 93:49 | Per-unit nav agent naming/layout; complements A* service Pattern 7 |
| 4 | **Camera pan/zoom** rig | ~45:21, 100:52 | Orthographic RTS camera child setup |
| 5 | **Selection UI** node | ~424:18 | Dedicated `selection` scene branch — author notes single-select limitations ~134:54, 200:06 |
| 6 | **Health bar** child UI | ~230:36 | Unit overlay pattern — defer for castle-sim (no hero HP focus) |

**Not observed in keyword sweep:** flow fields, AStarGrid2D, economy chains, minimap — tutorial is RPG/combat-heavy after early RTS scaffolding.

### Pre-transcript metadata `[TENTATIVE-META]`

| Field | Value |
|-------|-------|
| Project | **Tiny Sword Goblin Slayers** (itch.io) |
| Stated topics | RTS gameplay, player combat, goblin AI, defense, RPG progression, UI structure |
| Asset pack | Pixel Frog Treasure Hunters |

### Explicit reject list (confirmed scope fence)

Per @concepts/scope-tiers.md — do **not** import without operator sign-off:

- RPG leveling, XP, skill trees, equipment stats
- Quest log / journal / narrative campaign structure
- Party inventory, loot drops, boss encounter design
- Hero direct-action combat as core loop (goblin-slayer fantasy)
- Explosion/VFX-heavy combat polish as priority over economy loop
- Full 11h follow-along port of Tiny Sword codebase

### Cross-watchlist status (2026-06-25)

| Watchlist | Videos | Transcripts OK | Blocked |
|-----------|--------|----------------|---------|
| @sources/sh2-youtube-parity-watchlist-2026-06-17.md | 7 | 7 | 0 |
| @sources/sh2-kingmaker-youtube-watchlist-2026-06-19.md | 7 | 5 | 2 (private / no subs) |
| This shelf | 1 | 1 | 0 |

### Post-transcript checklist

1. [x] Fetch EN transcript
2. [x] Sample timestamps (~15–20 min + keyword hits) — not full 11h paste
3. [ ] Operator skim chapters for box-select / command panel if implementing Fork B HUD
4. [x] Update `briefs/research/godot-rts-rpg-youtube-watchlist.md`

**Verdict:** **STEAL-FROM (patterns, optional watch)** — gitignored `briefs/research/godot-rts-rpg-youtube-watchlist.md`; transcript **unblocked 2026-06-25**.

Cross-ref: SH2-specific parity stays @sources/sh2-kingmaker-youtube-watchlist-2026-06-19.md

## Dead Ends

- Treating RPG leveling/combat as castle-sim scope — out of @concepts/scope-tiers.md north star
- Substituting older KIMS uploads for watchlist ID `9TVAnK6bRPs`
