---
title: "holaOS — all-in-one AI agent workspace (MCP + SQLite memory)"
type: entity
tags: [tool, k231, atto, ccc, mcp, memory]
keywords: [holaOS, MCP, SQLite, shared memory, agent workspace, BYOK, Modified Apache]
related:
  - sources/eval-url-revenue-opportunity-2026-08-11.md
  - concepts/wiki-tooling-evaluation.md
  - entities/tools/stagehand.md
  - sources/eval-project-evaluation-revenue-2026-08-11.md
maturity: draft
created: 2026-08-11
updated: 2026-08-11
phase_0_verdict: "CONDITIONAL Extract 2026-08-11 (NOASSERTION Modified Apache, ~53MB)"
---

## Relations

- @sources/eval-project-evaluation-revenue-2026-08-11.md

- @sources/eval-url-revenue-opportunity-2026-08-11.md — CONDITIONAL Extract
- @concepts/wiki-tooling-evaluation.md
- @entities/tools/stagehand.md — combo: Stagehand v4 + holaOS → resilient Atto retrieval

## Raw Concept

- **Repo**: `github.com/holaboss-ai/holaOS`
- **License**: **NOASSERTION** (Modified Apache file) — gh api override; do not trust eval SPDX
- **Tier**: Extract (CONDITIONAL — patterns only)
- **Primary fit**: Atto / CCC — MCP + SQLite-backed durable shared memory patterns
- **Phase-0**: `.local/adopts/holaOS` ~53MB

## Narrative

Agent workspace letting Claude Code / Codex operate over local tools and files with durable shared memory (SQLite-backed context/preferences/history) — solving cross-session context loss. Extracting the **MCP + SQLite memory patterns** enhances atto-mcp state retention across archival searches.

**Constraints:** **do not vendor full tree into atto-mcp**; NOASSERTION/Modified Apache requires legal review before distribution; Electron desktop overhead vs headless execution — extract patterns only; SQLite job-queue reliability needs stress testing before merge.
