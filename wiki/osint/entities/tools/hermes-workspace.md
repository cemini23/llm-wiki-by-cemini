---
title: Hermes Workspace — web GUI for Hermes Agent
type: entity
tags: [tool, hermes, agent-ui, k113]
keywords: [hermes-workspace, outsourc-e, monaco, tmux, kb-server]
related:
  - sources/multi-wiki-tool-eval-v5-k113-2026-06-12.md
  - concepts/tool-evaluation-framework.md
  - concepts/librarian-server-architecture.md
  - "@ccc-wiki/entities/tools/hermes-workspace.md"
maturity: draft
created: 2026-06-12
updated: 2026-06-12
license_verified: MIT
---

## Relations

- @sources/multi-wiki-tool-eval-v5-k113-2026-06-12.md — K113 Adopt
- @concepts/librarian-server-architecture.md — optional kb-server graph browser
- @ccc-wiki/entities/tools/hermes-workspace.md — primary harness home

## Raw Concept

- **Repo:** `github.com/outsourc-e/hermes-workspace`
- **Tier:** Adopt → **CONDITIONAL-GO** (laptop Hermes GUI; not prod)
- **License:** MIT `[CONFIRMED]` 2026-06-12 (`gh api`)
- **Stars:** 5,652; pushed 2026-06-09

## Narrative

Native web workspace for Hermes Agent: streaming chat, PTY terminal, memory browser, skills inspector, Monaco editor. Node 22+ / Python 3.11+ stack.

**Integration vector (laptop):** parallel sessions outside Cursor; tmux workers; visual skill manager; optional kb-server REST edits to `/opt/cemini-wiki/wiki/` without polluting IDE context.

**Overlap:** lazy-tool + Cursor remain canonical for OSINT curation — Hermes workspace is **optional second surface** for long Hermes runs.

**Phase-0:** `bash scripts/adopt_k113_phase0.sh` — clone + README install smoke.

**NO-GO:** prod `/opt/cemini`, 24/7 trading path, librarian replacement.
