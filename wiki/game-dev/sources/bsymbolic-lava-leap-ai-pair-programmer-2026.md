---
title: bsymbolic — Lava Leap AI pair programmer case study (2026)
type: source
tags: [source, case-study, phaser, tdd, ai-pair]
keywords: [lava-leap, phaser, claude, tdd, procedural-generation]
related:
  - concepts/ai-assisted-game-dev-workflows.md
read_status: read
source_type: blog
source_url: https://dev.to/bsymbolic/lava-leap-shipping-an-endless-climber-with-an-ai-pair-programmer-30f3
maturity: validated
created: 2026-06-13
updated: 2026-06-13
---

## Raw Concept

Endless climber **Lava Leap** built with Claude as pair programmer — TDD milestones, parametric level gen, WebGL verification tricks.

## Narrative

### Process [CONFIRMED]

1. Brainstorm → design spec
2. Plan: **28 TDD tasks**, 8 milestones (v1); reviewer passes each milestone
3. Human plays live before sign-off
4. v2: +9 milestones (achievements, daily seed, shop, procedural music)

### Stack

Phaser 3 + TypeScript + Vite; Vitest + Playwright; PixelLab sprites; procedural audio via `tools/gen-music.mjs`.

### Key architecture: parametric reachability

Level generator clamps platforms inside provable movement envelope (jump, double-jump, dash). **12 unit tests** on generator. Set-piece chunks pass `validateChunk` — rejects unreachable gaps and "sucker" coin placements.

### Event spine

Typed `gameEvents` emitter — achievements/audio/UI decouple from player class. Avoid naming collision with `Phaser.Scene.events`.

### Gotchas [CONFIRMED]

| Issue | Fix |
|-------|-----|
| `tsc` emits `.js` beside `.ts`; Vite serves stale | `"noEmit": true` in tsconfig |
| WebGL screenshots blank | Read scene state via `window.__game`; pump `game.step()` |
| `scene.start()` kills caller | Settings must `scene.start('Menu')` on exit |

## Snippets

Transferable pattern for castle-sim: **prove invariants in tests** before AI scales content (e.g. pathfinding reachability).
