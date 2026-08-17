---
title: "Differential fault injection for LLM modernization (arXiv 2608.14527) — OSINT stub"
type: source
tags: [arxiv, stub, k240, ccc-k284, dual-id]
keywords: [fault-injection, ftinj, GAMESS, off-nominal, modernization]
related:
  - sources/arxiv-2608.14380-agentrewind-2026-08-17.md
  - sources/arxiv-2608.14490-twin-2026-08-17.md
  - concepts/agentic-legacy-code-modernization.md
maturity: draft
created: 2026-08-17
updated: 2026-08-17
read_status: read
---

## Relations

- Canon: CCC **K284** (same PDF). OSINT does not duplicate the CCC page. **No ftinj clone.**
- @sources/arxiv-2608.14380-agentrewind-2026-08-17.md — CCC K282 stub
- @sources/arxiv-2608.14490-twin-2026-08-17.md — CCC K283 stub
- @concepts/agentic-legacy-code-modernization.md — K235 HPC oracle-bound sibling

## Raw Concept

| Field | Value |
|-------|--------|
| Paper | arXiv:2608.14527, validating LLM-modernized scientific software via differential fault injection |
| File | `arxiv-2608.14527-validating-llm-modernized-scientific-software-th.pdf` |
| sha256 | `6f353fe48d425904889f2321d51b66748b436a62980e94211c64defe5217039c` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.14527-validating-llm-modernized-scientific-software-th.pdf` |
| Dual-ID | **OSINT K240** stub. **CCC K284** = canon. **CCC K240** = robotics solver (old). Policy only. |

## Narrative

OSINT stub. Policy only — no public `ftinj` SPDX, no clone.

**Steal:** a passing nominal test suite does not exercise fault/perturbation/precision response. LLM code modernization needs paired differential fault injection at shared driver sites (same fault → same classification/iteration/energy). Match harness + compilation config (`-O1` vs `-O2` can fake a one-iteration skew). Off-nominal fidelity ≠ absolute resilience.

## Snippets

> Canon: CCC K284. No ftinj clone this batch. [Source: `.local/reports/license-k240-2026-08-17.md`]
