---
title: "Premise scope and dependency invalidation"
type: concept
related:
  - sources/arxiv-physscope-agentic-multimodal-physics-2611.23010.md
  - concepts/lossless-visual-memory-harness.md
  - concepts/harness-attribution-multimodal-eval.md
  - concepts/typed-judgement-desk-pattern.md
updated: 2026-11-22
---

## Raw Concept

Question this page answers: a fact was true in state A and is revised in state B. What else becomes untrustworthy?

Synthesised from one source: `@sources/arxiv-physscope-agentic-multimodal-physics-2611.23010.md` (PhysScope, 2611.23010).

## Narrative

PhysScope defines the **scope** of a premise with three parts: the entities it concerns, the states in which it applies, and the conditions under which it holds. A model can read a diagram correctly and still apply a constraint outside its scope. The error then propagates.

The paper's harness enforces two rules:

1. Attach scope to each premise during reasoning.
2. When a revision is accepted, **invalidate every registered dependent**.

That second rule is the general one. Accepted changes do not silently coexist with conclusions drawn from the old value. Dependents are marked stale and must be re-derived.

### Why it transfers

The same structure appears in three Cemini places:

- **Wiki pages.** When a source page is superseded, every claim derived from it should be re-checked. The `[RETRACTED]` tag and the `related:` graph are a manual version of this.
- **Agent working memory.** A revised plan invalidates the sub-tasks built on the old plan.
- **Backtests.** A changed data snapshot invalidates results that used the old one.

PhysScope reports +9.34 points over Canvas-CoT with Gemini-3.8-flash, and gains on out-of-distribution PhysUniBench. [TENTATIVE] single source; effect is measured on physics VQA.

## Snippets

> "Accepted revisions invalidate registered dependents, thereby maintaining scope-aware working memory." [Source: arxiv-2611.23010-physscope-agentic-multimodal-physics-reasoning-w.pdf p.1]

> "We define the scope of a premise by the entities it concerns, the states in which it applies, and the conditions under which it holds." [Source: arxiv-2611.23010-physscope-agentic-multimodal-physics-reasoning-w.pdf p.2]
