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
  - sources/inbox-arxiv-reject-batch-2026-06-23.md
  - meta/cross-wiki-routing.md
read_status: read
source_type: operator-watchlist
source_url: https://www.youtube.com/watch?v=9TVAnK6bRPs
maturity: validated
created: 2026-06-23
updated: 2026-06-24
---

## Raw Concept

Optional Godot 4 RTS/RPG long-form tutorial for **camera, selection, and command HUD** patterns — not SH2 parity. Transcript fetch attempted 2026-06-23; **blocked until premiere** (~2026-06-24). Pre-transcript metadata only.

## Narrative

### Videos

| ID | Title | Channel | Transcript | Status |
|----|-------|---------|------------|--------|
| 9TVAnK6bRPs | Build a Complete RTS RPG in Godot 4 \| Full Game Tutorial 11h | KIMS MAKING GAMES | ❌ | **Premiere retry 2026-06-24** — still unplayable via API (~14 min at fetch) |

Transcript archive (session): `/tmp/godot-rts-yt-transcripts.json` — entry `9TVAnK6bRPs` status `unavailable` (VideoUnplayable: premieres in ~14 minutes at 2026-06-24 fetch).

**Fetch command (retry after premiere):**

```python
from youtube_transcript_api import YouTubeTranscriptApi
api = YouTubeTranscriptApi()
data = api.fetch("9TVAnK6bRPs", languages=["en"])
```

### Pre-transcript metadata `[TENTATIVE-META]`

From oEmbed + channel marketing (not `[OBSERVED-YT]`):

| Field | Value |
|-------|-------|
| Project | **Tiny Sword Goblin Slayers** (itch.io) |
| Stated topics | RTS gameplay, player combat, goblin AI, defense, RPG progression, UI structure |
| Asset pack | Pixel Frog Treasure Hunters |
| Godot pin | 4.6.x mentioned in related uploads |

**Steal candidates (hypothesis — verify against transcript chapters):**

1. **RTS camera + command layer** — orthographic/pan rig, unit group orders (castle-sim Fork B 3D architect adjacency)
2. **Box / multi-select + command panel layout** — bottom-bar resource + selection panel (SH2 HUD parity, not RPG stats pane)
3. **Villager/job automation** — channel trailer mentions AI job system for pawns; may overlap peasant task queue — **only if transcript shows grid/building hooks, not RPG XP**

### Explicit reject list (pre-transcript scope fence)

Per @concepts/scope-tiers.md — do **not** import without operator sign-off:

- RPG leveling, XP, skill trees, equipment stats
- Quest log / journal / narrative campaign structure
- Party inventory, loot drops, boss encounter design
- Hero direct-action combat as core loop (goblin-slayer fantasy)
- Day/night cycle (unless architect-only cosmetic)
- Full 11h follow-along port of Tiny Sword codebase

### Cross-watchlist status (2026-06-23)

| Watchlist | Videos | Transcripts OK | Blocked |
|-----------|--------|----------------|---------|
| @sources/sh2-youtube-parity-watchlist-2026-06-17.md | 7 | 7 | 0 |
| @sources/sh2-kingmaker-youtube-watchlist-2026-06-19.md | 7 | 5 | 2 (private / no subs) |
| This shelf | 1 | 0 | 1 (premiere) |

### Post-premiere ingest checklist

1. Fetch EN transcript → segment by timestamps (sample every ~15–20 min; do not paste full 11h text into wiki)
2. Tag `[OBSERVED-YT]` steal/reject rows with video IDs + timestamps
3. If ≥3 RTS UI/camera patterns repeat → delta @concepts/godot-pathfinding-patterns.md or Fork B architect brief only
4. Update `briefs/research/godot-rts-rpg-youtube-watchlist.md` acceptance boxes

**Verdict:** **STEAL-FROM (patterns, optional watch)** — gitignored `briefs/research/godot-rts-rpg-youtube-watchlist.md`; **transcript pending premiere**.

Cross-ref: SH2-specific parity stays @sources/sh2-kingmaker-youtube-watchlist-2026-06-19.md

## Dead Ends

- Treating RPG leveling/combat as castle-sim scope — out of @concepts/scope-tiers.md north star
- Substituting older KIMS uploads (`nhuhLbUCL9I`, `mMSsBrIjM24`) for this watchlist ID — different cuts; not operator-curated list
