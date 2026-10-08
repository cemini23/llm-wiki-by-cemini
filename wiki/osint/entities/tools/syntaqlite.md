---
title: "syntaqlite — SQLite SQL parser, linter, and language server"
type: entity
tags: [tool, sqlite, lint, lsp, atto, apache-2.0, k285]
keywords: [syntaqlite, sqlite, static-analysis, lsp, formatter, atto-vault, k285]
related:
  - sources/eval-github-repository-revenue-2026-10-08.md
  - concepts/k285-eval-wave.md
maturity: draft
created: 2026-10-08
updated: 2026-10-08
---

## Relations

- @sources/eval-github-repository-revenue-2026-10-08.md — K285 eval (tier: **Extract**)
- @concepts/k285-eval-wave.md — K285 cluster hub

## Raw Concept

- **Repo:** `github.com/LalitMaganti/syntaqlite`
- **Tier (K285):** **Extract** (route: Atto vault; GuruWatcher ledgers)
- **License:** **Apache-2.0** (verified 2026-10-08)
- **Stars:** 823 (verified)
- **Description:** "A fast parser, formatter, static analyzer, and language server for SQLite SQL"

## Narrative

A **parser, formatter, static analyzer, and language server for SQLite SQL**.

### Why it matters here

SQLite backs the Atto vault tables and the GuruWatcher ledgers. A **static analyzer** catches **silent schema and syntax mismatches** before they corrupt a table — the same "lint before it bites" role the workspace's gate chain plays for code.

### Play

Run `syntaqlite` as a static check wherever the project ships SQLite SQL. Cheap, Apache-2.0, no runtime dependency.

### Boundary

FILE only. No install this session.

## Snippets

> "A fast parser, formatter, static analyzer, and language server for SQLite SQL." [Source: eval-github-repository-revenue-2026-10-08.md, Phase-0 verified]
