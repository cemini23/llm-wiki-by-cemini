---
title: Executable 3D verification — run it, measure the geometry, then let a model judge
type: concept
tags: [3d, harness, verification, k292]
keywords: [execution check, 3D IoU, collision, contact, bounding box, VLM judge, targeted repair, 3DCodeBench, deterministic first]
related:
  - sources/arxiv-3dcodeverse-2610.22341-2026-10-16.md
  - concepts/k292-3d-printing-wave.md
  - concepts/k293-3d-printing-wave.md
maturity: draft
read_status: read
created: 2026-10-16
updated: 2026-10-20
---

## Relations

- @sources/arxiv-3dcodeverse-2610.22341-2026-10-16.md — the paper
- @concepts/k292-3d-printing-wave.md
- @concepts/k293-3d-printing-wave.md — FunCAD: test the mechanism, then trust the picture

## Raw Concept

**The question this page answers:** how do you verify generated 3D content without a human looking at every render?

Source: 3DCodeVerse (arXiv 2610.22341, USC / Google DeepMind et al.), ingested 2026-10-16.

## Narrative

### The three stages, in order

1. **Execute.** Does the program run in its declared environment. Binary, cheap, first.
2. **Measure.** Geometry toolkits compute **3D IoU, collision, contact, overlap, distance, bounding-box and part inventories**. Deterministic numbers, no model involved.
3. **Judge.** A VLM assesses the render, and the harness **repairs the specific failure** it identifies.

**The ordering is the design.** Deterministic checks run before the model, so the model is only asked what arithmetic cannot answer. This is the same shape as the K290 VEPA pattern — an LLM proposes, a deterministic layer disposes — and the opposite of asking a VLM to score everything.

### What it buys

The harness beats one-shot generation by **15.5 to 29.1 points**. Against **Claude Design (3D Object)** with **both driven by Claude Opus 5.5**, it wins **90% of pairwise human evaluations** at a judge score of **88 vs 37**.

The framing matters: **same backbone on both sides**, so the win measures the harness, not the model. One comparator, one seed, human-preference scale — treat 90% as an upper bound, not a proportion.

Geometry checks are where the deterministic stage pays most plainly: **12/12 renders pass** against **7/36** for a world-model predictor.

### The corpus

**269,597 unique executable programs** across Blender `bpy`, CadQuery, OpenSCAD, Three.js, URDF and GLSL. **92% is two sources** — DeepCAD→CadQuery at 47.55% and Shadertoy GLSL at 44.50% — so a model fine-tuned here mainly learns CAD reconstruction and shader code, not general 3D design. 768,596 training pairs, 891m tokens.

LoRA fine-tuning lifts **Qwen3.5-9B from 0.0 to 84.9** on execution rate (CadQuery 98.5, Blender 90.3) and Qwen3.8-27B from 51.9 to 92.9. A 9B model going from zero executable output to 85% says most of "3D coding" is format knowledge.

### The caveat the paper does not state

**There is no limitations section, and the main tables are one seed at T=0.7.** The dataset distribution is the practical limit: it is a CAD and shader corpus wearing a general 3D label.

## Snippets

> It uses execution checks, spatial measurements, and visual feedback to automatically evaluate and revise generated programs without human feedback during generation. [Source: arXiv 2610.22341, abstract]

> our 3DCodeVerse harness achieves a 90% win rate against Claude Design (3D Object) in pairwise human evaluations, when both are utilized by Claude Opus 5.5 [Source: arXiv 2610.22341, abstract]
