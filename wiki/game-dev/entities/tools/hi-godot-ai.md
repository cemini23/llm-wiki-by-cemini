---
title: hi-godot/godot-ai — Godot MCP server and plugin
type: entity
tags: [entity, tool, godot, mcp, ai, phase-0]
keywords: [godot-ai, hi-godot, mcp, plugin, asset-library]
related:
  - concepts/ai-game-dev-tool-stack-2026.md
  - entities/tools/godot-mcp-landscape.md
  - entities/engines/godot-4.md
  - concepts/agent-harness-castle-project.md
  - sources/hi-godot-ai-phase-0-audit-2026-06-13.md
  - entities/tools/sods2-godot-mcp.md
  - entities/tools/ziva-godot-agent.md
  - entities/tools/gamedevbench.md
  - sources/gamedevbench-phase-0-audit-2026-06-21.md
  - sources/ziva-godot-agent-phase-0-audit-2026-06-21.md
maturity: validated
created: 2026-06-13
updated: 2026-06-21
---

## Relations

- @cybersecurity-wiki/concepts/mcp-security-posture.md
- @ccc-wiki/concepts/skill-vetting.md
- @sources/hi-godot-ai-phase-0-audit-2026-06-13.md — audit trail

## Raw Concept

Most mature open **Godot + MCP** integration (hi-godot/godot-ai). Phase-0 complete 2026-06-13.

## Narrative

### Phase-0 audit (2026-06-13)

| Check | Result |
|-------|--------|
| License | MIT [CONFIRMED] |
| Maturity | ~500★, Godot Asset Library, CI, releases through Jun 2026 |
| Godot | 4.3+ (4.4+ recommended) |
| Endpoint | `http://127.0.0.1:8000/mcp` localhost |
| Surface | ~41 MCP tools — node/scene/script **writes**, batch_execute, project_run |
| castle-sim M0 | **Do not install** — wiki spec + Cursor only |

### Adoption path (W2)

1. Sandbox clone of `castle-sim`
2. Read-only tools first (`editor_state`, `scene_get_hierarchy`)
3. Human-reviewed writes only
4. MCP security checklist passed

| Verdict | **CONDITIONAL-GO** at W2 harness — not before M0 spike ships |

## Snippets

Asset Library: https://godotengine.org/asset-library/asset/5050
