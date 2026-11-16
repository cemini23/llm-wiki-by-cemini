---
title: The agent harness as a learned program, not fixed scaffolding
type: concept
maturity: draft
related:
  - sources/arxiv-modharness-rl-2611.18533.md
updated: 2026-11-16
---

## Raw Concept

Question this page answers: should the harness around an agent be hand-written and frozen, or learned alongside the model?

From ModHarness-RL (arXiv 2611.18533).

## Narrative

Most agentic RL fixes the harness while training the model. The paper's argument is that the right harness depends on the domain, the data and the model, and shifts as the model improves — so it should be a learned object.

The construction splits the harness into two programs over a structured record of the interaction:
- **Compression** decides what of the accumulated history enters the context.
- **Steering** supplies guidance when behaviour deviates.

During RL, candidate programs are proposed from recent trajectories, verified by execution, and replayed over past trajectories. The harness therefore tracks the model's changing behaviour rather than staying at its initial guess.

Reported result: held-out improvement over a fixed-harness baseline in most settings, on CodeSearch, ALFWorld and BIRD SQL, with 1.5B to 8B models.

Transferable idea, independent of RL: context assembly and deviation guidance are two distinct, separable levers. A harness that only tunes context (retrieval, summarisation) and never tunes guidance is leaving one lever fixed.

[TENTATIVE] One paper's abstract. The "most settings" qualification is load-bearing and the failure cases are not described there.

## Snippets

> "a harness for agentic RL can be learned from the task's data and evolved with the model."
