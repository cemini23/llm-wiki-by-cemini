---
title: Agentic Legacy-Code Modernization (verification-oracle pattern)
type: concept
tags: [concept, agentic-workflow, legacy-code, verification, ccc, k235]
keywords: [modernization, Fortran, oracle, bit-for-bit, human-gates, escaped-defect]
related:
  - sources/arxiv-2608.12249-hpc-modernization-agentic-2026-08-13.md
  - sources/arxiv-2608.14527-fault-injection-llm-modernization-2026-08-17.md
  - concepts/agent-harness-verification-bottleneck.md
  - concepts/agent-toolkit-routing-research-backlog.md
  - sources/arxiv-2608.16112-strategic-technical-debt-2026-08-18.md
maturity: draft
created: 2026-08-13
updated: 2026-08-17
---

## Relations

- @sources/arxiv-2608.12249-hpc-modernization-agentic-2026-08-13.md
- @sources/arxiv-2608.14527-fault-injection-llm-modernization-2026-08-17.md — K240 / CCC K284 stub; off-nominal paired FI; no ftinj clone
- @concepts/agent-harness-verification-bottleneck.md — same thesis from the K234 Charity Majors lane
- @concepts/agent-toolkit-routing-research-backlog.md — K235 backlog bump

## Raw Concept

What this page answers: what does a production-scale agentic legacy-code conversion actually require to be safe, and where does delegation break? Synthesized from the GAMESS F77→F2008 case study (2608.12249).

## Narrative

The GAMESS case establishes a reusable structure for delegating large mechanical code transformations to agents:

1. **Agents author the spec, humans hold the gates** — three prompt-specialized roles operate under a version-controlled specification the agents wrote and revised; humans gate a small number of decision points.
2. **The verification oracle is inherited from the domain, not invented by the harness** — chemistry output compared bit-for-bit against golden references (12th-decimal sensitivity). The oracle is exact *because* the domain already demanded it; nothing extra had to be built.
3. **The boundary of safe delegation = exactly where the oracle stops seeing.** The escaped defect proves the point: an agent faithfully reproduced a `DOUBLE PRECISION` declaration that always contradicted the code's bit-packing semantics. It compiled, satisfied every style-guide clause, and was locally accurate — and wrong. Only the bit-for-bit oracle caught it. No prompt, compiler flag, or style check would have.
4. **Scale properties**: 56k lines, 12 files, ~37 min/file validation; time scales with file count, not file size; 11/12 first-pass correct; aggregate line count flat (-0.94%) — evidence against LLM padding/compression failure modes.

Transferable to this workspace: any agentic rewrite lane (transpiler tests, wiki migrations, `/route` execute stages) should define its **oracle first** and refuse delegation beyond its visibility. Complements the harness-verification bottleneck thesis: cheap post-generation verification is worth more than a smarter generator.

## Snippets

> "The boundary of safe delegation lies exactly where that oracle stops seeing." [Source: arXiv:2608.12249 p.1]

## Dead Ends

- Compiler-level defense alone: `-std=f2008` strictness caught two defect classes (rank-1 dummy args, Hollerith literals) but could not catch the semantic alias bug — tightening the language standard is a cheap first line, not a substitute for the oracle.
