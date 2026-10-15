---
title: "Chen & Koudas 2026 — What Drives AI Citations? Content, Retrieval and Model Knowledge in GEO"
type: source
tags: [seo, geo-aeo, academic-paper, citation-visibility, retrieval]
keywords: [GEO, generative engine optimization, ChatGPT citations, retrieval augmented generation, brand bias, within-website design]
related:
  - concepts/retrieval-vs-citation-visibility-geo.md
  - concepts/competitive-geo-citation-factors.md
  - concepts/ai-citation-sourcing-geo.md
  - concepts/geo-visibility-measurement.md
  - sources/jiang-2026-chatgpt-citations-retrieval-to-citation.md
maturity: validated
read_status: deep-read
created: 2026-10-14
updated: 2026-10-14
---

## Relations

- @concepts/retrieval-vs-citation-visibility-geo.md — the paper's central split
- @concepts/competitive-geo-citation-factors.md — answers the same question from a 252k-trial tournament
- @concepts/ai-citation-sourcing-geo.md
- @concepts/geo-visibility-measurement.md — citation counts are highly repeatable; the sampling design this implies
- @sources/jiang-2026-chatgpt-citations-retrieval-to-citation.md — companion study on the same retrieval-to-citation step

## Raw Concept

Title: What Drives AI Citations? Content, Retrieval and Model Knowledge in Generative Engine Optimization (GEO)
Authors: Mahe Chen, Nick Koudas (University of Toronto)
Type: arXiv preprint, ACM format
Location: `research to be indexed/seo/arxiv-2610.15033-what-drives-ai-citations-content-retrieval-and-m.pdf`
Retrieved: 2026-10-14
Pages: 11
Read status: deep-read

## Narrative

**The largest observational GEO study to date.** Two 90-day collections of daily answers to commercial questions, in contrasting markets:

| Market | Questions | Answers | Citations |
|---|---|---|---|
| US home internet (few large brands) | 651 | 143,249 | 396,188 |
| Small B2B software vendors | 55 | 14,850 | 71,849 |
| **Total** | **706** | **158,099** | **468,037** |

### The headline result — retrieval beats page properties

The paper separates two questions a publisher cares about, and they have different answers:

- **Within one website**, which page gets cited? **Page properties explain 2.8%** of the variation. Retrieval explains **32%**.
- **Across websites**, page properties do appear effective — but only because good practices concentrate on popular sites that are cited for other reasons.

> "Every page ChatGPT cites is one its own search retrieved." The citation set is a **subset of the retrieval set**. No on-page change reaches a page the engine never fetched.

### What actually moves citations

| Practice | Within-website effect | Verdict |
|---|---|---|
| Title and paragraphs matching the user's question | Positive | **Real — the main lever** |
| FAQ blocks | None within-site | Cross-site artifact only |
| Structured data | None within-site | Cross-site artifact only |
| Summary boxes | None within-site | Cross-site artifact only |
| Author boxes | None within-site | Cross-site artifact only |
| Page speed | None within-site | Cross-site artifact only |

This directly contradicts the standard GEO advice list. The study's design is why: a within-website comparison holds the site's authority constant, so a practice cannot inherit credit from the domain.

### Retrieval is rewritten every time

The engines do not run the user's question. They **rewrite it into new sub-queries on every answer**, and those sub-queries:
- rarely coincide with Google's or Bing's results, and
- change between runs.

Content therefore acts **indirectly** — by matching the engine's rewritten queries in meaning, not by matching the user's phrasing.

### Brand knowledge is a separate channel

The model's own parameters shape citations independently of any page:

- ChatGPT **writes brands it knows into its searches**, and prefers websites it knows.
- It **names brands with no supporting page at all**.
- Controlled experiments show **brand names reorder its rankings of products with identical facts**.

> "Pages are thus cited when searched; brands are also named when remembered."

### Method notes

Four approaches: a within-website design with a five-test robustness rule, an **API replay** of every question exposing the engine's searches and retrieved rankings, a search-free model probe, and controlled single-factor experiments (source order, brand names, publisher names, alternative set). Findings **replicate in the small-B2B market**. Data and code released.

## Snippets

> "Page properties ... explain little of the variation between pages of a website (2.8% for ChatGPT), although citation counts are highly repeatable. The reason lies in retrieval: every page ChatGPT cites is one its own search retrieved, and retrieval explains 32% of the same variation." [Source: arxiv-2610.15033 p.1]

> "Pages whose title and paragraphs match the questions people ask are cited more, whereas FAQ blocks, structured data, summary boxes, author boxes and page speed appear effective only across websites." [Source: arxiv-2610.15033 p.1]

> "Controlled experiments show that brand names reorder its rankings of products with identical facts. Pages are thus cited when searched; brands are also named when remembered." [Source: arxiv-2610.15033 p.1]

> "The engines rewrite each question into new sub-queries on every answer, rank pages by ho[st]..." [Source: arxiv-2610.15033 p.2]

## Dead Ends

- Treating an across-website correlation as a causal effect. Practices cluster on popular sites, which are cited for reasons unrelated to the practice. The paper's within-website design exists to remove exactly this confound.
- Optimising on-page markup while ignoring retrieval reach. If the engine's search never returns the page, no FAQ block, schema block, or speed gain can matter.
