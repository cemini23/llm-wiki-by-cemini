---
title: Headroom — prompt compression proxy for agent context
type: entity
tags: [entity, tool, context-compression, mcp, k129]
keywords: [headroom, headroomlabs-ai, Apache-2.0, token compression, MCP, RAG chunks]
related:
  - sources/eval-url-cemini-research-2026-06-25.md
  - sources/cemini-repository-evaluation-plan-runtime-2026-07-04.md
  - concepts/mcp-context-optimization.md
  - concepts/context-compression-resume-pattern.md
  - concepts/self-compacting-language-model-agents.md
  - concepts/wiki-tooling-evaluation.md
  - entities/tools/obsidian-mind.md
maturity: draft
created: 2026-06-25
updated: 2026-07-04
---

## Relations

- @sources/eval-url-cemini-research-2026-06-25.md — K129 Adopt row (URL 6)
- @sources/cemini-repository-evaluation-plan-runtime-2026-07-04.md — K143 Phase-0 refresh
- @concepts/mcp-context-optimization.md — token budget discipline for MCP tool outputs
- @concepts/self-compacting-language-model-agents.md — in-trace compaction vs proxy compression (complementary)
- @entities/tools/obsidian-mind.md — sibling K143 memory/vault pattern, Steal-from only

## Raw Concept

Phase-0 prompted by K129 **Cemini URL Evaluation Research.docx** URL 6 — `headroomlabs-ai/headroom`.

## Narrative

**Headroom** (Apache-2.0) compresses tool outputs, logs, files, and RAG chunks **before they reach the LLM** — library, proxy, and MCP server. Claims 60–95% token reduction with preserved answer quality.

**Phase-0 (2026-06-25):**

| Check | Result |
|-------|--------|
| License | **Apache-2.0** (`gh api` — SPDX Apache-2.0) |
| Hardcoded wiki layout | N/A — compression proxy |
| Maturity | **50479★**, pushed 2026-06-25, 384 open issues |
| OSINT fit | **Adopt** — token-efficient log ingestion for long research sessions |
| CCC-wiki fit | **Adopt** — MCP proxy layer for agent harness cost control |

**Posture:** **Adopt** as optional MCP proxy on laptop research stack. Eval doc previously marked UNAVAILABLE in wave-5-1 — K129 re-fetch succeeded. Not on cemini-prod trading path.

**Phase-0 refresh (2026-07-04):** **Adopt reaffirmed** for OSINT/CCC context compression. `gh api` + LICENSE confirm Apache-2.0; maturity improved materially since K129 (~56k★, pushed 2026-07-03, latest release/PyPI 0.30.0). Evidence files in the audit included `wiki/ccr.md`, `wiki/mcp.md`, `wiki/LIMITATIONS.md`, `wiki/proxy.md`, `headroom/cache/compression_store.py`, and CCR/proxy/security tests.

**Caveats:** CCR retrieval is not permanent storage — default local TTLs are short (roughly 30–60 minutes depending on mode). Cursor setup remains manual, proxy/header behavior is moving, and local `.headroom` cache/log hygiene matters. Use as optional laptop/CCC infrastructure, not as a durable wiki or trading-state memory layer.

## Snippets

> "Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 60-95% fewer tokens, same answers." [Source: https://github.com/headroomlabs-ai/headroom README (retrieved 2026-06-25)]

## Dead Ends

- Wave-5 eval `@sources/wave-5-1-link-eval-stacks.md` listed headroom UNAVAILABLE — superseded by K129 successful fetch.
