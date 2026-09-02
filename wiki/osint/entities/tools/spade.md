---
title: "SPADE — self-play synthetic environments (MIT Extract)"
type: entity
tags: [tool, poker, rl, k243, mit, extract]
keywords: [spade, Gym, self-play, environment-designer]
related:
  - sources/arxiv-2608.19197-spade-2026-08-20.md
  - concepts/llm-environment-engineer-rl-curriculum.md
  - concepts/poker-arena-multi-axis-cognitive-profile.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-08-20
updated: 2026-08-20
harness_verb: FILE
wire_note: Poker Arena REFERENCE; no decide() retune
---

## Relations

- @sources/arxiv-2608.19197-spade-2026-08-20.md — primary paper
- @concepts/llm-environment-engineer-rl-curriculum.md
- @concepts/poker-arena-multi-axis-cognitive-profile.md — no live-betting loop
- @concepts/cemini-license-posture.md

## Raw Concept

OSINT K243 Phase-0 Extract. Clone `.local/adopts/spade`. https://github.com/spade-rl/spade

## Narrative

| Field | Value |
|-------|--------|
| License | **MIT** [CONFIRMED gh 2026-08-20] |
| Local | `.local/adopts/spade` (~1.4MB) |
| Verdict | **Extract REFERENCE** |
| wire_status | `policy_wired` |

Self-play RL framework: one LLM writes Gym-style environments, another solves them, Designer trained on hint-based regret. Poker Arena **REFERENCE** for synthetic executable curricula. **Do not retune `decide()`** unless a one-line steal already matches Arena briefs. No exploit/jailbreak environments.

## Snippets

> SPADE MIT Extract. Poker Arena REFERENCE. [Source: `.local/reports/license-k243-2026-08-20.md`]
