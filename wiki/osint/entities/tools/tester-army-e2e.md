---
title: "tester-army/e2e — agentic test harness with cached action replay"
type: entity
tags: [tool, testing, agent-harness, playwright, mcp, k283]
keywords: [e2e, tester-army, agentic-testing, cached-replay, playwright, mcp, atto]
related:
  - sources/eval-github-repos-dev-tools-2026-10-06.md
  - concepts/k283-eval-wave.md
  - concepts/agent-tool-use-verification.md
maturity: draft
created: 2026-10-06
updated: 2026-10-06
---

## Relations

- @sources/eval-github-repos-dev-tools-2026-10-06.md — K283 eval (tier: Extract)
- @concepts/k283-eval-wave.md — K283 cluster hub
- @concepts/agent-tool-use-verification.md — agent verification thread

## Raw Concept

- **Repo:** `github.com/tester-army/e2e`
- **Tier (K283):** **Extract**
- **License (docx claim):** Apache-2.0 — unverified
- **Stack:** TypeScript, Node.js, Playwright, agent-device, MCP, Vercel AI SDK
- **Docx metadata:** 5,514★ / Oct 2026 / 294 issues — **NOT independently verified** (bash has no network)

## Narrative

An open agentic testing framework for web, iOS and Android. The mechanism that matters: an agent explores a UI **once**, the action trace is **cached**, and later CI runs **replay the cached trace deterministically** — so tokens are spent on discovery, not on every regression run.

### Why it matters here

Closes a cost gap in Atto's UI regression testing: the civil-record share views and portal navigation are dynamic, but the assertions are fixed. Route: Atto share-portal CI, under CCC test-automation patterns.

### Boundary

Agentic browser suites hitting Atto UI fixtures **must use synthetic test records only** — never real genealogical data in trace capture. Extract the technique; no clone this session.

## Snippets

> "The repository provides a caching layer that executes AI agent browser workflows once and replays them deterministically for subsequent CI runs." [Source: eval-github-repos-dev-tools-2026-10-06.md]
