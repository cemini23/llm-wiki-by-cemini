---
title: Scientific conclusion synthesis eval — SciConBench clean-room pattern
type: concept
tags: [concept, agent-eval, research-quality, benchmark]
keywords: [SciConBench, SciConHarness, clean-room, Cochrane, synthesis F1]
related:
  - sources/arxiv-2606-11337-sciconbench-scientific-synthesis-agents-2026-06-13.md
  - entities/benchmarks/sciconbench.md
  - concepts/cemini-wiki-ingest-workflow.md
  - concepts/llm-agent-systems.md
  - "@cybersecurity-wiki/sources/arxiv-2606-07992-vats-error-path-mcp-injection-2026-06-13.md"
maturity: draft
created: 2026-06-13
updated: 2026-06-13
---

## Relations

- @sources/arxiv-2606-11337-sciconbench-scientific-synthesis-agents-2026-06-13.md
- @entities/benchmarks/sciconbench.md
- @concepts/cemini-wiki-ingest-workflow.md
- @cybersecurity-wiki/sources/arxiv-2606-07992-vats-error-path-mcp-injection-2026-06-13.md — complementary MCP trust failure mode

## Raw Concept

K114 arXiv 2606.11337 — eval methodology for whether agents can synthesize scientific conclusions without training-set leakage.

## Narrative

### Problem

Deep-research agents can appear competent when evals allow access to canonical review corpora used as labels. **SCICONHARNESS** enforces MCP clean-room: block Cochrane ground-truth artifacts during agent runs.

### Headline result `[TENTATIVE — skimmed source]`

Even strongest tested agent reaches modest F1 (~0.34 clean-room). Unconstrained setups overstate capability by double-digit F1 points — supports Cemini **Tier 3 NO-GO** on autonomous wiki synthesis without human gates.

### Steal-from for Cemini

1. **Clean-room eval** before promoting agent-generated briefs to prod
2. **Atomic-fact decomposition** for ingest QA (claim-level precision/recall)
3. **Monthly benchmark refresh** model for wiki gap / digest quality regression

**Verdict:** REFERENCE — run periodic spot-checks on conductor/librarian synthesis; no SciConBench install on prod without operator GO.

## Snippets

> "Unconstrained eval inflates scores by 0.02–0.172."
> — [Source: arxiv-2606-11337-sciconbench-scientific-synthesis-agents-2026-06-13.md]
