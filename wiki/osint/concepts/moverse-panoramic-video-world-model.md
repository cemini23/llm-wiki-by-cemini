---
title: MoVerse panoramic video world model
type: concept
tags: [concept, world-model, gaussian-splatting, castle-sim, k122]
keywords: [MoVerse, 360 panorama, 3D Gaussian scaffold, single-image, real-time video, steal-from]
related:
  - sources/arxiv-moverse-panoramic-world-model-2606.13376-2026-06-18.md
  - sources/leworldmodel-2603.19312v2.md
maturity: draft
created: 2026-06-18
updated: 2026-06-18
---

## Relations

- @sources/arxiv-moverse-panoramic-world-model-2606.13376-2026-06-18.md — primary source
- @sources/leworldmodel-2603.19312v2.md — JEPA control world model contrast (pixels → actions vs pixels → roam video)
- @game-dev-wiki/entities/projects/castle-sim.md — steal-from target

## Raw Concept

K122 ingest of arXiv **2606.13376**. Real-time **single-image → navigable 3D world → streaming video** pipeline using panoramic diffusion + 3D Gaussian scaffold + autoregressive video student.

## Narrative

**Architecture pattern (steal for castle-sim):**
1. **Expand partial observation** — one screenshot/concept art → full 360° context (topology-aware diffusion).
2. **Persistent spatial memory** — lift to renderable 3D scaffold (Gaussians) decoupled from final pixels.
3. **Interactive observation** — camera-path-conditioned video at 8 FPS (RTX 4090).

**Why castle-sim cares:** Stronghold-like slices need **playtest parity** and **marketing flythroughs** before full Godot art pass. MoVerse offers a **reference workflow** for "one castle keep render → explorable preview video" — not a Godot plugin.

**Phase-0:** `Orange-3DV-Team/MoVerse` — 85 stars, pushed 2026-06-13, **no LICENSE** on GitHub; weights gated. **REFERENCE only** until license + weights ship.

**Posture:** Brief to `../projects/castle-sim/briefs/` — steal-from note, no install.

## Snippets

> "Separates world construction from observation rendering." [Source: arXiv:2606.13376 (retrieved 2026-06-18)]

## Dead Ends

- Gaussian splat scaffold ≠ Godot NavigationMesh — do not plan runtime import without dedicated spike.
- 29 MB PDF / corporate-gated repo — not a K-batch Adopt candidate today.
