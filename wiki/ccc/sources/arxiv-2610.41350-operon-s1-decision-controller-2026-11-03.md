---
title: "Operon-S1 — separating judgement from doing with a System 1 decision harness"
type: source
tags: [source, arxiv, agents, architecture, system-one, separability]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-03
updated: 2026-11-03
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Operon-S1: a fast decision controller for long-horizon biomedical agents |
| Authors | Genoria AI Team — Yuejie Hou, Yueyuxiao Yang, Weiting Tang, Meng Yang |
| arXiv | 2610.41350 |
| Pages | 40 |
| Read status | skimmed (abstract) |

## Narrative

The problem it names is precise: in current agents, the judgements about **conventions, skills, errors, evidence, and stopping** are made **inside the reasoning that does the work**. Because they are entangled with the work, they cannot be measured, replaced, or improved separately.

Operon-S1 pulls those judgements out into a **decision harness**.

The mechanism has two parts:

1. **13 decision points** where the agent's recurring judgements are posed as **closed questions**.
2. The harness **acts only through fixed messages that never contain an answer**. So any model that can answer the questions can serve as the judge.

Across seven life-science benchmarks, a **local** decision model took over those judgements.

### Why the design is the contribution

The "messages never contain an answer" rule is subtle and load-bearing. It means the judge is answering *only* the question — it cannot see the intended action and agree with it. That removes the most common failure of a critic model, which is being led by the proposal it is judging.

Posing judgement as closed questions also makes it **measurable**. A free-text judgement cannot be scored; a closed answer can, and a scored answer can be replaced or improved.

### The generalisation, and its limit

Separating judge from doer is the same structure as CLEO and RoboArchitect in this batch — three papers, three domains, one idea: **the part of an agent that decides should be separable from the part that executes**, because separable parts can be measured.

The limit is that the decision points must be **enumerated in advance**. Thirteen points cover biomedical conventions; a different domain needs its own list, and building that list is the actual work.

### Caveat

Abstract only. No benchmark numbers are reproduced here.

## Snippets

> "A decision harness poses the agent's recurring judgements as closed questions at 13 decision points and acts only through fixed messages that never contain an answer, so any model that answers the questions can serve as the judge." [Source: arxiv-2610.41350 p.1]

## Dead Ends

- **Porting the 13 points to another domain.** They are biomedical. The list has to be rebuilt.
