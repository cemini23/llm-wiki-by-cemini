# Roadmap

Forward-looking project plan. Companion to:

- `wiki/log.md` — backward-looking chronological log of completed operations
- `LESSONS.md` — meta-lessons about *how* we work
- `CLAUDE.md` — the operational schema (rules of the wiki)

Roadmap entries are aspirational and re-shuffle as priorities shift. As an item ships, move it to **Done** with the commit SHA.

---

## Now — current session (2026-04-25)

| Item | Status | Model | Notes |
|---|---|---|---|
| **C** Exercise Exa on a real research question | queued | Opus | Pick a substantive question (e.g. "regulatory developments for prediction-market DCMs since the Feb 25 Kalshi advisory"), run through `web_search_advanced_exa`, file the synthesis as a brief. Pressure-tests the doctrine end-to-end. |

## Next session — break-and-resume

| Item | Status | Model | Notes |
|---|---|---|---|
| **D** Big orphan sweep | queued | mixed | 201 of 311 pages have zero inbound `related:` edges (post-A this drops by ~7-10). A focused sweep would file each orphan under the right entity/concept. Opus for categorization decisions, Sonnet for bulk re-linking. Multi-hour, deserves its own session. |

## Soon — small carryover items

| Item | Status | Notes |
|---|---|---|
| Index SPY, QQQ, IWM ticker reports | blocked on user drop | When user drops `SPY <date>.docx` etc. into `research to be indexed/`, run `scripts/index_tickers.py`. Completes watchlist 30/30. |
| Split `wiki/concepts/publishers-exclusion.md` into APA vs IAA disambiguation | pending | Two distinct legal concepts currently sharing one page. |
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
