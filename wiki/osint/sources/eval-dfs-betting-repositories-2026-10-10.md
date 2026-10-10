---
title: "DFS & betting repositories evaluation — 20 rows, docx says 20/20 dead, Phase-0 finds 19/19 live (2026-10-10)"
type: source
tags: [source, k288, eval, dfs, parlays, fanduel, odds, eval-quality]
keywords: [k288, dfs-optimizer, fanduel, devig, odds-scraper, prop-board, false-negative, eval-quality, ceminidfs, ceminiparlays]
related:
  - concepts/k288-eval-wave.md
  - concepts/active-project-research-routing.md
  - concepts/agent-toolkit-routing-research-backlog.md
maturity: draft
created: 2026-10-10
updated: 2026-10-10
read_status: read
---

## Relations

- @concepts/k288-eval-wave.md
- @concepts/active-project-research-routing.md
- @concepts/agent-toolkit-routing-research-backlog.md

## Raw Concept

| File | `Evaluating DFS and Betting Repositories.docx` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/Evaluating DFS and Betting Repositories.docx` |
| Retrieved | 2026-10-10 |
| Dual-ID | **OSINT K288** |
| Batch theme | NFL daily-fantasy lineup optimization, sportsbook odds scraping, parlay expected-value modeling |
| Rows | 20 URLs |
| sha256 | `6a17333b066d8b7c…` |

## Narrative

### The docx verdict: 20 of 20 UNAVAILABLE

Every row is marked **UNAVAILABLE** with "returns an HTTP 404". The aggregate reads **0 Integrate · 0 Extract · 0 Watch · 0 Context · 0 Pass · 20 UNAVAILABLE** and concludes "all 20 evaluated candidates failed reachability verification."

### Phase-0 (2026-10-10): the verdict is a mass false negative

`gh api` was run against every GitHub row. **All 19 GitHub repos exist and returned repo metadata.** There is **no 404.** The docx is wrong on every row.

| Repo | Stars | License | Last push |
|------|-------|---------|-----------|
| `nickdemarinis7/dfs-optimizer` | 0 | none | 2026-10-10 |
| `mehpackers13/fanduel-bot` | 0 | none | 2026-10-10 |
| `matthewmehl14-glitch/fanduel-devig-machine` | 1 | none | 2026-10-10 |
| `SuhasK14/Odds-Search` | 0 | none | 2026-10-10 |
| `kel-reid/DFS-Optimizer` | 0 | none | 2026-10-10 |
| `dave-mio1905w9/fanduel-odds-scraper` | 0 | none | 2026-10-10 |
| `nsierchio/fanduel-vip-console` | 1 | none | 2026-10-09 |
| `nexona-dev/NFL-DFS-Simulator` | 0 | none | 2026-10-07 |
| `dburch19142/NFL_Fanduel` | 0 | none | 2026-10-08 |
| `carlie4real-beans/fanduel-optimizer` | 0 | none | 2026-10-06 |
| `ChungChainz/nhl-anytime-goal-comparison` | 0 | none | 2026-10-06 |
| `Authentic-66/FanDuel-DFS-Model` | 0 | none | 2026-10-10 |
| `kenepp1031/nfl-prop-board` | 0 | none | 2026-10-04 |
| `atlantahouseplants/MLBDFSLineupOptimizer` | 0 | none | 2026-09-30 |
| `louaih/bonus-hedge` | 2 | **MIT** | 2026-09-29 |
| `johnson-shuffle/fantasy` | 0 | none | 2026-09-27 |
| `kycoonyatFD/nfl-assets-dashboard` | 0 | none | 2026-09-23 |
| `everworldlife-netizen/fanduel-pace-totals` | 0 | none | 2026-09-20 |
| `jdangeldoc/hidden-edge-fanduel` | 0 | none | 2026-09-27 |

(`afflucky/dfs-optimizer-pro`, a Hugging Face Space, was not re-checked.)

Several were pushed **weeks before** the docx ran — `kycoonyatFD/nfl-assets-dashboard` (Sep 23), `everworldlife-netizen/fanduel-pace-totals` (Sep 20), `jdangeldoc/hidden-edge-fanduel` (Sep 27). Those cannot have been "not yet created" at eval time. **The eval's reachability layer is broken.**

### The confabulated works-cited

The docx's "Works cited" section is the tell. To synthesise sources for URLs it could not fetch, it matched the **username substrings** to unrelated web pages:

- `Authentic-66/FanDuel-DFS-Model` → "VANS Kids Sk8 Authentic 66 Sweatshirt", "Trish Stratus WWE Autographed… #66".
- `atlantahouseplants/MLBDFSLineupOptimizer` → "Atlanta Houseplants — Office Plant Design, Installation & Care".
- `dburch19142/NFL_Fanduel` → an accounting-firm succession notice and a GoFundMe.

None of these relate to DFS. **The citations are generated filler. Do not trust this docx's sources.**

### What the repos actually are

Reading the names and the docx's own (unverified) stack notes: NFL DFS lineup optimizers (LP/PuLP), FanDuel odds scrapers, a **FanDuel devig machine**, an odds search tool, a VIP-bet console, an NHL anytime-goal comparison, an MLB DFS optimizer, a props board, a pace/totals model, and a bonus-hedge tool. That is squarely the **CeminiDFS** and **CeminiParlays** territory.

**Operator guidance (2026-10-10): for DFS and parlay evaluations, licence weight is lowered.** Judge these on fit and technique. Only one carries a licence at all (`louaih/bonus-hedge`, MIT).

### Boundary

**No clones.** These are evaluation leads, not installs. **Never scrape sportsbook boards; never auto-submit a ticket.** A human types every line.

### Distribution

- DFS rows → `../CeminiDFS/briefs/2026-10-10_k288-dfs-repositories.md`
- Parlays rows (devig, odds search, bonus hedge) → `../CeminiParlays/briefs/2026-10-10_k288-parlays-repositories.md`

## Snippets

> "All 20 candidate URLs returned HTTP 404 unreachable status; no licenses could be identified." [Source: Evaluating DFS and Betting Repositories.docx — **false; Phase-0 found all 19 GitHub repos live**]

> "GitHub - mehpackers13/kalshi-bot: Self-improving Kalshi prediction, https://github.com/mehpackers13/kalshi-bot" [Source: Evaluating DFS and Betting Repositories.docx — an unrelated repo cited for a `fanduel-bot` row]
