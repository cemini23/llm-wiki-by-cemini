---
title: "helix-foundry — local ontology drafter with a human promotion gate (Apache-2.0)"
type: entity
tags: [tool, ontology, provenance, atto, local-first, apache-2.0]
keywords: [helix foundry, ontology agent, promotion gate, citation lineage, helixdb, loopback]
related:
  - sources/eval-multi-wiki-repository-revenue-2026-11-04.md
  - entities/tools/lexifina-global-law.md
  - "@ccc-wiki/entities/tools/open-ontologies.md"
maturity: draft
created: 2026-11-04
updated: 2026-11-04
---

## Raw Concept

Surfaced by @sources/eval-multi-wiki-repository-revenue-2026-11-04.md, URL 16, **Extract** tier, high confidence. Routed to Atto, family-tree, and Collectibles.

The question this page answers: **how does a local ontology drafter keep a human in the loop, and what does it send out?**

## Narrative

### What it is

`HelixDB/helix-foundry`. **Apache-2.0** across the site, the backend, its three Docker images, and HelixDB itself. 2.0k stars, 360 commits.

It joins a company's databases, tools, and documents, has an agent **propose an ontology** covering that data, and loads the result into HelixDB as a single graph. You browse the graph and ask questions with **cited answers**.

Two properties make it interesting for Atto:

1. **A mandatory human version-promotion gate.** An agent-proposed ontology does not become the live one by itself.
2. **Row and quote provenance.** Answers cite the row or quote they came from, so a claim traces to a record.

That is close to what `atto-mcp` needs for citation lineage — and it is the same shape as @ccc-wiki/entities/tools/open-ontologies.md's blast-radius certificates, approached from the drafting side rather than the verification side.

### Phase-0, 2026-11-04 — the finding that decides the routing

**Local binding is confirmed.** The web UI binds loopback and accepts only `localhost:3000`; the data store listens on `127.0.0.1:8333`. The README adds an explicit warning: **"Never expose it through a reverse proxy, tunnel or port forward."**

**Local binding is not the same as offline.** The README states:

> Foundry will use Claude or OpenAI if your shell has the corresponding API key. Otherwise it falls back to a local Ollama, LM Studio or any OpenAI-compatible server you point it at.

So on a machine where `ANTHROPIC_API_KEY` or `OPENAI_API_KEY` is exported — which is the normal state of this workspace — **family records would go to a frontier model by default**.

That is a direct conflict with Atto's ban 4, and it is the kind of conflict that does not announce itself. The tool looks local; the binding is loopback; the traffic is not.

### The conditions for use

All four, not any one:

1. **No cloud model keys in the environment** when it runs. Not "unset in the shell" — verified absent for the process.
2. **A local endpoint pinned explicitly.** Ollama or an OpenAI-compatible server on loopback.
3. **Synthetic Rossi and 900-series fixtures only** for any evaluation — never real `Desktop/family/` records, which is Atto's standing rule.
4. **No reverse proxy, tunnel, or port forward.** The README's own warning.

### What to take without the dependency

Even if the tool is never run, two of its ideas transfer:

- **Promotion as an explicit human act.** An agent drafts; a person promotes. That maps onto Atto's `truth.ged` human gate exactly.
- **Answers carry their row or quote.** A citation is not a reference to a document, it is a pointer to the evidence inside it.

### Status

Extract. The provenance and promotion patterns are the asset. Running it against real family data is **not** sanctioned without the four conditions above.

## Snippets

> "Everything in this repository, the site and the backend, is Apache 2.0." — README [fetched 2026-11-04]

> "Never expose it through a reverse proxy, tunnel or port forward." — README [fetched 2026-11-04]

> "Foundry will use Claude or OpenAI if your shell has the corresponding API key." — README [fetched 2026-11-04]

## Dead Ends

- **Assuming loopback binding means nothing leaves the machine.** The model call is the outbound path, not the UI.
- **Running it on `Desktop/family/research/` with a key in the environment.** That is the exact leak the Atto boundary exists to prevent.
