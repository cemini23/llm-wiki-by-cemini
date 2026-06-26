---
title: hera-agent-godot — Phase-0 audit — 2026-06-26
type: source
tags: [source, phase-0, godot, cli, agent, audit]
keywords: [hera-agent-godot, notnull92, phase-0, cli, low-token]
related:
  - entities/tools/hera-agent-godot.md
  - entities/tools/godot-mcp-landscape.md
  - entities/tools/godot-stagehand.md
  - entities/tools/hi-godot-ai.md
  - sources/notnull92-hera-agent-godot-devto-2026-06-25.md
  - concepts/agent-harness-castle-project.md
  - concepts/godot-stagehand-ci-smoke-plan.md
  - concepts/ai-game-dev-tool-stack-2026.md
  - entities/projects/castle-sim.md
  - sources/inbox-arxiv-reject-batch-2026-06-26.md
  - meta/cross-wiki-routing.md
read_status: read
source_type: operator-audit
source_url: https://github.com/NotNull92/hera-agent-godot
maturity: validated
created: 2026-06-26
updated: 2026-06-26
---

## Raw Concept

Phase-0 audit of **NotNull92/hera-agent-godot** — Go CLI + Godot 4.7+ editor addon for low-token agent control of live editor state. DEV.to launch 2026-06-25.

## Narrative

### Checks

| Gate | Result |
|------|--------|
| License | **MIT** [CONFIRMED — GitHub API + README] |
| Maturity | ~2★ (Jun 2026); active push 2026-06-26; core CLI surface marked complete in README |
| Godot version | **4.7+ required** [CONFIRMED] — blocks castle-sim on 4.5.2/4.6.x pin |
| Transport | localhost HTTP/RPC editor addon; instance discovery via `~/.hera-agent-godot/instances/` |
| Tool surface | `status`, `scene`, `node`, `run`/`stop`, `game`, `output`, `screenshot`, `eval`, `batch`, `smoke` — write-capable |
| vs MCP | Author claims ~0 schema tokens/turn vs 4k–31k for Godot MCP; measured in `docs/LOW_TOKEN.md` |
| castle-sim fit | **CONDITIONAL-GO (W2 verify alt)** — low-token shell loop for story-004-class smoke; A/B vs @entities/tools/godot-stagehand.md after 4.7 pin |

### Steal value

| Extract | Skip |
|---------|------|
| `hera smoke` / `hera run --wait` + `hera output --type error` verify loop | Default write tools on prod repo |
| Compact JSON for Codex/Cursor shell stories | Replacing human playtest gate |
| Runtime assert + screenshot for HUD stories | Mandatory before M0 pathfinding spike |

### Security posture [TENTATIVE]

- Localhost-only addon server — same bar as @entities/tools/hi-godot-ai.md
- **Write-capable** node/scene edits — sandbox clone + @ccc-wiki skill-vetting first

### Verdict

**CONDITIONAL-GO** — adopt at W2 **after Godot 4.7 pin bump** + regression pass. Operator brief: gitignored `briefs/research/hera-agent-godot-w2-pilot.md`.

Cross-ref: @sources/chierhu-ai-coding-tools-game-dev-2026-06-21.md (runtime-blindness); @sources/godot-47-release-shelf-2026-06-25.md (pin gate).

## Dead Ends

- Phase-0 on CaR video-world-models repo (2606.23105) — out of game-dev scope
- hera-agent-unity for castle-sim — Godot-only project
