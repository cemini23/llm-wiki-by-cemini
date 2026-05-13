---
title: Sparse autoencoders (SAEs) — feature decomposition for LLM internals
type: concept
tags: [concept, interpretability, sparse-autoencoder, sae, feature-steering, mech-interp]
keywords: [sparse autoencoders, SAE, dictionary learning, monosemantic features, feature steering, interpretability]
related:
  - concepts/mechanistic-interpretability.md
  - sources/qwen-scope.md
maturity: draft
created: 2026-05-13
updated: 2026-05-13
---

## Relations

- `@concepts/mechanistic-interpretability.md` — parent field; SAEs are the current dominant tool
- `@sources/qwen-scope.md` — Qwen-Scope: SAE library trained on Qwen activations

## Raw Concept

What prompted this page: qwen-scope source needed a concept anchor for the SAE method. SAEs are central enough to mech-interp to warrant their own page rather than a one-liner in a parent concept.

## Narrative

A sparse autoencoder takes an LLM's hidden-state vectors at a chosen layer, runs them through an overcomplete encoder + L1-sparsity penalty, and pops out a dictionary of features. Each feature is a direction in activation space that fires for some recognizable input pattern — sometimes a specific token, sometimes a concept ("medical terminology", "sycophantic praise", "code about prime numbers"), sometimes a circuit role ("subject of a relative clause").

Two things you can do with an SAE:
1. **Probe** — feed text through, see which features activate, get a feature-level explanation of model behavior.
2. **Steer** — at inference, add or subtract a feature's direction from the residual stream to push the model toward or away from that behavior. Used for refusal tuning, persona shifts, and bias mitigation.

**Cemini relevance**: low direct use; high indirect importance. SAE-derived steering is one of the foundational tools Anthropic uses to ship safer Claude versions, so improvements here propagate into our agent stack.

See `@sources/qwen-scope.md` for an open SAE library + steering interface for the Qwen family. This is a stub.
