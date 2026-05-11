---
title: "CTOP — htop-Style Process Monitor for AI Coding Agents"
type: entity
tags: [tool, workflow-laptop, claude-code, observability, token-tracking, mit-license]
keywords: [ctop, htop, process monitor, Claude Code, token tracking, context window, CLI TUI]
related:
  - sources/evaluating-code-for-trading-stacks.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-05-10
updated: 2026-05-10
---

## Relations
- `@sources/evaluating-code-for-trading-stacks.md` — source evaluation brief (URL 8)
- `@concepts/tool-evaluation-framework.md` — three-surface fit (workflow-only)
- `@concepts/cemini-license-posture.md` — MIT, IP-sale clean

## Raw Concept

CTOP is a TUI process monitor specifically for AI coding agent sessions (Claude Code, Codex CLI). Tracks CPU, RAM, uptime, and real-time token utilization across input/output/cache-creation/cache-read against the 200k context window.

- **Repo**: `github.com/aakashadesara/ctop`
- **License**: MIT [NEEDS VERIFICATION 2026-05-10]
- **Stack**: Pure Node.js, zero external dependencies
- **Install**: `npm i -g ctop-claude` or Homebrew
- **Footprint**: ~40-70 MB resident (V8 baseline overhead)
- **Keybindings**: Vim-style; SIGTERM/SIGKILL rogue sessions inline

## Narrative

CTOP solves the silent token-burn problem during heavy Claude Code workflows. When the solo developer runs multiple parallel agent sessions across different repos, CTOP renders a dedicated TUI pane that exposes context-window utilization in real time.

### Integration vectors

**Workflow laptop (Adopt — ✅)**: Install globally on macOS via npm or Homebrew. Run in dedicated iTerm2 pane alongside Obsidian + active Claude Code panes during intensive curation sessions. Prevents financial token drain and identifies zombie processes stuck in infinite loops.

**Cemini prod (No — ❌)**: Production environment is programmatic LangGraph + DeepSeek HTTP endpoint. No interactive CLI agent processes. CTOP provides zero operational value to a headless trading stack.

**Wiki server (No — ❌)**: Librarian uses API-based HTTP/MCP queries. No interactive shells.

### Risks

- **Tight Claude Code coupling**: parses specific process signatures + log formats emitted by Claude Code and Codex CLI. If Anthropic ships updates that change process tree structure or log format, CTOP loses tracking until the repo updates.
- **DeepSeek endpoint compatibility**: NEEDS VERIFICATION 2026-05-10 — token metrics parser may be hardcoded to Anthropic response payloads. If Claude Code is routed through OpenAI-compatible custom endpoints (DeepSeek), tracking may degrade.
- **MIT license**: assertion from source brief; verify before commit (low risk — laptop-only deployment, no IP-exposure surface).

### Cemini significance

Indirect: better token observability on the workflow laptop directly reduces operational cost during heavy ingest sessions. No prod-side integration required.

### Adoption checklist

- [ ] `npm i -g ctop-claude` (or Homebrew tap if available)
- [ ] Verify LICENSE = MIT after install
- [ ] Test with active Claude Code session — confirm token-tracking accuracy
- [ ] If DeepSeek-routed: verify parser handles non-Anthropic response shapes
- [ ] Add to iTerm2 default workspace alongside Obsidian

[Source: Evaluating Code for Trading Stacks.docx, URL 8]
