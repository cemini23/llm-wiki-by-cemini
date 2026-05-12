---
title: "Ducky — Desktop GUI All-in-One (REJECT)"
type: entity
tags: [tool, desktop-gui, tauri, reject-tier, k39]
keywords: [ducky, desktop gui, headless mismatch]
related:
  - sources/evaluating-project-links-stacks.md
  - concepts/tool-evaluation-framework.md
maturity: draft
created: 2026-05-11
updated: 2026-05-11
---

## Relations
- `@sources/evaluating-project-links-stacks.md` — source evaluation brief (URL 10)
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied

## Raw Concept

- **Repo / URL** (per source brief): `github.com/thecmdguy/Ducky`
- **Tier (per source brief)**: **Reject**
- **License**: not located in eval brief — irrelevant given architectural veto

## Narrative

Desktop GUI application (likely Tauri / Electron). Eval brief rejects on fundamental headless-infrastructure mismatch.

### Integration vector

**Reject** — Cemini's Hetzner stack is headless; developer workflow is CLI/TUI-centric (Claude Code in terminal). Desktop GUI tooling has no fit on any of the three surfaces (Cemini-prod / Wiki-librarian / Workflow-laptop).

### Why not even Reference-only

Generic desktop-app patterns — no novel architecture worth extracting.

[Source: Evaluating Project Links for Stacks.docx URL 10; retrieved 2026-05-11]
