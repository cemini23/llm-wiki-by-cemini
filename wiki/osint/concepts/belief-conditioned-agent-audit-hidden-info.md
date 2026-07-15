---
title: Belief-conditioned agent audit for hidden-information games
type: concept
tags: [concept, poker, llm-agents, audit, hidden-information, k167]
keywords: [external belief, belief-action deviation, information isolation, offline improvement]
related:
  - sources/arxiv-2607.10814-belief-conditioned-llm-agents-werewolf-audit-2026-07-15.md
  - concepts/hierarchical-bounded-agent-memory.md
  - concepts/generator-verifier-inference-time-steering.md
maturity: draft
created: 2026-07-15
updated: 2026-07-15
---

## Relations

- @sources/arxiv-2607.10814-belief-conditioned-llm-agents-werewolf-audit-2026-07-15.md — K167 deep-read

## Raw Concept

How to evaluate LLM agents in high-variance imperfect-information games without trusting win rate alone.

## Narrative

**Pattern (Werewolf / poker-transfer):**

1. **Information isolation** — engine holds truth; agents see only legal public+private context.
2. **External belief layer** — role/hand probabilities as shadow baseline or optional context injection.
3. **Belief–action deviation log** — classify harmful vs justified vs strategic overrides (consistency may be low).
4. **Defensive offline loop** — aggregate batch bad cases → human-reviewed strategy versioning; refuse single-trajectory online rewrites.

Use for Poker Arena HL/analyze: log decide() vs HUD/belief recommendation; improve handbook offline.
