---
title: "Beever Atlas — Dual-Memory Knowledge Graph for Intelligence Distillation"
type: entity
tags: [tool, knowledge-graph, graphrag, intelligence, mcp, weaviate, neo4j, fastapi, k37, k46]
keywords: [beever-atlas, google-adk, knowledge-graph, weaviate, neo4j, graphrag, intelligence-distillation, mcp-server, apache-license, adopt]
related:
  - sources/evaluating-urls-system-integration.md
  - sources/multi-wiki-link-eval-v4-2026-05-15.md
  - concepts/tool-evaluation-framework.md
  - entities/infrastructure/conductor-librarian-architecture.md
maturity: validated
created: 2026-05-11
updated: 2026-05-15
license_verified: Apache-2.0
---

## Relations

- @sources/evaluating-urls-system-integration.md — K37 source evaluation (URL 15, Steal-from)
- @sources/multi-wiki-link-eval-v4-2026-05-15.md — K46 v4 re-evaluation: upgraded to Adopt
- @concepts/tool-evaluation-framework.md — three-surface methodology applied
- @entities/infrastructure/conductor-librarian-architecture.md — dual-memory architecture (Weaviate + Neo4j) mirrors librarian's vector+graph topology

## Raw Concept

- **Repo / URL**: `github.com/Beever-AI/beever-atlas`
- **Tier**: **Adopt** (upgraded from Steal-from, K37 → K46). The v4 multi-wiki evaluation re-assessed at 326 stars, last commit 2026-04-30, 1 open issue — mature enough for adoption.
- **License** [VERIFIED 2026-05-11]: **Apache-2.0** (clean for pattern extraction per Cemini license posture).

## Narrative

Beever Atlas deploys a 6-stage Google ADK pipeline that distills unstructured chat logs and conversations into atomic facts and entity relationships. The dual-memory architecture combines:

- **Weaviate** — semantic vector search for fuzzy concept retrieval
- **Neo4j** — deep entity relationship graphs for structured knowledge queries

This mirrors the OSINT librarian's topology (vector embeddings + graph relationships) but adds the intelligence distillation pipeline — extracting structured facts from raw conversation streams. The built-in 16-tool MCP server demonstrates a production MCP deployment pattern for querying graph stores.

### K37 → K46 upgrade rationale

K37 rated Steal-from due to early-stage maturity (293 stars, ~3 weeks old). K46 v4 re-evaluation finds 326 stars, 1 open issue, active maintenance through April 2026, and a mature 16-tool MCP server — satisfying the Adopt threshold. The dual-memory design also independently validates the librarian's vector+graph approach.

### Integration vector

Adopt: the dual-memory pattern and 6-stage ADK pipeline are reference architectures for any future automated intelligence distillation in the OSINT wiki. The 16-tool MCP server configuration provides a baseline for MCP-to-graph-store query patterns. Still do NOT deploy full stack (distributed infra too heavy for CPX21) — pattern extraction only.

### Risks

Full Beever deployment requires distributed infrastructure unsuited for the 4 GB librarian envelope. Pattern extraction only.

## Cross-wiki routing

- **@ccc-wiki** — brief documenting the 16-tool MCP server configuration as a baseline for MCP-to-graph-store query patterns.
