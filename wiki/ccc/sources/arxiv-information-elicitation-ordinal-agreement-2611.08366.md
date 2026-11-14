---
title: "Information elicitation by ordinal agreement (Kendall tau peer prediction)"
type: source
related:
  - concepts/ordinal-peer-prediction.md
  - concepts/auto-researcher-human-similarity.md
  - concepts/gatekeeper-layered-agent-evaluation.md
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Information Elicitation by Ordinal Agreement |
| Author | Yiling Chen, Shi Feng, Grant Schoenebeck, Fang-Yi Yu |
| Type | arXiv paper (cs.GT), 2611.08366 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2611.08366-information-elicitation-by-ordinal-agreement.pdf` |
| Retrieved | 2026-11-10 |
| Pages | 33 |
| Read status | read |

## Narrative

Many evaluation tasks need ordinal judgement and have no ground truth. Examples are peer review, peer assessment, and RLHF preference collection. Without ground truth, a mechanism cannot pay for "correct" answers. Peer prediction pays agents for the statistical agreement between their reports.

Older peer-prediction mechanisms assume the agent reports all private information. That fails when an agent holds rich private information, such as a full review, but the designer wants a coarse ordinal report, such as a ranking.

The paper proposes a simple mechanism. Reward each agent by the **pairwise agreement** of its report with a peer, measured by Kendall tau. The mechanism supports full rankings, top-K sets, bucket orders, and rankings over subsets. Each agent is scored against one randomly drawn peer.

The theoretical result holds under **Bayesian Stochastically Order Consistent (Bayesian SOC)** information structures. This class includes the Mallows and Thurstone models. Under these structures, truthful ordinal reporting is stochastically dominant, and strongly truthful when strategies cannot coordinate on an item index. Stochastic dominance also gives robustness to nonlinear utility, such as risk aversion.

Experiments use synthetic Mallows and Thurstone data and a real-data stress test on the SUSHI preference dataset. Truthful payments shift right, and the mechanism has the highest normalised sensitivity among tested baselines.

Relevance to Cemini: this is a design rule for any panel that asks several models or humans to rank outputs. **Pay or weight by pairwise agreement, not by absolute score.** It also explains why a cheap ordinal review can be more honest than a calibrated 1-10 rubric.

## Snippets

> "We propose a simple ordinal peer-prediction mechanism that rewards agents based on pairwise agreement, measured by Kendall tau." [Source: arxiv-2611.08366-information-elicitation-by-ordinal-agreement.pdf p.1]
