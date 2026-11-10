---
title: "Visual token routing — spend context on the pixels that change the next action"
type: concept
related:
  - sources/arxiv-visual-token-routing-2611.06854.md
  - concepts/context-engineering.md
  - concepts/computer-use-agent-harness.md
  - concepts/token-economics-and-prompt-caching.md
updated: 2026-11-10
---

## Raw Concept

Question this page answers: for a computer-use agent, which parts of a screenshot history earn their context cost?

Synthesised from `@sources/arxiv-visual-token-routing-2611.06854.md`.

## Narrative

A single 1080p screenshot becomes about 2,000 visual tokens. A 100-step desktop task with full history holds more than 200,000 visual tokens by the last step. One minute of game play at 30 fps can hold about 400,000.

Visual Token Routing trains a small spatio-temporal router. It reads each image region across the current and previous K screenshots and decides whether the token enters the language model. Kept tokens are scaled by their keep probability, following mixture-of-experts practice. Dropped tokens are removed from the sequence.

Results with 2,000 training steps: full-resolution parity on OSWorld, CUA-World, and game action prediction, with 2.5 to 5.8 times fewer visual tokens, up to 3.3 times lower inference cost, and up to 2.9 times faster prefill. [TENTATIVE: single source, self-reported]

### The transferable test

The router is a trained component, so Cemini cannot adopt it directly. The rule underneath it transfers: **a token earns its place only if it can change the next action.** Two questions apply to any context decision:

1. Would the next action be the same without this token?
2. Is this token a repeat of one already in context?

Taskbars, unchanged backgrounds, and static documents fail both tests. So does a duplicated tool-output block in a Claude Code session.

### Relation to prompt caching

Removing tokens from the middle of a prompt changes the prefix and can invalidate a cache. A router that acts per step is safe only when the removed region is outside the cached prefix. See `@concepts/token-economics-and-prompt-caching.md`.

## Snippets

> "the router keeps only the tokens of the typed file name. It drops the regions that did not change, and also drops the circled part of the video, which changed but is not relevant to the task." [Source: arxiv-2611.06854-visual-token-routing-learning-to-keep-tokens-tha.pdf p.2]
