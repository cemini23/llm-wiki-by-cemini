---
title: "claude-mem — Persistent Memory Plugin for Claude Code"
type: entity
tags: [tool, memory, claude-code, plugin, context, workflow, adopted]
keywords: [claude-mem, persistent memory, context persistence, Claude Code plugin, ChromaDB, Bun]
related:
  - sources/evaluating-links-trading-wiki-stacks.md
  - concepts/tool-evaluation-framework.md
maturity: validated
created: 2026-05-10
updated: 2026-05-10
laptop_install: VERIFIED 2026-05-10 (v13.0.1)
---

## Relations
- `@sources/evaluating-links-trading-wiki-stacks.md` — source evaluation brief (URL 18)

## Raw Concept

Claude-Mem is a Claude Code plugin that provides persistent, compressed memory across sessions by silently observing terminal activities, tool executions, and file edits, then injecting relevant context on session start.

- **Repo**: `github.com/thedotmack/claude-mem`
- **License**: Apache-2.0 [VERIFIED 2026-05-10 via Phase-0 audit]
- **Stack**: Bun worker, SQLite, ChromaDB
- **Maturity**: 74,494 ★, last commit 2026-05-10 (active daily), 40 open issues
- **Install**: `npx claude-mem install` (preferred) or `/plugin marketplace add thedotmack/claude-mem`
- **Privacy**: local-only; data dir `~/.claude-mem` (configurable via `CLAUDE_MEM_DATA_DIR`); no telemetry; `<private>` tags strip sensitive content before storage

## Narrative

Claude-Mem solves the context-amnesia problem during multi-day algorithmic development cycles. It runs as a background Bun process, observing all Claude Code activity, compressing it into a Chroma vector database, and injecting relevant history on session start via a `SessionStart` hook.

### Integration vectors

- **Workflow (Adopt)**: Install via `/plugin marketplace add thedotmack/claude-mem` on the local macOS environment. Operates silently in background.
- **Cemini prod (No)**: Background terminal-observation plugins on the memory-constrained Hetzner host serve no trading purpose and introduce security vulnerabilities.
- **Wiki server (No)**: CPX21 already has Node.js + Ollama embeddings. Adding Bun + SQLite + Chroma duplicates functionality.

### Risks

- **Token efficiency paradox**: While designed to save context, dynamically injecting large arrays of historical memory vectors via SessionStart can rapidly accelerate API input token consumption. Must verify configurable injection limits.

### Resolved questions

- Injection-limit configurability [VERIFIED 2026-05-10 via Phase-0 audit]: `CLAUDE_MEM_SEMANTIC_INJECT_LIMIT` env var caps SessionStart injection to top-N most-relevant observations. Default: 5. Set in `/src/shared/SettingsDefaultsManager.ts:122`. Top-N semantic filtering structurally averts the token-efficiency paradox identified during ingest.

### Adoption status — INSTALLED at laptop level 2026-05-10 (v13.0.1)

`npx claude-mem install` completed cleanly on laptop. Marketplace registered at `~/.claude/plugins/marketplaces/thedotmack`, data dir `~/.claude-mem`, worker pid running, ChromaDB MCP supervisor process up.

Verified defaults (from production bundle `dist/npx-cli/index.js` `Z.DEFAULTS`):
- `CLAUDE_MEM_SEMANTIC_INJECT: "false"` (lazy injection — only on user-relevance match)
- `CLAUDE_MEM_SEMANTIC_INJECT_LIMIT: "5"` (top-N cap)
- `CLAUDE_MEM_CONTEXT_OBSERVATIONS: "50"` (worker observation buffer)
- `CLAUDE_MEM_CONTEXT_SESSION_COUNT: "10"` (rolling session memory)
- `CLAUDE_MEM_SKIP_TOOLS: "ListMcpResourcesTool,SlashCommand,Skill,TodoWrite,AskUserQuestion"` (no noise)
- Provider: `claude` via subscription auth
- Data dir: `~/.claude-mem` (default homedir; configurable via `CLAUDE_MEM_DATA_DIR`)

Known issue at install: Claude Desktop OAuth token stale (flagged in `~/.claude-mem/oauth-stale.marker`). Worker still runs; observation pipeline functional. Re-login via Claude Desktop will refresh.

Next-session verification (2026-05-11+): confirm `SessionStart` hook injects relevant observations on relevant prompts. Track via `http://localhost:37702` live activity dashboard.

[Source: Evaluating Links for Trading and Wiki Stacks.docx, URL 18]
