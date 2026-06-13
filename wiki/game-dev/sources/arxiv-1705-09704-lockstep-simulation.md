---
title: arXiv 1705.09704 — Lock-step simulation (Haskell)
type: source
tags: [source, paper, networking, lockstep, multiplayer]
keywords: [lockstep, deterministic, multiplayer, arxiv, networking]
related:
  - concepts/rts-networking-deferred.md
  - concepts/game-dev-wiki-scope.md
read_status: read
source_type: research-paper
source_url: https://arxiv.org/abs/1705.09704
arxiv_id: "1705.09704"
maturity: validated
created: 2026-06-13
updated: 2026-06-13
---

## Relations

- @concepts/rts-networking-deferred.md — hobby MP deferred research

## Raw Concept

ICFP 2017 pearl: **Lock-Step Simulation Is Child's Play** — lockstep + client prediction in Haskell CodeWorld.

## Narrative

### Core idea [CONFIRMED]

- Lockstep: broadcast **inputs only**; each client simulates state locally (Doom-era pattern)
- Desync is hard in imperative code; authors argue **pure FP** makes consistency easier
- CodeWorld extension: middle-school-friendly networked games with prediction

### Relevance to castle-sim

**Deferred** until after vertical slice (@concepts/scope-tiers.md — hot-seat/LAN first). When researching MP:

- Godot GDScript is **not** Haskell-pure — desync discipline still hard
- See also Glenn Fiedler deterministic lockstep articles [TENTATIVE]

### Not a pathfinding paper

Exa `lockstep-rts` cluster included this; indexed under networking, not pathfinding.

## Snippets

> "The state of the game itself is never transmitted over the network."
