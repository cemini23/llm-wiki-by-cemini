---
title: "ontographia — ontology-gated query compilation (Apache-2.0, 15 stars)"
type: entity
tags: [tool, ontology, cypher, query-compilation, atto, low-maturity]
keywords: [ontographia, intent json, cypher 25, neo4j, schema-constrained, linkml, owl]
related:
  - sources/eval-multi-wiki-link-revenue-v10-11-2026-11-05.md
  - entities/tools/helix-foundry.md
  - "@ccc-wiki/entities/tools/open-ontologies.md"
maturity: draft
created: 2026-11-05
updated: 2026-11-05
---

## Raw Concept

Surfaced by @sources/eval-multi-wiki-link-revenue-v10-11-2026-11-05.md, URL 10, **Extract** tier. Routed to Atto and family-tree.

The question this page answers: **how do you let a model ask a graph question without letting it write the query?**

## Narrative

### What it is

`edgesentry/ontographia`. **Apache-2.0.**

A pipeline that turns an ontology plus an **Intent** JSON into safe, parameterised Cypher for Neo4j 2025+:

```
Ontology → COM → validate(Intent) → AST → Cypher 25 + $params
```

It ingests RDF, OWL, LinkML, YAML, and OBO. A **Rust core** does validation and query generation, with Python and Go bindings and an `otg` CLI.

### Why the architecture is exactly right for Atto

The design rule is one sentence: **the model emits schema-constrained Intent, never raw Cypher**, and the core validates it against the ontology before compilation.

That is the same separation that makes @ccc-wiki/entities/tools/open-ontologies.md's certificates meaningful and that @entities/tools/helix-foundry.md implements from the drafting side. Ontographia implements it on the **query** side.

The consequence for Atto is concrete. A genealogical question — "which siblings were born in the same comune before 1900" — becomes a structured Intent that either validates or does not. The model cannot invent a traversal, cannot reference a relation the ontology does not have, and cannot produce a query that means something different from what it said.

That is stronger than prompting for care.

### Phase-0, 2026-11-05 — the maturity is the problem

**15 stars, 0 forks, 105 commits.** The report does not mention size; that is a very small project to put in a product's query path.

**And the one question that decides Atto usability is unanswered.** The LLM is optional — `ontographia[llm]`, labelled *experimental* — and the README **does not state whether the LLM layer works with a local model or requires a cloud service**. `docs/llm.md` would likely say, and it was not in reach.

For Atto that is not a detail. The deterministic core is local and safe by construction. The moment an LLM turns a question into an Intent, ban 4 applies: if that call goes to a hosted model, a natural-language question about a family record leaves the machine.

**A local model producing Intent JSON is acceptable. A cloud model is not.** Which one it supports is unknown.

### What to take without the dependency

The **compile-don't-generate** contract:

1. The model outputs a **structured intermediate**, not a query.
2. The intermediate is validated against a declared schema.
3. Only a valid intermediate compiles.
4. Invalid means an error, not a best-effort query.

That is implementable over any store, at any size, and it is the part of this project worth having.

### Status

Extract, **pattern strongly, dependency not yet**. Revisit when the LLM layer's locality is documented and the project has more than 105 commits behind it.

## Snippets

> "schema-constrained Intent, never raw Cypher" — README [fetched 2026-11-05]

> "Ontology → COM → validate(Intent) → AST → Cypher 25 + $params" — README [fetched 2026-11-05]

## Dead Ends

- **Assuming the experimental LLM layer runs locally.** Not stated.
- **Dropping a 15-star project into a product query path** on the strength of a correct architecture.
