---
title: "SparkToro — Share of Influence: channel weighting across a buyer journey"
type: source
related:
  - concepts/share-of-influence-channel-measurement.md
  - entities/tools/sparktoro.md
  - concepts/ai-assistant-usage-buyer-journey-share.md
  - concepts/search-query-data-supply.md
updated: 2026-11-25
read_status: read
maturity: draft
---

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | NEW Feature: Share of Influence Lets You Calculate which Channels Contribute to any Buyer Journey |
| **Author** | SparkToro (Rand Fishkin) |
| **Type** | Product announcement (vendor blog) |
| **URL** | https://sparktoro.com/blog/new-feature-share-of-influence-lets-you-calculate-which-channels-contribute-to-any-buyer-journey/ |
| **Published** | 2026-11-24 |
| **Location** | `research to be indexed/newsletter-rss-sparktoro-2026-11-24-new-feature-share-of-influence-lets-you-calculat.md` |
| **Retrieved** | 2026-11-24 (RSS); full page fetched 2026-11-25 |
| **Pages** | n/a (web article) |
| **Read status** | read |

The RSS body cut off mid-sentence. The full page was fetched on 2026-11-25. The screenshots on that page are images, so the numbers in them are not recorded here.

## Narrative

SparkToro already reported which single sources an audience follows. Share of Influence adds a layer above that: it ranks **channels** of influence, weighted by how much they contribute to a buyer journey. For wine fridge shoppers, the top channels include niche publications such as Wine Spectator and Wine Folly [Source: sparktoro.com/blog/new-feature-share-of-influence/, retrieved 2026-11-25].

**What it measures.** A ranked list of channels that affect a purchase journey, each with a weight, a journey stage, and a confidence level. The output is comparative, not absolute.

**How the weight is set.** SparkToro feeds clickstream data and crawled data into "a moderately complex sequence of equations" built with AI help. A channel gains weight when the audience uses it far more than the average web user in that country, and when relevant content inside it has large viewership. It loses weight when the opposite holds. Baseline comparison is against general web users in the same country [Source: sparktoro.com/blog/new-feature-share-of-influence/, retrieved 2026-11-25].

**Journey stages.** A "By Journey" tab splits influence across four stages: Awareness, Interest, Consideration, and Conversion. It also gives typical journey length in touchpoints:

| Category | Touchpoints |
|----------|-------------|
| Candy bars | 2–3 |
| Wine fridge | 4–7 |
| Enterprise B2B software | 15–20 |

**Data inputs.** The base is SparkToro's clickstream panel, described as "where millions of people go on the web." On top, it layers crawled or retrieved data from YouTube, Reddit, social platforms, Google keyword volume, AI prompts, and podcast platforms.

**What the article does not say.** It never defines the unit of the weight. It does not confirm that values are percentages. It gives no panel size, no country coverage, and no formula. Any reading of the numbers as a percent share is an assumption, not a fact from the source.

**Stated limits.** All figures are modelled estimates. Some carry a "Low" confidence mark. The author says the data "could be wrong." An expert may find the output disagrees with personal experience. The feature may help most in new spaces or when behaviour is shifting.

**Why it matters here.** The metric gives a channel-level view of a purchase journey. For local marketing, that frames a budget question: which channels carry the journey before a shop is chosen. It is not a GEO or local-pack metric, and it does not measure citations or rankings. See @concepts/share-of-influence-channel-measurement.md for the reading rules.

## Snippets

> "Share of Influence ... produces an extremely impressive list of channels that impact buyer journeys, weighted by the amount they contribute." [Source: sparktoro.com/blog/new-feature-share-of-influence/, retrieved 2026-11-25]

> Rand Fishkin, on the estimates: the data "could be wrong!" [Source: sparktoro.com/blog/new-feature-share-of-influence/, retrieved 2026-11-25]
