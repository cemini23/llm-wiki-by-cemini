---
title: "Gemini DR — Cross-venue market scanner research (WC 2026)"
type: source
tags: [source, gemini-deep-research, world-cup-2026, cross-venue, polymarket, kalshi, module-6, k99]
keywords: [fee-adjusted-edge, semantic-trap, round-of-32, group-qualify, oracle-risk, 48-team-format]
related:
  - sources/gemini-wc2026-market-probability-gaps-2026-06-05.md
  - sources/gemini-wc2026-knockout-market-map-2026-06-05.md
  - sources/gemini-wc2026-cross-venue-arbitrage-dynamics-2026-05-29.md
  - sources/gemini-wc2026-market-gap-live-verification-2026-05-29.md
  - concepts/cross-venue-arbitrage-pattern.md
  - concepts/world-cup-advance-market-bot-v1.md
  - entities/tools/world-cup-bot.md
  - sources/gemini-wc2026-prediction-markets-inventory-2026-06-09.md
maturity: validated
created: 2026-06-05
updated: 2026-06-09
---

## Relations

- @sources/gemini-wc2026-market-probability-gaps-2026-06-05.md — fade-watch pair table + YAML seed (K99)
- @sources/gemini-wc2026-knockout-market-map-2026-06-05.md — post–group-stage scanner expansion
- @concepts/cross-venue-arbitrage-pattern.md — Module 6 reference loop; K99 fee + semantic updates
- @entities/tools/world-cup-bot.md — `config/cross_venue.yaml`, fee-adjusted alert gate

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Cross-Venue Market Scanner Research |
| Author | Gemini Deep Research |
| Type | docx |
| Location | `cemini-librarian:/opt/cemini-bulk/research/gemini-wc2026-cross-venue-scanner-research-2026-06-05.docx` |
| Retrieved | 2026-06-05 |
| Read status | deep-read |

## Narrative

Quantitative synthesis for **Module 6** (PM↔Kalshi alert/exec). Extends K83 with 48-team semantics, fee EV math, oracle mismatch, and fade-watch cohort (USA, Mexico, England, Croatia, Switzerland).

### Headline findings [CONFIRMED]

1. **Advance ≠ Round of 16 (2026)** — Group escape → **Round of 32**; pairing PM advance with `KXWCROUND-26RO16` is a catastrophic semantic mismatch (double-digit false arb).
2. **Fee-adjusted edge** — Kalshi ~7% on **net profit** erodes raw gaps on favorites; USA **4.0pp raw → -2.02pp** fee-adjusted (Jun 5 snapshot).
3. **Oracle latency** — Kalshi ESPN/FIFA centralized settle (~5–9 min) vs Polymarket UMA disputes can trap capital on one leg.
4. **Home-nation bias** — Kalshi US retail inflates USMNT/MEX vs global PM liquidity (USA largest dislocation, still sub-5pp raw alert).
5. **Alert-only posture** — No auto-hedge recommendation; human depth review mandatory.

### Fee model (scanner)

For PM yes at `p` and Kalshi yes at `k` with `p < k` (buy PM yes + Kalshi no):

- Raw gap pp = `(k - p) × 100`
- Conservative fee drag pp ≈ `(fee_pct / 100) × k × 100`
- Fee-adjusted pp = raw gap pp − fee drag pp

### Semantic allow-list

| Pairable | Block |
|----------|-------|
| PM R32 / group advance ↔ `KXWCGROUPQUAL` | PM advance ↔ `KXWCROUND-26RO16` |
| Group winner ↔ `KXWCGROUPWIN` | Stub 50¢ PM slugs without FIFA suffix |

## Snippets

> "If an automated scanner maps a Polymarket Group Advancement contract to a Kalshi Round of 16 contract, it will systematically misidentify these semantic mismatches as massive, double-digit arbitrage opportunities." [Source: Cross-Venue Market Scanner Research.docx]

> "The 4.0 pp gap entirely fails to survive the fee model, meaning the scanner will correctly log the data but suppress the alert." [Source: World Cup 2026 Market Probability Gaps.docx — cited in scanner report]
