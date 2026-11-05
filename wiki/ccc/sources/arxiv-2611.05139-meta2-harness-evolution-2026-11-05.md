---
title: "Meta2 — learning how to evolve a harness, rather than one harness"
type: source
tags: [source, arxiv, harness, agents, meta-learning, long-horizon]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-05
updated: 2026-11-05
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Meta2: Precomputing Reusable Knowledge for Online Harness Evolution in Long-Horizon Agents |
| Authors | Lingzhi Yuan, Yiguang Cai, Weize Liu, Siqi Yang, Feijiang Han, Yongkyun Lee, Udari Madhushani Sehwag, Furong Huang (UMD, UW, UIUC, Scale AI) |
| arXiv | 2611.05139 |
| Pages | 45 |
| Read status | skimmed (abstract) |

## Narrative

Harness optimisation improves long-horizon agents by refining prompts, tools, memory, and hooks **around a frozen model**. Two existing modes both fail in a specific way:

- **Offline** learns from completed trajectories but ships **one shared harness**, which overfits the training tasks and cannot react to evidence that appears mid-run.
- **Online** adapts during a run but must reason about every intervention from scratch, or lean on verifier feedback that is usually **unavailable at test time**.

**Meta2 moves the offline optimisation one level up.** Instead of learning a harness, it learns **reusable knowledge about how to evolve a harness**, then applies that knowledge per task, online.

Offline it learns a textual **Meta-Skill** by contrasting training rollouts of the same task agent under three configurations.

### Why this is the right shape

It resolves the offline/online tension without picking a side. The expensive learning still happens offline, where trajectories exist and verification is possible. The *output* of that learning is not a fixed artefact but a procedure, so it does not overfit and it can act on mid-run evidence.

That is the distinction that matters: **ship an adaptation method, not an adapted harness.**

### Fit

This is the fourth paper in two batches to argue that the harness, not the model, is where the leverage is — alongside CLEO, RoboArchitect, and Ask-Don't-Equip. Meta2 adds the missing piece: how to keep that adaptation from overfitting.

**Caveat.** Abstract only. No benchmark figures reproduced.

## Snippets

> "Rather than optimizing a shared harness, it learns reusable knowledge for harness evolution and applies it within each task online." [Source: arxiv-2611.05139 p.1]

## Dead Ends

- **Citing a result.** Abstract only.
