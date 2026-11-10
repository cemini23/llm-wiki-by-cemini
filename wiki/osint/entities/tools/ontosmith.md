---
title: "ontosmith — propose-then-judge fact extraction (MIT, but needs Neo4j and a cloud LLM)"
type: entity
tags: [tool, ontology, extraction, provenance, atto, blockers]
keywords: [ontosmith, flat ontology, proposer, judge, evidence span, neo4j, jev]
related:
  - sources/eval-multi-wiki-link-evaluation-2026-11-10.md
  - entities/tools/jevals.md
  - entities/tools/gbrain.md
maturity: draft
created: 2026-11-10
updated: 2026-11-10
---

## Raw Concept

Surfaced by @sources/eval-multi-wiki-link-evaluation-2026-11-10.md, URL 10, **Extract** tier. Routed to Atto and family-tree.

The question this page answers: **how do you extract facts into a graph without letting the model decide what a fact is?**

## Narrative

### The flow

Starts from **an ontology you define**, not from whatever a model extracts:

1. **Profile** — a deterministic census of the corpus.
2. **Design** — draft a schema; **a human must approve it**.
3. **Build** — cheaper models **propose** candidate facts; rule-based gates check them; a decision model (Jev) **decides** what gets written.
4. **Traceability** — every accepted triple keeps its **evidence passage and provenance**.
5. **Serving** — search, HTTP API, demo app.

The ontology is deliberately **flat**: no class hierarchy, no reasoning. Four domain packs plus a Core baseline.

### Why the propose/judge split is the right shape for Atto

The model never decides what is true. It proposes candidates under a schema a human approved, and a separate decision step accepts or rejects against rules. Nothing enters the graph without an **evidence passage** attached.

That is the same contract as the compile-don't-generate principle in @entities/tools/ontographia.md and the certificate discipline in the open-ontologies work — applied to extraction rather than querying or verification.

### Phase-0, 2026-11-10 — three blockers the report missed

**MIT**, 264 stars, 0.1.9 on PyPI. And then:

| Blocker | Detail |
|---------|--------|
| **Neo4j required** | Live builds need Neo4j 5.x Community and **fail early** without it. The report routes this to Atto explicitly "without Neo4j". That is wrong. Some features run without it (profiling, inspection, verification, the demo), but not a build. |
| **Cloud LLM by default** | One LLM connection is needed for builds, and **no local NLP stack is included**. The default preset routes through **OpenRouter to four models including Claude Haiku and Sonnet**, on a single key. Other providers can be bound, but the shipped default is a cloud call. |
| **Linux only** | "Developed and tested only on Linux, with **WSL2 required on Windows**." macOS is not mentioned. This estate is a macOS laptop. |

**The third is the one that decides it.** Even if Neo4j were installed and a local model bound, the tool has never been tested on the platform it would run on.

### What is worth taking now

The **contract**, which costs nothing:

- A **flat** schema, human-approved before extraction.
- **Proposer** and **judge** as separate roles, with different models.
- **Evidence span mandatory** on every accepted fact.
- **Budget calculated before the build**, not discovered after.

Each of those is a design rule that transfers to `atto-mcp` regardless of whether ontosmith ever runs.

### Status

Extract, **contract only**. Do not attempt an install on macOS without a Linux or WSL2 environment to test in first.

## Snippets

> "Build: cheaper models propose candidate facts. Rule-based gates check them, and a decision model called Jev decides what gets written." [fetched 2026-11-10]

> "Developed and tested only on Linux, with WSL2 required on Windows." [fetched 2026-11-10]

> Neo4j 5.x Community Edition is enough, "and the build fails early if no store is reachable." [fetched 2026-11-10]

## Dead Ends

- **Reading "without Neo4j" as accurate.** Live builds require it.
- **Assuming the default model path is local.** It is OpenRouter → Claude.
- **Installing on macOS.** The project has not been tested there.
