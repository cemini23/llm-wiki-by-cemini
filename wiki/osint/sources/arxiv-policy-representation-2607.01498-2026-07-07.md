---
title: Towards learning representations of policies in 2p zero-sum imperfect-info games (arXiv 2607.01498)
type: source
tags: [source, arxiv, poker, game-theory, representation-learning, k148]
keywords: [2607.01498, policy-representation, SSL, imperfect-information, poker]
related:
  - concepts/policy-representation-learning-imperfect-info.md
  - concepts/multi-agent-fictitious-play-llm.md
  - concepts/devfun-poker-agent-challenge-2026.md
  - entities/tools/pokerkit.md
maturity: draft
read_status: skimmed
created: 2026-07-07
updated: 2026-07-07
clusters: [poker, game-theory]
---

## Relations

- @concepts/policy-representation-learning-imperfect-info.md — K148 synthesis
- @concepts/devfun-poker-agent-challenge-2026.md — HU sandbox opponent modeling hook

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2607.01498](https://arxiv.org/abs/2607.01498) |
| **Authors** | Kevin Wang, Kevin Yang, Arjun Prakash, Amy Greenwald |
| **License** | CC BY 4.0 |
| **Code** | https://github.com/VitamintK/ssl-project |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2607.01498-towards-learning-representations-of-policies-in.pdf` |

## Narrative

Self-supervised / representation-learning approach to encode **policies** (not just states) in two-player zero-sum imperfect-information games. Poker-arena steal: embed opponent `decide()` trajectories for clustering / exploit routing in HU sandbox — complements MAFP + multi-axis eval from K146 cluster. `[TENTATIVE]` — verify method transfer to No-Limit HU before implementation.

## Snippets

> "Towards Learning Representations of Policies in Two-Player Zero-Sum Imperfect-Information Games" [Source: arXiv:2607.01498]
