---
title: "Ordinal peer prediction — pay for pairwise agreement, not absolute score"
type: concept
related:
  - sources/arxiv-information-elicitation-ordinal-agreement-2611.08366.md
  - concepts/auto-researcher-human-similarity.md
  - concepts/gatekeeper-layered-agent-evaluation.md
  - sources/arxiv-auto-researchers-reconstruct-human-2611.12429.md
updated: 2026-11-10
---

## Raw Concept

Question this page answers: how do you reward honest ranking when no ground truth exists?

Synthesised from `@sources/arxiv-information-elicitation-ordinal-agreement-2611.08366.md`.

## Narrative

Peer review, peer assessment, and RLHF preference collection share three properties. Evaluators hold informative but imperfect signals. Effort improves judgement. There is no verifiable ground truth.

Peer prediction pays agents for statistical agreement between reports instead of for correctness. Older mechanisms assume the agent reports all private information. That fails when an agent holds a rich review but the designer asks only for a ranking.

The mechanism here is simple. Reward each agent by pairwise agreement between its report and one randomly drawn peer, measured by **Kendall tau**. It supports full rankings, top-K sets, bucket orders, and rankings over assigned subsets.

The guarantee holds under **Bayesian Stochastically Order Consistent** information structures, which include the Mallows and Thurstone models. Truthful ordinal reporting is stochastically dominant, and strongly truthful when strategies cannot coordinate on an external item index. Stochastic dominance also survives risk-averse utility.

### Why it matters for model panels

Cemini runs multi-model councils (`super-audit`, `free-audit`, `council-of-high-intelligence`). Most of those ask each model for a verdict or a score. This paper suggests a cheaper and more honest protocol:

- Ask each model to **rank** the candidate patches, not to score them.
- Score a model's judgement by pairwise agreement with the panel, not by whether its number was closest to the mean.
- Compare against one randomly drawn peer, not the whole panel, to keep the reward simple and auditable.

### Caveat

The guarantee is for agents that are paid. A model asked to rank in a prompt has no incentive to be truthful. The result informs **how to weight** panel votes, not how to motivate the models.

## Snippets

> "we prove that truthful reporting is stochastically dominant, and strongly truthful under index-equivariant strategies." [Source: arxiv-2611.08366-information-elicitation-by-ordinal-agreement.pdf p.1]
