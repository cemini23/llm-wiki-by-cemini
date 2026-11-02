---
title: "BoardUI — copy-and-own React Aria agent-chat components (MIT)"
type: entity
tags: [tool, frontend, react, accessible, design-system, atto]
keywords: [boardui, react aria, tailwind v4, agent chat, llms.txt, agents.md, semantic tokens]
related:
  - "@osint-wiki/sources/eval-multi-wiki-link-revenue-v10.10-batch-c-2026-11-02.md"
  - entities/tools/unslop.md
maturity: draft
created: 2026-11-02
updated: 2026-11-02
---

## Raw Concept

Surfaced by @osint-wiki/sources/eval-multi-wiki-link-revenue-v10.10-batch-c-2026-11-02.md, URL 19, **Extract** tier. Routed to Atto and Collectibles.

The question this page answers: **what should an agent-built interface start from, instead of a blank page?**

## Narrative

### What it is

Source components you copy into your repository and then own. Built on **React Aria** and **Tailwind v4**.

| Component | Purpose |
|-----------|---------|
| `agent-chat`, `agent-log`, `agent-thinking` | The chat surfaces every agent product needs |
| `app-shell` | Layout frame |
| Accessible data tables | The hardest component to get right |
| Stat cards | Numeric summaries |
| 400+ semantic tokens | One place to restyle everything |

**MIT** for the 69-component open-source repository. The 19-chart, 10-template Pro tier on boardui.com is commercial and separate.

### The design decision worth taking

Two things make this different from a component library.

**1. Accessibility is inherited, not added.** React Aria handles focus management, keyboard interaction, and screen-reader semantics. Those are the parts agents get wrong most often, because they are the parts a prompt does not describe.

**2. It ships agent-readable instructions** — an `AGENTS.md` and an `llms.txt` rule set. The components come with the rules for using them, in the form a coding agent reads.

That second point is the reason this belongs in a CCC page as well as a product page. Copy-and-own components with machine-readable usage rules is a pattern for making an agent produce consistent output without a long prompt.

### Fit with unslop

The pair works: BoardUI supplies a correct starting structure, @ccc-wiki/entities/tools/unslop.md audits and removes generic styling after the fact. Starting from a good base costs less than repairing a bad one.

### Caveats

- **Copy-and-own means you maintain it.** No upstream fix arrives automatically. That is the trade for full control.
- **Tailwind v4** — confirm the target project is on it before copying.
- The Pro tier is a separate commercial product. Nothing in the free repository requires it.

### Status

Extract. Source components, MIT, own them.

## Snippets

> "Delivers copy-and-own React Aria + Tailwind v4 source components (agent-chat, agent-log, agent-thinking, app-shell, accessible data tables, stat cards, and 400+ semantic tokens) plus an AGENTS.md / llms.txt rule set so Claude Code and Cursor build directly on…" — report, URL 19

## Dead Ends

- **Expecting upstream fixes.** Copy-and-own means the code is yours to maintain.
