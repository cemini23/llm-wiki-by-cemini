---
title: Claude operating manual (Cemini OSINT wiki vault)
type: meta
tags: [meta, obsidian-second-brain, claude-code, vault-manual]
keywords: [obsidian-second-brain, _CLAUDE.md, vault, session-start]
related:
  - sources/obsidian-second-brain-eugeniughelbur.md
maturity: core
created: 2026-06-01
updated: 2026-06-01
---

## Relations

- @dashboard.md — Obsidian Dataview hub; same vault root
- @index.md — page catalog
- @log.md — ingest/query chronology
- @sources/obsidian-second-brain-eugeniughelbur.md — upstream tool eval + adoption

# Claude operating manual — Cemini OSINT wiki vault

> Read this before any `/obsidian-*` command or vault write in this directory.
> Canonical schema for ingest/lint lives one level up: `../CLAUDE.md` (workspace root).

## Vault identity

- **This is the git wiki** (`wiki/`), not a personal PKM vault. Structure: `sources/`, `entities/`, `concepts/`, `sweeps/`, `meta/`.
- **Catalog:** `index.md` (human + agent index). **Ops log:** `log.md` (append-only ingest/query entries). Do not replace these with obsidian-second-brain `Logs/` layout without operator approval.
- **Links:** use `@path/to/page.md` in prose (Cemini convention). Obsidian `[[wikilinks]]` are optional in body text only; do not rename paths to match Obsidian graph alone.

## Background agent — OFF

`OBSIDIAN_BG_AGENT_ENABLED` must stay **unset** for this vault. PostCompact headless writes use `--dangerously-skip-permissions` and assume `People/`, `Projects/`, `Daily/` folders — incompatible with curated wiki ingest. Use explicit slash commands and normal agent edits with git review instead.

## Write rules (mandatory)

1. **Git-tracked** — every change must be reviewable (`git diff`). No silent bulk merges.
2. **Proposals first** for experimental refactors: write under `/tmp/cemini-osb-proposals/`, then copy in after human OK.
3. **No delete/move/archive** of wiki pages unless operator requests (aligns with obsidian bg-agent safety constraint).
4. **Frontmatter** — follow `../CLAUDE.md` wiki page format (`type`, `maturity`, `related`, `updated`).
5. **Bidirectional `related:`** — if A links B, update B's `related` and `## Relations`.
6. **Never run on librarian** — `cemini-librarian:/opt/cemini-wiki/` is read-only from laptop automation.

## What works here

- **SessionStart** vault context (`load_vault_context.py`) — enabled.
- **Slash commands** — `obsidian-architect`, `obsidian-research`, etc., when they respect paths above.
- **Skip** default `/obsidian-init` — would regenerate `index.md` / `Logs/` and fight existing Cemini layout.

## Operator

- Policy: `../.local/obsidian-second-brain-cemini-policy.md` (gitignored).
- Health: `python3 ~/.claude/skills/obsidian-second-brain/scripts/vault_health.py --path "<this vault>"` (Obsidian-link metrics; orphan counts are expected for `@path` wikis).
