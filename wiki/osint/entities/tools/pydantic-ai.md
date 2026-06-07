---
title: pydantic-ai — typed LLM agent framework (Pydantic)
type: entity
tags: [tool, ccc, agents, python, adopt, k103]
keywords: [pydantic-ai, structured-output, mcp, langgraph, monty-sandbox]
related:
  - sources/multi-wiki-tool-eval-v8-k103-2026-06-07.md
  - concepts/cemini-license-posture.md
  - sources/tradingagents.md
  - "@ccc-wiki/entities/tools/pydantic-ai.md"
maturity: draft
created: 2026-06-07
updated: 2026-06-07
phase_0_verdict: "GO 2026-06-07 — MIT core confirmed; do NOT adopt pydantic-ai-gateway (AGPL-3.0)"
---

## Relations

- @sources/multi-wiki-tool-eval-v8-k103-2026-06-07.md — K103 Adopt
- @sources/tradingagents.md — sibling multi-agent finance framework (steal-from)

## Raw Concept

- **URL:** https://github.com/pydantic/pydantic-ai
- **Tier:** Adopt (CCC + Cemini financial typed agents)
- **License:** MIT (core) [CONFIRMED 2026-06-07]
- **Companion AGPL:** `pydantic/pydantic-ai-gateway` — **Reject for prod**

## Narrative

Industry-standard Python agent framework: Pydantic-typed tool I/O, provider abstraction, MCP/A2A surfaces, Monty sandboxed execution. Reduces hallucinated tool args vs free-text parsing in `agents/orchestrator.py`.

**Phase-0 GO:** laptop install via `adopt_k103_phase0.sh`; prod integration via staged brief (targeted modules, not framework-wide rewrite).

## Snippets

> "Shift away from fragile free-text parsing toward strongly-typed Pydantic models for LLM outputs." [Source: Tool Evaluation and Wiki Fit.docx URL 27; K103]
