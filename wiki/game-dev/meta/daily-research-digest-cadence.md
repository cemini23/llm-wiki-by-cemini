---
title: Daily research digest cadence (game-dev-wiki)
type: concept
tags: [meta, automation, discovery, k115, federation]
keywords: [daily-research-digest, exa, sweep, inbox, federated-digest]
related:
  - meta/cross-wiki-routing.md
  - concepts/game-dev-wiki-scope.md
  - sources/bootstrap-game-dev-wiki-2026-06-13.md
maturity: validated
created: 2026-06-13
updated: 2026-06-13
---

## Relations

- @osint-wiki/concepts/federated-daily-research-digest.md — federation install kit
- @meta/cross-wiki-routing.md — ingest routing

## Raw Concept

K115 federated install: morning **discovery-only** loop for Godot RTS, castle sim design, and agent-game-dev headlines.

## Narrative

| Field | Value |
|-------|-------|
| **Cadence** | Daily @ staggered local (`com.cemini.daily-research-digest.game-dev`) |
| **Installed** | 2026-06-13 (K115 bootstrap) |
| **Script** | `~/bin/cemini-daily-research-digest-game-dev` → `scripts/daily_research_digest_run.py` |
| **Config** | `scripts/daily_research_config.yaml` |
| **Report** | `wiki/sweeps/YYYY-MM-DD-daily.md` |
| **Template** | `wiki/sweeps/_daily-template.md` |
| **Inbox** | `research to be indexed/` |

### Operator loop

1. Review `wiki/sweeps/YYYY-MM-DD-daily.md`
2. Pick rows; say **full ingest** in Cursor with Game Dev wiki folder open
3. Weekly: optional Monokern on top ROADMAP topic

### Gates

Tier 3 autonomous ingest **NO-GO** — digest is candidates only.

Manual run:

```bash
python3 scripts/daily_research_digest_run.py
```

## Snippets

*(none)*
