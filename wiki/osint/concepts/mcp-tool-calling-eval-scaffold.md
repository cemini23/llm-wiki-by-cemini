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
  - sources/arxiv-agents-all-the-way-down-2606.11869-2026-06-16.md
  - concepts/agents-all-the-way-down-methodology.md
  - sources/arxiv-claw-swe-bench-2606.12344-2026-06-16.md
  - concepts/claw-swe-bench-harness-evaluation.md
  - sources/arxiv-harnessfix-trace-repair-2606.06324-2026-06-16.md
  - entities/tools/reverse-skill.md
maturity: draft
created: 2026-06-02
updated: 2026-10-25
cross-wiki-source: "@ccc-wiki/concepts/maven-agentic-tool-calling-generalization.md"
---

## Relations

- @ccc-wiki/concepts/maven-agentic-tool-calling-generalization.md — CCC canon (2605.30738)
- @entities/tools/lazy-tool.md — deferred MCP discovery on laptop
- @concepts/agents-all-the-way-down-methodology.md — K118 P5 agent-tests-agent complements deterministic tests
- @sources/arxiv-agents-all-the-way-down-2606.11869-2026-06-16.md — K118 source

## Narrative

**Steal-from** [TENTATIVE] — MAVEN argues tool-calling agents fail on **strategy composition** and **intermediate state** across domains. Cemini prod touchpoints: prod-mcp surface, lazy-tool catalog, conductor fan-out.

**Smoke matrix (operator / server-Claude):**

1. Same natural-language task run against **two MCP domains** (e.g. `polymarket_health` vs `kb_search`).
2. Score whether **intermediate state** (IDs, filters, prior tool outputs) survives the second tool call.
3. Record pass/fail in brief or ROADMAP — not a shipped benchmark binary.

**Verdict:** evaluation discipline only — no MAVEN framework install.

**K100 allowlist (2026-06-05):** live inventory in `.cursor/mcp-allowlist-draft.yaml` — deny-by-default; prod-mcp read tier populated; `notify_operator` blocked pending operator GO. Enforcement: option A (lazy-tool) laptop / option B (server) prod — see `briefs/2026-05-31_prod-mcp-allowlist-draft-k100-from-cybersec.md`.

**K101 ADK Arena (2026-06-06):** MCP-Atlas is a named adapter in ADK Arena's benchmark suite — extend smoke matrix step (2) to include **MCP-native** intermediate state (tool catalog discovery → `invoke_proxy_tool` chain). Phase-0: `@entities/tools/adk-arena.md` **NO-GO** full install — steal **GTFA claim-coverage** scoring from `mcpatlas/adapter.py` for 1–3 manual smoke tasks only.

**Smoke run (2026-06-06):** 3 tasks, mean GTFA **0.89 PASS** — report `.local/reports/mcp-smoke-2026-06-06.md`. Catalog chain 1.00; dual-domain + conductor 0.83 (kb retrieval skew when prod metrics injected without concept slug).

**Intermediate-state rule (2026-06-06 fix):** When step 1 is prod-mcp health/metrics and step 2 is kb_search for **eval discipline**, append concept slug `mcp-tool-calling-eval-scaffold` to the kb query — raw channel/lag tokens route to prod architecture pages.

**lazy-tool aliases:** After `lazy-tool reindex`, run `bash scripts/lazy_tool_enrich_prod_health.sh` so `search_tools("polymarket health")` resolves `get_stream_health` / `get_data_health`.

**K118 agent-tests-agent (2026-06-16):** @concepts/agents-all-the-way-down-methodology.md P5 — general-purpose agent drives custom agent (prod-mcp CLI, lazy-tool) through scenario scripts; record tool traces + pass/fail. Complements GTFA smoke matrix above; does not replace pytest on prod code.

## Snippets

> "Generalization across agentic tool-calling environments remains a central challenge." [Source: @ccc-wiki/sources/arxiv-maven-agentic-tool-calling-2605.30738.md]
