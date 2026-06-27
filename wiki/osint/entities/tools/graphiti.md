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
maturity: validated
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

**K132 operator spike: PASS (2026-06-27).** Not pending. Aura holds r2+ episodes; v1 extracted facts may still appear in hybrid search until manual purge.

Brief: `briefs/ccc-2026-06-27_k132-graphiti-temporal-kg-spike.md`

### K132 spike status (2026-06-27)

Runner: `.local/graphiti_spike_ingest.py` + venv `.local/venv-graphiti-spike/` (`graphiti-core`).

| Check | Result |
|-------|--------|
| Neo4j Aura (`NEO4J_*` in repo `.env`) | **PASS** — direct connect + indices |
| Episode ingest (20 `wiki/entities/tools/` pages) | **PASS** — all 20 episodes OK |
| Hybrid search — gbrain RETIRED vs Adopt | **PASS** — top facts include *distinct from retired gbrain MCP* |
| Cross-encoder rerank (`search_` + OpenRouter) | **SKIP** — OpenRouter logprobs incompatible; default `GRAPHITI_SEARCH_MODE=basic` |
| Re-ingest verification (2026-06-27) | **PASS** — r2 episodes ingested; fresh facts present (legacy v1 may coexist in Aura) |

**Env wiring:** Neo4j from `OSINT WORKSPACE/.env`; LLM + embeddings from `~/.cemini/llm-routing.env` (`OPENROUTER_API_KEY`, default models `google/gemini-2.5-flash` + `openai/text-embedding-3-small`). Optional native rerank: `GRAPHITI_CROSS_ENCODER=openai` when `OPENAI_API_KEY` set. Re-run: `source scripts/source_llm_routing_env.sh && python3 .local/graphiti_spike_ingest.py` (add `--search-only` or `--verify-only`).

Report: `.local/reports/graphiti-spike-2026-06-27.md`. Posture remains **Adopt** for laptop-side temporal KG eval; not prod trading stack.

## Snippets

> Apache-2.0 temporal knowledge graph for AI agent memory [Source: getzep/graphiti GitHub (retrieved 2026-06-27)]
