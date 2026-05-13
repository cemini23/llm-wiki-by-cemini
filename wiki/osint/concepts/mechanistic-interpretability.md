---
title: Mechanistic interpretability — circuit-level understanding of LLMs
type: concept
tags: [concept, interpretability, mechanistic-interpretability, circuits, sae, llm-internals]
keywords: [mechanistic interpretability, circuits, sparse autoencoders, SAE, feature steering, activation patching, llm internals]
related:
  - concepts/sparse-autoencoders.md
  - sources/qwen-scope.md
  - concepts/ai-safety.md
maturity: draft
created: 2026-05-13
updated: 2026-05-13
---

## Relations

- `@concepts/sparse-autoencoders.md` — the headline method this field uses at the moment
- `@sources/qwen-scope.md` — Qwen-Scope: SAE-based interpretability + steering for the Qwen model family
- `@concepts/ai-safety.md` — sibling concept; mech-interp is one of the technical tools the safety community uses

## Raw Concept

What prompted this page: qwen-scope source flagged that no mechanistic-interpretability hub existed. The field has matured enough (SAEs, circuit-tracing, activation patching) to deserve its own concept page even if Cemini's direct use is limited.

## Narrative

Mechanistic interpretability ("mech-interp") tries to reverse-engineer what specific neurons, attention heads, and circuits inside an LLM actually do. The current frontier method is **sparse autoencoders (SAEs)** — train an overcomplete autoencoder on a layer's activations, get features that correspond to recognizable concepts ("DNA sequence", "Python type-error", "expressing uncertainty"), and steer the model by adding or subtracting feature directions at inference.

**Cemini relevance**: not direct. We don't run SAEs in production. But:
- Interpretability-derived feature steering is what powers some of the safer instruction-following / refusal-tuning methods we rely on through the API.
- If a Cemini agent starts emitting odd patterns (e.g. hedging when it should commit), upstream understanding from this field tells us whether it's a training-data shift, a steering-vector hack, or genuine model drift.

For deeper Qwen-specific work, see `@sources/qwen-scope.md`. For the SAE methodology, see `@concepts/sparse-autoencoders.md`.

This is a stub.
