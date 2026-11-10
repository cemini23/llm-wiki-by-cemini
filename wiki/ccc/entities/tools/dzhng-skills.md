---
title: "dzhng/skills — spec-slicing and review skills for coding agents (MIT)"
type: entity
tags: [tool, skills, claude-code, spec, review, game-time, mit]
keywords: [dzhng skills, write-spec, implement-spec, find-state-machines, auto-research, screenshot-critique]
related:
  - "@osint-wiki/sources/eval-multi-wiki-link-evaluation-2026-11-10.md"
  - entities/tools/worktrunk.md
maturity: draft
created: 2026-11-10
updated: 2026-11-10
---

## Raw Concept

Surfaced by @osint-wiki/sources/eval-multi-wiki-link-evaluation-2026-11-10.md, URL 14, **Integrate** tier. Routed to game-time, Atto, and Collectibles.

The question this page answers: **what does a mature agent skill library look like when it is about process rather than capability?**

## Narrative

### What it is

**MIT.** A collection of reusable agent skills for planning and building software, working across Claude Code, Codex, Cursor, and opencode.

Install: `npx skills add dzhng/skills`, or copy the folders.

### The four categories

| Category | Skills |
|----------|--------|
| **Engineering** | explore-unknowns, auto-research, **write-spec**, **implement-spec**, implement-spec-with-goal, implement-spec-with-codex, close-spec, handoff-spec, refactor-clean, port-features, write-tests, audit-tests, audit-performance, **find-state-machines**, find-overengineering, ratchet-files, write-docs, code-review, audit-decisions, retro, eli5, review, codex, claude, marketing-pages |
| **Visual review** | design-with-images, **compare-screenshots**, screenshot-critique, preview-shots |
| **Authoring** | write-skills, audit-agents, eval-skills |
| **Graphics** | renderer, launch-video, cinematic-shot, isometric-motion, xiaohei-illustrations |

### The pair that carries the Integrate

**`write-spec` → `implement-spec`** slices a feature into **independently verifiable, human-reviewable passes** with API seams and playable checkpoints at the end of each.

That is the same discipline this workspace already applies in two places — the frozen design log, and the "one milestone with an AI opponent" argument for game-time — expressed as an installable procedure rather than a written rule.

**`close-spec` and `handoff-spec`** are the underrated half. Most spec workflows have no defined end and no clean transfer, which is how a spec becomes a permanent open artefact nobody reads.

### Why this one is safe to adopt

It is a **skill library**, not a dependency. It writes instructions into a harness; it does not add runtime code, does not call a model, and does not touch data.

That is why it can be Integrate while the three Atto Extract items in the same batch all have blockers. Nothing in this library can leak a record.

### The specific fits

- **game-time** — `find-state-machines` and `auto-research` for tick loops and balance sweeps; `renderer` and `compare-screenshots` for the visual side.
- **Atto** — `write-spec`/`implement-spec` around the Intent contract.
- **Collectibles** — `audit-performance` and `ratchet-files` for a pipeline that has grown without a cleanup pass.

### Caveats

- Sub-skills like `implement-spec-with-codex` bind to a specific harness. Read before installing the whole set.
- A skill library is only as good as the person choosing which skills to run. Installing all 40 puts 40 procedures in front of the model.

### Status

Integrate. Install selectively, not wholesale.

## Snippets

> Skills install with `npx skills add dzhng/skills` or by copying the skill folders. Licence: "MIT". [fetched 2026-11-10]

## Dead Ends

- **Installing the entire library.** Pick the four or five that match the current phase.
