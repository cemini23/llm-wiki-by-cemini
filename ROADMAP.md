# Roadmap

Forward-looking project plan. Companion to:

- `wiki/log.md` — backward-looking chronological log of completed operations
- `LESSONS.md` — meta-lessons about *how* we work
- `CLAUDE.md` — the operational schema (rules of the wiki)

Roadmap entries are aspirational and re-shuffle as priorities shift. As an item ships, move it to **Done** with the commit SHA.

---

## Now — current session (2026-04-25)

*(empty — G+H + I shipped; see Done. Deep-read of `sources/3-10-cryptographic-research.md` queued next per Soon-row.)*

## Next session — break-and-resume

| Item | Status | Model | Notes |
|---|---|---|---|
| **D** Big orphan sweep | queued | mixed | 198 of 313 pages have zero inbound `related:` edges (post-A baseline; brief in `briefs/` doesn't change this). A focused sweep would file each orphan under the right entity/concept. Opus for categorization decisions, Sonnet for bulk re-linking. Multi-hour, deserves its own session. |
| **F** Per-ticker Exa research briefs + cross-link to research corpus | queued | mixed | Run an Exa pass per indexed ticker (27 today; 30 once SPY/QQQ/IWM land). File each as `briefs/2026-MM-DD_<symbol>-exa-deep-dive.md`. Cross-reference back to (a) `wiki/entities/tickers/<symbol>.md` and (b) any matching Gemini DR-derived `wiki/sources/` pages. Format suggestion: 6-section structure mirroring the existing ticker reports (Business / Competitive / Financial / Recent Events / Forward Catalysts / Analyst & Sell-Side) but **forward-looking only — last 90-180 days**, since the Gemini DR pass covers the historical baseline. Opus for synthesis sections, Sonnet for the mechanical Exa-search-and-extract step. Each brief ~15-30 min focused work; full sweep ~7-15 hours, naturally batched in 5-7 tickers per sub-session. |

## Soon — small carryover items

| Item | Status | Notes |
|---|---|---|
| Index SPY, QQQ, IWM ticker reports | blocked on user drop | When user drops `SPY <date>.docx` etc. into `research to be indexed/`, run `scripts/index_tickers.py`. Completes watchlist 30/30. |
| Deep-read `wiki/sources/3-10-cryptographic-research.md` | pending | Stub-status; promote with full read pass when relevant. |

## Eventually — larger / structural

| Item | Status | Notes |
|---|---|---|
| **E** Storage compaction | deferred — own session | Disk 88% full, 25G free. Market dataset (1.6G, 17K `.txt` files) → Parquet recovers ~1.4G; or delete locally if server-resident. Research corpus (596M PDFs) → SQLite FTS index + zip originals saves ~200-300M and speeds up grep. **Verify market data is on the server before deleting locally.** Destructive in spirit; needs deliberate planning. |
| Bootstrap full PDF content index | partial | 230 stubs done from first-page extraction. Full-corpus deep-read is the long horizon — happens organically as queries surface specific sources. |
| Workspace ↔ server reconciliation rhythm | open | Per memory, body-divergence is intentional (workspace = Gemini DR-curated; server `research_wiki/` = DeepSeek RAG cache). Periodic comparison of *structure* (page counts, slug parity) would catch drift. Cron candidate. |
| Briefs distribution automation | open | Manual `scp` to `/opt/cemini/briefs/` works for now. Revisit only if brief volume grows or if a "stage in `briefs/` → push button → it's on the server" flow becomes worth the friction-removal. |
| Test suite for `scripts/index_tickers.py` | deferred | No fixtures yet. Defer until the script is touched again or a regression is observed. |

## Open questions

- Rename workspace folder off `Desktop/OSINT WORKSPACE`? (User offered; no pressing reason yet.)
- LICENSE file — only if we ever plan to make the repo public; private for now.
- Is the local `market dataset/` actually used, or is it server-resident-and-also-on-laptop redundancy? Decide before E (storage compaction).

## GitHub-specific dev infra (under consideration)

| Item | Priority | Notes |
|---|---|---|
| ~~`.github/workflows/lint.yml`~~ | ✅ shipped as B′ (`33aca6c`) | Runs `wiki_lint.py` on push + weekly Mon 12:00 UTC cron + manual dispatch. Informational, non-gating. |
| ~~Pre-commit hook (local)~~ | ✅ shipped as B′ (`33aca6c`) | `scripts/pre-commit.sh` blocks server IP / `.env*` / `.DS_Store` / `sk-…` API keys in staged additions. Install with `bash scripts/install-hooks.sh`. |
| GitHub Issues for roadmap items | low | Could mirror this file as Issues. Overkill for a one-person project right now. Revisit if the roadmap grows past ~20 items. |
| Dependabot / Renovate | skip | No `requirements.txt` to watch. |
| LICENSE file | skip | Private repo. |
| Auto-format frontmatter workflow | skip | Risk of clobbering hand-edited YAML. Lint surfaces issues, human fixes. |

---

## Done — this session

| Item | Commit | Notes |
|---|---|---|
| ROADMAP.md created | `526b174` | Forward-looking project plan; companion to `wiki/log.md` (chronological) and `LESSONS.md` (meta-lessons). |
| **A** Crypto concept scaffold + cross-link 7 ticker reports | `4c6aa85` | Created `wiki/concepts/crypto-asset-taxonomy.md` (4 categories: store-of-value, programmable L1, memecoin/PoW, oracle middleware) and `wiki/concepts/oracle-networks.md` (LINK-focused). Added bidirectional `related:` edges across all 7 crypto ticker pages (btc/eth/sol/doge/ada/avax/link), the watchlist, and `wiki/index.md`. Folded original B.3 (ada/avax/link → watchlist backlinks) into this work. Lint clean; orphans 201 → 198. |
| **B** Two loop-closers | `0d59a60` | (1) `stock-7-4-5.md` resolved: Tandiontong + Sitompul, GATR J. Bank. Fin. Review 2(2):21–27 (2017), Altman Z-Score + beta + inflation on Indonesian BEI, cluster `uncategorized→quant-finance`. (2) 3 undated `[NEEDS VERIFICATION]` in `deepseek-api.md` stamped `2026-04-25`. |
| **B′** GitHub Actions lint workflow + local pre-commit hook | `33aca6c` | `.github/workflows/lint.yml` (push + Mon 12:00 UTC cron + manual dispatch). `scripts/pre-commit.sh` blocks server IP / `sk-…` keys / `.env*` / `.DS_Store`. `scripts/install-hooks.sh` symlinks the hook into `.git/hooks/`. Made `wiki_lint.py` portable (`__file__`-relative `WIKI` path) so CI can find the wiki. Hook validated against 5-pattern matrix + caught its own first commit attempt. Also moves the GitHub-specific dev infra "Pre-commit hook" + "lint workflow" rows out of the "under consideration" table. |
| **C** Exa pressure-test brief: post-Kalshi-advisory regulatory landscape | `69d872d` | `briefs/2026-04-25_post-kalshi-advisory-regulatory-update.md` (gitignored) — synthesis of CFTC ANPRM (RIN 3038-AF65, 91 FR 12516, comments due Apr 30) + state enforcement track (MI civil, AZ 20 misdemeanor counts, NV TRO, NY cease-and-desist) + federal preemption counter-suit (CFTC sued AZ+CT+IL, Liburdi TRO Apr 10 expired Apr 24, Third Circuit upheld NJ, Sixth Circuit split → SCOTUS path) + Selig House Ag testimony. 4 parallel `web_search_advanced_exa` queries date-bounded `2026-02-25 → 2026-04-25`, all primary-doc-corroborated. Doctrine pressure-test passed; ingest-back-to-wiki plan deferred (~4-6 page mini-cluster). Lint clean. Same commit also adds new "Next session" row **F** (per-ticker Exa research briefs) per user request. |
| **G+H** Post-Kalshi regulatory ingest + publisher's-exclusion APA/IAA split | `8f21f64` | **G**: ingest-back of the C brief — 4 new pages (`sources/cftc-anprm-prediction-markets-2026-03-16.md`, `sources/cftc-selig-house-ag-testimony-2026-04-16.md`, `sources/cftc-v-arizona-tro-liburdi-2026-04-10.md`, `concepts/dcm-state-preemption.md`); compliance-research S20 promotion with full FR docket; kalshi role 3 expanded with "actively defended by federal counter-suit" qualifier; hyperliquid + polymarket cross-links. **H**: split `concepts/publishers-exclusion.md` into APA-exclusion-schedule sense (`-apa.md`, the renamed original via `git mv`) and IAA §202(a)(11) bona-fide-publication sense (`-iaa.md`, new); disambig stub at the vacated path; 7 caller pages re-pointed; closes the "Soon" row. Combined commit because 4 files (polymarket / ip-sale-readiness / compliance-research / index) carry hunks from both threads. 16 files, 554 insertions. Lint clean (0 bidirectional gaps, 0 dangling, 0 missing). |
| **I** Data-source expansion from public-apis curated list | `d337e51` | Librarian-hygiene pass against https://github.com/public-apis/public-apis. 8 new `entities/data-sources/` stubs (sec-edgar, federal-register-api, openfigi, coingecko, nws-weather-gov, opensanctions, marketaux, nasdaq-data-link), each `maturity: draft` with one strategic backlink hub. Bidirectional updates to 6 hub pages; index Data sources 5 → 13 rows resorted alphabetically. Triaged ~40 candidates rejected (duplicate or fail curation bar). 15 files, 538 insertions. Lint clean. Cemini integration angles flagged "not yet wired" throughout — librarian-side additions; no server-side configuration implied. |
