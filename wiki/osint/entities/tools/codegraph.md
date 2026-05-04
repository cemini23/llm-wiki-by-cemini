---
title: codegraph — Token-Efficient AST Indexer for Claude Code
type: entity
tags: [dev-tooling, claude-code, ast, knowledge-graph, sqlite, node, mit, adopted-tier, laptop-only]
keywords: [codegraph, ast-indexer, tree-sitter, claude-code, token-efficiency, call-graph, knowledge-graph]
related:
  - sources/links-2-5-4-tool-eval.md
  - concepts/wiki-tooling-evaluation.md
  - entities/tools/swarmvault.md
maturity: draft
created: 2026-05-04
updated: 2026-05-04
---

## Relations

- @sources/links-2-5-4-tool-eval.md — origin source: 2026-05-04 Gemini DR eval, URL 3, **Adopt** tier verdict
- @concepts/wiki-tooling-evaluation.md — codegraph is laptop-side workflow tool; complements (does not replace) the librarian-side wiki-compiler decision
- @entities/tools/swarmvault.md — swarmvault also uses tree-sitter but for the wiki layer; codegraph is for the codebase layer (different deployment slot)

## Raw Concept

Localized, semantic codebase indexing utility designed to augment Claude Code by pre-indexing call graphs and symbol relationships into a SQLite knowledge graph. Identified as **Adopt-tier** in the 2026-05-04 Gemini DR eval — laptop install only.

## Narrative

- **URL**: https://github.com/colbymchenry/codegraph
- **License**: MIT
- **Stack**: TypeScript (94.8%), Node.js, SQLite + tree-sitter
- **Maturity**: 678 stars, 237 commits
- **Distribution**: npm
- **Language coverage**: 19+ languages, including native Python parsing
- **Sync model**: native OS filesystem events (FSEvents on macOS) for "Always Fresh" indexing

### Why Adopt for laptop only

Per the Gemini DR eval and the wiki's existing structure: the librarian server's job is markdown compilation, not codebase parsing. codegraph indexes source code, which is irrelevant to a knowledge-base server. But on the laptop, it provides a **token-efficient call-graph view** for Claude Code sessions on Cemini's Python codebase — eliminating blind file scans during `services/llm_analyst/` development.

### Install path

```
npm install -g codegraph
```

Caveat: SQLite indices must be `.gitignore`d to prevent binary blobs polluting version control. The eval flags this explicitly.

### Risks (per Gemini DR)

- Bus factor: single-contributor project
- FSEvents memory leaks during massive refactor / dependency-tree changes (e.g. modifying `site-packages`)
- Specific RAM/disk metrics not yet verified — [NEEDS VERIFICATION 2026-05-04]

## Snippets

- **Token-efficiency claim**: "fundamentally eliminates the need for agents to blindly scan files, drastically reducing token consumption and accelerating architectural exploration." [Source: links 2 5_4.docx URL 3]
- **Mechanism**: "autonomously parsing local repository source code, intelligently mapping call graphs, and structuring symbol relationships into a pre-indexed knowledge graph maintained within a SQLite database." [Source: links 2 5_4.docx URL 3]
- **Recommendation tier**: "Adopt. The tool should be immediately installed on the developer's primary laptop to augment Claude Code sessions, specifically targeting a reduction in LLM tool calls during the development of new FastMCP endpoints." [Source: links 2 5_4.docx URL 3]
