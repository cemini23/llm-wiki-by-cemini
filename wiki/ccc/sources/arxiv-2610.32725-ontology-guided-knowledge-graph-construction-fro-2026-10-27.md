---
title: "Ontology-Guided Knowledge Graph Construction from Scientific Publications"
type: source
tags: [source, arxiv, knowledge-graph, agentic-pipeline]
related: []
maturity: draft
read_status: skimmed
created: 2026-10-27
updated: 2026-10-27
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Ontology-Guided Knowledge Graph Construction from Structured Metadata and Climate Science Publications |
| Authors | Aayush Acharya, Qi Zhang, Eduard Dragut, Longin Jan Latecki (Temple University) |
| arXiv | 2610.32725 |
| File | `arxiv-2610.32725-ontology-guided-knowledge-graph-construction-fro.pdf` |
| Retrieved | 2026-10-27 |
| URL | https://arxiv.org/abs/2610.32725 |
| Read status | skimmed (abstract + intro) |

## Narrative

Manual curation cannot keep pace with scientific literature. The paper builds an **agentic, ontology-guided framework** for knowledge-graph construction.

The pipeline uses specialised agents for four jobs: document understanding, information extraction, ontology conformance, and entity linking. An LLM first extracts triples with explicit textual evidence. A multistage verification step then grounds each triple in the ontology, enforcing schema constraints and requiring a text fragment as evidence.

Agreement study over 1,000 extracted triples: Gemini-2.5-flash reaches Cohen's κ of 0.640–0.700 against three human annotators. Human–human agreement on the same task is 0.616–0.689. The model sits inside the human range.

Applied to 2,000 climate-science publications, the pipeline produced a graph with 133,990 nodes and 755,308 relations. Of the 23,327 triples the publications contribute after validation, 98.96% were judged correct.

**Why it matters.** Two transferable ideas for a curated wiki. First, require a text fragment as evidence for every extracted claim — that is the same discipline as a citation tag. Second, put the ontology at the artifact level rather than trying to model every entity occurrence. The second point matches the sibling paper on enterprise RAG in this same wave.

## Snippets

> "By enforcing schema constraints and requiring evidence in the form of text fragments, we ensure the data is both semantically consistent and traceable." [Source: `arxiv-2610.32725-ontology-guided-knowledge-graph-construction-fro.pdf` p.1 (arXiv 2610.32725), retrieved 2026-10-27]
