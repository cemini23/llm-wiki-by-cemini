---
title: RLCard — reinforcement learning toolkit for card games
type: entity
tags: [entity, tool, poker, rl, python, k130, adopt]
keywords: [rlcard, datamllab, MIT, PettingZoo, NFSP, CFR, poker-rl-baselines]
related:
  - sources/eval-poker-github-repos-2026-06-26.md
  - concepts/devfun-poker-agent-challenge-2026.md
  - concepts/poker-arena-multi-axis-cognitive-profile.md
  - concepts/wiki-tooling-evaluation.md
  - entities/tools/pokerkit.md
  - sources/multi-wiki-tool-eval-v7-k92-2026-06-01.md
maturity: draft
created: 2026-06-26
updated: 2026-06-26
---

## Relations

- @sources/eval-poker-github-repos-2026-06-26.md — K130 Adopt row (URL 20)
- @sources/multi-wiki-tool-eval-v7-k92-2026-06-01.md — prior CONDITIONAL-GO → gambling-wiki
- @entities/tools/pokerkit.md — live Arena engine (do not substitute)

## Raw Concept

Phase-0 prompted by K130 **Poker GitHub Repository Evaluation.docx** — `datamllab/rlcard`.

## Narrative

**RLCard** wraps discrete card games (Leduc, Limit Hold'em, Blackjack, …) for RL with PettingZoo-compatible APIs, CFR/NFSP/DQN baselines, and `step_back()` tree traversal [TENTATIVE — single eval source].

**Phase-0 (2026-06-26):**

| Check | Result |
|-------|--------|
| License | **MIT** (`gh api`, 3508★) |
| Hardcoded layout | N/A — RL env library |
| Arena overlap | **Steal offline only** — chart ablation / population bot training outside Arena clock |
| gambling-wiki | Primary domain owner — see `.local/venv-gambling-research` (`wiki/log.md` 2026-06-19) |

**Posture:** **Adopt** for offline poker-RL baselines in isolated venv. **NO** production coupling to cemini-prod or Arena submit path.

## Snippets

> "It implements complex state abstraction, chance sampling CFR, NFSP, and Deep Q-learning right out of the box." [Source: Poker GitHub Repository Evaluation.docx URL 20 (retrieved 2026-06-26)]

## Dead Ends

- Vendor RLCard into `decide()` hot path — latency + env mismatch vs PokerKit Arena table dict.
