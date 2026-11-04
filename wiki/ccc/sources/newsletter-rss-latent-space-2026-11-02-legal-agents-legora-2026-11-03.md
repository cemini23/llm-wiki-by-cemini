---
title: "Latent Space — Legora: building legal agents you cannot see the data for"
type: source
tags: [source, newsletter, agents, evaluation, legal-tech, privacy]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-03
updated: 2026-11-03
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Building Legal Agents When You Can't See the Data — Jacob Lauritzen, CTO of Legora |
| Source | latent-space |
| Published | 2026-11-02 |
| Read status | skimmed — episode summary |

## Narrative

**A hard evaluation problem, stated cleanly:** Legora cannot read a single trace of what its agent does for a lawyer, because the data belongs to the law firm's clients. How do you build and test an agent when you cannot see its work?

### The company

Founded in a Stockholm basement with ChatGPT, Swedish law, and a search tool. Now: drafts and edits Word documents, reviews 10,000 contracts in one table, runs due diligence, and coordinates work between lawyers, clients, and other agents.

- **$100 million ARR** in April, less than 18 months after launch.
- **1,800+ customers.**
- **$550M in March at $5.55bn**, then **$550M in October at $8.8bn**.
- Five acquisitions this year, including Wexler.

### The three things worth taking

**1. Test environments built like worlds.** Three engineers and three lawyers construct test environments **modelled on customers' work** — explicitly compared to the "worlds" used in reinforcement learning. When you cannot see production, you build a synthetic production that resembles it and iterate there.

That is the only viable answer to the constraint, and it costs a standing team: three engineers plus three lawyers is a permanent function, not a project.

**2. About 60% of legal work is done well by current models.** The remaining 40% needs a smarter model, not a better harness. That is a useful split to hear from an operator — it says the ceiling is model capability in a domain where the harness is already mature.

**3. They resisted a model picker for years, then added one.** The reversal is more informative than the decision. A model picker is an admission that no single model wins at everything, and that the customer's task mix varies enough to matter.

### Why it is filed here rather than in a legal wiki

The transferable content is **the evaluation-under-opacity pattern**, not the legal domain. Any agent working on data the builder cannot see — and that includes anything running over private vaults or client files — faces the same problem and needs the same answer: a synthetic world built with domain experts, maintained as a standing cost.

That is directly relevant to how this workspace evaluates anything touching private material.

**Caveat.** Episode summary only, single source. The 60% figure is the CTO's estimate, not a measurement.

## Snippets

> "Legora can't read a single trace of what its agent does for a lawyer. The data belongs to the law firm's clients." [retrieved 2026-11-03]

> "How three engineers and three lawyers build test environments modeled on customers' work, much like the 'worlds' used in reinforcement learning" [retrieved 2026-11-03]

## Dead Ends

- **Citing 60% as a measured threshold.** It is an operator's estimate.
