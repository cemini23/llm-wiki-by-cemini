---
title: "CAMP — weight mapping for LLMs on 3D in-memory compute arrays"
type: source
tags: [source, arxiv, hardware, inference, out-of-scope]
keywords: [CAMP, 3D-IMC, analog in-memory computing, weight mapping, tensor parallelism, batch parallelism, KV cache]
related:
  - concepts/corpus-overflow-out-of-scope.md
maturity: draft
read_status: read
created: 2026-11-10
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | CAMP: Context-Aware Mapping and Placement for LLMs on 3D-IMC Arrays |
| Author | Orhun Görkem, Athanasios Vasilopoulos, Georgios Pagonis, Victoria Clerico, Hadjer Benmeziane, Irem Boybat, Hsinyu Tsai, Abu Sebastian, William Andrew Simon (IBM Research) |
| Type | arXiv preprint (cs.AR) |
| arXiv | 2611.07707v1, 5 Nov 2026 |
| Location | `research to be indexed/seo/arxiv-2611.07707-camp-context-aware-mapping-and-placement-for-llm.pdf` |
| Retrieved | 2026-11-10 |
| File | `arxiv-2611.07707-camp-context-aware-mapping-and-placement-for-llm.pdf` |
| Pages | 20 |
| Read status | read (abstract, introduction) |

## Narrative

**The problem.** Serving a large language model is limited by memory movement. Analog in-memory computing removes the cost of loading static weights, because the multiply-accumulate runs inside the array. 3D-IMC stacks the arrays in vertical tiers, which raises capacity. The vertical tiers cannot be read at the same time, so **where the weights sit** decides which computations can run in parallel. [Source: arxiv-2611.07707 p.1-2]

**The proposal.** Context-Aware Mapping and Placement (CAMP) encodes the inference context in a **conflict matrix**. The context has three parts: the hardware architecture, the network shape (dense or mixture-of-experts), and the runtime setting (batch size, sequence length). A profiling loop then prunes the search and returns a mapping. [Source: arxiv-2611.07707 p.2-3]

**Reported results.** Compute utilization rises from **42.4% to 60.3%**. The paper reports up to **2.0×** higher 3D-IMC throughput and **1.74×** higher end-to-end throughput against the state of the art. The method is offline and needs no hardware change. [Source: arxiv-2611.07707 p.1]

### Relevance to SEO

**None.** This paper is accelerator architecture. It holds no search, retrieval, content or marketing component. Nothing here changes how a page is retrieved, filtered, sampled or cited.

It is filed for inventory honesty only, under the corpus-overflow convention.

**Name collision to note.** "CAMP" is used here for a hardware mapping algorithm. The same acronym appears in other literature. Search for the full title, not the acronym.

## Snippets

> "how weights are placed in memory determines which Matrix-Vector Multiplications (MVMs) can execute concurrently, affecting latency and throughput." [Source: arxiv-2611.07707 p.1]

> "improving 3D-IMC compute utilization from 42.4% to 60.3%, delivering up to 2.0× higher 3D-IMC throughput and 1.74× higher end-to-end throughput." [Source: arxiv-2611.07707 p.1]

## Dead Ends

- **Searching for a GEO lever in the paper.** There is none. The only SEO-adjacent fact is that inference cost is falling, and this paper is one of many causes.
