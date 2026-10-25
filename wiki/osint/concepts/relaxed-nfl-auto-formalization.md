---
title: Relaxed NFL — two-stage auto-formalization
type: concept
tags: [concept, auto-formalization, verifier, k131]
keywords: [Relaxed-NFL, Core-NFL, elaboration, informal-to-formal]
related:
  - sources/arxiv-relaxed-nfl-auto-formalization-2606.24443-2026-06-26.md
  - sources/arxiv-forex-lean4-fallacy-detection-2606.21867-2026-06-25.md
  - concepts/generator-verifier-inference-time-steering.md
  - concepts/probabilistic-agent-policy-verification.md
  - concepts/rlvf-verifier-feedback-training.md
  - concepts/poker-arena-multi-axis-cognitive-profile.md
  - concepts/devfun-poker-agent-challenge-2026.md
  - concepts/llm-agent-systems.md
maturity: draft
created: 2026-06-26
updated: 2026-10-25
---

## Relations

- @sources/arxiv-relaxed-nfl-auto-formalization-2606.24443-2026-06-26.md — K131 primary
- @sources/arxiv-forex-lean4-fallacy-detection-2606.21867-2026-06-25.md — K129 Lean4 verification cluster
- @concepts/poker-arena-multi-axis-cognitive-profile.md — structured trajectory as intermediate language

## Raw Concept

K131 synthesis of arXiv **2606.24443**. **Relaxed Natural Formal Language (Relaxed NFL)** is an intermediate representation between informal math and prover-ready **Core NFL** — preserves informal structure, tolerates partial specs; **elaboration** resolves ambiguity before verification.

## Narrative

### Why two stages

Direct informal→prover translation fails because LLMs must bridge a large representational gap in one shot. Relaxed NFL splits:

1. **Auto-formalize** to permissive structured form (fast, auditable)
2. **Elaborate** to fully specified Core NFL (deterministic refinement)
3. **Verify** with theorem prover or static checker

### Poker Arena mapping [TENTATIVE]

| Relaxed NFL stage | Poker analog |
|-------------------|--------------|
| Relaxed NFL | `DecideTrace`: street, action class, sizing intent (may omit exact chip counts) |
| Elaboration | PokerKit state fill-in, pot/stack reconciliation |
| Verification | Harness + hand legality + multi-axis rubric |

Brief: `agents/devfun-poker-arena/briefs/2026-06-26_k131-relaxed-nfl-verifier-steal.md`

## Snippets

> "remaining ambiguity … resolved during a later elaboration stage" [Source: arxiv-2606.24443 abstract (retrieved 2026-06-26)]
