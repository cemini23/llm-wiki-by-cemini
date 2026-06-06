---
title: MCP tool-calling eval scaffold (MAVEN steal-from)
type: concept
tags: [concept, mcp, evaluation, steal-from, k94]
keywords: [maven, tool-calling, lazy-tool, prod-mcp, conductor, generalization]
related:
  - "@ccc-wiki/concepts/maven-agentic-tool-calling-generalization.md"
  - "@ccc-wiki/sources/arxiv-maven-agentic-tool-calling-2605.30738.md"
  - "@cybersecurity-wiki/concepts/mcp-security-posture.md"
  - entities/tools/lazy-tool.md
  - concepts/cemini-workflow-tooling-audit-2026-05-30.md
  - concepts/adk-arena-framework-evaluation.md
  - sources/arxiv-adk-arena-agent-dev-kits-2606.05548-2026-06-06.md
  - entities/tools/adk-arena.md
maturity: draft
created: 2026-06-02
updated: 2026-06-06
cross-wiki-source: "@ccc-wiki/concepts/maven-agentic-tool-calling-generalization.md"
---

## Relations

- @ccc-wiki/concepts/maven-agentic-tool-calling-generalization.md — CCC canon (2605.30738)
- @entities/tools/lazy-tool.md — deferred MCP discovery on laptop

## Narrative

**Steal-from** [TENTATIVE] — MAVEN argues tool-calling agents fail on **strategy composition** and **intermediate state** across domains. Cemini prod touchpoints: prod-mcp surface, lazy-tool catalog, conductor fan-out.

**Smoke matrix (operator / server-Claude):**

1. Same natural-language task run against **two MCP domains** (e.g. `polymarket_health` vs `kb_search`).
2. Score whether **intermediate state** (IDs, filters, prior tool outputs) survives the second tool call.
3. Record pass/fail in brief or ROADMAP — not a shipped benchmark binary.

**Verdict:** evaluation discipline only — no MAVEN framework install.

**K100 allowlist (2026-06-05):** live inventory in `.cursor/mcp-allowlist-draft.yaml` — deny-by-default; prod-mcp read tier populated; `notify_operator` blocked pending operator GO. Enforcement: option A (lazy-tool) laptop / option B (server) prod — see `briefs/2026-05-31_prod-mcp-allowlist-draft-k100-from-cybersec.md`.

**K101 ADK Arena (2026-06-06):** MCP-Atlas is a named adapter in ADK Arena's benchmark suite — extend smoke matrix step (2) to include **MCP-native** intermediate state (tool catalog discovery → `invoke_proxy_tool` chain). Phase-0: `@entities/tools/adk-arena.md` **NO-GO** full install — steal **GTFA claim-coverage** scoring from `mcpatlas/adapter.py` for 1–3 manual smoke tasks only.

## Snippets

> "Generalization across agentic tool-calling environments remains a central challenge." [Source: @ccc-wiki/sources/arxiv-maven-agentic-tool-calling-2605.30738.md]
