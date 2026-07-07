---
title: RTS networking — deferred research notes
type: concept
tags: [concept, networking, lockstep, multiplayer, deferred]
keywords: [lockstep, deterministic, multiplayer, rts, deferred]
related:
  - concepts/scope-tiers.md
  - sources/arxiv-1705-09704-lockstep-simulation.md
  - concepts/game-dev-wiki-scope.md
  - sources/inbox-arxiv-reject-batch-2026-07-07.md
maturity: draft
created: 2026-06-13
updated: 2026-07-07
---

## Relations

- @concepts/scope-tiers.md — MP deferred until slice playable

## Raw Concept

Research shelf for **later** multiplayer — not v0. Indexed from Exa lockstep cluster.

## Narrative

### ROADMAP default

Hot-seat / solo first (D2). Real-time online MP is Tier 3 aspiration.

### Lockstep pattern [CONFIRMED arXiv 1705.09704, Gaffer On Games]

- Send **inputs only**; each client runs identical sim
- Bandwidth scales with player count × input size, not entity count
- **Desync** is the hard problem — requires deterministic physics/economy/RNG
- Godot GDScript float math + thread timing → high desync risk without discipline

### When to revisit

After vertical slice v0 + optional hot-seat pass:

1. Audit sim for fixed-point or integer-only critical paths
2. Read Glenn Fiedler deterministic lockstep series [TENTATIVE]
3. Prototype LAN two-client wall place + peasant sync

### Determinism as a formal property (research aside)

@sources/inbox-arxiv-reject-batch-2026-07-07.md — arXiv 2607.04958 ("Look-Ahead-Freedom as Temporal Non-Interference") frames "no later state influences an earlier decision" as **temporal non-interference over a time-indexed lattice**. Same shape as a **lockstep replay** invariant: a deterministic tick must consume only ≤t state. Primary home is @osint-wiki (quant backtesting); logged here only as a Tier-N replay-verification analogy — **not** a slice adoption.

## Snippets

Do not architect v0 code for lockstep — but **avoid** nondeterministic floats in economy counters if MP is plausible Tier 2.
