---
title: NotNull92 — hera-agent-godot DEV.to launch — 2026-06-25
type: source
tags: [source, godot, agent, cli, devto, digest]
keywords: [hera-agent-godot, notnull92, cli, low-token, editor]
related:
  - entities/tools/hera-agent-godot.md
  - sources/hera-agent-godot-phase-0-audit-2026-06-26.md
  - entities/tools/godot-mcp-landscape.md
  - entities/tools/godot-stagehand.md
  - sources/chierhu-ai-coding-tools-game-dev-2026-06-21.md
  - sources/inbox-arxiv-reject-batch-2026-06-26.md
  - concepts/agent-harness-castle-project.md
  - meta/cross-wiki-routing.md
read_status: read
source_type: web-article
source_url: https://dev.to/notnull92/i-built-a-tool-that-lets-ai-see-and-control-the-godot-editor-53ej
maturity: validated
created: 2026-06-26
updated: 2026-06-26
---

## Raw Concept

DEV.to launch post for **hera-agent-godot** — low-token Go CLI + Godot 4.7+ `@tool` addon that lets shell-based agents inspect/control a **live editor** (scene tree, run/stop, screenshots, runtime assert, error log).

## Narrative

### Problem framed [CONFIRMED — author]

AI agents read files but cannot see running editor state → false confidence ("should work") vs broken scenes at Play.

### Solution surface [CONFIRMED — README cross-check]

| Capability | Example CLI |
|------------|-------------|
| Editor discovery | `hera status`, `hera instances` |
| Scene tree R/W | `hera scene tree`, `hera node` |
| Run/stop + wait | `hera run --current --wait` |
| Error log | `hera output --type error` |
| Runtime QA | `hera game assert`, `hera screenshot --runtime --analyze` |
| Batch | `hera batch`, `hera smoke` |

**Design bet:** CLI-first compact JSON vs MCP schema bloat (~0 tool schemas per turn vs 4k–31k tok for Godot MCP servers) — see repo `docs/LOW_TOKEN.md`.

### Othello demo [TENTATIVE — author claim]

One-prompt Reversi build with move simulation + screenshot/score/turn verification loop.

### castle-sim fit

| Extract | Skip |
|---------|------|
| Closes runtime-blindness for **W2 verify** alongside @entities/tools/godot-stagehand.md | Requires **Godot 4.7+** — pin bump before adopt |
| Shell-native — works with Cursor/Codex without MCP wiring | Full editor write access — sandbox first |
| `smoke` command aligns with story-004 pattern | Replace stagehand without A/B |

**Verdict:** Phase-0 → @sources/hera-agent-godot-phase-0-audit-2026-06-26.md → **CONDITIONAL-GO** W2 alt.

## Snippets

```
GitHub: https://github.com/NotNull92/hera-agent-godot
Asset Store: https://store.godotengine.org/asset/notnull92/hera-agent-godot/
```

## Dead Ends

- Adopting before castle-sim Godot pin reaches 4.7+ stable
- Running write commands on production castle-sim repo without sandbox clone
