---
title: AI game dev tool stack — 2026 landscape
type: concept
tags: [concept, tools, ai, mcp, godot, automation]
keywords: [mcp, godot-ai, claude-code, stagehand, playtest, unity-mcp]
related:
  - concepts/ai-assisted-game-dev-workflows.md
  - entities/tools/claude-code-game-studios.md
  - entities/tools/godot-mcp-landscape.md
  - entities/tools/hi-godot-ai.md
  - entities/tools/godot-stagehand.md
  - entities/tools/godot-ai-playtest.md
  - entities/tools/serpent-ai.md
  - entities/tools/airtest.md
  - sources/exa-ai-gamedev-tools-batch-2026-06-13.md
  - sources/tool-evaluation-cross-wiki-routing-2026-06-13.md
  - sources/serpent-ai-phase-0-audit-2026-06-13.md
  - sources/airtest-phase-0-audit-2026-06-13.md
  - concepts/agent-harness-castle-project.md
  - concepts/game-dev-wiki-scope.md
  - concepts/llm-npc-runtime-ai-shelf.md
  - concepts/tool-evaluation-cross-wiki-batch-2026-06-13.md
  - sources/bigdevsoon-void-balls-ai-10days-2025.md
  - sources/godot-stagehand-phase-0-audit-2026-06-13.md
  - sources/hi-godot-ai-phase-0-audit-2026-06-13.md
maturity: validated
created: 2026-06-13
updated: 2026-06-15
---

## Relations

- @cybersecurity-wiki/concepts/mcp-security-posture.md — before installing MCP servers
- @image-gen-wiki/entities/uis/comfyui.md — art lane (not codegen)

## Raw Concept

Catalog of **AI + automation tools** for game development — codegen, editor MCP, playtesting, PCG — with adoption posture for hobby projects.

## Narrative

### Layer model

```
┌─────────────────────────────────────────┐
│  Human: vision, fun, scope, playtest    │
├─────────────────────────────────────────┤
│  Harness: planner → implementer → review  │  CCGS, CCC ship-subagent
├─────────────────────────────────────────┤
│  IDE/terminal: Cursor, Claude Code, Codex│
├─────────────────────────────────────────┤
│  Engine MCP: Godot/Unity bridge           │  hi-godot, Unity MCP, Glade
├─────────────────────────────────────────┤
│  Automation: Stagehand, ai-playtest, CI   │
├─────────────────────────────────────────┤
│  Generative media: ComfyUI, ElevenLabs…   │  @image-gen-wiki
└─────────────────────────────────────────┘
```

### Codegen & orchestration

| Tool | What it does | Posture | Notes |
|------|--------------|---------|-------|
| [Claude Code Game Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | 49 agents, 72+ skills, studio hierarchy | **STEAL-FROM** | @entities/tools/claude-code-game-studios.md |
| [OpenCode Game Studios](https://github.com/striderZA/OpenCodeGameStudios) | CCGS port for OpenCode | WATCH | Phase gates, hybrid pipelines |
| [gamestudio-subagents](https://github.com/pamirtuna/gamestudio-subagents) | 12 terminal agents | WATCH | Python; multi-engine |
| [game-mcp](https://github.com/xthenyo/game-mcp) | Unity 6 + Claude Code + MCP, "bible-first" | WATCH | `npx game-mcp` bootstrap |
| Cursor Agent | In-IDE multi-file edits | **GO** | Default for wiki + castle-sim |
| GitHub Copilot | Inline completion | GO adjunct | +55% task speed [arXiv 2302.06590] — not architecture |

### Godot MCP / editor bridge

| Tool | Stars | Tools count | Posture |
|------|-------|-------------|---------|
| [hi-godot/godot-ai](https://github.com/hi-godot/godot-ai) | ~500 | MCP + plugin | **EVAL** — Asset Library, active |
| [Sods2/godot-mcp](https://github.com/Sods2/godot-mcp) | new | 77 / 15 cats | WATCH — full IDE integration |
| [Farraskuy/Godot-MCP](https://github.com/Farraskuy/Godot-MCP) | 1 | 168 claimed | WATCH — verify before trust |
| [FunplayAI/funplay-godot-mcp](https://github.com/FunplayAI/funplay-godot-mcp) | — | — | WATCH |
| [godot-runtime-bridge](https://github.com/Aesthetic-Engine/godot-runtime-bridge) | — | Runtime inspect | WATCH — play/debug |

**Default for castle-sim v0:** markdown spec + Cursor — **no MCP write access** until Phase-0 audit (@entities/tools/godot-mcp-landscape.md).

### Visual / screen automation

| Tool | Mechanism | Posture | Notes |
|------|-----------|---------|-------|
| [Airtest](https://github.com/AirtestProject/Airtest) | Image template matching | **Adopt** @ccc-wiki | @entities/tools/airtest.md — Phase-0 CONDITIONAL-GO |
| [SerpentAI](https://github.com/SerpentAI/SerpentAI) | Pixel agent environments | **STEAL-FROM** | Dormant; @entities/tools/serpent-ai.md — Phase-0 complete |

### Testing & playtest automation

| Tool | Engine | Mechanism | Posture |
|------|--------|-----------|---------|
| [godot-stagehand](https://github.com/mrf/godot-stagehand) | Godot | External Go driver, Playwright-like | **EVAL** for W2 harness |
| [godot-ai-playtest](https://github.com/marcushale/godot-ai-playtest) | Godot 4 | TCP JSON-RPC plugin + Python client | WATCH |
| [testplay-runner](https://github.com/Kubonsang/testplay-runner) | Unity | Go CLI, JSON stdout for agents | Unity only |
| modl.ai | Unity/Unreal | Autonomous playtest bots | Commercial; studio scale |
| LLM playtest papers | — | arXiv 2509.22170 etc. | Research shelf |

Pair with @ccc-wiki verification gates: automated tests **do not replace** human fun pass.

### Unity-specific (reference)

| Tool | Role |
|------|------|
| Unity MCP | Claude ↔ scene hierarchy (Void Balls workflow) |
| UniGen | NL → Unity 3D multi-agent (research) |

Not on castle-sim path (Godot chosen) but patterns transfer.

### Procedural content (LLM agents)

| Repo | Focus | Tier |
|------|-------|------|
| AgenticPCG | Agent-driven PCG | Research |
| SceneSynth | Scene generation | WATCH |
| hayba | — | WATCH |

Defer until core loop ships — PCG without fun loop = pretty empty levels.

### Runtime NPC AI (separate from dev tools)

GDC/industry: NVIDIA ACE on-device SLMs, Ubisoft dynamic NPC research, arXiv dialogue systems. **Not dev acceleration** — product feature shelf for Tier 3+.

### Adoption order (hobby)

1. Markdown GDD + Cursor/Claude Code (**now**)
2. Unit tests + lint in game repo (**M0**)
3. CCGS role patterns without full install (**steal**)
4. godot-stagehand for regression (**W2**)
5. hi-godot MCP after security audit (**conditional**)
6. Generative art via @image-gen-wiki (**W3**)

## Snippets

MCP admission checklist (abbrev):

```
[ ] Read cybersecurity MCP posture
[ ] Phase-0: license, maintainer, tool write scope
[ ] Sandbox project first — not production castle-sim
[ ] Prefer read-only scene inspect before mutating tools
```

## Dead Ends

- 168-tool MCP plugins without audit — tool count ≠ trust
- Replacing human playtest with LLM agents for **fun** tuning — not validated for hobby quality bar
