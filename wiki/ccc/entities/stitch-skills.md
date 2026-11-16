---
title: "stitch-skills — design-to-code agent skills for Stitch MCP (Apache-2.0)"
type: entity
related:
  - "@osint-wiki/sources/2026-11-16-deep-research-link-eval-agentic-harnesses.md"
  - "@osint-wiki/concepts/agent-link-evaluation-gates-v1013.md"
maturity: draft
created: 2026-11-16
updated: 2026-11-16
---

## Raw Concept

Routed from
@osint-wiki/sources/2026-11-16-deep-research-link-eval-agentic-harnesses.md, URL 4,
during the 2026-11-16 ingest. Graded **Extract**.

The question this page answers: **how does an agent turn a screen description into UI
code it can then critique?**

## Narrative

A library of agent skills that drive Google's Stitch MCP server: turn a screen
description into UI code, then critique the render. Apache-2.0, 9.7k stars, last push
2026-08-17.

Routed to game-dev (strategy HUD design loop) and image-gen (screen generation and
visual critique), with CCC holding the skill architecture.

Relevant to game-time because the HUD is authored as browser UI, and a
description-first design step fits the clean-room slice workflow. Read for the loop
shape — describe, generate, critique — not for installation; the Workstation Harness
Freeze blocks new skills.

## Snippets

> A library of Agent Skills designed to work with the Stitch MCP server.
> [Source: Cemini Multi-Wiki Link Evaluation.docx, URL 4, retrieved 2026-11-16]
