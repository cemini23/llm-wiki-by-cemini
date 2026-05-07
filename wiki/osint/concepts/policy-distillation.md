---
title: "Policy Distillation — Multi-Expert Consolidation via RLVR and OPD"
type: concept
tags: [rl-marl, ml-methods, policy-distillation, multi-expert, grpo]
keywords: [RLVR, OPD, policy-distillation, multi-expert-consolidation, GRPO, reinforcement-learning, token-priors, Conductor-Path-A]
related:
  - sources/co-evolving-policy-distillation-2604.27083.md
  - sources/sakana-conductor-rl-orchestration.md
  - sources/training-free-grpo-cai-2025.md
  - sources/training-free-grpo-iclr-2026.md
  - concepts/agent-native-research-artifacts.md
  - sources/blade-bayesian-listwise-alignment.md
  - concepts/llm-listwise-alignment.md
maturity: draft
created: 2026-05-02
updated: 2026-05-07
---

## Raw Concept

How can multiple expert model capabilities be consolidated into a single student model? What are the tradeoffs between RLVR (Reinforcement Learning with Verifiable Rewards), OPD (Online Policy Distillation), and token-prior approaches?

## Narrative

Policy distillation consolidates capabilities from multiple expert models into a single student. Three approaches exist on a continuum:

1. **Token-priors / Training-Free GRPO** — No model training. Historical routing decisions inform prompt prefixes that guide model selection. Captures ~70% of benefit with zero training cost. This is Conductor Path B.

2. **RLVR** (Reinforcement Learning with Verifiable Rewards) — Student trained via RL with reward signals from verifiable outcomes (math proofs, code execution, factual accuracy). Requires training infrastructure.

3. **OPD** (Online Policy Distillation) — Student and teacher policies co-evolve; student learns from teacher while teacher also adapts. Most capable but most complex.

For Conductor: Path B (token-priors) is the correct first step. Path A (trained 8B orchestrator) would use RLVR/OPD methodology. The co-evolving paper validates that accumulating real calibration data before training is the right sequence.

**ARA connection**: The @concepts/agent-native-research-artifacts.md exploration graph doubles as preference-signal training data. Every accept/reject/revision logged in `/trace` is a structured preference pair over research decisions — the same signal class that RLVR and OPD consume. An ARA corpus thus provides ready-to-use training environments: task in `/logic/experiments.md`, reward in `/evidence/`, and preference signals in `/trace/`.

## Snippets

- RLVR and OPD are points on a continuum of co-evolving distillation, not separate techniques. [Source: co-evolving-policy-distillation-2604.27083.pdf]
- Token-prior approaches capture ~70% of full RLVR benefit before any model training. [Source: co-evolving-policy-distillation-2604.27083.pdf]
