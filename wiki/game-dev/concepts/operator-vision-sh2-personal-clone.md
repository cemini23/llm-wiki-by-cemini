---
title: Operator vision — personal Stronghold 2 clone
type: concept
tags: [concept, scope, stronghold-2, operator, vision]
keywords: [stronghold-2, personal, clone, scope, north-star]
related:
  - concepts/stronghold-2-systems-inventory.md
  - concepts/scope-tiers.md
  - concepts/vertical-slice-v0.md
  - entities/projects/castle-sim.md
  - entities/games/stronghold-series.md
  - concepts/godot-3d-sh2-architect-spike-plan.md
  - concepts/stronghold-2-architect-controls.md
  - concepts/stronghold-2-github-ecosystem-shelf.md
  - concepts/stronghold-2-popularity-model.md
  - entities/engines/godot-4.md
  - entities/tools/stronghold2-analyse-hub.md
  - entities/tools/stronghold2-mp-ai-patch.md
  - sources/stronghold-2-heaven-gameinfo-2026-06-13.md
maturity: validated
created: 2026-06-13
updated: 2026-06-15
---

## Relations

- @concepts/stronghold-2-systems-inventory.md — full SH2 mechanics map
- `briefs/GDD-sh2-personal-clone.md` — phased build plan (local, gitignored)

## Raw Concept

**Operator decision (2026-06-13):** Favourite game is **Stronghold 2**. Personal clone target — solo use, no sale.

**Fork B locked (2026-06-13):** **Godot 3D rebuild** — operator: "weird to play 2D when I could buy SH2"; 3D castle building is non-negotiable. See @concepts/godot-3d-sh2-architect-spike-plan.md.

Existing `castle-sim` 2D work = **salvage sim logic**, freeze presentation line until 3D spike passes.

## Narrative

### What "copy" means here

| In scope | Out of scope |
|----------|--------------|
| SH2 mechanics: popularity, honour, crime, kingmaker ranks, food chains, siege rules | Firefly campaign plot, voice acting, licensed music |
| SH2 **feel**: village management interrupted by war, lord activities, rank progression | Pixel-perfect UI clone or trademark use |
| Placeholder / generated art | Ripping SH2 `.pak` textures or models |
| Personal Mac/Steam playtest build | Steam release, multiplayer matchmaking service |

### Gap vs current castle-sim

`castle-sim` today (~5% of SH1, 0% of SH2 signature systems):

- Godot 4, **2D prototype** (logic lab) — 3D is **primary line** from story-005 onward
- SH2 systems still missing: honour, crime, kingmaker, estates, 3D architect mode (in progress)

Closing the gap is **multi-year part-time** unless scope is staged ruthlessly.

### Presentation fork — **D4 closed: Fork B**

| Fork | Status |
|------|--------|
| ~~A — 2D + SH2 mechanics~~ | Rejected — operator wants 3D |
| **B — Godot 3D rebuild** | **SELECTED** — architect camera, thick walls, tower fantasy path |
| ~~C — 2.5D isometric~~ | Fallback if M0.3D spike KILLs |

First gate: `briefs/story-005-3d-architect-spike.md` → @concepts/godot-3d-sh2-architect-spike-plan.md

### Mac reference play (while building)

**Stronghold 2: Steam Edition** has no native Mac build. **CrossOver 24+** — community rating “Runs Great”; install Windows Steam in bottle; launch `Stronghold2.exe` if Firefly launcher fails. Use for side-by-side UX reference, not asset extraction.

### Phase ladder (Kingmaker-aligned, after M0.3D PROCEED)

See `briefs/GDD-sh2-personal-clone.md` for story breakdown. Summary:

1. **Spine (done/in progress)** — grid, pathfinding, one resource, labour, basic combat
2. **SH1 economy depth** — granary, tax, multi-food, popularity immigration
3. **SH2 identity** — honour currency, Lord's Kitchen/feasts, gong+crime+courthouse
4. **SH2 war** — no wall-hacking, siege ladder/ram, rank-gated units
5. **SH2 fantasy** — joust, fair, Lady/dance, monastery, estates
6. **Kingmaker mode** — full rank table as skirmish sandbox

Each phase should be **playable alone** — clone Crusader/SH2 scope only at the end.

### Research sources (priority order)

1. **Stronghold 2: Steam Edition** — operator owns / should buy for reference [TENTATIVE]
2. [Stronghold 2 Heaven](https://stronghold2.heavengames.com/gameinfo/) — mechanics tables (honour, kingmaker, popularity)
3. @sources/gamespy-stronghold-2-bradbury-qa-2004.md — siege/wall design
4. @sources/simon-bradbury-stronghold-heaven-sh3-2011.md — what fans rejected (scope caution)
5. MobyGames / Firefly press sheet — modes and feature list

### Wiki / repo routing

| Artifact | Location |
|----------|----------|
| SH2 mechanics truth | @concepts/stronghold-2-systems-inventory.md |
| SH1 baseline (still useful) | @concepts/stronghold-systems-inventory.md |
| Build stories | `briefs/GDD-sh2-personal-clone.md`, `briefs/story-*.md` |
| Code | `castle-sim/` (private) |

## Snippets

Operator intent (paraphrased 2026-06-13):

> SH2 was my favourite; I want a local game that lets me play that experience again — not for sale, just for me.

## Dead Ends

- Declaring "full SH2 clone" as Tier 1 — Bradbury + indie scope lessons say otherwise
- Abandoning M0–M1 pathfinding/labour code — it's the hardest RTS substrate SH2 also needs
- Public wiki implying we ship Firefly IP — keep repo private (ROADMAP D3) until placeholders only
