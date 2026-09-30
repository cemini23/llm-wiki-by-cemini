---
title: "Harness learning for generalizable test-time adaptation (2609.35738)"
type: source
tags: [source, k276, agents, harness]
keywords: [k276, harness-learning, proposer, meta-learning, FILE]
related:
  - concepts/k276-harness-evolution-wave.md
maturity: draft
created: 2026-09-30
updated: 2026-09-30
read_status: skimmed
---

## Relations

- @concepts/k276-harness-evolution-wave.md

## Raw Concept

| File | `arxiv-2609.35738-harness-learning-enables-generalizable-test-time.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2609.35738-harness-learning-enables-generalizable-test-time.pdf` |
| Archive | egress-fi 2026-09-30 |
| Retrieved | 2026-09-30 |
| Dual-ID | **OSINT K276** |
| sha256 | `469fdb0f1673ab1aacce96d24a8a1f6a0c35a479db799e4574e65a3beb38678f` |
| arXiv | 2609.35738 |
| Authors | Alvin Zhang, Xuecheng Liu, Zixuan Wang, Fahim Tajwar, Daman Arora, Ruslan Salakhutdinov, Daniel Khashabi, Yuda Song, Andrea Zanette |

## Narrative

The paper defines an agent as a model plus its harness: the executable program that organizes model calls, tool use, and information flow.

The method, called harness learning, trains a proposer model to revise a solver's harness from execution feedback. The authors frame this as meta-learning over executable programs, where a harness revision plays the role of a weight update. The proposer trains with reinforcement learning, with revised-harness task performance as the reward.

At test time the proposer uses feedback from successive runs on a new task to refine the harness. No parameter update happens at test time.

Results: harness learning improves revision quality on reasoning and multi-hop question answering. The ability to adapt at test time transfers to unseen tasks. Policies trained on single revisions keep improving over multiple rounds.

The authors admit the benefit of training on revision sequences varies by setting.

This is the closest paper in the wave to our own harness work. It is a training method, not a drop-in tool. No code URL found. No clone. Do not auto-evolve our skills from it. FILE only.
