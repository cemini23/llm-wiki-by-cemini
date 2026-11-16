---
title: "WeightBench: Evaluating Language Models as Weight-Space Programmers (2611.18553)"
type: source
maturity: draft
related:
  - concepts/weight-space-programming.md
updated: 2026-11-16
---

## Raw Concept

- **Title:** WeightBench: Evaluating Language Models as Weight-Space Programmers
- **Authors:** Aayush Marasini, Barsat Khadka, Nick Rahimi (University of Southern Mississippi)
- **Type:** arXiv preprint
- **Location:** `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2611.18553-weightbench-evaluating-language-models-as-weight.pdf`
- **Retrieved:** 2026-11-16
- **arXiv:** 2611.18553
- **Read status:** skimmed (abstract)

## Narrative

Weight-space programming is the claim that a language model can read, repair or write another network's parameters without gradient descent. WeightBench tests it on 42 tasks across five tracks: reading weights, fixing weights, writing weights, recognising impossible edits, and data-free compression. Target networks run from 2K-parameter control policies to 7B-parameter language models.

The headline split is between small and large targets. Frontier agents can already read small networks and write working control policies without ever running them. They cannot yet patch language models, compress them without data, or distinguish an impossible edit from a merely hard one.

Scores on all 42 tasks: Claude Opus 5.5 macro 0.535, Sonnet 5.5 0.466, Haiku 5.5 0.402, DeepSeek v4-flash 0.215. On the 38 tasks it ran, GPT-6.1-sol reaches 0.568 against Opus's 0.546.

The "impossible edit" track is the one worth remembering: a model that cannot tell an impossible edit from a hard one will keep trying, which is the failure mode that makes this technique unsafe to leave unattended.

[Source: arxiv-2611.18553-weightbench-evaluating-language-models-as-weight.pdf]

## Snippets

> "frontier agents can already read small networks and write working control policies without ever running them, but cannot yet patch language models, compress them without data, or tell an impossible edit from a hard one."
