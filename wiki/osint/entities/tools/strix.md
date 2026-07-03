---
title: Strix — AI penetration testing agent
type: entity
tags: [entity, tool, cybersec, pentest, k141]
keywords: [strix, usestrix, Docker, PoC, Apache-2.0, semgrep]
related:
  - sources/eval-multi-wiki-agent-harness-v2-2026-07-03.md
  - sources/3-27-links-re-2.md
  - concepts/wiki-tooling-evaluation.md
maturity: draft
created: 2026-07-03
updated: 2026-07-03
---

## Relations

- @sources/eval-multi-wiki-agent-harness-v2-2026-07-03.md — K141 Adopt row
- @sources/3-27-links-re-2.md — prior mention in links eval

## Raw Concept

K141 Phase-0 on [usestrix/strix](https://github.com/usestrix/strix) — autonomous pentest agent with Docker sandbox + verified PoCs.

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | `usestrix/strix` |
| **License** | **Apache-2.0** (`gh api` 2026-07-03) |
| **Stars / pushed** | ~33.7k★; pushed 2026-07-03 |
| **Verdict** | **Adopt** — cybersec-wiki / laptop audit spikes |
| **Steal** | MapReduce LLM compression for huge semgrep JSON; GitHub Actions scoped review |

**Not prod trading** — isolated Docker required.

Brief: `briefs/cybersec-2026-07-03_k141-strix-adopt.md`

## Snippets

> "Generates verified Proof of Concepts before reporting vulnerabilities." [Source: Multi-Wiki Link Evaluation Plan 1.docx URL 7 (retrieved 2026-07-03)]
