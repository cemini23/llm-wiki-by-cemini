---
title: "code-review-graph"
type: entity
tags: [tool, k174, mcp]
keywords: [code-review-graph, tree-sitter, MCP, blast-radius]
related:
  - sources/eval-repository-revenue-opportunity-analysis-2026-07-19.md
  - concepts/wiki-tooling-evaluation.md
  - entities/tools/i-have-adhd.md
maturity: draft
created: 2026-07-19
updated: 2026-07-19
---

## Relations

- @sources/eval-repository-revenue-opportunity-analysis-2026-07-19.md
- @concepts/wiki-tooling-evaluation.md
- @entities/tools/i-have-adhd.md

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | tirth8205/code-review-graph |
| **License** | MIT (~16MB shallow clone) |
| **Verdict** | **Extract** |
| **Routing** | CCC / TipDrop / xsp |

Local-first Tree-sitter code intelligence graph (SQLite) for MCP/CLI — blast-radius context so agents read only changed dependents. Claims large token reductions on reviews.

## Wired (K174 local)

- Clone: `.local/adopts/code-review-graph`
- Script: `scripts/adopt_k174_local.sh` (optional `pip install` / MCP notes)
- Combo with @entities/tools/i-have-adhd.md
