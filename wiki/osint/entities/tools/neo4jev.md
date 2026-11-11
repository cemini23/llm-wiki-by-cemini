---
title: "neo4jev — bounded graph navigation with Jev (MIT, but hosted-only)"
type: entity
tags: [tool, graph, jev, neo4j, atto, hosted-only]
keywords: [neo4jev, system_one, beam search, noul, choice, typesafe, neo4j, kinship]
related:
  - sources/eval-multi-wiki-repository-revenue-2026-11-11.md
  - entities/tools/jevals.md
  - entities/tools/ontosmith.md
maturity: draft
created: 2026-11-11
updated: 2026-11-11
---

## Raw Concept

Surfaced by @sources/eval-multi-wiki-repository-revenue-2026-11-11.md, URL 13, **Extract** tier. Routed to Atto, family-tree, and CeminiParlays.

The question this page answers: **how do you walk a graph without asking an LLM to write a query?**

## Narrative

### What it does

A demo application from jexp that walks a Neo4j graph **one relationship hop at a time**. Instead of free-text generation, it uses TypeSafe's `system_one` structured-decision API:

- At each node, the outgoing relationships are offered as **choices**, and the API returns **a probability for each**.
- It adds **beam search**, and asks "has the goal been reached?" **in the same call**.
- Goal modes: free text, a specific target node, or a path pattern.
- Reusable library, three Jupyter notebooks, a Streamlit app, and `neo4j-viz` display.

**MIT.**

### Why the shape is right for Atto

Kinship disambiguation is a graph walk with a small branching factor. "Is this Giuseppe the son of that Giuseppe" is a choice among a handful of candidate edges, each with a confidence — not a traversal to be written in Cypher and hoped over.

Asking for a **probability distribution over the actual outgoing edges** is a far stronger constraint than generating a query. The model cannot invent a relationship that does not exist in the graph, because it only ever chooses from the edges in front of it.

That is the same rule `ontographia` enforces by compiling Intent against an ontology, reached from the graph side.

### Phase-0, 2026-11-11 — it is not local

**This is the finding that decides the routing.** The report lists it alongside open-weight local Jev replicas. The README is unambiguous:

> It **"is not local. It relies on a remote TypeSafe `system_one` service and needs a `TYPESAFE_API_KEY`."** Without the key "each call is attempted and fails", and the notebooks continue on **"explicitly labelled stand-in answers"**.

It also **requires Neo4j** — defaulting to the public Companies demo graph, schema-agnostic otherwise.

So two dependencies, one of which is a cloud call on every hop.

### The distinction that matters

`jevals` (catalogued 2026-11-10) is the **same Jev family** and documents an **offline backend**: Laya, in-process on Apple Silicon, no key. `neo4jev` is the opposite.

**Same family, opposite locality.** Do not generalise from one to the other — check the backend in each.

### Status

Extract, **design reference only**. The pattern is worth taking; the implementation cannot run under Atto's ban 4 and needs Neo4j besides.

## Snippets

> It relies on a remote TypeSafe `system_one` service and needs a `TYPESAFE_API_KEY`. [fetched 2026-11-11]

> Without the key, each call is attempted and fails, and the notebooks and app continue on "explicitly labelled stand-in answers" rather than model output. [fetched 2026-11-11]

## Dead Ends

- **Assuming it runs locally because `jevals` does.** Different backend.
- **Treating the fallback output as a result.** It is labelled stand-in text, not model output.
