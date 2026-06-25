---
title: no-mistakes — Git push proxy with disposable worktrees
type: entity
tags: [entity, tool, git, validation, ccc, k129]
keywords: [no-mistakes, kunchenguid, MIT, git proxy, pre-push validation, worktree]
related:
  - sources/eval-url-cemini-research-2026-06-25.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/tracer-acceptor-gate-ingest.md
  - concepts/npm-supply-chain-defense.md
maturity: draft
created: 2026-06-25
updated: 2026-06-25
---

## Relations

- @sources/eval-url-cemini-research-2026-06-25.md — K129 Adopt row (URL 2)
- @concepts/wiki-tooling-evaluation.md — Phase-0 registry
- @concepts/tracer-acceptor-gate-ingest.md — adjacent pre-ship validation gate pattern

## Raw Concept

Phase-0 prompted by K129 **Cemini URL Evaluation Research.docx** URL 2 — `kunchenguid/no-mistakes`.

## Narrative

**no-mistakes** is an MIT-licensed **local Git proxy** (Go) that spins up disposable worktrees to validate pushes before they reach remotes — lint, tests, and policy checks as a push gate.

**Phase-0 (2026-06-25):**

| Check | Result |
|-------|--------|
| License | **MIT** (`gh api` — SPDX MIT) |
| Hardcoded wiki layout | N/A — git tooling |
| Maturity | **2743★**, pushed 2026-06-23, 23 open issues |
| OSINT fit | **Adopt** — enforce pre-ingest / pre-commit validation on wiki git pushes |
| CCC-wiki fit | **Adopt** — agent harness safety layer alongside hooks |

**Posture:** **Adopt** for OSINT + CCC wikis. Pair with `ingest_session_gate.py` and `wiki_lint.py --fail-on-graph` — proxy catches what hooks miss on direct `git push`. Not deployed on cemini-prod (laptop research authoring only).

## Snippets

> "git push no-mistakes" [Source: https://github.com/kunchenguid/no-mistakes README tagline (retrieved 2026-06-25)]

## Dead Ends

- Docx "last commit NOT FOUND" — `gh api` shows active pushes; eval fetch gap only.
