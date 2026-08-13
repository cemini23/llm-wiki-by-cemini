---
title: "LLM Tutor Answer-Withholding — Supervisor Architecture + Evidence-Driven Tuning"
type: source
tags: [arxiv, k235, tutoring, socratic, guardrails, ccc, education]
keywords: [2608.12292, withhold-answer, supervisor, help-ladder, socratic, guardrail, evaluation]
related:
  - concepts/socratic-answer-withholding-contract.md
  - concepts/agent-harness-verification-bottleneck.md
maturity: draft
created: 2026-08-13
updated: 2026-08-13
read_status: skimmed
---

## Relations

- @concepts/socratic-answer-withholding-contract.md — synthesized pattern page
- @concepts/agent-harness-verification-bottleneck.md — same family: enforced contracts over model prompts

## Raw Concept

| Field | Value |
|-------|--------|
| arXiv | 2608.12292 (2026-08-12) |
| Authors | Pisan (UW Bothell) |
| sha256 | `942eecb3e641d1f0b11ecac2469dd15c963c1efcae473843d6d6a35f5e93b368` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.12292-teaching-a-large-language-model-tutor-to-withhol.pdf` |
| retrieved | 2026-08-13 |

## Narrative

Motivation: a randomized study showed students using an unguarded chatbot scored higher while practicing but **lower on a later test** — a Socratic guarded version kept the practice gain and removed the later loss. A capable model pressed by a frustrated student does not withhold reliably on prompt alone.

Deployed architecture: **non-LLM policy core** reads trusted learner state and sets a per-turn ceiling on an **eight-rung help ladder**; a deterministic detector strips solution code; a separate LLM judge checks each risky reply against the contract. Tuning uses **no human subjects** — scripted student personas driven through the live pipeline and re-scored by a stronger model; every rejection's stated reason is recorded so failures are fixed by cause. This surfaced an interpretable "over-help ladder" (blatant solution leaks → naming the exact bug → over-citing general facts), each fix exposing the next. Final: full compliance on all four acceptance criteria.

The **measure–diagnose–fix loop is the transferable recipe**: any LLM agent that must refuse a capability it has (not just tutors — guardrail enforcement generally). Routing: CCC + Atto education-adjacent watch (no product install).

[Source: arXiv:2608.12292]

## Snippets

> "We offer the measure, diagnose, and fix loop as a reusable recipe for any LLM agent that must refuse a capability it has." [Source: arXiv:2608.12292 p.1]
