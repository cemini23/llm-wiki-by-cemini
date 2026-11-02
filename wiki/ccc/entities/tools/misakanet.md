---
title: "MisakaNet — local BM25 failure memory with a PostToolUse hook (MIT)"
type: entity
tags: [tool, claude-code, memory, hook, retrieval, local]
keywords: [misakanet, bm25, rrf, posttooluse hook, known root causes, local mcp, failure memory]
related:
  - "@osint-wiki/sources/eval-multi-wiki-link-revenue-v10.10-batch-c-2026-11-02.md"
maturity: draft
created: 2026-11-02
updated: 2026-11-02
---

## Raw Concept

Surfaced by @osint-wiki/sources/eval-multi-wiki-link-revenue-v10.10-batch-c-2026-11-02.md, URL 14, **Extract** tier. Routed to Atto, Collectibles, and CCC.

The question this page answers: **how do you stop an agent from re-diagnosing the same failure every session?**

## Narrative

### What it is

Three parts, all local:

1. **`misakanet-core`** — a zero-dependency Python search engine over past lessons, using **BM25 with reciprocal rank fusion**.
2. **`scripts/mcp_server.py`** — a local stdio MCP server over that index.
3. **A Claude Code `PostToolUse` hook on error** — injects a mandatory "search known root causes before retrying" prompt.

**MIT.** The setup package is `@misaka-net/misakanet-setup`; the repository uses DCO sign-off.

### Why the hook is the interesting part

The retrieval engine is ordinary — BM25 is decades old and needs no dependencies. What is not ordinary is **when** it fires.

Most memory systems ask the model to decide to look something up. A model in a failure loop does not reliably do that; it retries. This design does not ask. A `PostToolUse` error hands control to the hook, the hook runs the search, and the result arrives whether the model wanted it or not.

That is an external control, not a prompt instruction, and external controls hold where instructions drift.

### Fit

- **CCC** — the pattern is the transferable asset: a PostToolUse error hook that forces retrieval before retry.
- **Atto and Collectibles** — the lesson index accumulates project-specific root causes. Local, no data leaves the machine.
- **Run it in `--no-register` / local-only mode.** The report names this as a hard condition. Confirm before installing.

### Caveats

- BM25 is keyword matching. It will miss a failure described in different words than it was recorded. Do not treat a miss as proof the lesson does not exist.
- The hook fires on error. Decide what counts as an error, or it will fire constantly.

### Status

Extract, **pattern first**. The local-only mode is a precondition, not a preference.

## Snippets

> "Provides a zero-dependency local Python BM25 + RRF lesson search engine (misakanet-core), a local stdio MCP server (scripts/mcp_server.py), and a Claude Code PostToolUse/error hook pattern that injects a mandatory 'search known root causes before retrying' prompt." — report, URL 14

## Dead Ends

- **Relying on it as a complete memory.** BM25 misses paraphrase. It reduces repeat diagnosis; it does not eliminate it.
