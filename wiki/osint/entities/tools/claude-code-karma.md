---
title: "claude-code-karma — Claude Code session monitoring dashboard (Adopt-tier)"
type: entity
tags: [tool, claude-code, monitoring, dashboard, ccc-wiki, adopt-tier, observability]
keywords: [claude-code-karma, session monitoring, token tracking, Claude Code, Apache-2.0, cost observability]
related:
  - sources/tool-evaluation-multi-wiki-audit-may-2026.md
maturity: draft
created: 2026-05-16
updated: 2026-05-16
---

## Relations

- `@sources/tool-evaluation-multi-wiki-audit-may-2026.md` — source evaluation that classified this as Adopt-tier

## Raw Concept

Identified in the May 2026 44-tool multi-wiki audit. Apache-2.0 licensed web dashboard for monitoring active Claude Code sessions. 204 stars, 28 forks. Primary fit: CCC wiki. Cross-route: OSINT wiki for LLM observability and cost tracking documentation.

## Narrative

A specialized dashboard for continuous monitoring of active Claude Code sessions — tracks context windows, token consumption, and session state.

**Integration path**: The core live-session-status-monitoring concept will be adapted as a dedicated MCP server hook for instrumenting laptop-side Claude Code sessions. This enables precise token-utilization tracking during complex algorithmic strategy generation for `/opt/cemini`.

**License**: Apache-2.0 — clean for internal enterprise adoption with patent grant.

**Why Adopt**: Token economics and context-window tracking are critical for multi-agent orchestration. This provides the observability layer the CCC wiki's conductor/librarian architecture needs.

**Open question** [OPEN QUESTION 2026-05-16]: Scalability testing needed when monitoring hook is deployed across concurrent high-density multi-agent swarms.
