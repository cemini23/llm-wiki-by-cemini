---
title: "FalkorDB — sparse-matrix property-graph database with native HNSW vector indexes; benchmark-leading GraphRAG SDK (SSPL-licensed, IP-sale poison-pill on deployed stack)"
type: source
tags: [github, graph-database, graphrag, knowledge-graph, hnsw, vector-search, property-graph, opencypher, sspl-license, ip-sale-blocker, workspace-side-only]
clusters: [llm-agents]
keywords: [falkordb, graphrag-sdk, graphblas, sparse-matrix, opencypher, hnsw, property-graph, sspl, hybrid-query, knowledge-graph]
related:
  - concepts/wiki-tooling-evaluation.md
  - sources/agentmemory-rohitg00-cpr-impl.md
  - concepts/ip-sale-readiness.md
  - concepts/cryptographic-audit-trail.md
maturity: validated
read_status: read
created: 2026-04-28
updated: 2026-04-28
---

## Relations

- @concepts/wiki-tooling-evaluation.md — synthesis page; **deferred for deployed-stack adoption (SSPL poison-pill); workspace-side experiment candidate**
- @sources/agentmemory-rohitg00-cpr-impl.md — sibling memory-engine candidate; agentmemory's RRF fusion (BM25 + Vector + Graph) is one possible architecture for the same hybrid retrieval problem FalkorDB addresses in a single DB
- @concepts/ip-sale-readiness.md — license posture is the dominant axis: SSPL v1 is the same poison-pill family as AGPL; an acquirer of the Cemini IP integrating FalkorDB in a customer-facing service either pays for a commercial license or open-sources the entire service stack
- @concepts/cryptographic-audit-trail.md — graph databases enable schema-bound queries that vector-RAG cannot answer; cited GraphRAG benchmarks (3-4× better on cross-document reasoning) parallel the audit-trail story — provenance is a graph problem, not a chunk problem

## Raw Concept

- **Original title**: FalkorDB — *Ultra-fast, Multi-tenant Graph Database. Powering Generative AI, Agent Memory, Cloud Security, and Fraud Detection.*
- **Author**: 70 contributors, top: swilly22, jeffreylovitz, AviAvni, gkorland, dependabot[bot]
- **Type**: GitHub repo + commercial DB (FalkorDB Inc.)
- **URL**: https://github.com/falkordb/falkordb / https://www.falkordb.com/
- **Retrieved**: 2026-04-28 (via Exa `crawling_exa` + `web_search_exa` for license + benchmarks)
- **Stars**: 4164 ⭐⭐⭐⭐ (mature ecosystem)
- **License**: **SSPL v1** 🔴 (poison-pill family with AGPL — see narrative)
- **Created**: 2023-07-20; **Last push**: 2026-04-24; **Latest release**: v4.18.1 (2026-04-12)
- **Stack**: C (55%), Python (22%), Gherkin tests (16%); runs as a Redis module
- **Read status**: read (deep-read README + license docs + benchmarks; verified license against `docs.falkordb.com/References/license.html`)

## Narrative

FalkorDB is a **property-graph database that uses sparse adjacency-matrix representations via GraphBLAS** for graph operations — the first DB to ship this approach commercially. It runs as a Redis module (load it as a module to a Redis server). Speaks openCypher (Property Graph Model). **Native HNSW vector indexes since v4.0+** mean hybrid queries (vector-similarity + graph-traversal) work in a single Cypher statement, eliminating the dual-DB sync problem that plagues pgvector + Neo4j or Qdrant + ArangoDB topologies.

### Why this matters for the workspace librarian

The Cemini workspace wiki **is already a graph**. Every page has bidirectional `related:` edges. `wiki_lint.py` enforces graph integrity (orphans / bidir gaps / dangling / missing @paths are all graph-validity checks). The bidirectional discipline is non-negotiable in `CLAUDE.md`. FalkorDB would be a **native fit for representing the wiki as a queryable graph** — convert each `.md` page to a node, each `related:` entry to an edge, embed the page's Narrative + Snippets into HNSW for semantic queries. Hybrid retrieval (graph traversal + vector similarity in one Cypher query) is the kind of pattern wiki-grep + Dataview + grep-by-cluster cannot do today.

### GraphRAG benchmarks — why this beats vector-only RAG for our queries

Two independent benchmarks (cited from external Exa search):

**AIMultiple benchmark (2026-03-20)**, 3,904 Amazon electronics reviews, ~900 queries:
- Vector-RAG better for *specific document search*: **54% vs 35%**
- Graph-RAG better for *aggregation queries*: **23% vs 8%** (3× lift)
- Graph-RAG better for *cross-document reasoning*: **33% vs 8%** (4× lift)
- "Without Cypher aggregation, Graph RAG drops from 73.5% to 23.1%, near Vector RAG at 18.5%. The 50pp gap was not retrieval. It was computation: the graph traverses, groups, and counts across the full dataset before the LLM generates an answer."

**FalkorDB GraphRAG-Bench (own benchmark, 2026)**:
- FalkorDB GraphRAG SDK: **69.73 overall** (Novel: 63.73, Medical: 75.73)
- G-Reasoner: 66.12
- Vector-RAG (with rerank): **55.39** (~14 percentage points behind)
- HippoRAG2: 60.67

The cross-document reasoning advantage is **directly relevant to our query patterns**. Examples of Cemini-side queries that would be graph-RAG-natural and vector-RAG-poor:
- "What entities are referenced by both `concepts/scatter-gather-topology.md` and `entities/frameworks/langgraph.md` but NOT by `entities/infrastructure/deepseek-api.md`?" (set-difference traversal — vector-RAG cannot answer)
- "Show me all pages where the `[NEEDS VERIFICATION]` tag is older than 7 days AND the page has more than 3 inbound `related:` edges" (predicate join across nodes + edge counts — vector-RAG cannot answer)
- "Find K-series source pages that contradict an entity-page claim by date — surface the contradiction graph" (cross-document reasoning across cluster — exactly the K8 stale-snapshot pattern)

### License: the dominant blocker

**FalkorDB ships under the Server Side Public License v1 (SSPLv1).** From the project's own license docs:

> "If you make the functionality of the Program available to third parties as a service, you must make the Service Source Code available."

Plain-English implications for Cemini:
- **Self-hosting for internal use**: permissible without open-sourcing.
- **Offering FalkorDB as a managed service to customers**: requires open-sourcing the entire service stack OR purchasing a commercial license.
- **Embedding FalkorDB in a customer-facing trading product** (the Cemini IP-sale path): falls under the SSPL "available to third parties as a service" trigger. An institutional acquirer faces the same trade-off — open-source their stack or license commercially.

**SSPL is in the same poison-pill family as AGPL** for IP-sale due diligence. K6 / K7 corporate-structure work flagged AGPL projects (DB-GPT, etc.) as institutional-acquirer-rejected. SSPL receives identical treatment. This is **not a bug to fix at integration time** — it's a structural license incompatibility with the IP-sale narrative documented in `concepts/ip-sale-readiness.md`.

### Adoption verdict (per the wiki-tooling-evaluation concept page)

**Workspace-side experiment** ✅ — internal-tooling on the laptop, not customer-facing-service. The SSPL "service to third parties" trigger does not fire for purely-internal tooling.

**Hetzner deployed stack** ❌ — would compromise the IP-sale narrative.

**Mitigation if the experiment proves valuable**: keep markdown as canonical (filesystem-first), use FalkorDB as a *derived index* rebuilt nightly from the markdown wiki. If the experiment is abandoned, deleting the FalkorDB instance loses nothing — markdown is the source of truth. If FalkorDB stays, the workspace gains GraphRAG retrieval for laptop-side librarian queries; the deployed Cemini stack stays SSPL-clean by using a different (pgvector-based) retrieval path that the cpr-pattern wiring can implement on the deployed Python stack.

### What FalkorDB does not solve

- **Schema migration**: importing 373 markdown pages requires an importer (write Cypher + frontmatter parser; 1-2 days work).
- **Markdown ↔ graph drift**: any time markdown edits land but the FalkorDB index hasn't rebuilt, queries return stale results. Solvable with a watch-on-filesystem-change rebuild script, but adds operational complexity.
- **Per-page hash incremental compile** (the llm-wiki-compiler win): FalkorDB doesn't ship this; you'd write your own.

## Snippets

### S1 — License (`docs.falkordb.com/References/license.html`)

> "FalkorDB is licensed under the Server Side Public License v1 (SSPLv1). The Server Side Public License (SSPLv1) is designed to ensure that if you use FalkorDB as part of a service you make available to others (e.g., in the cloud or as an API), you are required to make the source code of your complete service available under the SSPLv1 license. […] If your closed-source project does not make FalkorDB available to external users as part of a service, you can use it without open-sourcing the rest of your code. However, if you provide FalkorDB as part of a service, the SSPLv1 requires you to open-source your codebase associated with the service."

### S2 — Architectural innovation (`README.md`)

> "FalkorDB is the first **queryable Property Graph database to leverage sparse matrices** for representing the adjacency matrix in graphs and linear algebra to query the graph."

### S3 — GraphRAG vs Vector-RAG benchmark (AIMultiple, 2026-03-20)

> "Vector RAG finds specific documents better (54% vs 35%). Graph RAG retrieves relevant results for aggregation queries 3x more often (23% vs 8%) and for cross-document reasoning 4x more often (33% vs 8%). […] Without Cypher aggregation, Graph RAG drops from 73.5% to 23.1%, near Vector RAG at 18.5%. The 50pp gap was not retrieval. It was computation: the graph traverses, groups, and counts across the full dataset before the LLM generates an answer."

### S4 — Hybrid query pattern (FalkorDB graphrag-sdk repo, comparing dual-DB topologies)

> "FalkorDB (v4.0+) supports HNSW vector indexes natively. […] | Issue | Impact | | --- | --- | | Data synchronization | Embeddings can drift out of sync with graph nodes | | Operational complexity | Two databases to maintain, monitor, backup | | Query latency | Network hop between DBs adds ~5-20ms per query | | Transactional integrity | No atomic operations across both systems | | Query expressiveness | Cannot combine vector similarity with graph patterns in one query |"

### S5 — GraphRAG-Bench leaderboard (FalkorDB GraphRAG SDK README)

> "| Rank | System | Novel (Multi-Doc) | Medical (Single-Doc) | Overall | | :--- | :--- | :---: | :---: | :---: | | 1 | FalkorDB GraphRAG SDK | 63.73 | 75.73 | 69.73 | | 2 | G-Reasoner | 58.94 | 73.30 | 66.12 | […] | 6 | RAG (w rerank) (Vector RAG) | 48.35 | 62.43 | 55.39 |"
