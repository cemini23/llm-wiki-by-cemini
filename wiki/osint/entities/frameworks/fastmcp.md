---
title: FastMCP
type: entity
tags: [framework, mcp, llm-tooling, python]
keywords: []
related:
  - sources/3-19-compliance-research.md
  - sources/3-19-ip-sale-research.md
  - sources/3-19-kalshi-trading-strategy-research.md
  - sources/3-19-langgraph-scatter-gather-financial-analysis.md
  - concepts/skill-vetting.md
  - entities/frameworks/langgraph.md
  - entities/infrastructure/deepseek-api.md
  - sources/4-5-links.md
  - entities/frameworks/autoagent.md
  - concepts/wiki-tooling-evaluation.md
  - sources/atomicmemory-llm-wiki-compiler.md
  - sources/willynikes2-knowledge-base-server.md
  - sources/agentmemory-rohitg00-cpr-impl.md
  - concepts/ai-organisation-design.md
  - concepts/mcp-tool-marketplace.md
  - sources/playwright-mcp-microsoft.md
  - sources/sentrux-ast-sensor.md
  - sources/vibe-trading-hkuds.md
  - sources/4-5-links-2.md
  - sources/agent-browser-vercel-labs.md
  - sources/piebald-claude-code-system-prompts.md
  - sources/3-26-b.md
  - sources/3-26-link-re-3.md
  - sources/wave-5-1-link-eval-more.md
  - sources/4-3-link-re-2.md
maturity: validated
created: 2026-04-23
updated: 2026-04-30
---

## Relations

- @sources/3-19-compliance-research.md
- @sources/3-19-ip-sale-research.md
- @sources/3-19-kalshi-trading-strategy-research.md
- @sources/3-19-langgraph-scatter-gather-financial-analysis.md
- @concepts/skill-vetting.md
- @entities/frameworks/langgraph.md
- @entities/infrastructure/deepseek-api.md — LLM brain that consumes MCP-exposed tools
- @sources/4-5-links.md — K8 deep-read 2026-04-28 — Cemini-internal evaluation doc. K8 server-probe finding: **130 registered `@mcp.tool` decorators** (vs the doc's "22" claim, ~6× over). **[UPDATE 2026-04-30 K11]**: FastMCP upgraded to **3.1.0**; MCP code restructured from `services/cemini_mcp/` → `/opt/cemini/cemini_mcp/server.py` (2,536 lines); current tool registration count ~30 lines matching `mcp.tool` — down from K8's 130, reflecting code consolidation and FastMCP 3.x API changes. The growth in tool count amplifies the doc's prescription to consolidate FastMCP tools into a hot-reloadable single-file registry behind a fixed adapter boundary
- @entities/frameworks/autoagent.md — K8 promotion 2026-04-28 — Single-File Registry-Driven Harness pattern is the named architectural recipe for consolidating the 130 `@mcp.tool` decorators into one structured, hot-reloadable file. AutoAgent's pattern is the operative target for the FastMCP tool-registry consolidation work prescribed in K8
- @concepts/wiki-tooling-evaluation.md — 2026-04-28 — wiki-tooling adoption candidates each ship their own MCP server (llm-wiki-compiler: 7 tools / knowledge-base-server: 16 tools / agentmemory: full MCP+REST). Any of them coexists with the deployed `cemini_mcp` (130 `@mcp.tool` decorators here) on a separate transport / endpoint; no integration conflict. Tool-namespace discipline: workspace-side wiki-tooling MCP runs on laptop or stdio; the deployed `cemini_mcp` runs on Hetzner over its own transport
- @sources/atomicmemory-llm-wiki-compiler.md — 2026-04-28 — primary wiki-tooling adoption candidate; ships an MCP server (`llmwiki serve`) with 7 tools (`ingest_source`, `compile_wiki`, `query_wiki`, `search_pages`, `read_page`, `lint_wiki`, `wiki_status`) + 5 resources. Closes the laptop ↔ server gap for the dev-stack DeepSeek brain to query the workspace wiki without re-deploying Track B `wiki_search` server-side
- @sources/willynikes2-knowledge-base-server.md — 2026-04-28 — sibling MCP-server-with-memory-engine candidate; 16 MCP tools + REST API + OpenAPI 3.1 + ChatGPT Custom GPT integration. Heavier integration surface than llm-wiki-compiler; deferred adoption decision
- @sources/agentmemory-rohitg00-cpr-impl.md — 2026-04-28 — Apache-2.0 cpr-pattern reference impl exposes its functionality via MCP server. Pattern is more useful than the runtime for the deployed Python stack; pipeline shape (PostToolUse hook → SHA-256 dedup → privacy filter → LLM compress → BM25+Vector+Graph RRF) ports into Python on the Cemini stack alongside FastMCP tool-call wrappers
- @sources/wave-5-1-link-eval-more.md — Wave 5.1 agent-framework evaluation; Instructor's structured-output extraction pattern integrates via FastMCP `@mcp.tool` decorators on LangGraph nodes
- @sources/4-3-link-re-2.md — K14 deep-read 2026-05-01; references FastMCP tool integration patterns across Docs 1, 3, 4

## Raw Concept

Synthesized from 4 source(s) referencing this entity across the Cemini research corpus. Category: frameworks.

## Narrative

FastMCP is a Python framework for building Model Context Protocol (MCP)
servers — the Anthropic-originated standard for LLM-tool interaction.
Cemini exposes its internal toolkits (position lookup, venue order
submission, historical-data query, risk-check) as MCP servers so that
any MCP-compatible agent (LangGraph supervisors, external clients) calls
them through a uniform, typed, permission-gated interface. `[RETRACTED 2026-04-24]`
Earlier phrasing named "LangGraph DeepSeek-R1 agents" as the caller —
DeepSeek/Ollama are not deployed on Cemini; the MCP servers are
LLM-agnostic by design, which is the point of the protocol.

**Deployed version (server probe 2026-04-30 K11)**: FastMCP **3.1.0**
(upgraded from ~2.x referenced in K8/K9/K10 docs — major version bump).
MCP code lives at `/opt/cemini/cemini_mcp/server.py` (2,536 lines;
restructured from the earlier `services/cemini_mcp/` path). ~30 tool
registration lines (consolidated from K8's 130 — reflects FastMCP 3.x
API changes + code reorganization). Container: `cemini_mcp` (image
`cemini-mcp:latest`, healthy).

Why FastMCP matters to the IP-sale thesis: MCP is the emerging
cross-vendor tooling standard. By wrapping all Cemini capabilities
behind MCP servers, the acquiring firm can plug in any compliant MCP
client (Claude, GPT-class models, their own fine-tunes, or a future
local model) without rewriting the tool layer. This decouples the
trading logic from any single LLM provider — a deal-favorable piece of
forward-compatibility.

## Snippets

*(populate as source stubs are deep-read.)*
