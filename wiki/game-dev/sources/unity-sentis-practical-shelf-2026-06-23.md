---
title: Unity Sentis practical shelf — on-device small ML (not LLM NPCs) — 2026-06-23
type: source
tags: [source, unity, sentis, onnx, ml, digest]
keywords: [unity-sentis, onnx, inference, adaptive-difficulty, shelf]
related:
  - concepts/llm-npc-runtime-ai-shelf.md
  - concepts/game-ai-rl-augmentation-shelf.md
  - concepts/scope-tiers.md
  - entities/engines/godot-4.md
  - sources/inbox-arxiv-reject-batch-2026-06-27.md
  - meta/cross-wiki-routing.md
read_status: read
source_type: web-article
source_url: https://toolaipilot.com/blog/i-spent-three-months-learning-unity-sentis-and-here-is-what-it-can-actually-do-inside-a-real-game-build
maturity: validated
created: 2026-06-27
updated: 2026-06-27
---

## Raw Concept

Practitioner blog (Jun 2026) on **Unity Sentis** — ONNX inference in Unity 6 for small purpose-trained models. **Not** LLM dialogue; contrast for castle-sim Tier 3+ on-device ML vs Godot gap.

## Narrative

### What Sentis is [CONFIRMED]

Runtime **inference only** — bring ONNX model; train in PyTorch/Colab outside Unity. Included free in Unity 6 Package Manager.

### Systems author built [TENTATIVE — single dev report]

| System | Pattern | Performance note |
|--------|---------|------------------|
| Vision enemy detection | Binary classifier on synthetic LOS geometry | <2ms GPU inference; beats naive raycast on partial occlusion |
| Adaptive difficulty | 3-class classifier on death/time/accuracy features | Beats manual thresholds |
| Mobile gestures | Accelerometer sequence classifier | Needed more diverse training data |

### Hard limits cited [CONFIRMED]

- **No in-game LLMs** — even quantised SLMs too large/slow for consumer real-time dialogue
- Best with models **<20MB mobile / <50MB PC**
- Requires ML training pipeline outside engine — not a codegen assistant
- Complements Unity ML-Agents (train) → Sentis (ship inference)

### castle-sim mapping (Godot north star)

| Extract | Skip |
|---------|------|
| Small ONNX classifiers for **adaptive difficulty** or perception leaves — Phase E+ shelf | Pivot to Unity for Sentis |
| Difficulty classifier ≈ honour/popularity tuning leaf (EA DRL paper pattern) | LLM lord dialogue |
| Backend/platform testing on target hardware early | Expect Godot equivalent today |

**Verdict:** **STEAL-FROM (patterns, Unity contrast)** — no Phase-0 (engine-bundled). Godot has no Sentis equivalent; defer runtime ML to Phase E+ JSON/BT director first.

Cross-ref: @concepts/game-ai-rl-augmentation-shelf.md (modular leaves); @concepts/llm-npc-runtime-ai-shelf.md (LLM ≠ Sentis).

## Dead Ends

- Unity Sentis for castle-sim implementation — ROADMAP D4 locked Godot
- Sentis as NPC dialogue engine — author explicitly rejects LLM-in-game via Sentis
