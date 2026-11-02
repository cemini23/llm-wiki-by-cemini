---
title: "design-log-methodology — frozen design, immutable implementation results"
type: entity
tags: [tool, agents, harness, methodology, ccc, specification]
keywords: [design log, null hypothesis, implementation results, frozen spec, cursor rules, claude.md]
related:
  - "@osint-wiki/sources/eval-multi-wiki-link-revenue-v10.10-batch-b-2026-11-01.md"
maturity: draft
created: 2026-11-01
updated: 2026-11-01
---

## Raw Concept

Surfaced by @osint-wiki/sources/eval-multi-wiki-link-revenue-v10.10-batch-b-2026-11-01.md, URL 16, **Extract** tier. Routed to CeminiDFS, Atto, Collectibles, and repo-wide `.cursor/rules/` plus `claude.md`.

The question this page answers: **how do you stop a coding agent from quietly changing the specification while implementing it?**

## Narrative

### The problem it names

An agent asked to implement a spec will, when it hits a contradiction, resolve the contradiction itself. The code then matches neither the spec nor the intent, and the drift is invisible after the fact because the spec was never edited.

### The mechanism

A version-controlled `./design-log/` folder replaces the long prompt.

| Phase | Rule |
|-------|------|
| Before changes | Read `./design-log/` first. Create a log and get approval for a new feature. |
| When authoring | Decisions for the Implementer (TL;DR) → Background → Problem → Prior Art. |
| When implementing | **The design section is frozen.** Do not edit it. Append an "Implementation Results" section. |

The **Implementation Results** section is immutable and additive. It records deviations and their reasons, test results such as `X/Y passing`, and a final summary of departures from the original design.

### The gate that carries the weight

"Minimize new surface (null hypothesis first)." Before any new code, the author must justify why the existing primitives do not suffice. That single rule blocks the most common agent failure: building a parallel implementation of something the repository already has.

Two other rules matter:

- **Read before writing.** The agent checks existing logs before touching code.
- **Cite with `file:line`.** Real code, real paths, real type signatures. Not descriptions of code.

### Portability — Phase-0, 2026-11-01

The repository ships `design-log.mdc`, a Cursor rule file. The README's Claude Code instruction says to "Copy the file [design-log-rules.md] into `claude.md`". So the content is portable text, not a Cursor-only artifact.

**Licence caveat.** The report states MIT. The README fetched on 2026-11-01 does **not** state a licence. The repository has 66 stars. Since the transferable asset is the **methodology** — a set of prose rules — this is not a blocker for use. Confirm the licence before copying files verbatim.

### Why it fits this workspace

This workspace already has the exact failure the methodology targets. The CLAUDE.md schema defines page types, frontmatter rules, and hard bans. A brief that quietly redefines those while implementing would be invisible.

The design log gives the missing audit trail: a frozen design, plus an append-only record of what actually happened.

### Status

Extract, **methodology only**. Confirm the licence before copying files.

## Snippets

> "Leave the initial section untouched, and append an 'Implementation Results' section as work progresses. That section should record deviations and their reasons, test results (e.g., X/Y passing), and a final summary of departures from the original design." [README, fetched 2026-11-01]

> "Justify why existing primitives don't suffice, and trace runtime behavior with `file:line` citations in the first draft." [README, fetched 2026-11-01]

> "The Claude Code instructions say to 'Copy the file design-log-rules.md into `claude.md`'" — so the rule content is portable even though the source file is a Cursor rule file. [fetched 2026-11-01]

## Dead Ends

- **Copying the rule file before the licence is confirmed.** The README states no licence. Use the methodology; verify before vendoring.
