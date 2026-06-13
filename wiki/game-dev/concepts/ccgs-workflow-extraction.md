---
title: CCGS workflow extraction — steal-for Cursor / castle-sim
type: concept
tags: [concept, ccgs, harness, workflow, claude-code, steal-from]
keywords: [ccgs, workflow-catalog, skills, agents, vertical-slice, gdd]
related:
  - entities/tools/claude-code-game-studios.md
  - concepts/agent-harness-castle-project.md
  - concepts/ai-assisted-game-dev-workflows.md
  - concepts/vertical-slice-v0.md
  - sources/ccgs-workflow-catalog-2026.md
  - sources/starlog-ccgs-49-agents-2026.md
  - sources/exa-npc-pcg-ccgs-batch-2026-06-13.md
maturity: validated
created: 2026-06-13
updated: 2026-06-13
---

## Relations

- @ccc-wiki/entities/tools/claude-code-game-studios.md — CCC canonical stub
- @ccc-wiki/concepts/subagent-orchestration.md — dispatch primitives

## Raw Concept

Deep extraction from **Donchitos/Claude-Code-Game-Studios** (49 agents, 73 skills, 7 workflow phases) — adapted for **Cursor + Codex + wiki/briefs** without requiring Claude Code install.

## Narrative

### What CCGS is [CONFIRMED — upstream]

Not a game engine — a **process envelope** for Claude Code:
- `.claude/agents/*.md` — role definitions (model tier, tools, escalation)
- `.claude/skills/*/SKILL.md` — slash-command workflows
- `.claude/docs/workflow-catalog.yaml` — phase gates + **artifact checks**
- `design/`, `docs/architecture/`, `production/` — expected folder artifacts

**Hard constraint:** upstream targets **Claude Code only** [TENTATIVE — Starlog 2026]. Cursor operators **steal patterns**, not full install.

### Seven phases → castle-sim mapping

| CCGS phase | Key artifacts | castle-sim / wiki equivalent |
|------------|---------------|------------------------------|
| **Concept** | `game-concept.md`, `art-bible.md`, `systems-index.md` | @concepts/scope-tiers.md + `briefs/` GDD stub |
| **Systems design** | Per-system GDDs, cross-GDD review | @concepts/stronghold-systems-inventory.md slices |
| **Technical setup** | `architecture.md`, ADRs, control-manifest | `castle-sim` repo structure + Phase-0 Godot |
| **Pre-production** | UX specs, `/prototype`, `/vertical-slice` | @concepts/vertical-slice-v0.md M0/M1 gates |
| **Production** | epics, stories, `/dev-story`, sprints | Codex one-subsystem-per-swarm |
| **Polish** | balance, perf, soak | Post-M1 |
| **Release** | launch checklist, store | Steam/itch deferred |

Phase gates are **advisory** in CCGS (`/gate-check` never hard-blocks) — human decides proceed [CONFIRMED workflow-catalog.yaml header].

### Agent roster — what to steal (not all 49)

| CCGS agent | Cursor/harness mapping | Model |
|------------|------------------------|-------|
| creative-director | Opus planner — scope veto | Opus |
| game-designer | Wiki spec author | Opus/Sonnet |
| godot-gdscript-specialist | Codex implementer swarm | Codex |
| qa-lead / qa-tester | Reviewer subagent + human playtest | Sonnet |
| prototyper | Pathfinding spike agent | Codex |
| performance-analyst | Defer until perf issues | — |

Skip engine agents: `ue-*`, `unity-*` unless pivoting engine.

**Godot-relevant specialists:** godot-gdscript-specialist, godot-shader-specialist, godot-specialist, level-designer, systems-designer.

### Skills — priority steal list (73 total)

| Priority | Skill | Why |
|----------|-------|-----|
| P0 | `brainstorm`, `map-systems` | Scope + system decomposition |
| P0 | `vertical-slice` | PROCEED/PIVOT/KILL gate — mirrors v0 |
| P0 | `dev-story` | One story implementation loop |
| P1 | `design-system`, `design-review`, `review-all-gdds` | GDD quality |
| P1 | `gate-check`, `playtest-report` | Verification |
| P1 | `balance-check`, `smoke-check`, `regression-suite` | QA automation |
| P1 | `create-architecture`, `architecture-decision` | ADR habit |
| P2 | `prototype` | Throwaway vs vertical slice distinction |
| P2 | `team-combat`, `team-level`, … | Domain team bundles — adapt for siege/economy |
| P3 | `art-bible`, `asset-spec` | Route art prompts to @image-gen-wiki |

Full catalog: @sources/ccgs-workflow-catalog-2026.md

### game-designer agent pattern [CONFIRMED — upstream agent file]

Steal collaboration protocol:
1. Ask clarifying questions first
2. Present 2–4 options with MDA/theory reasoning
3. Incremental file write — **user approves each section**
4. `disallowedTools: Bash` for pure design agents

Maps to: **planner never commits code without operator "yes".**

### vertical-slice skill [CONFIRMED]

Distinct from `/prototype`:
- **Prototype** — "Is core mechanic fun?" (early)
- **Vertical slice** — "Can we build full loop at production quality?" (late pre-prod)

Outputs `PROCEED | PIVOT | KILL` — align with @concepts/vertical-slice-v0.md spike gate (M0) vs playable slice (M1).

### Cursor adaptation (minimal port)

Do **not** clone 49 agents. Port **structure**:

```
wiki/           ← design truth (public)
briefs/         ← session GDD + stories (gitignored)
castle-sim/     ← code
ROADMAP.md      ← phase tracker

Planner prompt: read wiki → write briefs/story-NNN.md
Implementer: one story, one subsystem
Reviewer: diff + playtest checklist from vertical-slice-v0
```

Optional: copy `workflow-catalog.yaml` ideas into `briefs/WORKFLOW.md` with artifact globs for lint script later.

### Model economics (from Starlog / CCGS)

| Tier | Use |
|------|-----|
| Opus | Creative director, architecture, vertical-slice verdict |
| Sonnet | Design docs, code review |
| Codex | Implementation swarms |
| Haiku | Format/lint — optional |

Matches @concepts/agent-harness-castle-project.md matrix.

### Anti-patterns [CONFIRMED upstream + Starlog]

- Installing CCGS for a **game jam** — overhead kills velocity
- Using all 72 skills before shipping M0
- Skipping design artifacts because AI can "just code"
- Expecting CCGS to enforce discipline — **human can override everything**

| Verdict | **STEAL-FROM** workflow + ~12 skills + 6 agent roles; **no** full CCGS dependency |

## Snippets

M0 gate borrowed from CCGS vertical-slice falsifiable question:

```markdown
Validation question: Can a peasant chop wood, path around a placed wall,
and deposit at stockpile in one uninterrupted loop?
Verdict: PROCEED / PIVOT / KILL
```

## Dead Ends

- Full CCGS in Cursor without Claude Code — path mismatch; extract docs only
- OpenCode Game Studios fork — WATCH if migrating off Claude Code terminal
