---
title: Claude-Code-Game-Studios Phase-0 audit — 2026-06-13
type: source
tags: [source, phase-0, ccgs, claude-code, audit]
keywords: [ccgs, claude-code-game-studios, steal-from, harness]
related:
  - entities/tools/claude-code-game-studios.md
  - concepts/ccgs-workflow-extraction.md
  - sources/ccgs-workflow-catalog-2026.md
read_status: read
source_type: operator-audit
source_url: https://github.com/Donchitos/Claude-Code-Game-Studios
maturity: validated
created: 2026-06-13
updated: 2026-06-13
---

## Raw Concept

Phase-0 audit of **Donchitos/Claude-Code-Game-Studios** — harness framework, not a runtime game dependency.

## Narrative

### Method

Clone @ main (2026-05-13) to `/tmp/phase0-audit/Claude-Code-Game-Studios`. Inventory `.claude/agents` (49), `.claude/skills` (73), `workflow-catalog.yaml`.

### Checks

| Gate | Result |
|------|--------|
| License | **MIT** [CONFIRMED] |
| Maturity | ~21k★, active releases (v1.0.0 May 2026) |
| Runtime requirement | **Claude Code only** — not Cursor-native |
| Content | Shell + markdown agents/skills; no malicious binaries in root audit |
| Value | Workflow phases, artifact gates, vertical-slice skill |
| Risk | Vendor lock-in to Anthropic Claude Code; learning curve; self-discipline still required |

### Verdict for game-dev-wiki

| Use case | Verdict |
|----------|---------|
| Full install in Cursor | **NO-GO** — wrong host product |
| Steal workflow + P0 skills | **GO** — @concepts/ccgs-workflow-extraction.md |
| Steal agent role graph | **GO** — @entities/tools/claude-code-game-studios.md |

Overall: **STEAL-FROM / CONDITIONAL-GO** (patterns only).

## Snippets

Port guide: @concepts/ccgs-workflow-extraction.md — map to wiki + briefs + Codex swarms.
