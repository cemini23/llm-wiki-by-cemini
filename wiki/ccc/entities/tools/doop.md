---
title: "doop — self-hosted design canvas with an MCP server (AGPL-3.0, not MIT)"
type: entity
tags: [tool, design, mcp, agpl, licence-trap, atto, game-time]
keywords: [doop, design canvas, mcp tools, agpl-3.0, pglite, self-hosted, screenshot loop]
related:
  - "@osint-wiki/sources/eval-multi-wiki-repository-revenue-2026-11-04.md"
maturity: draft
created: 2026-11-04
updated: 2026-11-04
---

## Raw Concept

Surfaced by @osint-wiki/sources/eval-multi-wiki-repository-revenue-2026-11-04.md, URL 11, **Extract** tier, routed to game-time and Atto.

The question this page answers: **can an agent iterate on a live interface it can also see?**

## Narrative

### What it is

An open-source design canvas, positioned as an alternative to Paper.design and Claude Design. Humans and agents design on it together in real time. **Frames render real HTML**, so what you see is the thing that will ship, not a mock.

The MCP server exposes **42 tools** — the report said 40; the README says 40 built-in plus two Linear tools from an extension. They cover canvases, frames, streaming HTML, **screenshots**, prototypes, comments, style guides, assets, and web imports.

The screenshot tool is the interesting one. It closes the loop an `unslop`-style audit otherwise has to work around: the agent edits, then **looks at** what it made, rather than reasoning about CSS and hoping.

Self-hosting is `bun run dev` or `docker compose up` with embedded PGlite; the canvas runs locally with no configuration.

### Phase-0, 2026-11-04 — the licence is the finding

**The report says "MIT — complies with Game-Time's zero-copyleft rule." That is wrong.**

The README states **GNU AGPL v3**. Self-hosting and modification are fine. Offering a modified version as a service means publishing your changes. The name and logo are trademarks, so a derived service needs a new brand.

**Consequences, in order of severity:**

1. **It cannot enter game-time.** Game-Time's stated rule is zero-copyleft production dependencies. AGPL is the strongest copyleft there is.
2. **It cannot ship inside an Atto kit.** Atto has commercial SKUs.
3. **It is usable as an operator-side development tool**, self-hosted, on loopback, with no redistribution — the same footing as @entities/tools/theatre.md's studio package.

**The second correction:** the canvas is local, the AI is not. Agents you connect yourself — Claude Code, ChatGPT, Cursor — "drive the canvas from outside, on your own subscription" and use their own hosted models. The built-in Doop Agent is off by default and needs a connected model account, or an Anthropic or Azure key.

So "self-hosted" describes the *canvas*. The design intelligence is a cloud model, which for Atto means the ban-4 question again: what is being sent, and to whom.

### Fit, honestly

- **Atto portals** — the vision fit is real (iterate on a page with an agent that can see it), but the licence confines it to a dev tool and the model path confines it to non-vault material.
- **game-time HUDs** — good fit for the workflow, disqualified as a dependency.
- **Collectibles** — no route described in the report; do not invent one.

### Status

Extract, **as an operator tool only**. Never a build dependency. The 42-tool surface and the screenshot loop are the ideas worth taking even if the tool is not used.

## Snippets

> "GNU AGPL v3. You can self-host and modify it, but offering a modified version as a service means you have to publish your changes." — README [fetched 2026-11-04]

> Agents "drive the canvas from outside, on your own subscription" and use their own hosted models. — README [fetched 2026-11-04]

## Dead Ends

- **Treating Doop as MIT.** It is AGPL-3.0. Bundling it into game-time or an Atto kit is the failure mode.
- **Reading "self-hosted" as "runs offline".** The canvas is local; the agent's model is not.
