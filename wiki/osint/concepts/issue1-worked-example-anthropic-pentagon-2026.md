---
title: "Worked Example — Three-Formula System on the Anthropic-Pentagon June-30 Polymarket Binary (Outlier Weekly Issue 1)"
type: concept
tags: [concept, polymarket, worked-example, three-formula, regulatory-binary, outlier-weekly, issue-1]
keywords: [anthropic-pentagon-2026, three-formula-worked-example, regulatory-binary-poisson, outlier-weekly-issue1, forward-track-2026-06-30]
related:
  - concepts/issue2-worked-example-iran-airspace-2026.md
  - concepts/three-formula-system-polymarket-rare-events.md
  - concepts/poisson-edge-rare-events.md
  - concepts/shannon-entropy-kl-divergence-prediction-markets.md
  - concepts/taleb-fat-tails-barbell-prediction-markets.md
  - concepts/kelly-sizing-quarter.md
  - entities/platforms/polymarket.md
maturity: draft
created: 2026-05-14
updated: 2026-05-26
---

## Relations

- @concepts/issue2-worked-example-iran-airspace-2026.md — second consecutive Outlier skip-discipline case (geo tail, 2026-05-26); codifies ≥3pp publish re-run
- @concepts/three-formula-system-polymarket-rare-events.md — parent synthesis; this page is the second worked example after the canonical earthquake example
- @concepts/poisson-edge-rare-events.md — Poisson with caveats on binary regulatory markets (this page's methodological contribution)
- @concepts/shannon-entropy-kl-divergence-prediction-markets.md — KL produces SKIP at small divergence; this example illustrates that case
- @concepts/taleb-fat-tails-barbell-prediction-markets.md — Anthropic-Pentagon classified tail-bucket, 1.5x multiplier
- @concepts/kelly-sizing-quarter.md — quarter-Kelly sizing applied throughout
- @entities/platforms/polymarket.md — execution venue

## Raw Concept

What this page answers: when the three-formula synthesis is applied end-to-end to a single live Polymarket regulatory binary (Anthropic-Pentagon June-30), what does it produce, how does the "Poisson with caveats" framing apply to binary outcomes, and what happens when the market moves into the immediate neighborhood of the Poisson fair value between draft and publish? The worked example is performed at p_market ≈ 32¢ YES; the publish-day re-run at ≈ 27¢ YES collapses the synthesis to an effective SKIP. The forward-tracked entry is a SKIP — the first published instance of the methodology's skip-discipline.

Source: this page is the wiki cross-post of *Outlier Weekly*, Issue 1, published 2026-05-14 at https://outlierweekly.substack.com/p/issue-1-one-market-three-formulas. The Substack issue is the public artifact; this page is the wiki-internal calibration record.

## Narrative

### Market context

The market resolves YES if Anthropic and the U.S. Department of Defense reach a qualifying commercial agreement allowing DOD use of Claude or other Anthropic models, by 2026-06-30 23:59 ET. Continuation of phase-out usage does NOT count. Mere designation reversals without an accompanying agreement do NOT count [Source: Polymarket resolution rules, verified 2026-05-14]. The market launched 2026-03-06 in response to the February 2026 Pentagon supply-chain designation. YES price at analytical draft (Issue 1 §4 walk): ≈ 32¢. YES price at Day-4 publish-day lock (2026-05-14 ≈11:50a EDT): ≈ 27¢. The 5pp move is what collapses the synthesis to SKIP — see "Publish-day re-run" subsection below.

Window from Issue 1 ship to resolution: approximately 6.5 weeks.

Liquidity disclosure: 24-hour volume on the June-30 outcome was thin at publish (Filter 2 of the market-screening framework was relaxed for Issue 1 launch on methodology-demonstration grounds). Per the Issue 1 §4 disclosure: thin liquidity is a feature for a methodology demonstration (mispricing concentration), not a defect. Future issues default to enforcing Filter 2.

### Poisson with caveats (the methodological contribution)

The wiki's parent Poisson page is explicit that binary outcomes are generally a poor Poisson fit when the underlying event is heterogeneous or non-memoryless. The Anthropic-Pentagon market arguably violates memorylessness — each week without an agreement updates the probability of the next week through political and procurement-cycle dependencies.

Issue 1's contribution: Poisson *with caveats* is still a defensible primary base rate as long as the analyst is transparent about the assumption violation, and the magnitude of disagreement with the market is small enough that the position size stays small regardless. This framing handles binary regulatory markets in a way that does not require abandoning the synthesis or pretending the Poisson fit is clean.

The base-rate sketch used was λ = 0.05 qualifying agreements per active-negotiation week, derived from a small precedent set (ZTE, Kaspersky, and several smaller AI-vendor incidents). This is a sketch, not a calibrated regression. A more aggressive λ (0.08 per week) flips the direction; a more conservative λ (0.03 per week) calls for a larger NO position. Future issues will pin down the base rate with proper data.

### Math walk (analytical draft at p_market = 32¢)

Poisson:

```
P(≥1 agreement in 6.5 weeks | λ = 0.05) = 1 − exp(−0.325) ≈ 0.278  →  fair value 27.8¢
edge = 27.8 − 32 = −4.2¢  →  BUY_NO
quarter_kelly = |4.2 / 100| / 4 ≈ 0.0105
```

Shannon / KL:

```
KL(0.278 || 0.32) ≈ 0.006 bits  →  SKIP bucket
contribution = 0
```

Taleb:

```
tail-bucket classification: YES (kurtosis-high, single-headline re-pricing capacity)
multiplier: 1.5x
```

Synthesis:

```
weighted_fraction = 0.40 · 0.0105 + 0.35 · 0 + 0.25 · 1.5 · 0.0105
                  ≈ 0.0081
final_fraction = 0.81% of bankroll on NO
```

Override gates: none fire (KL bits < 0.30, |Poisson edge| < 30¢, no insider entropy collapse).

Quarter-Kelly cap (25%): does not bind. Per-position hard cap (5%): does not bind.

### Publish-day re-run (p_market = 27¢)

Between the analytical walk above and Day-4 publish-day lock (2026-05-14 ≈11:50a EDT), the market moved from 32¢ to 27¢ YES — into the immediate neighborhood of the Poisson fair value of 27.8¢. Re-running the synthesis:

```
Poisson edge = 27.8 − 27 = +0.8¢  →  near-zero edge (effectively BUY_YES, but inside noise)
quarter_kelly = |0.8 / 100| / 4 ≈ 0.002

KL(0.278 || 0.27) < 0.01 bits  →  SKIP bucket (well inside the 0.01-bit floor)
contribution = 0

Taleb tail-bucket multiplier: 1.5x (unchanged)

weighted_fraction = 0.40 · 0.002 + 0.35 · 0 + 0.25 · 1.5 · 0.002
                  ≈ 0.0008 + 0 + 0.00075
                  ≈ 0.0016
final_fraction ≈ 0.16% of bankroll  →  below the per-call minimum-actionable threshold (effective SKIP)
```

The Issue 1 forward-track entry is therefore SKIP, not a position. This is the first published instance of the synthesis's skip-discipline — the methodology refuses to trade when market and model converge inside the noise floor, and the refusal is logged in the same place a sized position would be.

### Forward-track entry

| Field | Value |
|-------|-------|
| Market | Anthropic-Pentagon deal by June 30, 2026 |
| Outcome | June 30 |
| Direction | **SKIP** (model–market convergence at publish-time) |
| Entry price (YES) at draft | ≈ 32¢ (worked example) |
| Entry price (YES) at Day-4 lock | ≈ 27¢ |
| Sized fraction | 0% of bankroll |
| Resolution date | 2026-06-30 |
| Model output (draft, 32¢) | Poisson −4.2¢ → BUY_NO; Shannon 0.006 bits → SKIP; Taleb tail-bucket 1.5x; weighted 0.81% NO |
| Model output (publish, 27¢) | Poisson +0.8¢ → near-zero edge; Shannon < 0.01 bits → SKIP; Taleb tail-bucket 1.5x; weighted ≈ 0% (effective SKIP) |
| Status as of file-back date | SKIP — no position taken; market re-watched if it re-prices >5pp from 27¢ before June 30 |
| Public sheet | https://cemini23.github.io/outlier-weekly-methodology/forward-track/ |

Resolution outcome will be updated on this page within 72 hours of June 30 resolution. Because the call is a SKIP, the resolution is evaluated as SKIP-CORRECT (the position the methodology would have taken at 27¢ would have lost — so the refusal saved the portfolio from a small drawdown) or SKIP-WRONG (the position would have won — so the refusal cost the portfolio a small gain). Either outcome populates the post-mortem section below.

### Cemini-internal calibration value

Beyond the public forward-track, this entry has wiki-internal calibration value:

1. **Validates the "Poisson with caveats" framing** on a real binary regulatory market. Future regulatory-binary issues cite this page rather than re-deriving the framing.
2. **Documents the first published skip-discipline case.** The parent three-formula-system page now has two worked examples — the canonical earthquake (Poisson dominates, sized at 0.83%) and this regulatory binary (Poisson partial at 32¢ → 0.81% NO at draft, then collapsing to effective SKIP at the 27¢ publish-day lock). Future Cemini strategy work can compare them: the earthquake example illustrates the *sized-position* output; this regulatory binary illustrates the *refusal-to-trade* output. Both are valid synthesis outputs.
3. **Records the directional-flip-on-small-drift sensitivity.** A 5pp market move (32¢ → 27¢) was sufficient to flip the directional signal from BUY_NO to near-zero BUY_YES and collapse the weighted position size from 0.81% to ~0.16% (below actionable threshold). Future issues should treat any pre-publish drift greater than ~3pp as a re-run trigger, not a pass-through.
4. **Records the λ-sketch sensitivity analysis** for future calibration. The forward-track outcome plus the post-mortem will inform whether 0.05 / week is in the right neighborhood for regulatory-binary base rates.

## Snippets

> "The methodology is not telling you to make a fortune on this market. It is telling you a small position is mathematically defensible based on a back-of-envelope base-rate sketch and a fat-tail-aware sizing layer." [Source: *Outlier Weekly* Issue 1, section "What does the weighted synthesis output, and what is the position?"]

> "λ = 0.05 per week is a sketch from precedent, not a calibrated regression. A more aggressive λ flips the direction; a more conservative λ calls for a larger NO." [Source: *Outlier Weekly* Issue 1, section "Does Poisson apply to this market?"]

> "The directional signal that had read BUY_NO at 32¢ flattens to a near-zero edge at 27¢ — under the synthesis's skip-discipline rules, that collapses the weighted output to an effective non-position. The forward-track row therefore records SKIP, not a sized bet. The methodology refuses the trade when the market and the model converge inside the noise floor; Issue 1's forward-track is the first published instance of that refusal." [Source: *Outlier Weekly* Issue 1, section "What is the forward-track entry for this call?"]

## Dead Ends

- **Refusing to apply Poisson to binary outcomes at all** — would leave the synthesis with only KL + Taleb on regulatory-binary markets, both of which require an operator estimate as input. Without Poisson as a third independent signal, the regulatory-binary case collapses to "operator estimate vs market" — exactly the single-indicator failure the synthesis is designed to avoid.
- **Pretending the Poisson fit is clean** — the parent Poisson page is explicit that binaries are poor fits. Ignoring that violates the wiki's own discipline and produces over-confident sizing.
- **Sizing the position larger to "make Issue 1 exciting"** — the methodology rewards consistent application across a portfolio, not heroics on any one market. The honest output collapsed from 0.81% NO at 32¢ to effective SKIP at 27¢; over-sizing or sticking with the 0.81% number after the market moved would have been a forward-track liability the first time a regulatory binary resolves against the methodology.
- **Pass-through publishing at 32¢ after the market moved to 27¢** — would have shipped the analytical-draft direction (BUY_NO) at a price where the synthesis no longer supports it. The methodology's skip-discipline catches exactly this case. The "5pp tolerance" rule in the operator playbook was an upper bound on *re-run trigger*, not a license to ignore directional flip; the Issue 1 publish-day call confirms the tighter ~3pp drift threshold (see calibration-value #3 above).
