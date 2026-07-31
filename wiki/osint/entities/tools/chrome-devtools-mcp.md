---

title: chrome-devtools-mcp — Chrome DevTools Protocol MCP server
type: entity
tags: [entity, tool, mcp, browser, k141, k202]
keywords: [chrome-devtools-mcp, CDP, MCP, Apache-2.0, Lighthouse, Atto]
related:
  - sources/eval-multi-wiki-agent-harness-v2-2026-07-03.md
  - sources/eval-github-repo-mcp-plan-2026-07-05.md
  - sources/eval-github-revenue-browser-automation-2026-07-28.md
  - entities/tools/page-agent.md
  - entities/tools/puppeteer.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/gpuology-genealogy-agent-kit.md
maturity: draft
created: 2026-07-03
updated: 2026-07-31
wire_status: deferred
wire_note: next: ask operator before project MCP install
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

## Snippets

> Apache-2.0 — exposes CDP to agents via MCP. [Source: eval-multi-wiki-agent-harness-v2-2026-07-03.md]
