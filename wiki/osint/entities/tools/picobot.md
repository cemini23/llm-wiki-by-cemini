---
title: "Picobot — Ultra-Lightweight MCP-Native Cross-Channel Agent (Go)"
type: entity
tags: [tool, mcp, agent, go, cross-channel, telegram, discord, slack, whatsapp, cemini-prod-candidate]
keywords: [picobot, MCP, cross-channel agent, Go binary, Telegram, Discord, WhatsApp, lightweight agent, alpine docker]
related:
  - sources/evaluating-code-for-trading-stacks.md
  - concepts/cross-channel-agent-gateway.md
  - concepts/mcp-tool-marketplace.md
  - concepts/cemini-license-posture.md
  - concepts/tool-evaluation-framework.md
  - entities/tools/mercury-agent.md
maturity: draft
created: 2026-05-10
updated: 2026-05-10
---

## Relations
- `@sources/evaluating-code-for-trading-stacks.md` — source evaluation brief (URL 4)
- `@concepts/cross-channel-agent-gateway.md` — pattern picobot exemplifies
- `@concepts/mcp-tool-marketplace.md` — picobot is MCP-client-native
- `@concepts/cemini-license-posture.md` — MIT, IP-sale clean
- `@entities/tools/mercury-agent.md` — parallel Node.js implementation (Steal-from)

## Raw Concept

Picobot is an ultra-lightweight, self-hosted AI agent compiled as a single, statically linked Go binary. Designed for absolute portability and execution speed on severely constrained hardware (e.g., $5/month VPS, Termux on Android).

- **Repo**: `github.com/louisho5/picobot`
- **License**: MIT [NEEDS VERIFICATION 2026-05-10]
- **Stack**: Pure Go, zero CGO dependencies
- **Maturity**: v0.2.0 [NEEDS VERIFICATION 2026-05-10]
- **Binary size**: ~9 MB
- **Runtime RAM**: <25 MB resident under load (estimate)
- **Channels**: Telegram, Discord, Slack, WhatsApp (via whatsmeow + modernc.org/sqlite)
- **MCP support**: native client — delegates tool execution to external MCP servers

## Narrative

Picobot solves the persistent cross-channel agent communication problem with extreme efficiency. Where most agent frameworks ship as bloated Python or Node.js daemons, picobot is a single ~9 MB Go binary with native MCP client support.

### Integration vectors

**Cemini prod (Adopt — ✅)**: Deploy as isolated `alpine:3.20` Docker container in existing `docker-compose.yml`. Configure `mcpservers` block to point at Cemini's FastMCP endpoints. Elegantly solves Telegram/Discord alerts + admin overrides without bloating the Python orchestrator with async polling loops.

**Wiki server (Adopt — ✅)**: Install on Hetzner CPX21 directly. Configure to query `llmwiki serve` MCP endpoint via Telegram input. Near-zero RAM footprint preserves headroom (Ollama + embedding models already consume ~1 GB of the 4 GB envelope).

**Workflow laptop (Partial — ⚠️)**: Server-oriented infrastructure, but Go source code is worth reading for raw Telegram Bot API handling patterns (no bloated third-party SDKs).

### Risks

- **whatsmeow + modernc.org/sqlite**: pure-Go SQLite port has occasionally different concurrent write-lock characteristics vs canonical C-SQLite. Profile under multi-channel concurrent load before declaring production-ready.
- **Maturity (v0.2.0)**: skill API + state migrations may experience breaking changes. Pin to specific commit at install; re-verify on minor version bumps.
- **MIT license**: assertion from source brief; **Phase-0 audit required before prod commit** per Cemini license-posture policy.

### Cemini significance

Adopts cleanly across **two surfaces** (Cemini prod + wiki server). Resolves cross-channel communication architectural problem without language friction (Go binary, no Python/Node runtime drag). The MCP-client-native design means picobot inherits whatever tool surface FastMCP exposes — no separate integration per channel.

### Phase-0 audit checklist

- [ ] Clone to `/tmp/picobot-audit/`; verify LICENSE = MIT
- [ ] Confirm v0.2.0 latest tag + commit recency
- [ ] Inspect `modernc.org/sqlite` lock behavior under simulated concurrent Telegram + Discord writes
- [ ] Verify MCP client implementation matches stdio MCP standard (not custom protocol)
- [ ] Profile resident RAM under 1000-message/hour synthetic load

[Source: Evaluating Code for Trading Stacks.docx, URL 4]
