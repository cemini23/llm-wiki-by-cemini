---
title: "product-engineering — 45 release-gate skills from shipped products (MIT)"
type: entity
related:
  - "@osint-wiki/sources/2026-11-16-deep-research-link-eval-agentic-harnesses.md"
  - "@osint-wiki/concepts/agent-link-evaluation-gates-v1013.md"
updated: 2026-11-16
---

## Raw Concept

Surfaced by
@osint-wiki/sources/2026-11-16-deep-research-link-eval-agentic-harnesses.md, URL 18,
**Extract** tier. Routed to CCC and game-dev.

The question this page answers: **which checks belong between "code written" and
"code shipped"?**

## Narrative

### What it does

A skill pack of 45 checks drawn from three products that shipped. The ones that matter
here are the verification skills:

- **intended-versus-implemented** — compare the specification against the code that
  exists, and report the drift
- **independent review** — a fresh reviewer that does not see the author's reasoning
- **release gate** — a checklist that runs before a merge

Each skill is prose plus a procedure. There is no runtime.

### Why it fits

The federation already runs a review lane — `code-review` for defects, `simplify` for
quality. Those two read a diff. This pack adds the **specification** as an input, which
neither of ours does.

For game-time the relevant check is pre-release spec-versus-code verification: a slice
is described in a design note and built in `packages/`, and nothing currently compares
the two.

### Maturity

611 stars, pushed the day of the check, zero open issues. MIT.

### Why it does not install

Forty-five skills would land as 45 local skill files. The Workstation Harness Freeze
(Gate 3) blocks that. Extract the two or three procedures that fill a real gap —
intended-versus-implemented is the strongest — and write them into the projects' own
`AGENTS.md` or `CLAUDE.md`.

### Status

**SHIPPED in Atto — `b31dae4` (2026-11-24).** The intended-versus-implemented procedure
is a repo-local check, not an installed skill:

- `scripts/check-intended-vs-implemented.py`
- `docs/INTENDED_VS_IMPLEMENTED.md` — the procedure
- `docs/intended-vs-implemented-exceptions.txt` — 10 documented exceptions
- `reports/2026-11-24-intended-vs-implemented-pass.md` — first pass found 14 drift
  findings, 5 paths fixed, 0 broken refs or links

The frontend state checklist from the same pack also shipped as
`apps/desktop/STATE_CHECKLIST.md`, gated in `AGENTS.md` and enforced through the pull
request template. See @ccc-wiki/entities/tools/ag-ui.md for the third item in that
commit.

## Snippets

> 45 agent skills from shipping three live products: decide what to build, and how to
> verify it before release.
> [Source: Cemini Multi-Wiki Link Evaluation.docx, URL 18]

## Dead Ends

- **Installing all 45.** The freeze blocks it, and most overlap `code-review` and
  `simplify`.
