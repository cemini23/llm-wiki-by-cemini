---
title: Headroom — prompt compression proxy for agent context
type: entity
tags: [entity, tool, context-compression, mcp, k129]
keywords: [headroom, headroomlabs-ai, Apache-2.0, token compression, MCP, RAG chunks]
related:
  - sources/eval-url-cemini-research-2026-06-25.md
  - concepts/mcp-context-optimization.md
  - concepts/context-compression-resume-pattern.md
  - concepts/self-compacting-language-model-agents.md
  - concepts/wiki-tooling-evaluation.md
maturity: draft
created: 2026-06-25
updated: 2026-06-25
---

## Relations

- @sources/eval-url-cemini-research-2026-06-25.md — K129 Adopt row (URL 6)
- @concepts/mcp-context-optimization.md — token budget discipline for MCP tool outputs
- @concepts/self-compacting-language-model-agents.md — in-trace compaction vs proxy compression (complementary)

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

## Snippets

> "Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 60-95% fewer tokens, same answers." [Source: https://github.com/headroomlabs-ai/headroom README (retrieved 2026-06-25)]

## Dead Ends

- Wave-5 eval `@sources/wave-5-1-link-eval-stacks.md` listed headroom UNAVAILABLE — superseded by K129 successful fetch.
