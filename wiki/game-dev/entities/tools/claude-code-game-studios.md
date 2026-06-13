---
title: Claude-Code-Game-Studios — role graphs (steal-from)
type: entity
tags: [entity, tool, claude-code, multi-agent, steal-from]
keywords: [claude-code-game-studios, role-graph, planner, implementer, ccgs]
related:
  - concepts/agent-harness-castle-project.md
  - concepts/ccgs-workflow-extraction.md
  - concepts/ai-assisted-game-dev-workflows.md
  - concepts/ai-game-dev-tool-stack-2026.md
  - concepts/game-dev-wiki-scope.md
  - entities/engines/godot-4.md
  - sources/ccgs-workflow-catalog-2026.md
  - sources/starlog-ccgs-49-agents-2026.md
  - sources/claude-code-game-studios-phase-0-audit-2026-06-13.md
maturity: validated
created: 2026-06-13
updated: 2026-06-13
cross-wiki-source: @ccc-wiki/entities/tools/claude-code-game-studios.md
---

## Relations

- @ccc-wiki/entities/tools/claude-code-game-studios.md — canonical CCC entity
- @concepts/ccgs-workflow-extraction.md — **deep extraction + Cursor port guide**

## Raw Concept

[`Donchitos/Claude-Code-Game-Studios`](https://github.com/Donchitos/Claude-Code-Game-Studios) — MIT virtual game studio for **Claude Code**: 49 agents, 73 skills, 7-phase workflow with artifact gates. ~21k★ (2026-06).

## Narrative

### Components [CONFIRMED — repo API + workflow-catalog]

| Asset | Count | Location |
|-------|-------|----------|
| Agents | 49 | `.claude/agents/*.md` |
| Skills | 73 | `.claude/skills/*/SKILL.md` |
| Phases | 7 | `.claude/docs/workflow-catalog.yaml` |
| Engine refs | Godot, Unity, UE | `docs/engine-reference/` |

### Why it exists [CONFIRMED — README]

Single AI chat lacks studio discipline — no design review, QA, or scope veto. CCGS adds **structure as code**.

### Steal-for castle-sim (Cursor path)

Full install requires Claude Code. **Extract instead:**

| Steal | Skip |
|-------|------|
| Phase + artifact model (@sources/ccgs-workflow-catalog-2026.md) | All 49 agent files verbatim |
| P0 skills: brainstorm, map-systems, vertical-slice, dev-story | Unity/UE specialist agents |
| game-designer collaboration protocol (ask → options → approve writes) | Git hooks until repo mature |
| PROCEED/PIVOT/KILL vertical slice gate | 72-skill learning curve upfront |

Detailed port: @concepts/ccgs-workflow-extraction.md

### Godot agents in roster

godot-gdscript-specialist, godot-csharp-specialist, godot-shader-specialist, godot-gdextension-specialist, godot-specialist — map to Codex swarms on `castle-sim/`.

### Forks

- [OpenCode Game Studios](https://github.com/striderZA/OpenCodeGameStudios) — phase gates, OpenCode port

| Verdict | **STEAL-FROM** — @concepts/ccgs-workflow-extraction.md is the operator guide |

### Phase-0 audit (2026-06-13)

| Check | Result |
|-------|--------|
| License | MIT |
| Install target | Claude Code only — **NO-GO** full install in Cursor |
| Pattern extraction | **GO** — see @sources/claude-code-game-studios-phase-0-audit-2026-06-13.md |

## Snippets

Upstream: `npx` / clone into Claude Code project; not compatible with Cursor out of box.

Phase-0 before any install: @ccc-wiki/concepts/skill-vetting.md
