---
title: "MoVerse — Real-Time Video World Modeling with Panoramic Gaussian Scaffold — arXiv 2606.13376"
type: source
tags: [source, arxiv, world-model, gaussian-splatting, castle-sim, k122]
keywords: [2606.13376, MoVerse, panoramic, 3D Gaussian, video world model, RTX 4090, single-image]
related:
  - concepts/moverse-panoramic-video-world-model.md
  - sources/leworldmodel-2603.19312v2.md
maturity: draft
read_status: read
created: 2026-06-18
updated: 2026-06-18
clusters: [llm-agents]
---

## Relations

- @concepts/moverse-panoramic-video-world-model.md — K122 synthesis + castle-sim steal-from
- @sources/leworldmodel-2603.19312v2.md — JEPA world-model sibling (control vs visual roaming)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | MoVerse: Real-Time Video World Modeling with Panoramic Gaussian Scaffold |
| **Authors** | Yang Zhou, Ziheng Wang, Yuqin Lu, Haofeng Liu, Jun Liang, Shengfeng He, Jing Li |
| **arXiv** | 2606.13376 v2 (17 Jun 2026) |
| **sha256** | `fe4aeafb99817ab308ae69c91cda3843ea6f2ddfbde1ada8541ef3c0b136f645` |
| **Repo** | `Orange-3DV-Team/MoVerse` — **no LICENSE** on GitHub; code/models gated pending corporate review [NEEDS VERIFICATION 2026-06-18] |
| **Project** | https://orange-3dv-team.github.io/MoVerse/ |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2606.13376-2606-13376v1-moverse-real-time-video-world-model.pdf` |
| **Retrieved** | 2026-06-18 (daily digest inbox) |
| **Read status** | read (abstract + pipeline summary) |

## Narrative

MoVerse builds an **interactively navigable 3D world from a single narrow-field-of-view (NFOV) image**, then streams photorealistic video along user camera trajectories at **8 FPS on one RTX 4090**.

**Three-stage pipeline:**
1. **Panoramic generation** — topology-aware diffusion expands NFOV → gravity-aligned 360° ERP panorama.
2. **3D Gaussian scaffold** — feed-forward residual prediction lifts panorama to persistent, splattable 3D Gaussians (spatial memory).
3. **Autoregressive video refinement** — bidirectional diffusion teacher distilled to causal student for bounded-latency streaming; scaffold renderings conditioned on camera path.

**Design insight:** separates **world construction** (offline-ish scaffold) from **observation rendering** (online video), combining explicit 3D controllability with generative video quality.

**Cemini posture:** **REFERENCE / steal-from** for `@game-dev-wiki` castle-sim — procedural environment expansion from a single concept art / screenshot, playtest flythrough capture, or marketing trailer generation. **Not** for CeminiSuite trading stack. Phase-0: repo exists but **no SPDX license** + weights unreleased → **REFERENCE only** until license verified.

## Snippets

> "MoVerse supports real-time scene roaming at 8 FPS on a single NVIDIA RTX 4090 GPU, demonstrating a practical path toward single-image world creation with interactive video output." [Source: arXiv:2606.13376 abstract (retrieved 2026-06-18)]

> "It separates world construction from observation rendering." [Source: arXiv:2606.13376 abstract (retrieved 2026-06-18)]

## Dead Ends

- GitHub `Orange-3DV-Team/MoVerse`: `license: null`, pretrained models "coming soon" — cannot Phase-0 install on laptop.
- Godot castle-sim uses mesh/grid pathfinding, not Gaussian splats — steal is **workflow pattern** (single-image → explorable preview), not drop-in renderer.
