---
title: "SkillOpt — Executive Strategy for Self-Evolving Agent Skills (arXiv:2605.23904)"
type: source
tags: [source, arxiv, agent-skills, skill-optimization, microsoft, k84]
keywords: [skillopt, text-space-optimizer, validation-gated-edits, learning-rate-budget, rejected-edit-buffer]
related:
  - concepts/skillopt-controllable-skill-optimizer.md
  - concepts/high-signal-paper-patterns.md
  - sources/agentic-harness-engineering.md
  - concepts/conductor-orchestrator.md
maturity: draft
read_status: read
created: 2026-05-30
updated: 2026-05-30
---

## Relations

- @concepts/skillopt-controllable-skill-optimizer.md — synthesized method page
- @sources/agentic-harness-engineering.md — complementary harness evolution line (AHE)
- @concepts/conductor-orchestrator.md — skills as external state vs frozen analyst nodes

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | SkillOpt: Executive Strategy for Self-Evolving Agent Skills |
| **Author** | Yang et al. (Microsoft + SJTU/Tongji/Fudan) |
| **Type** | arXiv preprint |
| **Location** | `cemini-librarian:/opt/cemini-bulk/research/2605.23904v2.pdf` |
| **arXiv** | 2605.23904 |
| **Retrieved** | 2026-05-30 |
| **Pages** | 27 |
| **Read status** | read (abstract + intro) |

## Narrative

Proposes **SkillOpt** — a separate optimizer model that treats agent **skills as trainable external state** (single markdown document) while the base agent stays frozen. Rollouts are scored; the optimizer proposes bounded **add/delete/replace** edits; an edit is accepted only if a **held-out validation score strictly improves**.

Mechanisms aimed at stability: textual learning-rate budget, rejected-edit buffer, epoch-wise slow/meta updates. Positions against hand-crafted skills, one-shot generation, and uncontrolled self-revision loops.

**Cemini relevance:** directly applicable to `@ccc-wiki` skill packs and OSINT `scripts/skill_audit.py` evolution — validation-gated skill edits mirror our brief-audit discipline. Not a prod trading dependency.

## Snippets

> "A textual learning-rate budget, rejected-edit buffer, and epoch-wise slow/meta update make skill training stable while adding zero inference-time model calls." [Source: 2605.23904v2.pdf p.1]
