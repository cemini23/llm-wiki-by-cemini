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

## Cemini wiki federation

**Eight** interlinked markdown wikis plus the **Cemini Financial Suite** trading stack. Page bodies use `@<alias>/path/to/page.md` (aliases in `CLAUDE.md` → Related Wikis).

| Alias | Repository | Visibility | Focus |
|-------|------------|------------|--------|
| **`osint-wiki`** | **This repo** (`llm-wiki-by-cemini`) | **Private** | Financial / quant / prediction-market automation; librarian kb-server; CeminiSuite briefs |
| `gambling-wiki` | [Gambling-wiki](https://github.com/cemini23/Gambling-wiki) | **Public** | Sports betting, casino, poker, DFS, best ball; PM retail strategy |
| `game-dev-wiki` | [Game-Dev-wiki](https://github.com/cemini23/Game-Dev-wiki) | **Public** | Hobby game dev — castle/RTS research, Godot evals, agent harness |
| `ccc-wiki` | [cemini-claude-code-CCC](https://github.com/cemini23/cemini-claude-code-CCC) | **Public** | Cursor / Claude Code meta-wiki — MCP, skills, conductor, eval prompts |
| `image-gen-wiki` | [uncensored-image-gen-wiki](https://github.com/cemini23/uncensored-image-gen-wiki) | Public | Image / video / voice generation, persona ops |
| `seo-wiki` | [SEO-GEO-B-M-Wiki](https://github.com/cemini23/SEO-GEO-B-M-Wiki) | Public | Local SEO, GBP, GEO/AEO, creator marketing |
| `3d-printing-wiki` | [3D-Printing-Wiki](https://github.com/cemini23/3D-Printing-Wiki) | Public | FDM/FFF, Bambu, slicers, print farms |
| `cybersecurity-wiki` | [Cybersecurity-wiki](https://github.com/cemini23/Cybersecurity-wiki) | Public | Pentest, red team, SOC, certifications |
| *Cemini Financial Suite* | Private trading stack (`Cemini-Financial-Suite`; not a wiki) | **Private** | Production `/opt/cemini` — read-only from this workspace |

**Privacy:** This OSINT wiki and the financial suite are **private**. **`ccc-wiki`** and the **five public domain wikis** (including `gambling-wiki`) are on GitHub. Do not commit `.local/`, `briefs/`, or `hot.md`.

**Sync:** `scripts/sync_wiki_to_librarian.sh` (hourly cron + post-commit) rsyncs all seven wikis to `cemini-librarian:/opt/cemini-wiki/<alias>/wiki/`.

**Eval prompt:** `@ccc-wiki/prompts/deep-research-multi-wiki-eval-v7-2026-06-13.md` (nine surfaces; `gambling-wiki` = surface 3; `game-dev-wiki` = surface 8).

## Cemini media

- Newsletter: [Outlier Weekly](https://outlierweekly.substack.com)
- YouTube: [@Cemini23](https://www.youtube.com/@Cemini23)
