---
title: Sods2/godot-mcp Phase-0 audit — 2026-06-13
type: source
tags: [source, phase-0, godot, mcp, audit]
keywords: [sods2, godot-mcp, typescript, phase-0]
related:
  - entities/tools/godot-mcp-landscape.md
  - entities/tools/hi-godot-ai.md
read_status: read
source_type: operator-audit
source_url: https://github.com/Sods2/godot-mcp
maturity: validated
created: 2026-06-13
updated: 2026-06-13
---

## Raw Concept

Phase-0 audit of **Sods2/godot-mcp** — Node.js MCP server + Godot editor TCP plugin (77 tools).

## Narrative

### Method

Clone @ main (2026-04-12) to `/tmp/phase0-audit/godot-mcp`.

### Checks

| Gate | Result |
|------|--------|
| License | **MIT** [CONFIRMED] |
| Maturity | New (low stars), CI workflow present |
| Tools | 77 across 15 categories — file delete/rename, scene edit, debugger, export |
| Architecture | Node MCP stdio + editor plugin TCP `127.0.0.1:6008`; hybrid file fallback without editor |
| Failure modes | **Broad write + delete** surface; file ops work even without editor running |

### vs hi-godot/godot-ai

| | Sods2/godot-mcp | hi-godot/godot-ai |
|---|-----------------|-------------------|
| Stars | Low | ~500 |
| Stack | Node/TS | Python + GDScript plugin |
| Tool count | 77 named | ~41 MCP / 120 ops |
| Asset Library | No | Yes |

### Verdict

**CONDITIONAL-GO** — viable alternative to hi-godot if Node stack preferred; **same security bar** — sandbox only, no delete tools until trusted. Prefer **hi-godot** for maturity unless Sods2 features required (debugger breakpoints).

## Snippets

Install: `npm install && ./scripts/install.sh` — targets Claude Code `.mcp.json`.
