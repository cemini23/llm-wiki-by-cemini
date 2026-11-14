---
title: "The EC anonymisation measures for Google Search data fail — and what that means for query data supply"
type: source
tags: [source, arxiv, search-data, regulation, dma, privacy, keyword-research]
related:
  - concepts/search-query-data-supply.md
  - concepts/corpus-overflow-out-of-scope.md
maturity: draft
read_status: read
created: 2026-11-14
updated: 2026-11-14
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Anonymous in Name Only: A Critical Review and a Reidentification Exercise on the European Commission's Anonymization Measures for Google Search Data under Article 6(11) of the DMA |
| Authors | David Sánchez, Benet Manzanares, Josep Domingo-Ferrer (Universitat Rovira i Virgili; ENS-PSL) |
| arXiv | 2611.17012 (cs.CR) |
| Pages | 32 |
| Location | `research to be indexed/seo/arxiv-2611.17012-anonymous-in-name-only-a-critical-review-and-a-r.pdf` |
| Retrieved | 2026-11-13 |
| Read status | read |

## Narrative

**SEO judgement first.** This paper does not study ranking, retrieval or citation. It has no GEO/AEO content. Its one live connection to this wiki is upstream of SEO work: it describes the legal regime that decides whether third parties receive **Google Search query, click and view data**. That data is the raw material of keyword research. The practical effect on practitioners is filed on @concepts/search-query-data-supply.md.

### What the paper examines

On 16 July 2026 the European Commission set out the measures Alphabet must implement to share Google Search data with competing search engines under Article 6(11) of the Digital Markets Act (case DMA.100209). The paper reviews these measures and tests them on real data. [Source: arxiv-2611.17012 p.1]

The technical measures are:

- **Entity allow list.** A word survives only if it appeared in queries from at least **50 signed-in users** in the past **13 months**. The list is updated monthly, and an allowed entity stays for five years.
- **Length threshold.** A query is suppressed unless it is shorter than **95%** of distinct queries issued in 2025 in its inferred language.
- **Metadata generalisation.** Each language, location and device combination must be shared by at least **1,000 signed-in users**. Location is generalised to country level. The timestamp is kept at day granularity.
- **Contractual safeguards.** Recipients are prohibited from attempting reidentification.

[Source: arxiv-2611.17012 p.6]

### The finding

The authors apply the measures to six months of Google Search data for Ireland and Spain, then count what stays unique. In Ireland, over the six-month window, **17.91%** of queries remain unique. Unique search records reach **24.27%** without the timestamp and **43.82%** with it. [Source: arxiv-2611.17012 p.9]

They report low-effort reidentification, record linkage and attribute inference:

- Hundreds of unique queries contained personal names and, in some cases, birth years that passed the entity threshold.
- Many Irish **Eircodes** passed the entity detector. Thousands of queries contained Eircodes, many for private residences, some as a directions origin.
- Queries in the least-represented languages clustered on a single day of a week, which suggests one traveller. Combining date, language, location and content produced a detailed profile.

[Source: arxiv-2611.17012 p.10]

The authors test the measures against the three EDPB criteria from Guidelines 02/2026 — no record isolation, no linkage, no inference — and state that the measures meet **none** of them. [Source: arxiv-2611.17012 p.3, p.30]

### Why the paper says the design fails

The suppression test checks each query component **in isolation**. It does not test whether the combination of components makes the record unique. The paper calls this the recurring error of ignoring joint uniqueness. [Source: arxiv-2611.17012 p.8-9]

The authors also attack the risk framing. The EC document uses the phrase "residual risk" more than a hundred times and never quantifies it. The definition the EC adopts comes from an unnamed expert report that has not been disclosed. [Source: arxiv-2611.17012 p.8]

### The claim most relevant here

In Recital (572) the EC states a goal of preserving "unique queries" and long-tail queries. The paper argues that this goal is incompatible with anonymisation: rare records are exactly the records that identify people. [Source: arxiv-2611.17012 p.8]

That is the tension a keyword-research practitioner inherits. Long-tail query data is the most useful data for a small site. It is also the data that the privacy analysis says must not be released. `[TENTATIVE]` — the paper argues the point; it does not measure a tooling outcome.

### The honest limits

- One paper, by three authors with a data-privacy research position. No reply from the Commission is included.
- The analysis covers Ireland and Spain. The authors argue the result generalises because Google holds about **89.69%** of the EEA search market, but only two countries are measured. [Source: arxiv-2611.17012 p.6]
- The paper's own remedy is well-established anonymisation, not disclosure. It does not propose publishing more query data.

## Snippets

> "the EC's approach relies on unjustified heuristics rather than formal privacy guarantees, underestimates the risks inherent in free-text search queries, and sacrifices data utility without achieving meaningful protection." [Source: arxiv-2611.17012 p.1]

> "data anonymization is especially about protecting the most vulnerable minority records — the records that are particularly exposed precisely because they are the rarest and most outlying." [Source: arxiv-2611.17012 p.8]

## Dead Ends

- **Using this paper for a GEO or AEO claim.** It measures privacy, not citation.
- **Reading Article 6(11) as a new keyword-data source.** It is a competition remedy. Whether any SEO tool gets access is unresolved — see @concepts/search-query-data-supply.md.
