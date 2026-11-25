---
title: AI in investment research — more output, more correlation
type: concept
maturity: draft
related:
  - sources/substack-rss-klement-2026-11-24-the-upside-of-ai-for-investment-analysis.md
  - sources/substack-rss-klement-2026-11-25-the-downside-of-ai-for-investment-analysis.md
  - concepts/ai-industry-trends-2026.md
updated: 2026-11-25
---

## Raw Concept

Question this page answers: what does AI do to investment research — more and faster analysis, or more crowded and stickier views?

From two Klement on Investing posts, 2026-11-24 and 2026-11-25, each reporting a separate study.

## Narrative

### The upside: more output, faster

FactSet added generative AI in 2023, which gives a natural experiment. Analysts who used it cited about 26 percent more third-party sources, covered about 24 percent more topics, and used about 21 percent more analyses and tools. Reports shipped faster. FactSet's share of analyst-report citations rose from about 25 percent to about 50 percent. [Source: substack-rss-klement-2026-11-24-the-upside-of-ai-for-investment-analysis.md]

That measures quantity and speed. Accuracy and hallucination were not tested in that study, which the author notes.

### The downside: more correlation, more stickiness

Lo and co-authors simulated seven large language models across 64 stock scenarios that varied analyst consensus, momentum, valuation and volatility. Two effects appeared. More capable models returned more similar answers across different inputs, so model quality removes variation rather than adding judgement. And portfolio volatility, while falling as stocks are added, stayed above the theoretical minimum, on a floor set by how resistant the model is to changing its view. [Source: substack-rss-klement-2026-11-25-the-downside-of-ai-for-investment-analysis.md]

The mechanism: everyone uses the same tool, so everyone buys and sells the same names. Different vendors do not help, because they read the same data.

### The combined read

The two studies are not in conflict. One measures the analyst's output; the other measures what happens to the market when that output is homogeneous. Both can be true: reports get broader and faster, and the recommendations inside them converge.

### What this means for a research stack here

- An AI-assisted feed that fans out to several models on the same inputs is one view, not an ensemble. Independent inputs matter more than independent vendors.
- A model that ignores changed inputs is a risk in a rebalancing context. It should be tested by feeding it a changed environment and checking whether the recommendation moves.
- Speed and breadth are the measurable wins. Treat them as such, and do not claim accuracy from them.

### Limits

Both studies are single-vendor or simulated. The herding result is a model environment, not observed market behaviour, because AI-driven investment is still a small share of flow. No production data yet.

[OPEN QUESTION 2026-11-25] How large the correlation effect is at realistic adoption levels is unmeasured.
