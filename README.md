# Cemini OSINT Research Workspace

A local knowledge hub for OSINT and financial research, organized as an
LLM-curated, human-read wiki. This repo holds the **schema, the wiki, and
the helper scripts**. Raw sources archive on the laptop; **no 24/7 librarian
server** (decommissioned 2026-06-14).

## What's tracked

| Path           | Role                                                              |
| -------------- | ----------------------------------------------------------------- |
| `CLAUDE.md`    | The schema — tells the LLM how to operate this workspace.         |
| `ROADMAP.md`   | Active workstream, decisions, and open questions.                 |
| `LESSONS.md`   | Meta-lessons about *how we work* (distinct from `wiki/log.md`).   |
| `wiki/`        | The library: `index.md`, `log.md`, `sources/`, `entities/`, `concepts/`. |
| `scripts/`     | Python helpers — docx extraction, stub generation, lint, gap detection. |
| `agents/`      | Agent harnesses (e.g. `devfun-poker-arena/` — tracked briefs + examples). |
| `.cursor/`     | Cursor rules + federation skills (`/goal`, `to-issues`, `grill-with-docs`). |
| `.gitignore`   | This file's enforcement layer.                                    |

## What's not tracked (and why)

- **`research to be indexed/`** — transient drop-zone for new sources awaiting
  ingest. Gitignored.
- **`briefs/`** — operational deliverables staged for distribution to
  claude.ai or the CeminiSuite dev stack. Gitignored.
- **`.local/archives/research/`** — post-ingest raw PDFs/docx. Gitignored.
- **`hot.md`** — session-state cache (curator working memory across
  compaction boundaries). Gitignored (changes every session).
- **`.local/`** — server connection details (SSH targets, IPs). Gitignored.
- **`.claude/settings.local.json`** — Claude Code per-project allowlist.
  Gitignored.
- **`.DS_Store`, `__pycache__/`, etc.** — OS and tooling cruft.

## Architecture — laptop wiki + prod trading fleet

1. **Raw sources** — immutable. **Laptop archive:** `.local/archives/research/`
   after ingest. Transient drop: `research to be indexed/`.
   - Older source pages may cite `cemini-librarian:/opt/cemini-bulk/...` as
     historical provenance only (host deleted 2026-06-14).

2. **The wiki** (`wiki/`, tracked) — LLM-written, human-read, cross-linked
   markdown. **Canonical on laptop git** (~536 pages). Federation wikis in
   sibling repos under `~/Desktop/projects/`.

3. **The schema** (`CLAUDE.md`, tracked) — how the LLM runs the wiki.

4. **Hetzner fleet (trading only)**
   - **`cemini-prod`** — CeminiSuite trading stack (`/opt/cemini`)
   - **`cemini-egress-fi`** — Helsinki order egress (HL + PM)
   - **`cemini-librarian`** — **deleted** — see `wiki/meta/librarian-decommission-2026-06-14.md`

## Fleet posture (2026-06-14)

| Host | Purpose |
|------|---------|
| prod | Live trading, Lane A, streams |
| egress-fi | HL / PM order routing |
| laptop | Wiki, ingest, briefs, research |

kb-server / stash / lazy-tool `kb_search` are **not** available until librarian is
restored from snapshot.

## Quick start

```bash
# Wiki health
python3 scripts/wiki_lint.py

# Gap detection (Tier 1)
python3 scripts/wiki_gap_detect.py

# Pre-distribution brief check
python3 scripts/skill_audit.py briefs/<file>.md
```

## Related repos

- **CeminiSuite** — `~/Desktop/projects/CeminiSuite` (prod deploy monorepo)
- **Federation hub** — `~/Desktop/projects/cemini-federation-hub`
- **CCC wiki** and six public domain wikis — see `CLAUDE.md` Related Wikis table

See `CLAUDE.md` for full operating schema and `ROADMAP.md` for active workstreams.

## Collaborators

**New to this repo?** Read in order:

1. **`CLAUDE.md`** — how agents and humans operate the wiki (ingest, query, lint, distribution).
2. **`wiki/index.md`** — page catalog; **`wiki/log.md`** — recent operations.
3. **`.cursor/README.md`** — MCP setup (lazy-tool must be **On** when this folder is open).

**What stays private (gitignored):**

- **`briefs/`** — prod / CCC staging briefs (server IPs, deploy steps). Not in git by design.
- **`.local/`** — SSH targets, API keys, reports. Never commit.
- **`research to be indexed/`** — transient inbox before ingest.

**TipDrop (David):** product wiki + handoff briefs live in **`tipdrop-workspace-kit`** (`~/Desktop/projects/tipdrop-workspace-kit`). This repo holds research canon; TipDrop kit gets operator-actionable briefs that cite `@osint-wiki/...` pages. Ritual: `tipdrop-workspace-kit/briefs/OSINT-HANDOFF-INGEST-RITUAL.md`.

**Health checks before pushing:**

```bash
python3 scripts/wiki_lint.py
python3 scripts/ingest_session_gate.py
```
