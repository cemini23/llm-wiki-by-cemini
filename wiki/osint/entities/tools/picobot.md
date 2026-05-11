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
maturity: validated
created: 2026-05-10
updated: 2026-05-10
phase_0_audit: GO (2026-05-10)
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
- **License**: **MIT [CONFIRMED 2026-05-10]** — Phase-0 audit: LICENSE file is standard MIT boilerplate
- **Stack**: Pure Go, zero CGO dependencies **[CONFIRMED 2026-05-10]** — `go.mod` requires `modernc.org/sqlite v1.46.1` (pure-Go SQLite); `mattn/go-sqlite3` appears only as transitive of color libs
- **Maturity**: **v0.2.0 [CONFIRMED 2026-05-10]** — 86 commits, last push 2026-03-28 (~6 weeks pre-audit), tags v0.1.0-beta → v0.2.0, 1.2k stars, 3 open issues
- **Binary size**: ~9 MB (README claim; needs runtime verification on Alpine build)
- **Runtime RAM**: ~10 MB idle (README claim line 6); needs `ps -o rss` capture during prod soak
- **Channels**: Telegram, Discord, Slack, WhatsApp **[CONFIRMED 2026-05-10]** — whatsmeow pure-Go (no Java/Kotlin bridges)
- **MCP support**: native stdio client **[CONFIRMED 2026-05-10]** — `internal/mcp/client.go:34-50` implements `NewStdioClient()` per MCP spec; Streamable HTTP transport also supported

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

### Phase-0 audit findings (2026-05-10) — **GO**

- [x] LICENSE = MIT confirmed (top-level)
- [x] v0.2.0 latest tag; 86 commits; last push 2026-03-28; 1.2k stars; 3 open issues
- [x] Pure-Go SQLite (`modernc.org/sqlite v1.46.1`) — no CGO, Alpine-distributable
- [x] MCP stdio client per spec (`internal/mcp/client.go:34-50`); HTTP transport fallback exists
- [x] Cross-channel implementations all use modern, maintained libraries (discordgo v0.28.1, slack-go v0.14.0, whatsmeow pure-Go)
- [ ] **Deferred (post-deploy)**: binary size verification on Alpine `go build -ldflags="-s -w"`
- [ ] **Deferred (post-deploy)**: RAM profile under 1000-msg/hr synthetic load
- [ ] **Deferred (post-deploy)**: whatsmeow stability monitoring (WebSocket reverse-eng has platform-blocking history)

**Verdict**: GO ✅ — proceed to production adoption brief.

[Source: Evaluating Code for Trading Stacks.docx, URL 4]
[Audit: Phase-0 Explore agent, 2026-05-10]
