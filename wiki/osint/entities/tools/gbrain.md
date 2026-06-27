---
title: "gbrain (garrytan) — agent memory router (RETIRED 2026-05-18)"
type: entity
tags: [tool, agent-memory, knowledge-graph, ccc-wiki, retired, osint, entity-extraction]
keywords: [gbrain, garrytan, agent brain, memory router, multi-modal, entity extraction, backlink, MIT, retired]
related:
  - sources/tool-evaluation-multi-wiki-audit-may-2026.md
  - sources/eval-tool-routing-hermes-plan-2026-06-27.md
maturity: draft
created: 2026-05-16
updated: 2026-06-27
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

**Open question** [NEEDS VERIFICATION 2026-06-27]: Entity extraction accuracy under dense financial jargon — unchanged from 2026-05-16; K132 spike may revisit if hybrid-search eval runs.
