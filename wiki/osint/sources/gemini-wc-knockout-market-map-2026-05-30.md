---
title: "Gemini DR — WC 2026 knockout-round market map (Polymarket + Kalshi)"
type: source
tags: [source, gemini-deep-research, world-cup-2026, polymarket, kalshi, knockout, market-phases, k85]
keywords: [round-of-32, reach-final, stage-of-elimination, match-moneyline, to-advance, resolution-class, market-phases]
related:
  - sources/gemini-world-cup-market-structure-research-2026-05-29.md
  - sources/gemini-wc2026-cross-venue-arbitrage-dynamics-2026-05-29.md
  - sources/gemini-wc-inplay-pregame-lp-risks-2026-05-30.md
  - sources/gemini-wc-tournament-phase-router-2026-05-30.md
  - concepts/world-cup-tournament-phases-lp-strategy.md
  - concepts/world-cup-advance-market-bot-v1.md
  - concepts/polymarket-sports-lp-operating-rules.md
  - concepts/cross-venue-arbitrage-pattern.md
  - entities/tools/world-cup-bot.md
  - entities/platforms/polymarket.md
  - entities/platforms/kalshi.md
maturity: validated
created: 2026-05-30
updated: 2026-05-30
---

## Relations

- @sources/gemini-world-cup-market-structure-research-2026-05-29.md — K82 group-stage contract map; this report extends through final
- @sources/gemini-wc-inplay-pregame-lp-risks-2026-05-30.md — companion on in-play / pregame gates (DR 09)
- @concepts/world-cup-tournament-phases-lp-strategy.md — primary synthesis consumer
- @entities/tools/world-cup-bot.md — feeds `config/market_phases.yaml`

## Raw Concept

| Field | Value |
|-------|-------|
| Title | World Cup 2026 Knockout-Round Market Map and Automated Trading Infrastructure |
| Author | Gemini Deep Research (prompt 08-knockout-market-map) |
| Type | docx synthesis report |
| Location | `cemini-librarian:/opt/cemini-bulk/research/WC 2026 Knockout Market Mapping.docx` |
| Retrieved | 2026-05-30 |
| Read status | deep-read |

## Narrative

Gemini DR mapping **group → final** market inventory for Polymarket + Kalshi under the **48-team / 104-match** 2026 format. Primary bot upgrade path: extend Module 1 scanner beyond single `advance to knockout` regex via `config/market_phases.yaml` + phase router (**DR 10 ingested 2026-05-30**).

### v2 LP priority sequence [TENTATIVE — single Gemini source]

1. **Group advance** (`advance to knockout` = **Reach Round of 32** in 48-team format) — keep v1 core
2. **Knockout milestone** (`Reach Round of 16`, `Reach QF`, `Reach SF`, `Reach Final`) — long-duration LP post-group
3. **Match-level** — high velocity; bifurcate **90-min moneyline** vs **To Advance** (includes ET/pens)
4. **Outright winner / Golden Boot** — map for pricing anchors; **not LP targets** (capital lockup, immediate No on elimination)

### FIFA 2026 phase calendar [CONFIRMED dates via report citations]

| Phase | Window | Bot note |
|-------|--------|----------|
| Group stage | 2026-06-11 → 2026-06-27 (72 fixtures) | Advance markets resolve iteratively on mathematical elimination |
| **Zero-day transition** | **2026-06-27** (final Group L) | All remaining advance markets + R32 listings surge; bracket permutations pre-compute |
| Round of 32 | 2026-06-28 → 2026-07-03 | `Reach R16` ≈ match **To Advance** (1:1 parity) |
| Round of 16 | 2026-07-04 → 2026-07-07 | Deprecate R32 regex; prioritize QF reach patterns |
| Quarterfinals | 2026-07-09 → 2026-07-11 | 48h rest → **safest KO LP window** (stable pre-kickoff) |
| Semifinals | 2026-07-14 → 2026-07-15 | Peak match liquidity; `Reach Final` merges with SF To Advance |
| Third place + Final | 2026-07-18 → 2026-07-19 | MetLife final |

Milestone markets (`Reach QF/SF/Final`) may **list before teams are known** — scanner must track from tournament open and scale min size by temporal proximity.

### Resolution classes (critical parser split)

| Class | Settles on | LP risk |
|-------|------------|---------|
| **90-min moneyline (3-way)** | Regulation + stoppage only; **Draw** if tied at whistle | Extreme near 85′ in tied games — must **hard-halt at 90′** |
| **To Advance / To Qualify** | Full tie incl. ET + pens | Different delta profile; do not mix with 90-min scanner |
| **Reach milestone** | Team eliminated before stage → No | Immediate resolution on KO exit |
| **WC winner** | Immediate No on any KO elimination | Not LP-safe |

**Postponement:** Kalshi/regulated path — resume within 48h keeps market live; else last fair price. PM optimistic-oracle path can lock capital in disputes — bot must pull on `Delayed`/`Suspended`/`Abandoned` fixture state.

### Kalshi cross-venue map [TENTATIVE tickers from report]

| Kalshi series | PM equivalent | Logic |
|---------------|---------------|-------|
| `KXWCGAME` / `kxwcgame-*` | Match fixtures | Date+team coded strings |
| `KXWCSTAGEOFELIM` / `kxwcstageofelim-*` | `Reach {stage}` markets | **Inverse:** "eliminated IN R16" Yes ↔ "Reach QF" No |
| `KXWCGROUPWINNER` | Group winner | Existing Module 6 scope |
| `KXMENWORLDcup` | WC winner | Alert / macro hedge only |

### LP reward mechanics (knockout scaling)

- Rewards anchor on **Adjusted Midpoint** with **quadratic** spread penalty — wide quotes harvest little yield
- **`rewardsMinSize`** / min incentive threshold is **per-market dynamic** — semifinal floors >> group stage
- Bot must poll reward endpoints continuously; min size also anti-sybil against dust orders

### Implementation estimate

Report appendix JSON was **corrupted** (empty `market_phases` array) — prose recommends **~4 engineer-days** for scanner + phase config beyond v1. Hand-built YAML in `config/market_phases.yaml`; DR 10 router spec adds **~12d** FSM + ledger scope.

## Snippets

> "Advance to Knockout" is synonymous with "Reach Round of 32" in the 2026 format. [Source: WC 2026 Knockout Market Mapping.docx]

> A 3-way moneyline tied at 90′ resolves Draw even if a team wins in extra time; To Advance markets include ET and penalties. [Source: WC 2026 Knockout Market Mapping.docx]

> Kalshi Stage of Elimination resolves affirmatively if the team is **defeated in** that round — invert when pairing to PM Reach markets. [Source: WC 2026 Knockout Market Mapping.docx]

> Critical vulnerability: zero-day transition 2026-06-27 when third-place math finalizes and R32 markets open simultaneously. [Source: WC 2026 Knockout Market Mapping.docx]
