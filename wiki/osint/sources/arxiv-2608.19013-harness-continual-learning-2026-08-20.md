---
title: "Harness Continual Learning (arXiv 2608.19013)"
type: source
tags: [arxiv, harness, ccc, k243]
keywords: [HCL, harness-level-forgetting, guarded-evolution, Macaron]
related:
  - concepts/continual-harness-online-self-improvement.md
  - concepts/skill-misevolution.md
  - concepts/agent-harness-verification-bottleneck.md
  - sources/arxiv-2608.09819-macaron-v1-2026-08-11.md
  - sources/arxiv-2608.18565-semaplc-2026-08-20.md
  - sources/arxiv-2608.19047-eureka-2026-08-20.md
  - sources/newsletter-rss-latent-space-2026-08-20-glm53-harness.md
maturity: draft
created: 2026-08-20
updated: 2026-08-20
read_status: read
---

## Relations

- @concepts/continual-harness-online-self-improvement.md — pairs Macaron / K263; no weight download
- @concepts/skill-misevolution.md — do not unattended auto-evolve skills
- @concepts/agent-harness-verification-bottleneck.md — evaluator commits; worker proposes
- @sources/arxiv-2608.09819-macaron-v1-2026-08-11.md — versioned model-harness pairs
- @sources/arxiv-2608.18565-semaplc-2026-08-20.md — verification-gated completion
- @sources/arxiv-2608.19047-eureka-2026-08-20.md — meta-agent orchestration sibling

## Raw Concept

| Field | Value |
|-------|--------|
| Paper | arXiv:2608.19013, "Harness Continual Learning: Continual Adaptation Beyond Model Parameters" |
| Authors | Borui Kang, Jinrui Gu, Junhan Lv, Wenbin Li, Lei Wang, Yang Gao (Nanjing / Wollongong) |
| Retrieved | 2026-08-20 |
| File | `arxiv-2608.19013-harness-continual-learning-continual-adaptation.pdf` |
| sha256 | `ed0e60b249fefe74a4c093bbb5fdee1ed2592c1bb8b2a8be0bc17ad8c1473665` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.19013-harness-continual-learning-continual-adaptation.pdf` |
| Dual-ID | **OSINT K243**. CCC. **No weight download.** |

## Narrative

Continual learning has been model-centric. Modern agents also adapt through prompts, memories, tools, skills, and routing. Because those contents jointly shape later execution, a harness update can break previously reliable behavior **even when the model is frozen**. The authors name this **harness-level forgetting** and formulate Harness Continual Learning (HCL): the harness evolves around a frozen foundation model.

They instantiate four execution-facing components (Task Interface, Experience Memory, Capability Map, Adaptive Router) and **guarded harness evolution**: a Continual Optimizer proposes candidates from post-execution feedback; a Continual Evaluator commits only after checking current improvement, historical retention, and validity. Reported relative gains exceed 10% over baselines in some settings; retention sweeps show the stability–plasticity trade-off can be tuned.

**Concrete claim `[TENTATIVE]`:** a memory update, skill revision, or routing edit can turn an earlier correct trajectory into a failure without touching weights. CCC steal: proposal ≠ commit. Pairs Macaron-V1 versioned model-harness pairs. Do **not** unattended auto-evolve `.cursor/skills/*`. Do not swap `/route`. No HF weights.

## Snippets

> "a harness update can disrupt previously reliable behavior even when the model is frozen." [Source: arxiv-2608.19013 abstract]
