---
title: context-mode — tool-output sandboxing and session memory
type: entity
tags: [tools, context-management, mcp, agents, licensing]
keywords: [context-mode, elastic-license, tool-output-sandbox, sqlite-fts5, context-reduction, mcp]
related:
  - sources/eval-url-revenue-opportunity-2026-10-13.md
  - concepts/k290-eval-wave.md
  - concepts/agentic-context-management.md
maturity: draft
created: 2026-10-13
updated: 2026-10-13
wire_status: extract_only
---

## Relations

- @sources/eval-url-revenue-opportunity-2026-10-13.md
- @concepts/k290-eval-wave.md
- @concepts/agentic-context-management.md

## Raw Concept

**What prompted this page:** K290 tool eval (2026-10-13), entry 3. `github.com/mksglu/context-mode`.

## Narrative

A tool that **sandboxes tool output** — the docx claims **~98% context reduction** — and adds **SQLite FTS5 session memory** over **MCP**. The mechanism is **keeping large tool returns out of the model context** and querying them locally instead.

**License:** **Elastic License 2.0 (ELv2)** — `[CONFIRMED]` against the repo. **ELv2 is not open source** in the OSI sense: it bars providing the software as a managed service and removing licence/key functionality. The docx's own risk note says to **extract architectural patterns rather than redistribute** the code.

**Docx tier: Extract** — which is consistent with the licence. **Do not vendor the tree.**

**Claimed fit:** cut token and engineering cost across **Atto, CeminiDFS, CeminiParlays**.

**Phase-0 status:** ran 2026-10-13. Cloned to `.local/adopts/k290/context-mode` (19.6 MB). **`gh api` returns `NOASSERTION`** — the Elastic Licence 2.0 is not a licence GitHub recognises, which is consistent with it being non-OSI and with the Extract-only tier.

**Related prior art in this wiki:** `@concepts/agentic-context-management.md` covers the staging/elision findings from the harness-design paper (`@sources/arxiv-2609.20804-harness-design-coding-2026-09-18.md`), which found that **staging rule-based elision before LLM summarisation is the strongest efficiency path**. `context-mode` implements the "keep it out of context, query it locally" variant of the same idea.

## Snippets

> ELv2 … Extract architectural patterns … rather than redistributing. [Source: Repository Revenue Opportunity Analysis.docx — entry 3]
