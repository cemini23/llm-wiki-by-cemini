---
title: "Gemini DR — WC 2026 in-play, pregame, and injury-driven LP risks"
type: source
read_status: read
tags: [source, gemini-deep-research, world-cup-2026, polymarket, lp, in-play, pregame, lineup, k85]
keywords: [courtsiding, lineup-leak, cancel-window, ghost-quote, queue-depletion, hard-halt, cross-market-contagion]
related:
  - sources/gemini-sports-prediction-bot-pitfalls-2026-05-29.md
  - sources/gemini-polymarket-lp-rewards-world-cup-2026-05-29.md
  - sources/gemini-world-cup-market-structure-research-2026-05-29.md
  - sources/gemini-wc-knockout-market-map-2026-05-30.md
  - sources/gemini-wc-tournament-phase-router-2026-05-30.md
  - concepts/world-cup-advance-market-bot-v1.md
  - concepts/polymarket-sports-lp-operating-rules.md
  - concepts/world-cup-tournament-phases-lp-strategy.md
  - concepts/production-trading-blind-spots.md
  - entities/tools/world-cup-bot.md
  - sources/rohonchain-fifa-wc-shock-recovery-strategy-2026-06-02.md
  - concepts/polymarket-football-shock-recovery-trading.md
  - projects/world-cup-bot/Architecture/Architecture - match_shock_v1.md
maturity: validated
created: 2026-05-30
updated: 2026-06-02
---

## Relations

- @sources/gemini-sports-prediction-bot-pitfalls-2026-05-29.md — baseline failure modes; this report operationalizes gates
- @concepts/polymarket-sports-lp-operating-rules.md — cancel-window + fill-handler updates land here
- @concepts/world-cup-tournament-phases-lp-strategy.md — phase-specific cancel policy
- @entities/tools/world-cup-bot.md — v1 `no_in_play_quotes` policy

## Raw Concept

| Field | Value |
|-------|-------|
| Title | World Cup 2026 Prediction Market Liquidity: Pregame, In-Play, and Injury-Driven Microstructure Risks |
| Author | Gemini Deep Research (prompt 09-inplay-pregame-lp-risks) |
| Type | docx synthesis report |
| Location | `cemini-librarian:/opt/cemini-bulk/research/World Cup Bot Risk Research.docx` |
| Retrieved | 2026-05-30 |
| Read status | deep-read |

## Narrative

Defines **v1 defensive gates** and **v2 roadmap** for a WC LP bot that must never quote in-play. Core thesis: PM order books reprice roster/news **5–60 minutes** slower than centralized books → resting limits get picked off unless bot pulls early.

### Pregame (T-24h → T-10h)

| Trigger | Typical PP move | v1 gate | v2 gate |
|---------|-----------------|---------|---------|
| Confirmed XI / presser injury | ~5pp+ | **Full skip** at scheduled lineup drop; T-10h hard cancel | Webhook book-pull + 5–60m observe before re-quote |
| Unverified lineup leak (Twitter) | ~3pp drift | **human_review**; stop queue replenish | NLP on trusted accounts (@BenCrellin tier) → instant pull |
| Queue depletion anomaly | n/a | Treat as adverse selection — pull, don't replenish | 3σ vs MES velocity monitor |

Safe yield window: **T-24h to T-10h** with stable mids. Final hours = information asymmetry zone.

### In-play — v1 **hard_halt**

- Goal propagation: stadium/Opta APIs **1–3s** vs consumer TV **45–60s** → "courtsiding" / stadium API arbitrage [TENTATIVE industry estimates in report]
- **Cross-market contagion (48-team):** live goal in Group A shifts third-place math → instant repricing on unrelated Group F `To Advance` markets while bot quotes stale mids
- PM keeps advance/knockout markets **open during live group matches** [TENTATIVE — verify per market at launch]
- **Never chase live LP rewards** ($3k live spread pool per PM US docs cited) — EV negative without sub-10ms infra

### Knockout-specific

| Risk | Mitigation |
|------|------------|
| 90-min vs To Advance confusion | Schema tag `resolution_class`; halt 90-min at regulation whistle |
| **Ghost quote window** post-whistle | Cancel all team futures **≥5 min before** expected match end |
| 48–72h turnarounds | Extend cancel window to **24h** pre-kickoff for all KO fixtures |
| ET/pens | 90-min book settled; advancement derivatives continue |

### Cancel-window policy (recommended overrides)

| Tournament phase | Cancel before kickoff | Notes |
|------------------|----------------------|-------|
| Friendlies / early group | **10h** (v1 default) | Current bot config |
| Final group (concurrent MD3) | **12h** | Peak third-place contagion |
| Knockout R32 → Final | **24h** | Post-match injury/fatigue news window |
| Prefer quote window | **≥24h** | Unchanged |

`operating_yaml_patch` from report (v2 — **not yet in prod operating.yaml**):

```yaml
calendar:
  prefer_hours_before_kickoff: 24
  cancel_hours_knockout: 24
  cancel_hours_final_group: 12
```

### v2 feature roadmap (ranked)

1. Live-score API auto-halt (Opta / Stats Perform — FIFA official feed; ~$10k/yr tier cited)
2. Phase-aware calendar (10h / 12h / 24h by phase)
3. Cross-market 48-team advancement probability matrix
4. Twitter webhook + NLP for lineup leaks
5. Queue depletion velocity monitor

### Reward tier discipline

- Target **Early** + **Day-of** tiers only ($150–600 spread pools cited)
- Abandon order book before **Live** period despite highest incentives

## Snippets

> "The T-10h cancel window serves as a crude but highly effective blunt instrument to ensure the bot is completely flat before the chaotic pre-match news cycle begins." [Source: World Cup Bot Risk Research.docx]

> v1 policy: `no_in_play_quotes` — hard halt the moment fixture state → Live. [Source: World Cup Bot Risk Research.docx]

> Ghost quote window: resting bids on eliminated teams filled in seconds before oracle resolution. [Source: World Cup Bot Risk Research.docx]

> Final group concurrent matches: extend cancel to 12h; knockout rounds: 24h. [Source: World Cup Bot Risk Research.docx]
