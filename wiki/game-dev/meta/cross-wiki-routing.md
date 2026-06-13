---
title: Cross-wiki routing (game-dev vs ccc vs image-gen)
type: concept
tags: [meta, routing, federation]
keywords: [routing, ccc-wiki, image-gen-wiki, osint-wiki, ingest]
related:
  - concepts/game-dev-wiki-scope.md
  - meta/daily-research-digest-cadence.md
  - sources/bootstrap-game-dev-wiki-2026-06-13.md
maturity: core
created: 2026-06-13
updated: 2026-06-13
---

## Relations

- @concepts/game-dev-wiki-scope.md — full boundary table
- @osint-wiki/concepts/game-dev-wiki-federation.md — OSINT pointer hub

## Raw Concept

Ingest routing when a source touches game design, agent harness, or art pipeline.

## Narrative

### Stay in game-dev-wiki

- Godot/Unity/Bevy tutorials for RTS or building sims
- Stronghold / castle sim design analysis
- Hobby scope, milestone specs, playtest gates
- Game-specific agent harness notes

### Route to @ccc-wiki (stub + brief)

- Generic subagent orchestration, Cursor skills, MCP infra
- Multi-wiki eval prompt updates (surface 9)

### Route to @image-gen-wiki

- ComfyUI workflows, sprite generation, tile sets
- Stub here with art requirements + Godot import notes

### Route to @osint-wiki

- Federation sync scripts, librarian deploy, CeminiSuite
- Private poker/PM bot code

### Bulk URL evaluation

Use `@ccc-wiki/concepts/deep-research-evaluation-prompt.md` (v7 body at CCC `prompts/deep-research-multi-wiki-eval-v7-2026-06-13.md`) — **game-dev-wiki** = surface 9.

From OSINT ingest: `python3 scripts/cross_wiki_route.py --target-wiki game-dev-wiki`

## Snippets

*(none)*
