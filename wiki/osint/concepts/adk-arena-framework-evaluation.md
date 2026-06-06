---
title: ADK Arena — agent framework evaluation via LLM-as-a-Developer
type: concept
tags: [concept, agent-harness, evaluation, reference, k101]
keywords: [adk-arena, 2606.05548, llm-as-a-developer, framework-choice, mcp-atlas]
related:
  - sources/arxiv-adk-arena-agent-dev-kits-2606.05548-2026-06-06.md
  - entities/tools/adk-arena.md
  - concepts/mcp-tool-calling-eval-scaffold.md
  - concepts/system-scaling-harness-evaluation.md
  - concepts/conductor-orchestrator.md
  - concepts/wiki-tooling-evaluation.md
  - "@ccc-wiki/concepts/adk-arena-agent-framework-benchmark.md"
maturity: validated
created: 2026-06-06
updated: 2026-06-06
cross-wiki-source: "@ccc-wiki/concepts/adk-arena-agent-framework-benchmark.md"
---

## Relations

- @sources/arxiv-adk-arena-agent-dev-kits-2606.05548-2026-06-06.md — Microsoft / Ohio State paper
- @ccc-wiki/concepts/adk-arena-agent-framework-benchmark.md — CCC harness-primary
- @concepts/mcp-tool-calling-eval-scaffold.md — MCP-Atlas named in ADK Arena adapter set

## Narrative

**REFERENCE** [CONFIRMED — empirical study] — first ecosystem-scale comparison of **51 Python Agent Development Kits** using **LLM-as-a-Developer**: one coding agent learns each framework's API, ships runnable agents, and is scored on SWE-bench / τ²-bench / Terminal-Bench / **MCP-Atlas**.

**Implications for Cemini:**

| Claim | Action |
|-------|--------|
| Framework choice ≈ model choice for agent outcomes | Justifies harness investment (Cursor skills, lazy-tool, conductor) over raw frontier model swaps |
| Median framework ~32% vs best ~80% | Phase-0 audits before adopting parallel ADK stacks — see `@concepts/wiki-tooling-evaluation.md` |
| Docs/source/params substitutable (28–40% usage band) | Skills + wiki schema may compensate for thin MCP docs — but not a license to skip `inspect_capability` |
| MCP-Atlas in benchmark suite | Extend MAVEN smoke matrix with MCP-native tasks |

**Phase-0 entity (2026-06-06):** `@entities/tools/adk-arena.md` — **NO-GO adopt** (Docker ~50GB, 1★ repo, cannot eval lazy-tool/conductor). **Steal-from:** MCP-Atlas GTFA, token proxy, 3-level codegen feedback.

**Verdict:** evaluation discipline + CCC cross-link — **no** local replication of 204-pair shootout on laptop.

## Snippets

> "Generation succeeds for 57% of runs, and its cost varies 5.6× across frameworks ($0.6 to $3.4 per agent), a quantitative proxy for API complexity."

> — [Source: arxiv-2606.05548-adk-arena-evaluating-agent-development-kits-via.pdf abstract, retrieved 2026-06-06]
