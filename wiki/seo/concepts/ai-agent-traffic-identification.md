---
title: "AI agent traffic identification — model fingerprinting and the cloaking risk"
type: concept
related:
  - sources/arxiv-capta-identifying-llms-behind-ai-agents-2611.32686.md
  - concepts/generative-engine-optimization.md
  - concepts/agent-ready-website-local-bm.md
  - concepts/retrieval-vs-citation-visibility-geo.md
updated: 2026-11-25
maturity: draft
---

## Raw Concept

This page answers one question: can a website tell which AI model is behind an agent visit, and what does that mean for GEO measurement? The source is @sources/arxiv-capta-identifying-llms-behind-ai-agents-2611.32686.md, a Tsinghua security paper, read 2026-11-25.

## Narrative

**The capability.** A server can identify the LLM behind an AI agent without seeing the model. The method, CAPTA, replaces a CAPTCHA with multiple-choice probes. Models have stable option preferences, so a small set of probes separates them. The paper reports 99.0% mean accuracy with 10 probes across 25 models, and 99.7% across 28 agent–model combinations.

**Why a site would want this.** Two reasons, and they differ in ethics.

1. **Measurement.** Label agent visits by backend model. A GEO audit could then separate traffic from different AI engines instead of counting all "AI" as one bucket.
2. **Selective delivery.** Serve a given model different content than a human sees. The paper calls this cloaking and gives a shopping example: fake promotions for agents, the real page for people.

**The wiki's standing.** The first use is measurement and is acceptable if disclosed. The second use corrupts the evidence base. If an agent answers from a cloaked page, that answer says nothing about the real page. Any GEO claim built on agent transcripts then carries a hidden error term.

**Why it matters for citation audits.** Most GEO measurement reads what an engine says. It assumes the engine read the page. Cloaking breaks that assumption. It is one more reason to treat AI-engine answers as a sample with noise, alongside the sampling noise in @concepts/geo-visibility-measurement.md. See also @concepts/retrieval-vs-citation-visibility-geo.md.

**Practical status for this workspace.** `[OPEN QUESTION 2026-11-25]` The wiki has not tested server-side model labelling on any Cemini site. The paper has no website deployment. Do not treat this as an available tool. Treat it as a known capability and a known risk.

**Scale context from the paper.** AI agent traffic exceeded 6.6 billion requests in one month in Q2 2026 (DataDome, as cited). That figure makes agent-side measurement a material share of web traffic, not a curiosity.

## Snippets

> "a service could selectively deliver manipulated content to AI agents while showing the original content to human visitors. This technique is known as cloaking." [Source: arxiv-2611.32686-capta-identifying-llms-behind-ai-agents.pdf p.1]
