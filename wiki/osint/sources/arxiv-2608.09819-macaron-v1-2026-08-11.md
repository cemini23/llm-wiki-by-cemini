---
title: "Macaron-V1 — Open Continual Learning with Self-Improvement and Mixture-of-LoRA"
type: source
tags: [arxiv, k232, ccc]
keywords: [2608.09819, macaron, mixture-of-lora, continual-learning, self-improvement, mindforge]
related:
  - concepts/continual-harness-online-self-improvement.md
  - sources/arxiv-2608.19013-harness-continual-learning-2026-08-20.md
maturity: draft
created: 2026-08-11
updated: 2026-08-20
read_status: skimmed
---

## Relations

- @concepts/continual-harness-online-self-improvement.md

## Raw Concept

| Field | Value |
|-------|--------|
| arXiv | 2608.09819 |
| sha256 | `795eb2936d46aab06c84f36be947fd326853bf6c0573d49942ad53196262001d` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.09819-macaron-v1-towards-open-continual-learning-with.pdf` |
| retrieved | 2026-08-11 |

## Narrative

Macaron-V1 (Mind Lab, 49 pp) is an open agent-model family for **experiential intelligence** — learning from experience in real environments and continuing to learn after deployment. Two system goals: **Adaptation** via recursive improvement of versioned model-harness pairs (experience from one configuration evaluated under an external contract and used to construct its successor); **Collaboration** via the **Mixture-of-LoRA (MoL)** architecture that freezes a base model, composes specialist LoRA adapters, and routes one LoRA per user turn. Flagship **Venti** = 744B GLM-5.2 base + 4 LoRAs (chat, agent, coding, GenUI); **Tall** = Qwen3.6-based 50B for local deployment.

Supporting infra: UI4A component-native GenUI harness, stateful action substrate, versioned Harness Context Protocol contract, the **MindForge** agentic RL framework, **MinT** post-training platform, **LongStraw** long-context RL, and stability techniques for sparse MoE/DSA bases. Evaluated on Personal Intelligence, GenUI, and general capability benchmarks. Continual-learning compounding gains remain open questions.

**Routing:** CCC **Watch** — MoL routing + versioned model-harness pairs + MindForge RL are architecture patterns for continual learning; **no 744B weight pull / no HF blob download** (size + scope gate).

[Source: arXiv:2608.09819]
