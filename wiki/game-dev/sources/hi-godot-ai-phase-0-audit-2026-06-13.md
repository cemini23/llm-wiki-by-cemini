---
title: hi-godot/godot-ai Phase-0 audit — 2026-06-13
type: source
tags: [source, phase-0, godot, mcp, audit]
keywords: [godot-ai, hi-godot, mcp, phase-0]
related:
  - entities/tools/hi-godot-ai.md
  - entities/tools/godot-mcp-landscape.md
  - concepts/ai-game-dev-tool-stack-2026.md
read_status: read
source_type: operator-audit
source_url: https://github.com/hi-godot/godot-ai
maturity: validated
created: 2026-06-13
updated: 2026-06-13
---

## Raw Concept

Phase-0 audit of **hi-godot/godot-ai** — leading Godot MCP plugin + Python server.

## Narrative

### Method

Clone `https://github.com/hi-godot/godot-ai` @ main (2026-06-12) to `/tmp/phase0-audit/godot-ai`. Read LICENSE, README, `docs/TOOLS.md`, CI badge.

### Checks

| Gate | Result |
|------|--------|
| License | **MIT** [CONFIRMED] |
| Maturity | ~500★, Asset Library + Store, CI + codecov, 66 releases, active (Jun 2026) |
| Godot version | 4.3+ (4.4+ recommended) |
| Transport | localhost `http://127.0.0.1:8000/mcp` [CONFIRMED] |
| Tool surface | ~41 MCP tools / 120 ops — **scene, script, node writes**, batch_execute, project_run |
| Dependencies | Python server via `uv`; plugin auto-starts server |
| Failure modes | Full editor write access; mis-prompt can corrupt scenes/scripts; localhost-only reduces remote attack but not prompt injection |

### Security posture [TENTATIVE — not full code audit]

- Binds 127.0.0.1 — OK for local dev
- **Write-capable** — requires @cybersecurity-wiki MCP posture + @ccc-wiki skill-vetting before castle-sim install
- Do **not** use during M0 pathfinding spike

### Verdict

**CONDITIONAL-GO** — adopt at **W2 harness pilot** in sandbox clone of `castle-sim`, read-only tools first (`editor_state`, `scene_get_hierarchy`), then scoped writes with human review.

## Snippets

Clone: `git clone https://github.com/hi-godot/godot-ai.git /tmp/phase0-audit/godot-ai`
