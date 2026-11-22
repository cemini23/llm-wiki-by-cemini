---
title: "PhysScope — premise scope and dependency invalidation in multimodal physics reasoning"
type: source
related:
  - concepts/premise-scope-dependency-invalidation.md
  - concepts/lossless-visual-memory-harness.md
  - concepts/harness-attribution-multimodal-eval.md
updated: 2026-11-22
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | PhysScope: Agentic Multimodal Physics Reasoning with Grounded Visual Memory |
| Author | Haoyang Liu, Kecheng Liang, Xinyu Li, Weixing Chen, Yang Liu (SYSU) |
| Type | arXiv paper (cs.CV), 2611.23010 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2611.23010-physscope-agentic-multimodal-physics-reasoning-w.pdf` |
| Retrieved | 2026-11-22 |
| Pages | 31 |
| Read status | read |

## Narrative

PhysScope is an inference-time visual harness. It targets a specific error: a model reads a diagram correctly, then applies a constraint outside the states or conditions in which it holds. The error then propagates through later calculations.

The paper defines the **scope** of a premise by three things: the entities it concerns, the states in which it applies, and the conditions under which it holds. Its example is a rope at 30° in state A and 53° in state B. A model that represents state B correctly can still substitute the 30° value into the velocity constraint at B.

The harness imposes explicit scope constraints during reasoning and checks proposed revisions against sources and scopes. Accepted revisions **invalidate registered dependents**, so working memory stays scope-aware.

On PhysAlign it beats direct solving across all six evaluated VLMs. With Gemini-3.8-flash it beats Canvas-CoT by 9.34 points and improves on out-of-distribution PhysUniBench. The ablations support explicit scope management and dependency maintenance as design principles.

The pattern is general, not physics-specific: when a fact is revised, everything derived from it must be marked stale. That is the same rule a wiki needs when a source page is superseded. [TENTATIVE] single source.

## Snippets

> "Accepted revisions invalidate registered dependents, thereby maintaining scope-aware working memory." [Source: arxiv-2611.23010-physscope-agentic-multimodal-physics-reasoning-w.pdf p.1]
