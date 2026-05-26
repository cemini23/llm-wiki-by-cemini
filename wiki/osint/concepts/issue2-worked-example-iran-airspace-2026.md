---
title: "Worked Example — Three-Formula System on Iran Airspace June-30 Polymarket Binary (Outlier Weekly Issue 2)"
type: concept
tags: [concept, polymarket, worked-example, three-formula, geopolitical-binary, outlier-weekly, issue-2, skip-discipline]
keywords: [iran-airspace-2026, three-formula-worked-example, geopolitical-tail-binary, outlier-weekly-issue2, forward-track-2026-06-30, publish-discipline-3pp]
related:
  - concepts/three-formula-system-polymarket-rare-events.md
  - concepts/issue1-worked-example-anthropic-pentagon-2026.md
  - concepts/poisson-edge-rare-events.md
  - concepts/shannon-entropy-kl-divergence-prediction-markets.md
  - concepts/taleb-fat-tails-barbell-prediction-markets.md
  - concepts/kelly-sizing-quarter.md
  - entities/platforms/polymarket.md
maturity: draft
created: 2026-05-26
updated: 2026-05-26
---

## Relations

- @concepts/three-formula-system-polymarket-rare-events.md — parent synthesis; third worked example after earthquake (canonical) and Issue 1 regulatory binary
- @concepts/issue1-worked-example-anthropic-pentagon-2026.md — prior skip-discipline case; Issue 2 tightens pre-publish re-run to ≥3pp drift
- @concepts/poisson-edge-rare-events.md — Poisson on geopolitical closure sketch (λ per week, same caveats as regulatory binaries)
- @concepts/shannon-entropy-kl-divergence-prediction-markets.md — KL remains in SKIP bucket at publish lock
- @concepts/taleb-fat-tails-barbell-prediction-markets.md — geo tail-bucket, 1.5× multiplier
- @concepts/kelly-sizing-quarter.md — quarter-Kelly + sub-0.5% actionable-minimum SKIP rule (Issue 2 operational addition)
- @entities/platforms/polymarket.md — execution venue

## Raw Concept

What this page answers: when the three-formula synthesis is applied to a **geopolitical** tail binary (Iran major airspace closure by June 30, 2026), what does it produce at evening draft vs publish-day lock, and how does overnight repricing (+2.4pp YES) collapse a marginal edge into a second consecutive forward-track **SKIP**? Issue 2 also records the newsletter readability reboot (output-first, ≤3 concepts, first person) and the public methodology updates on the forward-track sheet.

Source: wiki file-back from *Outlier Weekly*, Issue 2, published 2026-05-26 at https://outlierweekly.substack.com/p/issue-2-iran-airspace-three-formulas. Public forward-track row: https://cemini23.github.io/outlier-weekly-methodology/forward-track/.

## Narrative

### Market context

The market resolves YES if Iran initiates a **major** closure of its airspace (not solely weather-related) by **2026-06-30, 11:59 PM ET** — a broad suspension of commercial flights across Iran or a major Iranian airspace region [Source: Polymarket resolution rules, Gamma API 2026-05-26].

Issue 2 was chosen for **category breadth** (geopolitical vs Issue 1’s regulatory Anthropic–Pentagon binary) and **liquidity** (~$195k 24h volume at publish lock).

| Lock | YES price | Notes |
|------|-----------|-------|
| Evening draft (2026-05-25) | ≈ 27.25¢ | Poisson sketch implied marginal +2–3¢ YES edge |
| Publish-day lock (2026-05-26) | ≈ 29.7¢ | Poisson fair ≈ market; synthesis ≈ 0.16% → **SKIP** |

Window from Issue 2 ship to resolution: approximately **5.0 weeks**.

### Poisson sketch (geopolitical closure intensity)

Same discipline as Issue 1: Poisson is a **transparent sketch**, not a calibrated geopolitical model. Escalation weeks during Gulf conflict clusters inform λ ≈ **0.065–0.075** “closure-intensity units” per week.

```
P(≥1 qualifying closure in 5.0 wk | λ = 0.07) = 1 − exp(−0.35) ≈ 0.295  →  fair ≈ 29.5¢
```

At **29.7¢** publish lock: edge ≈ **0¢** → Poisson **SKIP** (inside 1¢ noise band).

At **27.25¢** evening draft: edge ≈ **+2–3¢** → marginal BUY_YES at candidate level only.

### Shannon / KL (publish lock)

Operator subjective YES: **38%** (escalation / partial-disruption read — disclosed sketch, not a model output).

```
KL(0.38 || 0.297) ≈ 0.023 bits  →  SKIP bucket (< 0.05)
```

### Taleb

**Tail-bucket** classification (headline re-pricing risk). Multiplier **1.5×** on Poisson arm — cannot create edge when Poisson and KL are quiet.

### Synthesis (publish lock)

```
weighted_fraction ≈ 0.40 · 0.00075 + 0.35 · 0 + 0.25 · 1.5 · 0.00075
                  ≈ 0.0016  (≈ 0.16% YES)
```

**Operational rule (Issue 2):** synthesis **< ~0.5% of bankroll** → log **SKIP** on forward-track even if directionally non-zero.

### Publish discipline codified

1. **≥3pp re-run** between draft and publish (Issue 1 documented 5pp Anthropic move; Issue 2 standardizes 3pp).
2. **Sub-0.5% actionable minimum** for logging sized positions.
3. **Dual-price forward-track** when draft and publish locks differ.

Public methodology index updated 2026-05-26 (GitHub `cemini23/outlier-weekly-methodology`, commit `05b1fc9`).

### Forward-track entry

| Field | Value |
|-------|-------|
| Market | Iran closes airspace by June 30, 2026 |
| Outcome | June 30 |
| Direction | **SKIP** |
| Entry YES (draft → publish) | 27¢ → **29.7¢** |
| Sized fraction | **0%** |
| Resolution date | 2026-06-30 |
| Model output (publish) | Poisson ≈0¢; KL 0.023 bits SKIP; tail 1.5×; weighted ≈0.16% → SKIP |
| Status as of file-back | OPEN — post-mortem SKIP-CORRECT / SKIP-WRONG within 72h of resolution |
| Public sheet | https://cemini23.github.io/outlier-weekly-methodology/forward-track/ |
| Issue link | https://outlierweekly.substack.com/p/issue-2-iran-airspace-three-formulas |

**Re-watch trigger:** YES outside **24–34¢** before resolution → re-run and log in a future issue.

### Cross-issue calibration

| Issue | Category | Publish SKIP reason |
|-------|----------|---------------------|
| 1 | Regulatory (Anthropic–Pentagon) | Market converged to Poisson fair (27¢ lock) |
| 2 | Geopolitical (Iran airspace) | Market already at Poisson fair (30¢ lock); sub-0.5% rule |

Issue 1 anchor market (Anthropic June-30) repriced to **~46% YES** by 2026-05-26 — outside the 5–35% rare-event band; not reused for Issue 2.

## Snippets

> "At 29.7¢ YES, Poisson fair value and the market overlap. KL is noise. The synthesis is 0.16% — I log SKIP." [Source: *Outlier Weekly* Issue 2, publish lock section]

> "Issue 2 is shorter, answer-first, and encodes a 3¢ re-run before every publish lock." [Source: *Outlier Weekly* Issue 2, readability section]

## Dead Ends

- **Forcing a sized YES to contrast Issue 1** — overnight +2.4pp move removed edge; logging 0.16% as a hero call would violate the sub-0.5% actionable rule.
- **Reusing Anthropic–Pentagon for Issue 2** — market left rare-event band (~46% YES); skip narrative is post-mortem only.
- **Treating Issue 2 crypto draft (BTC ATH Aug 1)** — market does not exist as standalone binary; Iran June-30 was the live pick per Day-12 screen.
