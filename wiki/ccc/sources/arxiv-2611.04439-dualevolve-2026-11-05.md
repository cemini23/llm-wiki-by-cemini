---
title: "DualEvolve — separate signal for experiment quality, not just task score"
type: source
tags: [source, arxiv, self-improvement, agents, recommender-systems, orchestration]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-05
updated: 2026-11-05
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | DualEvolve: Dual-Level Self-Evolution of Mechanism and Orchestration for Recommendation |
| Authors | Tianqi Gao (independent), Chenxu Wang (Meituan), Wenxuan Ya and others |
| arXiv | 2611.04439 |
| Pages | 12 |
| Read status | skimmed (abstract) |

## Narrative

Recommender-system development is a repeated cycle: design a model, train, validate, iterate. LLM agents increasingly run that cycle, and sustained improvement requires evolving **both the model and the development workflow**.

The paper's observation is precise: **task-performance-driven approaches select updates by final score alone**, so the agent gets no separate signal about *the quality of its experimentation*.

### The two levels

- **Inner evolution** — revises model and training code using task feedback, to improve recommendation performance.
- **Outer evolution** — scores the **inner-loop experimental process**, updates **harness and skill rules** from those scores and execution traces, and adjusts orchestration choices based on next-round scores.

So the outer loop optimises for *better experiments*, not better scores.

### Why the separation matters

A loop that only rewards final score will happily converge on whatever cheaply moves the metric — the same failure mode as tuning on a validation set. Giving the process its own score creates pressure toward experiments that **produce information**, which is what makes the next round better rather than just different.

It is the same distinction this workspace applies to DFS tuning: tune on the stable metric, validate on the noisy one. Here, score the experiment, not only the outcome.

**Caveat.** Abstract only. Evaluated on MovieLens-1M and three Amazon datasets; no figures reproduced.

## Snippets

> "Task-performance-driven approaches select updates mainly by candidates' final scores, without a separate optimization signal for experimentation quality." [Source: arxiv-2611.04439 p.1]

## Dead Ends

- **Citing a lift.** Abstract only, and the domain is recommendation.
