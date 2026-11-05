---
title: "Sparse internal control — steering a frozen model from a few nodes"
type: source
tags: [source, arxiv, activation-steering, control, interpretability]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-05
updated: 2026-11-05
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Sparse Internal Control of Language Models |
| Author | Xizhe Zhang |
| arXiv | 2611.04349 |
| Pages | 45 |
| Read status | skimmed (abstract) |

## Narrative

Activation steering can change a frozen model's behaviour without training. The open question is **how to choose and evaluate a compact, multi-site control interface** — which nodes, which directions, how many.

### The framework

A **local target-controllability** formulation characterises candidate **site–direction pairs** by their behavioural effects, under three constraints:

- **target recovery** — does the intended behaviour appear,
- **off-target preservation** — does everything else stay put,
- **intervention energy** — how much perturbation is applied.

Two selectors instantiate it: **Driver-OMP** selects nodes by sparse reconstruction of a desired behavioural displacement; **Coverage-Driver** favours stable coverage across prompts.

Plus a **six-axis evaluation protocol**: reachability, signed reversal, dose response, feedback, and two more.

### Why the constraints are the contribution

The interesting part is not that steering works — it does. It is that the framework makes the **tradeoff explicit**. Any intervention that moves a behaviour also perturbs everything else; the question is how much and where. Naming off-target preservation as a constraint rather than hoping for it is the discipline.

The six-axis protocol is the other half. Most steering results report that a behaviour changed. Reporting **signed reversal** (does the opposite direction reverse it?) and **dose response** (does more do more?) turns a demonstration into a measurement.

### Relevance here

This is the constructive counterpart to the abliteration work in the lab and to the single-neuron investment-bias finding: if a behaviour can be moved from a handful of nodes, then the same handful must be checked before any claim that a model's behaviour is intrinsic.

**Caveat.** Abstract only; no effect sizes.

## Snippets

> "A local target-controllability formulation characterizes candidate site–direction pairs by their behavioral effects and specifies constraints on target recovery, off-target preservation, and intervention energy." [Source: arxiv-2611.04349 p.1]

## Dead Ends

- **Citing a steering effect size.** Abstract only.
