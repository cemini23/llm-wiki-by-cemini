---
title: "Latent Thought vs Chain of Thought — Computational Tradeoffs"
type: concept
tags: [reasoning, llm-science, ml-methods]
keywords: [latent-thought, chain-of-thought, CoT, TCk, parallel-computation, approximate-counting, abstract-cot, reasoning-depth]
related:
  - sources/cot-vs-latent-thought-2509.25239.md
  - sources/thinking-without-words-abstract-cot-2604.22709.md
  - concepts/recursive-multi-agent-systems.md
  - sources/recursive-multi-agent-systems-2604.25917.md
maturity: validated
created: 2026-05-02
updated: 2026-05-11
---

## Raw Concept

What are the computational tradeoffs between latent (internal) reasoning in transformers and explicit Chain of Thought (CoT) reasoning? When should a routing system choose one over the other?

## Narrative

Latent thought (internal transformer computation) and Chain of Thought (explicit step-by-step token generation) enable **different computational complexity classes**. Latent thought operates within TCk (threshold circuits), enabling parallel computation. CoT enables approximate counting via stochastic decoding — a sequential capability. This is not a quality spectrum but a computational capability boundary.

Abstract Chain-of-Thought (IBM Research, 2026) proposes a middle ground: compress reasoning into abstract tokens in latent space, maintaining CoT-quality results at lower token cost.

For Conductor routing: queries requiring parallel multi-dimensional reasoning may be well-served by chat models (latent). Queries requiring sequential derivation need CoT (reasoner). Abstract CoT, if exposed by providers, could handle the current reasoner-escalation cases at chat-model cost.

RecursiveMAS provides an implementation-level instantiation of latent thought for multi-agent systems: the inner RecursiveLink generates latent thoughts directly in continuous embedding space, bypassing vocabulary-space decoding and re-encoding. Each agent produces m≈ 80 latent thought steps, sufficient to stabilize performance across benchmarks. The outer RecursiveLink extends this paradigm to cross-agent communication — agents exchange latent states rather than text, preserving gradient flow across the full system unrolling. This validates the latent-thought thesis in an operational multi-agent setting.

## Snippets

- Latent thought: TCk complexity class, parallel computation. CoT: approximate counting via stochastic decoding, sequential. [Source: cot-vs-latent-thought-2509.25239.pdf]
- Abstract CoT compresses reasoning into shorter token sequences via latent-space abstract tokens. [Source: thinking-without-words-abstract-cot-2604.22709.pdf]
