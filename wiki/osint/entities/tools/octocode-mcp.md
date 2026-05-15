---
title: "Octocode MCP — LSP-Based Code Intelligence via Model Context Protocol"
type: entity
tags: [tool, mcp, lsp, code-intelligence, developer-tooling, typescript, claude-code]
keywords: [octocode-mcp, bgauryy, lsp, code-intelligence, ripgrep, call-hierarchy, mcp-server, mit-license, adopt]
related:
  - sources/multi-wiki-link-eval-v4-2026-05-15.md
  - entities/infrastructure/conductor-librarian-architecture.md
maturity: draft
created: 2026-05-15
updated: 2026-05-15
---

## Relations

- @sources/multi-wiki-link-eval-v4-2026-05-15.md — evaluated in v4 link-eval (Adopt tier)
- @entities/infrastructure/conductor-librarian-architecture.md — MCP server pattern aligns with conductor/librarian topology

## Raw Concept

Promoted from the v4 multi-wiki link evaluation (2026-05-15). Tier: **Adopt**. Primary fit: CCC-wiki.

URL: https://github.com/bgauryy/octocode-mcp
License: MIT
Stars: 822 | Last commit: 2025-12-15 | Open issues: 0
Stack: TypeScript / JavaScript / LSP / MCP

## Narrative

A production-ready MCP server combining fast text-based code exploration (localSearchCode via ripgrep) with deep semantic intelligence (lspGotoDefinition, lspFindReferences, lspCallHierarchy via Language Server Protocol). Zero open issues on a completed, stable feature set.

Key tools:
- **localSearchCode** — ripgrep-powered full-text search with regex support
- **lspGotoDefinition / lspFindReferences** — precise symbol-level navigation
- **lspCallHierarchy** — call graph traversal for tracing algorithmic logic through complex codebases
- **lspHover** — type information and documentation on hover

The lspCallHierarchy tool is directly applicable to standardizing the tracking of algorithmic backtesting logic in the Cemini financial codebase — enabling automated audit trails for trading strategy provenance.

Stability note: no 2026 commits — the feature set is complete and static, not abandoned. This is a finished tool, not a decaying one.

## Cross-wiki routing

- **@ccc-wiki** — primary destination. Full tool entity page for MCP server configuration patterns.
- **@osint-wiki** — brief documenting lspCallHierarchy for backtesting logic audits.
