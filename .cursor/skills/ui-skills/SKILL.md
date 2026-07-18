---
name: ui-skills
description: >-
  Route frontend / TipDrop UI work through ibelick/ui-skills (baseline-ui,
  improve-ui, fixing-*). Use when polishing UI, removing AI slop, motion,
  a11y, or metadata. Prefer /baseline-ui and npx ui-skills start.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
---
# ui-skills (K173 Extract)

Canonical clone: `.local/adopts/ui-skills` (MIT). Skill packs live at `.local/adopts/ui-skills/skills/` (also symlinked into TipDrop `.cursor/skills/ui-skills/skills` after `bash scripts/adopt_k173_local.sh`).

## Agent must

1. For TipDrop or any React/Tailwind UI task, read the relevant skill under `.local/adopts/ui-skills/skills/` (`baseline-ui`, `improve-ui`, `fixing-*`).
2. Default to **baseline-ui** constraints before inventing layout chrome.
3. Operator shortcut: `cd .local/adopts/ui-skills && npx ui-skills start` (or `npx ui-skills categories`).

## Do not

- Re-clone PostHog to get analytics UI.
- Vendor AGPL tools (wigolo) into TipDrop.
