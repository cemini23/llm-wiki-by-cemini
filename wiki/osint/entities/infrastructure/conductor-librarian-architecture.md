---
title: "Conductor-Librarian Architecture — Multi-Model Orchestration + Vector/Graph Knowledge Store"
type: entity
tags: [infrastructure, conductor, librarian, mcp, knowledge-base, vector-store, model-routing]
keywords: [conductor, librarian, model-orchestration, pgvector, knowledge-graph, mcp-server, kb-server, stash, dual-memory]
related:
  - entities/tools/beever-atlas.md
  - entities/tools/octocode-mcp.md
  - entities/tools/turbovec.md
maturity: draft
created: 2026-05-15
updated: 2026-05-15
---

## Relations

- @entities/tools/beever-atlas.md — Weaviate+Neo4j dual-memory design independently validates the librarian's vector+graph topology
- @entities/tools/octocode-mcp.md — LSP-based code analysis complements the conductor's model-routing architecture
- @entities/tools/turbovec.md — SIMD vector compression directly applicable to the librarian's pgvector embedding store

## Raw Concept

Stub created during K46 ingest to resolve dangling references from beever-atlas, octocode-mcp, and turbovec entity pages. These three tools independently validate architectural patterns in Cemini's conductor-librarian stack.

## Narrative

The conductor-librarian stack is Cemini's dual-system knowledge infrastructure:

- **Conductor** — multi-model orchestrator that routes queries to the best model (deepseek-chat vs deepseek-reasoner) based on query taxonomy. Exposed as an MCP server (`conductor/mcp_server.py`).
- **Librarian** — kb-server that serves the OSINT wiki (and sibling wikis) via REST API for semantic search. Uses pgvector for embeddings + structured metadata for graph-style queries.

The dual-memory pattern (vector embeddings for fuzzy search + structured graphs for relationship queries) is independently validated by Beever Atlas's Weaviate+Neo4j design.
