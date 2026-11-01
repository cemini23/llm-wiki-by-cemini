---
title: "Using geometry to see why volatility scales with √t"
type: source
tags: [source, newsletter, volatility, correlation, options]
related: []
maturity: draft
read_status: read
created: 2026-11-01
updated: 2026-11-01
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Using Geometry to See Why Volatility Scales With √t |
| Source | moontower |
| File | `substack-rss-moontower-2026-10-28-using-geometry-to-see-why-volatility-scales-with.md` |
| Retrieved | 2026-11-01 |
| URL | https://moontowermeta.com/using-geometry-to-see-why-volatility-scales-with-root-t/ |
| Read status | read |

## Narrative

Moontower Meta dates this post to 2026-10-28. The post builds the square-root-of-time rule from right triangles. It then changes the angle to show what correlation does to distance from the start. Every figure below comes from this post alone.

The post states a rule of thumb. A move of 1% a day is about 16% a year because √252 ≈ 16. It calls one day's move σ. When the next day is independent, it draws that move at a right angle to the path so far. Each independent day adds one σ² to the squared distance. After t days the squared distance is t·σ², so the distance is σ√t. The post says variance adds across days and volatility scales with √t. A check with σ = 1 gives 1.414² + 1² = 3 and √3 ≈ 1.732. Six independent days trace the spiral of Theodorus: σ, σ√2, σ√3, 2σ, σ√5, σ√6. Four days put the path 2σ from the start.

The post then lets the angle θ leave 90°. It calls the result the law of cosines: Pythagoras plus a correction term, 2ab·cos θ. It sets cos θ equal to the correlation ρ between the new day's move and the path so far. With a = σ√2 and b = σ, it gives three day-3 results. At 60° (cos θ = 0.5) c² = 3σ² + 1.41σ² = 4.41σ², so c ≈ 2.10σ. At 90° c² = 3σ², so c ≈ 1.73σ. At 120° (cos θ = −0.5) c² = 3σ² − 1.41σ² = 1.59σ², so c ≈ 1.26σ. It maps θ = 0° to ρ = +1, 60° to ρ = +0.5 (momentum), 90° to ρ = 0, 120° to ρ = −0.5 (reversion), and 180° to ρ = −1. The √t rule is the 90° case.

The post holds one angle and walks further. After six days it reports 4.22σ at 60°, against σ√6 = 2.45σ. It reports 2.45σ at 90°. It reports 1σ at 120°, and says the path closes into a hexagon. After 20 days it reports 11.9σ at 60°, against σ√20 = 4.5σ. Below 90° it says distance grows close to linearly, about σ·cos θ per day once the path is away from the start (≈0.5σ a day at 60°). Above 90° it says distance levels off at −σ ÷ (2·cos θ): 1.93σ at 105° and 1σ at 120°. It calls a fixed angle to the running total a toy. It says the usual measure is the correlation between returns k days apart. Positive cross terms make the distance longer than σ√t. Negative cross terms make the distance shorter.

The post compares a daily hedger with a holder to expiry by a variance ratio. VR = 1 means independent days. VR > 1 means momentum. VR < 1 means reversion. The example uses 1% daily volatility, which the post annualizes to 15.9%, and sets ρₖ = ρᵏ. For ρ = −0.5 it reports VR(20) = 0.36 and a 20-day volatility that annualizes to 9.5%. For ρ = 0 it reports VR(20) = 1 and 15.9%. For ρ = +0.5 it reports VR(20) = 2.80 and 26.6%. It says daily delta-hedge P&L is roughly ½·Γ·S² × (that day's squared return − one day of implied variance). The daily squared returns pay the hedger. An unhedged hold to expiry depends on the 20-day distance. On the reverting series the hedger realizes 15.9% and the holder gets the distribution of a 9.5% volatility. On the trending series the hedger realizes 15.9% and the holder gets 26.6%. For a quant-finance reader, the split separates hedge-frequency variance from terminal variance when daily returns correlate. For a macro reader, the same split applies when a regime has momentum or reversion.

## Snippets

> "The rule of thumb for a random walk is that volatility scales with the square root of time. 1% a day is about 16% a year because √252 ≈ 16." [Source: https://moontowermeta.com/using-geometry-to-see-why-volatility-scales-with-root-t/ (retrieved 2026-11-01)]
