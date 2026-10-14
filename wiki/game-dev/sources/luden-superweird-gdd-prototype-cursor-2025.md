---
title: Luden.io — GDD to prototype with Cursor, Zed, LÖVE (2025)
type: source
tags: [source, case-study, cursor, gdd, prototype, loven2d]
keywords: [luden, superweird, cursor, gdd, prototype, tiled]
related:
  - concepts/ai-assisted-game-dev-workflows.md
read_status: partial
source_type: blog
source_url: https://blog.luden.io/generating-prototypes-from-game-design-document-with-cursor-zed-and-l%C3%B6ve-
maturity: tentative
created: 2026-06-13
updated: 2026-06-13
---

## Raw Concept

Luden.io experiment: automate **SuperWEIRD** prototypes from markdown GDD using Cursor/Zed agent mode + LÖVE 2D + Tiled.

## Narrative

### Stack [CONFIRMED — Exa snippet; full article 404 at fetch time]

- IDEs: Cursor / Zed agent mode
- Models: ChatGPT 4.1, Claude 4
- Docs: markdown GDD + style guide + task list
- Graphics: procedural code-defined art
- Levels: Tiled Map Editor
- Engine: LÖVE (CLI-friendly Lua)

### Outcome [CONFIRMED — article summary]

- Approach **did not work as planned** for full automation
- Still transformed SuperWEIRD pre-production in unexpected ways
- Sources published for others to replicate experiments

### Lesson for wiki operators

GDD-driven prototype generation = useful **exploration** tool, not replacement for design iteration. Pair with honest postmortem when automating pre-prod.

## Dead Ends

- Full article body needs operator fetch or NotebookLM pass — upgrade `read_status` when available
