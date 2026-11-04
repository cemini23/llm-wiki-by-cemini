---
title: "scenario-labs/skills — MIT skill set, but every generation needs Scenario's cloud"
type: entity
tags: [tool, agents, skills, image-gen, vendor-lock, game-time]
keywords: [scenario skills, baseline plus delta, grid maker, quality gate, creative units, mcp]
related:
  - "@osint-wiki/sources/eval-multi-wiki-link-revenue-v10.11-2026-11-03.md"
maturity: draft
created: 2026-11-03
updated: 2026-11-03
---

## Raw Concept

Surfaced by @osint-wiki/sources/eval-multi-wiki-link-revenue-v10.11-2026-11-03.md, URL 16, **Extract** tier. Routed to game-time, Basgiath, and Collectibles.

The question this page answers: **what can you take from a vendor skill library without taking the vendor?**

## Narrative

### What it is

A large library of `SKILL.md` files for Claude Code, Cursor, Codex, and Copilot. **MIT.**

Broad coverage: images, multi-reference, product shots, brand kits, storyboards, game assets, sprite animation, side-view game kits, textures, skyboxes, 3D, video, audio, UGC, reels, consistency, identity libraries, model training, asset analysis, quality gates, refine loops.

**Two classes of skill:**

| Class | Requirement |
|-------|-------------|
| Generation skills | **Scenario's MCP server** at `mcp.scenario.com`, an account or API key, and **"Creative Unit" credits** |
| Expert tools | A locally installed DCC app — ZBrush, Blender, Maya, Unreal, Unity, Godot, Roblox Studio |

### Phase-0, 2026-11-03 — the cost gate is vendor-scoped

The report extracts a "pre-spend cost-estimation" pattern. What the repository actually ships is **cost estimation for Scenario credits**. It is not a general model of what a generation will cost; it is a meter for that vendor's currency.

That distinction decides the whole adoption.

The three patterns still worth taking, because they are ideas rather than dependencies:

1. **Baseline-plus-delta prompt architecture.** Generate a canonical baseline once, then express every variant as a delta from it. That is how consistency is held across a sprite set without re-describing everything each time.
2. **Grid Maker sprite sheets.** Author sheets on a grid so frames stay registered — a layout convention, not a service.
3. **Quality Gate grading against a brief.** An automated check that compares a generated asset to the stated brief before it enters the build.

### Where the vendor cloud does not fit

- **Collectibles.** The pre-grade pipeline is local-first by construction. Sending card images to a third-party generation cloud crosses that boundary, and the report's own hard ban on unverified blind-comp auto-listing applies.
- **Basgiath.** Fan-made, non-monetised, and constrained by the ban on official art. Paying per credit to generate assets is a cost against a project that must not earn revenue.
- **game-time.** Plausible, but the project does not exist yet, and a per-credit dependency is the wrong first commitment for a project at day zero.

### The licence note

The report correctly separates the two repositories: **`scenario-labs/skills` is MIT**, while the separate **`scenario-labs/blender-plugin` is GPL-3.0**. Do not conflate them.

### Status

Extract, **patterns only**. No account, no key, no credits.

## Second sighting — 2026-11-04, and the claim that keeps reappearing

`@osint-wiki/sources/eval-multi-wiki-repository-revenue-2026-11-04.md` URL 8 rates it **Extract** again and states: *"MIT — complies with Game-Time's zero-copyleft production dependency requirement."*

**That sentence is true and misleading at the same time.** The repository licence is MIT; the skills are not usable without Scenario's MCP server, an account or API key, and paid Creative Unit credits. A zero-copyleft *dependency* requirement is satisfied; a **zero-cost, zero-vendor, offline-first** requirement is not, and Game-Time's stated constraints include offline-first.

This is the second batch to make the same framing error, so it is worth naming as a standing correction: **for this repository, quote the licence and the vendor requirement in the same sentence, every time.** A licence check that stops at the LICENSE file will keep passing this and keep missing the dependency.

## Snippets

> "Most skills rely on the Scenario MCP server at `https://mcp.scenario.com/mcp`." Usage is measured in "Creative Unit" credits. [README, fetched 2026-11-03]

> "License: MIT." [README, fetched 2026-11-03]

## Dead Ends

- **Reading the pre-spend cost gate as a general cost model.** It meters Scenario credits.
- **Using the generation skills for Collectibles.** Card images would leave the machine.
