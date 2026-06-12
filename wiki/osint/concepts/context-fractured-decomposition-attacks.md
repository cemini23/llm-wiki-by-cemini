---
title: Context-Fractured Decomposition (CFD) — artifact provenance gap attacks
type: concept
tags: [concept, agent-security, provenance, mcp, tool-using-agents, k112]
keywords: [cfd, provenance-gap, artifact-lineage, cross-session, jailbreak, context-fractured]
related:
  - sources/arxiv-context-fractured-decomposition-cfd-2606.09084-2026-06-12.md
  - concepts/seclaw-agent-security-evaluation.md
  - concepts/ems-execution-security-gaps.md
  - concepts/conductor-orchestrator.md
  - concepts/librarian-server-architecture.md
  - concepts/llm-agent-systems.md
maturity: draft
created: 2026-06-12
updated: 2026-06-12
---

## Relations

- @sources/arxiv-context-fractured-decomposition-cfd-2606.09084-2026-06-12.md — primary source (2606.09084)
- @concepts/seclaw-agent-security-evaluation.md — trajectory-aware eval complement
- @concepts/conductor-orchestrator.md — multi-hop MCP write/read surfaces
- @concepts/librarian-server-architecture.md — wiki/brief artifacts persist across sessions

## Raw Concept

K112 ingest — deployment failure mode for tool-using agents when enforcement is fragmented and **artifact provenance** is untracked.

## Narrative

**Provenance gap:** safety monitors assume a contiguous trace; real pipelines split across sessions, tools, and agent instances while **files/logs/caches** persist. Attackers write benign payloads early, trigger harmful composition later via innocuous per-step tool calls.

**CFD vs STAC/backdoor:** intent-bearing pieces never co-occur in one monitor window — single-turn judges fail.

**Cemini mitigations (prescribed-not-built):**

| Layer | Action |
|-------|--------|
| Artifact writes | Lineage tags (source session, tool, trust tier) on `briefs/`, wiki edits, `.local/reports/` |
| MCP tool outputs | Treat cross-session file reads as untrusted until provenance verified |
| Eval | Extend MCP smoke matrix with CFD-style delayed-composition scenarios |

**Posture:** REFERENCE — prod brief for conductor artifact policy; cybersec-wiki handoff for offensive methodology.

## Snippets

> "Risk emerges only under delayed artifact-mediated composition."

> — [Source: arxiv-2606.09084-context-fractured-decomposition-attacks-on-tool.pdf, retrieved 2026-06-12]
