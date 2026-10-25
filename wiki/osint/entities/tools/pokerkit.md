---
title: PokerKit — Python poker engine (UofT CPRG)
type: entity
tags: [entity, tool, poker, python, k130, adopt]
keywords: [pokerkit, uoftcprg, MIT, devfun-arena, hand-evaluation, NLHE]
related:
  - sources/eval-poker-github-repos-2026-06-26.md
  - entities/platforms/devfun-arena.md
  - concepts/devfun-poker-agent-challenge-2026.md
  - concepts/poker-arena-multi-axis-cognitive-profile.md
  - concepts/wiki-tooling-evaluation.md
  - entities/tools/ai-pokergame.md
  - entities/tools/rlcard.md
  - sources/arxiv-policy-representation-2607.01498-2026-07-07.md
maturity: validated
created: 2026-06-26
updated: 2026-10-25
---

## Relations

- @sources/eval-poker-github-repos-2026-06-26.md — K130 Adopt row (URL 24)
- @entities/platforms/devfun-arena.md — **production dependency** in `agents/devfun-poker-arena`
- @concepts/devfun-poker-agent-challenge-2026.md — Researcher Round sandbox

## Raw Concept

Phase-0 prompted by K130 **Poker GitHub Repository Evaluation.docx** — `uoftcprg/pokerkit`.

## Narrative

**PokerKit** is an MIT-licensed, typed Python poker framework (University of Toronto Computer Poker Research Group). Supports NLHE, Short-Deck, multi-street state, burns, mucks, and showdown ordering.

**Phase-0 (2026-06-26):**

| Check | Result |
|-------|--------|
| License | **MIT** (`gh api`, 471★, pushed 2026-05-22) |
| Arena deployment | **CONFIRMED** — `agents/devfun-poker-arena/pyproject.toml` pins `pokerkit`; selfplay adapter in `examples/selfplay.py` |
| K130 eval claim | Adopt tier **validated** — eval confirms existing stack choice; not a new install |

**Posture:** **Adopt** — canonical engine for dev.fun Arena starter kit. No parallel poker engine evaluation needed unless PokerKit API breaks Arena introspection contract.

## Snippets

> "It supports exceptionally complex game state management—including card burns, hand mucking, chip pulling logic, and exact showdown order." [Source: Poker GitHub Repository Evaluation.docx URL 24 (retrieved 2026-06-26)]

## Dead Ends

- Replacing PokerKit with RLCard for **live Arena `decide()`** — wrong layer; RLCard is offline baseline only (@entities/tools/rlcard.md).
