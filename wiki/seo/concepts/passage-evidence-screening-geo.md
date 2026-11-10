---
title: "Passage evidence screening — the cheap gate a page must clear first"
type: concept
tags: [concept, geo-aeo, retrieval, filtering, content-design]
keywords: [passage-level relevance, cascade, deciding evidence, chunk view, retrieval gate, filter stage, CascadeFilter]
related:
  - sources/arxiv-cascadefilter-semantic-filtering-2611.08367.md
  - concepts/retrieval-vs-citation-visibility-geo.md
  - concepts/generative-engine-optimization.md
  - concepts/on-page-seo-local.md
maturity: draft
created: 2026-11-10
updated: 2026-11-10
---

## Raw Concept

**The question this page answers.** A generative search engine retrieves a large set of pages. It must then decide which pages to read and which to use. What decides that first cut, and what can a publisher do about it?

**Sources that synthesize into this page.** One source at present: @sources/arxiv-cascadefilter-semantic-filtering-2611.08367.md. The claim is [TENTATIVE] because one paper supports it and no search-engine measurement supports it yet.

## Narrative

### The mechanism

A retrieval pipeline runs in stages. A cheap stage reads a short piece of text. A more expensive stage reads the full page. An expensive model decides the last cases. @sources/arxiv-cascadefilter-semantic-filtering-2611.08367.md formalises this as a three-stage cascade and optimises the thresholds between the stages.

The design detail that matters for content work is why the first stage reads a **chunk** rather than the page. The authors report that the chunk view "isolates the deciding signal — a different error mode, not just cheaper". Their example puts a **28-token** deciding passage against a **430-token** full document. [Source: arxiv-2611.08367 p.3]

### What follows for a page

1. **Put the deciding fact in one compact block.** A page that states its main answer in a short, self-contained passage clears the cheap gate. A page that spreads the answer across a long document asks the filter to read the whole document.
2. **Make the block stand alone.** A passage that needs the paragraph above it to make sense is expensive to use. A passage that names the subject and the answer is cheap.
3. **Do not hide the answer behind a flourish.** The first stage tests a condition, for example "does this passage state the shop's Sunday hours?" A poetic opening does not satisfy the condition.
4. **Expect the expensive stage to be reached only sometimes.** Most pages will never be read in full.

### The honest limits

- This is an argument from a filtering paper, not a measurement on a search engine. No engine has published a cascade structure of this exact shape.
- The paper optimises **cost** against an oracle. Its accuracy numbers describe agreement with a stronger model, not agreement with the truth.
- Passage-level relevance already appears in the GEO literature from several directions. This page supplies a mechanism, not a new effect size.

### How the page fits with the rest of the wiki

@concepts/retrieval-vs-citation-visibility-geo.md separates retrieval visibility from citation visibility. This page sits inside the retrieval half: it explains one reason a retrieved page never becomes a cited page. @concepts/on-page-seo-local.md carries the writing rules for the passage itself.

## Snippets

> "Chunk view isolates the deciding signal — a different error mode, not just cheaper." [Source: arxiv-2611.08367 p.3]

> "its threshold calibration follows a prescribed adjustment sequence after cascade assembly, rather than minimizing cost over alternative combinations of stage thresholds." [Source: arxiv-2611.08367 p.1]

## Dead Ends

- **Reading the cascade as a ranking model.** The cascade decides whether a record satisfies a condition. It does not order the records.
- **Optimising for a chunk size.** The paper fixes chunking by retrieved evidence, not by a fixed token count. No content rule follows from the 28-token example beyond "keep the deciding sentence short".
