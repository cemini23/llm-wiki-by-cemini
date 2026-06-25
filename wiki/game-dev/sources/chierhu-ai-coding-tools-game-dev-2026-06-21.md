---
title: Chier Hu — AI coding tools for game dev (first principles) — 2026-06-21
type: source
tags: [source, ai, workflow, godot, cursor, claude-code, digest]
keywords: [ai-game-dev, cursor, claude-code, codex, godot, mcp, vibe-coding]
related:
  - concepts/ai-assisted-game-dev-workflows.md
  - concepts/ai-game-dev-tool-stack-2026.md
  - concepts/agent-harness-castle-project.md
  - entities/engines/godot-4.md
  - entities/tools/hi-godot-ai.md
  - entities/tools/godot-mcp-landscape.md
  - sources/inbox-arxiv-reject-batch-2026-06-25.md
  - meta/cross-wiki-routing.md
read_status: read
source_type: web-article
source_url: https://chierhu.medium.com/ai-coding-tools-for-video-game-development-a-first-principles-analysis-of-what-actually-works-90dfa10edd13
maturity: validated
created: 2026-06-25
updated: 2026-06-25
---

## Raw Concept

Medium long-form (Jun 2026) synthesizing **what actually works** for AI-assisted game development — representation + training-data density as first principles; tool-by-tool verdicts for Cursor, Claude Code, Codex, Copilot, Antigravity.

## Narrative

### First principles [CONFIRMED]

| Principle | Implication for castle-sim |
|-----------|---------------------------|
| LLMs manipulate **text** | Godot `.gd`/`.tscn`/`project.godot` win over Blueprint/binary editors |
| **Runtime-blindness ceiling** | Agent must run game + read console/screenshot — @entities/tools/godot-stagehand.md, MCP |
| Training-data density tracks competence | Godot rising post-Unity pricing; C# Unity still strong; Unreal Blueprints near-zero |

### Tool verdicts (mid-2026) [TENTATIVE — author synthesis]

| Tool | Best engines | castle-sim fit |
|------|--------------|----------------|
| **Claude Code** | Godot standout, web, Pygame | **Primary W2 executor** — text scenes, CLI launch |
| **Cursor** | Unity C#, web, Godot | Planner + multi-file refactor in castle-sim repo |
| **Codex** | Browser games + Playwright loop | Secondary; weak on native Godot unless skills wired |
| **Copilot** | Unity autocomplete | Inline GDScript helper only |
| **Antigravity** | Web with browser actuation | Parallel smoke-test pattern |

### Evidence caveats [CONFIRMED]

- METR RCT: experienced devs **19% slower** with AI while believing **20% faster** — perception gap matters for interdependent game systems
- Pieter Levels fly.pieter.com ($87k MRR) — **browser/JS** success; almost nothing shipped Steam-quality purely via AI
- DEV.to RTS-in-Godot Claude experiment **abandoned** — loss of control / cognitive offload

### castle-sim harness alignment

| Extract | Skip |
|---------|------|
| Godot CLI-friendly = AI-friendly (vivecuervo7 card game case) | One-shot 11h codebase generation |
| MCP closes runtime-blindness for editor state | Treating AI as source of truth without playtest |
| PLAN.md + AGENTS.md + verification loop (Codex pattern) | Already in `briefs/WORKFLOW.md` — keep human playtest gate |

**Verdict:** **STEAL-FROM (workflow framing)** — reinforces W2 stack; no new Phase-0 tool.

Cross-ref: @concepts/ccgs-workflow-extraction.md for role graphs; @entities/tools/ziva-godot-agent.md for in-editor alt.

## Dead Ends

- Pivot castle-sim to Three.js for AI velocity — ROADMAP D4 locked Godot 3D SH2
- Expecting AI to ship Kingmaker parity without operator playtest — contradicts harness verify gate
