---
title: "GitHub Batch Evaluation.docx — Unusual Whales MCP/API batch (2026-06-28)"
type: source
tags: [tool-evaluation, unusual-whales, mcp, tipdrop, k133]
keywords: [unusualwhales-mcp, openclaw, tipdrop, mcp-server, gemini-deep-research-v9]
related:
  - concepts/wiki-tooling-evaluation.md
  - concepts/cemini-license-posture.md
  - entities/tools/unusualwhales-mcp.md
  - entities/tools/openclaw.md
  - sources/openclaw-ios-node-2026-06-29.md
  - sources/eval-multi-wiki-discord-link-2026-06-28.md
  - sources/eval-repo-plan-tipdrop-legacy-2026-06-28.md
  - sources/eval-multi-wiki-openclaw-ecosystem-2026-06-30.md
maturity: draft
read_status: read
created: 2026-06-28
updated: 2026-06-30
clusters: [agent-harness, wiki-tooling]
---

## Relations

- @entities/tools/unusualwhales-mcp.md — Adopt (MIT, gh-verified)
- @sources/eval-multi-wiki-discord-link-2026-06-28.md — sibling Discord batch
- @sources/eval-repo-plan-tipdrop-legacy-2026-06-28.md — sibling TipDrop legacy batch

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | GitHub Repository Batch Evaluation |
| **Type** | DOCX (Gemini Deep Research RUNTIME v9) |
| **sha256** | `e69caead3c1cd2efd8f461e7b18647822edcc46ce50b7bbd577f13d34f6b1bc2` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/GitHub Repository Batch Evaluation.docx` |
| **Retrieved** | 2026-06-28 |
| **Read status** | read (`gh api` on Adopt row) |

## Narrative

K133 batch — **20 URLs** on Unusual Whales API clients, MCP servers, DiscordMonitor clones, OpenClaw crawler.

### Tier distribution

| Tier | Count | Repos |
|------|-------|-------|
| **Adopt** | 1 | phields/unusualwhales-mcp |
| **Reference-only** | 1 | danwagnerco/mcp-server-unusualwhales |
| **Reject** | 1 | airnub/unusualwhales-api-client (no license) |
| **UNAVAILABLE** | 17 | 404 UW bots; OpenClaw crawler missing |

### Adopt — `gh api` (2026-06-28)

| Repo | Docx | Verified | Posture |
|------|------|----------|---------|
| phields/unusualwhales-mcp | Adopt | **MIT**, 4★, pushed 2025-08-04 | **Adopt** — TypeScript Hono MCP; stdio/SSE/HTTP; dark pool + flow tools |
| unusual-whales/unusual-whales-official-mcp | (proxy in docx) | **MIT**, 71★ | **Reference** — canonical vendor MCP; prefer when TipDrop wires official stack |

### Cross-wiki steals (no OSINT entity stubs)

- **OpenClaw** DM pairing (`dmPolicy="pairing"`) → @entities/tools/openclaw.md + K133 cybersec brief; iOS node hardening → @sources/openclaw-ios-node-2026-06-29.md
- **danwagnerco** filter heuristics (min_volume_oi_ratio, RepeatedHits) → reference-only rewrite

### TipDrop compliance gate

Adopted MCP output must **not** pipe raw UW flow into DRY_RUN Discord without NFA/CFTC 4.41 sanitization middleware.

## Snippets

> phields/unusualwhales-mcp — MIT, Hono MCP exposing UW dark pool and options flow endpoints. [Source: eval docx URL 3, 2026-06-28; gh api 2026-06-28]
