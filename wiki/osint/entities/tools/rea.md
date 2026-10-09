---
title: "REA — agent-first reverse-engineering toolkit (MCP)"
type: entity
tags: [tool, reverse-engineering, mcp, security, mit, k285]
keywords: [rea, reverse-engineering, hopper, decompilation, mcp, agent-first, k285]
related:
  - sources/eval-github-repository-revenue-2026-10-08.md
  - concepts/k285-eval-wave.md
  - entities/tools/agent-security-lab.md
  - sources/eval-multi-repo-revenue-2026-10-09.md
maturity: draft
created: 2026-10-08
updated: 2026-10-09
---

## Relations

- @sources/eval-github-repository-revenue-2026-10-08.md — K285 eval (tier: **Extract**)
- @concepts/k285-eval-wave.md — K285 cluster hub
- @entities/tools/agent-security-lab.md — authorized-lab context
- @sources/eval-multi-repo-revenue-2026-10-09.md — K287 fold. Owned-lab boundary stays.

## Raw Concept

- **Repo:** `github.com/morluto/rea`
- **Tier (K285):** **Extract** (route: local abliterated lab)
- **License:** **MIT** (verified 2026-10-08)
- **Stars:** 19,363 (verified), active
- **Description:** "Reverse engineer anything with agents, from app behavior down to native binaries"

## Narrative

An **agent-first reverse-engineering toolkit and MCP server** that bridges Claude/Cursor into **Hopper disassembly and execution tracing**.

### Why it matters here

The **reusable pattern is MCP-mediated decompilation**: an agent drives a disassembler through a tool interface and gets structured output back. For the **authorized operator lab**, that is background binary analysis without hand-driving the GUI.

**Re-evaluation signal:** this was a **Pass in K283** and is an **Extract here**. The technique is now mature enough to record.

### Hard gates

- Needs a **local Hopper Disassembler**.
- **Authorized scope only** — whitehat, owned systems.
- **No PoC. No exploit steps. No payloads in the wiki.**

### Boundary

FILE the pattern only. No clone this session.

### K287 fold (2026-10-09)

Already audited. The docx scores Extract again. `gh api` on 2026-10-09: **MIT**, 43,530 stars, last push 2026-10-09. The owned-lab boundary stays. No new lab brief. No install. No exploit text.

## Snippets

> "Reverse engineer anything with agents, from app behavior down to native binaries." [Source: eval-github-repository-revenue-2026-10-08.md, Phase-0 verified]
