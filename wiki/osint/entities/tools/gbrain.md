---
title: "gbrain (garrytan) — agent memory router (RETIRED 2026-05-18)"
type: entity
tags: [tool, agent-memory, knowledge-graph, ccc-wiki, retired, osint, entity-extraction]
keywords: [gbrain, garrytan, agent brain, memory router, multi-modal, entity extraction, backlink, MIT, retired]
related:
  - sources/tool-evaluation-multi-wiki-audit-may-2026.md
  - sources/eval-tool-routing-hermes-plan-2026-06-27.md
  - entities/tools/graphiti.md
  - sources/eval-multi-wiki-link-evaluation-2026-11-10.md
  - entities/tools/ontosmith.md
maturity: draft
created: 2026-05-16
updated: 2026-11-10
---

## Relations

- `@sources/tool-evaluation-multi-wiki-audit-may-2026.md` — source evaluation that classified this as Adopt-tier
- `@sources/eval-tool-routing-hermes-plan-2026-06-27.md` — K132 re-eval (docx Adopt vs RETIRED posture)

## Raw Concept

Identified in the May 2026 44-tool multi-wiki audit. MIT-licensed TypeScript agent brain / thin router for multi-modal media ingestion. 12,200 stars. Primary fit: CCC wiki. Cross-route: OSINT wiki for automated intelligence extraction from financial podcasts and market analysis streams.

## Narrative

**RETIRED 2026-05-18 — adopted but unused.** gbrain was MCP-wired into `.mcp.json` after the May 2026 audit and a vector + knowledge-graph index was built on cemini-librarian (~929 pages). In practice it was never load-bearing: wiki work is done with direct file reads (always current) and full-text search via kb-server (bot-facing, indexes all four wikis). gbrain was a third retrieval layer redundant with both — its semantic/graph features add little for a wiki that is already hand-linked with explicit `related:` frontmatter, `@path` cross-links, and a curated `index.md`. Its git-based sync also conflicted with the rsync wiki-sync (rsync dirties the working tree, blocking gbrain's `git pull`), so it would have needed an ongoing maintenance cron to stay current. Decommissioned rather than carry that cost: removed from `.mcp.json` (`local` + `librarian` envs). The install remains inert on cemini-librarian (`/opt/gbrain` 328M, `/root/.gbrain` brain DB 277M) — purgeable if disk is needed; re-installable from the public MIT repo if a real semantic-search need ever appears. See `@ROADMAP.md`.

**K132 update (2026-06-27):** `eval-tool-routing-hermes-plan-2026-06-27.md` re-proposes **Adopt** (24.3k★, MIT confirmed). Posture unchanged: **RETIRED** for MCP deployment. Approved next step is **hybrid-search spike only** — see `briefs/ccc-2026-06-27_k132-gbrain-hybrid-search-spike.md`. Consider `@entities/tools/graphiti.md` for temporal KG instead of full gbrain restore.

Original evaluation (kept for the record):

Garry Tan's opinionated agent brain — a thin router that transforms articles, audio, and video transcripts into rich "brain pages" with deep entity extraction and backlink propagation.

**Key capability**: Multi-modal ingestion pipeline — audio → transcript → entities → brain pages. This is directly applicable to OSINT wiki's need for automated intelligence extraction from financial podcasts, earnings calls, and external market commentary.

**CCC wiki fit**: The entity extraction and backlink propagation patterns mirror the librarian architecture's knowledge-graph construction. The thin-router design (vs. heavy framework) matches the CCC preference for composable, single-purpose tools.

**License**: MIT — aggressive corporate adoption permitted.

**Open question** [OPEN QUESTION 2026-11-10]: Entity extraction accuracy under dense financial jargon. Unchanged since 2026-05-16 and not resolvable by looking anything up — only a test on real corpus text settles it. The K132 hybrid-search spike was approved and never run.

## Re-surfaced as Extract — 2026-11-10, and one retirement reason has expired

`@sources/eval-multi-wiki-link-evaluation-2026-11-10.md` URL 4 rates it **Extract** again, routed to Atto and family-tree, with a claimed ~86% cut in multi-session vault token cost.

**Read the 2026-05-18 retirement reasoning against what is true now.** It rested on two arguments:

1. **Redundant with two other retrieval layers** — direct file reads, and "full-text search via kb-server (bot-facing, indexes all four wikis)".
2. **Git-based sync conflicted with rsync** wiki-sync.

**Argument 1 has partly expired.** `cemini-librarian` and kb-server were **deleted 2026-06-14**. The full-text search layer that made gbrain a third redundant tier no longer exists. What remains is direct file reads — which are current but do not retrieve semantically, and do not span sessions.

That does not automatically revive the tool. It does mean the earlier verdict was reasoned against an architecture this workspace no longer has.

### Phase-0, 2026-11-10 — what the current README says

| Property | Finding |
|----------|---------|
| Licence | **MIT** — "GBrain is MIT-licensed and free to self-host; gbrain.io is optional paid hosting" |
| Store | **Markdown in a git repo.** "The database is an index rebuildable from it." |
| Local engine | **PGLite** (WASM Postgres 17), no setup, personal brains to ~50K pages |
| Large engine | Postgres + pgvector, self-hosted or Supabase, same interface |
| **Where data leaves** | **Synthesis requires a configured chat model**; optional embedding/reranking providers can receive text; hosted gbrain.io is paid |
| Keyless path | **Keyword-only search needs no model API** |
| Install | **Not on npm** — an unrelated `gbrain` package shadows it; install via Bun from GitHub |
| Backup | "Markdown export is not a full database backup" |

**The storage decision is the part worth taking on its own merit:** the durable artefact is Markdown in version control, and the retrieval index is disposable. A bad index is an inconvenience, not a data loss.

### What this does and does not reopen

- **Reopened:** cheap cross-session recall over an existing Markdown corpus, with keyless keyword search and no cloud call.
- **Not reopened:** synthesis and semantic search, both of which need a model and therefore fall under Atto's ban 4 unless the model is local.
- **Unchanged:** the git-sync conflict is still a real operational cost if it runs against this repo.

**Next step if pursued:** a hybrid-search spike on the *existing* wiki Markdown, read-only, keyless — the same scope the K132 note already approved and that was never run.
