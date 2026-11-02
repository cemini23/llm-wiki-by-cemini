---
title: "heretic — training-free refusal-direction ablation (licence unstated)"
type: entity
tags: [tool, abliteration, model-modification, local-lab, defensive-research, licence-unknown]
keywords: [heretic, abliteration, refusal direction, weight modification, training-free, slop suppression]
related:
  - "@osint-wiki/sources/eval-multi-wiki-link-revenue-v10.10-batch-c-2026-11-02.md"
maturity: draft
created: 2026-11-02
updated: 2026-11-02
---

## Raw Concept

Surfaced by @osint-wiki/sources/eval-multi-wiki-link-revenue-v10.10-batch-c-2026-11-02.md, URL 10, **Extract** tier. Routed to the local-abliterated / operator lab.

The question this page answers: **how is a refusal direction removed from a model's weights, and what does it cost?**

## Narrative

### What it does

`p-e-w/heretic` modifies model weights directly, with no training.

Two effects:

1. **Strips safety-refusal directions** from the weights.
2. **Suppresses conversational "slop"** — the filler phrasing a model produces by default.

The claim is that base-model **coding and reasoning capability is preserved**.

### Why "training-free" matters

Abliteration is a weight-space edit, not a fine-tune. There is no dataset, no gradient step, and no run. The refusal behaviour is treated as a direction in activation space that can be projected out.

The consequence is that the edit is fast and cheap, and the consequence of *that* is that capability damage is easy to miss. A fine-tune has a training curve that shows degradation. A weight projection has none. The only way to know what was lost is to measure.

**So measure.** Run capability benchmarks before and after, on the tasks that matter for the intended use. "Preserves coding" is the author's claim, on the author's choice of tasks.

### Scope — this lab's rules

This page documents a capability for the **local-abliterated / operator lab** under its existing constraints:

- Authorized defensive and whitehat scope only.
- Zero crimeware.
- No TipDrop or David-kit routing.

The workspace's abliteration work has treated the technique as an object of study — measuring what it does to model behaviour — not as a way to produce a model for misuse. That framing does not change here.

### The licence problem

**Licence not found** in the repository metadata. The report notes it is archived on Software Heritage and installable via `pip install git+https://github.com/p-e-w/heretic.git`.

An unstated licence means the code cannot be redistributed, and arguably should not be vendored. Use it as a **method reference** and re-implement if it needs to ship anywhere.

Verify the licence before installing it into an environment that is not disposable.

### Status

Extract, **method reference**, licence unresolved.

## Snippets

> "Upgrades the Cybersecurity wiki/briefs/ (local-abliterated-lab) planner+executor stack with an in-house, training-free weight modification pipeline that strips safety-refusal directions and suppresses conversational slop while preserving base model coding and…" — report, URL 10

> "License: NOT FOUND — archived on Software Heritage and installable via pip install git+https://github.com/p-e-w/heretic.git." — report, URL 10

## Dead Ends

- **Assuming capability is preserved because the author says so.** There is no training curve to inspect. Measure it.
- **Vendoring code with no stated licence.** It cannot be redistributed.
