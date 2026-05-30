---
name: cemini-wiki-graph
description: >-
  Obsidian graph + backlink review ritual for the OSINT git wiki before commit.
  Use when curating wiki pages in Obsidian, reviewing orphans/backlinks visually,
  or when the user asks for graph review, Obsidian curation, or pre-commit wiki
  health check alongside wiki_lint.py. Complements kepano obsidian-skills in
  .agents/skills/. Canonical path remains git wiki/ + @path syntax.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
---

# Cemini wiki graph curation (Obsidian overlay)

## Setup (once)

```bash
bash scripts/setup_obsidian_vault.sh --open
```

Vault root = `wiki/` (same files git tracks). `.obsidian/` is local-only (gitignored).

## Pre-commit ritual (5 min)

1. Run mechanical lint: `python3 scripts/wiki_lint.py --fail-on-graph`
2. Open Obsidian **Graph view** on `wiki/` — orphans highlighted (`showOrphans: true`)
3. For each orphan cluster: add `related:` backlink or stub page per CLAUDE.md
4. **Backlinks pane** on edited pages — confirm bidirectional edges match `related:`
5. Commit wiki changes; post-commit hook syncs librarian

## /save pattern (claude-obsidian adapted)

When persisting chat insights to the wiki (Steal-from @sources/agriciDaniel-claude-obsidian.md):

1. Pick page type: source | entity | concept
2. Write YAML frontmatter per CLAUDE.md (type, maturity, related, dates)
3. Sections: Relations → Raw Concept → Narrative → Snippets
4. Add bidirectional `related:` on all `@path` targets
5. Update `wiki/index.md` + append `wiki/log.md` for ingests

Do **not** create a second canonical vault — all saves land in `wiki/*.md` in this repo.

## When to use Obsidian vs Cursor

| Task | Tool |
|------|------|
| Agent ingest / lint / Exa | Cursor + lazy-tool |
| Graph orphan hunt / human skim | Obsidian graph |
| Served RAG | kb-server on librarian |
| Episodic memory | stash MCP |
