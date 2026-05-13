---
title: Reasoning models — extended-chain-of-thought LLMs (o-series, R-series)
type: concept
tags: [concept, reasoning-models, chain-of-thought, test-time-compute, o1, deepseek-r1, llm-tier]
keywords: [reasoning models, chain of thought, test-time compute, o1, o3, deepseek r1, claude thinking, gemini thinking, retrieval during reasoning]
related:
  - sources/retrieve-during-reasoning.md
  - concepts/retrieval-augmented-generation.md
  - concepts/agent-cost-routing-model-orchestra.md
maturity: draft
created: 2026-05-13
updated: 2026-05-13
---

## Relations

- `@sources/retrieve-during-reasoning.md` — primary source: retrieval interleaved with reasoning steps
- `@concepts/retrieval-augmented-generation.md` — sibling concept; retrieval-during-reasoning is the next-gen RAG variant
- `@concepts/agent-cost-routing-model-orchestra.md` — reasoning models occupy the "expensive top tier" slot in routing

## Raw Concept

What prompted this page: retrieve-during-reasoning source needed a hub for the broader reasoning-model category. The o-series + R-series of LLMs that spend extra compute at inference deserve a concept page now that they're a separate procurement category.

## Narrative

A reasoning model spends extra compute at inference time — long internal chain-of-thought, multiple drafts, self-critique — to produce a better final answer than a standard chat model would. The category includes OpenAI's o1/o3, DeepSeek-R1, Claude Opus with extended thinking, Gemini with thinking modes.

**Key properties for Cemini procurement**:
- **Cost** — typically 5–20× the per-token cost of a chat-tier model, because most of the tokens are hidden CoT.
- **Latency** — seconds to tens of seconds per response, sometimes longer. Unsuitable for hot trading loops; suitable for plan-and-then-execute flows.
- **Failure mode** — over-thinking simple questions, sometimes producing worse answers than a chat model would.

**Cemini fit**: reasoning models earn their slot at the apex of the agent orchestra (`@concepts/agent-cost-routing-model-orchestra.md`) — final synthesis, decision gate, audit-trail summary. Cheap auxiliary models handle the upstream fan-out.

**Retrieval-during-reasoning** (cf. `@sources/retrieve-during-reasoning.md`) is the next-gen variant: the model issues retrieval queries mid-CoT, not just before. Promising for any Cemini surface that needs "look-it-up while you think" behavior (e.g. ticker research where facts update inside the reasoning trace).

This is a stub.
