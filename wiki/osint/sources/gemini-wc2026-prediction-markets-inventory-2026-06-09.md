---
title: "Gemini DR — WC 2026 prediction markets exhaustive inventory + cross-venue architecture"
type: source
tags: [source, gemini-deep-research, world-cup-2026, polymarket, kalshi, cross-venue, market-map, k109]
keywords: [group_advance_r32, semantic-blocklist, resolution_class, gamma-api, kalshi-elections-api, machine-readable-json]
related:
  - sources/gemini-wc2026-cross-venue-scanner-research-2026-06-05.md
  - sources/gemini-wc2026-market-probability-gaps-2026-06-05.md
  - sources/gemini-wc2026-knockout-market-map-2026-06-05.md
  - sources/gemini-wc2026-market-gap-live-verification-2026-05-29.md
  - sources/trading-posts-compilation-8-2026-06-09.md
  - concepts/cross-venue-arbitrage-pattern.md
  - concepts/world-cup-advance-market-bot-v1.md
  - concepts/world-cup-tournament-phases-lp-strategy.md
  - entities/tools/world-cup-bot.md
  - entities/platforms/polymarket.md
  - entities/platforms/kalshi.md
maturity: validated
read_status: deep-read
created: 2026-06-09
updated: 2026-06-09
---

## Relations

- @sources/gemini-wc2026-cross-venue-scanner-research-2026-06-05.md — K99 semantic + fee layer; **K109 supersedes inventory depth**
- @sources/trading-posts-compilation-8-2026-06-09.md — K108 retail hygiene overlay
- @concepts/cross-venue-arbitrage-pattern.md — WC vertical semantic blocklist
- @entities/tools/world-cup-bot.md — `config/cross_venue.yaml`, Gamma/Kalshi polling

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | 2026 FIFA Men's World Cup Prediction Markets: Exhaustive Inventory and Cross-Venue Arbitrage Architecture |
| **Author** | Gemini Deep Research |
| **Type** | docx |
| **sha256** | `ee93a59a209422e2` (full: `ee93a59a209422e2…` from preingest) |
| **Location** | `cemini-librarian:/opt/cemini-bulk/research/2026-fifa-world-cup-prediction-markets-2026-06-09.docx` |
| **Retrieved** | 2026-06-09 |
| **Data pull** | 2026-06-09 17:21 UTC |
| **Read status** | deep-read |

## Narrative

Pre-kickoff **machine-readable catalog** of PM (~392+ base markets) and Kalshi (~440+ base markets) for FIFA 2026. Standardizes `resolution_class` tags for world-cup-bot routing. Supersedes partial ticker maps from K83/K99 with full 48-team enumeration matrices and explicit **semantic blocklist** (`REJ_01`–`REJ_04`).

### Scale anchors [CONFIRMED — FIFA 2026 format]

- 48 teams, 12 groups, **104 matches**
- Group stage: 2026-06-11 → 2026-06-27
- Knockout: R32 (Jun 28–Jul 3) → R16 → QF → SF → Final (Jul 19)
- **32 teams** advance from groups (24 top-two + **8 best third-place**)

### Market counts (indexed live 2026-06-09)

| Platform | Class | Count |
|----------|-------|-------|
| Polymarket | `group_advance_r32` | 48 |
| Polymarket | `reach_r16` / `qf` / `sf` / `final` | 48 each (192 total) |
| Polymarket | `outright_winner` | 49 |
| Polymarket | `group_winner` | 48 (12×4) |
| Polymarket | `stage_of_elimination` | ~5–6 teams live; ~42 TBD |
| Kalshi | `KXWCGROUPQUAL` | 48 |
| Kalshi | `KXWCROUND` (RO16/QUAR/SEMI/FINAL) | ~192 |
| Kalshi | `KXWCGAME` (90-min 1x2) | 104 fixtures scaling |
| Kalshi | macro props (`KXWCHOSTKO`, `KXWCREGIONKO`, `KXWCGROUPWINELIM`) | no PM equivalent |

### Top semantic traps (hardcode in scanner suppression)

1. **Advance ≠ R16** — PM `group_advance_r32` ↔ Kalshi `KXWCROUND-26RO16` is **REJ_01** (100% hedge break if team dies in R32).
2. **Third-place math** — `group_winner` ≠ `group_qualify`; bottom finisher ≠ inverse of advance (`REJ_03`, third-place asymmetry).
3. **Kalshi SF loser grading** — `KXWCSTAGEOFELIM-SEMI` Yes includes semifinal losers regardless of third-place playoff.
4. **90-min vs To Advance** — Kalshi `KXWCGAME` is regulation 1x2; PM match slugs often omit suffix (`REJ_04`).
5. **Group bottom trap** — `KXWCGROUPBOTTOM` No does not imply `group_advance_r32` Yes (3rd can miss best-eight-thirds).

### Verified pairable (rules_hash)

| PM | Kalshi | Hash |
|----|--------|------|
| `world-cup-winner` | `KXMENWORLDCUP` | MATCH_01 |
| `world-cup-group-[x]-winner` | `KXWCGROUPWIN-26[X]` | MATCH_02 |
| `world-cup-team-to-advance…` | `KXWCGROUPQUAL-26[X]` | MATCH_03 |
| `reach-quarterfinals` | `KXWCROUND-26QUAR` | MATCH_04 |

### June 27 zero-day

Final group day: third-place qualification reprices cross-dependent until Group L final whistle — advance markets stay open; bots need live fixture state (points, GD, fair-play) not static mids.

### Fee-adjusted arb [CONFIRMED methodology]

Kalshi ~7% on **net profit** widens threshold; naive `p < k` without fee drag yields negative EV on favorites. Scanner must use fee-adjusted pp (see K99 formula).

### Machine-readable appendix

Full JSON in source docx §10 — `polymarket_events`, `cross_venue_pairs`, regex for PM match rules parsing, `pulled_at_utc`. **Prod action:** vendor subset into `world-cup-bot/config/wc_market_registry.json` (see prod brief).

### LP routing note

PM Sports LP rewards apply to advance / reach-milestone series; **group_winner** child events marked **No** LP in catalog — do not route Module 1 quoter to those slugs.

## Snippets

> "Polymarket's group_advance_r32 cannot be hedged against Kalshi's KXWCROUND-26RO16. A failure here results in a 100% loss of hedge if a team is eliminated in the R32." [Source: 2026 FIFA World Cup Prediction Markets.docx §1]

> "Algorithms must hard-reject these assumed matches at the routing layer. Failure to implement this suppression list will result in immediate capital loss." [Source: 2026 FIFA World Cup Prediction Markets.docx §7]

> "Never map a Kalshi KXWCGAME contract to a Polymarket match contract during the knockout stages without explicitly executing regex on the Polymarket description for ET/Penalty disclaimers." [Source: 2026 FIFA World Cup Prediction Markets.docx §8]
