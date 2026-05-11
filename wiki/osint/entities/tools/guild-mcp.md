---
title: "guild — Local-First Search MCP Server (Go)"
type: entity
tags: [tool, mcp-server, go-binary, bm25, rrf, librarian-candidate, k38]
keywords: [guild, mcp, adopt, three-surface-eval]
related:
  - sources/link-evaluation-brief-trading-stack.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-05-11
updated: 2026-05-11
---

## Relations
- `@sources/link-evaluation-brief-trading-stack.md` — source evaluation brief (URL 18)
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied
- `@concepts/cemini-license-posture.md` — license posture context

## Raw Concept

- **Repo / URL**: `github.com/mathomhaus/guild`
- **Tier (per source brief)**: **Adopt**
- **License**: [NEEDS VERIFICATION 2026-05-11] License needs verification before Hetzner deploy.

## Narrative

Go MCP server for local-first search + retrieval. Embedded SQLite in `~/.guild/`. Hybrid: BM25 keyword + int8 ONNX vector similarity, fused via Reciprocal-Rank Fusion (RRF).

### Integration vector

Adopt — architectural pivot for the librarian server. Single Go binary with RRF replaces the heavy memory-intensive Ollama instance. Frees Hetzner CPX21 RAM headroom.

### Risks

Go binary opacity — debugging without Go expertise is hard. Embedded SQLite managed by compiled binary is rigid (vs. flat SQLite file).

[Source: Link Evaluation Brief Trading Stack.docx, URL 18]
