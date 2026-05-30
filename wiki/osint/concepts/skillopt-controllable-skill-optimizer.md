---
title: SkillOpt — controllable text-space skill optimizer
type: concept
tags: [concept, agent-skills, skill-training, validation-gated, k84]
keywords: [skillopt, add-delete-replace, held-out-validation, rejected-edit-buffer, learning-rate-budget]
related:
  - sources/skillopt-executive-strategy-self-evolving-agent-skills-2026-05-30.md
  - sources/agentic-harness-engineering.md
  - concepts/sia-unified-harness-weight-self-improvement.md
maturity: draft
created: 2026-05-30
updated: 2026-05-30
---

## Relations

- @sources/skillopt-executive-strategy-self-evolving-agent-skills-2026-05-30.md — primary source (arXiv:2605.23904)

## Raw Concept

SkillOpt (Microsoft, May 2026) treats an agent **skill document** as trainable external state with a frozen executor model. A separate optimizer proposes bounded edits; acceptance requires **strict improvement on held-out validation** — analogous to weight-space SGD but in text.

## Narrative

**Steal-for-CCC:** validation-gated skill edits + rejected-edit buffer map cleanly onto `scripts/skill_audit.py` and Cursor skill packs. **Not prod trading.**

Potential pilot: evolve one high-churn skill (e.g. brief-audit checklist) with scored rollouts from `skill_audit.py` verdict history.

## Snippets

> "An edit is accepted only when it strictly improves a held-out validation score." [Source: 2605.23904v2.pdf via skillopt source page]
