---
title: "Cross-Channel Agent Gateway"
type: concept
tags: [concept, architecture-pattern, mcp, cross-channel, telegram, discord, slack, whatsapp]
keywords: [cross-channel gateway, MCP-native agent, Telegram bot, Discord bot, lightweight agent, Go binary, side-channel alerts]
related:
  - sources/evaluating-code-for-trading-stacks.md
  - entities/tools/picobot.md
  - entities/tools/mercury-agent.md
  - concepts/mcp-tool-marketplace.md
  - concepts/cemini-deployment.md
maturity: draft
created: 2026-05-10
updated: 2026-05-10
---

## Relations
- `@sources/evaluating-code-for-trading-stacks.md` — pattern derived from URLs 3 + 4
- `@entities/tools/picobot.md` — production-ready Go instance of this pattern
- `@entities/tools/mercury-agent.md` — Node.js reference instance (Steal-from)
- `@concepts/mcp-tool-marketplace.md` — gateway delegates to MCP servers for tool execution
- `@concepts/cemini-deployment.md` — where this pattern slots into the trading stack

## Raw Concept

The cross-channel agent gateway pattern names a recurring architectural shape: a lightweight, network-attached agent process that bridges human-facing messaging channels (Telegram, Discord, Slack, WhatsApp) to a backend tool execution surface (MCP servers, FastMCP, programmatic LLM endpoints) — without coupling the production trading/research orchestrator to async polling loops or platform SDKs.

## Narrative

### The problem

Trading stacks and research workflows benefit from out-of-band communication:
- **Outbound**: critical alerts (risk limit breaches, position-size warnings, ingest failures) to operator's phone
- **Inbound**: admin overrides, ad-hoc research queries, status interrogation from mobile

The naive solution embeds Telegram/Discord SDKs directly into the production Python orchestrator. This pollutes the orchestrator with:
- Async event-loop logic (poll-vs-webhook complexity)
- Platform-specific authentication state
- Rate-limit handling for each channel
- Update/migration burden as platform APIs evolve

Critically, it couples the trading hot path to potentially-stalling network I/O on consumer messaging APIs.

### The pattern

A **gateway process** lives between channels and orchestrator:

```
[Telegram / Discord / Slack / WhatsApp]
        ↓ (channel-specific protocols)
   ┌─────────────────────────┐
   │   Cross-Channel Gateway │   ← lightweight, isolated process
   │   (e.g. picobot)        │
   └─────────────────────────┘
        ↓ (MCP / FastMCP / HTTP)
   [Trading Orchestrator / Research Layer]
```

Key properties:
1. **Process-isolated** — separate Docker container, separate failure domain
2. **MCP-native** — speaks Model Context Protocol downstream; channel-protocols upstream
3. **Stateless or thin-stateful** — credentials + routing tables only, no business logic
4. **Lightweight** — ideally sub-50 MB resident; Go binary or compiled language preferred over Node/Python runtime drag

### Instances catalogued

| Instance | Language | Resident RAM | License | Status |
|----------|----------|-------------:|---------|--------|
| picobot | Go (static binary) | <25 MB | MIT | **Adopt (K36)** |
| mercury-agent | Node.js daemon | 80–150 MB | MIT | Steal-from |

**Why picobot wins for production**: smaller footprint, no runtime, MCP-native client built-in, pure-Go SQLite (no CGO).

**Why mercury-agent is worth mining**: permission-hardened shell-exec layer + SQLite FTS5 memory schema are independently valuable; translate to Python and integrate into FastMCP.

### Cemini significance

This pattern operationalizes the long-standing requirement to surface trading alerts to a mobile device + accept admin overrides without bloating the Python production stack. Picobot adoption directly retires the alternative of embedding `python-telegram-bot` into `agents/orchestrator.py`.

### Anti-patterns

- **Don't embed channel SDKs into trading code** — mixes consumer-API rate-limit logic with trade-execution latency budgets
- **Don't write a Python-based gateway** — adds another async event-loop process to a stack already heavy with LangGraph + FastMCP loops
- **Don't centralize state in the gateway** — keep it routing-only; persistent context belongs in PostgreSQL/pgvector, not in `~/.mercury/memory/` SQLite

### Open questions

- How does picobot handle WhatsApp's session-state churn (whatsmeow + pure-Go SQLite) under multi-channel concurrent writes? [NEEDS VERIFICATION 2026-05-10]
- What's the right authentication/authorization model when admin overrides arrive via Telegram — Telegram user ID allowlist + per-tool capability check?

[Sources: Evaluating Code for Trading Stacks.docx URL 3 (mercury-agent), URL 4 (picobot)]
