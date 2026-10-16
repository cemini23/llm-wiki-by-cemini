---
title: K292 3d-printing wave — executable 3D code and a no-human verification harness
type: source-hub
tags: [k292, 3d-printing, code-generation, harness]
keywords: [3DCodeVerse, CadQuery, OpenSCAD, Blender, executable dataset, geometric verification, LoRA execution rate]
related:
  - sources/arxiv-3dcodeverse-2610.22341-2026-10-16.md
  - concepts/executable-3d-verification-harness.md
maturity: draft
read_status: read
created: 2026-10-16
updated: 2026-10-16
wire_status: policy_wired
---

## Relations

- @sources/arxiv-3dcodeverse-2610.22341-2026-10-16.md
- @concepts/executable-3d-verification-harness.md

## Raw Concept

**OSINT K292 3d-printing wave, 2026-10-16.** One arXiv paper. **No clone. No install.**

## Narrative

`arXiv 2610.22341` — **3DCodeVerse**, USC with Google DeepMind and seven other institutions.

**Three parts:**

1. **A dataset of 269,597 unique executable 3D programs** across Blender `bpy`, CadQuery, OpenSCAD, Three.js, URDF and GLSL, packaged with assets. **92% of it is two sources** — DeepCAD→CadQuery at 47.55% and Shadertoy GLSL at 44.50% — so it is really a CAD-reconstruction and shader corpus.
2. **LoRA baselines:** Qwen3.5-9B goes from **0.0 to 84.9** execution rate on 3DCodeBench; Qwen3.8-27B 51.9 → 92.9.
3. **A harness that verifies without a human:** execute, then **measure the geometry numerically** (3D IoU, collision, contact, overlap, distance, bounding-box and part inventories), then let a VLM judge the render and repair the specific failure.

**The harness number:** 90% pairwise human-preference win over Claude Design (3D Object) with **both driven by Claude Opus 5.5**, judge score 88 vs 37. Same backbone both sides, so it measures the harness — but it is one comparator, one seed, and the paper **states no limitations**. Treat 90% as a ceiling.

**What travels:** the ordering. **Deterministic checks first, model judgement second.** → `@concepts/executable-3d-verification-harness.md`

## Snippets

> Notably, our 3DCodeVerse harness achieves a 90% win rate against Claude Design (3D Object) in pairwise human evaluations, when both are utilized by Claude Opus 5.5. [Source: arXiv 2610.22341, abstract]
