---
title: Game dev wiki scope and sibling boundaries
type: concept
tags: [concept, meta, federation, scope]
keywords: [scope, boundary, ccc-wiki, image-gen-wiki, castle-sim, stronghold]
related:
  - concepts/scope-tiers.md
  - concepts/stronghold-deconstruction.md
  - concepts/agent-harness-castle-project.md
  - concepts/ai-assisted-game-dev-workflows.md
  - concepts/ai-game-dev-tool-stack-2026.md
  - meta/cross-wiki-routing.md
  - meta/daily-research-digest-cadence.md
  - sources/bootstrap-game-dev-wiki-2026-06-13.md
maturity: core
created: 2026-06-13
updated: 2026-06-13
---

## Relations

- @meta/cross-wiki-routing.md — ingest routing checklist
- @concepts/scope-tiers.md — hobby scope tiers
- @ccc-wiki/concepts/subagent-orchestration.md — generic harness (sibling)
- @image-gen-wiki/index.md — art pipeline sibling

## Raw Concept

Meta page defining what belongs in **game-dev-wiki** vs **@ccc-wiki**, **@image-gen-wiki**, and **@osint-wiki**.

## Narrative

### Primary home here

- Castle / RTS **design research** (Stronghold deconstruction, scope tiers)
- Engine Phase-0 evals (Godot, Unity, Bevy) for hobby project
- Vertical slice specs and milestone acceptance criteria
- Game-specific **agent harness** (planner/executor matrix for castle-sim milestones)
- **AI-assisted game dev** workflows, shipped case studies, Godot/Unity tooling landscape (game context)
- Reference game entities (Stronghold series) — design lens only

### Primary home in @ccc-wiki

- Subagent orchestration primitives, scatter-gather, harness frameworks
- Cursor audit model matrix, skill audits, MCP tooling
- Generic multi-wiki eval prompts (surface 8 = game-dev primary fit; surface 9 = CCC harness meta)

### Primary home in @image-gen-wiki

- ComfyUI workflows, sprite/tile generation, LoRA for art assets
- This wiki documents **import into Godot** and art requirements only

### Primary home in @osint-wiki

- CeminiSuite, trading stack, federation **sync scripts** (operator infra)
- Private agent code (poker arena, PM bots)

### Code boundary

Runnable game source lives in **separate repos** (`game-projects/` pointer). Public wiki = research + design + harness notes only.

## Snippets

> Operator direction: long-horizon Stronghold-inspired hobby sim; research wiki first, `castle-sim` repo after Phase 0. [Source: operator 2026-06-13]
