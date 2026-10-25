---
title: K288 Eval Wave — the DFS eval's mass false negative (Oct 2026)
type: concept
tags: [k288, eval, dfs, parlays, eval-quality, ceminidfs, ceminiparlays]
keywords: [k288, dfs-eval, false-negative, fanduel, devig, odds-scraper, ceminidfs, ceminiparlays, recap-tool-gaps]
related:
  - concepts/k285-eval-wave.md
  - concepts/k288-arxiv-wave.md
  - concepts/k288-feeds-wave.md
  - concepts/active-project-research-routing.md
  - sources/eval-dfs-betting-repositories-2026-10-10.md
  - concepts/k287-eval-wave.md
maturity: draft
created: 2026-10-10
updated: 2026-10-25
harness_verb: FILE
wire_status: policy_wired
---

## Relations

- @concepts/k287-eval-wave.md
- @concepts/k288-arxiv-wave.md
- @concepts/k288-feeds-wave.md
- @concepts/active-project-research-routing.md
- @sources/eval-dfs-betting-repositories-2026-10-10.md

## Raw Concept

K288 eval hub. **One eval docx, 20 URLs.** Dual-ID **OSINT K288**. Theme: NFL DFS lineup optimization, sportsbook odds scraping, parlay EV modelling.

## Narrative

### The docx says 20/20 dead. Phase-0 says 19/19 live.

The docx marks **every row UNAVAILABLE** — "returns an HTTP 404" — and concludes "all 20 evaluated candidates failed reachability verification."

**`gh api` against every GitHub row returned repo metadata. There is no 404.** The verdict is a **mass false negative**.

This is worse than a miss. Several repos were pushed **weeks before** the docx ran (Sep 20, Sep 23, Sep 27), so they cannot have been "not yet created". **The eval's reachability layer is broken.**

### The tell: a confabulated works-cited

To synthesise sources for URLs it could not fetch, the docx matched **username substrings** to unrelated web pages: `Authentic-66/FanDuel-DFS-Model` → "VANS Kids Sk8 Authentic 66 Sweatshirt" and a Trish Stratus figurine; `atlantahouseplants/MLBDFSLineupOptimizer` → an Atlanta plant shop; `dburch19142/NFL_Fanduel` → an accounting-firm succession notice. **The citations are generated filler.**

### The eval-quality arc across waves

| Wave | Signal |
|------|--------|
| K281 | 7 of 20 URLs dead |
| K282 | 6 of 20 dead |
| K283 | 34 of 40 rows `NOT FOUND` metadata |
| K284 | 0 dead; one **false negative** (`ts-rust` rated 404, alive) |
| K285 | 0 dead |
| **K288** | **20 of 20 rated 404 — all live.** |

The failure mode **flipped**: from dead links in the list, to **live links declared dead**. A reachability layer that reports 100% failure is itself the finding.

### What the repos are

NFL DFS lineup optimizers (LP/PuLP), FanDuel odds scrapers, a **devig machine**, an odds search tool, a VIP console, an NHL anytime-goal comparison, an MLB DFS optimizer, a props board, a pace/totals model, a bonus-hedge tool. Squarely **CeminiDFS** and **CeminiParlays** territory.

**Operator guidance (2026-10-10): for DFS and parlay evaluations, licence weight is lowered.** Judge on fit and technique. Only `louaih/bonus-hedge` carries a licence (MIT).

### The recap zips (operational, not sources)

Two week-4 recap packs arrived with the docx: `dfsrecapweek4.zip` and `week4parlaysrecap.zip`. Both are **desk output**, not research — a recap, scores/ledger CSVs, and a `tool-gaps.md` of structured findings. **`do_not_auto_apply=true` on every row.** They route as **briefs** to the DFS and Parlays workspaces, not as wiki source pages.

### Boundary

**Zero clones. No install.** **Never scrape sportsbook boards; never auto-submit a ticket.** A human types every line.

### Distribution

- `../CeminiDFS/briefs/2026-10-10_k288-dfs-repositories.md`
- `../CeminiParlays/briefs/2026-10-10_k288-parlays-repositories.md`
- Recap tool-gaps → the same two workspaces.
