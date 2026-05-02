---
title: "Co-Evolving Policy Distillation — Unifying RLVR and OPD for Multi-Expert Consolidation"
type: source
tags: [rl-marl, ml-methods, policy-distillation, multi-expert, grpo]
keywords: [RLVR, OPD, policy-distillation, multi-expert-consolidation, GRPO, reinforcement-learning, verifiable-reward, online-policy-distillation]
related:
  - concepts/policy-distillation.md
  - sources/sakana-conductor-rl-orchestration.md
maturity: draft
read_status: deep-read
created: 2026-05-02
updated: 2026-05-02
arxiv: "2604.27083"
---

## Raw Concept

- Original title: Co-Evolving Policy Distillation: A Unified Analysis of RLVR and OPD
- Type: PDF (arXiv preprint)
- Location: cemini-librarian:/opt/cemini-bulk/research/Co-Evolving Policy Distillation.pdf
- Retrieved: 2026-05-02
- Pages: ~15p
- Read status: deep-read

## Narrative

This paper provides a unified analytical framework for two reinforcement learning techniques for consolidating multiple expert models into a single student: **RLVR** (Reinforcement Learning with Verifiable Rewards) and **OPD** (Online Policy Distillation). The key insight: rather than treating these as separate approaches, they are points on a continuum of "co-evolving" distillation where the student and teacher policies update simultaneously.

Direct relevance to Conductor Path A: when Cemini graduates from Path B (token-prior API routing) to Path A (trained 8B orchestrator), this paper's unified framework provides the training methodology. Instead of static distillation from frontier models, the co-evolving approach allows the 8B orchestrator to improve alongside the models it routes to, continuously adapting to model capability shifts.

The paper also validates Conductor's current Path B architecture: the finding that simple token-priors (Training-Free GRPO) can capture ~70% of the benefit of full RLVR training before any model fine-tuning occurs supports the decision to ship Path B first and accumulate calibration data before committing to GPU hosting for Path A.

## Snippets

- RLVR and OPD are points on a continuum of co-evolving distillation; the student and teacher policies can update simultaneously rather than sequentially. [Source: Co-Evolving Policy Distillation.pdf]
- Token-prior approaches (Training-Free GRPO) capture approximately 70% of full RLVR benefit before any model fine-tuning, supporting a "measure first, train later" deployment strategy. [Source: Co-Evolving Policy Distillation.pdf]
