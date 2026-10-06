---
title: "ColeMurray/background-agents — async worker structure for detached agent jobs"
type: entity
tags: [tool, agent-harness, async, guruwatcher, k283]
keywords: [background-agents, async-workers, detached-jobs, guruwatcher, claim-ingestion, k283]
related:
  - sources/eval-github-repos-dev-tools-2026-10-06.md
  - concepts/k283-eval-wave.md
  - entities/tools/guruwatcher.md
maturity: draft
created: 2026-10-06
updated: 2026-10-06
---

## Relations

- @sources/eval-github-repos-dev-tools-2026-10-06.md — K283 eval (tier: Extract)
- @concepts/k283-eval-wave.md — K283 cluster hub
- @entities/tools/guruwatcher.md — target project

## Raw Concept

- **Repo:** `github.com/ColeMurray/background-agents`
- **Tier (K283):** **Extract** (route: GuruWatcher)
- **License:** NOT FOUND (docx)
- **Stack:** Python, TypeScript, async task workers
- **Docx metadata:** NOT FOUND

## Narrative

Async worker structures for **long-running, detached agent operations** that do not tie up an interactive CLI. The wiki references this repo in two earlier tool-eval sources; K283 scores it as the GuruWatcher background-worker pattern.

### Why it matters here

GuruWatcher must ingest incoming market newsletters and parse parameters **without blocking its main event loop**. Detached workers keep Discord alert turnaround fast. Pairs with @entities/tools/keyed-lock.md for per-ticker concurrency.

### Boundary

**Alert-only invariant:** background agents must never place trades and must never overwrite `watches.json` state.

## Snippets

> "Implements asynchronous worker structures for long-running, detached agent operations without tying up interactive CLI interfaces." [Source: eval-github-repos-dev-tools-2026-10-06.md]
