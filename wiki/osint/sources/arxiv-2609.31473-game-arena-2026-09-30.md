---
title: "Game Arena: strategic LLM evaluation in competitive environments (2609.31473)"
type: source
tags: [source, k276, agents, evaluation, games]
keywords: [k276, game-arena, kaggle, werewolf, FILE]
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

| File | `arxiv-2609.31473-game-arena-strategic-llm-evaluation-in-competiti.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2609.31473-game-arena-strategic-llm-evaluation-in-competiti.pdf` |
| Archive | egress-fi 2026-09-30 |
| Retrieved | 2026-09-30 |
| Dual-ID | **OSINT K276** |
| sha256 | `38aecfb8317abc3477fb7249a96e6fecf800c1be6e096f5184aeb72caca12547` |
| arXiv | 2609.31473 |
| Authors | Bovard Doerschuk-Tiberi, Yao Yan, Justin Chiu, Hann Wang, Timothy Chung, and others (Kaggle; Google DeepMind) |
| Repo | `https://github.com/google-deepmind/game_arena` |
| Project page | `https://www.kaggle.com/game-arena` |

## Narrative

Kaggle Game Arena evaluates language models by head-to-head play instead of static tests. The stated reason: fixed test sets saturate, and they leak into training corpora. Game play gets harder as models improve, so the benchmark does not saturate.

Three pilot environments: Chess, Poker, and Werewolf. Those cover perfect information, imperfect information, and multiplayer settings. Ten frontier models played full round-robins.

The harness is a shared text protocol. A model gets a natural-language state and history, and returns one action. Reported scale: 40 games per Chess pair, 20,000 hands per Poker pair with duplicate-hands mirroring, and about 31,500 Werewolf games.

Two reported results are worth keeping. Model strength is not consistent across games, so one arena rank does not transfer. And the authors argue for outcome metrics over subjective human or LLM judges.

The authors admit fixed game counts per pair are not compute-efficient, model churn breaks long-run comparison, and there is no cross-game rating.

Relevance: this is an evaluation-harness pattern, not a product. The useful idea is that a competitive environment resists saturation and contamination better than a fixed test set.

Repo SPDX is Apache-2.0, 8,494 KB, 116 stars (gh api 2026-09-30). Poker as a product is retired in this workspace. No clone. FILE only.
