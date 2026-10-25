---
title: ThinkRail (JetBrains) — spec-graph MCP for coding agents
type: entity
tags: [tool, ccc, spec-driven-development, mcp, jetbrains]
keywords: [thinkrail, pi-spec-graph, spec_get, spec_graph, SPEC.md]
related:
  - @osint-wiki/sources/eval-multi-wiki-link-revenue-v10.9-2026-10-25.md
  - entities/tools/worktrunk.md
maturity: draft
created: 2026-10-25
updated: 2026-10-25
phase_0_verdict: CONDITIONAL-GO — no shipped MCP server
wire_status: pending
wire_note: Extract packages/spec-graph tool source and wrap it. Do not assume mcp/server.mjs exists.
---

## Raw Concept

Phase-0 on [JetBrains/thinkrail](https://github.com/JetBrains/thinkrail), 2026-10-25. Source: v10.9 multi-wiki link evaluation, URL 5, scored Extract (CCC primary) for atto and guruwatcher.

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | https://github.com/JetBrains/thinkrail |
| **License** | Apache-2.0 (verified) |
| **Last commit** | 2026-10-25 |
| **Size** | 30 MB / 1928 files |
| **Verdict** | CONDITIONAL-GO |

### The idea worth taking

A coding agent forgets a project's invariants between sessions. ThinkRail keeps them in a machine-readable specification graph — `SPEC.md` and `architecture.md` — that agents query before editing.

`packages/spec-graph/tools/` ships seven tools, verified present:

`get.ts` · `grep.ts` · `graph.ts` · `delete.ts` · `create.ts` · `update.ts` · `validate.ts`

### Why it is CONDITIONAL-GO, not GO

The source report claims the spec-graph is "already been proven portable to Claude Code and Codex as a lightweight stdio MCP server (mcp/server.mjs)".

**That file is not in the public repo.** Phase-0 checked. `packages/spec-graph/package.json` declares no `bin` and no `main`; its scripts are only `typecheck` and `test`.

So the tool *logic* is present and Apache-2.0, but **the MCP wrapper would have to be written.** That is a real cost the report did not count.

### The invariants worth encoding

For Atto: the human-gate rule on `truth.ged`. An agent must not write it.
For GuruWatcher: `watches.json` hold/trigger state must not be clobbered.

Those two rules, written once and queried every session, are the whole payoff.

### Context cost

Ten workflow skills load at roughly 400 tokens always-on. Install two: `importing-a-codebase` and the spec-graph wrapper.

## Snippets

> "Extracting this spec-graph MCP layer into /Users/claudiobarone/Projects/atto and /Users/claudiobarone/Projects/GuruWatcher ensures coding agents systematically check module invariants" — source report, URL 5

## Dead Ends

- **Assuming `mcp/server.mjs` exists.** It does not. Verified 2026-10-25.
- **Switching editors to ThinkRail's desktop GUI.** Unnecessary; the value is the spec graph, not the IDE.
