---
title: "RLVF — Formally Verified Law as verifier reward (2606.23913)"
type: source
tags: [formal-verification, rlvf, legal-ai, verifier-feedback, k131]
keywords: [RLVF, autoformalization, verification-kernel, legal-AI, self-improving]
related:
  - concepts/rlvf-verifier-feedback-training.md
  - concepts/generator-verifier-inference-time-steering.md
  - concepts/probabilistic-agent-policy-verification.md
  - sources/arxiv-forex-lean4-fallacy-detection-2606.21867-2026-06-25.md
  - sources/arxiv-relaxed-nfl-auto-formalization-2606.24443-2026-06-26.md
maturity: draft
read_status: read
created: 2026-06-26
updated: 2026-06-26
clusters: [llm-agents, verifier]
---

## Relations

- @concepts/rlvf-verifier-feedback-training.md — RLVF training loop synthesis
- @concepts/generator-verifier-inference-time-steering.md — inference-time vs training-time verifier steering
- @sources/arxiv-forex-lean4-fallacy-detection-2606.21867-2026-06-25.md — K129 ForEx Lean4 verifier cluster

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Closing the Loop: Formally Verified Law as a Reward Signal for Self-Improving Legal AI |
| **Authors** | Armin Heydari, Torben Leowald |
| **arXiv** | [2606.23913](https://arxiv.org/abs/2606.23913) |
| **sha256** | `e7f75a476be5b7e83b31d068b4a45db409ec09edc813f8212c317b75979a0d01` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2606.23913-2606-23913v1-closing-the-loop-formally-verified.pdf` |
| **Retrieved** | 2026-06-26 (daily digest inbox) |
| **Read status** | read (abstract + architecture skim) |

## Narrative

K131 legal-AI paper with **Cemini-relevant verifier architecture**, not legal-domain deployment. Three-layer stack: (1) autoformalization of statutes, (2) **verification kernel** checking candidate legal reasoning, (3) explanation generation. Training uses **Reinforcement Learning from Verifier Feedback (RLVF)** — verifier pass/fail (or graded checks) as the reward signal instead of human preference labels.

**Posture:** REFERENCE for verifier-steering cluster (poker trajectory checks, harness tests). No legal-AI product path.

### Architecture layers (skim)

| Layer | Role | Cemini steal |
|-------|------|--------------|
| Autoformalization | Informal → formal spec | Same gap as Relaxed NFL / ForEx — intermediate representation before hard prover |
| Verification kernel | Deterministic accept/reject | Static harness + poker hand-legality checker analog |
| RLVF | Verifier-shaped RL reward | Complements Best-of-N inference steering (K123 VERITAS) |

## Snippets

> "Training: Reinforcement Learning from Verifier Feedback (RLVF)" [Source: arxiv-2606.23913 p.1 TOC (retrieved 2026-06-26)]
