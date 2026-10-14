---
title: Stronghold 2 — architect view & keyboard controls (Fork B reference)
type: concept
tags: [concept, stronghold-2, ux, 3d, controls]
keywords: [architect-view, spacebar, camera, hotkeys, godot-spike]
related:
  - concepts/stronghold-2-castle-structures.md
  - concepts/godot-3d-sh2-architect-spike-plan.md
  - concepts/operator-vision-sh2-personal-clone.md
  - sources/gamespy-stronghold-2-bradbury-qa-2004.md
  - sources/stronghold-2-heaven-targeted-2026-06-13.md
  - sources/sh2-youtube-parity-watchlist-2026-06-17.md
  - concepts/stronghold-2-systems-inventory.md
  - entities/tools/stronghold2-analyse-hub.md
maturity: validated
created: 2026-06-13
updated: 2026-06-17
---

## Relations

- @concepts/godot-3d-sh2-architect-spike-plan.md — **story-005** acceptance criteria
- @sources/gamespy-stronghold-2-bradbury-qa-2004.md — Bradbury: architect for gap-free walls

## Raw Concept

SH2 separates **immersive lord view** from **architect top-down** for construction QA. Fork B must nail **Space toggle**, scroll/zoom/rotate, and wall-gap visibility — core "Stronghold feel" for the operator.

## Narrative

### Architect view [CONFIRMED — Stronghold Nation, GameSpy Q&A]

- **Toggle:** `Spacebar` — bird's-eye / flattened overhead; press again to return
- **Purpose:** spot **wall gaps**, align buildings, paint long wall segments
- **Also in UI:** Castle View menu (eye icon) → Architect's View
- Bradbury intent: no foot-soldier wall hacking — architect mode compensates with **readable perimeter**

### General controls [CONFIRMED — Stronghold Nation SH2 shortcuts]

| Input | Action |
|-------|--------|
| `P` | Pause / unpause |
| `+` / `-` (numpad) | Game speed (default ~35) |
| `W A S D` or arrows | Pan map |
| `R` / `F` or mouse wheel | Zoom |
| `Q` / `E` or middle-mouse drag | Rotate map |
| Mouse wheel (building selected) | Rotate building placement |
| `Tab` | Toggle interface panels |
| `.` | Cycle estates |
| `K G B N O M T J` | Jump to Keep, Granary, Barracks, Merc post, Monastery, Market, Treasury, Siege camp |
| `L` | Locate lord |
| `Ctrl+Alt+0–9` / `Alt+0–9` | Bookmark map location |

**SH1 vs SH2:** original Stronghold used Space for "flatten landscape"; SH2 reframes it as dedicated **Architect View** (not just clip art removal).

### Game views menu [CONFIRMED — Stronghold Nation game views]

Other scripted cameras (exit via click): Lord's Eye, Granary overview, etc. — lower priority for clone v0 than architect toggle.

### story-005 spike checklist (Godot)

Minimum parity for operator playtest:

1. **Space** toggles orthographic/top-down rig vs perspective follow cam
2. Wall preview shows **continuous segment** with gap highlight (different material/emissive)
3. **P** pause; **WASD** pan; wheel zoom
4. Optional v0.1: `Tab` hide build HUD for screenshots

Non-goals for spike: estate cycling, bookmark keys, full jump-to-building hotkeys.

### Play-session capture prompts

YouTube parity path filled 2026-06-17 — see @sources/sh2-youtube-parity-watchlist-2026-06-17.md:

- [x] Architect toggle — **instant cut**, walls hidden in overhead mode; **zoom resets** on toggle `[OBSERVED-YT]` *UaSfyPXD4i8*
- [x] Wall placement — segment/gatehouse clicks, not drag paint `[OBSERVED-YT]` *cEXhEXHypzo*
- [ ] Retail-only: gap highlight material, exact zoom limits

Log answers in `briefs/research/sh2-playsession-checklist.md`.

## Dead Ends

- **2D isometric only** — operator rejected; architect mode is 3D-native
- **Copy full SH2 keymap day one** — spike needs Space + pan/zoom only
