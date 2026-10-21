---
title: "Before Retrieval Begins — tool admission is not text refusal"
type: source
related:
  - concepts/k293-cybersec-wave.md
maturity: draft
read_status: skimmed
updated: 2026-10-20
---

## Raw Concept

Title: Before Retrieval Begins: Safety and Tool-Use Decisions in LLM Agents
Authors: Aditya Nawal, Manit Baser, Mohan Gurusamy (National University of Singapore)
Type: arXiv preprint (2610.23071)
Location: `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2610.23071-before-retrieval-begins-safety-and-tool-use-deci.pdf`
Retrieved: 2026-10-20
Read status: skimmed (abstract)

## Narrative

Tool-safety work usually starts after the call. This paper scores the earlier decision: whether to call the tool at all.

Across seven open-weight models, the unweighted average harm rate after an admitted harmful request is **74.5%**. A factorial edit of the request finds that neutralizing the requested operation produces the largest admission contrast, **19 points**. A linear direction fit on that contrast moves held-out admission in four of the seven models. It is not only an operation-specific switch, because it also moves some operation-neutralized requests.

Written refusal is only partly the same decision. A written refusal accompanies **33.6%** of admitted harmful calls. Plain-text refusal training reduces unsafe admission in models that still do benign tool use. Text refusal is not a proxy for the call decision. Evaluate and supervise admission directly.

The paper includes model-generated harmful text. This page does not. **No PoC.**

## Snippets

> "They motivate direct evaluation and supervision of tool admission rather than treating text refusal as its proxy." [Source: arxiv-2610.23071 abstract]
