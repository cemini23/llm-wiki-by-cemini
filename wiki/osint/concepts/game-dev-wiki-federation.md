---
title: Game dev wiki federation (cross-wiki)
type: concept
tags: [concept, meta, federation, game-dev-wiki]
keywords: [game-dev-wiki, godot, stronghold, castle-sim, agent-harness]
related:
  - concepts/gambling-wiki-federation.md
  - concepts/federated-daily-research-digest.md
  - entities/tools/claude-code-game-studios.md
  - "@ccc-wiki/concepts/deep-research-evaluation-prompt.md"
  - concepts/active-project-research-routing.md
  - sources/arxiv-2608.16859-harnesseval-w-2026-08-18.md
maturity: validated
created: 2026-06-13
updated: 2026-06-17
---

## Relations

- @game-dev-wiki/concepts/game-dev-wiki-scope.md — scope boundary (primary)
- @game-dev-wiki/concepts/agent-harness-castle-project.md — game-specific harness
- @game-dev-wiki/meta/cross-wiki-routing.md — ingest routing
- @ccc-wiki/entities/tools/claude-code-game-studios.md — role graph steal-from
- @ccc-wiki/concepts/deep-research-evaluation-prompt.md — v7 eval surface 8 (game-dev)
- @concepts/federated-daily-research-digest.md — per-wiki digest rollout

## Raw Concept

Pointer hub for the public **@game-dev-wiki** repo (`../projects/Game Dev wiki/`). OSINT keeps federation infra; game-dev-wiki keeps hobby castle/RTS research.

## Narrative

### Eval prompt (bulk URL batches)

Use `@ccc-wiki/concepts/deep-research-evaluation-prompt.md` (v7 body at `prompts/deep-research-multi-wiki-eval-v7-2026-06-13.md`) — nine surfaces; **game-dev-wiki** = surface 8 (hobby game dev, engines, agent-assisted slices).

### Split

| Topic | game-dev-wiki | osint-wiki / ccc |
|-------|---------------|------------------|
| Stronghold / castle sim design | **Primary** | cross-link only |
| Godot RTS vertical slice | **Primary** | — |
| Subagent orchestration primitives | stub | **@ccc-wiki** primary |
| CeminiSuite / PM bots | out of scope | **@osint-wiki** |
| Sprite/tile generation | requirements | **@image-gen-wiki** primary |

### Ingest routing

Sources teaching **how to build/design games** or **game-specific agent harness** → route stub to game-dev-wiki. Generic harness → `@ccc-wiki`. See `@game-dev-wiki/meta/cross-wiki-routing.md`.

## Snippets

*(none)*
