---
title: agent-skill-manager (asm) — Claude/Codex skill registry CLI
type: entity
tags: [tool, ccc, skills, cursor, adopt, k103]
keywords: [asm, luongnv89, skill-registry, claude-code, codex]
related:
  - sources/multi-wiki-tool-eval-v8-k103-2026-06-07.md
  - concepts/cemini-license-posture.md
  - "@ccc-wiki/entities/tools/agent-skill-manager.md"
  - concepts/claude-code-skills-md-workflow.md
maturity: draft
created: 2026-06-07
updated: 2026-06-07
phase_0_verdict: "CONDITIONAL-GO 2026-06-07 — MIT verified; path defaults (~/.claude/skills) require isolated test dirs before global symlink"
---

## Relations

- @sources/multi-wiki-tool-eval-v8-k103-2026-06-07.md — K103 eval Adopt
- @concepts/cemini-license-posture.md — MIT clears IP perimeter

## Raw Concept

- **URL:** https://github.com/luongnv89/asm
- **Tier:** Adopt (CCC-wiki primary)
- **License:** MIT (`gh api` + LICENSE file) [CONFIRMED 2026-06-07]
- **Stars / issues / push:** ~350★ / 27 open / 2026-06-03

## Narrative

TypeScript CLI for modular agent skill registries — batch ingest, `asm eval`, provider integrations for Claude Code and Codex. Complements `.cursor/mcp.json` lazy-tool routing without replacing conductor/kb-server.

**Phase-0 (2026-06-07):** CONDITIONAL-GO — laptop-only; pin version; never auto-symlink into prod paths. Failure mode: overwriting mixed-repo skill directories.

**Install:** `scripts/adopt_k103_phase0.sh` (optional asm clone to `~/.claude/skills/revfactory-harness` sibling path — document only unless operator enables).

## Snippets

> "Registry resolution + batch skill ingestion for Cursor IDE environments." [Source: Tool Evaluation and Wiki Fit.docx URL 1; K103]
