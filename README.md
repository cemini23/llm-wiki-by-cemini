# Cemini OSINT Research Workspace

A local knowledge hub for OSINT and financial research, organized as an
LLM-curated, human-read wiki. This repo holds the **schema, the wiki, and
the helper scripts**. Raw sources live on a dedicated librarian server;
wiki pages are synced there for 24/7 MCP serving.

## What's tracked

| Path           | Role                                                              |
| -------------- | ----------------------------------------------------------------- |
| `CLAUDE.md`    | The schema — tells the LLM how to operate this workspace.         |
| `ROADMAP.md`   | Active workstream, decisions, and open questions.                 |
| `LESSONS.md`   | Meta-lessons about *how we work* (distinct from `wiki/log.md`).   |
| `wiki/`        | The library: `index.md`, `log.md`, `sources/`, `entities/`, `concepts/`. |
| `scripts/`     | Python helpers — docx extraction, stub generation, lint, gap detection. |
| `.gitignore`   | This file's enforcement layer.                                    |

## What's not tracked (and why)

- **`research to be indexed/`** — transient drop-zone for new sources awaiting
  ingest. Gitignored.
- **`briefs/`** — operational deliverables staged for distribution to
  claude.ai or the CeminiSuite dev stack. Gitignored.
- **`hot.md`** — session-state cache (curator working memory across
  compaction boundaries). Gitignored (changes every session).
- **`.local/`** — server connection details (SSH targets, IPs). Gitignored.
- **`.claude/settings.local.json`** — Claude Code per-project allowlist.
  Gitignored.
- **`.DS_Store`, `__pycache__/`, etc.** — OS and tooling cruft.

## Architecture — three layers + librarian server

1. **Raw sources** — immutable. Canonical location: `cemini-librarian:/opt/cemini-bulk/`
   (migrated from laptop 2026-04-28). Backed by Hetzner daily snapshots.
   - `research/` — ~283 PDFs and reports (642 MB)
   - `market-dataset/` — ~17.6k files of historical market data (1.6 GB)
   - **Read pattern**: `ssh cemini-librarian "cat /opt/cemini-bulk/research/<filename>"`
     or `scp` to `/tmp/` for local deep-read sessions.
   - **Drop pattern**: scp new sources to librarian after ingest; remove from laptop.

2. **The wiki** (`wiki/`, tracked) — LLM-written, human-read, cross-linked
   markdown pages with YAML frontmatter. ~455 pages. Synced to
   `cemini-librarian:/opt/cemini-wiki/wiki/` for 24/7 MCP serving via kb-server
   (FTS5 BM25, port 3838).

3. **The schema** (`CLAUDE.md`, tracked) — how the LLM runs the wiki.
   Co-evolves with the workspace.

4. **Librarian server** — dedicated Hetzner CPX21 (Ashburn, $13.99/mo, 3 vCPU,
   4 GB RAM, 80 GB NVMe). Runs kb-server (`willynikes2/knowledge-base-server`,
   MIT) on port 3838. Wiki synced hourly via `scripts/sync_wiki_to_librarian.sh`.
   See `@concepts/librarian-server-architecture.md` for the full plan.

See `CLAUDE.md` for the full operational schema (page formats, ingest
workflow, citation tags, distribution rules, session-start rituals).

## Distribution targets

The wiki is the librarian; consumers live elsewhere:

- **claude.ai** — context for conversations and writing tasks.
- **CeminiSuite** — the production trading stack on a Hetzner host.
  Connection details in `.local/server.md` (gitignored). This workspace
  ships briefs into `/opt/cemini/briefs/` only; everything else on the
  server is read-only from here.
- **Librarian MCP** — kb-server at `cemini-librarian:3838` serves wiki
  content to the Cemini production brain via MCP (Phase 4 wiring shipped,
  verification pending; server-stack scope).

## Getting started

```bash
# clone
git clone <this repo>
cd "OSINT WORKSPACE"

# scripts assume Python 3.11+ with python-docx; install as needed:
pip install python-docx

# raw sources are on the librarian server, not the laptop.
# verify connectivity:
ssh cemini-librarian "ls /opt/cemini-bulk/research/ | head -5"

# wiki lint (run after any wiki edit):
python3 scripts/wiki_lint.py

# wiki sync to librarian (or wait for hourly cron):
scripts/sync_wiki_to_librarian.sh
```

## Sister wikis

This is one of **six** interconnected Cemini knowledge wikis. Cross-wiki links use `@<alias>/path/to/page.md` syntax (aliases + paths in `CLAUDE.md` under "Related Wikis"):

- `osint-wiki` — this wiki (financial / quant / prediction-market research) · **private (not publicly available)**
- `image-gen-wiki` — uncensored image / video / voice generation
- `seo-wiki` — local SEO, GBP, GEO/AEO, creator marketing
- `3d-printing-wiki` — FDM/FFF printing, Bambu, slicers, print farms
- `cybersecurity-wiki` — offensive / defensive security research
- `ccc-wiki` — Cemini Claude Code meta-wiki (workflow, subagents, MCP/conductor) · **private (not publicly available)**

This OSINT wiki is a **private repository — not publicly available**. It holds financial research plus connection details for the Cemini production stack; it is not published, mirrored, or open-sourced. The CCC meta-wiki is likewise private. The other four sister wikis are public.
