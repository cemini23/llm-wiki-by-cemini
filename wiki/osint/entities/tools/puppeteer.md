---
title: puppeteer — headless Chrome/Firefox automation
type: entity
tags: [entity, tool, browser, k202, integrate]
keywords: [puppeteer, CDP, WebDriver BiDi, Apache-2.0]
related:
  - entities/tools/browserless.md
  - sources/eval-github-revenue-browser-automation-2026-07-28.md
  - entities/tools/chrome-devtools-mcp.md
  - entities/tools/flaresolverr.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/gpuology-genealogy-agent-kit.md
maturity: draft
created: 2026-07-28
updated: 2026-07-28
---

## Relations

- @entities/tools/browserless.md — K202 backlink

- @sources/eval-github-revenue-browser-automation-2026-07-28.md — K202 Integrate
- @entities/tools/chrome-devtools-mcp.md — combo MCP + Puppeteer
- @entities/tools/flaresolverr.md — CF bypass layer
- @concepts/wiki-tooling-evaluation.md
- @concepts/gpuology-genealogy-agent-kit.md — Atto Antenati DOM automation

## Raw Concept

K202 Phase-0 on [puppeteer/puppeteer](https://github.com/puppeteer/puppeteer).

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | `puppeteer/puppeteer` |
| **License** | **Apache-2.0** (`gh api` 2026-07-28) |
| **Stars / size** | ~95k★ · GitHub size ~1.4GB — **do not clone monorepo** |
| **Verdict** | **Integrate** via project `npm i puppeteer` (Atto / GuruWatcher) |
| **Routing** | Atto #1 · GuruWatcher #2 · TipDrop |
| **Risk** | Unmasked headless → WAF bans; pair with FlareSolverr / residential proxies |

## Snippets

> DOM-aware automation for Antenati / JS-heavy finance pages. [Source: @sources/eval-github-revenue-browser-automation-2026-07-28.md]
