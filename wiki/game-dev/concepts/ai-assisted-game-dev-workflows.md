---
title: AI-assisted game dev workflows — patterns and case studies
type: concept
tags: [concept, ai, agents, workflow, indie, harness]
keywords: [ai-game-dev, claude-code, cursor, solo-dev, playtest, gdd]
related:
  - concepts/ai-game-dev-tool-stack-2026.md
  - concepts/agent-harness-castle-project.md
  - concepts/game-dev-wiki-scope.md
  - entities/tools/claude-code-game-studios.md
  - sources/pchojecki-catvivors-claude-code-steam-2026.md
  - sources/morinaga-shin-koikoi-claude-godot-2026.md
  - sources/bsymbolic-lava-leap-ai-pair-programmer-2026.md
  - sources/bigdevsoon-void-balls-ai-10days-2025.md
  - sources/luden-superweird-gdd-prototype-cursor-2025.md
  - sources/chierhu-ai-coding-tools-game-dev-2026-06-21.md
  - sources/devto-claude-code-godot-skeleton-implementation-2026-06-28.md
  - sources/claude-code-cc-ios-port-2026-07-07.md
  - sources/godot-engine-ai-contribution-policy-2026-07-01.md
  - sources/exa-ai-gamedev-tools-batch-2026-06-13.md
  - concepts/agentic-pcg-level-design.md
  - concepts/ccgs-workflow-extraction.md
maturity: validated
created: 2026-06-13
updated: 2026-07-03
---

## Relations

- @ccc-wiki/concepts/subagent-orchestration.md — generic orchestration primitives
- @ccc-wiki/concepts/agent-completion-verification-gates.md — done = tests + playtest
- @concepts/agent-harness-castle-project.md — castle-sim-specific harness instance

## Raw Concept

Synthesized **AI + human** game development workflows from shipped indie case studies and multi-agent frameworks (2025–2026). Applies to any hobby/commercial game, not only castle-sim.

## Narrative

### Universal pattern

```
Blueprint (markdown GDD/readme)
  → Trash prototype (fast, ugly, playable)
  → Nail ONE fun loop (hardest phase)
  → Content expansion (faster once loop works)
  → Platform grind (Steam/itch export, store page)
  → Human playtest gate (AI cannot judge fun)
```

[CONFIRMED] across Catvivors, Shin KoiKoi, Lava Leap, Void Balls, Luden.io SuperWEIRD experiment.

### Workflow variants

| Pattern | Best for | Example | Human role |
|---------|----------|---------|------------|
| **Terminal pair (Claude Code)** | Full-stack solo, Godot/Unity | Catvivors on Steam | Vision, balance, playtest |
| **IDE pair (Cursor/Claude)** | Scoped features, GDScript/C# | Shin KoiKoi (70% UI scaffold) | Architecture, feel, export fixes |
| **Multi-agent studio (CCGS)** | Long projects needing QA/design gates | Donchitos 49-agent graph | Operator picks workflow; review gates |
| **Parallel domain agents** | Art+code+audio stack | Void Balls (8 agents, Unity MCP) | Palette/constraints, curation |
| **TDD milestone swarm** | Procedural games with invariants | Lava Leap (28 tasks, reviewer passes) | Design spec, live play verify |
| **GDD → prototype automation** | Pre-prod exploration | Luden.io + LÖVE + Tiled | Honest postmortem when automation fails |

### Timeline reality (honest)

| Project | "Fast" claim | Hidden pre-work | Hard phase |
|---------|-------------|-----------------|------------|
| Catvivors | Months to EA | AI researcher background | **2 weeks** first fun level |
| Shin KoiKoi | 2 days code | **3 weeks** design/scope | macOS ETC2 export |
| Lava Leap | 31 commits v1 | Brainstorm + design spec | WebGL verify (no screenshots) |
| Void Balls | 10 days | Studio workflow existing | 88 test files as safety net |
| Luden SuperWEIRD | Prototype gen | Full GDD + style guides | Approach **did not work as planned** |

### Non-negotiable human gates

1. **Fun / game feel** — LLMs do not know if combat is satisfying [@sources/pchojecki-catvivors-claude-code-steam-2026.md]
2. **Scope cuts** — AI expands feature surface unless constrained by markdown blueprint
3. **Platform export** — Steam/itch/macOS signing often longer than core gameplay coding
4. **Art direction** — constrain palette/style or output looks random (Void Balls 7-color rule)
5. **Security** — MCP write access to editor = vet first (@cybersecurity-wiki)
6. **Comprehension debt** — AI code that runs locally but operator cannot explain = **Skeleton Implementation** [@sources/devto-claude-code-godot-skeleton-implementation-2026-06-28.md]; pairs with METR perception gap [@sources/chierhu-ai-coding-tools-game-dev-2026-06-21.md]

### Skeleton Implementation (Godot + Claude Code) [TENTATIVE]

Practitioner essay on Claude Code + MCP Godot workflows [@sources/devto-claude-code-godot-skeleton-implementation-2026-06-28.md]:

| Symptom | Mitigation |
|---------|------------|
| Viewport/camera/scene-tree bugs after "working" AI PR | Flag spatial edits for human review; do not trust screenshot-only verify |
| MCP session memory substitutes for learning | Decision log in wiki/briefs; read generated code before merge |
| Short-term velocity, long-term debug tax | Monthly manual subsystem (no AI) to retain engine intuition |

**AI-safe vs protect:** boilerplate autoloads/signals → agent; architect camera, nav semantics, game feel → operator. Castle-sim fence: gitignored `briefs/research/agent-skeleton-implementation-fence.md`.

**Engine vs game repo:** Godot Foundation bans most AI in **upstream engine PRs** only [@sources/godot-engine-ai-contribution-policy-2026-07-01.md] — castle-sim harness unchanged.

### Multi-agent structure (why not one chat)

Single session problems [CONFIRMED — CCGS readme]:

- Magic numbers, skipped design docs, no QA pass
- No "does this fit the vision?" reviewer

**Fix:** named roles + handoff edges — steal from @entities/tools/claude-code-game-studios.md or @ccc-wiki ship-subagent pattern. Castle-sim instance: @concepts/agent-harness-castle-project.md.

### Pre-production: GDD-driven prototype gen

@sources/luden-superweird-gdd-prototype-cursor-2025.md — Luden.io used Cursor/Zed agent mode + markdown GDD + LÖVE + Tiled. **Lesson:** automation did not replace design iteration; it transformed the game unexpectedly. Still valuable for **exploration**, not hands-off shipping.

### Recommended hobby stack (2026-06-13)

| Phase | Tool | Notes |
|-------|------|-------|
| Research | This wiki + Exa digest | Spec before code |
| Plan | Opus / planner agent | `briefs/` markdown |
| Implement | Cursor Agent or Codex swarm | One subsystem per task |
| Godot bridge | Wiki spec first; MCP later | @concepts/ai-game-dev-tool-stack-2026.md |
| Verify | Human playtest + `godot-stagehand` / unit tests | AI playtest = WATCH |
| Art | @image-gen-wiki ComfyUI | Not in codegen path |

## Snippets

Blueprint stub for any game:

```markdown
# Game readme (AI context)
Engine: Godot 4.5 GDScript
Scope: vertical slice only — list EXPLICIT cuts
Core loop: one sentence
Milestone M0: playable criteria (binary pass/fail)
```

## Dead Ends

- "AI generates finished game" — no shipped case study supports one-shot shipping
- Local 32GB+ LLM for solo dev — subscription tools cheaper for most hobbyists [Catvivors author]
- UniGen / zero-code Unity — research demo; not production harness for castle-sim
