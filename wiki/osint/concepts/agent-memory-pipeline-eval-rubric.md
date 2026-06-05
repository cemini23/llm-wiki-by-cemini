---
title: Agent memory pipeline eval rubric (WorldMemArena steal-from)
type: concept
tags: [concept, agent-memory, evaluation, steal-from, k94]
keywords: [worldmemarena, memory-write, memory-maintenance, stash, claude-mem, librarian]
related:
  - "@ccc-wiki/concepts/worldmemarena-multimodal-agent-memory-eval.md"
  - "@ccc-wiki/sources/arxiv-worldmemarena-agent-memory-2605.29341.md"
  - entities/tools/claude-mem.md
  - concepts/librarian-server-architecture.md
  - concepts/monokern-compounding-research-pipeline.md
  - concepts/agent-memory-cross-scenario-generality.md
  - sources/arxiv-cross-scenario-agentic-generality-2606.04315-2026-06-05.md
maturity: draft
created: 2026-06-02
updated: 2026-06-05
cross-wiki-source: "@ccc-wiki/concepts/worldmemarena-multimodal-agent-memory-eval.md"
---

## Relations

- @ccc-wiki/concepts/worldmemarena-multimodal-agent-memory-eval.md — CCC ingest of arXiv 2605.29341
- @entities/tools/claude-mem.md — Write stage (session observations)
- @concepts/librarian-server-architecture.md — Retrieval/serving (kb-server, bulk)

## Narrative

**Steal-from** [CONFIRMED 2026-06-02] — WorldMemArena (2605.29341) scores long-horizon memory by **pipeline stage**, not a single “did it remember?” score. Multimodal action-world loops are out of scope for Cemini; the **stage separation** ports cleanly.

| Stage | Cemini analogue |
|-------|-----------------|
| **Write** | claude-mem observations, wiki ingest, librarian bulk moves |
| **Maintenance** | `maturity:` bumps, stale `[NEEDS VERIFICATION]`, federation lint, `wiki/log.md` |
| **Retrieval** | conductor, stash `recall`, kb-server / lazy-tool |
| **Use** | Session tool choice, prod MCP allowlists, skill routing |

**Use:** quarterly memory-stack review (stash + claude-mem + wiki) — score each stage before adding another memory product.

**K100 extension:** pair pipeline stages with the **five-scenario matrix** from `@concepts/agent-memory-cross-scenario-generality.md` — do not certify memory stack on chat-QA alone.

## Snippets

> "Memory must track an evolving world, revise what has gone stale, and surface the right evidence at decision time." [Source: @ccc-wiki/sources/arxiv-worldmemarena-agent-memory-2605.29341.md]
