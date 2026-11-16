---
title: "univer — headless spreadsheet engine and draft-worktree review (Apache-2.0 core)"
type: entity
related:
  - "@osint-wiki/sources/2026-11-16-deep-research-link-eval-agentic-harnesses.md"
  - "@osint-wiki/concepts/agent-link-evaluation-gates-v1013.md"
updated: 2026-11-16
---

## Raw Concept

Surfaced by
@osint-wiki/sources/2026-11-16-deep-research-link-eval-agentic-harnesses.md, URL 1,
**Extract** tier. Routed to Collectibles and Atto.

The question this page answers: **can an operator approve a generated spreadsheet
before it reaches the master manifest?**

## Narrative

### What it does

Univer is a TypeScript office-suite SDK — spreadsheets, documents, and slides — with
three parts that matter here:

- **`@univerjs/*`** — the editing runtime. Heavy, browser-based, not what we need.
- **`univer-cli`** — a local draft-and-review loop. It stages a change in an isolated
  worktree and opens a local viewer, so a human merges or discards before it lands.
- **`univer-node-backend`** — headless formula calculation and XLSX export in a Node
  worker.

### Why it fits Collectibles

Collectibles already computes grading economics. The repository holds
`consignment_manifest.py`, `grade_calc.py`, and `grading_dry_run.py`. [CONFIRMED —
local check 2026-11-16]

So the arithmetic is not the gap. The gap is the **review surface**: an operator
preparing a multi-tier PSA/BGS/CGC submission manifest currently inspects CSV output.
A local viewer with formula-checked cells gives a human gate that a CSV cannot.

The draft-worktree pattern also maps onto Atto concierge deliverables, where an agent
builds a tabular extraction for a client and a human signs it off before it ships.

### Why the editing runtime stays out

`@univerjs/presets` pulls a React or Vue editing stack. Collectibles is Python. Adding
a web office suite to review three columns of numbers is a poor trade.

Extract means: `univer-cli`'s draft-and-review shape, and `univer-node-backend` for
XLSX export and formula checking. Not the editor.

### Licence boundary

The open-source packages are Apache-2.0. The Pro plugins, Server SDK, and exchange
servers are commercially licensed and out of scope. Extraction must stay inside the
open-source `@univerjs/*` packages, `univer-cli`, and `univer-sdk-skills`.

### Risk

`univer execute` runs JavaScript without a sandbox. Treat any formula cell as code from
an untrusted source, and keep generated workbooks outside the master manifest until a
human approves them — which is Collectibles' existing hard ban on blind auto-listing,
so the rule already agrees.

### Status

Extract, design reference. Blocked from installation by the Workstation Harness Freeze.

## Snippets

> `univer-cli` provides an isolated draft Worktree review workflow and
> `univer-node-backend` provides headless spreadsheet and formula generation.
> [Source: Cemini Multi-Wiki Link Evaluation.docx, URL 1]

## Dead Ends

- **Embedding the full Univer editor.** Too heavy for a three-column review step in a
  Python project.
- **Trusting `univer execute`.** It runs JavaScript with no sandbox.
