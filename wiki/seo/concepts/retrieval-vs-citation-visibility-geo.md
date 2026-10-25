---
title: "Retrieval visibility vs citation visibility in GEO"
type: concept
tags: [seo, geo-aeo, citation-visibility, retrieval, measurement]
keywords: [GEO, retrieval visibility, citation visibility, generative engine, query rewriting, share of voice]
related:
  - sources/chen-2026-what-drives-ai-citations.md
  - sources/jiang-2026-chatgpt-citations-retrieval-to-citation.md
  - concepts/competitive-geo-citation-factors.md
  - concepts/geo-visibility-measurement.md
  - concepts/ai-citation-sourcing-geo.md
maturity: validated
created: 2026-10-14
updated: 2026-10-14
---

## Relations

- @sources/chen-2026-what-drives-ai-citations.md — 158,099 answers; retrieval explains 32% against 2.8% for page properties
- @sources/jiang-2026-chatgpt-citations-retrieval-to-citation.md — SSE traces; retrieval frequency predicts citation, proxies recover a quarter of URLs
- @concepts/competitive-geo-citation-factors.md — the gatekeeper factors that decide ranking inside the retrieved set
- @concepts/geo-visibility-measurement.md — how to measure any of this
- @concepts/ai-citation-sourcing-geo.md

## Raw Concept

The question this page answers: **when a generative engine cites a page, which step actually decided it — and what can a publisher change?**

Prompted by two independent 2026 studies reaching the same conclusion from different methods: Chen & Koudas (158,099 answers, API replay) and Jiang et al. (SSE traces across four ChatGPT settings).

## Narrative

A generative engine answers in two stages, and they are **separately optimisable**:

1. **Retrieval visibility** — does the engine's own search return your page at all?
2. **Citation visibility** — given the retrieved set, is your page one of the handful shown as a source?

**Being retrieved is necessary and not sufficient.** Both studies find that the first stage dominates the second, and that most published GEO advice targets the wrong one.

### The evidence

| Finding | Source |
|---|---|
| Retrieval explains **32%** of within-website citation variance | Chen & Koudas |
| Page properties explain **2.8%** | Chen & Koudas |
| **Every cited page is one the engine's own search retrieved** | Chen & Koudas |
| Candidates retrieved **more often across runs** are cited more | Jiang et al. |
| Google Search + Responses API together recover **~25%** of cited URLs | Jiang et al. |
| Longer retrieval snippets are a **weaker but consistent** signal | Jiang et al. |

### What the split explains

**Why the standard GEO checklist underperforms.** Chen & Koudas test FAQ blocks, structured data, summary boxes, author boxes, and page speed **within a single website**. None move citations there. They appear effective only *across* websites — because the sites that adopt them are the sites already cited for other reasons. A within-website design removes that confound; the effects vanish.

**Why content still matters, indirectly.** Content is not irrelevant — it acts **through retrieval**. Pages whose title and body match the engine's rewritten sub-queries in meaning are retrieved more, therefore cited more. The lever is relevance to the *engine's* query, not to the user's phrasing.

**Why query rewriting breaks naive tracking.** Engines rewrite each question into new sub-queries **on every answer**, and those sub-queries rarely match Google or Bing results and change between runs.

**Why brand is a second, separate channel.** ChatGPT writes brands it knows **into its searches**, prefers sites it knows, and **names brands with no supporting page**. Controlled experiments show brand names reorder rankings of products with **identical facts**. Retrieval explains page citations; parametric knowledge explains brand mentions. They need separate measurement.

### How this should change practice

- **Measure the two stages separately.** A single "are we cited" number cannot tell you whether to fix reach or fix content.
- **Measure at hostname and entity level**, not just exact URL — the proxies agree far better there.
- **Track retrieval stability, not just presence.** A page retrieved in 1 of 10 runs is not the same asset as one retrieved in 9.
- **Re-test after a model change.** Jiang et al. find materially different retrieval behaviour across ChatGPT 5.2→5.5, including multi-round retrieval arriving in the Thinking mode.
- **Do not infer causation from across-site correlations.** That is the specific error the within-website design corrects.

### Open question

Neither paper settles **how to raise retrieval visibility deliberately.** Both establish that it dominates. Chen & Koudas show content-relevance to the rewritten query is the mechanism; whether that is achievable by page edits, or is mostly a function of domain authority and brand recall, is not resolved here.

[OPEN QUESTION 2026-10-14] — whether the 32%/2.8% split holds for non-commercial query classes. Both collections are commercial-question markets.

## Snippets

> "Pages are thus cited when searched; brands are also named when remembered." [Source: arxiv-2610.15033 p.1]

> "GEO should distinguish retrieval visibility from citation visibility, account for rewritten queries and run-to-run variation, and consider hostname- and entity-level presence in addition to exact URLs." [Source: arxiv-2610.15382 p.1]

## Dead Ends

- **Optimising markup while ignoring retrieval.** If the engine's search never returns the page, no FAQ block, schema block, or speed gain can reach the citation set.
- **Treating Google rank as a proxy for generative citation.** Measured agreement is weak at URL level and the proxies recover only about a quarter of cited URLs.
- **Assuming one setting generalises.** Retrieval behaviour differs across ChatGPT 5.2→5.5; a strategy validated on one setting is unvalidated on the next.
