---
title: Cindy (makecindy) — desktop multi-agent shell
type: entity
tags: [tool, ccc, agent-harness, context-tier]
keywords: [cindy, orca-workflow, skillhub, desktop agent]
related:
  - @osint-wiki/sources/eval-multi-wiki-link-revenue-v10.9-2026-10-25.md
maturity: draft
created: 2026-10-25
updated: 2026-10-25
phase_0_verdict: CONTEXT
wire_status: none
wire_note: Wiki reference only. No install.
---

## Raw Concept

URL 1 of @osint-wiki/sources/eval-multi-wiki-link-revenue-v10.9-2026-10-25.md. Tier **Context**.

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | https://github.com/makecindy/cindy |
| **License** | Apache-2.0 (report) |
| **Stars** | 4.4k (621 forks) |
| **Open issues** | 1.6k, 311 open PRs |
| **Verdict** | CONTEXT — architectural reference only |

Desktop/mobile agent shell bundling local file access, cross-harness memory, SkillHub plugins, and Orca multi-agent workflows (`packages/orca-workflow`, `packages/lizi-mcps`, `apps/desktop/maker-ipc/orca*`).

**Why not adopted:** the stack already standardizes on Cursor and Claude Code, and Atto already ships `atto-mcp`. A third-party desktop wrapper adds no SKU revenue.

**Why it is not even a soft candidate:** the issue tracker reports severe macOS instability — V8 heap OOM after ~50 hours (#7015), 600-second SDK hard timeouts that truncate turns with no UI feedback (#7034), and broken terminal sync after importing Claude Code sessions (#6998).

One idea worth reading, not running: the authorization-card pattern for remote MCP/plugin grants (#4813).

## Dead Ends

- Adopting it as a daily driver. Stability regressions, no revenue path.
