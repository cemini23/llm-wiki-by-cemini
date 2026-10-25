---
title: "Mercury Agent — Background-Capable AI Daemon (Node.js)"
type: entity
tags: [tool, steal-from, agent, daemon, sqlite-fts5, agent-skills, mit-license]
keywords: [Mercury, autonomous agent, systemd, LaunchAgent, Telegram, SQLite FTS5, second brain, permission-hardening, Agent Skills spec]
related:
  - sources/evaluating-code-for-trading-stacks.md
  - concepts/cross-channel-agent-gateway.md
  - concepts/tool-evaluation-framework.md
  - entities/tools/picobot.md
maturity: draft
created: 2026-05-10
updated: 2026-05-10
---

## Relations
- `@sources/evaluating-code-for-trading-stacks.md` — source evaluation brief (URL 3)
- `@concepts/cross-channel-agent-gateway.md` — Mercury and picobot exemplify two paths
- `@entities/tools/picobot.md` — production-ready Go alternative

## Raw Concept

Mercury is an autonomous AI agent running as a background daemon (systemd / LaunchAgent / Windows Task Scheduler). Behavior defined via user-owned Markdown skill files (Agent Skills spec). Persistent "Second Brain" via local SQLite + FTS5. Routes LLM traffic through DeepSeek / OpenAI.

- **Repo**: `github.com/cosmicstack-labs/mercury-agent`
- **License**: MIT [NEEDS VERIFICATION 2026-05-10]
- **Stack**: Node.js
- **Memory**: SQLite with FTS5 (full-text search), `~/.mercury/memory/`
- **Channels**: CLI + Telegram

## Narrative

**Recommendation: Steal-from, not adopt.** Mercury introduces unnecessary Node.js daemon into a Python-rigid orchestration stack (LangGraph + FastMCP). Cross-channel concerns are better served by picobot (Go, MCP-native, smaller).

### Patterns worth stealing

1. **Permission-hardened shell exec layer** — sanitization + serialization logic for executing shell commands and routing outputs back to LLM context without prompt-injection vulnerabilities. Translate to Python; integrate into FastMCP shell-tool wrapper.
2. **SQLite FTS5 memory schema** — local persistent context store with FTS indexing. Reference design; Cemini's PostgreSQL/pgvector covers production but FTS5 pattern useful for laptop-local context.
3. **Agent Skills spec adherence** — Markdown-defined agent behavior aligns with Cemini's own skill catalog approach. Cross-pollinate spec compliance.

### Why not adopt the daemon

- Node.js daemon scatters orchestration logic across two languages (Python + Node)
- SQLite FTS5 memory siloed from production PostgreSQL/pgvector → fragmented intelligence
- Cross-channel routing problem already solved better by picobot

### Risks (if stealing code)

- **License verification**: confirm MIT before importing any extracted code
- **Shell-exec layer**: verify exact sanitization approach handles ANSI escape pollution + ensures no prompt-injection vector remains
- **Resident RAM**: source brief notes profiling gap during heavy Telegram polling + concurrent SQLite writes [OPEN QUESTION 2026-05-10]

[Source: Evaluating Code for Trading Stacks.docx, URL 3]
