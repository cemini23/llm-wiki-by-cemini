---
title: "willynikes2/knowledge-base-server — persistent memory engine + 16-tool MCP server with three-tier (hot/warm/cold) memory architecture"
type: source
tags: [github, npm, mcp-server, knowledge-base, persistent-memory, sqlite-fts5, embeddings, three-tier-memory, multi-agent, sidecar]
clusters: [llm-agents]
keywords: [knowledge-base-server, kb-server, memstalker, three-tier-memory, hot-warm-cold, kb-classify, kb-promote, kb-synthesize, fts5, hybrid-search]
related:
  - concepts/wiki-tooling-evaluation.md
  - sources/atomicmemory-llm-wiki-compiler.md
  - sources/agentmemory-rohitg00-cpr-impl.md
  - sources/wastedcode-memex.md
  - sources/llm-wiki.md
  - concepts/context-compression-resume-pattern.md
  - entities/frameworks/fastmcp.md
  - concepts/mcp-tool-marketplace.md
  - sources/agriciDaniel-claude-obsidian.md
maturity: validated
read_status: read
created: 2026-04-28
updated: 2026-04-28
---

## Relations

- @concepts/wiki-tooling-evaluation.md — synthesis page; ranks this as **deferred** (sidecar value gated on multi-agent need we don't yet have)
- @sources/atomicmemory-llm-wiki-compiler.md — sibling Karpathy-pattern tool; covers the compile/query/lint loop directly without three-tier memory or self-learning loop
- @sources/agentmemory-rohitg00-cpr-impl.md — sibling memory engine; agentmemory uses iii-engine + TS, kb-server uses Express + SQLite + JS; both implement compress-preserve-resume in different shapes
- @sources/llm-wiki.md — Karpathy's gist; kb-server's "self-learning loop" (capture → classify → promote → synthesize → compound) is a strict superset of Karpathy's ingest→compile→query→save-back loop
- @concepts/context-compression-resume-pattern.md — kb-server's `kb_promote` (raw → structured) maps to cpr-pattern Phase 1 Compress; `kb_synthesize` (cross-source themes) is novel beyond cpr-pattern
- @entities/frameworks/fastmcp.md — kb-server's 16-tool MCP server is the closest stylistic peer to Cemini's deployed `cemini_mcp` (130 `@mcp.tool` decorators); kb-server is JS-first, Cemini is Python-first

## Raw Concept

- **Original title**: knowledge-base-server — *Make every AI agent you use smarter. Persistent memory with SQLite FTS5, MCP server, Obsidian sync, and self-learning intelligence pipeline.*
- **Author**: Shawn Daniel (willynikes2) "with significant contributions from Claude, Codex, and Gemini"
- **Type**: GitHub repo + paid SaaS sibling (Memstalker.com)
- **URL**: https://github.com/willynikes2/knowledge-base-server
- **Retrieved**: 2026-04-28 (via Exa `crawling_exa`)
- **Stars**: 162; **License**: MIT 🟢
- **Created**: 2026-04-03; **Last push**: 2026-04-04
- **Stack**: JavaScript (89.6%), Node.js ≥ 18, Express, SQLite (FTS5), Xenova all-MiniLM-L6-v2 embeddings (local — no external API for embeddings)
- **Read status**: read (deep-read README; mapping against the schema and the three-tier memory pattern)

## Narrative

knowledge-base-server is a **JavaScript memory engine + MCP server** that sits between human-curated knowledge (Obsidian vault, files, web clippings) and AI agents that consume it. It runs as an Express daemon on port 3838, exposes 16 MCP tools + a REST API + an OpenAPI 3.1 spec, and uses SQLite + FTS5 for keyword search and local Xenova embeddings for semantic search. Designed for the "one brain, multiple agents" pattern: Claude + Codex + Gemini all read/write the same knowledge base.

**Architectural distinction from llm-wiki-compiler**: kb-server is database-first (SQLite is canonical, Obsidian sync is bidirectional), llm-wiki-compiler is filesystem-first (markdown is canonical, hash-incremental compile updates pages in place). For our workspace, **filesystem-first is the strong preference** (git is the version-control story; markdown is the universal-format story; database-vs-markdown drift is a risk we don't want to add). kb-server's SaaS shadow Memstalker.com ($12/mo first-500 tier) suggests the project's center of gravity is the hosted-product business; the open-source repo is dual-purposed.

**Three-tier memory** (hot / warm / cold) is the project's most conceptually-load-bearing innovation:
- **Hot** — active project context, recent sessions, current decisions; retrieved first
- **Warm** — accumulated lessons, validated workflows; retrieved when relevant
- **Cold** — raw captures, archived sources; retrieved only on deep-dive

**Why three tiers** (verbatim from README): "Without tiering, a search for 'authentication' returns every raw article you ever clipped alongside your actual auth architecture decision. The tiers ensure agents get signal, not noise."

This is a **different angle on the cpr-pattern problem** than agentmemory's Compress/Preserve/Resume. agentmemory compresses the trajectory itself (long debate → dense summary → resumable context); kb-server tiers the trajectory by recency-and-promotion-status. Both attempt the same end (signal-vs-noise in retrieval); different mechanism. Cross-link in the cpr-pattern concept page captures this as a *parallel* technique, not a competing one.

**The self-learning loop** (kb-server's framing for the compounding pattern):
```
Sessions 1-10:    AI makes mistakes. You correct. Fixes get captured.
Sessions 10-50:   AI recognizes patterns. Starts getting things right more often.
Sessions 50-100:  AI knows your codebase, preferences, architecture patterns.
Sessions 100+:    One-shot clean code.
```

Loop steps: AI attempts → output evaluated (human judgment) → corrections captured (`kb_capture_session`, `kb_capture_fix`) → KB ingests session data → `kb_synthesize` connects to existing knowledge → agent instructions auto-update with lessons → next session starts with better context.

This is **NOT fine-tuning, NOT RLHF** — it is "self-modifying instructions through operational history." The model doesn't change; the context it receives does. Same posture our workspace already takes with `LESSONS.md` (meta-lessons, distinct from `wiki/log.md`). kb-server automates what we do manually with `LESSONS.md` updates.

**16 MCP tools** (the project's headline integration surface):

| Tool | Description |
|---|---|
| `kb_search` | Full-text search with BM25 + highlighted snippets |
| `kb_search_smart` | Hybrid keyword + semantic search |
| `kb_context` | Token-efficient briefing (summaries only, claims 90%+ savings) |
| `kb_read` | Read full document by ID |
| `kb_list` | List documents filtered by type / tag |
| `kb_write` | Write new note to the Obsidian vault |
| `kb_ingest` | Ingest raw text |
| `kb_classify` | Auto-classify (type / tags / summary / confidence) |
| `kb_promote` | Promote raw source → structured (insight / lesson / decision / runbook) |
| `kb_synthesize` | Cross-source synthesis (themes, patterns, opportunities) |
| `kb_capture_session` | Record a debugging/coding session |
| `kb_capture_fix` | Record bug fix (symptom / cause / resolution) |
| `kb_capture_web` / `kb_capture_youtube` | Web article + YouTube transcript capture |
| `kb_vault_status` | Vault indexing stats |
| `kb_safety_check` | Review destructive action against KB history (multi-model consensus) |

The `kb_classify` + `kb_promote` + `kb_synthesize` triple is the project's **intelligence pipeline** that distinguishes it from a vanilla "vector DB + MCP server." Auto-classification assigns `type` and `tags`, computes `confidence`, generates summaries — exactly the manual ingest work the workspace currently does by hand. Adoption tradeoff: gain automation, lose direct human-curated control.

**Multi-agent shared brain**: Claude + Codex + Gemini connect to the same kb-server; what one agent learns, the others read. Useful when the user runs multiple agents across multiple machines; less critical for our single-Claude workflow.

**Hosted SaaS shadow** — Memstalker.com — same engine, $12/mo first-500-tier (normally $25). Self-host remains free and full-featured. The dual-licensing-via-SaaS pattern is fine but worth noting: any feature gap between OSS and SaaS would surface as a "pay or DIY" decision.

**Why deferred** (per the wiki-tooling-evaluation concept page): kb-server is more opinionated than llm-wiki-compiler, has a heavier integration surface (Express daemon + auth + setup wizard), and the multi-agent shared-brain value isn't a need we currently have. If we ever expand to multi-agent (Claude Code + Cursor + Codex), re-evaluate.

## Snippets

### S1 — Three-tier memory rationale (`README.md`, "Three-Tier Memory")

> "Hot: Active project context, recent sessions, current decisions / Warm: Accumulated lessons, research, validated workflows / Cold: Raw captures, archived sources, old terminal logs. Why three tiers? Without tiering, a search for 'authentication' returns every raw article you ever clipped alongside your actual auth architecture decision. The tiers ensure agents get signal, not noise. Hot knowledge is always fresh and relevant. Cold knowledge is preserved but doesn't pollute active context."

### S2 — Self-learning loop framing (`README.md`, "The Self-Learning Loop")

> "Sessions 1-10: AI makes mistakes. You correct. Fixes get captured. / Sessions 10-50: AI recognizes patterns. Starts getting things right more often. / Sessions 50-100: AI knows your codebase, preferences, architecture patterns. / Sessions 100+: One-shot clean code. […] This is NOT fine-tuning. NOT RLHF. It is self-modifying instructions through operational history. The model doesn't change. The context it receives does. And context is everything."

### S3 — Token-optimized retrieval claim (`README.md`, "Token-Optimized Retrieval")

> "kb_context returns summaries and metadata WITHOUT full content — 90%+ token savings. kb_search uses FTS5 with BM25 ranking, title boosting, and AND-first precision. kb_search_smart combines keyword and semantic search for conceptual queries. kb_read loads full content only when needed, after context identifies relevant docs. Agents get the right information in the fewest possible tokens."

### S4 — Architectural diagram (`README.md`, "Architecture")

```
                     +------------------+
                     |   AI Agents      |
                     | Claude | Codex   |
                     | Gemini | ChatGPT |
                     +--------+---------+
                              |
                MCP (stdio)   |   REST API (/api/v1/)
                MCP (HTTP)    |   OpenAPI 3.1
                              |
                     +--------+---------+
                     |    KB Server     |
                     |   Express :3838  |
                     +--------+---------+
                              |
          +-------------------+-------------------+
          |                   |                   |
 +--------+-------+  +-------+--------+  +-------+--------+
 | SQLite + FTS5  |  |  Embeddings    |  |  Obsidian      |
 | documents      |  |  all-MiniLM    |  |  Vault Sync    |
 | vault_files    |  |  L6-v2 local   |  |  (bidirectional)|
 | embeddings     |  |  cosine sim    |  |  source of truth|
 +----------------+  +----------------+  +----------------+
```

### S5 — Why-this-exists framing (`README.md`, "Why This Exists")

> "I built this because I run three AI agents (Claude, Codex, Gemini) across multiple projects. Without shared context, each agent starts from zero every session. […] With the KB server, all three agents share the same brain. Claude captures a bug fix at 2am, Codex finds it the next morning. Gemini reviews code with full project history. The system gets smarter every day — not because the models improve, but because the context they receive compounds. […] AI is only as good as its context. This is the context layer."
