---
title: godot-ai-playtest Phase-0 audit — 2026-06-13
type: source
tags: [source, phase-0, godot, playtest, audit]
keywords: [godot-ai-playtest, tcp, json-rpc, automation]
related:
  - entities/tools/godot-ai-playtest.md
  - entities/tools/godot-stagehand.md
read_status: read
source_type: operator-audit
source_url: https://github.com/marcushale/godot-ai-playtest
maturity: validated
created: 2026-06-13
updated: 2026-06-13
---

## Raw Concept

Phase-0 audit of **marcushale/godot-ai-playtest** — TCP JSON-RPC plugin for external Godot control.

## Narrative

### Method

Clone @ main (2026-04-01) to `/tmp/phase0-audit/godot-ai-playtest`.

### Checks

| Gate | Result |
|------|--------|
| License | **MIT** [CONFIRMED] |
| Maturity | Small (~3★), PyPI package, v0.4.0 release |
| Transport | TCP :9876 JSON-RPC (in-game plugin) |
| Scope | Integration tests, AI agent control, CI screenshots — **not** unit tests (use GUT/gdUnit4) |
| Failure modes | TCP port exposed when plugin enabled — strip from export builds |

### vs godot-stagehand

| | ai-playtest | stagehand |
|---|-------------|-----------|
| Protocol | JSON-RPC TCP | WebSocket + MCP |
| MCP native | No (Python client) | Yes |
| Maturity | Lower stars | More MCP/CI docs |

### Verdict

**CONDITIONAL-GO** — WATCH alternative to stagehand; pick **one** automation stack at W2 to avoid dual TCP/WS ports.

## Snippets

`pip install godot-ai-playtest` — Python client for CI scripts.
