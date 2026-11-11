---
title: "Continual-ARC — measuring skill acquisition over a working lifetime"
type: source
tags: [source, arxiv, benchmark, continual-learning, agents, harness]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-11
updated: 2026-11-11
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Continual-ARC: Measuring Skill Acquisition over a Working Lifetime |
| Author | Daniel Lenton (Unify) |
| arXiv | 2611.14505 |
| Pages | 51 |
| Read status | skimmed (abstract) |

## Narrative

**The benchmark that fixes what current continual-learning benchmarks cannot do.**

Three stated limitations of existing work:

- they focus on a **single applied domain**;
- they **serve each instance only once**;
- they assume a **single family of learner**, so memory-based and weight-based systems are rarely compared on the same scale.

### The design

Built from the **three ARC-AGI editions**, whose tasks need **no domain knowledge**. That is what makes cross-domain and cross-learner comparison possible at all — nothing in the task presupposes a specialty.

Two properties matter:

- **Dormant gaps.** The same tasks **return after a gap with fresh instances**, so a system that memorised answers does not benefit, but a system that learned the skill does.
- **New tasks keep arriving.** The stream does not end.

On each instance the learner may **pay for demonstrations, submit answers, or act inside the harness**, with retries permitted. Cost is part of the measurement.

### Why the return-with-fresh-instances design is the key

It is the only design that distinguishes **memorising** from **learning** without changing the task distribution. If a task returns and the learner solves a *new* instance, the capability transferred. If it only solves the one it saw, it memorised.

That is the same test this workspace implicitly applies when asking whether a claimed pattern transfers to a new project — and the same test that distinguishes a skill from a saved answer.

**Caveat.** Abstract only. No leaderboard or cost figures reproduced.

## Snippets

> "The same tasks return after dormant gaps with fresh instances, while new tasks keep arriving." [Source: arxiv-2611.14505 p.1]

> "On each instance, the learner may pay for demonstrations, submit answers, or act inside the harness, with retries permitted." [Source: arxiv-2611.14505 p.1]

## Dead Ends

- **Citing a result.** Abstract only.
