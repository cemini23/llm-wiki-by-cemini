---
title: "Qistas — a pre-registered, portable fairness evaluation protocol"
type: source
tags: [source, arxiv, fairness, evaluation, protocol, iraq]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-03
updated: 2026-11-03
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Qistas: A Pre-Registered, Portable Protocol for Fairness Evaluation of Large Language Models |
| Authors | Nawar S. Alseelawi (University of Misan), Mustafa S. Aljumaily (Missan Oil Company) |
| arXiv | 2610.40893 |
| Pages | 19 |
| Read status | skimmed (abstract) |

## Narrative

Two criticisms of fairness benchmarks, both fair:

1. They are **English-born and American in their social categories**. Translated versions carry those categories into societies where they do not apply.
2. **Almost none fix their hypotheses before the models are run.** The categories can be chosen after seeing results.

Qistas (Arabic qisṭās, "the just balance") is a **protocol**, not a benchmark: designed to be portable across countries, and **instantiated first for Iraq**. It evaluates how LLMs treat a society's social, confessional, and regional constituencies.

### Why pre-registration is the contribution

A fairness benchmark that picks its categories after seeing model behaviour can find a disparity in anything. Fixing the hypotheses first is the only way the result can falsify something.

That discipline is identical to the one this workspace applies to backtests — define the metric and the split before the run, or the run finds whatever you were looking for.

### The portability design

Rather than translating an American instrument, the protocol defines a **procedure** for a country to construct its own instantiation. That is the difference between localization and translation, and it is why the paper claims portability rather than coverage.

**Caveat.** Abstract only. The reviewed seed and the Iraqi instantiation are not reproduced here.

## Snippets

> "Fairness benchmarks for large language models (LLMs) are overwhelmingly English-born and American in their social categories; translated versions carry those categories into societies where they do not apply, and almost none fix their hypotheses before the models are run." [Source: arxiv-2610.40893 p.1]

## Dead Ends

- **Reading this as a benchmark you can run.** It is a protocol for constructing one.
