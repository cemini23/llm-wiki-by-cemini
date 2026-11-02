---
title: "agentdiscoverability.com/track — Agent Tool Optimization (ATO) framework"
type: entity
tags: [tool, seo, geo, mcp, discovery, atto, saas]
keywords: [agent tool optimization, ato, claude connector, chatgpt plugin, mcp schema, found picked positioned]
related:
  - sources/eval-multi-wiki-link-revenue-v10.10-batch-b-2026-11-01.md
  - "@seo-wiki/concepts/agent-first-web-atml-framework.md"
maturity: draft
created: 2026-11-01
updated: 2026-11-01
---

## Raw Concept

Surfaced by @sources/eval-multi-wiki-link-revenue-v10.10-batch-b-2026-11-01.md, URL 8, **Extract** tier. Routed to Atto and `atto-mcp`, with a secondary SEO wiki routing.

The question this page answers: **how does a tool get picked by an agent that is choosing among tools?**

## Narrative

### What it is

A benchmark and registry platform. It tracks agent-tool directories daily: more than 8 495 ChatGPT Plugins with about 1 020 added in seven days, plus Claude Connectors, Grok, Muse, and Gemini. It is proprietary SaaS. A public brand and domain score check is free; managed and agency tiers are paid.

### The framework

**Agent Tool Optimization (ATO)**, in three stages:

| Stage | Question |
|-------|----------|
| **Found** | Can the agent discover the tool at all? |
| **Picked** | Given several candidates, does the agent choose this one? |
| **Positioned** | Within the answer, where does the tool appear? |

Measured over trailing 30-day intent runs, so it is behavioural, not a static lint score.

### Why this is a different problem from SEO

Classic SEO optimises for a human reading a results page. ATO optimises for a model deciding which function to call. The selection signal is the tool's **name, description, and schema**, because that is all the model sees when it builds a tool call.

The concrete rules the report extracts:

- **Tool name alignment.** The function name should match the words a user would actually say, not the internal module name.
- **Long description matching.** The long description should contain the phrasing of real customer queries.
- **Structured outputs.** Return typed structures the model can reason over rather than prose.

### Applying it to atto-mcp

Atto sells Concierge at $2 500 and above, and a $499–$899 kit range. If a buyer finds Atto by asking an assistant a genealogy question, then the assistant's tool selection is a sales channel. `atto-mcp` should be legible to that selection:

| Rule | Atto action |
|------|-------------|
| Name alignment | Expose tool names in the vocabulary of the question — place lookup, record search, archive lookup — not internal engine names. |
| Description matching | Put the customer phrasing in the long description: what a person researching Italian ancestry actually types. |
| Structured outputs | Return typed records, not formatted prose. |

This connects to the shipped Atlas CLI contract in @concepts/historical-jurisdiction-atlas.md, which already returns JSON with defined exit codes — that is the right shape for an agent-facing surface.

### Caveat

The source is a vendor that sells optimisation for its own index. The three-stage framework is sound and portable. The **scores** are the vendor's own. Extract the framework; do not treat a score as an independent measurement.

### Phase-0 status

**Not run.** Proprietary SaaS with no repository. The methodology is extracted from the report's description.

### Status

Extract, **framework only**. No account, no paid tier, nothing installed.

## Snippets

> "Introduces the 'Agent Tool Optimization' (ATO) framework (Found -> Picked -> Positioned across trailing 30-day intent runs) and concrete MCP schema optimization rules (Tool name alignment, Long description update matching customer…)" — report, URL 8

## Dead Ends

- **Treating the vendor's score as independent.** The platform sells optimisation for the index it scores against.
