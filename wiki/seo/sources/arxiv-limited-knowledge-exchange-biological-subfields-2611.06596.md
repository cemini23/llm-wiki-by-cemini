---
title: "Limited knowledge exchange across biological subfields — a bibliometric pipeline with an LLM classifier"
type: source
tags: [source, arxiv, bibliometrics, classification, out-of-scope]
keywords: [agent-based modelling, bibliometric analysis, LLM classification, Qwen3, terminology divergence, Web of Science]
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
| Title | Limited knowledge exchange across biological subfields in agent-based modelling: an LLM-assisted bibliometric analysis |
| Author | Kira Pugh, Rebecca M Crossley, Sara Hamis (Uppsala University; University of Oxford) |
| Type | arXiv preprint (physics.soc-ph) |
| arXiv | 2611.06596v1, 4 Nov 2026 |
| Location | `research to be indexed/seo/arxiv-2611.06596-limited-knowledge-exchange-across-biological-sub.pdf` |
| Retrieved | 2026-11-10 |
| File | `arxiv-2611.06596-limited-knowledge-exchange-across-biological-sub.pdf` |
| Pages | 21 |
| Read status | read (abstract, method) |

## Narrative

**The question.** Agent-based models (ABMs) spread across ecology, epidemiology and oncology. The mathematics under them is largely shared. Do the subfields share knowledge with each other? [Source: arxiv-2611.06596 p.1]

**The pipeline.** A keyword search of the Web of Science Core Collection returned 23,902 documents. After cleaning, 22,936 articles remained. Two zero-shot prompts on a small local model, **Qwen3:8b**, classified each article. Prompt 1 split biology from not-biology. Prompt 2 assigned the biology articles to a subfield. [Source: arxiv-2611.06596 p.1-2]

**Reported results.** Citations stay inside the subfield: **83%** for ecology, **81%** for epidemiology, **69%** for oncology. **91%** of authors with two or more articles publish inside one subfield only. Permutation tests put both results far from chance (p ≤ 0.001). [Source: arxiv-2611.06596 p.1]

**Terminology diverges.** "Individual-based model" is used mainly in ecology. "Agent-based model" is used in epidemiology, oncology and outside biology. The two names describe overlapping methods. [Source: arxiv-2611.06596 p.1]

### Relevance to SEO

**Almost none.** The paper is a scientometrics study of biology. It holds no search, retrieval, content or marketing component.

**One thin transferable idea.** The same method carries two names in two communities, so a vocabulary built from one community misses the other. That is the same failure mode a keyword map has when it is built from one competitor's vocabulary. [TENTATIVE — inference from the terminology finding, not a tested SEO result]

The pipeline itself — a small local model classifying a large corpus at temperature zero, with human-annotated development and test sets — is a cheap pattern worth remembering for large content inventories. It is a pattern, not a finding about search.

Filed for inventory honesty only.

## Snippets

> "Terminology also differs, with "individual-based model" used mainly in ecology and "agent-based model" in epidemiology, oncology, and outside biology." [Source: arxiv-2611.06596 p.1]

> "83%, 81%, and 69% of citations from ecology, epidemiology, and oncology articles, respectively, go to articles in the same subfield." [Source: arxiv-2611.06596 p.1]

## Dead Ends

- **Treating the classification accuracy as validated.** The paper reports agreement against a human-annotated set, and the paper's development loop reused samples from the same distribution. It is adequate for a bibliometric count, not for a claim about content quality.
