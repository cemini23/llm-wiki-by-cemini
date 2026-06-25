---
title: IRumAI — reinforcement learning for Indian Rummy
type: concept
tags: [concept, card-games, rl, imperfect-information, k129, gambling-cross]
keywords: [IRumAI, Indian Rummy, PPO, meld-validity, deadwood, EURECOM, hidden information]
related:
  - sources/arxiv-irumai-indian-rummy-ppo-2606.21975-2026-06-25.md
  - concepts/poker-arena-multi-axis-cognitive-profile.md
  - concepts/active-project-research-routing.md
  - concepts/rl-marl-research.md
maturity: draft
created: 2026-06-25
updated: 2026-06-25
---

## Relations

- @sources/arxiv-irumai-indian-rummy-ppo-2606.21975-2026-06-25.md — primary source (arXiv 2606.21975)
- @concepts/poker-arena-multi-axis-cognitive-profile.md — sibling imperfect-info card-game eval cluster (poker HU sandbox)
- @gambling-wiki/concepts/card-games-imperfect-information.md — cross-wiki: retail rummy / meld-game domain (stub if missing)

## Raw Concept

Prompted by arXiv **2606.21975** (K129). First RL agent for **Indian Rummy** — meld-validity constraints, wildcard dynamics, deal space >7×10²² configurations.

## Narrative

Indian Rummy differs from poker: a hand is **functionally worthless** until all thirteen cards partition into valid sequences/sets. IRumAI uses PPO with meld-aware observations, deadwood-driven reward shaping, and dual-branch conv nets — BC warm-start on demonstrations, RL vs weak heuristics only, then generalizes to beat search baselines unseen in training.

| Metric | IRumAI | Strongest search baseline |
|--------|--------|---------------------------|
| Win rate vs SOTA heuristic | 53.9% | — |
| Inference latency | 0.33 ms/action | ~2.3 s (7000× slower) |

**Linear probing** suggests implicit opponent-hand modeling from public melds/discards — relevant to poker **Memory Gap** axis diagnostics [TENTATIVE].

**Cemini posture:**

| Surface | Verdict |
|---------|---------|
| poker-arena | **Out of scope** — full RL training pipeline; steal observation-encoding patterns only |
| @gambling-wiki | **REFERENCE** — Indian Rummy domain agent benchmark for card-game wiki |
| CeminiSuite prod | **No route** |

## Snippets

> "Despite its massive player base and complex hidden-information dynamics, Indian Rummy has received no reinforcement learning attention." [Source: arXiv:2606.21975 abstract (retrieved 2026-06-25)]

> "IRumAI requires just 0.33 ms per action, which is over 7,000× faster than the state-of-the-art heuristic." [Source: arXiv:2606.21975 abstract (retrieved 2026-06-25)]
