# Cemini OSINT Research Workspace — Schema

This file is the **schema**: it tells you (the LLM) how to operate this workspace. Everything else is either a raw source, a wiki page, or a meta file. Read this on every session start. Active workstreams + open decisions live in `ROADMAP.md`, not here.

## Purpose

Local knowledge hub for OSINT and financial research — a librarian that **manages, curates, and distributes** that knowledge.

- **Manage** — inventory source material; track what's been read, extracted, and shipped
- **Curate** — pull relevant fragments out of raw sources; structure them as interlinked wiki pages
- **Distribute** — route findings to the right consumer:
  - **claude.ai** — context for a conversation, writing task, or general research
  - **CeminiSuite** (dev stack on Hetzner, `/opt/cemini`) — ticker research, strategy input, anything for the dev stack's knowledge base

Distribution is a deliberate step, not a default. Stage candidates in `briefs/` first; never push directly to the server.

## Architecture — three layers

1. **Raw sources** — immutable. You read them, never modify them. **Canonical location: `cemini-egress-fi:/opt/cemini-bulk/research/<wiki-id>/`** after ingest (transient drop: `research to be indexed/` before ingest). `[DECOMMISSIONED 2026-06-14]` Old `cemini-librarian` bulk deleted; source pages may still cite `cemini-librarian:` paths as immutable ingest-time provenance.
   - **Drop pattern**: `research to be indexed/` → ingest → `bash scripts/archive_raw_to_egress.sh --wiki-id osint "<file>"` (scp + rm local)
   - **Read pattern**: `ssh cemini-egress-fi cat /opt/cemini-bulk/research/osint/<filename>` or laptop Preview while file is still in inbox

2. **The wiki** — LLM-written, human-read. **Canonical location: laptop `wiki/`** (git). Sibling federation wikis live in their own repos under `~/Desktop/projects/`. No 24/7 kb-server sync — see `@meta/librarian-decommission-2026-06-14.md`.

3. **The schema** — this file.

Staging/output lives outside the wiki:
- `briefs/` — one-off deliverables ready to ship to claude.ai or CeminiSuite (gitignored)
- `research to be indexed/` — transient drop zone for new raw sources (gitignored)
- `LESSONS.md` — meta-lessons about *how we work* (distinct from `wiki/log.md`)
- `hot.md` — ephemeral session-state cache (gitignored)
- `ROADMAP.md` — active workstreams + open decisions (tracked)

## Deployment boundary — what runs where

Two Hetzner servers for **trading**; laptop for **research authoring**. See `@meta/librarian-decommission-2026-06-14.md`.

- **Laptop** (this workspace) — canonical git wiki, briefs, local backtests. Powered off = curation pauses only; **no** remote wiki serving dependency.
- **cemini-prod** (`/opt/cemini`) — 24/7 CeminiSuite trading stack (Lane A, PM, Kalshi, HL adapters, Redis `intel:*`).
- **cemini-egress-fi** (Helsinki) — order egress relay for Hyperliquid + Polymarket `POST /order` (SSH tunnel from prod); **federation raw-source cold store** at `/opt/cemini-bulk/research/<wiki-id>/` (read-only bulk, separate from order path).
- **`cemini-librarian`** — **DELETED 2026-06-14.** Historical design: `@concepts/librarian-server-architecture.md`.

Rule: do not assume kb-server, stash, or librarian SSH paths exist. Query wikis via Read/grep locally; use Exa for external gaps.

## Folder layout

```
LAPTOP (~/Desktop/OSINT WORKSPACE/):
  CLAUDE.md                    # this file — the schema
  LESSONS.md                   # meta-lessons (how we work, not what we did)
  ROADMAP.md                   # active workstream / decisions / done log
  hot.md                       # session-state cache (gitignored)
  research to be indexed/      # transient drop zone (gitignored)
  briefs/                      # staging for outputs → claude.ai or CeminiSuite (gitignored)
  wiki/                        # canonical wiki (laptop git only)
    index.md                   # content-oriented catalog of all wiki pages
    log.md                     # append-only chronological operations log
    sources/                   # one page per ingested source
    entities/                  # tickers, companies, people, facilities, organizations, tools, infrastructure
    concepts/                  # topics, theses, methodologies, strategies
  scripts/                     # wiki_lint.py, skill_audit.py, preingest_check.py, wiki_gap_detect.py, cross_doc_dedup.py, sync_wiki_to_librarian.sh, etc.
  ui/                          # local dev tooling (e.g. Cemini AI chat front-end + proxy to cemini-egress-fi gateway)
  .local/                      # gitignored, local-only (server connection details, etc.)

.local/ (gitignored):
  arctic-market-dataset/     # optional laptop Arctic LMDB for equity backtests

cemini-egress-fi (cold store — all federation wikis):
  /opt/cemini-bulk/research/<wiki-id>/   # osint, ccc, seo, image-gen, gambling, game-dev, cybersec, 3d-printing
```

Pages can be nested inside `entities/` when `Domain > Topic > Subtopic` hierarchy is warranted (e.g. `entities/companies/geo-group.md`, `entities/tickers/nvda.md`, `entities/tools/swarmvault.md`). `concepts/` and `sources/` are flat by convention.

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

- `type` determines section template
- `maturity`: `draft` → `validated` (cross-referenced + checked) → `core` (battle-tested source of truth). Move up (occasionally down) as evidence warrants
- `related[]` is **bidirectional**: if A lists B, B must list A
- `created` / `updated`: ISO dates; bump `updated` on meaningful body changes

### Body sections (in order, include only what's relevant)

- `## Relations` — inline list of `@path/to/page.md` annotations matching `related:` frontmatter
- `## Raw Concept` — provenance. For source pages: title/author/retrieval-date/filename/URL. For entity/concept pages: what prompted this page, which sources synthesized into it
- `## Narrative` — the body. Prose, tables, structured data, diagrams. Concept pages: synthesized understanding, neutral, well-sourced — opinion belongs in briefs, not concept pages
- `## Snippets` — verbatim quotes / code / formulas / data with citations
- `## Dead Ends` (optional) — what was tried + why it failed + what was learned. See `@concepts/exploration-graph-dead-ends.md`

### Page-type quick reference

- **Source page** (`wiki/sources/<slug>.md`) — one per ingested source. Raw Concept fields: title / author / type / location / retrieved / pages / read-status (skimmed | read | deep-read | unread-stub).
- **Entity page** (`wiki/entities/<category>/<slug>.md`) — tickers, companies, people, infrastructure, tools, frameworks. Raw Concept: what prompted the page + which sources synthesize into it.
- **Concept page** (`wiki/concepts/<slug>.md`) — topics, theses, methodologies. Raw Concept: the question or topic the page answers.
- **Brief page** (`briefs/<YYYY-MM-DD>_<slug>.md`) — deliverable for distribution. Body sections: `## Target` (claude.ai | CeminiSuite | …) / `## Summary` / `## Body` / `## Sources`.

## Cross-link + citation conventions

**Cross-links** (`@path` syntax):
- Use `@path/to/page.md` inline (no leading slash, relative to `wiki/`)
- Bidirectional: A → B and B → A both required
- Stub pages preferred over orphan mentions: if a topic comes up without a page, create a stub
- **Typed dependencies** (optional, ARA protocol): `@I path/...` (imports), `@B path/...` (bounds), `@M path/...` (baseline/measure). Untyped `@path` means general-related. See `@concepts/typed-relation-dependencies.md`

**Citation tags**:
- Source page: `[Source: filename.pdf p.5]`
- External URL: `[Source: https://... (retrieved YYYY-MM-DD)]`
- Multiple: `[Sources: filename.pdf p.5, filename2.pdf p.12]`

**Claim confidence tags**:
- `[CONFIRMED]` — ≥2 independent sources
- `[TENTATIVE]` — single source or circumstantial
- `[NEEDS VERIFICATION YYYY-MM-DD]` — plausible but untested. **Always include the date** so `wiki_gap_detect.py` can flag staleness
- `[RETRACTED]` — previously believed, now disproven. Keep in place with a note; don't delete

## Operations

### Ingest (adding a new source)

1. New source dropped into `research to be indexed/` (transient drop zone)
2. **Run `python3 scripts/preingest_check.py`** — detects duplicates by sha256 / arXiv ID / DOI / URL / filename / title. Verdicts: `DUPLICATE` (do not ingest without deciding to supersede / fold / re-download), `LIKELY` (human review), `NEW` (proceed)
3. Read the source (or relevant pages for long PDFs)
4. **Discuss key takeaways with the user before writing**
4b. **Cross-wiki routing check** — before writing pages, evaluate whether the source contains off-topic content more relevant to another wiki (@image-gen-wiki, @seo-wiki, or @3d-printing-wiki). If so:
   - Call `python3 scripts/cross_wiki_route.py` to create a stub page or brief in the correct wiki, piping content via stdin
   - Use `--type page` for substantive material, `--type brief` for tangential material
   - **When in doubt, prefer a brief over a stub** — briefs are cheaper and don't create maintenance burden in the target wiki
4c. **X `Posts.docx` style pass (seo-wiki handoff)** — when ingesting `Posts.docx` or writing/updating a `trading-posts-compilation-*` source page:
   - Read `@seo-wiki/prompts/posts-docx-style-pass.md` and run the ritual after the OSINT source page exists (same session or immediately after commit)
   - Update `@seo-wiki/concepts/x-account-voice-and-format.md` — exemplar table, snippets, steal/avoid flags, paragraph-discipline / paste warnings
   - Append Article beats to `@seo-wiki/concepts/x-article-3-notes.md` or create `@seo-wiki/concepts/x-article-N-notes.md` when a long-form maps to the operator's X lane (local wiki, agent tooling, Obsidian/Claude workflows, prediction markets)
   - Append one line to `@seo-wiki/wiki/log.md`: `style-pass | Posts.docx K## | …`
   - **Does not replace** 4b — OSINT keeps topic routing and synthesis; SEO keeps operator voice + Article queue only. Ingest stays in OSINT; no need to drop `Posts.docx` in the SEO repo.
5. Create `wiki/sources/<slug>.md` — frontmatter + Raw Concept + short Narrative. Cite the eventual canonical location: `[Source: <filename>.pdf p.5]`
6. Identify entities + concepts the source touches. For each:
   - If page exists: update it, add `related:` backlink, bump `updated:`
   - If no page: create a stub (frontmatter + one-line Narrative + Relations). Real content accumulates over subsequent ingests
7. Update `wiki/index.md` — add rows for new pages
8. Append to `wiki/log.md`: `## [YYYY-MM-DD] ingest | <source title>` with bullets of what changed
9. **Archive raw source to egress-fi**: `bash scripts/archive_raw_to_egress.sh --wiki-id osint "research to be indexed/<filename>"` — update source page `Location` to `cemini-egress-fi:/opt/cemini-bulk/research/osint/<filename>`. Sibling wikis use their federation id (see `federation_paths.yaml`). Script removes local copy on success; pass `--keep-local` to retain inbox/raw-sources copy.
10. Run lint + **`python3 scripts/ingest_session_gate.py`** + commit + push (wiki only)
11. **Update ROADMAP.md + stage briefs in `briefs/` per `post_ingest_workflow` memory rule.** This is the immediately-next step after commit-and-push. Without it, ingest research dies in the wiki.
12. A single ingest must touch 3-15 pages. If it touches 0 new pages, ask whether the source is worth ingesting

### Query (answering a question)

1. Read `wiki/index.md` first to locate relevant pages
2. Read those pages; follow `@relations` where useful
3. Synthesize the answer with inline citations to source pages and raw sources
4. **OOD signal**: if the wiki doesn't contain a real answer, say so explicitly. Don't fabricate from tangential matches. Offer to ingest sources that would fill the gap
5. **File answers back**: if the query produced a valuable synthesis, file it as a new concept page or brief. Don't let insights die in chat
6. Append a query entry to `log.md` if substantive

### Lint (periodic health check)

Run on request. The mechanical checks are automated by `scripts/wiki_lint.py`:

- **Orphans** — pages with zero inbound `related:` references
- **Bidirectional gaps** — A lists B as related but B doesn't list A
- **Dangling links** — `related:` paths that don't resolve
- **Missing pages** — `@path` mentions in body where the file doesn't exist
- **Cited-unread stubs** — source pages with `read_status=unread-stub` and ≥1 inbound edge
- **Frontmatter quality** — missing `type`/`maturity`/mismatched `updated`
- **Stale `[NEEDS VERIFICATION YYYY-MM-DD]` tags** (≥7 days old by default)

These still need human/LLM judgment:
- **Contradictions** — two pages making incompatible claims. Flag with `[NEEDS VERIFICATION YYYY-MM-DD]` and note on both pages
- **Stale claims** — superseded by newer sources. Move to `[RETRACTED]` with pointer

### Gap detection (Tier 1)

Run `python3 scripts/wiki_gap_detect.py` on request. Three gap types:

- **Type A — Cited-unread stubs** (≥2 inbound + `read_status=unread-stub`). Output includes proposed Exa query
- **Type D — Stale `[NEEDS VERIFICATION YYYY-MM-DD]`** (≥7d old). Output includes the surrounding claim sentence for Exa-resolution
- **Type E — Thin concept pages** (`## Narrative` <100 words). Output lists inbound source pages worth deep-reading

Tier 1 is **descriptive only** — produces a candidate list, doesn't fetch via Exa. The user picks; the LLM executes via Exa MCP.

**Tier 2** (proactive Exa with user-gated commit) is roadmapped, not built. **Tier 3** (fully autonomous outbound ingest) is explicitly out of scope on drift / cost / trust grounds.

### Brief audit (pre-distribution sanity check)

Run `python3 scripts/skill_audit.py briefs/<file>.md` before scp'ing a brief to prod. Static checks (40% of design weight):

- Required sections (`## Target`, `## Summary`)
- Cross-links (`@path` resolution)
- Citation tags (Sources section OR inline tags)
- NEEDS VERIFICATION freshness (≥30d old by default)
- Prose quality (no emoji unless authorized; no TODO/FIXME at ship time)
- Frontmatter (well-formed YAML if present)

Veto gates wired: Operational Stability + Scientific Integrity. Output: PASS / WARN / REJECT verdict.

## External research — Exa MCP

When the wiki + raw sources can't answer, or when a source cites unverified URLs, the **Exa MCP server** is the canonical external-research path:

| Tool | When to use |
|------|-------------|
| `mcp__exa__web_search_exa` | Quick targeted lookup — fact-check, find a primary source URL |
| `mcp__exa__web_search_advanced_exa` | Date-bounded, domain-scoped, or category-filtered. When `web_search_exa` returns too much noise |
| `mcp__exa__crawling_exa` | Pull clean LLM-friendly content from a known URL — turns `[Source: https://...]` into verifiable text for `## Snippets` |
| `mcp__exa__company_research_exa` | Ticker watchlist gap-fills + entity expansion |
| `mcp__exa__people_search_exa` | Founder, exec, key-personnel discovery |
| `mcp__exa__deep_researcher_start` / `_check` | Async multi-step research jobs — novel concept-page bootstrapping |
| `mcp__exa__get_code_context_exa` | Library / SDK source-code context |

**Workflow integration**:
- **Ingest**: when a source cites a URL, prefer `crawling_exa` to pull cited page directly into `## Snippets`
- **Query (OOD)**: before declaring a wiki gap, run `web_search_exa`. If results converge, ingest the best 1-2 hits as new source pages
- **Lint**: `[NEEDS VERIFICATION]` tags trigger an Exa cross-check before being upgraded to `[CONFIRMED]` or moved to `[RETRACTED]`

Cost discipline: Exa is a paid API. Default `numResults: 3-5` for routine queries; `deep_researcher_*` reserved for genuine multi-source synthesis.

The `exa:search` skill (from `exa@claude-plugins-official`) fans out across parallel subagents for genuinely complex research questions.

## Distribution rules

Material ready to leave the wiki goes through `briefs/` first:

- **→ claude.ai** — copy the relevant brief body
- **→ CeminiSuite** — stage in `briefs/`, confirm content with user, then Claude Code handles `scp` to `/opt/cemini/briefs/`. **Code and config modifications on the server remain out-of-scope from this workspace** — those flow through a separate server-Claude session that reads the brief and executes with its own review loop. This workspace can place staging material on the server (brief transfers into `/opt/cemini/briefs/` only) but does not modify any other path under `/opt/cemini/`. Read-only operations on the server (ssh ls, grep, cat for verification) are fine.

## Working method

- Search the wiki first. Raw sources second. External sources last (via Exa MCP)
- Prefer paraphrase + cite over raw quote. Quotes go in `## Snippets` with full citation
- When stress-testing a claim, actively look for disconfirming evidence
- Flag single-source claims explicitly
- File insights into wiki pages or briefs before they disappear from chat
- For substantial briefs (engineering days + operational cost commitments): dispatch a codex / Plan / code-reviewer agent for an independent pass before user GO/NO-GO sign-off — saves wrong-direction implementation effort

## Phase-0 audit pattern (before adopting an external tool)

Before adopting a third-party tool that would integrate into Cemini's stack or wiki, run a Phase-0 source audit (Explore subagent, ~30 min):

1. Clone the repo to `/tmp/<tool>-audit/`
2. Verify license matches the eval claim
3. Verify maturity signals (stars, commits, last push, open issues)
4. **Audit for the most-likely failure mode for this tool class**:
   - Wiki-tooling: hardcoded directory layout? (kills nested-wiki support — see SwarmVault NO-GO 2026-05-04, PageIndex NO-GO 2026-05-05)
   - Skill libraries: domain-fit mismatch? (Cemini already covers source-side workflow — see Claude-OSINT NO-PORT 2026-05-05)
   - Per-tool-class specifics: see `wiki/entities/tools/<tool>.md` audits for examples
5. Compare against existing Cemini coverage (don't adopt parallel implementations of what we already have)
6. Decide GO / CONDITIONAL-GO / NO-GO and record in the entity page

This pattern has shipped 3 clean rejections of credible-looking but wrong-fit tools across K28+K30. Saves ~2-4 hours of misaligned implementation per audit.

## Session-start ritual

On every new session, **before any other work**, run these checks (cheap, under a minute):

### 0. Resume from hot.md

Read `hot.md` (gitignored session-state cache). Report in one line:

> "Resuming from K30 (Polymarket-readiness wave + 3 audits + 6 prod briefs staged). Workspace idle. Next: your direction."

If `hot.md` is missing (first run, deleted, gitignored on a fresh clone), say:

> "No `hot.md` found — fresh session. Want me to rebuild session state from `wiki/log.md` + `ROADMAP.md`?"

At session end, rewrite `hot.md` with updated position, open decisions, pending actions.

### 1. Tier-2 sweep cadence

```bash
ls -1t wiki/sweeps/*.md 2>/dev/null | head -1
```

If most recent sweep file is **>7 days old** OR `wiki/sweeps/` is empty, prompt:

> "It's been N days since the last Tier-2 arXiv sweep. Want me to run one now?"

Tier 2 is user-gated-commit; do NOT silently auto-run.

### 2. Inbox check

```bash
ls -1 "research to be indexed/" 2>/dev/null | grep -v '^\.'
```

If items exist that the user hasn't asked you to address, mention briefly: "Btw, you have N items in `research to be indexed/`. Want me to triage them?"

### 3. HL funding Dune backtest cadence (quarterly)

```bash
./scripts/check_hl_funding_backtest_due.sh
```

If exit code **0** (due), prompt:

> "Quarterly HL funding Dune backtest is due (see `wiki/meta/hl-funding-backtest-cadence.md`). Want me to run it now? (~10–15 min laptop + Dune credits)"

Do **not** auto-run; user-gated like Tier-2 sweep. On completion, bump `last_run` / `next_due` (+90 days) on the cadence page and note in `wiki/log.md` if posture changes.

### 4. PM LP spread backtest cadence (quarterly)

```bash
./scripts/check_pm_lp_backtest_due.sh
```

If exit code **0** (due), prompt:

> "Quarterly PM LP spread backtest is due (see `wiki/meta/pm-lp-backtest-cadence.md`). Want me to run it now? (`bash scripts/run_pm_lp_backtest.sh` — public Gamma + CLOB, ~1 min)"

Do **not** auto-run. On completion, bump cadence meta and note in `wiki/log.md` if spread tiers change. Reports: `.local/reports/pm-lp-backtest-YYYY-MM-DD.html`.

### 5. Kalshi LP spread backtest cadence (quarterly)

```bash
./scripts/check_kalshi_lp_backtest_due.sh
```

If exit code **0** (due), prompt:

> "Quarterly Kalshi LP spread backtest is due (see `wiki/meta/kalshi-lp-backtest-cadence.md`). Want me to run it? (`bash scripts/run_kalshi_lp_backtest.sh` — public trade-api, ~1–2 min)"

Do **not** auto-run. Reports: `.local/reports/kalshi-lp-backtest-YYYY-MM-DD.html`.

### 6. Equity signal backtest cadence (quarterly)

```bash
./scripts/check_equity_signal_backtest_due.sh
```

If due: prompt to run `bash scripts/run_equity_signal_backtest.sh` (needs `ssh cemini-librarian` + ArcticDB). See `wiki/meta/equity-signal-backtest-cadence.md`.

### 7. Cross-venue PM×Kalshi backtest cadence (quarterly)

```bash
./scripts/check_cross_venue_backtest_due.sh
```

If due: prompt to run `bash scripts/run_cross_venue_backtest.sh`. See `wiki/meta/cross-venue-backtest-cadence.md`.

### 8. WC LP safety DR cadence — **RETIRED 2026-07-28**

World Cup window over; world-cup-bot dropped. `check_wc_lp_safety_due.sh` always exits 1. Do **not** prompt. See `wiki/meta/wc-lp-safety-cadence.md`.

### 9. Wiki gap detect Tier 1 cadence (weekly)

```bash
./scripts/check_wiki_gap_detect_due.sh
```

If due: prompt to run `bash scripts/run_wiki_gap_detect.sh` (~1 min). Report lands in `.local/reports/`. See `wiki/meta/wiki-gap-detect-cadence.md`. Tier 2 Exa remains user-gated.

### 10. Federation morning summary (operator hub)

```bash
cemini-federation-morning-summary
# or: bash ../projects/cemini-federation-hub/scripts/run_federation_morning_summary.sh
```

Report: `cemini-federation-hub/hub/sweeps/YYYY-MM-DD-federation.md`. Install once: `bash ../projects/cemini-federation-hub/scripts/install_federation_hub.sh`. See `@meta/federation-operator-hub-stub.md`.

### 11. Daily research digest cadence

```bash
./scripts/check_daily_research_digest_due.sh
```

If exit code **0** (no report for today): prompt to run `bash scripts/run_daily_research_digest.sh` (~30s + Exa). Report: `wiki/sweeps/YYYY-MM-DD-daily.md`. See `wiki/meta/daily-research-digest-cadence.md` and `@concepts/cemini-wiki-ingest-workflow.md`.

### 12. Obsidian vault (operator setup)

If `wiki/.obsidian/` missing: `bash scripts/setup_obsidian_vault.sh`. Graph review ritual: `.cursor/skills/cemini-wiki-graph/SKILL.md`.

Keep each check under 60 seconds. Rituals that grow into multi-minute operations should become opt-in commands instead.

## Related Wikis

When a query needs data from another wiki, reference it using the `@wiki-alias/path/to/page.md` syntax. The LLM resolves these by reading the other wiki's files directly.

Paths below are relative to this CLAUDE.md file's directory. Resolve `../` against this file's location to get the absolute path.

| Alias | Path | Visibility | Description |
|-------|------|------------|-------------|
| `osint-wiki` | `wiki/` | **Private** | Financial research, quant finance, prediction markets, CeminiSuite, RL for trading |
| `image-gen-wiki` | `../Image gen/wiki/` | Public | Uncensored image generation, model cataloging, ComfyUI, LoRA, persona/character ops |
| `seo-wiki` | `../SEO:GEO B&M Business/wiki/` | Public | Local SEO, GBP optimization, GEO/AEO, web design, social media, creator marketing |
| `3d-printing-wiki` | `../3d printing/wiki/` | Public | FDM/FFF printing, Bambu, materials, slicers, print farms, store ops |
| `cybersecurity-wiki` | `../Cybersecurity wiki/wiki/` | Public | Cybersecurity research — offensive security (pentest / red team / bug bounty / exploit dev), defensive operations (SOC / IR / threat hunting), certifications + careers, threat actors. Shared territory: OSINT tradecraft + investigative methodology |
| `gambling-wiki` | `../Gambling wiki/wiki/` | **Public** | Sports betting, casino, poker, DFS, best ball, prediction-market wagering (retail/strategy). Shared territory: Kelly, FLB, Kalshi/Polymarket cross-venue — osint-wiki owns bots/CeminiSuite |
| `game-dev-wiki` | `../Game Dev wiki/wiki/` | **Public** | Hobby game dev — castle/RTS research, engine evals, agent-assisted slice workflow. Shared territory: subagent harness — ccc-wiki owns primitives |
| `ccc-wiki` | `../Cemini claude code CCC/wiki/` | **Public** | Cursor + Claude Code meta-wiki — workflow, subagents, MCP/conductor, hooks, skills, slash commands, /goal · Ralph · OpenSpec. Shared territory: agent orchestration, conductor/librarian architecture, skill audits |
| `federation-hub` | `../cemini-federation-hub/hub/` | **Private** | Operator control plane — morning federation summary, wiki path catalog, Obsidian triage (`@meta/federation-operator-hub-stub.md`) |

**Private (not public federation deliverables):** `osint-wiki`, **Cemini Financial Suite** (`../CeminiSuite`). **Public on GitHub:** `ccc-wiki` and the six domain wikis (including `gambling-wiki`, `game-dev-wiki`). See root `README.md` for repo URLs.

### Cross-wiki link syntax

- Use `@wiki-alias/path/to/page.md` for cross-wiki references (e.g., `@seo-wiki/concepts/geo-aeo.md`)
- Bidirectional: if OSINT page A references Image Gen page B, add a matching `@osint-wiki/...` backlink on page B
- When creating a stub in another wiki, note the cross-wiki dependency in `## Relations`

### Querying wikis (laptop-only; librarian decommissioned 2026-06-14)

kb-server and 24/7 conductor→librarian routing are **offline**. To answer questions:

1. Read `wiki/index.md` and grep across `wiki/` and sibling wiki repos (`@wiki-alias/...`)
2. Use **lazy-tool** only for **prod-mcp** health/tools — `kb_search` / `conductor_query` will fail unless librarian is restored
3. **exa** / **fetch** for external gaps

Historical sync/rsync instructions are archived in `@meta/librarian-decommission-2026-06-14.md`.

## Agent orchestration (laptop — K159)

Claude Code plugin **fable-advisor** is installed (user scope). In Claude Code sessions on this workspace:

- Start architect sessions with `/model fable` (or `/model opus` if Fable unavailable on plan).
- Delegate implementation via the orchestration skill — do not type bulk code in the architect session.
- Verify evidence before accepting implementer output; cross-vendor review when stakes are high.
- **Grok lane** needs [xAI Grok CLI](https://x.ai/cli) (`grok` on PATH); **Codex lane** uses local `codex` CLI (`@openai/codex` ≥0.145; ChatGPT login).

Canon: `@entities/tools/fable-advisor.md` · install: `bash scripts/adopt_k159_local.sh` · Codex repair/sync: `bash scripts/adopt_codex_cli.sh --smoke`

## Related — read-only from this workspace

- **CeminiSuite dev stack** — Hetzner host, `/opt/cemini` server root. Connection details (SSH target, IP) live in `.local/server.md` (gitignored). Has its own `CLAUDE.md` for dev work. **Never modify the server's `CLAUDE.md` from here.**
