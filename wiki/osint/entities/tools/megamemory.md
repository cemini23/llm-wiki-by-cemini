---
title: "MegaMemory — Local-First Knowledge Graph"
type: entity
tags: [tool, knowledge-graph, mcp-server, merge-engine, steal-from, k38]
keywords: [megamemory, steal-from, three-surface-eval]
related:
  - sources/link-evaluation-brief-trading-stack.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
maturity: validated
created: 2026-05-11
updated: 2026-05-11
license_verified: MIT
---

## Relations
- `@sources/link-evaluation-brief-trading-stack.md` — source evaluation brief (URL 16)
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied
- `@concepts/cemini-license-posture.md` — license posture context

## Raw Concept

- **Repo / URL**: `github.com/0xK3vin/MegaMemory`
- **Tier (per source brief)**: **Steal-from**
- **License** [VERIFIED 2026-05-11]: **MIT** (clean for pattern extraction per Cemini license posture). Maturity: 166★ / last push 2026-05-03 / ~3.1 months old.

## Narrative

Local-first persistent knowledge graph for AI coding agents. MCP server (stdio). 384-dim embeddings via Xenova/all-MiniLM-L6-v2 ONNX (~23 MB). Vectors in libsql/SQLite WAL mode. Two-way merge engine in `src/merge.ts` for syncing knowledge across diverging git branches.

### Integration vector

Steal-from: lift the **two-way merge engine** (`src/merge.ts`) algorithm and adapt it for `wiki_lint.py` to handle Markdown-repo merge conflicts. Do NOT adopt MCP server itself (workflow already standardized on Obsidian).

### Risks

Tight libsql schema lock-in; upstream schema changes complicate historical vector extraction.

[Source: Link Evaluation Brief Trading Stack.docx, URL 16]
