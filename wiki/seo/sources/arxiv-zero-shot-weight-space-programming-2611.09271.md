---
title: "Zero-shot weight-space programming across a game ladder"
type: source
tags: [source, arxiv, neural-networks, out-of-scope]
keywords: [weight-space programming, ReLU circuit, Nim, Connect Four, chess endgame, difficulty ladder, no gradient descent]
related:
  - concepts/corpus-overflow-out-of-scope.md
maturity: draft
read_status: read
created: 2026-11-10
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Zero-Shot Weight-Space Programming Across a Difficulty-Graded Ladder of Two-Player Games |
| Author | Eduardo Garrido Merchán (Universidad Pontificia Comillas, IIT DIGNUM) |
| Type | arXiv preprint (cs.AI) |
| arXiv | 2611.09271v1, 6 Nov 2026 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2611.09271-zero-shot-weight-space-programming-across-a-diff.pdf` |
| Retrieved | 2026-11-10 |
| File | `arxiv-2611.09271-zero-shot-weight-space-programming-across-a-diff.pdf` |
| Pages | 24 |
| Read status | read (abstract, introduction) |

## Narrative

**The practice under test.** Weight-space programming sets every weight of a feed-forward network by hand, from a written specification of the wanted computation. No gradient descent. No training data. [Source: arxiv-2611.09271 p.1]

**The design.** A four-rung ladder of games, each rung with a second, structurally unrelated game at matched difficulty. The rungs are Nim, tic-tac-toe, two sizes of Connect Four, and a chess endgame. Ten networks are built and independently checked. **Six admit a complete proof of correctness** against an independent oracle. [Source: arxiv-2611.09271 p.1]

**The finding at the top rung.** Chess-endgame correctness is exact where it is cheap: move legality, and a one-ply mate detector. It **collapses where correctness is expensive**. One-ply tactics succeed at 84.1-100%. Full adversarial play falls to 0.57-9.13%. The collapse reproduces across two unrelated games, so the authors read it as an architectural ceiling rather than an engineering shortfall. [Source: arxiv-2611.09271 p.1]

### Relevance to SEO

**None.** This paper contains no search, retrieval, content or marketing component. It tests whether a language model can hand-build a neural network for a board game.

The one idea with any bearing outside the paper is the design: hold a variable fixed and vary one axis at a time, so a failure has a named cause. That is a general experimental discipline. It is not an SEO result.

Filed for inventory honesty only.

## Snippets

> "Every network in this ladder is constructed the same way the tic-tac-toe network was: as an explicit, named sequence of linear maps, ReLU non-linearities, and concatenations, with every entry of every weight and bias matrix assigned once." [Source: arxiv-2611.09271 p.2]

> "The standard-sized rung confirms, by holding hand-set evaluation weights fixed and adding only shallow search, that the remaining gap is an architectural ceiling rather than a matter of engineering effort." [Source: arxiv-2611.09271 p.1]

## Dead Ends

- **Reading this as an agent-capability result for web tasks.** The tasks are board games with exact oracles. No web task appears.
