---
title: openclaw-zero-token — CDP browser session bridge
type: entity
tags: [entity, tool, openclaw, scraping, k137]
keywords: [zero-token, CDP, Playwright, browser automation, MIT]
related:
  - sources/eval-multi-wiki-openclaw-ecosystem-2026-06-30.md
  - entities/tools/openclaw.md
  - sources/playwright-mcp-microsoft.md
maturity: draft
created: 2026-06-30
updated: 2026-06-30
---

## Relations

- @sources/playwright-mcp-microsoft.md — Playwright MCP is preferred in-chat path per osint rules
- @sources/eval-multi-wiki-openclaw-ecosystem-2026-06-30.md — K137 Steal-from row

## Raw Concept

K137 eval on [linuxhsj/openclaw-zero-token](https://github.com/linuxhsj/openclaw-zero-token) — MIT Node.js bridge using Playwright/CDP for browser-based sessions.

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | `linuxhsj/openclaw-zero-token` |
| **License** | **MIT** (`gh api` 2026-06-30) |
| **Stars / pushed** | ~5k★; pushed 2026-06-29 |
| **Verdict** | **Steal-from** — resilient DOM traversal + session persistence patterns |
| **Caution** | Docx frames "zero-token" Web UI wrapping — steal **scraping resilience**, not ToS-evasion posture |

**Posture:** wiki-only; compare against built-in browser + playwright MCP before implementation.

## Snippets

> MIT repo — Playwright + CDP integrations for automated browser session handling. [Source: eval docx URL 16; gh 2026-06-30]
