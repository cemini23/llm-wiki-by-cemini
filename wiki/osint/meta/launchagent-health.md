---
title: LaunchAgent health — Cemini laptop automation
type: concept
tags: [meta, ops, launchagent, harness]
keywords: [launchagent, heartbeat, wiki-ingester, claude-mem, digest]
related:
  - meta/daily-research-digest-cadence.md
  - meta/federation-operator-hub-stub.md
  - concepts/file-keep-wire-harness.md
  - sources/super-audit-ai-harness-2026-09-02.md
maturity: draft
created: 2026-09-02
updated: 2026-09-02
---

## Relations

@meta/daily-research-digest-cadence.md · @meta/federation-operator-hub-stub.md · @concepts/file-keep-wire-harness.md · @sources/super-audit-ai-harness-2026-09-02.md

## Raw Concept

Prompted by super-audit Phase B (`reports/audit/premium-ai-harness-20260902/SYNTHESIS.md`). ~20 `com.cemini.*` LaunchAgents; several fail silently without stderr paths or operator review.

## Narrative

### Active (expected)

| Label | Schedule | Log | Purpose |
|-------|----------|-----|---------|
| `com.cemini.daily-research-digest` | 08:00 | `~/Library/Logs/cemini-daily-digest.log` | OSINT daily sweep |
| `com.cemini.daily-research-digest.*` | 08:10+ stagger | same family | Sibling wiki digests |
| `com.cemini.federation-morning-summary` | ~08:28 | `cemini-federation-summary.log` | Hub morning table |
| `com.cemini.inbox-notify` | WatchPaths | `cemini-inbox-watch.log` | Inbox drop alert |
| `com.cemini.prod-mcp-tunnel` | KeepAlive | tunnel log | Prod MCP localhost |
| `com.cemini.openrouter-cache-proxy` | KeepAlive | proxy log | Route cache / log |
| `com.cemini.wiki-gap-detect` | weekly | gap log | Tier-1 gap list |

### Disabled / operator-gated

| Label | Status | Reason |
|-------|--------|--------|
| `com.cemini.wiki-ingester` | **Unloaded** (2026-09-02) | Grok Build **402** weekly quota; Tier-3 ingest needs HITL. Re-enable with `CEMINI_ENABLE_WIKI_INGESTER=1` + balance reset. Plist renamed `*.disabled-*`. |
| `com.cemini.wiki-sync-verify` | `.disabled` | Librarian decommission |

### Broken — fix or unload

| Label | Symptom | Fix |
|-------|---------|-----|
| `com.cemini.claude-mem-worker` | `Cannot find module 'zod/v3'` in claude-mem 13.16.1 | Run `bun install` in `~/.claude/plugins/cache/thedotmack/claude-mem/13.16.1` or bootout until plugin updates. Watchdog respawns — unload both if not using claude-mem. |

### Ollama

**Not installed** — operator storage constraint. Super-audit runs 5-model (no free local slot). Acceptable.

### Operator rituals

```bash
launchctl list | grep cemini
tail -20 ~/Library/Logs/cemini-*.log
bash scripts/reinstall_morning_launchagents.sh   # reload digest schedule; wiki-ingester off by default
```

Reinstall script: `scripts/reinstall_morning_launchagents.sh`. Wiki-ingester wrapper: `scripts/run_wiki_ingester_grok_cli.sh` (manual dry-run only until HITL).

## Snippets

[Source: super-audit 2026-09-02 — LaunchAgent fix #6 in SYNTHESIS.md]

## Dead Ends

- Treating Grok 402 as auth/login — weekly Build quota resets; `grok login` does not fix 402.
