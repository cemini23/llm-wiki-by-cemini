---
title: Ziva 3 Godot agent — Phase-0 audit — 2026-06-21
type: source
tags: [source, phase-0, godot, mcp, agent, audit]
keywords: [ziva, godot, mcp, proprietary, playtest]
related:
  - entities/tools/ziva-godot-agent.md
  - entities/tools/hi-godot-ai.md
  - entities/tools/godot-mcp-landscape.md
  - concepts/ai-game-dev-tool-stack-2026.md
  - concepts/agent-harness-castle-project.md
  - entities/tools/godot-stagehand.md
  - entities/tools/hi-godot-ai.md
  - meta/cross-wiki-routing.md
  - sources/inbox-arxiv-reject-batch-2026-06-21.md
  - meta/cross-wiki-routing.md
read_status: read
source_type: operator-audit
source_url: https://ziva.sh/blogs/ziva-3-release
maturity: validated
created: 2026-06-21
updated: 2026-06-21
---

## Raw Concept

Phase-0 audit of **Ziva 3** (Jun 2026 release) — proprietary in-editor Godot agent with MCP export, built-in playtest loop, plan mode, local Ollama/LM Studio, and hosted multiplayer relay.

## Narrative

### Checks

| Gate | Result |
|------|--------|
| License | **None** on [ziva-sh/ziva-agent-plugin-godot](https://github.com/ziva-sh/ziva-agent-plugin-godot) — issues/docs only |
| Model | Closed runtime; default cloud LLMs; optional local models |
| Godot | 4.2+; GDExtension side panel |
| MCP | Exposes Godot tools to Cursor/Claude Desktop — competes with @entities/tools/hi-godot-ai.md |
| Playtest | Agent sends input + reads console — overlaps @entities/tools/godot-stagehand.md |
| castle-sim fit | **CONDITIONAL-GO (operator tool)** — not wiki/harness dependency |

### Steal value

| Extract | Skip |
|---------|------|
| Plan-mode approval gate before edits | Closed-source runtime in CI |
| Parallel subagent todo UX | Cloud code path for private castle-sim |
| Playtest-before-handoff pattern | Ziva relay for castle-sim MP (defer W2+) |

### vs hi-godot-ai

| | Ziva | hi-godot-ai |
|--|------|-------------|
| Agent location | In-editor panel | External MCP client (Cursor) |
| License | Proprietary | MIT |
| castle-sim W2 | Personal accelerator OK | **Default** for harness |

### Verdict

**CONDITIONAL-GO (operator)** — personal Godot IDE assistant; harness stays on Cursor + MIT MCP stack.

## Dead Ends

- Ziva as castle-sim CI verifier — closed, cloud-default, non-auditable
