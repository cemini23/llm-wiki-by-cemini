---
title: OSINT Workspace (repo)
type: project
status: active
date: 2026-06-01
updated: 2026-06-01
tags: [project, architecture, cemini-internal, osint-wiki]
keywords: [llm-wiki-by-cemini, OSINT WORKSPACE, laptop curator, git wiki]
local-path: /Users/claudiobarone/Desktop/OSINT WORKSPACE
github: llm-wiki-by-cemini
ai-first: true
related:
  - projects/osint-workspace/Architecture/Architecture - Overview.md
  - projects/osint-workspace/Architecture/Architecture - Key decisions.md
  - concepts/cemini-repository-topology.md
  - concepts/librarian-server-architecture.md
  - concepts/laptop-prod-research-split.md
maturity: validated
---

## Relations

- @projects/osint-workspace/Architecture/Architecture - Overview.md — machine-maintained codebase map (`/obsidian-architect`)
- @projects/osint-workspace/Architecture/Architecture - Key decisions.md — repo ADRs and commit-mined decisions
- @concepts/cemini-repository-topology.md — why this repo stays separate from `Cemini-Financial-Suite`
- @concepts/librarian-server-architecture.md — `cemini-librarian` serving path for synced `wiki/`
- @concepts/laptop-prod-research-split.md — laptop curates; prod executes briefs only

## For future Claude

This note is the **project hub** for the git repo `OSINT WORKSPACE` (`llm-wiki-by-cemini`): schema (`CLAUDE.md`), curated `wiki/`, automation `scripts/`, laptop `conductor/` MCP shim, and `ui/` dev chat proxy. It is not the production trading stack — that lives in `Cemini-Financial-Suite` on `cemini-prod`. Refresh architecture from commit `b960aae` via `Architecture - Overview.md` (2026-06-01 scan).

## Overview

| Field | Value |
| --- | --- |
| **Role** | Financial/OSINT research librarian — ingest, wiki, briefs staging |
| **Canonical code path** | `/Users/claudiobarone/Desktop/OSINT WORKSPACE` |
| **Primary artifact** | `wiki/` (~1.3k markdown pages, git-tracked) |
| **Distribution** | Briefs → `/opt/cemini/briefs/` (user-gated); wiki → `cemini-librarian:/opt/cemini-wiki/wiki/` hourly sync |

## Architecture notes

- [[projects/osint-workspace/Architecture/Architecture - Overview|Architecture - Overview]]
- [[projects/osint-workspace/Architecture/Architecture - Key decisions|Architecture - Key decisions]]

## Recent activity

- **2026-06-01** — `/obsidian-architect` first pass: `projects/osint-workspace/Architecture/*` at scan commit `b960aae`.
- **2026-06-01** — obsidian-second-brain activated on this vault (`wiki/_CLAUDE.md`); SessionStart inject; bg agent off.

## Key decisions

See [[projects/osint-workspace/Architecture/Architecture - Key decisions|Architecture - Key decisions]] and @concepts/cemini-repository-topology.md for federation vs monorepo posture.
