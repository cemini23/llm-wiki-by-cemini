---
title: "Replay for continual learning with multi-teacher on-policy distillation"
type: source
tags: [source, arxiv, continual-learning, distillation, replay, forgetting]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-03
updated: 2026-11-03
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Replay for LLM Continual Learning with Multi-Teacher On-Policy Distillation |
| Authors | Yiqiao Qiu (independent) |
| arXiv | 2611.02746 |
| Pages | 47 |
| Read status | skimmed (abstract) |

## Narrative

Multi-teacher on-policy distillation (MOPD) merges domain experts into one student, but needs **every expert available at once**. When domains arrive one at a time and earlier experts are gone, the problem is catastrophic forgetting.

The paper compares two recovery strategies against joint MOPD, on five domains with a **1.5B student and five public experts**:

1. **Self-replay** — the previous-stage student teaches replayed prompts from earlier domains at every stage.
2. **Snapshot recovery** — store every stage's snapshot, then run a final multi-teacher recovery stage.

It varies the replay budget and the replay signal — token-level distillation alone, or with alignment of hidden states, attention, and value relations.

Reported headline: sequential distillation without replay or recovery is **6.2 points below** 208-step joint MOPD on a 14-benchmark average, and **3.5 points below** on the 11-benchmark subset.

### Why the question is the right one

The realistic deployment is sequential — you get data, or a domain, not all of them at once. A method that requires all teachers simultaneously solves a problem nobody has. Reframing it as "what do you replay, and how much, when the teacher is gone" is the version that applies.

**Caveat.** Abstract only. The relative ranking of the two recovery strategies, and the effect of the richer replay signal, are not established on this page.

## Snippets

> "Sequential distillation without replay or recovery is 6.2 points below 208-step joint MOPD on a 14-benchmark average and 3.5 points below on the 11…" [Source: arxiv-2611.02746 p.1]

## Dead Ends

- **Citing which recovery strategy won.** Not established from the abstract.
