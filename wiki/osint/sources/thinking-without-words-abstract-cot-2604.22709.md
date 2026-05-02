---
title: "Thinking Without Words — Efficient Latent Reasoning with Abstract Chain-of-Thought"
type: source
tags: [reasoning, llm-science, ml-methods, latent-reasoning, abstract-cot]
keywords: [abstract-chain-of-thought, latent-reasoning, IBM, reasoning-efficiency, token-efficiency, abstract-tokens]
related:
  - concepts/latent-thought.md
  - sources/cot-vs-latent-thought-2509.25239.md
maturity: draft
read_status: deep-read
created: 2026-05-02
updated: 2026-05-02
arxiv: "2604.22709"
---

## Raw Concept

- Original title: Thinking Without Words: Efficient Latent Reasoning with Abstract Chain-of-Thought
- Author(s): IBM Research
- Type: PDF (arXiv preprint)
- Location: cemini-librarian:/opt/cemini-bulk/research/Thinking Without Words- Efficient Latent Reasoning with Abstract Chain-of-Thought.pdf
- Retrieved: 2026-05-02
- Pages: ~15p
- Read status: deep-read

## Narrative

IBM Research proposes **Abstract Chain-of-Thought** (Abstract CoT), a method for compressing reasoning chains into shorter, denser token sequences without losing reasoning fidelity. Instead of generating full natural-language reasoning steps ("let me think step by step..."), the model generates abstract tokens that represent reasoning operations in a compressed latent space, then decodes only the final answer in natural language.

This addresses the core cost driver in Conductor's cascade: reasoner model calls are expensive because they generate long CoT token sequences before producing the final answer. Abstract CoT suggests a middle path — models that perform reasoning in a compressed abstract space, achieving CoT-quality results at closer to chat-model token costs.

For Conductor specifically: if DeepSeek or another provider exposes an abstract-CoT model, it would slot into the cascade between `deepseek-chat` (latent/no explicit reasoning) and `deepseek-reasoner` (full CoT), potentially handling queries that currently escalate to reasoner at lower cost. This is a model-capability evolution to monitor rather than an immediate integration target.

Related to `@sources/cot-vs-latent-thought-2509.25239.md` — that paper establishes the theoretical computational separation; this paper proposes a practical mechanism for occupying the middle ground.

## Snippets

- Abstract CoT compresses reasoning chains into shorter, denser token sequences by representing reasoning operations in a compressed latent space rather than full natural language. [Source: Thinking Without Words.pdf]
- Achieves reasoning quality comparable to full CoT with substantially fewer output tokens, directly addressing the cost/latency gap between chat and reasoner models. [Source: Thinking Without Words.pdf]
- If exposed as a model capability, Abstract CoT would occupy the middle ground between pure latent reasoning (chat models) and full explicit CoT (reasoner models). [Source: Thinking Without Words.pdf]
