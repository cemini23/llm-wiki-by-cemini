---
title: "estella — TypeScript game engine over a C++/WebAssembly core (Apache-2.0)"
type: entity
related:
  - "@osint-wiki/sources/2026-11-16-deep-research-link-eval-game-media.md"
  - "@osint-wiki/concepts/agent-link-evaluation-gates-v1013.md"
updated: 2026-11-16
maturity: draft
---

## Raw Concept

Surfaced by
@osint-wiki/sources/2026-11-16-deep-research-link-eval-game-media.md, URL 10,
**Extract** tier. Routed to game-time.

The question this page answers: **what does a mature ECS look like when the authoring
layer is TypeScript and the hot path is native?**

## Narrative

### What it does

A 2D and 3D engine. The pattern is the split:

- **Authoring in TypeScript** — entity, component, and system definitions are ordinary
  TypeScript, so an agent can read and write them.
- **Execution in C++/WebAssembly** — the tick loop and rendering run native.
- **SDK boundary** — the TS surface is the API; the Wasm core is opaque.

### Why it is relevant

game-time and castle-sim both need a component model that an agent can reason about.
The interesting claim here is not the engine but the **boundary discipline**: a small,
typed, agent-readable surface in front of a native core that never appears in the
agent's context.

That is the same shape as the ReplayKit and slice work — keep the model's view narrow
and typed.

### What extract means

Read the architecture. Do not swap engines. game-time already has a renderer and a
slice pipeline; replacing them is out of scope and would break the shipped work.

Take: the ECS naming, the system-ordering rules, and the way the TS SDK hides the Wasm
boundary.

### Maturity

938 stars, pushed the day of the check, 9 open issues, Apache-2.0. Newer and smaller
than the big engines, which is why the architecture is legible.

### Status

Extract, architecture reference only.

## Snippets

> A fast 2D and 3D game engine — TypeScript SDK, C++/WebAssembly core.
> [Source: Cemini Multi-Wiki Link Evaluation (1).docx, URL 10]

## Dead Ends

- **Replacing the game-time renderer.** Out of scope; the shipped slice depends on it.
