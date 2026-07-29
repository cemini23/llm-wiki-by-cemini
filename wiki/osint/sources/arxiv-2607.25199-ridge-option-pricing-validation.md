---
title: "arXiv 2607.25199 — RIDGE: LLM option-pricing validation loop"
type: source
tags: [source, arxiv, options, xsp, validation, k206]
keywords: [RIDGE, Heston, Bates, rough Heston, CCF-PDE, LLM codegen, no-arbitrage]
related:
  - concepts/xsp-lane-trading-framework.md
  - concepts/wiki-tooling-evaluation.md
maturity: draft
created: 2026-07-29
updated: 2026-07-29
read_status: deep-read
---

## Relations

- @concepts/xsp-lane-trading-framework.md — SV option numerics / validation culture (not a trade signal)
- @concepts/wiki-tooling-evaluation.md — validation-as-method parallel

## Raw Concept

| Field | Value |
|-------|--------|
| Title | RIDGE: An Autonomous Framework for Validation and Method Discovery in LLM-Generated Option Pricing |
| Authors | Cheng / Liu / Oosterlee |
| arXiv | 2607.25199 |
| Filename | `arxiv-2607.25199-ridge-an-autonomous-framework-for-validation-and.pdf` |
| sha256 | `6e86e49b4b90543236e9f42329713f2090235706d97891d68c6a8faeca62a372` |
| Retrieved | 2026-07-29 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2607.25199-ridge-an-autonomous-framework-for-validation-and.pdf` |
| Repo | https://github.com/ShQiangLiu/ridge — **404 as of 2026-07-29**; Phase-0 deferred |

## Narrative

RIDGE (Repository-driven Iterative Diagnosis, Generation and Evaluation) validates LLM-generated option pricers with no-arbitrage, stress, benchmark, and consistency checks; diagnostic knowledge accumulates in a reusable repository. Applied to Heston, Bates, rough Heston, Heston–Hull–White, and G-SVJD. Dominant failures are numerical adaptivity and method/model mismatch — not typos. For HHW/G-SVJD, persistent MC failures drove a switch to conditional characteristic-function PDEs (CCF-PDE). Scores rise sharply with iteration (e.g. Heston 31→97/100).

**Route:** wiki + XSP validation culture only — not a Robinhood lane signal. Repo Phase-0 when public.

## Snippets

> Dominant failures are numerical adaptivity + method/model mismatch — not coding typos.

[Source: arXiv:2607.25199]
