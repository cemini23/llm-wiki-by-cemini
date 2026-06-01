---
title: "Gemini DR — WC conviction configuration audit (43 teams)"
type: source
tags: [source, gemini-deep-research, world-cup-2026, conviction, lp-safety, polymarket, k91]
keywords: [conviction-yaml, stale-config, fade-watch, cancel-window, injury-delta, toxic-flow]
related:
  - sources/gemini-wc-lp-team-safety-assessments-2026-05-30.md
  - concepts/world-cup-2026-group-conviction-matrix.md
  - concepts/world-cup-advance-market-bot-v1.md
  - entities/tools/world-cup-bot.md
  - meta/wc-lp-safety-cadence.md
maturity: draft
read_status: deep-read
created: 2026-05-31
updated: 2026-05-31
---

## Relations

- @sources/gemini-wc-lp-team-safety-assessments-2026-05-30.md — companion LP safety lens; this source expands to full 43-team configuration pass
- @concepts/world-cup-2026-group-conviction-matrix.md — matrix update input for tier/cap adjustments
- @entities/tools/world-cup-bot.md — conviction mode hierarchy and pre-kickoff risk posture consumer
- @meta/wc-lp-safety-cadence.md — cadence anchor for next re-check before further promotion

## Raw Concept

| Field | Value |
|-------|-------|
| Title | 2026 World Cup Polymarket LP bot — comprehensive conviction configuration audit |
| Author | Gemini Deep Research |
| Type | docx synthesis report |
| Location | `cemini-librarian:/opt/cemini-bulk/research/World Cup Bot Conviction Audit.docx` |
| Retrieved | 2026-05-31 |
| Read status | deep-read |

## Narrative

This report audits conviction tiers and risk posture across 43 teams with a focus on stale assumptions under late pre-tournament injury and roster volatility. It argues for stricter use of `fade_watch` in high-information-asymmetry windows and explicit precedence of restrictive modes over capital-deploying modes when conflicts occur.

### Key findings

| Category | Result |
|----------|--------|
| Scope | 43 teams reviewed |
| Critical stale configs | 5 flagged |
| Urgent tier changes | 4 recommended (`Canada`, `Japan`, `Scotland`, `Brazil` → `fade_watch`) |
| Temporal risk | 13 teams inside near-kickoff cancel window snapshot |

### Operating implications

- Treat stale injury/roster deltas as immediate tier-risk inputs, not advisory context.
- Enforce mode precedence: `fade_watch` overrides `bilateral_only` when both signals appear.
- Keep `skip` on geopolitical/entry-risk teams even when football-only probabilities appear attractive.
- Re-run safety review at the next scheduled cadence before restoring aggressive YES-side exposure.

### Confidence and handling

This is a single-source DR synthesis and should be applied as a risk-control input, not as a standalone pricing oracle. Use runtime market data and additional confirmations before promoting any downgraded team back into active quoting.

## Snippets

> In volatile pre-kickoff windows, restrictive alert-only modes should override active bilateral deployment to avoid one-sided toxic flow. [Source: World Cup Bot Conviction Audit.docx]

> Teams with material injury or squad-news deltas should be downgraded immediately when current conviction tiers are stale. [Source: World Cup Bot Conviction Audit.docx]
