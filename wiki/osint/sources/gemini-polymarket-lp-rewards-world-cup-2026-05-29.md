---
title: "Gemini DR — Polymarket LP rewards analysis (FIFA World Cup advance markets)"
type: source
read_status: read
tags: [source, gemini-deep-research, polymarket, lp-rewards, world-cup-2026, market-making, k82]
keywords: [liquidity-rewards, quadratic-spread, adjusted-midpoint, capital-tiers, adverse-selection, pre-match-cancel]
related:
  - sources/gemini-world-cup-market-structure-research-2026-05-29.md
  - sources/gemini-sports-prediction-bot-pitfalls-2026-05-29.md
  - sources/world-cup-youtube-research-compilation-2026-05-29.md
  - concepts/polymarket-lp-rewards-farming.md
  - concepts/polymarket-sports-lp-operating-rules.md
  - concepts/world-cup-advance-market-bot-v1.md
  - concepts/polymarket-lp-bot-phase0-spec.md
  - sources/gemini-wc-lp-team-safety-assessments-2026-05-30.md
  - sources/gemini-wc-inplay-pregame-lp-risks-2026-05-30.md
maturity: validated
created: 2026-05-29
updated: 2026-05-29
---

## Relations

- @concepts/polymarket-lp-rewards-farming.md — parent strategy page; this report sports/WC quant layer
- @concepts/polymarket-sports-lp-operating-rules.md — operational rules distilled from this + YouTube batch 4
- @concepts/world-cup-advance-market-bot-v1.md — implementation spec

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Polymarket LP Rewards Analysis: World Cup |
| Author | Gemini Deep Research |
| Type | docx |
| Location | `cemini-librarian:/opt/cemini-bulk/research/Polymarket LP Rewards Analysis_ World Cup.docx` |
| Retrieved | 2026-05-29 |
| Read status | deep-read |

## Narrative

Quantitative decomposition of Polymarket **liquidity reward economics** applied to **"Team to advance to Knockout Stages"** markets during the April 2026 **$5M+ sports incentive** epoch.

### Scoring mechanics (CLOB)

- **Quadratic spread function:** reward ∝ `((max_spread − distance) / max_spread)² × size` — marginal collapse away from midpoint.
- **Adjusted midpoint:** ignores sub-minimum "dust" orders — anti-manipulation.
- **Bilateral requirement:** single-sided quotes penalized ~⅓ in neutral band; **mandatory two-sided** near price extremes (>~90¢).
- **Time sampling:** ~10,080 snapshots/week — rewards integrate time at risk.

### Adverse selection

- **Pre-match equilibrium:** ~0.35%/day friction estimate when disciplined.
- **Live match window:** >25% capital at risk if quotes left up — **mandatory full pull 6–10h pre-kickoff**.
- **K56 Drake benchmark:** $50→$18 in 48h on continuous culture market — sports has definable "whistle"; culture markets do not.

### Capital tier model (median $450/day pool, $15k competing depth)

| Tier | Gross daily reward (model) | Net daily (after est. adverse) | Notes |
|------|---------------------------|--------------------------------|-------|
| $500 | ~$5–8 | ~$3 | Min-share + single-sided trap |
| **$2,000** | ~$53 | **~$46** | **Sweet spot** |
| $5,000 | ~$113 | ~$95 | Diminishing efficiency |
| $10,000 | ~$180 | ~$145 | Concentration / news-scrape risk |

### WC-specific topography

- Daily boosted pool **$300–600 per team** advance market [TENTATIVE — aligns K56 Neymar FIFA example + Gemini].
- 48-team third-place rule **flattens tail risk** for favorites early; mid-tier volatility remains in **20–40¢** band.
- Competing depth ~$12–20k on tier-2 nation advance markets in report assumptions.

### Engineering implications

- Gamma API for reward pool + CLOB for depth/competition measurement before deploy.
- Sub-100ms cancel/replace for institutional tiers; **manual+scheduled cancel sufficient** at $2K WC v1.
- Do not size on reward alone — **break-even adverse move** is the binding constraint.

## Snippets

> "The success of a liquidity deployment relies entirely on mastering the platform's proprietary quadratic reward scoring algorithm, minimizing the devastating costs of adverse selection." [Source: Polymarket LP Rewards Analysis_ World Cup.docx]

> "A $2,000 to $3,000 capital deployment represents the absolute optimal sweet spot for manual or semi-automated liquidity farming." [Source: Polymarket LP Rewards Analysis_ World Cup.docx]
