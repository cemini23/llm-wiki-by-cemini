---
title: "Klement on Investing — the downside of AI for investment analysis"
type: source
related:
  - concepts/ai-in-investment-research.md
  - concepts/ai-industry-trends-2026.md
updated: 2026-11-25
---

## Raw Concept

| Field | Value |
|-------|--------|
| Title | The downside of AI for investment analysis |
| Author | Joachim Klement (Klement on Investing) |
| Type | newsletter, RSS |
| Location | `research to be indexed/substack-rss-klement-2026-11-25-the-downside-of-ai-for-investment-analysis.md` |
| Retrieved | 2026-11-25 |
| Published | 2026-11-25 |
| Read status | read |

## Narrative

### The study

Andrew Lo and co-authors ask what happens when many investors use generative AI for stock decisions. They run a simulation, because AI-driven investment is not yet a large share of market action. Seven large language models are given 64 scenarios that differ in fundamental and price inputs: analyst consensus, momentum, valuation and volatility. Each model is asked what to do and to estimate the gap between fair value and price. [Source: substack-rss-klement-2026-11-25-the-downside-of-ai-for-investment-analysis.md]

### The result

Model capability, measured by the LMSYS Chatbot Arena ELO score, correlates with agreement. The more capable the model, the more it returns the same answer even when the inputs change. Noise is removed, which is normally good, but here it means the model gives the same recommendation regardless of the market environment.

The portfolio consequence: adding stocks lowers volatility, but it stays well above the theoretical minimum. It sits on a floor set by how resistant the model is to changing its view when inputs change.

### The interpretation

If everyone uses the same tool, they buy and sell the same stocks, which reduces diversification and makes markets riskier. Using different models does not fix it, because they read the same input data and converge anyway.

### The caveat

This is a model-environment simulation. The authors say so. How much of the effect appears in live markets is unknown, because AI-driven investment is too small a share today.

### Read

This is the counterpart to the 24 November post. One measures more and faster analyst output; this one measures correlated and sticky output. Together they are a fair statement of the trade-off, and they point at a concrete risk for any AI-assisted research stack: many models on the same inputs is one view, not many. Indexed in `concepts/ai-in-investment-research.md`.
