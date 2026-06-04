---
title: "NEMO — Execution-Aware Optimization Modeling via Autonomous Coding Agents (arXiv:2601.21372)"
type: source
tags: [source, arxiv, operations-research, autonomous-coding-agents, k98]
keywords: [2601.21372, nemo, optimization, aca, mbr, self-consistency, portfolio, supply-chain]
related:
  - concepts/nemo-execution-aware-optimization-modeling.md
  - sources/arxiv-sandboxed-coding-agents-omni-mod-2606-00579-2026-06-03.md
  - concepts/conductor-orchestrator.md
read_status: skimmed
maturity: draft
created: 2026-06-04
updated: 2026-06-04
---

## Relations

- @concepts/nemo-execution-aware-optimization-modeling.md — synthesis
- @sources/arxiv-sandboxed-coding-agents-omni-mod-2606-00579-2026-06-03.md — shared sandboxed-ACA pattern

## Raw Concept

| Field | Value |
|-------|-------|
| Title | NEMO: Execution-Aware Optimization Modeling via Autonomous Coding Agents |
| Authors | Yang Song et al. |
| arXiv | 2601.21372 (v2 cited in digest) |
| Retrieved | 2026-06-04 |
| Location | `cemini-librarian:/opt/cemini-bulk/research/arxiv-2601.21372-nemo-execution-aware-optimization-modeling-via-a.pdf` |
| read_status | skimmed |

## Narrative

NEMO maps natural-language decision problems to **executable** mathematical optimization code using **autonomous coding agents (ACAs)** in sandboxes — syntactic validity by construction, automated validate-and-repair loops. Novel coordination: **asymmetric validation** between independently generated optimizer vs simulator implementations, external memory for experience reuse, **MBR decoding** and self-consistency for robustness.

Reports SOTA on **8/9** optimization benchmarks with large absolute gains (up to ~28 pp) vs prior specialized LLM pipelines.

**Cemini relevance:** REFERENCE for portfolio/risk **offline** what-if tooling (rebalance, hedge sizing) — not on hot execution path. Complements conductor analyst workflows; any adopt needs Phase-0 on runtime cost and solver licensing [TENTATIVE].

## Snippets

> "NEMO instead treats ACAs as a first-class abstraction analogous to API-based interaction with LLMs; their sandboxed execution guarantees code is executable by construction"

> "asymmetric validation loops between independently generated optimizer and simulator implementations"

[Source: arxiv-2601.21372-nemo-execution-aware-optimization-modeling-via-a.pdf p.1, retrieved 2026-06-04]
