---
title: 'Architecting an Agentic Ecosystem for Cemini Suites: A Deep Evaluation of Pre-Built Skills'
type: source
tags: [docx, cemini-internal, llm-agents, market-microstructure, quant-finance, crypto, prediction-markets, alt-data]
related:
  - concepts/llm-agent-systems.md
  - concepts/market-microstructure.md
  - concepts/quant-finance.md
maturity: validated
created: 2026-04-23
updated: 2026-04-26
clusters:
  - llm-agents
  - market-microstructure
  - quant-finance
  - crypto
  - prediction-markets
  - cemini-internal
  - alt-data
---

## Relations

- @concepts/llm-agent-systems.md — cluster hub for LLM agent-systems research in the Cemini corpus
- @concepts/market-microstructure.md — Market Microstructure corpus-index hub (Q 2026-04-27)
- @concepts/quant-finance.md — Quantitative Finance corpus-index hub (Q 2026-04-27)

## Raw Concept

- Original title: Architecting an Agentic Ecosystem for Cemini Suites — A Deep Evaluation of Pre-Built Skills
- Authors: Cemini internal authoring team (unsigned)
- Affiliation: Cemini internal
- Type: DOCX, internal skills-evaluation document
- Location: research for cemini/AI Agent Skills for Financial Applications.docx
- Length: long-form
- Retrieved: 2026-04-23
- Publication date: 2026
- Read status: deep-read
- Primary cluster: alt-data
- All clusters: llm-agents, market-microstructure, quant-finance, crypto, prediction-markets, cemini-internal, alt-data
- Flag: **cemini-internal.**

## Narrative

Defines a **5-stage Agent Skill vetting protocol** for Cemini's adoption of third-party Agent Skills and evaluates 7 candidate skills against it. Vetting stages: (1) manifest review (SKILL.md structure and claimed permissions), (2) static code scan, (3) sandbox dry-run, (4) integration test, (5) production promotion with monitoring. Skills evaluated: **ccxt** (crypto exchange library), **predictmax** (prediction-market bot skill), **finance-dcf-builder** (DCF modeling), **async-python-patterns** (async helpers), **playwright-skill** (browser automation), **memory-protocol** (agent memory pattern), **debugging-protocol** (debugging helpers).

Each skill gets a disposition per stage with reasoning. ccxt passes (mature library, standard permissions); playwright-skill flagged for sandbox concerns; others in between. This is a working operational protocol, not research.

Companion document to `3-2-audit-dr` and `3-6-git-1` which flag the Agent Skills security risk in the abstract; this one is the concrete "here's how we vet them" response. Directly actionable. Useful as a blueprint for any organization adopting the Anthropic Agent Skills ecosystem.

## Key findings

- 5-stage skill vetting protocol: manifest review, static scan, sandbox dry-run, integration test, production promotion.
- 7 skills evaluated: ccxt, predictmax, finance-dcf-builder, async-python-patterns, playwright-skill, memory-protocol, debugging-protocol.
- ccxt passes all stages; playwright-skill flagged for sandbox concerns.
- Operational protocol, directly actionable.
- Companion to 3-2-audit-dr (which identifies the risk) — this doc is the response.

## Snippets

- **5-stage protocol** — Manifest review → static scan → sandbox dry-run → integration test → production promotion.
- **ccxt** — Mature crypto exchange library; passes vetting.
- **playwright-skill** — Flagged for sandbox permission concerns.
