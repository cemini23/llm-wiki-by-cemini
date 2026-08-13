---
title: Socratic Answer-Withholding as a Machine-Checkable Contract
type: concept
tags: [concept, guardrails, tutoring, socratic, ccc, k235]
keywords: [withhold-answer, help-ladder, policy-core, detector, measure-diagnose-fix]
related:
  - sources/arxiv-2608.12292-tutor-withhold-answer-2026-08-13.md
  - concepts/agent-harness-verification-bottleneck.md
  - concepts/agent-toolkit-routing-research-backlog.md
maturity: draft
created: 2026-08-13
updated: 2026-08-13
---

## Relations

- @sources/arxiv-2608.12292-tutor-withhold-answer-2026-08-13.md
- @concepts/agent-harness-verification-bottleneck.md — enforced contracts beat prompt-only behavior, again
- @concepts/agent-toolkit-routing-research-backlog.md — K235 backlog bump

## Raw Concept

What this page answers: how do you make an LLM reliably *not* use a capability it has? Synthesized from 2608.12292 (UW Bothell tutor).

## Narrative

The core problem generalizes far beyond tutoring: **a capable model pressed by a frustrated user does not withhold reliably on a prompt alone** — and the randomized-study stakes are real (unguarded chatbot: practice gain, later test loss; Socratic guard: gain kept, loss removed).

The architecture that works is a **per-turn, machine-checkable contract** layered outside the model:

1. **Non-LLM policy core** reads only trusted learner state and sets a per-turn ceiling on an eight-rung help ladder — the constraint comes from code, not prompting.
2. **Deterministic detector** strips solution code before it reaches the student.
3. **Separate LLM judge** audits each risky reply against the contract (model-as-verifier, not model-as-policy).

The tuning loop is the transferable recipe: **measure–diagnose–fix without human subjects** — scripted student personas driven through the live pipeline, re-scored by a stronger model, every rejection's stated reason recorded so failures are fixed *by cause*. That loop surfaced an interpretable "over-help ladder" (blatant leaks → naming the exact bug → over-citing general facts), each fix exposing the next, until full compliance on all four acceptance criteria.

Transferable to CCC: any agent that must refuse a capability it has — guardrail enforcement, scope refusal in /route, answer-suppression in eval harnesses. Structure: policy core (deterministic) + detector (deterministic) + judge (LLM) + persona-driven evals.

## Snippets

> "We offer the measure, diagnose, and fix loop as a reusable recipe for any LLM agent that must refuse a capability it has." [Source: arXiv:2608.12292 p.1]
