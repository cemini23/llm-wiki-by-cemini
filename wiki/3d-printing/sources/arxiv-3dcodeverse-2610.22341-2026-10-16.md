---
title: "3DCodeVerse — 269,597 executable 3D programs and a no-human verification harness (arXiv 2610.22341)"
type: source
tags: [3d, code-generation, harness, verification, source, k292]
keywords: [3DCodeVerse, Blender, bpy, CadQuery, OpenSCAD, Three.js, URDF, GLSL, geometric verification, VLM judge, 3DCodeBench]
related:
  - concepts/executable-3d-verification-harness.md
  - concepts/k292-3d-printing-wave.md
maturity: draft
read_status: read
created: 2026-10-16
updated: 2026-10-16
---

## Relations

- @concepts/executable-3d-verification-harness.md — the pattern this paper establishes
- @concepts/k292-3d-printing-wave.md — K292 3d-printing wave hub

## Raw Concept

Title: 3DCodeVerse: Exploring 3D Worlds as Code
Authors: Yipeng Gao, Ziyao Zeng, Jinfa Huang, Yijiang Li et al. (USC, Yale, Rochester, UCSD, Columbia, NTU, UCSC, Google DeepMind, Philo Labs)
Type: arXiv 2610.22341v1 [cs.CV], 34 pages, 15 Oct 2026
Location: `cemini-egress-fi:/opt/cemini-bulk/research/3d-printing/arxiv-2610.22341-3dcodeverse-exploring-3d-worlds-as-code.pdf`
Retrieved: 2026-10-16
Artifacts: `3dcodeverse.com` · `github.com/gaoypeng/3dcodeverse` · dataset `huggingface.co/datasets/ilabai/3dcodeverse`
Read status: read

## Narrative

A three-part ecosystem for **coding agents that produce 3D content**, and the dataset is the durable artefact.

**1. The dataset — 3DCodeVerse-2M.** **269,597 unique executable programs** across 9 collections, packaged with the source files and assets needed to run them in a declared environment. Export is 2,028,286 rows in 342 shards; training pairs **768,596 / 891m tokens**.

| Source | Programs | Share |
|---|---|---|
| DeepCAD → CadQuery | **128,201** | 47.55% (MIT) |
| Shadertoy GLSL | **119,961** | 44.50% |
| Articraft CadQuery | 6,882 | |
| Bioinspired3D | 6,343 | |
| Articraft URDF | 6,146 | |
| Thingiverse OpenSCAD | 1,193 | |
| 3DCodeBench factories | 486 | |
| Agent-written Three.js / Blender | 280 / 80 | |

The target formats are **Blender `bpy`, CadQuery, OpenSCAD, Three.js, URDF and GLSL** — the same set a print pipeline and a web pipeline would use. **The distribution is the caveat:** 92% of the corpus is two sources, so a model fine-tuned here is mostly learning CAD reconstruction and shader code.

**2. Fine-tuning baselines.** LoRA on open models, measured by execution rate:

- **Qwen3.5-9B: 0.0 → 84.9** on 3DCodeBench. Blender 90.3, CadQuery 98.5, OpenSCAD +36.0, GLSL +23.0.
- **Qwen3.8-27B: 51.9 → 92.9** (+41.0).

A 9B model going from **zero** executable output to 85% is the strongest single number in the paper, and it speaks to how much of "3D coding" is format knowledge rather than skill.

**3. The harness — and this is the transferable part.** A **multi-agent directed acyclic graph** that generates, refines and judges 3D content **with no human in the loop**. Verification is three-layered:

- **Execution checks** — does the program run in its declared environment.
- **Spatial measurement** — 3D IoU, collision, contact, overlap, distance, bounding-box and part inventories via dedicated geometry toolkits.
- **Visual judging** — a VLM assesses the render.

The harness is 17 modular skill bundles with a 28-rule router selecting up to 5 skills per task, and it doubles as a data engine: it records pass and refine traces for SFT and DPO.

**Results.** Against **Claude Design (3D Object)**, with **both driven by Claude Opus 5.5**, the harness wins **90% of pairwise human evaluations**, with a judge score of **88 vs 37**. Objects: 69-89% human preference, judge score +11 to +25 points. Gemini 3.8 Flash 61 → 87, GPT-6 Luna 64 → 86. The harness beats one-shot generation by **15.5 to 29.1 points**. On robotics geometry checks it passes **12/12** renders against **7/36** for a world-model predictor.

**Limitations: the paper has none.** There is no limitations section. The main tables are also **one seed at T=0.7**, which the paper does not flag. The 90% win is against a single comparator model on a human-preference scale.

### Why it matters here

1. **The verification pattern is model-agnostic and the real prize:** *execute → measure geometry numerically → let a VLM judge the render → repair the specific failure*. No human, and the numeric stage does the work that a VLM alone would do badly. This is the K290 VEPA shape — deterministic check first, model judgement second — applied to geometry.
2. **The dataset is directly usable** for a print pipeline: 128k CadQuery and 1,193 OpenSCAD programs with assets, under a HuggingFace-hosted release.
3. **The 90% figure needs its framing:** same backbone on both sides, one human-preference scale, one seed. It measures the harness, not the model, which is the useful reading anyway.

**No clone. No install. No trade.**

## Snippets

> Notably, our 3DCodeVerse harness achieves a 90% win rate against Claude Design (3D Object) in pairwise human evaluations, when both are utilized by Claude Opus 5.5. [Source: arXiv 2610.22341, abstract]

> It uses execution checks, spatial measurements, and visual feedback to automatically evaluate and revise generated programs without human feedback during generation. [Source: arXiv 2610.22341, abstract]

> Qwen3.5-9B execution rate 0.0 → 84.9 on 3DCodeBench after LoRA. [Source: arXiv 2610.22341, results]
