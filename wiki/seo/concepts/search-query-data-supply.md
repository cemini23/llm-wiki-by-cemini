---
title: "Search query data supply — where keyword data comes from and what gets suppressed"
type: concept
tags: [concept, seo, keyword-research, data-provenance, regulation]
keywords: [keyword data, query data, Google Search data, DMA Article 6(11), suppression threshold, long tail, anonymisation]
related:
  - sources/arxiv-2611.17012-dma-google-search-anonymization-2026-11-14.md
  - entities/tools/google-search-console.md
  - entities/tools/semrush.md
  - concepts/local-seo-foundations.md
maturity: draft
created: 2026-11-14
updated: 2026-11-14
---

## Raw Concept

**The question this page answers.** Every keyword volume or difficulty number has an origin. What is the origin, and what has been removed before a practitioner sees the data?

**Sources that synthesize into this page.** One source at present: @sources/arxiv-2611.17012-dma-google-search-anonymization-2026-11-14.md. That paper is a privacy critique, not an SEO study. The link to keyword research is this wiki's reading and it is `[TENTATIVE]`.

## Narrative

### Three supply routes

A practitioner gets query data through three routes, and each one filters the data differently.

| Route | Who supplies it | What is filtered |
|-------|-----------------|------------------|
| First-party | Google Search Console, site search logs | Only queries the site already appears for. Its own reporting thresholds hide low-volume terms. |
| Commercial tooling | Third-party vendors | Built from panel data, clickstream and estimation. Volume figures are modelled, not counted. |
| Regulatory | Google, under DMA Article 6(11) | Shared with competing **search engines**, after anonymisation |

### The regulatory route

On 16 July 2026 the European Commission set the anonymisation measures for this third route. The measures suppress rare words, short-list entities, and metadata combinations below 1,000 users. The review paper finds that they still leave **17.91%** of queries unique in a six-month Irish sample, and **43.82%** of records unique once the day-level timestamp is included. [Source: arxiv-2611.17012 p.6, p.9]

### The tension that matters for a small site

The paper quotes the Commission's stated goal of preserving "unique queries" and long-tail queries. It then argues the opposite point: rare records are the records that identify individuals. [Source: arxiv-2611.17012 p.8]

The practitioner consequence is direct. The long tail is the part of the query distribution a small local site can compete for. It is also the part that any sound anonymisation scheme must suppress or generalise. `[TENTATIVE]`

### What is not known

- Whether Article 6(11) gives **SEO tooling** access is unresolved. The remedy names third-party providers of online search engines, not analytics vendors. `[OPEN QUESTION 2026-11-14]`
- Whether the final joint DMA/GDPR guidelines were adopted after the paper's cut-off. The paper states that no final version had been adopted at writing. `[NEEDS VERIFICATION 2026-11-14]`
- Whether any commercial tool now reflects data from this route. `[OPEN QUESTION 2026-11-14]`

### Practical rule

Treat a volume number as a **modelled estimate with a known exclusion rule behind it**, not as a count. Before a keyword decision rests on a very specific long-tail term, prefer first-party evidence — Search Console impressions, site search logs, or a paid query report — over a modelled third-party figure.

## Dead Ends

- **Reading this page as legal advice.** It records one paper's argument.
- **Assuming the DMA opens Google query data to SEO tools.** The text does not say that.
