---
name: discord-ops
description: Use discord-ops MCP for Cemini/OSINT or youratto Discord admin (channels, webhooks, roles). Trigger when the operator asks Cursor to edit Discord server layout, create webhooks for #ops, or apply hybrid support channels. Default dry-run until LIVE OK.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
---

# discord-ops MCP (OSINT + youratto)

David’s TipDrop kit uses the same tool: **discord-ops** (`npx discord-ops@latest`) — agent-controlled Discord admin (channels/webhooks/roles), not a chat bridge.

## Projects (`~/.discord-ops.json`)

| Key | Use |
|-----|-----|
| `youratto` | youratto.com support/community server |
| `osint` | Optional Cemini/OSINT ops guild (may share bot + guild) |

## Setup (once)

```bash
bash scripts/setup_discord_ops_macos.sh
```

Then: quit Cursor → reopen → MCP → enable **discord-ops**.

## Operating rules

1. `DISCORD_OPS_DRY_RUN=true` by default. Mutations need explicit **LIVE OK**.
2. Never paste tokens/webhooks into chat. Tokens live in `~/.cemini/discord-ops.env` (0600).
3. Prefer TipDrop-style channel/webhook tools first; expand tool list only if needed.
4. For youratto layout + PII/UPL: read `briefs/2026-07-23_youratto-discord-support-runbook.md` (atto + OSINT mirrors).
5. Self-bots / user-token scrapers are **forbidden** (wiki: Telegram/Discord research + TipDrop K133).

## Skill sibling

Atto-focused prompts: `youratto-discord-ops` in the atto repo `.cursor/skills/`.
