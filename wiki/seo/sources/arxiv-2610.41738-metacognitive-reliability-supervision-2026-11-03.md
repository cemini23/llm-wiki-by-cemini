---
title: "Search when needed — supervising the decision to search, not the answer"
type: source
tags: [source, arxiv, agents, search, reinforcement-learning, reliability]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-03
updated: 2026-11-03
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Search When Needed, Proceed When Reliable: Metacognitive Reliability Supervision for Efficient Agentic Search |
| Authors | Minhao Sun, Zhijing Wu, Xian-Ling Mao (Beijing Institute of Technology) |
| arXiv | 2610.41738 |
| Pages | 12 |
| Read status | skimmed (abstract) |

## Narrative

Efficient agentic search needs a model to decide **whether it can proceed on what it knows** or must retrieve more.

The paper's critique of the obvious approach: supervising on **final-answer correctness** or trajectory-level feedback evaluates what the trajectory produced. But that output is jointly shaped by stochastic generation, retrieval quality, and downstream reasoning. So the signal is only **indirect evidence** about whether the decision state was reliable, and how retrieval changed it.

Their alternative is a **metacognitive framework** that scores two things separately:

- **Current-state reliability** — can the model proceed without searching?
- **Search-action score** — how much does retrieved evidence change that reliability?

Together these define the reward.

### The separation is the contribution

Collapsing "was the answer right" into "should I have searched" conflates three sources of variance. Splitting the reward into a state score and an action score means the model is trained on the decision, not on the outcome.

That is the same discipline as reporting calibration separately from accuracy: the useful quantity is the confidence, not the verdict.

**Relevance.** Any agent that decides whether to look something up — including this workspace's own retrieval habits — is making this decision. The framing to steal is: reward the decision quality, not the answer.

**Caveat.** Abstract only. No benchmark figure reproduced.

## Snippets

> "An effective reward should encourage search when external information is needed and favor searches that contribute to the answer." [Source: arxiv-2610.41738 p.1]

## Dead Ends

- **Citing an improvement figure.** Abstract only.
