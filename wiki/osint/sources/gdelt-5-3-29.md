---
title: "Talking to GDELT Through Knowledge Graphs"
type: source
tags: [pdf, k49, llm-agents]
clusters: [llm-agents]
related:
  - concepts/llm-agent-systems.md
maturity: validated
read_status: deep-read
created: 2026-04-23
updated: 2026-05-16
---

## Relations

- @concepts/llm-agent-systems.md — cluster hub for LLM agent-systems research in the Cemini corpus

## Raw Concept

- **Original title**: Talking to GDELT Through Knowledge Graphs
- **Author(s)**: Audun Myers, Max Vargas, Sinan G. Aksoy, Cliff Joslyn, Benjamin Wilson, Lee Burke, Tom Grimes (Pacific Northwest National Laboratory). arXiv:2503.07584v3, June 2025.
- **Type**: PDF
- **Location**: research for cemini/gdelt 5 3:29.pdf
- **Retrieved**: 2026-04-23 (filename date reflects download date, not publication)
- **Length**: 12p
- **Read status**: deep-read
- **Primary cluster**: llm-agents
- **All clusters**: llm-agents

## Narrative

This paper compares **Retrieval-Augmented Generation (RAG) approaches** for question-answering over the **GDELT** news dataset, using a case-study subset (the Baltimore Bridge Collapse) plus raw scraped article text. Plain vector-store RAG is known to fail at *global* questions because it only sees unstructured text fragments; the paper studies knowledge-graph (KG) alternatives.

A core contribution is recognizing that **GDELT-GKG2, though marketed as a "Global Knowledge Graph", is natively a relational database** of three linked tables — events (`expert.csv`), articles (`GKG.csv`), and a many-to-many mentions table joining them. The authors define a lightweight **ontology** from this relational schema and convert GKG2 into a *proper* KG (the "DKG"). They benchmark five retrieval pathways: (1) direct graph queries on the DKG; (2) G-Retriever over the DKG; (3) vector-store RAG over GKG2; (4) G-Retriever over an LLM-built KG (LlamaIndex over source articles, the "LKG"); and (5) Microsoft GraphRAG (the "GRKG").

Findings: the **ontology-based KGs are valuable for QA** and answer questions where traditional RAG fails, but **automated extraction of the relevant subgraph is hard**. Conversely, **LLM-generated KGs capture event summaries but lack consistency and interpretability**. The authors recommend a **synergistic ontology + LLM hybrid** for KG construction.

**Cemini relevance**: news-RAG / KG methodology for the librarian — a direct template for whether to serve the wiki via flat vector RAG or a typed knowledge graph, and a cautionary result that purely LLM-extracted graphs trade interpretability for coverage. The ontology-from-relational-schema pattern is reusable for structuring entity pages.

## Snippets

> "We find that while our ontology-based KGs are valuable for question-answering, automated extraction of the relevant subgraphs is challenging. Conversely, LLM-generated KGs, while capturing event summaries, often lack consistency and interpretability. Our findings suggest benefits of a synergistic approach between ontology and LLM-based KG construction." [Source: gdelt 5 3:29.pdf p.1]

> "while the GDELT-GKG2 dataset is not actually natively in the form of a knowledge graph, it is advertised and frequently cited as being one. We believe that we are making a distinct contribution to the research community by converting the very popular GKG2 database into a proper KG." [Source: gdelt 5 3:29.pdf p.3]
