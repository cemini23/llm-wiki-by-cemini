---
title: "modern-web-guidance — modern web platform skill for agents (Apache-2.0)"
type: entity
related:
  - "@osint-wiki/sources/2026-11-16-deep-research-link-eval-agentic-harnesses.md"
  - "@osint-wiki/concepts/agent-link-evaluation-gates-v1013.md"
maturity: draft
created: 2026-11-16
updated: 2026-11-16
---

## Raw Concept

Routed from
@osint-wiki/sources/2026-11-16-deep-research-link-eval-agentic-harnesses.md, URL 6,
during the 2026-11-16 ingest. Graded **Integrate**.

The question this page answers: **how does an agent stop reaching for a polyfill or a
deprecated API it learned from old training data?**

## Narrative

A skill that keeps a coding agent current on the web platform: baseline browser
features, no-polyfill guidance, and accessibility rules. Apache-2.0, 7.9k stars, pushed
the day of the check.

Routed to game-time. The fit is narrow and real: game-time renders its HUD in the
browser, and most "browser bug" time in a slice is a stale feature assumption, not a
logic error.

Against our stack the gap is partly open — the project has no modern-platform reference
in `AGENTS.md`. Installation is blocked by the Workstation Harness Freeze, so the
extract is the baseline-feature checklist, written into the project's own agent notes.

### Shipped 2026-11-24 — `c08bd1a`

The checklist landed as **Section 5 of `AGENTS.md`** in game-time, alongside the UI
design loop in `docs/UI_DESIGN_LOOP.md`. Both are repo-local: no global skills, plugins,
MCP servers, or design services.

That is the shape the freeze allows — the rules live in the project's own agent notes
rather than in an installed skill.

## Snippets

> Keep your coding agent up to date with the latest web best practices.
> [Source: Cemini Multi-Wiki Link Evaluation.docx, URL 6, retrieved 2026-11-16]
