---
title: chrome-devtools-mcp — Chrome DevTools Protocol MCP server
type: entity
tags: [entity, tool, mcp, browser, k141, k202]
keywords: [chrome-devtools-mcp, CDP, MCP, Apache-2.0, Lighthouse, Atto]
related:
  - sources/eval-multi-wiki-agent-harness-v2-2026-07-03.md
  - sources/eval-github-repo-mcp-plan-2026-07-05.md
  - sources/eval-github-revenue-browser-automation-2026-07-28.md
  - sources/2026-11-16-deep-research-link-eval-agentic-harnesses.md
  - concepts/agent-link-evaluation-gates-v1013.md
  - entities/tools/page-agent.md
  - entities/tools/puppeteer.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/gpuology-genealogy-agent-kit.md
maturity: draft
created: 2026-07-03
updated: 2026-11-16
harness_verb: WIRE
---

## Relations

- @sources/eval-multi-wiki-agent-harness-v2-2026-07-03.md — K141 Adopt row
- @sources/eval-github-repo-mcp-plan-2026-07-05.md — K146 reaffirm + telemetry flag
- @sources/eval-github-revenue-browser-automation-2026-07-28.md — K202 Integrate (Atto portal agent)
- @entities/tools/page-agent.md
- @entities/tools/puppeteer.md
- @concepts/wiki-tooling-evaluation.md
- @concepts/gpuology-genealogy-agent-kit.md

## Raw Concept

K141 Phase-0 on [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp); K202 reaffirm + Atto/GuruWatcher revenue path.

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | `ChromeDevTools/chrome-devtools-mcp` |
| **License** | **Apache-2.0** (`gh api` 2026-07-28) |
| **Stars / pushed** | ~48k★; pushed 2026-07-28 |
| **Verdict** | **Adopt / Integrate** — CCC browser MCP + Atto Antenati agent |
| **Clone** | `.local/adopts/chrome-devtools-mcp` (~16M shallow, K202) |
| **Ops** | Enforce `--no-usage-statistics`; sandbox; no GuruWatcher order placement via browser |

Brief: `briefs/ccc-2026-07-03_k141-page-agent-chrome-devtools-adopt.md` · Atto brief K202.

### Reaffirmed 2026-11-16 — Integrate, with a narrowed gap

The Deep Research batch graded this **Integrate** for game-time. Direct licence check
on 2026-11-16 confirms **Apache-2.0** and 57.6k stars, pushed that day. [CONFIRMED]

One correction to the report's gap claim: **game-time already ships Playwright**
(`packages/client/playwright.config.ts`, `e2e/shell.spec.ts`). Playwright is a test
runner that starts and stops on its own. This MCP attaches CDP to a live browser an
agent drives at run time for profiling and heap inspection. The overlap is the browser
dependency, not the job.

The freeze blocks adding another MCP server locally. Extraction here is the CDP
profiling recipe, not an installation.

## Snippets

> Apache-2.0 — exposes CDP to agents via MCP. [Source: eval-multi-wiki-agent-harness-v2-2026-07-03.md]
