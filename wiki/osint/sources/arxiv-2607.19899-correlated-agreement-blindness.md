---
title: "arXiv 2607.19899 — Correlated agreement blindness in multi-agent triage"
type: source
tags: [source, arxiv, multi-agent, harness, poker, ccc, k191]
keywords: [ARAT, disagreement, correlated failure, UNSW-NB15]
related:
  - concepts/code-as-agent-harness.md
  - concepts/agent-reactive-bugs.md
maturity: draft
read_status: read
created: 2026-07-23
updated: 2026-07-23
clusters: [k191-ingest]
---

## Relations

- @concepts/code-as-agent-harness.md
- @concepts/agent-reactive-bugs.md

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | 2607.19899 |
| **sha256** | `c47b9f73a8d0c75c6465850aa005da3142883ebac6a7bd5e05c23f6c215bc1e5` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2607.19899-harnessing-disagreement-detecting-correlated-agr.pdf` |

## Narrative

**Correlated agreement blindness:** as base agents improve they agree more, so disagreement-triggered escalation misses shared failure modes. ARAT (RF + k-NN + meta) reduces under-prediction vs soft voting on UNSW-NB15. **CCC/poker steal:** do not treat multi-agent consensus as safety; diversify for *productive disagreement*; keep conservative override / safety-flag gates on decide() / submit paths.
