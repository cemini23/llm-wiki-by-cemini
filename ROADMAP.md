# Roadmap

Companion to `CLAUDE.md` (schema), `wiki/log.md` (log), `LESSONS.md` (meta-lessons).
History before 2026-11-16 is in `docs/archive/ROADMAP_ARCHIVE_2026-11-16.md`.

---

## 1. Standing invariants and anti-bloat rules

- **Overwrite in place.** Never append a new dated state block. Edit the project's single block.
- **Uncapped discovery, one queue file per project.** Any number of `Integrate`/`Extract` winners per batch. Never a per-URL brief; append to `briefs/<project>-upgrade-queue.md`, ranked by ROI.
- **Harness is frozen during link evaluations.** No harness edits while an eval batch runs.
- **Boundary:** no install, no clone, no scrape, no trade, no xsp/pm scp, no route swap, never auto-arm.
- **Priority stack:** #1 Atto · Collectibles · Game-Time (co-equal). #2 CeminiDFS · CeminiParlays. #3 GuruWatcher · Basgiath.

Last updated: 2026-11-22.

## 2. Priority #1

### Atto

**Current:** The ISTAT gazetteer is the open design question for Atlas; the `?year=&place=` contract is agreed. No statute is treated as fact until the five-field citation check runs. For the HTR lane, 2611.24726 reports text-line segmentation at CER 2.48–7.07% and is the current best reference.

**Next:**
1. Scope the gazetteer source for suppressed comuni and pre-unification provinces.
2. Wire the firecrawl gov-index citation check into `atto-mcp`.
3. Slice eras for lazy-loading (issue #158 lesson).

### Collectibles

**Current:** The blocker is the hand-labelled set, not another crawler. Scraping stack: spider (MIT) and crawlee (Apache-2.0) are clean; pagesift is AGPL; botasaurus anti-detect is an open per-site evasion decision.

**Next:**
1. Build the labelled set before evaluating a ninth crawler.
2. Keep AGPL tools out of the shipped bundle.

### Game-Time

**Current:** `~/Projects/game-time` does not exist. Three Travian documents are the whole project: design brief, architecture spec, deep research. The design brief calls the spec "a two-year scope presented as four phases". A first milestone must contain an AI opponent.

**Next:**
1. Pick one milestone with an AI warlord in it, and scope only that.
2. Create the repo and the milestone spec.
3. Scaffold the slice harness.

## 3. Priority #2

### CeminiDFS

**Current:** The box-score Gaussian copula paper (2611.10152) is evidence for the copula step `dfs-distribution-layer` already specifies. It beats independence in 25 of 27 joint thresholds. Do not copy magnitudes; playing time drives the dependence.

**Next:**
1. Map dependence inputs to snap share and route participation.
2. Test the copula step against an independence baseline.

### CeminiParlays

**Current:** Exit quality is the moat, not quote price; 75% of volume is parlays. Judge McMahon held Novig's event contracts are sports betting and the CEA does not preempt state law. The CFTC state-access order collides with that. Geofence coverage is a correctness requirement. Kalshi now creates on-request RFQ markets, so new-series announcements are a discovery input.

**Next:**
1. Treat geofence coverage as a correctness gate, not a nicety.
2. Size against the venue the bot actually quotes on.
3. Watch new-series announcements as a market-discovery feed.

## 4. Priority #3 and infrastructure

- **GuruWatcher** — Alert-only, 15-minute timer on egress-fi. GW-06 (HTML cleaning turns `VIX < 20` into `VIX 20`) is data corruption and is still unfixed. A silent 2-hour outage on 2026-11-05 means "enabled" is not "ran". CPI-surprise direction is regime-dependent: the equity reaction to a positive surprise flipped sign after 2020 because shocks became supply-driven. Equity vol also rose while FX vol stayed flat.
- **Basgiath** — Waiting on `/seo geo` and `/seo agentic` passes. No code lane active.
- **OSINT Wiki** — Eight domains in one public repo since 2026-10-14. Inbox empty after the 2026-11-22 ingest of 95 sources. Lint reads 0 hard errors as of 2026-11-22. The digest duplicate check now finds real duplicates: 1 in 95, against 24 in 64 before the fix.
- **cemini-egress-fi** — Back since 2026-11-14, 16G stored, Tailscale-only. Archive writes queue locally when the link is down (CLAUDE.md Step 9).
