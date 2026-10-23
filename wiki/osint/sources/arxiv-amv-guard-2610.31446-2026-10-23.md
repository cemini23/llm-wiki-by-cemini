---
title: "AMV-GUARD — when is a memory safe enough to act on?"
type: source
related:
  - concepts/k294-osint-wave.md
  - concepts/options-agent-order-boundary.md
maturity: draft
read_status: skimmed
updated: 2026-10-23
---

## Raw Concept

Title: When is a memory safe enough to act on?
Authors: Yiqi Wang and coauthors
Type: arXiv preprint (2610.31446), 23 Oct 2026
Inbox file: `research to be indexed/osint/arxiv-2610.31446-when-is-a-memory-safe-enough-to-act-on-action-co.pdf`
Location: `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.31446-when-is-a-memory-safe-enough-to-act-on-action-co.pdf`
Retrieved: 2026-10-23
Read status: skimmed (abstract)

## Narrative

The same remembered fact can be used unchecked for a routine action. It must be re-checked before a high-consequence one.

A verification is worth its cost only if it can change the next action. AMV-GUARD extracts the premises of a candidate action and picks checks by bounded value of information.

On ToolSandbox, against a static policy with the same inputs:

| Measure | Result |
|---|---|
| Mean verification cost | **-33.9%** |
| Safe-proceed recall | **100%** |
| Gate harmful | **0%** |
| Proceed coverage | **38.83% to 44.17%** |

On an AppWorld transfer of the stopping core only, verification cost fell **21.3%**, with a small loss in safe-proceed recall and task success.

The check earns its place only when it can move the action. **No install. No trade.**
