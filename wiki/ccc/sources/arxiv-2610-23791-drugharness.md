---
title: "DrugHarness — evolvable skills for computational discovery workflows"
type: source
related:
  - concepts/k293-ccc-wave.md
maturity: draft
read_status: skimmed
updated: 2026-10-20
---

## Raw Concept

Title: DrugHarness: An Evolvable Agent Harness for Computational Drug Discovery
Authors: Yuxing Chen, Zhisheng Zhang, and colleagues (Shanghai Artificial Intelligence Laboratory; China Pharmaceutical University; and others)
Type: arXiv preprint (2610.23791)
Location: `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2610.23791-drugharness-an-evolvable-agent-harness-for-compu.pdf`
Retrieved: 2026-10-20
Read status: skimmed (abstract only)

## Narrative

DrugHarness is a skill harness around computational discovery tools. The operator-relevant claim is the loop, not the chemistry. This page does not record assays, structures, scores, or protocols.

The loop has three parts. A library of tool calls keeps the link between a candidate, a result, and the artifact. The harness proposes a skill only with an applicability condition and a cited piece of evidence. A separate agent reviews that skill, by source checks and by a targeted trial, and later runs update the skill's scope.

That is the same shape as a propose-then-verify gate. The reviewer is not the agent that wrote the skill. **No clone. No lab use. No install.**

## Snippets

> "An independent agent reviews candidate skills through source checks and targeted scientific trials when needed, while subsequent execution feedback refines their content and scope." [Source: arxiv-2610.23791 abstract]
