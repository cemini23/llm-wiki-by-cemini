---
title: tabularis — MCP-native Postgres/SQLite client (Adopt-tier, Cemini-financial fit)
type: entity
tags: [tool, database-client, postgresql, sqlite, mcp-server, tauri, rust, adopt-tier, cemini-cross-route, apache-2-0]
keywords: [tabularis, mcp server, postgres client, sqlite client, tauri v2, rust, sqlx, react 19]
related:
  - sources/multi-wiki-link-eval-prompt-2026-05-13.md
  - concepts/tool-evaluation-framework.md
  - concepts/mcp-tool-marketplace.md
maturity: draft
created: 2026-05-13
updated: 2026-05-28
---

## Relations

- `@sources/multi-wiki-link-eval-prompt-2026-05-13.md` — origin source (Doc 2, K42), Adopt-tier
- `@concepts/tool-evaluation-framework.md` — methodology
- `@concepts/mcp-tool-marketplace.md` — tabularis ships a native MCP server

## Raw Concept

- **URL**: `https://github.com/TabularisDB/tabularis`
- **License**: Apache-2.0
- **Stars**: 1.6k / 37 open issues
- **Stack**: React 19, TypeScript, Rust, Tauri v2, SQLx
- **Tier**: Adopt
- **Primary fit**: Workflow + Cemini-financial (PostgreSQL integration)

## Narrative

High-performance Rust desktop DB client with native MCP server. Allows AI assistants (Claude Desktop, Cursor, Windsurf) to execute SQL, explain query plans, inspect schemas.

### Cemini direct utility

Integrate native MCP server with `/opt/cemini` PostgreSQL instances to enable AI-assisted query generation against trading data + Polymarket backtesting metrics.

### Phase-0 audit (2026-05-28)

| Check | Result |
|-------|--------|
| License | **Apache-2.0** confirmed |
| Maturity | ~2.2k★, active, large Rust/Tauri codebase |
| MCP surface | Native MCP server for SQL/schema/query-plan workflows |

**Verdict: CONDITIONAL-GO** — useful laptop-side Postgres/SQLite assistant for `/opt/cemini` data inspection; not a prod trading-runtime dependency.

[Source: Multi-Wiki Link Evaluation Prompt.docx URL 10 (retrieved 2026-05-13)]
