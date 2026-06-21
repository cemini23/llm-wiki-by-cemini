---
title: Agent harness — castle sim project
type: concept
tags: [concept, agents, harness, codex, opus, fable]
keywords: [agent-swarm, codex, opus, fable, planner, executor, milestone-gates]
related:
  - concepts/game-dev-wiki-scope.md
  - concepts/vertical-slice-v0.md
  - concepts/indie-kingdom-builder-lessons.md
  - concepts/ai-assisted-game-dev-workflows.md
  - concepts/ai-game-dev-tool-stack-2026.md
  - concepts/ccgs-workflow-extraction.md
  - concepts/godot-stagehand-ci-smoke-plan.md
  - entities/tools/godot-stagehand.md
  - entities/tools/gamedevbench.md
  - sources/gamedevbench-phase-0-audit-2026-06-21.md
  - entities/tools/claude-code-game-studios.md
  - entities/tools/godot-mcp-landscape.md
  - meta/sibling-wiki-inventory.md
  - sources/bootstrap-game-dev-wiki-2026-06-13.md
  - entities/projects/castle-sim.md
  - concepts/game-ai-rl-augmentation-shelf.md
  - sources/arxiv-2606.20210-augmenting-game-ai-drl-2026-06-20.md
  - entities/tools/hi-godot-ai.md
  - entities/tools/ziva-godot-agent.md
  - sources/ziva-godot-agent-phase-0-audit-2026-06-21.md
maturity: draft
created: 2026-06-13
updated: 2026-06-21
---

## Relations

- @concepts/ai-assisted-game-dev-workflows.md — **general** AI game dev patterns (any project)
- @concepts/ai-game-dev-tool-stack-2026.md — MCP, automation, CCGS catalog
- @ccc-wiki/entities/tools/claude-code-game-studios.md — role graph steal-from
- @ccc-wiki/concepts/ship-subagent-writer-reviewer-tester.md — writer + tester → reviewer gate
- @ccc-wiki/concepts/agent-completion-verification-gates.md — done = tests + playtest
- @ccc-wiki/entities/patterns/scatter-gather.md — parallel Godot subsystems
- @ccc-wiki/concepts/skill-vetting.md — before untrusted skills
- @cybersecurity-wiki/concepts/mcp-security-posture.md — MCP admission (W2+)
- @cybersecurity-wiki/concepts/agent-skill-injection.md — SKILL.md poisoning
- @meta/sibling-wiki-inventory.md — full cross-wiki map

## Raw Concept

Model matrix and milestone gates for agent-assisted hobby game dev. Research phase uses wiki; execution phase uses per-slice Codex swarms.

## Narrative

### Roles

| Role | Model (2026-06-13) | Fallback when Fable returns |
|------|-------------------|----------------------------|
| **Planner / designer** | `claude-opus-4-8-thinking-high` | `claude-fable-5-thinking-high` |
| **Implementer swarm** | `gpt-5.3-codex` | same |
| **Third lens** | `gemini-3.1-pro` | art/spec review |

Fable withdrawn from Cursor subagents 2026-06-13 — Opus is default planner. [CONFIRMED — @ccc-wiki cursor-audit reference]

### Per-milestone workflow

1. **Research** — ingest sources into this wiki; update slice spec
2. **Plan** — Opus writes task breakdown in `briefs/` (gitignored) from wiki spec — use CCGS P0 skills as checklist (@concepts/ccgs-workflow-extraction.md)
3. **Execute** — Codex subagents implement **one subsystem** in `castle-sim` repo (`/dev-story` equivalent)
4. **Verify** — operator playtest + automated lint/tests; `PROCEED/PIVOT/KILL` on M0/M1 (@concepts/vertical-slice-v0.md)
5. **Promote** — update concept maturity when slice criteria pass

### Anti-patterns

- One prompt → full RTS
- Executor agents changing scope without planner pass
- Skipping playtest gate

### Steal-from

`Donchitos/Claude-Code-Game-Studios` — planner / implementer / reviewer edges only (`@entities/tools/claude-code-game-studios.md`).

## Snippets

> OMC-style game-dev case study pattern: Sonnet/Opus logic + Gemini art — validated for narrow vertical slices, not full Stronghold. [TENTATIVE — @osint-wiki/sources/omc-talent-container-paper.md]
