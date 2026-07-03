---
title: SWE-INTERACT user-driven coding eval (K141)
type: concept
tags: [concept, agent-harness, swe-bench, ccc, poker, k141, reference-only]
keywords: [multi-turn, user simulator, goal discovery, vague prompt, workspace inspection, Scale AI]
related:
  - sources/arxiv-2606.30573-swe-interact-2026-07-03.md
  - entities/tools/swe-interact.md
  - concepts/devfun-researcher-track-readiness-2026-06.md
  - sources/arxiv-toolbench-x-tool-unreliability-2606.25819-2026-06-26.md
maturity: draft
created: 2026-07-03
updated: 2026-07-03
---

## Relations

- @sources/arxiv-2606.30573-swe-interact-2026-07-03.md — Scale AI (2606.30573)
- @concepts/devfun-researcher-track-readiness-2026-06.md — Researcher Round eval posture

## Raw Concept

What prompted this page: K141 arXiv **2606.30573** — orthogonal eval axis for coding agents: **interactive goal discovery** vs one-shot fully-specified SWE tasks.

## Narrative

### Workflow under test

`GOAL-DISCOVERY → PLAN → APPROVAL → IMPLEMENT → REVISE → SUBMIT` with user simulator that:

- Starts with **vague** instructions
- **Inspects workspace** (shell, git, files)
- Reveals requirements progressively

### Transfer gap

~50% single-turn → ~25% multi-turn on matched tasks. Tests memory, rework discipline, ambiguity tolerance — not raw codegen.

### Cemini mapping

| Consumer | Steal |
|----------|-------|
| **Poker Arena** | Partial-spec bundle scenarios; rubric reveal mid-trajectory |
| **CCC harness** | Multi-turn Cursor/Claude Code regression with user-sim |

Briefs: `agents/devfun-poker-arena/briefs/2026-07-03_k141-swe-interact-multiturn-steal.md`, `briefs/ccc-2026-07-03_k141-swe-interact-harness-steal.md`

**Shipped 2026-07-03 (poker arena):** `sandbox_partial_spec_eval.py` + `researcher_rubric_reveal_v1` scenario in tri-verifier harness.

## Snippets

> "Tests whether agents can discover user intent, adapt to evolving requirements, and preserve correctness across turns." [Source: arxiv-2606.30573 §1 (retrieved 2026-07-03)]
