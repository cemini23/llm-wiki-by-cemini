# Wiki Log

Append-only chronological record of wiki operations: ingests, queries (substantive), lint passes, structural changes.

Entry format: `## [YYYY-MM-DD] <op> | <title>`. One line per entry above the body keeps `grep "^## \[" log.md` parseable.

Newest entries on top.

---

## [2026-04-25] devinfra | B′: GitHub Actions lint workflow + local pre-commit hook

Closed the dev-infra gap on the GitHub side. The wiki now has a CI lint pass and the local repo blocks the most likely accidental leaks before they leave the laptop.

### Three new artifacts

1. **`.github/workflows/lint.yml`** — runs `scripts/wiki_lint.py` on:
   - every push to `main`
   - weekly cron (Monday 12:00 UTC)
   - manual `workflow_dispatch`

   Output is `tee`'d to a file and posted to `$GITHUB_STEP_SUMMARY` so the lint report renders as a markdown panel on the workflow run page (no need to dig into raw logs). Informational only — the lint script always exits 0, so the workflow is non-gating by design.

2. **`scripts/pre-commit.sh`** — bash hook that scans staged content and filenames before each commit. Blocks:
   - **Filenames**: `.env` / `.env.*` / `.DS_Store` at any depth
   - **Content (added lines only)**: literal Hetzner server IP (constructed from string parts so the hook source itself doesn't trip), `sk-[A-Za-z0-9_-]{20,}` API key prefix (catches OpenAI / DeepSeek / Anthropic-style keys ≥20 chars after the `sk-`)

   Only ADDED lines (`git diff --cached -U0 | grep '^+'`) are scanned, so historical IP/key occurrences in untouched parts of files don't false-positive. The hook itself is excluded from content scanning via `:(exclude)scripts/pre-commit.sh`. Bypass when intentional: `git commit --no-verify`.

3. **`scripts/install-hooks.sh`** — idempotent installer that symlinks `.git/hooks/pre-commit → ../../scripts/pre-commit.sh`. Run once after fresh clone. Hooks live outside the repo's tracked tree, so this is the only way to propagate the hook to other machines / clones.

### Plumbing fix: `wiki_lint.py` made portable

`WIKI = Path("/Users/claudiobarone/Desktop/OSINT WORKSPACE/wiki")` was hardcoded — would have broken in CI on push #1. Replaced with `Path(os.environ.get("WIKI_DIR", Path(__file__).resolve().parent.parent / "wiki"))` — auto-resolves from the script's own location, with `WIKI_DIR` env-var override for non-standard layouts. Verified working from arbitrary `cwd`.

### IP-redaction sweep (pre-hook prep)

Two tracked files contained the literal Hetzner IP and would have been false-positive blocked by the new hook on subsequent edits:
- **`ROADMAP.md` line 55** (dev-infra table documenting the hook itself) — replaced literal IP with `<server-ip>`.
- **`scripts/phase2_spawn.py` line 280** (legacy entity-spawn narrative) — replaced `root@<literal-ip>` with `root@<see .local/server.md>`, matching the pattern from the prior 2026-04-24 IP-scrub on `CLAUDE.md` + `wiki/entities/infrastructure/hetzner.md`.
- **`wiki/log.md` line 217** (historical log entry documenting the prior scrub) — left intact. The hook scans only added lines, so this never trips on routine log appends near the top of the file.

### Hook validation (4-pattern test matrix)

| Test | Input | Expected | Got |
|---|---|---|---|
| Positive | Stage the legitimate B′ files | exit 0 | ✅ exit 0 |
| Server IP | `_leak_test.md` containing `ssh root@<literal-ip>` | block | ✅ blocked |
| API key | `_leak_test.md` containing a 28-char `sk-…` token | block | ✅ blocked |
| `.env*` filename | `git add -f .env.test` | block | ✅ blocked |
| `.DS_Store` filename | `git add -f .DS_Store` | block | ✅ blocked |

All test artifacts cleaned up; staged tree returned to just the legitimate B′ changes before commit.

**Self-meta validation**: the hook tripped a sixth time — on the first attempt to commit *this very entry*, because the API-key test-matrix row originally contained the literal `sk-…<28 chars>` token used in the negative test. Redacted to "28-char `sk-…` token" and re-committed. Confirms the hook's content-not-intent stance: it doesn't care whether you're documenting the leak or causing it.

---

## [2026-04-25] lint+ingest | B loop-closers: SSRN 3000747 resolved + deepseek-api dates added

Two mechanical follow-ups from prior sessions closed.

### B.1 — SSRN 3000747 provenance resolved via local PDF extraction

`wiki/sources/stock-7-4-5.md` was a stub with `[NEEDS VERIFICATION 2026-04-25]` on its provenance — the SSRN abstract page is not crawlable via Exa (`SOURCE_NOT_AVAILABLE` on both URL forms), and a prior `web_search_exa` pass didn't surface the specific abstract. Resolved by `pypdf` extraction of the local PDF.

**Confirmed identity:**
- **Title**: The Influence of Financial Distress Using Altman Z-Score, The Beta of Stocks and Inflation To The Stock Return
- **Authors**: Mathius Tandiontong and Margaretha Sitompul (Maranatha Christian University, Bandung, Indonesia)
- **Journal**: Journal of Finance and Banking Review (GATR Journals), ISSN 0128-3103, Vol. 2(2): 21–27, 2017
- **Content**: Empirical panel regression (75 Indonesian manufacturing companies, BEI 2008–2012). All three hypotheses confirmed: Altman Z-Score, beta stocks, and inflation each partially affect stock returns. R² = 28.7%.

Prior diction note ("Stock is one securities among other securities") was correctly flagged as regional/non-native-English — this is an Indonesian institutional paper, not a quality issue. Cluster updated `uncategorized → quant-finance`. `maturity: draft → validated`. Three verbatim snippets populated. `wiki/index.md` title entry replaced — removed the `⚠ SSRN page not crawlable` placeholder with real title + provenance metadata.

### B.2 — Undated `[NEEDS VERIFICATION]` tags in `deepseek-api.md` dated

Lint section 7 surfaced 3 undated `[NEEDS VERIFICATION]` tags (lines 39, 48, 62) in `wiki/entities/infrastructure/deepseek-api.md`. All three stamped with `2026-04-25` so the 7-day staleness clock can now track them. No semantic change — these are server-side verification items (Hetzner RAM spec, cost/rate-limit envelope, API key presence) whose resolution path is a future server-Claude workstream.

**Post-edit lint state**: 0 bidirectional gaps, 0 dangling links, 0 undated `[NEEDS VERIFICATION]` tags.

---

## [2026-04-25] structural | Crypto concept scaffold + cross-link 7 ticker reports

Removed the topical gap in the wiki between the 7 crypto ticker reports (BTC, ETH, SOL, DOGE, ADA, AVAX, LINK) and their lack of any synthesizing concept page. Until today crypto tickers were only related-back to `entities/ticker-watchlist.md` — there was no topic-first discoverability path for "what kind of asset is each of these?" or "what's an oracle?" Two new concept pages close that gap and net the orphan count from 201 → 198.

### What was created

1. **`wiki/concepts/crypto-asset-taxonomy.md`** — `validated`, four functional categories:
   - **Store-of-value (programmable scarcity)** — BTC
   - **Programmable L1 / smart-contract platform** — ETH, SOL, ADA, AVAX (with comparison table: consensus / execution / architectural posture)
   - **Memecoin (PoW, no smart contracts)** — DOGE
   - **Oracle middleware** — LINK
   - Synthesis section addresses why the 4-axis cut matters (trade-offs aren't 1D), what's *not* on the watchlist (no privacy coins, no L2s, no DeFi blue chips), and how each category's failure modes differ.

2. **`wiki/concepts/oracle-networks.md`** — `validated`, LINK-focused deep dive:
   - Sections: oracle problem / decentralized oracle networks (DONs) / major use cases (DeFi price feeds, VRF, automation, CCIP cross-chain) / failure modes / competitor oracles (Pyth, API3, RedStone, UMA) / Cemini strategy implications.
   - Several use-case-specific facts tagged `[NEEDS VERIFICATION 2026-04-25]` — these are the lint section 7 escalation candidates.

### Cross-linking executed

- **7 crypto ticker pages** (`btc/eth/sol/doge/ada/avax/link.md`): each got `concepts/crypto-asset-taxonomy.md` added to `related:` frontmatter + a `## Relations` body section block. `link.md` additionally got `concepts/oracle-networks.md`. All `updated:` bumped to 2026-04-25.
- **`wiki/entities/ticker-watchlist.md`**: ada/avax/link added to frontmatter `related:` (alphabetical), plus the 2 new concept pages. Body Relations section gained a new "Cross-cutting concept pages" subsection.
- **`wiki/index.md`**: new "### Crypto / blockchain" subsection added under Concepts (between "M&A / legal" and "Alt-data taxonomy (stubs)") listing the 2 new pages.

### Lint result post-edit

- 0 bidirectional gaps, 0 dangling links, 0 missing `@path` mentions — all `related:` edges resolve cleanly.
- Orphans: 201 → 198. The 2 new concept pages picked up enough inbound coverage from the 7 ticker pages + watchlist that neither is an orphan itself.
- 3 undated `[NEEDS VERIFICATION]` tags still flagged in `entities/infrastructure/deepseek-api.md` — that's the next-up B.2 item.

### Roadmap entry

`ROADMAP.md` created earlier this session as a forward-looking project plan companion to this log file. A is the first item moved to its "Done — this session" table. Original B.3 (ada/avax/link → ticker-watchlist backlinks) folded into A — separate roadmap line was redundant once the watchlist edit became part of the concept-scaffold cross-linking.

---

## [2026-04-25] ingest+lint | Exa follow-ups complete + 3 crypto tickers indexed

Closed out the three Exa-MCP follow-ups flagged in the prior entry, then absorbed three new ticker DOCXs from the inbox. One commit's worth of work, but it touches three distinct surfaces (lint script, source-page provenance, ticker corpus).

### Follow-up #1 — CFTC primary-source corroboration `[CONFIRMED]`

- Crawled `https://www.cftc.gov/media/13351/Enf_AdvisoryKalshi022526/download` via `mcp__exa__crawling_exa`, added as snippet **S19** to `wiki/sources/3-19-compliance-research.md`.
- Material upgrade: the existing `[NEEDS VERIFICATION]` flag on the Feb 25 2026 Kalshi MNPI Enforcement Advisory citation now becomes `[CONFIRMED]` — primary source text matches the secondary-source paraphrase, including the Section 5(d) DCM Core Principles audit-trail framing and CFTC's assertion of concurrent enforcement authority alongside DCM internal actions.
- Pattern worth keeping: `[NEEDS VERIFICATION]` → Exa crawl primary source → upgrade to `[CONFIRMED]` is now a documented escalation path.

### Follow-up #2 — URL-snippet audit (small scope, 5 hits)

The audit revealed the corpus is overwhelmingly built from local DOCX/PDF research, not URL-cited material — only ~8 source pages contained external URLs at all, and most of those were already-populated (e.g. `4-14-lang.md` had a GitHub repo URL but no crawl candidate; `4-5-links-2.md` was a multi-topic aggregate, not a target). The 5 actionable pages were all "literally unknown" SSRN/arXiv stubs whose titles were the URLs themselves.

| Page | Resolved title (Exa) | Confidence |
|---|---|---|
| `sources/3-26-git-re.md` | arXiv:2603.19461 = *Hyperagents* (Zhang, 19 Mar 2026). Prior "anomalous arXiv ID, possibly typo for 2503.19461" caveat **[RETRACTED]** — YYMM.NNNNN format = March 2026, valid. | `[CONFIRMED]` |
| `sources/stocks-4-4-5.md` | SSRN 2512437 = *Crossing Stocks and the Positive Grassmannian I* (Racorean, Government of Romania, Feb 2014, also arXiv:1402.1281) | `[CONFIRMED]` |
| `sources/stock-6-4-5.md` | SSRN 2654872 = *Comparable Stocks, Boundedly Rational Stock Markets and IPO Entry Rates* (Chok+Qian, Sept 2015, PLoS ONE 8(5):e61474) | `[CONFIRMED]` |
| `sources/hedgge-fund-1-4-5.md` | SSRN 2449165 = *Do Hedge Funds Prefer Safe Stocks?* (Cao+Green+Li, June 2014, 50p) | `[CONFIRMED]` |
| `sources/stock-7-4-5.md` | SSRN 3000747 — `crawling_exa` returned `SOURCE_NOT_AVAILABLE`, refined `web_search_exa` did not surface the specific abstract. Page diction ("Stock is one securities among other securities") suggests regional / non-native-English authored work, possibly an Indonesian SSRN posting. | partial — flagged `[NEEDS VERIFICATION 2026-04-25]`, resolution path is local PDF cover-page extraction |

`wiki/index.md` ticker entries also rewritten — same 5 pages had verbatim "Electronic copy available at:..." titles in the catalog, now show real titles + provenance metadata + SSRN/arXiv IDs.

**Operational lesson**: `crawling_exa` cannot reach SSRN abstract pages directly (whether via `ssrn.com/abstract=N` or `papers.ssrn.com/sol3/papers.cfm?abstract_id=N`) — both URL forms returned `SOURCE_NOT_AVAILABLE`. `web_search_exa` is the working fallback and resolved 4 of 5. For the one miss, the resolution path drops back to opening the local PDF.

### Follow-up #3 — `wiki_lint.py` extended with verification-age check

- Added section 7: scans every page body for `[NEEDS VERIFICATION YYYY-MM-DD]` and surfaces tags older than `--verify-age-days` (default 7).
- Also surfaces *undated* `[NEEDS VERIFICATION]` tags as a separate "add-a-date" category — can't compute age without one.
- Implementation: argparse for the threshold, `datetime.strptime` for the date, line-number tracking so the report points to the exact spot.
- Smoke-test result: 0 stale dated tags, 3 undated tags surfaced (all in `entities/infrastructure/deepseek-api.md`) — pre-existing follow-up, not in scope today.

### Ticker indexing — ADA, AVAX, LINK (completes the 7-coin crypto-native bench)

- Ran `scripts/index_tickers.py` against `research to be indexed/` — picked up `AVAX 3_24.docx` and `LINK 3_24.docx` first pass; **skipped** `_(ADA)3_24.docx` because the script's regex `^([A-Z]+)\s` requires a leading uppercase token followed by whitespace.
- Renamed `_(ADA)3_24.docx` → `ADA 3_24.docx` in-place, re-ran the script, ADA indexed cleanly.
- All 3 source DOCXs moved from `research to be indexed/` → `research for cemini/`. Inbox now empty.
- `wiki/entities/tickers/ada.md` (46K) + `avax.md` (59K) + `link.md` (50K) created from the standard 6-section Gemini Deep Research template.
- Watchlist `wiki/entities/ticker-watchlist.md` status rows flipped to ✅; **Progress: 27 / 30** (was 24/30 — pending: SPY, QQQ, IWM, the three index ETFs).
- `wiki/index.md` ticker block: alphabetically inserted ADA between AAPL and AMD, AVAX between ASTS and AVGO, LINK between INTC and META.
- `CLAUDE.md` Active research threads bullet bumped from "21 / 30" → "27 / 30" with the full updated ticker list.

### Reminder for next ingest

Filename convention is **`<TICKER> <date>.docx`** — leading-underscore-and-parens forms (`_(ADA)3_24.docx`) get skipped by the regex. The script's diagnostic message ("SKIP unknown filename pattern") is clear enough that rename-and-rerun is a 2-step fix, but worth surfacing the rule each time the watchlist gets touched.

---

## [2026-04-25] capability | Exa MCP wired in — external research now first-class

The wiki gains an external-research tool path. Until today, "search the
wiki first, raw sources second, external sources last" had no defined
external-source mechanism — `WebFetch` / `WebSearch` were available but
not part of the schema. Now they are, via Exa MCP, with `crawling_exa`
giving us LLM-clean primary-source text on demand.

### What was actually done

1. **Plugin install** — `claude plugin marketplace update claude-plugins-official`
   then `claude plugin i exa@claude-plugins-official` (v3.3.8, scope: user,
   status: enabled). Provides the `exa:search` orchestrator skill.
2. **MCP server registration via API key** — the plugin's MCP server
   stayed stuck in `mcp-needs-auth-cache.json` (OAuth flow not completed).
   Bypassed via `claude mcp add --transport http exa "https://mcp.exa.ai/mcp?exaApiKey=...&tools=web_search_exa,web_search_advanced_exa,get_code_context_exa,crawling_exa,company_research_exa,people_search_exa,deep_researcher_start,deep_researcher_check"`.
   Registration landed in `~/.claude/.claude.json` user-scope, project-
   pinned to this workspace path. After Claude Code restart, all 8
   `mcp__exa__*` tools surfaced in the deferred-tool registry. The
   plugin's OAuth-required server still appears in `claude mcp list` as
   `plugin:exa:exa` (status: needs auth) — harmless duplicate listing.
3. **Smoke test** — `mcp__exa__web_search_exa` query on "CFTC Enforcement
   Advisory issued February 25 2026 regarding material non-public
   information MNPI" returned the **primary-source URL**
   `https://www.cftc.gov/media/13351/Enf_AdvisoryKalshi022526/download` for
   the exact advisory cited in `sources/3-19-compliance-research.md`.
   The wiki had the date and topic but not the document URL — Exa
   discovered it on query #1. Candidate follow-up: `crawling_exa` that
   URL into the compliance source's `## Snippets` to convert the
   currently-paraphrased CFTC claim into verifiable text.
4. **`CLAUDE.md` schema update** — new section `## External research —
   Exa MCP` inserted between Lint and Distribution rules. Maps each of
   the 8 tools to its workflow role, then describes integration into
   each operation (Ingest / Query OOD signal / Lint NEEDS-VERIFICATION
   tag resolution). Cost-discipline note: default `numResults: 3–5`,
   reserve `deep_researcher_*` for legitimate multi-source synthesis.
5. **Working-method rule update** — "External sources last" amended to
   "External sources last (via Exa MCP — see External research section)"
   so the rule now points to the mechanism.
6. **Path correction** — `/tmp/index_tickers.py` reference in the per-
   ticker research thread updated to `scripts/index_tickers.py`
   (script was relocated yesterday).

### Why this matters

Three workflow upgrades, in increasing order of leverage:

1. **URL-cited claims become verifiable**. Today many `## Snippets`
   sections cite URLs but contain only paraphrased text. With
   `crawling_exa` we can populate verbatim primary-source text for any
   URL-cited claim at the cost of one MCP call.
2. **OOD answers stop being terminal**. Previously, when a query hit a
   wiki gap, the response was "we don't have that, want to ingest?"
   Now the response can be "we don't have that — Exa returned X, here's
   the synthesis, want me to file it as a new source page?"
3. **`[NEEDS VERIFICATION]` tags become resolvable in-loop**. Lint
   passes can now upgrade or retract claims live, rather than queueing
   them as future work.

### Lint state delta

| Metric | Before | After | Δ |
| --- | --- | --- | --- |
| Tracked schema operations | 3 (Ingest / Query / Lint) | 4 (+ External research) | +1 |
| Available MCP tools (Exa) | 0 | 8 | +8 |
| Workflow rules referencing Exa | 0 | 4 (Ingest / Query / Lint / Working method) | +4 |

### Candidate follow-ups (deferred)

- `crawling_exa` the CFTC Kalshi MNPI advisory URL into
  `sources/3-19-compliance-research.md` `## Snippets` and bump the
  cite from paraphrase to verbatim.
- Audit `wiki/sources/*.md` for URL-cited claims with no corresponding
  `## Snippets` entries; queue a batch `crawling_exa` pass.
- Extend `scripts/wiki_lint.py` to flag `[NEEDS VERIFICATION]` claims
  older than N days as Exa-resolution candidates.

---

## [2026-04-25] structural | git scaffold — workspace now version-controlled

User approved turning the workspace into a private GitHub repo for backup
and versioning. Initial commit `d2564c0` ("Initial commit: wiki, scripts,
schema baseline"). The push to a remote is the user's next step; this
log entry covers the local scaffold only.

### What was actually done

1. **`scripts/`** — created at workspace root; copied 11 Python helpers
   from `/tmp/` into it (`bootstrap_extract.py`, `extract_docx.py`,
   `generate_stubs.py`, `index_tickers.py`, `partition_phase1.py`,
   `phase2_aggregate.py`, `phase2_enrich_docx.py`, `phase2_spawn.py`,
   `phase3_lint.py`, `phase3_lint_fix.py`, `wiki_lint.py`). They were
   ephemeral in `/tmp/` and would have been lost on next macOS reboot;
   now durable.
2. **`.local/`** — created at workspace root; populated with `server.md`
   holding the Hetzner SSH target, server root path, allowed/disallowed
   operations from this workspace. Gitignored — never committed.
3. **Server-IP scrub** — replaced inline `5.161.53.103` with pointer-to-
   `.local/server.md` in three tracked files:
   - `CLAUDE.md` line 222 ("Related — read-only" section)
   - `wiki/entities/infrastructure/hetzner.md` line 40 (server-reference bullet)
   - `wiki/log.md` line 390 (brief-transfer scp entry)
   Remaining IP occurrences in `briefs/*.md` (5 files) and
   `.claude/settings.local.json` are gitignored, so untouched.
4. **`.gitignore`** — created. Excludes raw sources (`research for cemini/`,
   `market dataset/`, `research to be indexed/`), operational outputs
   (`briefs/`), credentials (`.local/`, `.claude/settings.local.json`),
   OS/editor cruft (`.DS_Store`, `__pycache__/`, etc.).
5. **`README.md`** — created at workspace root. One-page orientation:
   what's tracked, what's not (and why), three-layer architecture
   reminder, distribution targets, getting-started snippet.
6. **`git init` + initial commit** — 325 files staged, all under
   `CLAUDE.md`, `LESSONS.md`, `README.md`, `wiki/`, `scripts/`, and
   `.gitignore`. Verified the gitignored paths (briefs, .local, .claude,
   research for cemini, market dataset, research to be indexed) are
   absent from `git ls-files --cached`.

### Decisions worth remembering

- **`briefs/` is gitignored** (revised from earlier plan to commit).
  Briefs are operational/throwaway and contained five inline server-IP
  references. The wiki + `log.md` entries already document everything
  durable about each brief; the brief files themselves are point-in-time
  artifacts.
- **`.claude/settings.local.json` is gitignored** by the established
  `.local.json` Claude Code convention. Contained 8+ allow-listed bash
  commands embedding the server IP.
- **No remote configured.** User creates the private GitHub repo at
  their leisure and runs `git remote add origin … && git push -u origin
  main` themselves.

### Lint state delta

| signal | before | after |
| --- | --- | --- |
| version-controlled | no | yes (local) |
| inline server-IP occurrences in tracked files | 8 | 0 |
| Python scripts surviving `/tmp/` cleanup | 0 | 11 (in `scripts/`) |

### Followups

- Push to a private GitHub repo (user-side action).
- Periodic `git status` discipline at the end of ingest passes — they're
  natural commit boundaries now.
- If the script directory ever grows a runtime/`venv/`, add a `setup.md`
  or `requirements.txt` rather than relying on the README's pip hint.

---

## [2026-04-24] deep-read | sources/3-19-kalshi-trading-strategy-research.md — verified, snippeted, drift-corrected

Third source in the deep-read pass triggered by the 2026-04-24 lint scan (was 19 inbound; now 24 inbound after this pass added 5 new cross-links). Closes the original "top 3 cited-unread sources" pass.

### What was actually done
1. **Source extracted** — used `/tmp/extract_docx.py` against `research for cemini/3_19 Kalshi Trading Strategy Research.docx`. Output `/tmp/kalshi_strategy_research.txt` — 169 line-blocks, 9 H2 sections, 7 H3 subsections, 3 tables, 50 footnoted citations.
2. **Frontmatter sharpened** —
   - `Author(s)` resolved from "_unknown (stub — not yet read)_" to "Anonymous Gemini Deep Research-style synthesis; 50 footnoted external sources [Kalshi API docs, Federal Reserve FEDS 2026010, Karl Whelan / Becker / arXiv 2510.15205 / Aaltodoc / SFU Swartz et al., QuantPedia, Substack research blogs, CFTC Federal Register, Dentons / Cohen Milstein / Katten, HN/Reddit/r/algotrading, pykalshi GitHub]"
   - `Length` filled (~7,200 words; 9 H2; 7 H3; 3 tables; 50 footnotes)
   - `read_status: deep-read` added to **frontmatter** (was only in body block)
   - `updated:` bumped to 2026-04-24
3. **Section map** added to Raw Concept (10 H2 sections itemized for navigation).
4. **Cross-source synthesis note** added — explicitly frames this source as the **execution-architecture pillar** of the Cemini-Kalshi triad: regulatory/IP (`@sources/3-19-compliance-research.md`) + deal-economics (`@sources/3-19-ip-sale-research.md`) + execution-architecture (this source). Triad now closed bidirectionally at the source level.
5. **Abstract rewritten** to surface the CPU-only Hetzner forcing-function explicitly, name all 7 source-cited mathematical components (logit-space AS, Gumbel CDF, Bayesian Modified Kelly, BatchCancel weighting, reciprocal-bid reconstruction, pykalshi rationale, CFTC/MNPI compliance posture), and frame Polymarket arbitrage's explicit rejection.
6. **17 key-findings bullets** with section anchors, including: Arrow-Debreu binary contracts; FLB empirical table; Fed 2026 study Kalshi MAE numbers; weather Gumbel CDF + Bayesian climatology shrinkage; calendar spread arbitrage; AS in logit space derivation; Modified Kelly stack (fractional + Bayesian + temporal + 50% depth cap); 4-tier API rate-limit table; BatchCreate vs BatchCancel weighting asymmetry as the actual inventory-risk-management mechanism; WebSocket reciprocal-bid reconstruction; pykalshi <500-star filter exception rationale; CFTC exclusive federal jurisdiction + state preemption; Feb 25 2026 CFTC Enforcement Advisory + Cemini's zero-MNPI posture.
7. **Drift fix surfaced** — pre-existing key-finding bullet "Kalshi Premier/Prime API mandates rate-limiting + real-time monitoring — Kelly/CVaR governor + Prometheus/Loki/Grafana/Tempo stack satisfies" was conflating two sources. The "real-time monitoring mandate + Prometheus/Loki/Grafana/Tempo stack satisfies" framing is **from the compliance source** (DCM Core Principle 4); the Kalshi source itself documents rate-limit mechanics + technical-competency tier qualification + BatchCancel weighting as the actual inventory-management mechanism. Updated key findings reflect the source's actual content; the cross-source synthesis note documents the conflation source.
8. **11-row Cemini-stack mapping table** — binds each architectural component (FastAPI async loop, Polars vectorized DFs, Redis pub/sub, TimescaleDB, LangGraph 5-agent debate, FastMCP, Kelly/CVaR engine, BatchCancel 0.2x weighting, pykalshi-wrapped, Open-Meteo/FRED/SEC EDGAR, Pydantic v2) to its specific Kalshi-source justification with paragraph anchors.
9. **21 verbatim Snippets pulled** with section-anchored citations [Source: 3_19 Kalshi Trading Strategy Research.docx, § <section name>, ¶<line number in extraction>] — covers IP-sale framing, CPU-only constraint, FLB table + structural origin, shock-alpha numbers, weather ensemble + Gumbel + climatology shrinkage, Polymarket arb rejection, Devil's Advocate calendar-strip vol-surface watchdog, BS Greeks incompatibility, AS-in-logit rationale + reservation quote derivation, inverse-sigmoid round-trip, full-Kelly's 33% halving probability, Bayesian Modified Kelly + temporal discount, 4-tier API table, BatchCreate vs BatchCancel weighting table + adverse-shock liquidity-pull use case, WebSocket reciprocal-bid mechanism, pykalshi exception rationale, CFTC exclusive federal jurisdiction + state preemption, Feb 2026 CFTC Enforcement Advisory + Cemini compliance posture, integration recipe.
10. **No DeepSeek/Ollama retraction needed** — source's LLM-architecture rhetoric is implicit (does not name the local model); no inline workspace-level retraction marker required.

### Cross-link expansion (5 new edges added)
Added to source page's `related:` (mirrored as inbound on the targets):
- `sources/3-19-compliance-research.md` — companion regulatory source; both anchor on Kalshi DCM compliance under CFTC exclusive federal jurisdiction
- `sources/3-19-ip-sale-research.md` — companion deal-economics source; first paragraph of Kalshi source explicitly frames the strategy stack as IP-sale-valuation lever
- `entities/data-sources/gdelt.md` — adverse-shock signal that triggers BatchCancelOrders inventory withdrawal (the 0.2x token weighting makes 100-orders/sec liquidity pull feasible on Basic tier)
- `entities/frameworks/fastapi.md` — Polars-offload pattern explicitly cited as the mechanism keeping the FastAPI loop unblocked while reciprocal-bid reconstruction runs
- `entities/frameworks/pydantic-v2.md` — pykalshi natively emits Pydantic v2 domain models, which is the primary justification cited for the SDK adoption (despite <500-star filter exception)

### Drift discoveries surfaced for follow-up
- **Drift fix** — "Premier/Prime real-time monitoring mandate" was attributing a compliance-source recommendation to the Kalshi source. Now corrected; cross-source synthesis note added.
- **Side-effect Relations dedup** — adding `3-10-cryptographic-research.md` to the IP-sale Relations section (during this pass, since Kalshi triad-completion required all three sources to cross-reference each other) surfaced a pre-existing duplicate entry. Cleaned up; both entries merged with descriptive note retained.
- **New concept-page candidates surfaced (not created)** — `avellaneda-stoikov-logit-space.md`, `bayesian-modified-kelly.md`, `arrow-debreu-securities.md`, `calendar-spread-arbitrage.md`, and an `entities/sdks/pykalshi.md` would all consolidate single-source-cited material that's currently only narrated inline. Queue as future-promotion candidates if a second source ingests the same concepts.

### Lint state after this pass
| Dimension | Pre-pass | Post-pass |
|---|---|---|
| Orphans | 198 | 198 (unchanged — all in `sources/` bootstrap state) |
| Bidirectional gaps | 0 | 0 |
| Dangling `related:` edges | 0 | 0 |
| `@path` body mentions to missing files | 0 | 0 |
| Cited but unread source stubs | 26 | **25** (Kalshi source verified-deep-read) |
| Frontmatter quality issues | 0 | 0 |
| Outbound edges total | 594 | **604** (+10: 5 forward edges from source page + 5 backward) |

### Compounding value signals
- Kalshi source's inbound count: **19 → 24** (+26%) from this pass alone
- The Cemini-Kalshi triad (regulatory/IP + deal-economics + execution-architecture) is now structurally complete at the source level — every brief or query touching Kalshi compliance, valuation, or execution mathematics has direct linkage into all three reinforcing sources
- 11-row Cemini-stack mapping table makes the source the canonical reference for any Kalshi-execution-related question (which framework satisfies which requirement, which rate-limit mechanic enables which architectural pattern)
- 21 verbatim snippets with H2-section + paragraph-line citations make this source the backbone for prediction-market math queries (FLB empirics, AS-in-logit derivation, Modified Kelly, BatchCancel weighting) without requiring docx re-read
- The Kalshi source's drift fix sets a precedent: pre-existing wiki narratives generated during Phase 2 stub-promotion may carry source contamination from sister sources; deep-read pass should systematically check key-finding bullets against the actual extracted source text

### Pass complete
The original "top 3 cited-unread source stubs" deep-read pass (compliance + IP-sale + Kalshi) is now closed. Net result across all three deep-reads:
- Cited-unread stubs: 28 → 25 (−3, exactly matching the three deep-reads)
- Outbound edges: 547 → 604 (+57)
- Three top-cited sources now carry full Author + Length + section map + cross-source synthesis + verbatim snippets + bidirectional cross-links
- Two retraction lineages strengthened (DeepSeek-R1-14B + Ollama; pymerkle/OpenTimestamps/VCP); two complementary §1235 mitigation strategies properly disambiguated; one disambiguation flag (publisher's exclusion) deferred for future split-or-rename decision

### Next in queue
- `sources/3-10-cryptographic-research.md` (newly elevated to companion-tier; Author still `_unknown`, Length still `—` — natural deep-read #4 if user wants to extend the pass)
- `concepts/publishers-exclusion.md` split decision (APA-exclusion-schedule + IAA-publishers-exclusion) — flagged with `disambiguation_pending: true`
- Lint-script body-text mention check enhancement (catches "3-19 compliance research" prose cite without `related:` edge)

---

## [2026-04-24] deep-read | sources/3-19-ip-sale-research.md — verified, snippeted, cross-linked

Second source in the deep-read pass triggered by the 2026-04-24 lint scan (was 21 inbound; now 32 inbound after this pass added 11 new cross-links).

### What was actually done
1. **Source extracted** — used `/tmp/extract_docx.py` against `research for cemini/3_19 IP Sale Research.docx`. Output `/tmp/ip_sale_research.txt` — 133 line-blocks, 9 H2 sections, 4 tables, 56 footnoted citations.
2. **Frontmatter sharpened** —
   - `Author(s)` resolved from "_unknown (stub — not yet read)_" to "Anonymous Gemini Deep Research-style synthesis; 56 footnoted external sources spanning M&A diligence advisory firms, IRS PLRs, BVI valuation references, and deal-economics blogs"
   - `Length` filled (~7,400 words; 9 H2; 4 tables; 56 footnotes)
   - `read_status: deep-read` added to **frontmatter** (was only in body block)
   - `updated:` bumped to 2026-04-24
3. **Section map** added to Raw Concept (10 H2 sections itemized for navigation).
4. **Cross-source synthesis note** added — explicitly documents that this source's **"APA architecture+goodwill"** §1235 mitigation framing and the compliance source's **"provisional patent + Florida SMLLC"** framing are **complementary, not competing**. The wiki now carries both legitimate mitigation paths rather than the previously contaminated single one. Both source pages cross-link bidirectionally with this synthesis note.
5. **Abstract rewritten** to frame this source as the **deal-economics companion** to the compliance source's regulatory/IP frame and the cryptographic source's technical-audit frame.
6. **17 key-findings bullets** with section anchors, including: replacement-cost as primary valuation methodology; two-tier base+earnout deal structure (tech integration + Sharpe ratio over 12 mo); three named backtesting deal-killers (look-ahead bias, survivorship bias, curve fitting); IP-portability advantage of zero-vendor-lock-in data sources; cryptographic audit trail as trust-deficit mitigator for paper-trading; LLM-architecture-defensibility deal signal.
7. **12-row Cemini deal-economic mappings table** added — binds the source's deal-economic concepts (replacement-cost floor, earnout tier structure, deal-killer ledger entries, IP-portability scoring, model-catalogue clarity, audit-trail trust delta, etc.) to the specific Cemini-stack components that satisfy them.
8. **19 verbatim Snippets pulled** with section-anchored citations [Source: 3_19 IP Sale Research.docx, § <section name>, ¶<line number in extraction>] — covers replacement-cost methodology, base+earnout structure, the three backtesting deal-killers, OpenAPI/Pydantic catalogue as deal-accelerator, SBOM as supply-chain-due-diligence accelerator, zero-vendor-lock-in data-source scoring, cryptographic-audit-trail trust-deficit mitigation, skill-vetting as LLM-architecture-defensibility, and the §1235 architecture+goodwill framing.

### Cross-link expansion (11 new edges added)
Added to source page's `related:` (mirrored as inbound on the targets):
- `sources/3-19-compliance-research.md` — companion regulatory/IP source; documents complementary §1235 mitigation strategy
- `sources/3-10-cryptographic-research.md` — companion technical-audit source; provides the cryptographic-verifiability layer this source recommends
- `entities/frameworks/fastapi.md` — OpenAPI spec as named IP-sale deliverable
- `entities/frameworks/pydantic-v2.md` — model catalogue as "single-glance data-model comprehension" deal-accelerator
- `entities/security/syft.md` — auto-SBOMs as supply-chain-due-diligence accelerator
- `entities/security/cyclonedx.md` — service + license-expression schema fields map to deal-killer ledger entries
- `entities/data-sources/open-meteo.md` — zero-vendor-lock-in posture as IP-portability advantage
- `entities/data-sources/gdelt.md` — open alt-data as IP-portability advantage
- `concepts/cryptographic-audit-trail.md` — explicit cite as trust-deficit mitigator for paper-trading results
- `concepts/replacement-cost-valuation.md` — primary valuation methodology recommended for pre-revenue quant IP
- `concepts/skill-vetting.md` — LLM-architecture-defensibility deal signal (typed/gated/audited capability surface)

### Drift discoveries surfaced for follow-up
- **Side-effect bidirectional gap caught** — adding `3-19-compliance-research.md` as a backlink on `3-10-cryptographic-research.md` exposed that the compliance source was missing the 3-10 backlink the other direction. Fixed both directions; both now cross-link as companion deliverables for the institutional-acquirer due-diligence bundle.
- **`sources/3-10-cryptographic-research.md` elevated** from cited-orphan to companion-tier — by virtue of being explicitly cited as the technical-audit pillar of the deal-economic argument in this source, it is now a candidate for deep-read #4 (currently a partial stub: Author `_unknown`, Length `—`).

### Lint state after this pass
| Dimension | Pre-pass | Post-pass |
|---|---|---|
| Orphans | 198 | 198 (unchanged — all in `sources/` bootstrap state) |
| Bidirectional gaps | 0 | 0 (1 introduced mid-pass, fixed) |
| Dangling `related:` edges | 0 | 0 |
| `@path` body mentions to missing files | 0 | 0 |
| Cited but unread source stubs | 27 | **26** (IP-sale source verified-deep-read) |
| Frontmatter quality issues | 0 | 0 |
| Outbound edges total | 570 | **594** (+24: 11 forward edges from source page + 11 backward + 2 from 3-10↔compliance bidi fix) |

### Compounding value signals
- IP-sale source's inbound count: **21 → 32** (+52%) from this pass alone
- The two parallel §1235 mitigation strategies (provisional-patent+SMLLC + APA-architecture+goodwill) are now both legitimately documented; future IP-sale brief writing can choose between them or layer them rather than picking one and ignoring the other
- 12-row deal-economic mapping table is reusable scaffolding for the IP-sale brief, the deal-killer ledger memo, and any valuation-floor calculation
- 19 verbatim snippets with H2-section + paragraph-line citations make this source the backbone for any future deal-economics or valuation-methodology query — full claim-chain available without re-reading docx
- `3-10-cryptographic-research.md` is now structurally tied to both the compliance and IP-sale frames, completing the **diligence-bundle triad** (regulatory/IP + deal-economics + technical-audit) at the source level

### Next in queue
- `sources/3-19-kalshi-trading-strategy-research.md` (19 inbound) — last of the original 3-stub pass
- `sources/3-10-cryptographic-research.md` (now elevated; companion to compliance + IP-sale; partial stub awaiting full read)

---

## [2026-04-24] deep-read | sources/3-19-compliance-research.md — verified, snippeted, drift-corrected

Top-of-queue cited-unread stub from the 2026-04-24 lint pass (was 23 inbound; now 32 inbound after this pass added 9 new cross-links).

### What was actually done
1. **Source extracted** — wrote `/tmp/extract_docx.py` (python-docx + qn-namespaced iteration over body paragraphs and tables, emits `[H1]`/`[H2]`/`[H3]` heading anchors + `[TABLE START]/[TABLE END]` markers, list-style preservation). Output `/tmp/compliance_research.txt` — 167 line-blocks, 8 H2 sections, 8 H3 subsections, 4 tables, 60 footnoted citations.
2. **Frontmatter sharpened** —
   - `Author(s)` resolved from "_unknown (stub — not yet read)_" to "Anonymous deep-research deliverable (Gemini Deep Research-style synthesis); 60 footnoted external sources [WilmerHale, Dentons, Hogan Lovells, McDonald Hopkins, RSM US, Wipfli, NYSBA, ESMA, etc.]"
   - `Length` filled (~9,000 words; 8 H2; 8 H3; 4 tables; 60 footnotes)
   - `Read status` confirmed verified (was prematurely tagged "deep-read" in stub state)
   - Added `read_status: deep-read` to **frontmatter** (was only in body block) so the lint script's `read_status` heuristic correctly registers it. Cited-unread count dropped 28 → 27 in confirmation.
   - `updated:` bumped to 2026-04-24
3. **Section map** added to Raw Concept — 10 H2 sections itemized for navigation.
4. **Workspace-level retraction note** added — the source's Section 9 ("AI Regulations") presents `Ollama with DeepSeek-R1-14B for local inference (Step 52)` as a deployed component. Per @entities/infrastructure/deepseek-r1-14b.md and @entities/infrastructure/ollama.md, this local runtime is not actually deployed (CPU-only Hetzner; DeepSeek consumed via API). Source's mitigation logic still applies, just re-anchored to API-call latency.
5. **Narrative drift fixed** — the prior key-finding bullet "IRC §1221(a)(3) excludes self-created 'secret formula/process' from capital asset — APA must frame sale as architecture+goodwill to secure §1235 LTCG" was **drift**. Source's actual mitigation: file a **provisional patent application on the novel 5-agent LangGraph orchestration mechanism prior to executing the IP transfer**, then house the IP in a Florida SMLLC (federal disregarded entity preserves the individual creator's "holder" status under §1235 per IRS PLRs 200506008 and 200506009). Bullet rewritten to match source.
6. **NASD 1032(f) "off-the-shelf" specificity** added to the FINRA bullet — source explicitly extends Securities Trader registration even when the firm purchases the algo as-is and does not modify it (verbatim per S5).
7. **Cemini-specific architectural-as-legal mapping table** (11 rows) added — captures the source's recurring "tech decision = compliance artifact" pattern. Each row binds an architectural element (Pydantic v2 contracts, Devil's Advocate debate logs, pymerkle Merkle anchoring, Kelly/CVaR + congestion governor, AES-GCM vault, GitHub Actions Trivy/Semgrep, NautilusTrader backtests, SMLLC entity wrapper, provisional patent) to the specific statute / regulation it satisfies (OANDA/Alpaca non-transferability, NASD 1032(f), tamper-evident audit, Kalshi DCM self-limit-load + CFTC Core Principle 4, Florida SB 1452 secure custody, OSS-contamination deal-killer, MiFID II RTS 7 + SEC 15c3-5 kill-switch, IRC §1235).
8. **18 verbatim Snippets pulled** with section-anchored citations [Source: 3_19 Compliance Research.docx, § <section name>, ¶<line number in extraction>] — covers proprietary trading exemption, OANDA license non-transferability, IAA publisher's exclusion + CFTC Reg 4.14, NASD 1032(f) off-the-shelf extension, CFTC March 2026 ANPRM + DCM Core Principles 3 & 4, Kalshi technical-competency requirements, SB 1452 secure-custody-solution definition, AES-GCM vault statutory-compliance proof, copyleft contamination as deal-killer, Devil's Advocate native compliance artifact, pymerkle + OpenTimestamps Bitcoin anchoring, TCJA §1221(a)(3) hit, provisional-patent §1235 anchor, IRS PLRs 200506008/200506009, SEC AI-washing as documentation-rigor enforcement vector, 5-point strategic-acquisition roadmap. S17 carries the workspace-level Ollama/DeepSeek-R1-14B retraction marker inline.

### Cross-link expansion (10 new edges added)
Added to source page's `related:` (mirrored as inbound on the targets):
- `entities/frameworks/fastapi.md` — FastAPI request layer; **also fixed body-mention-without-link gap** (page narrative already cited "the 3-19 compliance research" but `related:` didn't list it)
- `entities/frameworks/nautilustrader.md` — MiFID II RTS 7 testing-mandate mitigation
- `entities/frameworks/torchrl.md` — observation-space cited as patentable-invention candidate
- `entities/components/kelly-cvar-risk-engine.md` — Kalshi self-limit-load mitigation
- `entities/security/trivy.md` — copyleft-license rejection; **also fixed body-cite-without-link gap** (Trivy narrative cites compliance research)
- `entities/security/semgrep.md` — defensive-coding gate; **same body-cite-without-link fix**
- `entities/security/cyclonedx.md` — SBOM format
- `entities/security/syft.md` — SBOM generation tool
- `concepts/sbom.md` — explicit deal-killer mitigation; concept page is `maturity: retracted` because the audit found SBOM not actually wired into CI; the deep-read sharpens the existing P1 wire-up ticket
- (`concepts/publishers-exclusion.md` already in `related:` — see disambiguation flag below)

### Drift discoveries surfaced for follow-up
- **`concepts/publishers-exclusion.md` disambiguation needed** — the page documents the **APA exclusion-schedule** mechanic (M&A carve-outs at acquisition). The 3-19 compliance source uses the same phrase in the **IAA §202(a)(11)** sense (bona-fide-publication exemption from RIA registration, with parallel CFTC Reg 4.14 CTA relief). Two distinct legal concepts sharing a phrase. Flagged the page with `[NEEDS VERIFICATION 2026-04-24]` at top of Narrative + `disambiguation_pending: true` frontmatter field, plus a pointer to S4 in the source's Snippets. Decision pending: split into `apa-exclusion-schedule.md` + `iaa-publishers-exclusion.md`, or rename + co-locate.
- **3 body-mention-without-link gaps** found and fixed during this pass (FastAPI, Trivy, Semgrep). Suggests the lint script should grow a "narrative text references source name without `related:` edge" check — currently it only checks `@path` markdown citations.

### Lint state after this pass
| Dimension | Pre-pass | Post-pass |
|---|---|---|
| Orphans | 198 | 198 (unchanged — orphans are sources/ stubs awaiting promotion) |
| Bidirectional gaps | 0 | 0 |
| Dangling `related:` edges | 0 | 0 |
| `@path` body mentions to missing files | 0 | 0 |
| Cited but unread source stubs | 28 | **27** (compliance source verified-deep-read) |
| Frontmatter quality issues | 0 | 0 |
| Outbound edges total | 547 | **570** (+23 from this pass: +10 from compliance source page + mirror + 9 backlinks-with-notes + 4 sharpened existing relations) |

### Compounding value signals
- Compliance source's inbound count: **23 → 32** (+39%) from this pass alone
- 11-row architectural-mapping table is reusable structure for downstream brief writing (IP-sale pitch deck, due-diligence prep memo, audit checklist)
- 18 verbatim snippets with H3-section + paragraph-line citations make this source the backbone for any future compliance-related query — full claim-chain available without re-reading docx

### Next in queue
- `sources/3-19-ip-sale-research.md` (21 inbound) — top of remaining queue
- `sources/3-19-kalshi-trading-strategy-research.md` (19 inbound)

---

## [2026-04-24] lint | Full structural sweep across 308 pages — clean except for 28 cited-unread source stubs

Ran a full lint pass via `/tmp/wiki_lint.py` (workspace-local script, not committed). Scanned all 308 pages (excluding `index.md` + `log.md`). Found 547 outbound `related:` edges across 110 inbound-covered pages.

### Results by lint dimension

| Dimension | Count | Status |
|---|---|---|
| Orphans (zero inbound) | **198** | Expected — all in `sources/`. The 226 source stubs are bootstrap-state per CLAUDE.md "Bootstrap in progress"; orphans = stubs not yet cited from any concept/entity. Not a defect. |
| Bidirectional gaps | **5 → 0** | All 5 came from `entities/infrastructure/deepseek-api.md` outbound edges added during 2026-04-24 promotion (draft → validated). Fixed this pass — `related:` + `## Relations` updated on `concepts/ip-sale-readiness.md`, `concepts/scatter-gather-topology.md`, `entities/frameworks/fastmcp.md`, `entities/frameworks/langgraph.md`, `entities/infrastructure/hetzner.md`. Re-run confirms 0. |
| Dangling `related:` edges | **0** | Clean — every `related:` path resolves to an existing file. |
| `@path` body mentions to missing files | **0** | Clean — no drive-by mentions to ghost pages. |
| Cited unread source stubs | **28** | Backlog — see queue below. |
| Frontmatter quality (no `type` / no `maturity`) | **0** | Clean. |

### Cited unread source stubs — top-10 prioritized for next deep-read pass

These are source stubs cited from multiple concept/entity pages but never deep-read. Highest-leverage compounding work; reading the top of this list improves the wiki's source-density across many pages at once.

| Inbound | Source | Likely topic clusters served |
|---|---|---|
| 23 | `sources/3-19-compliance-research.md` | IP-sale-readiness, audit-trail, regulatory framing |
| 21 | `sources/3-19-ip-sale-research.md` | IP-sale-readiness umbrella + replacement-cost / publishers-exclusion / IRC §1235 |
| 19 | `sources/3-19-kalshi-trading-strategy-research.md` | Kalshi venue, FLB / AS-logit, prediction-market doctrine |
| 12 | `sources/3-19-langgraph-scatter-gather-financial-analysis.md` | LangGraph topology, Send-API, the basis of the (now retracted) scatter-gather page |
| 11 | `sources/3-19-telegram-discord-research.md` | Alt-data ingestion, Telethon, alt-data taxonomy |
| 11 | `sources/3-10-cryptographic-research.md` | Audit-trail, Merkle / hash-chain / VCP framing |
| 9 | `sources/3-18-crypto-integration-technical-audit.md` | Hyperliquid + crypto venues + audit-trail engineering |
| 7 | `sources/3-9-pm-research.md` | Prediction-market doctrine, PM-vs-tickers calibration |
| 7 | `sources/forex-research-3-18.md` | OANDA / FX path; carry-trade concept |
| 6 | `sources/3-17-competition-research.md` | Competitive landscape (likely informs IP-sale acquirer narrative) |

**Recommended next session**: deep-read the top 3–5 (`3-19-compliance-research.md`, `3-19-ip-sale-research.md`, `3-19-kalshi-trading-strategy-research.md`). They subtotal **63 inbound references** — ~21% of all 308 inbound edges concentrate on those 3 unread pages.

### Lint-script provenance

`/tmp/wiki_lint.py` is workspace-local (not committed). Re-run any time via `python3 /tmp/wiki_lint.py`. Inputs: `wiki/**/*.md` frontmatter + body. Outputs: 6-bucket report. Re-runnable as a periodic health check; trivial to extend if more lint dimensions surface.

## [2026-04-24] housekeep | Bidirectional backlinks + watchlist divergence cleanup + 2 MEMORY.md entries

Three short cleanups closing loose ends from today's larger threads.

### 1. Bidirectional backlinks (3 fixes)
- `wiki/concepts/cryptographic-audit-trail.md` `related:` + `## Relations` now lists `concepts/equity-intraday-backfill-gap.md` (backfill INSERTs anchor into the same hash chain — explicit relationship now visible from both sides).
- `wiki/entities/ticker-watchlist.md` `related:` frontmatter now includes `entities/platforms/polygon.md`, `entities/infrastructure/yfinance.md`, `concepts/equity-intraday-backfill-gap.md` — closes the gap from this morning's 3-page additions.
- Closes the "Bidirectional gaps" lint item per CLAUDE.md.

### 2. Watchlist divergence section: RESOLVED
- ssh-verified `/opt/cemini/QuantOS/config/tickers.json` — server now carries the rebalanced 30-symbol list (no MARA/JPM/BAC/GS/UBER; INTC/GLW/PL/ASTS/SOFI present). Divergence ✅ closed.
- **Categorization variance preserved as intentional**: workspace splits the 5 new tickers across mega_cap/space_tech/industrials/fintech (human-readable librarian taxonomy); server collapses them to a single `frontier` category (operational tag for harvester/strategy code paths). Both encodings agree on the active-ticker set; not reconciling the bucket-naming.
- Updated the "Wiki-tracked divergence" section header to RESOLVED + preserved the diff as record-of-action; refreshed the "Raw config" snippet from the 2026-04-23 stale baseline to the 2026-04-24 live server state (no more MARA/JPM/BAC/GS/UBER, INTC/GLW/PL/ASTS/SOFI present, `frontier` as the new server-side category, `financials` sunset).

### 3. MEMORY.md: 2 new persistent-fact entries
- `polygon_not_authorized_doctrine.md` — Polygon plan returns NOT_AUTHORIZED on same-day equity intraday; `polygon_ingestor.py` self-heals via yfinance EOD sweep after 16:01 ET; crypto Coinbase path unaffected; yfinance fallback is bar-level (1-min) not tick-level.
- `workspace_server_body_divergence.md` — workspace `wiki/` = Gemini DR librarian; server `research_wiki/` = DeepSeek-regenerated RAG cache; same slug skeleton, different body methodology, intentionally not auto-reconciled (and CLAUDE.md scope rule blocks workspace from rsync'ing into non-`briefs/` server paths anyway). Linked from MEMORY.md so future sessions don't re-propose auto-sync jobs.

## [2026-04-24] milestone | Server-triage brief closeout + equity-intraday data-gap discovered + fix shipped

Server-Claude data audit returned three streams of results — all closing briefs cleanly with one new operational finding.

### Workstream A (Ollama hunt) ✅ clean
- **Zero consumer-path hits** for `ollama` / `OLLAMA` / `11434` across `agents/`, `services/`, `scripts/`, `docker/`, `.env`.
- All remaining references are **cosmetic wiki docs only** (retraction banners + historical notes) — no runtime impact.
- Root cause of user's "still looking for Ollama" symptom re-framed: was surfacing through `wiki_search` reads of retraction-banner text in `/opt/cemini/research_wiki/` pages, not from a live runtime reach. Cosmetic.
- **No rewire/remove PRs needed.** Brief closed.

### Workstream B (research_wiki refresh) ✅ complete — with divergence note
- **12 ticker pages added to server's `research_wiki/` via DeepSeek generation** (5 frontier: INTC/GLW/PL/ASTS/SOFI + 7 fills: COIN/DIS/MSTR/NFLX/ETH/SOL/DOGE). Server now carries 24 ticker pages + 304 total wiki pages.
- **UBER orphan reaped** from the DB, audit-chain entry written. This exercises the `--prune` path that was parked at end-of-Track-B-rebuild. One full prune round-trip complete.
- **Divergence flag**: the 12 server pages were **generated fresh via DeepSeek**, not rsync-copied from workspace. Workspace still holds the Gemini Deep Research bodies (institutional template, 6-section format). Server's `wiki_search` now embeds DeepSeek-generated bodies. Net: workspace = human-curated librarian (Gemini DR source-of-truth); server `research_wiki/` = RAG-lookup cache for LangGraph analyst (DeepSeek-regenerated). Same slug namespace, different body methodology. **Not reconciling automatically** — the two artifacts serve different consumers (workspace→user; research_wiki→LLM). Revisit if/when Gemini DR bodies become materially more accurate than DeepSeek regeneration for a given ticker.

### Data-audit result — new operational finding (equity intraday gap)

- **Crypto (Coinbase)** ✅ healthy all day — BTC/ETH/SOL etc. live through 21:10 UTC.
- **Equities** ❌ **missed full market session 13:30–20:00 UTC 2026-04-24**. Root cause: Polygon plan returns `NOT_AUTHORIZED` for same-day intraday data on equity ticks; `polygon_ingestor` market-hours gate silently skipped post-close once the NOT_AUTHORIZED came back. New tickers (INTC/GLW/PL/ASTS/SOFI) were backfilled from Apr 22 historical at container startup, so they had Apr 23 coverage but not Apr 24 live. GLW notably thinner (882 ticks) vs INTC/SOFI (~1,500+) — volume/liquidity tell.
- **Fix 1 (point fix)** — `scripts/backfill_yfinance.py` ran and inserted **13,258 bars** (390 × 34) for Apr 24's full session. All 5 new tickers verified: INTC $82.56, GLW $175.92, PL $35.43, ASTS $76.42, SOFI $18.45.
- **Fix 2 (doctrine)** — `polygon_ingestor.py` patched to add a **yfinance EOD sweep**: after 16:01 ET daily, ingestor checks if the session is missing and auto-backfills via yfinance. `yfinance` added to Dockerfile. Ingestor is now self-healing on the Polygon-intraday-NOT_AUTHORIZED failure mode going forward.
- **2 commits shipped** on this fix-pair.

### Workspace actions taken this pass
- **New concept page** `wiki/concepts/equity-intraday-backfill-gap.md` — captures the Polygon NOT_AUTHORIZED constraint, the yfinance EOD sweep doctrine, and the 2026-04-24 incident-of-record. Cross-linked from ticker-watchlist (which is the natural entry point for anyone checking per-ticker data completeness).
- **New platform stubs**: `wiki/entities/platforms/polygon.md`, `wiki/entities/infrastructure/yfinance.md` — one-line narratives, frontmatter-complete, cross-link to the new concept page. Content expands as more is learned (plan tier, specific quota limits, etc.).
- **Stale-state bug flagged for future**: Workstream B showed that workspace→server rsync is out-of-scope from this workspace per CLAUDE.md; server-Claude regenerates bodies via DeepSeek instead. This is the **documented pattern** going forward — workspace pages act as the slug/title/relations skeleton source-of-truth; server regenerates bodies as-needed for RAG-use. If a future case needs body-level parity, user runs the rsync manually or approves a one-off workspace exception.

### Brief-stack status
- `briefs/2026-04-24_server-triage-ollama-hunt-and-wiki-refresh.md` — **both workstreams closed**.
- `briefs/2026-04-24_post-capacity-alarm-followup.md` — all ✓ (closed earlier today).
- `briefs/2026-04-24_wiki-search-supervisor-wiring.md` — Parts 1 + 2a + 3 ✓; internal-supervisor work rolled into Step 83.
- `briefs/2026-04-24_track-c-ticket-memo.md` — staging-only; awaits Cemini milestone ledger (P0-1).

## [2026-04-24] distribute | Transferred `briefs/2026-04-24_server-triage-ollama-hunt-and-wiki-refresh.md` to `/opt/cemini/briefs/`

- scp of 7,972-byte / 110-line brief completed. Server-Claude session to execute Workstream A (Ollama reference grep-sweep across `/opt/cemini/`, bucketed report, no modifications until workspace reviews) and Workstream B (rsync workspace `wiki/` → server `research_wiki/` with `--delete`, re-ingest, smoke-test `wiki_search` for INTC/GLW/PL/ASTS/SOFI/SOL/DOGE, verify uber orphan reaped, audit chain clean).
- Workstreams independent; can run in parallel. A is grep-only + report-back (zero mutations); B is rsync+ingest+verify (also exercises the `--prune` path left pending at end-of-Track-B-rebuild for the uber orphan).

## [2026-04-24] ingest | SOL + DOGE + SOFI reports indexed; server-side wiki query issues flagged

- **Ingested 3 Gemini Deep Research reports** (all `_pending_` slots from the 2026-04-24 watchlist rebalance):
  - `SOL 4_24.docx` (3.0 MB) → `wiki/entities/tickers/sol.md` (49,796 B, crypto_native)
  - `DOGE 4_24.docx` (3.0 MB) → `wiki/entities/tickers/doge.md` (47,839 B, crypto_native)
  - `SOFI 4_23.docx` (3.0 MB) → `wiki/entities/tickers/sofi.md` (60,468 B, fintech)
  - Sources moved inbox → `research for cemini/` per standard ingest workflow.
  - **Filename-convention correction**: user's drops were `Solana 4_24.docx` / `_Dogecoin 4_24.docx` / `_SOFI 4_23.docx` — the script's regex `^([A-Z]+)\s` requires a leading uppercase-token-followed-by-space, so these skipped with `SKIP unknown filename pattern`. Renamed the 3 files to canonical `SOL 4_24.docx` / `DOGE 4_24.docx` / `SOFI 4_23.docx` before re-running. Reminder now carried in `wiki/entities/ticker-watchlist.md` "Progress" line so future drops follow the TICKER-not-company pattern on arrival.
- **Index + watchlist updated**:
  - `wiki/entities/ticker-watchlist.md` — 3 rows flipped from `_pending_` → ✅; `related:` list + Relations bullets extended by 3 entries; progress counter **21 / 30 → 24 / 30** (pending: ADA, AVAX, LINK, SPY, QQQ, IWM).
  - `wiki/index.md` — 3 new bullets in Tickers section (alphabetical: DOGE after DIS, SOFI + SOL after SMCI); watchlist reference-line progress counter bumped 13 / 30 (stale) → 24 / 30.
- **Server-side issues flagged by user** (to be handed to server-Claude this pass):
  - **"Still looking for Ollama"** — user reports the server is still trying to reach an Ollama endpoint despite the 2026-04-24 retraction pass that established local-DeepSeek/Ollama is not deployed + DeepSeek cloud API is the intended brain. This is the 3rd surface of the same symptom; needs a grep-sweep of `/opt/cemini/` consumer paths (`agents/orchestrator.py`, `services/llm_analyst/*`, env files, any docker-compose service referencing Ollama) to identify the stale reference and either rewire to `deepseek_client.py` or remove.
  - **"Wiki has no pages for INTC / GLW / PL / ASTS / SOFI yet (only legacy tickers)"** — workspace confirms INTC/GLW/PL/ASTS were created 2026-04-24; SOFI + SOL + DOGE ingested just now. Root cause is stale `research_wiki/` on server — last ingest predates these pages. Needs `rsync` refresh from workspace `wiki/` → server `research_wiki/` + re-run of `scripts/ingest_research_wiki.py` so `wiki_search` (tool #27) can see the 7 new pages (INTC, GLW, PL, ASTS, SOFI, SOL, DOGE) + any others that drifted.
- **Staged brief**: `briefs/2026-04-24_server-triage-ollama-hunt-and-wiki-refresh.md` — two workstreams (Ollama reference hunt + research_wiki refresh + re-ingest). Separate from in-flight briefs; server-Claude can run both in parallel since one is grep-only and the other is rsync+script.

## [2026-04-24] milestone | Track B + supervisor-wiring Parts 2a + 3 complete; wiki_search is tool #27 and live

- **Disk reclaim (server-side, approved by workspace)**: journalctl `--vacuum-size=200M` freed 2.2 GB; explicit `docker rmi` on 5 orphaned pre-rename images (docker-oanda_streamer, docker-pnl_attribution, docker-ccxt_normalizer, docker-finnhub_calendar, docker-risk_governor) freed 2.8 GB. 5.0 GB total reclaimed. Disk now at 16 GB free / 79% used. `docker image prune -a --filter "until=168h"` freed 0 B (all images were built 2026-04-20, inside the 7-day window — filter correctly blocked them; explicit rmi reached them).
- **Image built**: `cemini-mcp:latest` at 2.09 GB. Torch CPU-only wheel + sentence-transformers added per the amended rebuild spec. Container healthy.
- **wiki_search live as tool #27** (main tree had 26 tools; Track B's delta is the 27th). Smoke test: vector mode, count=5, top hit `ensemble-weather-forecasting` sim=0.30. MiniLM + pgvector HNSW cosine search verified working.
- **Tests**: 2910 passing (2907 + 3 new prune tests). Ruff clean. Two commits — `bae4909` (Track B initial wire-up) + `f1995ac` (Parts 2a + 3).
- **Part 2a (supervisor inventory)**: no scatter-gather supervisors exist. `agents/orchestrator.py` is a linear `StateGraph` (confirms Track C #3 retraction). `wiki_search` is exposed to external MCP clients via `cemini_mcp/server.py`; **internal LangGraph consumption is explicitly deferred to Step 83**. This is consistent with the step83-is-docs-only finding: the Send()-topology + richer audit-trail + internal-consumer wiring all collapse into one future build per step83's design spec.
- **Part 3 (ingest-prune)**: `--prune` flipped from unconditional to opt-in; `--prune-dry-run` added for inventory-without-deletion. Each reap logs to `audit_hash_chain` via the existing trigger. Current dry-run: 0 orphans. Pending exercise: uber.md reap — workspace's `wiki/entities/tickers/uber.md` is already absent (removed during 2026-04-24 watchlist rebalance); next workspace → `research_wiki/` rsync with `--delete` mirrors the absence, orphans the DB row, and the prune path reaps it in one pass.
- **Workspace state confirmed clean** on both server-Claude-flagged findings:
  - `wiki/concepts/scatter-gather-topology.md` P1-4 already carries the "build fresh per step83 spec / ~1–2 engineer-weeks" language (from 2026-04-24 post-inventory correction pass; line 32).
  - `uber.md` already absent from local wiki; no further workspace action needed before server rsync.
- **Status of the brief stack**:
  - `briefs/2026-04-24_wiki-search-supervisor-wiring.md` — Part 1 ✓, Part 2a ✓ (inventory: no supervisors to wire), Part 3 ✓. Internal-supervisor work rolled into Step 83.
  - `briefs/2026-04-24_post-capacity-alarm-followup.md` — all three workstreams (A disk reclaim, B Track B rebuild, C Track C walk) ✓.
  - `briefs/2026-04-24_track-c-ticket-memo.md` — staging-only; waits on Cemini milestone-ledger (P0-1) for formal ticket-filing.
- **Next forward step**: Step 83 implementation per its design spec. This is where scatter-gather / Send() topology / internal wiki_search consumer + the richer audit-trail all get built. Workspace-side: a dedicated wiring brief is due once Step 83 leaves design-only and enters implementation. No immediate workspace action on this; revisit when user signals.

## [2026-04-24] correct | step83-llm-analyst is docs-only, not a Send() prototype — 3 wiki pages + ticket memo updated

- **Source**: server-Claude Track B inventory probe (2026-04-24, in response to my 3-workstream decision request). Inventory confirmed: step83 worktree = **two doc commits** (implementation plan + design spec), `orchestrator.py` in step83 identical to main (same `StateGraph, END` imports, no `Send()`), `cemini_mcp/requirements.txt` + Dockerfile unmodified. No Send()-based scatter-gather code, no richer audit-trail code, no wiki_search code on any branch.
- **Why this matters**: Track C's walk (2026-04-24, see earlier log entry) speculated "the step83-llm-analyst worktree in particular carries a richer version of the audit-trail and scatter-gather code than main." That was inference from `docs/ROADMAP.md` marking step83 complete — but step83's deliverable was the *design spec*, not code. This inventory is ground truth; Track C's note about step83 is now disproven.
- **Updated pages**:
  - `wiki/concepts/scatter-gather-topology.md` — Option A ticket scope shifted from "rebase + merge step83 prototype (~2–5 days)" to "build Send() fresh per step83's design spec (~1–2 engineer-weeks)". Option B (retract + rename) unchanged at ~0.5 days. Default recommendation remains Option B unless Send() is on IP-sale critical path.
  - `wiki/entities/infrastructure/deepseek-api.md` — removed the "merge step83 prototype" reference; replaced with the corrected build-fresh path.
  - `briefs/2026-04-24_track-c-ticket-memo.md` — P1-4 ticket re-scoped with the post-inventory effort estimate and default-recommendation framing.
- **Track B rebuild approved**: aggressive prune (`docker image prune -a --filter "until=168h" -f`) + full rebuild sequence (stage + commit 5 untracked Track B items → dbmate up → patch requirements/Dockerfile → register wiki_search tool → rebuild image) per Workstream B of the post-capacity-alarm follow-up brief. Server-Claude to execute. Parts 2 + 3 of `wiki-search-supervisor-wiring.md` proceed post-rebuild.

## [2026-04-24] audit-apply | Track C concept audit → 15-page tag sweep + P0/P1 ticket memo

- **Received**: server-Claude's 15-concept walk (`briefs/track-c-walk-results.md`, 26.6 KB) with verdicts: **5 CONFIRMED** (macro-weather-regime, replacement-cost-valuation doc-only, mappo research-only, publishers-exclusion doc-only, irc-1235-capital-gains-safe-harbor doc-only), **5 TENTATIVE** (ip-sale-readiness, cryptographic-audit-trail, favorite-longshot-bias, game-of-attrition-doctrine, ensemble-weather-forecasting), **5 RETRACTED** (scatter-gather-topology, dispersion-trading, sbom, milestone-ledger, skill-vetting).
- **Applied tags on 15 concept pages** per each walk row's specific "Workspace action":
  - Full retractions (`maturity: retracted` + narrative struck with retained retracted-claim-of-record): `scatter-gather-topology.md`, `dispersion-trading.md`, `sbom.md`, `milestone-ledger.md`, `skill-vetting.md`.
  - Tentatives (maturity kept `validated`; inline `[TENTATIVE — 2026-04-24 Track C audit]` banner + specific sub-claim retractions with evidence): `ip-sale-readiness.md` (components 1,2,4 partial; 5 + SBOM retracted; 6 doc-only), `cryptographic-audit-trail.md` (hash chain real; pg_tamperlog/pymerkle/OpenTimestamps/VCP retracted), `favorite-longshot-bias.md` (AS-logit real; Gumbel + Polymarket retracted), `game-of-attrition-doctrine.md` (regime + Kelly real; CVaR not enforced as gate), `ensemble-weather-forecasting.md` (Open-Meteo real; Gumbel + multi-model + AS-logit weather retracted).
  - Confirmations (maturity kept `validated`; `[CONFIRMED]` banner + evidence bullets): `macro-weather-regime.md`, `mappo.md` (w/ TorchRL → PyTorch+PettingZoo+Gymnasium correction), `replacement-cost-valuation.md` (doc-only), `publishers-exclusion.md` (doc-only), `irc-1235-capital-gains-safe-harbor.md` (doc-only).
- **Staged ticket memo**: `briefs/2026-04-24_track-c-ticket-memo.md` — P0 milestone-ledger + P1 bundle (SBOM, CVaR-gate, vetting-ledger, scatter-gather reconcile) with dependency graph, per-ticket scope/done-criteria, provenance back to Track C walk evidence. Self-referential: P0-1 ships the ledger that will hold these tickets. Targets Cemini milestone ledger (once ledger exists).
- **Promoted**: `entities/infrastructure/deepseek-api.md` `draft` → `validated`. Evidence (from Track C concept #3 scatter-gather walk): `services/llm_analyst/deepseek_client.py` exists as a single shared client called by `agents/orchestrator.py`'s 4-analyst linear StateGraph. [NEEDS VERIFICATION] retained on model-ID + base-URL strings + API-key-in-`.env` presence.
- **Index updated**: all 15 concept rows in `wiki/index.md` `## Concepts` section now carry verdict markers `[C]` / `[T]` / `[R]` / `[Cd]` / `[Cr]` so readers scanning the catalog see audit status at a glance.
- **Pending (server-side)**: Track B inventory probe outstanding (requested as part of the same decision response that approved this workspace-side work). Post-inventory: Track B triage path decision, then supervisor-wiring Parts 2+3, then DeepSeek-API scatter-gather wiring brief.

## [2026-04-24] distribute | Transferred `briefs/2026-04-24_post-capacity-alarm-followup.md` to `/opt/cemini/briefs/`

- scp of 9,497-byte brief completed. Server-Claude session should execute Workstreams A (disk reclaim), B (Track B deploy investigation, read-only), and C (Track C walk-through override) in the parallelism pattern described in the brief (A + C start t=0; B investigation phase starts t=0; B's rebuild phase waits on user approval).
- Ground-rule note in the brief captures the nuance: Ollama-absent is correct state; local-LLM path is not the current target; Workstream B should additionally probe `.env` for the DeepSeek API key name and any existing client instantiation in `/opt/cemini`. This is discovery not action.
- Execution order across the whole pending-brief stack (unchanged by this follow-up):
  1. Post-capacity-alarm follow-up Workstreams A + B investigation + C (parallel) ← **next**
  2. User approves B-verdict rebuild path
  3. Supervisor-wiring brief Parts 2 + 3 (supervisor inventory, decision, impl + ingest-prune flag)
  4. Workspace applies Track C results (confidence tags on concept pages; ticket-file recommendations handed back)
  5. Separate brief: wire DeepSeek API into Cemini (pending draft — blocked until Part 1 of post-capacity-alarm returns + Track B deploy state is clear)

## [2026-04-24] clarify | DeepSeek path is cloud API (key in `.env`), not local weights — new `deepseek-api.md` entity

- **User clarification** following the retraction of the local-weights pages: "the whole point of having the wiki be local is that there isnt enough room on the server for a local llm, i dont have the hardware to run one locally yet but you should be able to use the deepseek api key in the .env to have some form of llm brain in the cemini program and use it to query the local database as needed."
- **What this changes**: the model *family* (DeepSeek) is still Cemini's intended LLM brain. What's retracted is the *local-runtime* deployment (14B weights + Ollama on Hetzner) — that requires hardware that doesn't exist. The operative path is the DeepSeek hosted Chat Completions API, using the API key already present in `/opt/cemini/.env` (name TBD — server-Claude to confirm in the 2026-04-24 post-capacity-alarm follow-up).
- **New entity page**: `wiki/entities/infrastructure/deepseek-api.md` (`maturity: draft`) documents the intended design: OpenAI-compatible SDK pattern with `base_url="https://api.deepseek.com"`; LangGraph supervisors invoke API client instead of Ollama; RAG remains local via pgvector `wiki_search` so no proprietary research leaves the host except via the LLM's response completions; cost + rate-limit envelope pending.
- **Forward-pointers added**: `deepseek-r1-14b.md` and `ollama.md` retraction notes now reference `deepseek-api.md` as the operative alternative. The index.md catalog entries updated the same way.
- **Architectural consequence**: @concepts/cryptographic-audit-trail.md should be revisited when API wiring lands — reasoning traces produced by a third-party service need a different audit anchor than locally-verifiable forward passes. Captured as an open thread on the `deepseek-api.md` page; not a retraction, just a pending refinement.
- **Replacement-cost line-item** on `replacement-cost-valuation.md` stays retracted on the "trained DeepSeek-R1 reasoning harness" clause — but will need a new line-item for "DeepSeek API integration + prompt engineering + wiki-search RAG wiring" once the wiring brief lands.
- **MEMORY.md**: the `retracted_deepseek_ollama.md` pointer updated to capture the nuance (local-weights path retracted; API path is live-intended, pending wiring).

## [2026-04-24] retract | DeepSeek-R1-14B + Ollama are NOT deployed on the Hetzner server

- **User correction**: "deepseek isnt supposed to be installed on the server neither is ollama we have gone through this before" — this is a recurring hallucination pattern the wiki kept reintroducing. Retracted at source this time.
- **Ground-truth evidence** (server-Claude diagnostics, 2026-04-24): no `~/.ollama` directory, `OLLAMA_MODELS` empty, no ollama binary on PATH, no `/usr/share/ollama` or `/opt/ollama`, `cemini_mcp` container requirements.txt contains no LLM-inference deps (no torch, transformers, ollama).
- **Retraction scope — pages fully retracted** (`maturity: retracted`, narrative struck with retained retracted-claim-of-record):
  - `wiki/entities/infrastructure/deepseek-r1-14b.md`
  - `wiki/entities/infrastructure/ollama.md`
- **Retraction scope — inline `[RETRACTED 2026-04-24]` tags applied** on the specific clauses that asserted DeepSeek/Ollama as deployed state (page-level `maturity` kept `validated`; the non-LLM content is unaffected):
  - `wiki/entities/infrastructure/hetzner.md` (CPU-only rationale)
  - `wiki/entities/infrastructure/redis.md` (claimed Ollama prompt-completion session cache)
  - `wiki/entities/observability/tempo.md` (inter-service tracing chain included Ollama)
  - `wiki/entities/frameworks/fastmcp.md` (named "LangGraph DeepSeek-R1 agents" as MCP callers)
  - `wiki/entities/frameworks/torchrl.md` (model-registry "alongside DeepSeek-R1 weights")
  - `wiki/entities/frameworks/langgraph.md` (related-link annotated; narrative unchanged)
  - `wiki/concepts/scatter-gather-topology.md` (reasoning-context + CPU-envelope claims)
  - `wiki/concepts/cryptographic-audit-trail.md` (DeepSeek reasoning-trace claim on anchored events)
  - `wiki/concepts/replacement-cost-valuation.md` (IP-sale replacement-cost line-item claim)
  - `wiki/concepts/sbom.md` (model-weight provenance row-set)
- **Index** (`wiki/index.md`): both entries annotated `[RETRACTED 2026-04-24]` inline (entries kept so the retraction is discoverable from the catalog).
- **Source pages unchanged**: the 3-18 crypto-integration and 3-19 LangGraph scatter-gather / Telegram-Discord research PDFs *do* propose DeepSeek-R1-14B on Ollama as a reference architecture. Source-summary pages faithfully report what the PDFs say; the synthesis error was downstream — crossing from "the research proposes X" to "Cemini runs X in production."
- **LESSONS.md**: new top entry codifying the pattern so it stops happening.
- **Related fix (minor)**: `briefs/2026-04-24_wiki-search-supervisor-wiring.md` Part 1 and `briefs/2026-04-24_track-c-milestone-ledger-walk.md` row 3 both cited DeepSeek/Ollama as production-state assumptions; annotated not rewritten since Part 1 has already been executed and the Track C row's grep probes are LLM-agnostic.

## [2026-04-24] distribute | Transferred both pending briefs to `/opt/cemini/briefs/` via scp

- Transferred `briefs/2026-04-24_track-c-milestone-ledger-walk.md` (12,682 bytes) and `briefs/2026-04-24_wiki-search-supervisor-wiring.md` (16,009 bytes) to the Hetzner host at `/opt/cemini/briefs/` (connection details in `.local/server.md`). Confirmed landing via `ssh ... 'ls -la /opt/cemini/briefs/'`.
- **Policy update note**: CLAUDE.md previously stated "Never push directly to the Hetzner server from this workspace... user handles the transfer." User has explicitly delegated brief-file transfers to Claude Code, citing that the desktop app has SSH access configured. Transfers of staged files in `briefs/` → `/opt/cemini/briefs/` are now in-scope for Claude Code. Code/config modifications on the server remain out-of-scope — those still flow through server-Claude sessions. CLAUDE.md to be amended accordingly (pending).
- Execution order communicated to user: Part 1 capacity check of wiring brief → Track C walk → workspace applies outcomes → Parts 2+3 of wiring brief.

## [2026-04-24] distribute | Staged `briefs/2026-04-24_track-c-milestone-ledger-walk.md` for CeminiSuite

- Track C from the original wire-in brief was never walked — 0 claim-confidence tags (`[CONFIRMED]/[TENTATIVE]/[NEEDS VERIFICATION]/[RETRACTED]`) exist anywhere in `wiki/concepts/`. Walk-through brief drafted for server-Claude (Path A — code-state audit over workspace-judgment audit).
- Brief contains: per-concept probe targets (grep strings, file patterns, psql queries); explicit output schema (Verdict / Evidence / Gap / Ticket recommendation / Workspace action per concept); special handling for 3 doc-only items (no code walk) + 1 research-only (mappo) + 1 meta-gap (milestone-ledger itself); time-box of ~15 min per concept (~2.5 hr total).
- **Design intent stated**: a `[RETRACTED]` verdict is the point of Track C, not a failure. Research-doc aspirational language was synthesized as fact during Phase 2; the audit surfaces where. Server-Claude is instructed not to hedge.
- Explicit anti-scope: no code changes, no server-side wiki edits, no ticket filing. Server-Claude returns `/opt/cemini/briefs/track-c-walk-results.md`; workspace pulls it back and applies tags to concept pages page-by-page.
- Suggests eating own dogfood — use `wiki_search` MCP tool to read the concept pages while doing the audit (validates retrieval quality against 15 known-content pages).
- **Per CLAUDE.md distribution rule: not pushed. User handles the transfer + server-Claude executes.**

## [2026-04-24] structural | Watchlist rebalance — added SOFI (fintech), +5 / −5 even swap (size preserved at 30)

- User follow-up after the MARA/JPM/BAC/GS/UBER removals: **SOFI added** as a new ticker in a new `fintech` category. The rebalance is now an **even +5 / −5 swap** — server-baseline size of 30 symbols is preserved, only the composition shifts.
- **Additions (5)**: ASTS (space tech), GLW (industrials), INTC (mega cap), PL (space tech), SOFI (fintech — pending research).
- **Removals (5)**: MARA (crypto-proxy redundant w/ COIN + MSTR), JPM/BAC/GS (Financials category sunset — placeholders, no research commissioned, off-strategy), UBER (consumer-tech single-report coverage deemed insufficient signal-to-noise; DIS + NFLX retained).
- **Watchlist updated**: Totals (23 equities + 7 crypto native = 30); Categories table (added Fintech row with SOFI); Report status table (+SOFI as `_pending_` row at bottom, now 30 rows total); progress 21 / 29 → **21 / 30**; divergence section renamed from "extension" to reflect swap framing (+5 / −5 net-zero diff); rationale block in divergence diff updated with SOFI explainer (digital-native neobank replaces legacy-bank Financials slot; fintech category is single-ticker for now, flagged for user review on whether to expand).
- **CLAUDE.md**: watchlist 29 → 30; progress 21/29 → 21/30; adds list updated to include SOFI; rebalance framing ("even +5 / −5") in the threads description.
- **Indexer**: `/tmp/index_tickers.py` CATEGORY dict patched to include `"SOFI": "fintech"` ready for when the SOFI docx drops.
- Server-side ticker-config edits are happening in parallel (per user); wiki is now aligned to the intended final state.

## [2026-04-24] structural | Watchlist trim — removed MARA, JPM, BAC, GS, UBER (−5, Financials sunset)

- User directed removal of 5 tickers from the wiki-tracked universe: MARA (crypto-proxy redundant w/ COIN + MSTR), JPM/BAC/GS (Financials category sunset — placeholders, no research commissioned, off-strategy), UBER (consumer-tech single-report coverage deemed insufficient signal-to-noise; DIS + NFLX retained).
- **Deleted** `wiki/entities/tickers/uber.md`. Source docx `UBER 3_24.docx` preserved in `research for cemini/` as historical record (raw-source layer is immutable per workspace schema). The 4 other tickers had no entity pages — nothing to delete there.
- **Watchlist updated**: frontmatter `related:` −1 entry (UBER); Relations section −1 line; narrative summary rewritten with divergence framing (+4 / −5 = net −1 → 29 symbols); Totals updated (22 equities, Financials sunset); Categories table — removed Financials row entirely, trimmed Crypto proxies (3→2), Consumer tech (3→2); Report status table −5 rows (MARA, JPM, BAC, GS, UBER); progress 22/34 → **21/29**.
- **Extension section renamed** "Wiki-tracked extension" → "Wiki-tracked divergence from server config"; JSON diff now carries both `add_to_active_tickers` and `remove_from_active_tickers`, plus `sunset_categories: ["financials"]`. Includes rationale per removal.
- **Index.md**: removed UBER entry from Per-ticker reports subsection (now 21 rows).
- **CLAUDE.md Active research threads**: watchlist 34 → 29; progress 22/34 → 21/29; UBER removed from indexed list; "Watchlist-extension rule" renamed to "Divergence-from-server rule" with add+remove framing.
- **Server-side follow-up needed**: (a) apply the combined add+remove diff to `/opt/cemini/QuantOS/config/tickers.json`; (b) delete the `research_wiki_pages` row for `page_path = 'entities/tickers/uber.md'` on the Hetzner DB — current ingest script is add/update only, doesn't reap orphaned rows after local deletions. Worth flagging in a future ingest-script enhancement: `DELETE FROM research_wiki_pages WHERE page_path NOT IN (<current fs set>)` at end of run, as an optional `--prune` flag.
- **Remaining on 29-ticker watchlist** (pending research): SPY, QQQ, IWM, SOL, DOGE, ADA, AVAX, LINK (8 tickers — 3 indices + 5 crypto-native).

## [2026-04-24] ingest | 9 Gemini Deep Research ticker reports (COIN, DIS, ETH, MSTR, NFLX + 4 watchlist extensions: ASTS, GLW, INTC, PL)

- User dropped 9 docx into `research to be indexed/`. 5 were on the existing 30-ticker watchlist (COIN, DIS, ETH, MSTR, NFLX); 4 are deliberate watchlist extensions (ASTS — AST SpaceMobile, GLW — Corning, INTC — Intel, PL — Planet Labs) confirmed by user.
- Verbose filenames renamed to ticker-prefix form so `index_tickers.py`'s `^([A-Z]+)\s` matcher picks them up: `Ethereum → ETH`, `MicroStrategy → MSTR`, `Netflix → NFLX`, `Planet Labs → PL`. Others (ASTS, COIN, DIS, GLW, INTC) already matched.
- Patched `/tmp/index_tickers.py` CATEGORY dict with 4 new entries: ASTS/PL → `space_tech`, GLW → `industrials`, INTC → `mega_cap`. Bumped TODAY constant to 2026-04-24.
- Ran indexer → 9 new entity pages written: `wiki/entities/tickers/{asts,coin,dis,eth,glw,intc,mstr,nflx,pl}.md` (50K–66K bytes). Source docx moved to `research for cemini/`.
- Two H1-parse misses (ASTS title came out as "ASTS) Equity Research Report (ASTS)"; ETH as "Comprehensive Network, Tokenomics, and Market Structure Analysis (ETH)") — manually patched to `"AST SpaceMobile (ASTS)"` and `"Ethereum (ETH)"` respectively. YAML-quoted per the 2026-04-24 lint rule (colons in value).
- **Watchlist updated (30→34)**: frontmatter `related:` list (+9 entries); Relations section (+9 with extension-date annotations); narrative totals (23 equities → 27); Categories table (added Space tech row with 2 entries, Industrials row with 1 entry, bumped Mega cap 6→7 for INTC); Report status table (5 rows flipped to ✅, 4 new rows appended); progress counter 13/30 → 22/34; added "Wiki-tracked extension" subsection under Snippets with proposed JSON diff for server-side `tickers.json` sync.
- **Index.md updated**: Per-ticker reports subsection rebuilt with 22 entries (added 9 new, kept alphabetical by company name, annotated extensions). Extension tickers flagged inline: ASTS/GLW/INTC/PL carry "(watchlist extension 2026-04-24)".
- **CLAUDE.md updated**: Active research threads — watchlist size 30 → 34, progress 13/30 → 22/34, added watchlist-extension rule (new tickers lead server config; annotate with date; re-pull after server absorbs).
- **Server sync follow-up**: `/opt/cemini/QuantOS/config/tickers.json` does not yet include the 4 extensions. Either extend on the server or keep the wiki as the canonical source pending formal expansion.
- **Remaining on the 34-ticker watchlist**: SPY, QQQ, IWM, MARA, JPM, BAC, GS, SOL, DOGE, ADA, AVAX, LINK (12 tickers, 7 equities + 5 crypto-native).

## [2026-04-24] distribute | Staged `briefs/2026-04-24_wiki-search-supervisor-wiring.md` for CeminiSuite

- Follow-up brief for server-Claude covering three open items from Track B post-ship:
  - (1) **Capacity verification** — pre/post image-size delta + `/var/lib/docker` headroom + MiniLM cache sanity + untouched-Ollama check; explicit alarm thresholds (image +1.4–2.0 GB expected; alarm >+3 GB; `/` ≥30 GB free; DeepSeek cache unchanged).
  - (2) **LangGraph supervisor wiring** — inventory all supervisors, decide per-supervisor whether `wiki_search` belongs in the inherited tool set, add with tests + prompt updates + skill-vetting ledger rows.
  - (3) **Ingest-prune flag** (added in a second pass after the watchlist rebalance) — `/opt/cemini/scripts/ingest_research_wiki.py` currently add/update-only; adds `--prune` + `--prune-dry-run` flags with audit-chain integration + test coverage. First real test case is the orphaned UBER row (deleted locally, still embedded in DB). Per-row audit events (`event_type='wiki_row_pruned'`) keep the prune chain reverse-traceable.
- Execution order gates Part 2c and Part 3a onward behind workspace review of Part 2a inventory — single review checkpoint covers both tool-wiring and ingest-script changes. Preserves skill-vetting doctrine (no bulk auto-inheritance of tools).
- **Per CLAUDE.md distribution rule: not pushed. User handles the transfer + server-Claude executes.**

## [2026-04-24] distribute | Track B shipped — Cemini pgvector RAG index live

- Second ingest on Cemini picked up 82 new/changed rows (the YAML-quoted set + a few session-updated pages). DB now at 293 rows in `qdb.public.research_wiki_pages`. SHA gate confirmed hot — only the changed set re-embedded.
- HNSW index built with `m=16, ef_construction=200` to match the existing `intel_embeddings` table's parameters (side-by-side query parity).
- Brief synced back with three server-side patches: (a) psycopg2 (v2) swap — server venv lacks psycopg v3; (b) DSN fallback from 4 `POSTGRES_*` / `DB_HOST` env vars with `172.23.0.12` bridge IP default for host-side runs outside the Docker network; (c) YAML `try/except` in `parse_page` for defense against future bad frontmatter; (d) explicit `conn = psycopg2.connect(...) + try/except/finally` pattern (psycopg2's context manager only manages the transaction, not the connection lifecycle).
- Fixed one brief-side sync error: the `try` block in `main()` was missing its `except/finally` closer in the workspace copy. Patched. Server-side code was already complete — the paste showed the intended block structure.
- **Canonical code from this point is `/opt/cemini/scripts/ingest_research_wiki.py`.** The brief is now a frozen point-in-time shipped-state record. Future iteration happens on the server; workspace brief no longer tracks.
- **Remaining for Track B**: wire the `wiki_search` FastMCP tool into Cemini's LangGraph supervisors per the brief. Not yet shipped.
- **Track C (milestone-ledger seed)**: not yet started. 15-row gap-analysis table still in the brief waiting for engineering review.

## [2026-04-24] lint | Quoted 83 source-stub titles to fix YAML parse errors

- Cemini pgvector ingest skipped 79 source pages on first run: unquoted colons in `title:` frontmatter (e.g. `title: RefineRL: Advancing...`) broke YAML parse. These were legacy stubs from the bootstrap-230 corpus ingest; the Phase 2 synthesis pages were already quoted correctly.
- Ran `/tmp/fix_yaml_titles.py` → quoted 83 titles (regex: unquoted value containing a `:`). Verified all 293 pages now parse via `yaml.safe_load`.
- Workspace is ready for re-rsync. Next ingest on Cemini should pick up the full 290-page set (vs 211 on first run).
- **Incidental finding**: several "titles" are actually document abstracts mis-captured as titles by an earlier bootstrap extraction. Out of scope for this fix — they're valid YAML now, they're just bad titles. Flag for a future lint pass.

## [2026-04-23] distribute | Staged `briefs/2026-04-23_cemini-wire-in.md` for CeminiSuite

- Two-track delivery brief drafted: (B) pgvector RAG ingestion of `wiki/` into `research_wiki_pages` + FastMCP-exposed `wiki_search` tool for LangGraph; (C) milestone-ledger seed table mapping 15 validated concept pages to `shipped | partial | gap-likely | doc-only` statuses with follow-up questions per row.
- Brief contains: full SQL schema, ingestion script (idempotent via SHA gate), rsync+ssh transfer recipe, skill-vetting audit for the retrieval tool, and a 4-step execution order (milestone-ledger-itself first, then verify claims, then file gap tickets).
- **Per CLAUDE.md distribution rule: nothing pushed to Hetzner. User runs the transfer after review.**

## [2026-04-23] lint | Phase 3 — closed bidirectional gaps + created 3 dangling-ref stubs

- Ran `/tmp/phase3_lint.py` across 290 pages. Initial state: **0 orphans**, **0 stale unread-stub tags**, **26 bidirectional gaps**, **3 dangling refs**.
- Ran `/tmp/phase3_lint_fix.py` → closed all 26 gaps (inserted reciprocal `related:` entries + updated Relations sections + bumped `updated`).
- Created 3 concept stubs (`maturity: draft`) for dangling refs from entity pages: `concepts/carry-trade.md`, `concepts/cameo-codes.md`, `concepts/goldstein-scale.md`. Added to index.md under Alt-data taxonomy (stubs) subsection.
- Re-ran lint → **0 orphans, 0 gaps, 0 dangling, 0 stale tags**. Clean.

## [2026-04-23] synthesis | Phase 2 — spawned 50 entity + concept pages from 5-manifest aggregation

- Aggregated entities/concepts across 5 Phase-1 manifests (`/tmp/phase1_agent{1_small,2_method,3_infra_strat,4_crypto,4_unblocked_docx}.json`) → 174 unique entities, 285 unique concepts, 4 tickers. Raw aggregation: `/tmp/phase2_aggregated.json`.
- Option A (priority tier) confirmed with user → spawned 35 entity + 15 concept pages via `/tmp/phase2_spawn.py` (all `maturity: validated`).
- **Entities** (35) by category: platforms (kalshi, polymarket, hyperliquid, oanda, alpaca); data-sources (gdelt, fred, open-meteo, finnhub, telethon); infrastructure (hetzner, ollama, deepseek-r1-14b, timescaledb, redis, pgvector, polars); frameworks (langgraph, fastapi, fastmcp, pydantic-v2, ccxt, nautilustrader, torchrl, pettingzoo, finbert); observability (prometheus, loki, grafana, tempo); security (syft, cyclonedx, trivy, semgrep); components (kelly-cvar-risk-engine).
- **Concepts** (15): ip-sale-readiness, cryptographic-audit-trail, scatter-gather-topology, macro-weather-regime, favorite-longshot-bias, replacement-cost-valuation, dispersion-trading, game-of-attrition-doctrine, ensemble-weather-forecasting, mappo, sbom, milestone-ledger, publishers-exclusion, irc-1235-capital-gains-safe-harbor, skill-vetting.
- Patched 28 source stubs' `related:` frontmatter + Relations section bidirectionally (entity/concept backlinks added without disturbing existing refs). `updated:` bumped to 2026-04-23.
- Promoted 9 previously-sandbox-blocked docx source stubs `draft → validated` and re-rendered their Narrative sections from `/tmp/phase1_agent4_unblocked_docx.json` (abstract + key_findings + entities + concepts instead of truncated stub text): 3-10-cryptographic-research, 3-18-crypto-integration-technical-audit, 3-19-langgraph-scatter-gather-financial-analysis, 3-19-ip-sale-research, 3-19-telegram-discord-research, 3-19-compliance-research, 3-19-kalshi-trading-strategy-research, trading-playbook-research, forex-research-3-18. Read status flipped `unread-stub → deep-read`; `unread-stub` tag removed.
- Updated `wiki/index.md`: Entities section expanded with 7 new subsections (platforms, data-sources, infrastructure, frameworks, observability, security, components); Concepts section replaced with 4-subsection grouping (strategy-doctrine, audit-compliance, trading-strategy, m-and-a-legal).
- **Non-spawned** (deferred): ~150 singleton entities + ~270 singleton concepts with single-source references. Policy: they remain inline-referenced on source stubs; promote to own page only if a future ingest introduces a second reference.
- **Phase 2 deliverables**: all 5 manifests reconciled into the wiki; no more sandbox-blocked sources; the Cemini IP-sale-to-institutional-buyer strategic frame now has a coherent index entry point.

## [2026-04-23] ingest | 5 more Gemini Deep Research ticker reports (AVGO, GOOGL, META, SMCI, UBER)

- User dropped 5 more ticker report docx into `research to be indexed/`: `Broadcom 3_24.docx`, `GOOGL 4_23.docx`, `Meta 4_23.docx`, `Uber 3_24.docx`, `SMCI 4_23.docx`.
- Non-ticker filenames renamed to canonical ticker-prefix form (`AVGO 3_24.docx`, `META 4_23.docx`, `UBER 3_24.docx`) so `index_tickers.py`'s `^([A-Z]+)\s` matcher picks them up; `GOOGL` and `SMCI` already matched.
- Ran `/tmp/index_tickers.py` → 5 new entity pages written: `wiki/entities/tickers/{avgo,googl,meta,smci,uber}.md` (51K–71K bytes). Source docx moved to `research for cemini/`.
- Updated watchlist: `related:` frontmatter, Relations section, and Report Status table (5 rows flipped to ✅). Progress counter 8 → 13.
- Updated `wiki/index.md`: added 5 new rows to Per-ticker reports subsection, bumped progress counter.
- Updated `CLAUDE.md` Active research threads progress counter.
- **Progress**: 13 / 30 tickers indexed. Remaining: SPY, QQQ, IWM, COIN, MSTR, MARA, JPM, BAC, GS, DIS, NFLX, ETH, SOL, DOGE, ADA, AVAX, LINK.
- **Workflow note**: verbose filenames (company names rather than tickers) need rename before the script runs. Script matcher only accepts `[A-Z]+\s...`.

## [2026-04-23] ingest | 8 Gemini Deep Research ticker reports indexed

- User dropped 8 docx reports into `research to be indexed/` (AAPL, AMD, AMZN, BTC, MSFT, NVDA, PLTR, TSLA — first batch of the 30-ticker watchlist) authored via the Gemini Deep Research prompt.
- Identified report template as the canonical per-ticker format: six sections — Business Overview · Competitive Landscape · Financial Profile · Recent Events · Forward Catalysts · Analyst & Sell-Side Context. Closes the "per-ticker report format" open question.
- Built `/tmp/index_tickers.py`: walks docx body in document order (paragraphs + tables), preserves Heading 1-4 + List Bullet/Number styles, renders tables as markdown pipe-tables, demotes all headings by one level to nest under the page's "## Narrative" anchor.
- Wrote 8 entity pages at `wiki/entities/tickers/<symbol>.md` (48K–62K bytes each). Frontmatter: `type: entity`, `maturity: validated`, `report_source: gemini-deep-research`, `report_date: 2026-04-23`, category + ticker + `related: [entities/ticker-watchlist.md]`.
- Moved source docx from inbox → `research for cemini/` for corpus persistence.
- Updated `wiki/entities/ticker-watchlist.md`: added 8 entries to frontmatter `related:`, populated Relations section, rebuilt "Report status" table (30 rows, 8 ✅ with links / 22 `_pending_`).
- Updated `wiki/index.md`: added "Per-ticker reports" subsection under Entities → Reference/infrastructure listing all 8 with category labels.
- **Progress**: 8 / 30 tickers indexed. Remaining: SPY, QQQ, IWM, META, GOOGL, SMCI, AVGO, COIN, MSTR, MARA, JPM, BAC, GS, DIS, NFLX, UBER, ETH, SOL, DOGE, ADA, AVAX, LINK.

## [2026-04-23] lint | Flagged 12 link-evaluation docs as multi-topic

- User flagged that files named `*links*.docx` / `*link re*.docx` are URL/GitHub-evaluation aggregates — each contains unrelated topics stitched together for review purposes, not a single-subject paper.
- Tagged 12 files (`3_26 link re 3`, `3_27 links 1/2/re 2`, `3_28 links 1/2`, `4_3 link re 2/research`, `4_4 link re/re 2`, `4_5 links/2`, `4_6 links`) with `link-evaluation` + `multi-topic` tags.
- Added a warning block at top of each stub: cluster tags reflect union of topics touched, not a single subject; sections should be treated as independent ingest candidates at promotion time.
- Cluster counts without link-eval noise (clean): llm-agents 114, rl-marl 87, cemini-internal 62, quant-finance 51, market-microstructure 49, prediction-markets 39, crypto 31, portfolio-strategy 30, infrastructure 24, ml-methods 24, options-derivatives 19, time-series 12, alt-data 11, audit-security 9, data-engineering 4, game-theory 1.

## [2026-04-23] lint | Library hygiene pass — dedupe, titles, multi-tag, quality flags

- Reframed goal: library is neutral/non-biased; schema should enable discovery, not drive a thesis.
- **Dedupe**: content-hashed first 1K chars of normalized text across 230 records. 4 duplicate files folded into 3 canonical pages (e.g. `4:14 lang.pdf` / `4:14 rl .pdf` / `pvg6 4:14.pdf` → single `4-14-lang.md`). Canonical chosen by preference: PDF > docx, then longest extracted text. Duplicate filenames listed in the canonical page's Raw Concept.
- **Title extraction improved**: absorbs multi-line titles (prepositions / short title-case tails / lowercase continuations) instead of cutting at the first line break. Fixed "Adaptive Social Metaverse Streaming based on Federated Multi-Agent Deep Reinforcement **Learning**" (was: "…Deep Reinforcement").
- **Multi-tag clusters**: `clusters: [...]` now lists every matching cluster, not just the first. Backward-compatible — primary cluster (for index grouping) is the first tag.
- Added clusters: `prediction-markets`, `alt-data`, `game-theory` on top of the original 12.
- **Quality flags**: 23 stubs (22 `no-cluster-match` + 1 `title-unclear`) carry a `needs-review` tag. Mostly hardware/math papers outside current cluster taxonomy.
- Old stubs backed up to `/tmp/wiki_sources_pre_hygiene/` before rewrite.
- **Final state**: 226 canonical stubs, 4 duplicates folded, 23 flagged for review, all `maturity: draft`.

## [2026-04-23] structural | Retracted DRI thesis from schema

- User flagged that the "DRI thesis" / "GEO Group" / "Detention Reengineering Initiative" thread carried forward in CLAUDE.md and memory was not actually their work.
- Triggered after a full-corpus scan turned up zero DRI-relevant material (228 PDFs/docx scanned end-to-end; 1 tangential ADS-B mention, 1 stray "surveillance state" phrase — nothing supporting the thesis).
- Removed from `CLAUDE.md`: the entire `Active research threads → DRI thesis` bullet, the `Retracted / weak` Kern County bullet, and the `Evidence streams currently feeding the DRI thesis` section. Replaced frontmatter example `related:` paths (geo-group, detention-reengineering-initiative) with generic placeholders.
- Removed from memory: deleted `memory/dri_thesis.md`, dropped its row from `MEMORY.md`.
- Cleaned remaining `DRI` mentions from `wiki/index.md`.

## [2026-04-23] ingest | Corpus bootstrap — 230 source stubs

- Extracted first ~3 pages / first ~2000 chars of every readable file in `research for cemini/` (147 PDFs + 81 docx + 2 md = 230 records). Image files (6 jpeg + 3 jpg + 1 png) and Apple Pages files (2) skipped — no text extraction path.
- Scripts used (retained in `/tmp/` for re-runs): `bootstrap_extract.py` (pypdf + python-docx) and `generate_stubs.py` (slug + title + cluster heuristics).
- Every record produced a `wiki/sources/<slug>.md` stub with frontmatter (`maturity: draft`, `read status: unread-stub`) and a Narrative seeded from the first sentences / abstract. All are **draft, unread** — titles and summaries will need cleanup on first deep read.
- Cluster distribution (first-keyword-wins heuristic — approximate, many papers straddle clusters):
  - `rl-marl`: 108 — `llm-agents`: 59 — `portfolio-strategy`: 12 — `options-derivatives`: 12 — `ml-methods`: 10 — `quant-finance`: 8 — `market-microstructure`: 6 — `uncategorized`: 6 — `osint-geopolitics`: 3 — `audit-security`: 3 — `crypto`: 2 — `cemini-internal`: 1
- Updated `wiki/index.md` to list all 230 source pages grouped by cluster.
- **Known stub artifacts**: some titles are truncated at line breaks (e.g. "Adaptive Social Metaverse Streaming based on Federated Multi-Agent Deep Reinforcement" cuts before "Learning"); some stubs landed in the wrong cluster because the heuristic matched an incidental keyword. These self-correct on read.
- **Not yet done**: no cross-references between stubs; no entity/concept pages spawned; no source has been promoted past `draft`.

## [2026-04-23] structural | Initial wiki scaffold

- Scaffolded `wiki/` with `index.md`, `log.md`, and the three content directories: `sources/`, `entities/`, `concepts/`.
- Rewrote root `CLAUDE.md` as a proper schema, synthesizing Karpathy's LLM Wiki pattern with ByteRover's Context Tree structure and Cemini's own ROADMAP page conventions.
- Created `briefs/` directory at workspace root for staged outputs.
- Migrated `reference/ticker-watchlist.md` → `wiki/entities/ticker-watchlist.md` with full frontmatter, retired the `reference/` folder.
- Source material consulted for schema design:
  - `research for cemini/llm-wiki.md` (Karpathy — local copy)
  - `research for cemini/llm re 4:3.pdf` (ByteRover paper, 19p — read in full)
  - `research for cemini/ROADMAP.md` (CeminiSuite dev roadmap — page-writing style reference)

No source pages yet. Bootstrap of `research for cemini/` corpus queued as next step — first-page extraction per PDF → `wiki/sources/` stubs with real titles + one-line summaries.
