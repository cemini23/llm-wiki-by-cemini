# Cemini OSINT Research Workspace

A local knowledge hub for OSINT and financial research, organized as an
LLM-curated, human-read wiki. This repo holds the **schema, the wiki, and
the helper scripts**. Raw sources, market data, and operational outputs
live locally and are gitignored.

## What's tracked

| Path           | Role                                                              |
| -------------- | ----------------------------------------------------------------- |
| `CLAUDE.md`    | The schema — tells the LLM how to operate this workspace.         |
| `LESSONS.md`   | Meta-lessons about *how we work* (distinct from `wiki/log.md`).   |
| `wiki/`        | The library: `index.md`, `log.md`, `sources/`, `entities/`, `concepts/`. |
| `scripts/`     | Python helpers — docx extraction, stub generation, lint, etc.     |
| `.gitignore`   | This file's enforcement layer.                                    |

## What's not tracked (and why)

- **`research for cemini/`** — 500M+ of source PDFs and reports. Immutable
  raw material, local-only.
- **`market dataset/`** — 1.6G of historical price data. Same reasoning.
- **`research to be indexed/`** — drop-zone for new sources awaiting ingest.
- **`briefs/`** — operational deliverables staged for distribution to
  claude.ai or the CeminiSuite dev stack. They contain server IPs and
  point-in-time context; not durable artifacts.
- **`.local/`** — server connection details (SSH targets, IPs). One commit
  away from public exposure on a private repo, so kept local.
- **`.claude/settings.local.json`** — Claude Code per-project allowlist;
  contains the same IPs.
- **`.DS_Store`, `__pycache__/`, etc.** — OS and tooling cruft.

## Three layers

1. **Raw sources** (gitignored) — read but never modified.
2. **The wiki** (`wiki/`, tracked) — LLM-written, human-read, cross-linked
   markdown pages with YAML frontmatter.
3. **The schema** (`CLAUDE.md`, tracked) — how the LLM runs the wiki.
   Co-evolves with the workspace.

See `CLAUDE.md` for the full operational schema (page formats, ingest
workflow, citation tags, distribution rules).

## Distribution targets

The wiki is the librarian; consumers live elsewhere:

- **claude.ai** — context for conversations and writing tasks.
- **CeminiSuite** — the production trading stack on a Hetzner host.
  Connection details in `.local/server.md` (gitignored). This workspace
  ships briefs into `/opt/cemini/briefs/` only; everything else on the
  server is read-only from here.

## Getting started

```bash
# clone
git clone <this repo>
cd "OSINT WORKSPACE"

# raw sources are local-only — nothing to fetch from the repo for those.
# You will need to populate research for cemini/, market dataset/, and
# briefs/ from your own backups.

# scripts assume Python 3.11+ with python-docx; install as needed:
pip install python-docx
```
