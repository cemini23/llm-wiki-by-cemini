---
title: "CLEO — optimize the harness, not the model: a minimal agent on a self-hostable LLM"
type: source
tags: [source, arxiv, agent-harness, self-hosted, security, minimalism]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-03
updated: 2026-11-03
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Optimize the Harness, Not the Model: Fitting a Minimal Agent to a Self-Hostable LLM for Investigative Analysis |
| Authors | Shai Nahum Gefen, Vered Chassida, Dmitry Bas (Dream Security, Tel Aviv) |
| arXiv | 2611.03434 |
| Pages | 3 |
| Read status | skimmed (abstract) |

## Narrative

**This is the most directly useful paper in the batch for this workspace**, and it is three pages long.

The setting: government intelligence teams need agents over large, messy evidence collections, but security and cost rule out hosted frontier models and broad tool surfaces that cannot be audited.

**CLEO** — Constrained Loop for Environment Optimization. Given an expert-validated dataset, it admits **only** the tools, guardrails, memory policies, and loop components that improve accuracy **while remaining general and auditable**. Everything else is excluded by construction.

The result: **83.8% pass rate on a held-out set**, within **1.2 points** of the strongest out-of-the-box Claude Code SDK baseline, while being **two orders of magnitude smaller**.

### Why the result matters more than the number

The interesting claim is not 83.8%. It is that **a harness two orders of magnitude smaller loses 1.2 points**. Most of what a large default harness contains is not contributing accuracy — it is surface area, and surface area is what an auditor has to review and an attacker gets to use.

That reframes harness design from "add capability until the score stops rising" to "admit a component only if it earns its place on both accuracy and auditability".

### The two admission criteria are the contribution

1. **Improves accuracy** on expert-validated data. Measurable.
2. **Remains general and auditable.** Not a special case, not an opaque blob.

The second criterion is what most harness tuning omits, and it is the one that matters for anything handling sensitive input.

### Fit here

- Directly relevant to the `design-log`-style frozen-objective discipline already in use.
- Relevant to any local-first project that cannot send data to a hosted frontier model.

**Caveat.** Three pages, abstract only. The dataset is expert-validated and unpublished; the 1.2-point gap is on their task, not on this workspace's.

## Snippets

> "CLEO admits only the tools, guardrails, memory policies, and loop components that improve accuracy while remaining general and auditable." [Source: arxiv-2611.03434 p.1]

> "The CLEO harness reaches an 83.8% pass rate, within 1.2 points of the strongest out-of-the-box Claude Code SDK baseline, while being two orders of magnitude smaller." [Source: arxiv-2611.03434 p.1]

## Dead Ends

- **Assuming 83.8% transfers.** Their task, their dataset.
