---
title: chrome-devtools-mcp — Chrome DevTools Protocol MCP server
type: entity
tags: [entity, tool, mcp, browser, k141]
keywords: [chrome-devtools-mcp, CDP, MCP, Apache-2.0, Lighthouse]
related:
  - sources/eval-multi-wiki-agent-harness-v2-2026-07-03.md
  - entities/tools/page-agent.md
  - concepts/wiki-tooling-evaluation.md
maturity: draft
created: 2026-07-03
updated: 2026-07-03
---

## Relations

- @sources/eval-multi-wiki-agent-harness-v2-2026-07-03.md — K141 Adopt row

## Raw Concept

K141 Phase-0 on [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp).

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | `ChromeDevTools/chrome-devtools-mcp` |
| **License** | **Apache-2.0** (`gh api` 2026-07-03) |
| **Stars / pushed** | ~45k★; pushed 2026-07-03 |
| **Verdict** | **Adopt** — CCC default browser MCP (pairs with built-in Cursor browser rule) |
| **Ops** | Enforce `--no-usage-statistics`; avoid thousand-tab profiles |

Brief: `briefs/ccc-2026-07-03_k141-page-agent-chrome-devtools-adopt.md`

## Snippets

> Apache-2.0 — exposes CDP to agents via MCP. [Source: eval-multi-wiki-agent-harness-v2-2026-07-03.md]
