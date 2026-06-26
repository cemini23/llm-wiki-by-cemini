---
title: RLVF — reinforcement learning from verifier feedback
type: concept
tags: [concept, verifier, rlvf, training, k131]
keywords: [RLVF, verifier-reward, autoformalization, legal-AI-pattern]
related:
  - sources/arxiv-rlvf-formally-verified-law-2606.23913-2026-06-26.md
  - concepts/generator-verifier-inference-time-steering.md
  - concepts/probabilistic-agent-policy-verification.md
  - concepts/continual-harness-online-self-improvement.md
  - sources/arxiv-forex-lean4-fallacy-detection-2606.21867-2026-06-25.md
maturity: draft
created: 2026-06-26
updated: 2026-06-26
---

## Relations

- @sources/arxiv-rlvf-formally-verified-law-2606.23913-2026-06-26.md — K131 primary source
- @concepts/generator-verifier-inference-time-steering.md — inference Best-of-N vs training-time RLVF
- @concepts/probabilistic-agent-policy-verification.md — trajectory-level bounds complement pointwise verifier rewards

## Raw Concept

K131 synthesis of arXiv **2606.23913**. **RLVF** uses a deterministic verification kernel (formal checks, harness tests, legality oracle) as the **RL reward signal** instead of human preference or outcome-only reward.

## Narrative

### RLVF vs inference steering

| Mechanism | When | Signal |
|-----------|------|--------|
| Best-of-N / VERITAS | Inference | Pick best of N generator samples |
| RLVF | Training | Update policy toward verifier-pass trajectories |
| Harness CI | Deploy gate | Block ship on verifier fail |

Cemini does not train legal models. The steal is **verifier-shaped rewards** for any self-improvement loop (poker bot offline RL with PokerKit legality oracle, harness self-edit with pytest as kernel).

### Layer stack (from legal paper, domain-agnostic)

1. **Autoformalization** — informal claim → structured intermediate (see @concepts/relaxed-nfl-auto-formalization.md)
2. **Verification kernel** — deterministic accept/reject
3. **RLVF** — policy gradient / RL from kernel output

## Snippets

> "Reinforcement Learning from Verifier Feedback (RLVF)" [Source: arxiv-2606.23913 (retrieved 2026-06-26)]
