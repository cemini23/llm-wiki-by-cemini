---
title: ToolBench-X tool-environment reliability hazards
type: concept
tags: [concept, tool-use, harness, benchmark, k131]
keywords: [ToolBench-X, specification-drift, tool-unreliability, agent-recovery]
related:
  - sources/arxiv-toolbench-x-tool-unreliability-2606.25819-2026-06-26.md
  - entities/tools/toolbench-x.md
  - concepts/code-as-agent-harness.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/llm-agent-systems.md
maturity: draft
created: 2026-06-26
updated: 2026-10-25
---

## Relations

- @sources/arxiv-toolbench-x-tool-unreliability-2606.25819-2026-06-26.md — K131 primary
- @entities/tools/toolbench-x.md — benchmark repo (REFERENCE-only)
- @concepts/code-as-agent-harness.md — harness should inject hazards, not assume clean MCP

## Raw Concept

K131 synthesis of arXiv **2606.25819**. Standard tool-use benchmarks assume stable schemas and honest tool outputs. **ToolBench-X** scores agents on **recoverable** failures across five hazard classes.

## Narrative

### Five hazard types

| Hazard | Agent recovery |
|--------|----------------|
| Specification Drift | Re-fetch tool schema / docs |
| Invocation Error | Fix args and retry |
| Execution Failure | Alternate tool or backoff retry |
| Output Drift | Validate output against expected invariants |
| Cross-source Conflict | Cross-check third source or canonical answer |

### Cemini harness steal

Apply to **lazy-tool / conductor** integration tests: inject transient MCP failures, stale capability catalog, and conflicting prod-mcp vs fetch responses — agent (or harness wrapper) must retry/recover. Paper benchmark is REFERENCE-only; repo has **NO LICENSE** (`gh api` 2026-06-26).

Brief: `briefs/ccc-2026-06-26_k131-toolbench-x-hazard-recovery.md`

## Snippets

> "each injected instance remains solvable through at least one valid recovery path" [Source: arxiv-2606.25819 abstract (retrieved 2026-06-26)]
