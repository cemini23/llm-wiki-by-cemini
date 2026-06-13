---
title: Agent harness — castle sim project
type: concept
tags: [concept, agents, harness, codex, opus, fable]
keywords: [agent-swarm, codex, opus, fable, planner, executor, milestone-gates]
related:
  - concepts/game-dev-wiki-scope.md
  - concepts/vertical-slice-v0.md
  - entities/tools/claude-code-game-studios.md
  - sources/bootstrap-game-dev-wiki-2026-06-13.md
maturity: draft
created: 2026-06-13
updated: 2026-06-13
---

## Relations

- @ccc-wiki/concepts/subagent-orchestration.md — generic orchestration
- @ccc-wiki/entities/tools/claude-code-game-studios.md — role graph steal-from
- @osint-wiki/entities/tools/hermes-agent.md — optional 24/7 operator path (out of scope for v0)

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
2. **Plan** — Opus writes task breakdown in `briefs/` (gitignored) from wiki spec
3. **Execute** — Codex subagents implement **one subsystem** in `castle-sim` repo
4. **Verify** — operator playtest + automated lint/tests; log failures in `wiki/log.md`
5. **Promote** — update concept maturity when slice criteria pass

### Anti-patterns

- One prompt → full RTS
- Executor agents changing scope without planner pass
- Skipping playtest gate

### Steal-from

`Donchitos/Claude-Code-Game-Studios` — planner / implementer / reviewer edges only (`@entities/tools/claude-code-game-studios.md`).

## Snippets

> OMC-style game-dev case study pattern: Sonnet/Opus logic + Gemini art — validated for narrow vertical slices, not full Stronghold. [TENTATIVE — @osint-wiki/sources/omc-talent-container-paper.md]
