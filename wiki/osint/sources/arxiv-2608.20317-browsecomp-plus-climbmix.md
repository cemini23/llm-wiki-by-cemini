---
title: BrowseComp-Plus on ClimbMix — retrieval, not reasoning, is the bottleneck
type: source
tags: [agentic-search, retrieval, evaluation, corpora]
keywords: [BrowseComp-Plus, ClimbMix, hop-grounding, evidence-recall, cmass, Castorini]
related:
  - concepts/agent-toolkit-routing-research-backlog.md
  - concepts/typed-relation-dependencies.md
  - sources/arxiv-k244-harness-skill-selection-cluster.md
maturity: draft
created: 2026-08-21
updated: 2026-08-21
read_status: skimmed
---

## Relations
- @concepts/agent-toolkit-routing-research-backlog.md
- @concepts/typed-relation-dependencies.md
- @sources/arxiv-k244-harness-skill-selection-cluster.md

## Raw Concept
- **title:** Projecting BrowseComp-Plus onto ClimbMix: Toward More Realistic Corpora for Agentic Search
- **author:** Sahel Sharifymoghaddam, Lingwei Gu, Yijun Ge, Jimmy Lin (University of Waterloo / Castorini)
- **type:** arXiv paper + GitHub/HF release
- **location:** research to be indexed/arxiv-2608.20317-browsecomp-plus-climbmix.pdf
- **retrieved:** 2026-08-21
- **pages:** arXiv HTML (pipeline, 57/830 yield, Table 1 eval, design rationale)
- **read-status:** skimmed

## Narrative
BrowseComp-Plus froze a ~100K-doc corpus built from the questions’ own supporting docs plus mined hard negatives — evidence *and* distractors were selected per query. This paper keeps the questions, relocates evidence onto ClimbMix (NVIDIA; 400B tokens, 553M ordinary web docs, *not* built for the benchmark).

Projection pipeline (dataset-agnostic; BM25 endpoint sufficient): decompose into hops (required vs confirmatory), ground each hop in ClimbMix, keep a question only if automatic verification + independent agent (Piika) + human review all confirm every hop is supported. Of 830 test questions, **57 survive**.

On those 57, the strongest agent (GPT-5.6 Sol max / Piika): answer accuracy 86.0%→80.7% (−5 pts) but **evidence recall 84.3%→21.4%** and **+63% search calls** (60.2→98.3). Weaker agents: recall collapses below 3%. Same agent answers all 57 when qrels are stuffed into context — the evidence is there; finding it at web scale is the task. Closed-book GPT-5.6 Sol already hits 70.2% on the projected 57, so accuracy alone is a contaminated headline; recall and tool-calls describe the search.

Release: https://github.com/castorini/cmass (academic; Apache-ish). Benchmark: huggingface.co/datasets/castorini/cmass. Hop decompositions / per-hop qrels withheld. Steal for agentic-search eval: project onto independent large corpora; score retrieval separately from reasoning; do not trust answer accuracy on questions the frontier model already memorized.

## Snippets
> Applied to the 830 BrowseComp-Plus test questions, our pipeline yields 57 fully grounded questions … the strongest agent we evaluate loses five points of answer accuracy but sees its evidence recall fall from 84.3% to 21.4% while issuing 63% more search calls. [Source: https://arxiv.org/abs/2608.20317 (retrieved 2026-08-21)]

> Retrieval, not reasoning, is what the benchmark now stresses. [Source: arxiv-2608.20317-browsecomp-plus-climbmix.pdf §1]

> That agent answers all 57 questions correctly when the judgments are supplied in context, and every question was human-verified to be grounded, so what BrowseComp-Plus_CM measures is the ability to find evidence at web scale rather than the ability to reason once it is found. [Source: arxiv-2608.20317-browsecomp-plus-climbmix.pdf §7]

Pipeline + analyses: https://github.com/castorini/cmass [Source: URL (retrieved 2026-08-21)]
