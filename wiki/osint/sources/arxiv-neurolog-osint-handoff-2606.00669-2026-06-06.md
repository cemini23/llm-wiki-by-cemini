---
title: NeuroLog — OSINT handoff stub (arXiv 2606.00669)
type: source
tags: [source, arxiv, cross-wiki-handoff, neuro-symbolic, k101]
keywords: [2606.00669, neurolog, cybersec-handoff, compile-free, vuln-discovery]
related:
  - "@cybersecurity-wiki/sources/arxiv-neurolog-auditable-vuln-discovery-2606.00669-2026-06-05.md"
  - "@cybersecurity-wiki/concepts/neuro-symbolic-auditable-reasoning.md"
  - concepts/cemini-wiki-ingest-workflow.md
maturity: draft
read_status: unread-stub
created: 2026-06-06
updated: 2026-06-06
---

## Relations

- @cybersecurity-wiki/sources/arxiv-neurolog-auditable-vuln-discovery-2606.00669-2026-06-05.md — **canonical** methodology + evaluation (K100 cybersec ingest)
- @cybersecurity-wiki/concepts/neuro-symbolic-auditable-reasoning.md — auditable derivation-tree pattern
- @concepts/cemini-wiki-ingest-workflow.md — cross-wiki handoff pattern (K101)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | NeuroLog: Reasoning You Can Audit — Neuro-Symbolic Vulnerability Discovery via LLM Facts, Datalog, and SMT |
| **Author** | Sanjay Rawat |
| **arXiv** | 2606.00669 |
| **Location** | `cemini-librarian:/opt/cemini-bulk/research/arxiv-2606.00669-neurolog-reasoning-you-can-audit-neuro-symbolic.pdf` |
| **Retrieved** | 2026-06-06 |
| **Read status** | unread-stub — deep-read lives on cybersec-wiki |

K100 routed vuln-discovery methodology to cybersec; K101 completes librarian move from OSINT inbox.

## Narrative

OSINT keeps this **pointer stub** only. Financial-quant routing does not apply — no CeminiSuite prod touchpoint.

Cybersec owns: LLM fact extraction → Soufflé Datalog → Z3 feasibility → ASan crash synthesis; compile-free opportunistic audits on C/C++ libraries.

## Snippets

> "What is new in NeuroLog is that the fact base comes from a language model rather than a compiler, that the whole pipeline runs without building the target, and that the SAT model is an artifact — input to crash synthesis — rather than a yes/no verdict."

> — [Source: arxiv-2606.00669-neurolog-reasoning-you-can-audit-neuro-symbolic.pdf abstract, retrieved 2026-06-06]
