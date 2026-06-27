---
title: Graphiti — temporal knowledge graph (Zep)
type: entity
tags: [tool, knowledge-graph, temporal, agent-memory, k132]
keywords: [graphiti, getzep, Apache-2.0, hybrid-search, episodic-memory]
related:
  - sources/eval-tool-routing-hermes-plan-2026-06-27.md
  - concepts/wiki-tooling-evaluation.md
  - entities/tools/claude-mem.md
  - entities/tools/gbrain.md
maturity: draft
created: 2026-06-27
updated: 2026-06-27
---

## Relations

- @sources/eval-tool-routing-hermes-plan-2026-06-27.md — K132 Adopt row
- @entities/tools/claude-mem.md — complementary session memory vs temporal KG

## Raw Concept

K132 Phase-0 on [getzep/graphiti](https://github.com/getzep/graphiti) — temporal knowledge-graph library for agent memory (bi-temporal facts, hybrid retrieval).

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | `getzep/graphiti` |
| **License** | **Apache-2.0** (`gh api` 2026-06-27) |
| **Stars / pushed** | ~28k★; pushed 2026-06-23 |
| **Verdict** | **Adopt** (laptop-side eval) — temporal KG for wiki entity edges + episodic facts |
| **Steal** | Bi-temporal edge updates; hybrid retrieval for federation grep gap |

**Not prod trading stack.** Pair with laptop wiki authoring; distinct from retired gbrain MCP (see `@entities/tools/gbrain.md`).

Brief: `briefs/ccc-2026-06-27_k132-graphiti-temporal-kg-spike.md`

## Snippets

> Apache-2.0 temporal knowledge graph for AI agent memory [Source: getzep/graphiti GitHub (retrieved 2026-06-27)]
