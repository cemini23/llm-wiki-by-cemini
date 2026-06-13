---
title: Agent + Godot MCP tooling landscape (2026)
type: entity
tags: [entity, tool, agent, godot, mcp]
keywords: [mcp, godot, llm, agent, codegen, hi-godot]
related:
  - concepts/agent-harness-castle-project.md
  - concepts/ai-game-dev-tool-stack-2026.md
  - entities/tools/hi-godot-ai.md
  - entities/tools/sods2-godot-mcp.md
  - entities/tools/godot-stagehand.md
  - entities/tools/godot-ai-playtest.md
  - sources/hi-godot-ai-phase-0-audit-2026-06-13.md
  - sources/sods2-godot-mcp-phase-0-audit-2026-06-13.md
  - sources/godot-stagehand-phase-0-audit-2026-06-13.md
  - sources/godot-ai-playtest-phase-0-audit-2026-06-13.md
maturity: validated
created: 2026-06-13
updated: 2026-06-13
---

## Relations

- @cybersecurity-wiki/concepts/mcp-security-posture.md
- @concepts/ai-game-dev-tool-stack-2026.md

## Raw Concept

Comparative landscape of Godot + LLM/MCP and automation tools — **Phase-0 audits complete 2026-06-13**.

## Narrative

### Phase-0 summary

| Tool | Verdict | When |
|------|---------|------|
| @entities/tools/hi-godot-ai.md | **CONDITIONAL-GO** | W2 editor MCP (sandbox) |
| @entities/tools/sods2-godot-mcp.md | **CONDITIONAL-GO** | W2 alt if Node/debugger needed |
| @entities/tools/godot-stagehand.md | **CONDITIONAL-GO** | W2 CI smoke (preferred automation) |
| @entities/tools/godot-ai-playtest.md | **CONDITIONAL-GO** | W2 alt — pick one with stagehand |
| Farraskuy/Godot-MCP (168 tools claimed) | **NO-GO** | Unverified; skip |
| funplay, dreamer568, etc. | **WATCH** | No Phase-0 |

### Default (M0–M1)

**Cursor + markdown spec** — no MCP write tools on `castle-sim` until M0 pathfinding spike passes.

### Security bar (all MCP)

1. @ccc-wiki skill-vetting
2. @cybersecurity-wiki MCP posture
3. localhost binding verified
4. Sandbox project before production repo

## Snippets

Audit clones: `/tmp/phase0-audit/{godot-ai,godot-mcp,godot-stagehand,godot-ai-playtest}`
