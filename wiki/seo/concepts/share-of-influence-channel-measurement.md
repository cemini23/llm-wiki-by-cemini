---
title: "Share of Influence — channel weighting for a buyer journey, and its limits"
type: concept
related:
  - sources/newsletter-rss-sparktoro-2026-11-24-new-feature-share-of-influence-lets-you-calculat.md
  - entities/tools/sparktoro.md
  - concepts/ai-assistant-usage-buyer-journey-share.md
  - concepts/search-query-data-supply.md
updated: 2026-11-25
---

## Raw Concept

This page answers one question: what does SparkToro's Share of Influence measure, and what can a marketer safely do with the numbers? The source is @sources/newsletter-rss-sparktoro-2026-11-24-new-feature-share-of-influence-lets-you-calculat.md, fetched 2026-11-25.

## Narrative

**What it measures.** Share of Influence ranks **channels** of influence for an audience, not single sources. Each channel gets a weight, the journey stage where it acts, and a confidence level. It sits one level above SparkToro's older source-level data [TENTATIVE — vendor announcement, no independent test].

**How the weight is built.** The base is a clickstream panel. On top, SparkToro layers crawled data from YouTube, Reddit, social platforms, Google keyword volume, AI prompts, and podcasts. A "moderately complex sequence of equations" turns that into a comparative weight. A channel gains weight when the audience uses it far more than the average web user in the same country, and when relevant content inside it has large viewership.

**Journey stages.** Awareness, Interest, Consideration, Conversion. The tool also reports typical journey length in touchpoints:

| Category | Touchpoints |
|----------|-------------|
| Candy bars | 2–3 |
| Wine fridge | 4–7 |
| Enterprise B2B software | 15–20 |

**Reading rules.** These matter more than the output.

1. **The unit is undefined.** The article never names the scale and never confirms percentages. Do not write "X% of influence" unless the product UI shows that label.
2. **All values are modelled.** Some carry a "Low" confidence mark. The author states the data "could be wrong."
3. **Expect disagreement.** A niche expert may find the ranked channels do not match personal experience.
4. **Best for new or shifting categories.** Where behaviour is stable, the panel adds little.

**How to use it for a local business.** Two safe uses. First, as a hypothesis list: which channels might carry a customer before they choose a shop. Second, as a comparison between two audiences, such as two trade segments. Do not use it to plan GEO, local-pack, or citation work. It does not measure citations, rankings, or AI visibility. For those, see @concepts/ai-assistant-usage-buyer-journey-share.md and @concepts/search-query-data-supply.md.

**What is missing.** No panel size, no country list, no formula, no validation. Mark any use as an estimate.

## Snippets

> Channels are "weighted by the amount they contribute" — the article gives no unit and no percent definition. [Source: sparktoro.com/blog/new-feature-share-of-influence/, retrieved 2026-11-25]
