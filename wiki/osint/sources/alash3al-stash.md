---
title: "alash3al/stash — Persistent Memory Layer for AI Agents (Apache-2.0, Go, MCP, Postgres+pgvector)"
type: source
tags: [github, mcp-server, ai-memory, postgres, pgvector, llm-agent-memory, librarian-tooling, adopt-tier, gemini-dr-wave5a, fork-and-maintain]
keywords: [stash, persistent-memory, mcp-server, ai-memory, episodic-memory, fact-extraction, postgres, pgvector, 8-stage-consolidation, claude-desktop, cursor, windsurf, cline, continue, openrouter, ollama, alash3al, apache-2-0, go-binary, librarian-deployment]
clusters: [librarian-tooling, llm-agents, infrastructure]
related:
  - sources/gemini-dr-wave5a-cemini-stack-2026-04-30.md
  - sources/upstash-context7.md
  - sources/atomicmemory-llm-wiki-compiler.md
  - concepts/llm-agent-systems.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/ip-sale-readiness.md
  - entities/infrastructure/pgvector.md
  - entities/infrastructure/hetzner.md
  - entities/infrastructure/deepseek-api.md
  - concepts/high-signal-paper-patterns.md
  - concepts/mcp-tool-marketplace.md
  - sources/agriciDaniel-claude-obsidian.md
maturity: validated
read_status: deployed
created: 2026-04-30
updated: 2026-05-02
---

## Relations

- @sources/gemini-dr-wave5a-cemini-stack-2026-04-30.md — Wave 5A canonical brief; URL 5 of the 6-URL evaluation; promoted to dedicated page from Adopt verdict
- @sources/upstash-context7.md — adjacent MCP-server-as-Adopt from Wave 4A (URL 14); pairs operationally with stash on the Wiki/Librarian deployment surface
- @sources/atomicmemory-llm-wiki-compiler.md — Wave 4B Adopt for the librarian; stash is the **complementary memory layer** to atomicmemory's wiki-compilation layer (compiler outputs static markdown; stash holds dynamic episodic memory)
- @concepts/llm-agent-systems.md — cluster hub; stash exemplifies the "agent memory" sub-topic — persistent context across sessions for MCP-protocol-compatible agents
- @concepts/wiki-tooling-evaluation.md — adoption decision parent; stash is a **maturity-stratified Adopt** ("Adopt-but-fork-and-pin" subtype, distinct from "Adopt-and-follow-upstream" qlib subtype)
- @concepts/ip-sale-readiness.md — Apache-2.0 root + transitive go.mod sweep required before commit (jackc/pgx, mark3labs/mcp-go are clean by reputation but require formal audit)
- @entities/infrastructure/pgvector.md — stash uses pgvector for vector recall; current Cemini pgvector deployment is the integration touch-point
- @entities/infrastructure/hetzner.md — CPX21 deployment surface (4 GB RAM / 80 GB NVMe); stash Go binary ~50-100 MB + dedicated PostgreSQL ~150-200 MB fits comfortably
- @entities/infrastructure/deepseek-api.md — stash MCP integration sits between Cemini's brain (DeepSeek-V4-Flash) and persistent memory; consolidation-pipeline LLM calls add operational cost surface

## Raw Concept

- **Original title**: "Stash — persistent memory layer for AI agents. Episodes, facts, and working context stored in Postgres. MCP server included. Self-hosted, single binary, no cloud required."
- **Author**: alash3al (sole contributor)
- **Repository**: https://github.com/alash3al/stash
- **License**: Apache-2.0 (file-level + repo-level confirmed via Exa `crawling_exa` 2026-04-30)
- **Primary language**: Go (81.5%) + Go templates (17.9%) + Dockerfile (0.6%)
- **Stars**: 407 (as of 2026-04-30)
- **Contributors**: 1
- **Created**: 2026-04-24 (6 days old at evaluation)
- **Latest release**: v0.2.6 on 2026-04-26
- **Releases**: 9 total
- **Topics**: ai, ai-agents, ai-memory, memory
- **Homepage**: https://alash3al.github.io/stash/
- **Read status**: read (README + license + go.mod headers + 8-stage-pipeline overview, via `crawling_exa`; deeper module-level read pending pre-adoption commit)
- **Discovered via**: User Wave 5A Gemini DR brief (2026-04-30)
- **Primary cluster**: librarian-tooling
- **All clusters**: librarian-tooling, llm-agents, infrastructure

## Narrative

### What it is

Stash is a self-hosted persistent-memory layer for LLM-based agents. Architecturally, it sits between an MCP-compatible agent (Claude Desktop, Cursor, Windsurf, Cline, Continue, OpenAI Agents, Ollama, OpenRouter, etc.) and a PostgreSQL+pgvector backend. The agent emits "observations" (raw episodes from a session); Stash routes them through an 8-stage consolidation pipeline that distills them into structured knowledge.

**The 8-stage consolidation pipeline**:
1. Episodes → raw observations
2. Facts → extracted atomic claims
3. Relationships → entity-entity links
4. Causal links → temporal/conditional structure
5. Goal tracking → outstanding intents
6. Failure patterns → things that didn't work
7. Hypothesis verification → what got confirmed/refuted
8. Confidence decay → time-weighted forgetting

Each stage processes only new data since the last run, so the consolidation cost is incremental rather than full-corpus. The output is a structured, queryable memory that the agent can recall via MCP tool calls.

The deployment is one Docker Compose command: `docker compose up` brings up Postgres+pgvector, the migrations, and the MCP server with background consolidation, all in one shot.

### Why this matters for Cemini

Two distinct deployment surfaces are evaluated:

**Wiki / Librarian server (CPX21)** — ✅ Adopt:
- Stash bridges the static `llm-wiki-compiler` (markdown corpus, embeddings) and the dynamic Claude Code research workflow.
- Solo-developer Claude Code on laptop connects remotely via MCP to the CPX21-hosted Stash MCP server, establishing a continuous memory chain across sessions.
- Resource footprint fits CPX21's 4 GB envelope: ~150-200 MB PostgreSQL + ~50-100 MB Go binary = ~250-300 MB resident, leaving comfortable headroom.
- Deployed as Dockerized systemd service.

**Cemini production stack** — ⚠️ Partial-fit:
- Could replace simple linear memory in `agents/orchestrator.py` (LangGraph orchestrator) for FastMCP-tool persistent context.
- BUT: the 8-stage LLM-call pipeline introduces token-cost amplification — every observation gets fanned out across 8 LLM calls. This is the **primary risk** for production adoption.
- Pre-prod gate: profile token-cost ratio (tokens-consumed-by-pipeline per 1000 tokens of raw episodic input) on representative Cemini workload.

**Workflow** — ✅ Yes-fit:
- Solo-dev local Claude Code → remote MCP → CPX21 Stash = unbroken memory chain across sessions.
- Direct alignment with the "research librarian" workflow ethos.

### Cross-paper / cross-tool synthesis

- **Pair with `@sources/upstash-context7.md`** (Wave 4A Adopt): context7 is "what does the API surface look like *now*" (up-to-date library docs); stash is "what did *this* user/session learn *across time*". Together they form a complete LLM memory stack — external knowledge (context7) + internal episodic memory (stash).
- **Pair with `@sources/atomicmemory-llm-wiki-compiler.md`** (Wave 4B Adopt): wiki-compiler emits static markdown; stash holds dynamic episodic memory. The Cemini wiki/librarian stack benefits from both.
- **Pair with `@entities/infrastructure/pgvector.md`**: stash piggybacks on Cemini's existing pgvector competency. The same vector-recall pattern Cemini uses for semantic search of the wiki applies to stash's fact-recall queries.

### Deployment (2026-05-02)

✅ Stash v0.2.9 deployed on `cemini-librarian` (5.161.179.207) as the librarian's episodic memory layer. Complements kb-server (static wiki RAG) with dynamic memory: episodes, facts, working context, contradictions, causal links, hypotheses, goals, and failure records — all stored in Postgres + pgvector and queryable via MCP SSE.

Key deployment choices: pre-built binary from GitHub releases (Go 1.25.5 requirement blocked build-from-source on Ubuntu 22.04 with Go 1.22.2). Ollama-backed embeddings (`nomic-embed-text`) and reasoning (`qwen2.5:0.5b`, ~500 MB) — zero-API-cost design fitting CPX21's 4 GB RAM envelope. Postgres 16 + pgvector 768-dim. Systemd-managed, consolidation every 5 minutes, 168h window.

Full deployment record: `briefs/2026-05-02_stash-deployment-record.md`.

### Risks & open questions

1. **Bus-factor: 1 contributor on a 6-day-old repo** — textbook fork-and-maintain situation. The project may evaporate if the maintainer pivots. **Mitigation**: pin v0.2.6, fork to Cemini-controlled GitHub org, treat as in-house code from day 1.

2. **Token-cost amplification from 8-stage pipeline** [NEEDS VERIFICATION 2026-04-30] — measure tokens-per-1000-input-tokens ratio on Cemini's actual workload. If the ratio exceeds ~10:1, prod adoption is uneconomical without per-stage cost gating.

3. **Transitive go.mod license sweep** [NEEDS VERIFICATION 2026-04-30] — Apache-2.0 root is clean. Transitive deps (jackc/pgx, mark3labs/mcp-go) are clean by reputation but need formal audit before any commit. Use `go-licenses` or equivalent.

4. **Consolidation-pipeline determinism** — the 8 stages run via LLM calls. Same input + different model temperature = different consolidation. For the Wiki/Librarian use case this is fine (research-assistant non-determinism is acceptable). For any future production path it would be a hard blocker.

5. **PostgreSQL upgrade compatibility** — Cemini's existing pgvector is on a specific Postgres version. Stash deploys its own dedicated Postgres instance (per docx evaluation) — keeps the two isolated, avoiding upgrade-coupling.

### Cemini-side adoption assessment

**Decision**: **Adopt for Wiki/Librarian server, defer Cemini-prod adoption pending token-cost profile.**

**Status: ✅ DEPLOYED 2026-05-02 on `cemini-librarian` (5.161.179.207).**

Deployment details: Stash v0.2.9 (pre-built binary from GitHub releases) deployed at `/opt/stash/` on the librarian server. Postgres 16 with pgvector extension (768-dim, nomic-embed-text). Embedding model via Ollama (`localhost:11434`); reasoning model `qwen2.5:0.5b`. MCP SSE endpoint on port 8080, HTTP on port 9090. Consolidation every 5 minutes, 168h window, similarity threshold 0.85. Systemd-managed (`stash.service`, enabled). Primary namespace: `/cemini`. Bootstrap memories stored — CeminiSuite platform architecture overview and key facts.

Two-layer memory architecture now operational on the librarian:
- **kb-server** (:3838) — static wiki RAG (markdown → embeddings → FTS5 search)
- **stash** (:8080 MCP / :9090 HTTP) — dynamic episodic memory (episodes, facts, working context, contradictions, causal links, hypotheses, goals, failure records)

Full deployment record: `briefs/2026-05-02_stash-deployment-record.md`.

Concrete next-steps (remaining):

1. **Fork-and-pin** ✅ DONE 2026-05-02 — forked to `cemini23/stash` (https://github.com/cemini23/stash) from `alash3al/stash` at v0.2.9.
2. **Wire laptop Claude Code MCP config** ✅ DONE 2026-05-02 — `~/.mcp.json` configured with SSE transport to `localhost:8088/sse` via SSH tunnel (`ssh -f -N -L 8088:localhost:8080 -o ServerAliveInterval=60 cemini-librarian`). Tunnel must be re-established after laptop reboot.
3. **Run 30-day shadow mode** with token-cost telemetry — observe pipeline cost on a sample of real sessions. **Decision gate** for any prod-stack consideration.
4. **Re-evaluate at next wave touch** for prod-stack adoption.

License + IP-sale-readiness disposition: **acceptable as-deployed**. Apache-2.0 is on the clean license list. Transitive sweep is the only outstanding gate.

### Citation

> alash3al. (2026). *Stash — Persistent Memory Layer for AI Agents*. v0.2.6. GitHub. https://github.com/alash3al/stash (License: Apache-2.0; retrieved 2026-04-30 via Exa `crawling_exa`)

## Snippets

> **The repo's identity statement**:
>
> "Stash — persistent memory layer for AI agents. Episodes, facts, and working context stored in Postgres. MCP server included. Self-hosted, single binary, no cloud required." [Source: github.com/alash3al/stash README, retrieved 2026-04-30]

> **The 8-stage consolidation rationale**:
>
> "Stash is a cognitive layer between your AI agent and the world. Episodes become facts. Facts become relationships. Relationships become patterns. Patterns become wisdom. An 8-stage consolidation pipeline turns raw observations into structured knowledge — facts, relationships, causal links, goal tracking, failure patterns, hypothesis verification, and confidence decay. Each stage only processes new data since the last run." [Source: github.com/alash3al/stash README, retrieved 2026-04-30]

> **Wave 5A integration vector**:
>
> "Stash will be deployed as a Dockerized systemd service on the CPX21 server. It will bridge the gap between the static llm-wiki-compiler and the dynamic reasoning of the analyst Claude Code instance. … This establishes an unbroken chain of memory from research session to production deployment via the MCP protocol." [Source: Codebase Evaluation for Trading & Wiki 4_30.docx URL 5]

> **Wave 5A risk caveat — the bus-factor + cost surface**:
>
> "Cost management is the primary risk associated with adoption. The 8-stage consolidation process (extracting facts, relationships, causal links) relies heavily on recursive LLM calls. If misconfigured, the operational expenditure to maintain the agent's memory could exceed the cost of the agent's primary task." [Source: Codebase Evaluation for Trading & Wiki 4_30.docx URL 5]
