---
title: "IRumAI — reinforcement learning for Indian Rummy PPO (arXiv 2606.21975)"
type: source
tags: [source, arxiv, rummy, reinforcement-learning, ppo, k129]
keywords: [2606.21975, IRumAI, Indian Rummy, PPO, meld-aware, deadwood, PettingZoo]
related:
  - concepts/devfun-poker-agent-challenge-2026.md
  - sources/arxiv-garip-self-play-2606.22688-2026-06-23.md
  - sources/arxiv-poker-arena-multi-axis-2606.13815-2026-06-18.md
  - concepts/multi-agent-fictitious-play-llm.md
  - concepts/irumai-indian-rummy-rl.md
maturity: draft
read_status: read
created: 2026-06-25
updated: 2026-10-25
clusters: [rl-marl, llm-agents]
---

## Relations

- @concepts/devfun-poker-agent-challenge-2026.md — imperfect-information card-game adjacent research
- @sources/arxiv-garip-self-play-2606.22688-2026-06-23.md — self-play regularization cluster (K127)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | IRumAI: Reinforcement Learning for Indian Rummy |
| **Authors** | Vignesh Mohan (IEEE CoG 2026) |
| **arXiv** | 2606.21975v1 (Jun 2026) |
| **sha256** | `f522a891bfc807b6c3caaab1dc491992e544ecf522b65325ba9ebb4959df192c` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2606.21975-irumai-reinforcement-learning-for-indian-rummy.pdf` |
| **Retrieved** | 2026-06-25 (inbox) |
| **Read status** | read (abstract + method stack) |

## Narrative

First RL agent for **13-card two-player Indian Rummy** — meld-validity constraint, wildcard joker, ~$7×10^{22}$ deal configurations [TENTATIVE — paper §III].

**Stack:** PettingZoo env, **ten-channel meld-aware observation**, dual-branch conv net, **PPO** vs fixed weak heuristic pool, BC warm-start on stronger demos, **potential-based deadwood reward shaping**.

**Results:** 53.9% win rate vs strongest search heuristic **MinDistOppAgent** (unseen in RL training); **0.33 ms/action** vs >2.3 s for search baseline (>7,000× faster) [TENTATIVE]. Linear probing: trunk encodes implicit opponent-hand info from public discards.

**Cemini posture:** **REFERENCE** for poker-arena — meld/sparsity reward shaping + fast inference without search; not NLHE transplant without sim.

## Snippets

> "Despite its massive player base and complex hidden-information dynamics, Indian Rummy has received no reinforcement learning attention." [Source: arXiv:2606.21975 abstract (retrieved 2026-06-25)]

> "IRumAI requires just 0.33 ms per action, which is over 7,000× faster than the state-of-the-art heuristic." [Source: arXiv:2606.21975 abstract (retrieved 2026-06-25)]

> "Linear probing reveals that the network implicitly models the opponent's hidden hand from public interactions." [Source: arXiv:2606.21975 abstract (retrieved 2026-06-25)]

## Dead Ends

- Rummy meld partition ≠ poker betting tree — environment code released but different game graph.
