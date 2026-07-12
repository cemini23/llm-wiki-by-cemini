---
title: Multiplayer interactive world models with representation autoencoders (2607.05352)
type: source
tags: [source, arxiv, world-models, game-dev, k151]
keywords: [MIRA, representation autoencoder, multiplayer, interactive world model]
related:
  - sources/arxiv-gameenginebench-2607.03525-2026-07-09.md
  - entities/tools/mira-world-model.md
maturity: validated
read_status: deep-read
created: 2026-07-09
updated: 2026-07-12
---

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2607.05352](https://arxiv.org/abs/2607.05352) |
| **Repo** | [mira-wm/mira](https://github.com/mira-wm/mira) |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2607.05352-2607.05352v1-multiplayer-interactive-world-model.pdf` |

## Relations

- @entities/tools/mira-world-model.md — K160 Phase-0 Watch
- @sources/arxiv-gameenginebench-2607.03525-2026-07-09.md — harness eval cluster

## Narrative

**MIRA** (mira-wm/mira): first multiplayer world model conditioning on **per-agent action streams** — attributes scene deltas to the correct player; coherent under arbitrary action combinations. Rocket League domain; 10k hours bot gameplay; **5B** latent diffusion; **20 FPS** on single B200; rollouts stable to 5+ minutes (hours observed). Apache-2.0 release includes dataset, training/inference code, live demo.

**castle-sim posture (K160):** shelf reference — steal MP attribution + coherence stress patterns for hot-seat replay verification; **no** generative world-model port. Detail: `../projects/castle-sim/briefs/2026-07-12_k160-mira-mp-attribution-steal.md`.

## Snippets

> "Multiplayer Interactive World Models with Representation Autoencoders" [Source: arXiv:2607.05352 title]
