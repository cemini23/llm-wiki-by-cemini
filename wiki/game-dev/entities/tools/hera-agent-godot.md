---
title: hera-agent-godot — low-token CLI editor control
type: entity
tags: [entity, tool, godot, agent, cli, phase-0]
keywords: [hera-agent-godot, notnull92, cli, low-token, editor]
related:
  - entities/tools/godot-mcp-landscape.md
  - entities/tools/godot-stagehand.md
  - entities/tools/hi-godot-ai.md
  - entities/tools/godot-ai-playtest.md
  - concepts/agent-harness-castle-project.md
  - concepts/godot-stagehand-ci-smoke-plan.md
  - concepts/ai-game-dev-tool-stack-2026.md
  - entities/projects/castle-sim.md
  - sources/hera-agent-godot-phase-0-audit-2026-06-26.md
  - sources/notnull92-hera-agent-godot-devto-2026-06-25.md
  - sources/godot-47-release-shelf-2026-06-25.md
maturity: validated
created: 2026-06-26
updated: 2026-06-26
---

## Relations

- @entities/tools/godot-mcp-landscape.md — CLI alt to MCP schema bloat
- @sources/hera-agent-godot-phase-0-audit-2026-06-26.md — audit trail

## Raw Concept

**NotNull92/hera-agent-godot** — MIT Go CLI + Godot 4.7+ `@tool` addon. Agents inspect/control **live editor** via compact JSON shell commands instead of MCP tool schemas.

## Narrative

### Phase-0 audit (2026-06-26)

| Check | Result |
|-------|--------|
| License | MIT [CONFIRMED] |
| Maturity | Early (~2★); core commands complete per README |
| Godot | **4.7+ required** — pin gate for castle-sim |
| Verdict | **CONDITIONAL-GO** — W2 verify alt after 4.7 bump |

### When to use (castle-sim W2)

| Prefer Hera | Prefer stagehand / hi-godot-ai |
|-------------|-------------------------------|
| Codex/Cursor shell stories, minimal context | MCP-integrated Cursor session |
| Low-token `smoke` + error log loop | WebSocket gameplay automation |
| Quick screenshot + runtime assert | Long-running CI driver |

### Security

Write-capable — sandbox clone only until @ccc-wiki skill-vetting + @cybersecurity-wiki MCP posture satisfied.

## Snippets

```bash
curl -fsSL https://raw.githubusercontent.com/NotNull92/hera-agent-godot/main/install.sh | sh
hera status
hera run --current --wait
hera output --type error
```

## Dead Ends

- Install on castle-sim before Godot 4.7 pin + story-029 regression re-run
