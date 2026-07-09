---
title: arXiv 2607.05352 — MIRA multiplayer interactive world models — 2026-07-09
type: source
tags: [source, arxiv, world-model, multiplayer, rocket-league]
keywords: [mira, world-model, representation-autoencoder, latent-diffusion, multiplayer]
related:
  - concepts/rts-networking-deferred.md
  - concepts/scope-tiers.md
  - concepts/game-ai-rl-augmentation-shelf.md
  - sources/arxiv-2606.29932-saga-civrealm-strategy-agents-2026-07-05.md
  - sources/inbox-arxiv-reject-batch-2026-07-09.md
  - meta/cross-wiki-routing.md
read_status: read
source_type: research-paper
source_url: https://arxiv.org/abs/2607.05352
maturity: validated
created: 2026-07-09
updated: 2026-07-09
---

## Raw Concept

**MIRA** — first **multiplayer** interactive world model: conditions on multiple agents' action streams, attributes scene changes to the correct player, stays coherent under arbitrary action combinations. Trained on 10k hours Rocket League bot gameplay; 5B-param latent diffusion model; ~20 FPS on B200; rollouts stable to 5+ minutes (hours in practice). Repo: `mira-wm/mira` (Apache-2.0, ~332★ Jul 2026).

## Narrative

### Architecture [CONFIRMED — abstract]

| Component | Role |
|-----------|------|
| **Representation autoencoder** | Video codec / latent space for world state |
| **Multiplayer conditioning** | Per-agent action streams — not treating other players as static environment |
| **Latent diffusion** | Generative rollouts with physical-interaction fidelity probes |
| **Rocket League domain** | Fast coupled dynamics; four-player matches |

### castle-sim mapping (STEAL-FROM — research shelf, Tier 3+)

| Extract | Skip |
|---------|------|
| **Multi-agent action attribution** pattern for future MP sim / replay verification | Training Rocket League world models for castle-sim |
| Contrast with single-player world models (CaR/MoVerse rejects) — MP coherence is the novelty | Replacing Godot sim with learned world model |
| Dataset + eval code as **research reference** for lockstep/MP research shelf | Phase-0 adoption — not a Godot engine tool |

**Verdict:** **STEAL-FROM (research shelf)** — gitignored `briefs/research/mira-multiplayer-world-model-shelf.md`. v0–v2: deterministic Godot sim; Tier 3+ MP: read for multiplayer state coherence patterns (@concepts/rts-networking-deferred.md).

**Repo:** `mira-wm/mira` Apache-2.0 — reference implementation + dataset release; **no Phase-0** (research stack, GPU inference, Rocket League domain).

## Dead Ends

- Using MIRA rollouts as castle-sim playtest substitute — wrong domain + non-deterministic
- Conflating world models with lord AI (@sources/arxiv-2606.29932-saga-civrealm-strategy-agents-2026-07-05.md) — MIRA is environment dynamics, not strategic planning
