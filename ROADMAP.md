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
| **A** Crypto concept scaffold + cross-link 7 ticker reports | in progress | Opus | Stand up `concepts/crypto-asset-taxonomy.md` (unifies all 7) and `concepts/oracle-networks.md` (LINK-focused). Add `related:` edges from BTC/ETH/SOL/DOGE/ADA/AVAX/LINK → these concepts. Removes 3+ orphans, creates discoverability by topic. Optional Tier-2: `concepts/blockchain-l1-comparison.md` if scope permits. |
| **B** Three loop-closers | queued | Sonnet | (1) Local-PDF extraction for SSRN 3000747 → resolves the partial from follow-up #2. (2) Add dates to 3 undated `[NEEDS VERIFICATION]` tags in `deepseek-api.md`. (3) Add `related:` backlinks for ada/avax/link → ticker-watchlist (always-on minimum cross-link). |
| **B′** Interlude: GitHub lint workflow + pre-commit hook | queued | Opus | `.github/workflows/lint.yml` runs `wiki_lint.py` on push to `main` + weekly cron Monday noon UTC. Pre-commit hook blocks server IP / `.env` / `.DS_Store` from being committed. Non-gating, informational only. |
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
| `.github/workflows/lint.yml` | high — doing as B′ this session | Runs `wiki_lint.py` on push + weekly cron. Informational, non-gating. |
| Pre-commit hook (local, `.git/hooks/pre-commit`) | high — doing as B′ this session | Block commits containing `5.161.53.103`, `\.env`, `.DS_Store`, raw API keys. Cheap insurance after the IP-scrub incident. |
| GitHub Issues for roadmap items | low | Could mirror this file as Issues. Overkill for a one-person project right now. Revisit if the roadmap grows past ~20 items. |
| Dependabot / Renovate | skip | No `requirements.txt` to watch. |
| LICENSE file | skip | Private repo. |
| Auto-format frontmatter workflow | skip | Risk of clobbering hand-edited YAML. Lint surfaces issues, human fixes. |

---

## Done — this session

(Empty so far. Items move here as they ship, with commit SHA.)
