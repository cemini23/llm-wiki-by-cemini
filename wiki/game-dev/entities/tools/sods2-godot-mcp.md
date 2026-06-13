---
title: Sods2/godot-mcp — Node MCP server for Godot IDE
type: entity
tags: [entity, tool, godot, mcp, node, phase-0]
keywords: [sods2, godot-mcp, typescript, mcp]
related:
  - entities/tools/godot-mcp-landscape.md
  - entities/tools/hi-godot-ai.md
  - sources/sods2-godot-mcp-phase-0-audit-2026-06-13.md
maturity: validated
created: 2026-06-13
updated: 2026-06-13
---

## Relations

- @sources/sods2-godot-mcp-phase-0-audit-2026-06-13.md

## Raw Concept

TypeScript MCP server (77 tools) + Godot editor TCP plugin. Phase-0 complete 2026-06-13.

## Narrative

### Phase-0 audit (2026-06-13)

| Check | Result |
|-------|--------|
| License | MIT |
| Tools | Scene/script/debug/export/**file delete** |
| Editor TCP | 127.0.0.1:6008 |
| vs hi-godot | Lower maturity; broader debugger tooling |

| Verdict | **CONDITIONAL-GO** — secondary to hi-godot unless Node/debugger features needed |

## Snippets

https://github.com/Sods2/godot-mcp
