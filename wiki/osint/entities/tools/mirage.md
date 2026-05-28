---
title: mirage (strukto-ai) — Unified Virtual File System for LLM agents (Steal-from, Cemini-financial)
type: entity
tags: [tool, vfs, virtual-filesystem, apache-2-0, steal-from, cemini-financial, redis-streams, postgres, mcp]
keywords: [mirage, strukto, virtual filesystem, vfs, posix mount, redis streams, mongodb, s3, gdrive, grep jq cat, llm tooling]
related:
  - sources/tool-evaluation-wiki-fit-2026-05-13.md
  - concepts/tool-evaluation-framework.md
  - concepts/conductor-orchestrator.md
maturity: draft
created: 2026-05-13
updated: 2026-05-28
---

## Relations

- `@sources/tool-evaluation-wiki-fit-2026-05-13.md` — origin source (Doc 3, K42), Steal-from
- `@concepts/tool-evaluation-framework.md` — methodology
- `@concepts/conductor-orchestrator.md` — Cemini agent stack — VFS mount could replace bespoke SDK code for Redis Streams/Postgres data access

## Raw Concept

- **URL**: `https://github.com/strukto-ai/mirage`
- **License**: Apache-2.0
- **Stars**: 2.1k / 13 open issues
- **Stack**: TypeScript (57.5%), Python (42.4%), Redis
- **Tier**: Steal-from
- **Primary fit**: Cemini financial + Workflow

## Narrative

Unified Virtual File System mounting MongoDB, Redis, Amazon S3, Google Drive as a POSIX directory tree so LLMs use stdlib Bash tools (`grep`, `jq`, `cat`) without bespoke SDK code.

### Cemini direct utility

Mount Redis Streams + PostgreSQL backtesting tables under `/opt/cemini/vfs/` so agents `grep`/`cat` market data natively. Transformative for `agents/orchestrator.py` hallucination reduction.

### Steal-from scope

Extract two-layer cache (Index cache + File cache) into existing LangGraph nodes rather than full Adopt. Avoid scope creep.

### Phase-0 audit (2026-05-28)

| Check | Result |
|-------|--------|
| License | **Apache-2.0** confirmed |
| Maturity | ~2.75k★, active, substantial codebase |
| Layout lock-in | **PASS** — no hardcoded wiki directory assumptions found in quick scan |
| Prod risk | VFS mount + Redis/Postgres connectors need hardened-namespace review before prod pods |

**Verdict: CONDITIONAL-GO (steal-from)** — extract cache/VFS patterns for agent data access; no full prod deploy without security soak.

[Source: Tool Evaluation and Wiki Fit.docx URL 10 (retrieved 2026-05-13)]
