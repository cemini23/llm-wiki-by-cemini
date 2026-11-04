---
title: "Context as infrastructure — knowledge compilation for retrieval in agentic systems"
type: source
tags: [source, arxiv, rag, agents, retrieval, harness]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-03
updated: 2026-11-03
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Context as Infrastructure: Knowledge Compilation for Retrieval in Agentic Systems with Harnesses |
| Authors | Zhichang Yu, Baining Cao, Sbaaoui Idriss, Qi Wang, Gangqiang Xu, and others (InfiniFlow) |
| arXiv | 2610.41172 |
| Pages | 13 |
| Read status | skimmed (title page) |

## Narrative

From the InfiniFlow group. The framing: retrieval-augmented generation is becoming **agentic** — a *search harness* writes queries, reads what it finds, and decides what to look for next.

The title's claim is that context should be treated as **infrastructure** rather than as a prompt payload: compiled ahead of time into a structure the harness can query, rather than assembled per turn.

**Why the framing is worth noting here.** This workspace already runs retrieval as infrastructure in effect — a wiki with an index, cross-links, and an ingest discipline. The difference is that its structure is maintained by hand and read by a human-plus-agent, not compiled by a system.

The interesting question the paper implies: what would the wiki look like if it were compiled for a harness rather than written for a reader, and would anything be lost. That is exactly the tension in the wiki-tooling evaluations already on file.

**Caveat.** Only the title page was read. No architecture, benchmark, or result is established on this page.

## Snippets

> "Retrieval-augmented generation is becoming agentic. A search harness writes queries, reads what it finds…" [Source: arxiv-2610.41172 p.1]

## Dead Ends

- **Citing a result.** Title page only.
