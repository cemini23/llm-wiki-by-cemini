---
title: System-scaling harness evaluation dimensions
type: concept
tags: [concept, agent-harness, evaluation, steal-from, k94]
keywords: [system-scaling, harness-metrics, verification, orchestration, 2605.26112]
related:
  - "@ccc-wiki/concepts/system-scaling-harness-agentic-ai.md"
  - "@ccc-wiki/sources/arxiv-system-scaling-harness-2605.26112.md"
  - concepts/tool-evaluation-framework.md
  - concepts/sia-unified-harness-weight-self-improvement.md
  - entities/tools/world-cup-bot.md
  - concepts/agents-last-exam-benchmark.md
  - concepts/adk-arena-framework-evaluation.md
  - sources/arxiv-agents-last-exam-2606.05405-2026-06-06.md
  - sources/arxiv-adk-arena-agent-dev-kits-2606.05548-2026-06-06.md
  - entities/tools/adk-arena.md
maturity: draft
created: 2026-06-02
updated: 2026-06-06
cross-wiki-source: "@ccc-wiki/concepts/system-scaling-harness-agentic-ai.md"
---

## Relations

- @ccc-wiki/concepts/system-scaling-harness-agentic-ai.md — CCC checklist (2605.26112)
- @concepts/tool-evaluation-framework.md — multi-wiki eval prompts
- @entities/tools/world-cup-bot.md — completion / verification gates

## Narrative

**Steal-from** arXiv 2605.26112 — progress in agentic AI requires **system scaling**: measure memory, retrieval, tools, orchestration, verification, and governance — not model-only success rates.

| Dimension | Cemini artifact |
|-----------|-----------------|
| Auditable | wiki `log.md`, git, ingest_session_gate |
| Persistent | librarian, stash, wiki sync |
| Modular | MCP servers, skills, subagents |
| Verifiable | `skill_audit.py`, pytest (prod), world-cup-bot gates |
| Orchestration | conductor, lazy-tool |

**Use:** extend Gemini/Exa tool-eval prompts (v8+) and prod brief acceptance — require harness-dimension notes per Adopt candidate.

**K101 extension:** `@concepts/agents-last-exam-benchmark.md` scores **whole professional workflows** (2.6% pass); `@concepts/adk-arena-framework-evaluation.md` isolates **framework choice** at ecosystem scale — complementary to subsystem checklist above.

## Snippets

> Treat memory, retrieval, tools, orchestration, verification, and governance as measurable harness subsystems. [Source: @ccc-wiki/sources/arxiv-system-scaling-harness-2605.26112.md]
