---
title: "jev-recipes — 248 small typed decisions for JavaScript and TypeScript (MIT)"
type: entity
related:
  - "@osint-wiki/sources/2026-11-16-deep-research-link-eval-agentic-harnesses.md"
  - "@osint-wiki/concepts/agent-link-evaluation-gates-v1013.md"
  - "@osint-wiki/entities/tools/neo4jev.md"
updated: 2026-11-16
---

## Raw Concept

Surfaced by
@osint-wiki/sources/2026-11-16-deep-research-link-eval-agentic-harnesses.md, URL 11,
**Extract** tier. Routed to Collectibles, GuruWatcher, CeminiParlays, and game-time.

The question this page answers: **what does a Jev decision look like when it is small,
local, and repeatable?**

## Narrative

### What it does

A recipe collection, not a framework. Each recipe is a single narrow decision in
JavaScript or TypeScript — route this request, rerank these results, pick one label,
extract one field — written as a Jev step with a bounded choice set.

The value is the **shape**: every recipe declares its candidates, its confidence, and
its fallback. That makes a decision auditable after the fact, which free prompts are
not.

### Locality — the difference from neo4jev

This is the opposite case to @entities/tools/neo4jev.md. `neo4jev` needs a remote
`system_one` call per hop and fails without a key. `jev-recipes` runs against a local
backend.

Always check the backend. The Jev family name says nothing about where inference runs.

### Where it fits

- **Collectibles** — sold-comp disambiguation. "Which of these five eBay sold listings
  is the same card in the same grade" is a bounded choice with a confidence, which is
  exactly the recipe shape.
- **CeminiParlays** — offline replay auditing. A typed decision per leg replays
  deterministically, so a past slip can be re-graded without a model call.
- **GuruWatcher** — claim triage on newsletter text.
- **game-time** — action evaluation in an offline loop.

### Maturity signal

37 stars, pushed 2026-11-06, zero open issues. Small and recent. That is a reference
library, not a dependency: take the recipe structure and write the few decisions the
projects actually need.

### Status

Extract, design reference. MIT, local, and small enough to read in one sitting.

## Snippets

> 248 small Jev decisions for JavaScript and TypeScript: route, rerank, extract.
> [Source: Cemini Multi-Wiki Link Evaluation.docx, URL 11]

## Dead Ends

- **Generalising locality across the Jev family.** `neo4jev` is hosted; this one is
  local. Check each backend.
- **Adding the package for one decision.** Copy the shape.
