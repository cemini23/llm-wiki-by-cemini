---
title: "Comparing three agent evaluation paradigms on enterprise analytics agents"
type: source
tags: [source, arxiv, evaluation, agents, enterprise, benchmark]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-11
updated: 2026-11-11
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Comparative Analysis of Agent Evaluation Frameworks: Stability, Detection, and Discovery in Enterprise Analytics Agents |
| Authors | Howard Zhang, Chuck Arvin, Logan Brown, Mihir Bhatia, Neelu Choudhary, Lily Miao (Amazon) |
| arXiv | 2611.14493 |
| Pages | 9 |
| Read status | skimmed (abstract) |

## Narrative

A three-phase comparison of three evaluation paradigms on the same class of agent — LLM analytics agents doing multi-tool enterprise workflows:

1. **Trace-based LLM judging**
2. **Text-only LLM judging with red-teaming**
3. **Deterministic heuristics**

The framing — **stability, detection, and discovery** — is the useful part. Those are three different questions, and an evaluation framework that is good at one is often poor at another:

- **Stability** — does the same agent score the same twice?
- **Detection** — does it catch failures that occurred?
- **Discovery** — does it surface failures nobody predicted?

A trace-based judge has more information and can therefore discover more; it can also be less stable, because a model scoring a trace varies. A deterministic heuristic is stable and only finds what it was written to find.

### Why the framing transfers

Any evaluation this workspace runs faces the same trade. The eval pipeline at the centre of six batches is a **discovery** instrument: it surfaces tools nobody predicted. It is not stable — the same URL re-tiers across passes — and it is not a detection instrument for whether a tool works.

Naming the three axes makes it possible to say which one a given evaluation is for, instead of treating "the eval" as one thing.

**Caveat.** Abstract only. No stability, detection-rate, or discovery figures reproduced.

## Snippets

> "We present a three-phase comparative study of three evaluation frameworks, each representing a distinct evaluation paradigm (trace-based LLM judging, text-only LLM judging with red-teaming, and deterministic heuristics)…" [Source: arxiv-2611.14493 p.1]

## Dead Ends

- **Citing which framework won.** Abstract only.
