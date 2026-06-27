---
title: no-mistakes — Git push proxy with disposable worktrees
type: entity
tags: [entity, tool, git, validation, ccc, k129]
keywords: [no-mistakes, kunchenguid, MIT, git proxy, pre-push validation, worktree]
related:
  - sources/eval-url-cemini-research-2026-06-25.md
  - sources/eval-tool-routing-hermes-plan-2026-06-27.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/tracer-acceptor-gate-ingest.md
  - concepts/npm-supply-chain-defense.md
maturity: draft
created: 2026-06-25
updated: 2026-06-27
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

## Setup

### macOS Build from Source

```bash
# Clone repository
mkdir -p "/Users/claudiobarone/Projects/tools"
cd "/Users/claudiobarone/Projects/tools"
git clone https://github.com/kunchenguid/no-mistakes.git

# Build binary
cd "/Users/claudiobarone/Projects/tools/no-mistakes"
make build

# Verify build
"/Users/claudiobarone/Projects/tools/no-mistakes/bin/no-mistakes" --version
# Output: no-mistakes version v1.31.2 (3c09496) 2026-06-27T13:00:24Z
```

Binary path: `/Users/claudiobarone/Projects/tools/no-mistakes/bin/no-mistakes`

### Repository Configuration

Initialize the gate in the target repository (run from repo root):

```bash
cd "/Users/claudiobarone/Desktop/OSINT WORKSPACE"
"/Users/claudiobarone/Projects/tools/no-mistakes/bin/no-mistakes" init
```

This creates:
- **Gate bare repo**: `/Users/claudiobarone/.no-mistakes/repos/906f23429d36.git`
- **Git remote `no-mistakes`**: pointing to the local gate
- **Agent skill**: `/no-mistakes` installed for Claude Code

### Remote Configuration Result

```
git remote -v
no-mistakes	/Users/claudiobarone/.no-mistakes/repos/906f23429d36.git (fetch)
no-mistakes	/Users/claudiobarone/.no-mistakes/repos/906f23429d36.git (push)
origin	https://github.com/cemini23/llm-wiki-by-cemini.git (fetch)
origin	https://github.com/cemini23/llm-wiki-by-cemini.git (push)
```

### Usage

Push through the gate instead of origin:

```bash
git push no-mistakes <branch>
```

The proxy spins up a disposable worktree, runs the validation pipeline, and forwards to origin only after all checks pass.

## Snippets

> "git push no-mistakes" [Source: https://github.com/kunchenguid/no-mistakes README tagline (retrieved 2026-06-25)]

## Dead Ends

- Docx "last commit NOT FOUND" — `gh api` shows active pushes; eval fetch gap only.
