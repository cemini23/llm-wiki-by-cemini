---
title: Silent errors in structured output
type: concept
maturity: draft
related:
  - sources/arxiv-silent-order-errors-browser-llm-2611.18284.md
updated: 2026-11-16
---

## Raw Concept

Question this page answers: what is a silent error, and why does schema validation not catch it?

From arXiv 2611.18284 (a browser-deployed order parser).

## Narrative

A model that converts free text into structure fails in two ways.

**Loud failure.** The output is malformed — unclosed structure, wrong type, unknown field. A parser rejects it and the caller retries. This is the failure everybody instruments.

**Silent failure.** The output is perfectly well formed and describes something the user did not say. It parses, it validates, it looks right, and it is wrong. Every structural check passes because nothing structural is broken.

A validator that checks schema cannot see this. Catching it needs a semantic comparison — a second check that asks whether the structured result means the same as the input. The demo does this with the benchmark's own matcher, ported to run client-side, so it can score every ticket as the user types.

The design rule: any pipeline that turns language into actions needs a semantic matcher on the output, not only a schema check. And it must be cheap enough to run on every interaction, or it will be skipped under load.

[TENTATIVE] Demonstrated on one narrow domain (pizza orders) with one small model.

## Snippets

> "It can print something broken, which any system rejects. Or it can print a clean, well formed order that nobody placed."
