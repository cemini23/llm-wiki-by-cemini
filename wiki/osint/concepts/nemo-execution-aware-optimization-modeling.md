---
title: NEMO — execution-aware optimization via sandboxed coding agents
type: concept
tags: [concept, operations-research, autonomous-agents, k98]
keywords: [nemo, optimization, aca, mbr, validate-repair, portfolio-rebalance]
related:
  - sources/arxiv-nemo-execution-aware-optimization-2601-21372-2026-06-04.md
  - concepts/conductor-orchestrator.md
  - sources/arxiv-sandboxed-coding-agents-omni-mod-2606-00579-2026-06-03.md
maturity: draft
created: 2026-06-04
updated: 2026-06-04
---

## Relations

- @sources/arxiv-nemo-execution-aware-optimization-2601-21372-2026-06-04.md — anchor paper

## Raw Concept

Synthesis of arXiv:2601.21372 for offline decision modeling, not live trading execution.

## Narrative

**Problem:** NL → optimization code pipelines break on non-executable outputs and brittle single-shot LLM codegen.

**NEMO pattern:** Treat **autonomous coding agents** like APIs — sandbox execute, validate, asymmetric cross-check (optimizer vs simulator), memory + MBR/self-consistency.

**Cemini use cases (REFERENCE):** portfolio rebalance what-if, hedge notionals, constraint feasibility checks in brief prep — route through conductor with human gate; **no** auto-deploy to prod solvers without license audit [NEEDS VERIFICATION 2026-06-04].

## Snippets

> "sandboxed execution guarantees code is executable by construction"

[Source: arxiv-2601.21372-nemo-execution-aware-optimization-modeling-via-a.pdf p.1, retrieved 2026-06-04]
