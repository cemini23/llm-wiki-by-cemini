---
title: "APS-RAG — Corrective Agentic Hybrid RAG (arXiv 2607.24663)"
type: source
tags: [source, arxiv, rag, mcp, harness, k198, ccc]
keywords: [APS-RAG, GraphRAG, corrective agent, MCP, APS-Bench]
related:
  - concepts/verifier-deployment-gap.md
  - concepts/code-as-agent-harness.md
  - concepts/cemini-wiki-ingest-workflow.md
maturity: draft
read_status: skimmed
created: 2026-07-28
updated: 2026-07-28
clusters: [k198-ingest]
---

## Relations

- @concepts/verifier-deployment-gap.md
- @concepts/code-as-agent-harness.md
- @concepts/cemini-wiki-ingest-workflow.md

## Raw Concept

| Field | Value |
|-------|-------|
| **Filename** | `arxiv-2607.24663-a-corrective-agentic-hybrid-rag-and-an-operation.pdf` |
| **sha256** | `eea9e7fa8917ca11c62802765865265aa4961c959579cd34633d8622f88ede5c` |
| **arXiv** | [2607.24663](https://arxiv.org/abs/2607.24663) |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2607.24663-a-corrective-agentic-hybrid-rag-and-an-operation.pdf` |

## Narrative

Argonne APS facility RAG: dense+sparse+KG with adaptive RRF, corrective agentic loop, ReAct over **MCP** tools. APS-Bench 50 QA; full Agentic GraphRAG 70.3% vital-nugget recall vs BM25 63.8%. Cross-encoder reranker is the big lever (−32.8% if removed).

**Steal (CCC/Atto):** operations-grounded eval harness + MCP tool layer pattern; do not adopt facility-specific stack wholesale.

## Snippets

> "removing [the cross-encoder] … reduces strict vital recall by 32.8%"
