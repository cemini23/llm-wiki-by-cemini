# Cemini OSINT Research Workspace — Schema

This file is the **schema**: it tells you (the LLM) how to operate this workspace. Everything else is either a raw source, a wiki page, or a meta file. Read this on every session start.

## Purpose

The workspace is a local knowledge hub for OSINT and financial research. Its job is to **manage, curate, and distribute** that knowledge — think of it as a librarian.

- **Manage** — inventory source material; track what's been read, extracted, and shipped
- **Curate** — pull relevant fragments out of raw sources; structure them as interlinked wiki pages
- **Distribute** — route findings to the right consumer:
  - **claude.ai** — when context is needed for a conversation, writing task, or general research
  - **CeminiSuite** (dev stack on Hetzner, `/opt/cemini`) — when material is ticker research, strategy input, or anything that belongs in the dev stack's knowledge base

Distribution is a deliberate step, not a default. Stage candidates in `briefs/` first; never push directly to the server.

## Pattern sources
This schema is synthesized from:
- **Karpathy's LLM Wiki** (local copy: `research for cemini/llm-wiki.md`) — three-layer architecture (raw / wiki / schema), `index.md` + `log.md` navigation, ingest/query/lint operations, "persistent compounding artifact"
- **ByteRover Context Tree** (local copy: `research for cemini/llm re 4:3.pdf`) — hierarchical `Domain > Topic > Subtopic > Entry`, explicit `@path` relations, YAML frontmatter with lifecycle metadata, ADD/UPDATE/UPSERT/MERGE/DELETE primitives with `reason` audit trail, OOD signaling

If you're ever uncertain about structure, defer to those documents.

## Architecture — three layers

1. **Raw sources** — immutable. You read them, never modify them.
   - `research for cemini/` — long-form PDFs, reports, notes (~242 files, 527M)
   - `market dataset/` — historical market data (~1.6G)

2. **The wiki** — LLM-written, human-read. This is the library proper.
   - `wiki/` — hierarchical markdown pages with explicit cross-references

3. **The schema** — this file. Tells the LLM how to run the wiki. Co-evolves over time.

Staging/output lives outside the wiki:
- `briefs/` — one-off deliverables ready to ship to claude.ai or Cemini
- `LESSONS.md` — meta-lessons about *how we work* (distinct from `wiki/log.md`)

## Folder layout

```
CLAUDE.md                    # this file — the schema
LESSONS.md                   # meta-lessons (how we work, not what we did)
research for cemini/         # raw sources: PDFs, images, docx
market dataset/              # raw data: Stocks/, ETFs/, Data/, kaggle/
briefs/                      # staging for outputs → claude.ai or Cemini
wiki/                        # the library
  index.md                   # content-oriented catalog of all wiki pages
  log.md                     # append-only chronological operations log
  sources/                   # one page per ingested source
  entities/                  # tickers, companies, people, facilities, organizations
  concepts/                  # topics, theses, methodologies, strategies
```

Pages can be nested further inside `sources/entities/concepts` when `Domain > Topic > Subtopic` hierarchy is warranted (e.g. `entities/companies/geo-group.md`, `entities/tickers/nvda.md`).

## Wiki page format

Every wiki page is a markdown file with YAML frontmatter + structured sections.

### Frontmatter (required)

```yaml
---
title: Human-readable page title
type: source | entity | concept | brief
tags: [coarse, category, labels]
keywords: [fine, grained, search, terms]
related:
  - entities/companies/example-co.md
  - concepts/example-concept.md
maturity: draft | validated | core
created: 2026-04-23
updated: 2026-04-23
---
```

- `type` — one of the four page kinds. Determines which section template applies.
- `maturity` — `draft` when first created, `validated` when cross-referenced and checked, `core` when it's been battle-tested as a source of truth. Move entries up (and occasionally down) as evidence warrants.
- `related` — explicit paths to cross-referenced pages. Bidirectional: if A lists B, B should list A. Check both directions when editing.
- `created` / `updated` — ISO dates. Update `updated` whenever the body changes meaningfully.

### Body sections

Four canonical sections, in order. Include only what's relevant per page type.

- `## Relations` — inline list of `@path/to/page.md` annotations matching `related:` frontmatter. Lets readers see links without parsing YAML.
- `## Raw Concept` — provenance. For source pages: original title, author, retrieval date, filename/URL. For entity/concept pages: what prompted this page, which sources it was synthesized from.
- `## Narrative` — the body. Prose, tables, structured data, diagrams. This is what a human reads.
- `## Snippets` — verbatim quotes, code, formulas, or raw data pulled from sources. Always with citation.

### Page-type templates

**Source page** (`wiki/sources/<slug>.md`) — one per ingested source:
```
## Raw Concept
- Original title: ...
- Author(s): ...
- Type: PDF | article | podcast | video | ...
- Location: research for cemini/3:29 19.pdf
- Retrieved: 2026-04-23
- Pages / length: 19p
- Read status: skimmed | read | deep-read | unread-stub

## Narrative
One-paragraph abstract, then bullet takeaways. Cite back to page numbers.

## Snippets
Verbatim pulls with page citations.
```

**Entity page** (`wiki/entities/<category>/<slug>.md`) — tickers, companies, people, facilities:
```
## Raw Concept
What prompted this page; which sources synthesize into it.

## Narrative
Who/what this entity is. Key facts, properties, current status.
Cross-link to related entities and concepts throughout.

## Snippets
Direct quotes or data points used as evidence.
```

**Concept page** (`wiki/concepts/<slug>.md`) — topics, theses, methodologies:
```
## Raw Concept
The question or topic this page answers.

## Narrative
The synthesized understanding. Keep this neutral and well-sourced — opinion and synthesis belong in briefs, not here.

## Snippets
```

**Brief page** (`briefs/<YYYY-MM-DD>_<slug>.md`) — one-off deliverable staged for distribution:
```
## Target
claude.ai | CeminiSuite | ...

## Summary

## Body

## Sources
List of wiki pages synthesized + raw sources cited.
```

## Relations syntax — how to cross-link

- Use `@path/to/page.md` inline (no leading slash, relative to `wiki/`).
- When you link from A → B, also add A to B's `related:` list. Bidirectional means bidirectional.
- If a topic keeps coming up without a page, create a stub page for it (frontmatter only + one-line narrative) rather than letting mentions pile up orphaned.

## Citation & claim tags

Every factual claim in the wiki must cite its source inline. Formats:
- Source page: `[Source: filename.pdf p.5]`
- External URL: `[Source: https://... (retrieved YYYY-MM-DD)]`
- Multiple sources: `[Sources: filename.pdf p.5, filename2.pdf p.12]`

Claim confidence tags (inline):
- `[CONFIRMED]` — supported by ≥2 independent sources
- `[TENTATIVE]` — single source or circumstantial
- `[NEEDS VERIFICATION]` — plausible but untested
- `[RETRACTED]` — previously believed, now disproven. Keep in place with a note; don't delete.

## Operations

### Ingest (adding a new source)

1. Read the source (or relevant pages for long PDFs).
2. Discuss key takeaways with the user before writing.
3. Create `wiki/sources/<slug>.md` — source page with frontmatter + Raw Concept + short Narrative.
4. Identify new entities and concepts the source touches. For each:
   - If a page exists: update it, add `related:` backlink, bump `updated:`.
   - If no page exists: create a stub (frontmatter + one-line Narrative + Relations). Real content accumulates over subsequent ingests.
5. Update `wiki/index.md` — add rows for any new pages.
6. Append to `wiki/log.md`: `## [YYYY-MM-DD] ingest | <source title>` with bullets of what changed.
7. A single ingest should touch 3–15 pages typically. If it touches 0 new pages, ask whether the source is worth ingesting.

### Query (answering a question)

1. Read `wiki/index.md` first to locate relevant pages.
2. Read those pages; follow `@relations` where useful.
3. Synthesize the answer with inline citations to source pages and raw sources.
4. **OOD signal**: if the wiki doesn't contain a real answer, say so explicitly. Don't fabricate from tangential matches. Offer to ingest sources that would fill the gap.
5. **File answers back**: if the query produced a valuable synthesis, file it as a new concept page or brief. Don't let insights die in chat.
6. Append a query entry to `log.md` if the query was substantive.

### Lint (periodic health check)

Run on request. Look for:
- **Contradictions** — two pages making incompatible claims. Flag inline with `[NEEDS VERIFICATION]` and note on both pages.
- **Stale claims** — superseded by newer sources. Move to `[RETRACTED]` with pointer to newer source.
- **Orphans** — pages with zero inbound `related:` links. Either delete, merge, or cross-link.
- **Missing pages** — concepts mentioned inline without a `@path` because no page exists yet. Create stubs.
- **Bidirectional gaps** — A lists B as related but B doesn't list A. Fix both sides.
- **Unread source stubs** that keep getting cited — promote with a real read pass.

## Distribution rules

Material ready to leave the wiki goes through `briefs/` first:

- **→ claude.ai** — context for a conversation, writing task, or general research. Copy the relevant brief body.
- **→ CeminiSuite** — ticker research, strategy input, or anything for the dev stack. Stage in `briefs/`, confirm content with the user, then Claude Code handles the `scp` transfer to `/opt/cemini/briefs/`. **Code and config modifications on the server remain out-of-scope from this workspace** — those flow through a separate server-Claude session that reads the brief at `/opt/cemini/briefs/<file>.md` and executes with its own review loop. This workspace can place staging material on the server (brief transfers into `/opt/cemini/briefs/` only) but does not modify any other path under `/opt/cemini/`. Read-only operations on the server (ssh ls, grep, cat for verification) are fine.

## Working method

- Search the wiki first. Raw sources second. External sources last.
- Prefer paraphrase + cite over raw quote. Quotes go in `## Snippets` with full citation.
- When stress-testing a claim, actively look for disconfirming evidence.
- Flag single-source claims explicitly.
- Don't let insights disappear into chat — file them.

## Active research threads

- **CeminiSuite per-ticker research** — active. Canonical format is the **Gemini Deep Research template** (six sections: Business Overview · Competitive Landscape · Financial Profile · Recent Events · Forward Catalysts · Analyst & Sell-Side Context). Watchlist (30 tickers — 2026-04-24 even +5 / −5 rebalance against the server baseline: added ASTS, GLW, INTC, PL, SOFI; removed MARA, JPM, BAC, GS, UBER with Financials category sunset, new Fintech category) at `wiki/entities/ticker-watchlist.md`. Indexed reports at `wiki/entities/tickers/<symbol>.md`. **Progress: 21 / 30** (AAPL, AMD, AMZN, ASTS, AVGO, BTC, COIN, DIS, ETH, GLW, GOOGL, INTC, META, MSFT, MSTR, NFLX, NVDA, PL, PLTR, SMCI, TSLA). Ingest workflow: user drops `<SYMBOL> <date>.docx` into `research to be indexed/` → Claude runs `/tmp/index_tickers.py` → moves source into `research for cemini/` → flips the status row in the watchlist table. **Divergence-from-server rule**: wiki-tracked additions/removals lead the server's `tickers.json`; annotate divergence in the watchlist's "Wiki-tracked divergence" section, apply the combined diff server-side, then re-pull config to restore parity.
- **Corpus inventory** — 230 stubs generated from `research for cemini/`. Clusters skew heavily to RL/MARL (108) and LLM agents (59). Corpus is research-methodology heavy — math, portfolio strategy, Cemini-internal audits — not ticker- or event-driven.

## Related — read-only from this workspace
- **CeminiSuite dev stack** — Hetzner host, `/opt/cemini` server root. Connection details (SSH target, IP) live in `.local/server.md` (gitignored). Has its own `CLAUDE.md` for dev work. **Never modify the server's `CLAUDE.md` from here.**

## Open questions
- PDF content index — 242 files in `research for cemini/` are date-named, not topic-named. Bootstrap in progress: extract first pages → create `wiki/sources/` stubs → deep engagement as PDFs are consulted.
- Whether to rename the workspace folder off `/Users/claudiobarone/Desktop/OSINT WORKSPACE` (user offered; no pressing reason yet).
