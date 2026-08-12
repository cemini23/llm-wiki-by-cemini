---
title: "MIRA — Medical Image Reflection for Agentic Diagnosis"
type: source
tags: [arxiv, k233, medical-ai, agents, rl]
keywords: [2608.10827, mira, medical-visual, tool-use-verification, mcts, reflective-principles, agentic-diagnosis]
related:
  - concepts/agent-tool-use-verification.md
maturity: draft
created: 2026-08-12
updated: 2026-08-12
read_status: skimmed
---

## Relations

- @concepts/agent-tool-use-verification.md

## Raw Concept

| Field | Value |
|-------|--------|
| arXiv | 2608.10827 |
| sha256 | `b2f5c70344e08c41552f0b97e4d1480ac722b7cc375e8f4e81b02ff9819815b8` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.10827-mira-medical-image-reflection-for-agentic-diagno.pdf` |
| retrieved | 2026-08-12 |
| authors | Shengzhi Wang, Jun Yang, et al. (Tongji Univ., Nanjing Univ., Northwestern Polytechnical, ENS-PSL) |

## Narrative

MIRA targets **when external tools are actually necessary** in medical visual diagnosis. The premise: indiscriminate tool use introduces noisy observations, propagates misleading evidence, and raises reasoning cost — and in diagnosis, merely acquiring observations is not enough; the agent must verify whether the tool action was appropriate, whether acquired evidence supports the current hypothesis, and whether weak/contradictory evidence calls for corrective reasoning.

Training is two-stage: (1) **SFT** on a curated medical tool-use + reflection dataset built by a **tool-augmented Monte Carlo Tree Search (MCTS) data engine** that jointly verifies visual-grounding accuracy and semantic reasoning consistency per node; (2) **RL** with an **online reflective-principle evolution** mechanism — failure cases are distilled into reflective principles injected into subsequent rollouts, with effective principles selected via trial-and-verification.

Route: **WATCH / wiki-only.** Medical domain OOD; no transferable OCR/HTR path to Atto unless the reflective tool-use-verification loop is extracted as a generic agent pattern (see `@concepts/agent-tool-use-verification.md`). Skip heavy medical weights.

[Source: arXiv:2608.10827]
