---
title: "Prompt structure redistributes LLM codegen security weaknesses (arXiv 2608.24857)"
type: source
tags: [arxiv, security, codegen, k247, cyber]
keywords: [prompt-engineering, Bandit, CodeQL, CWE, security-weaknesses]
related:
  - concepts/k247-agent-harness-wave.md
  - sources/arxiv-2608.21107-llm-se-security-evidence-map.md
maturity: draft
created: 2026-08-26
updated: 2026-08-26
read_status: read
---

## Relations

- @concepts/k247-agent-harness-wave.md — security eval axis for harness prompts
- @sources/arxiv-2608.21107-llm-se-security-evidence-map.md — SE+security survey sibling (K246)

## Raw Concept

| Field | Value |
|-------|--------|
| Paper | arXiv:2608.24857, "Prompt Structure Redistributes, Not Reduces: An Empirical Analysis of Security-Weaknesses in LLM-Generated Python Code" |
| Authors | Maitreyee Das Urmi, Jessica Pourleyli, Fabio Santos, Glaucia Melo |
| Retrieved | 2026-08-26 |
| File | `arxiv-2608.24857-prompt-structure-redistributes-not-reduces-an-em.pdf` |
| sha256 | `f32cf3425d92ffdd6a9596795422222aa4a63416cc3c616a21d58fbf37e3df81` |
| Dual-ID | **OSINT K247**. **Cyber-primary** brief pointer; no PoC payloads. |

## Narrative

424 security-sensitive Python tasks; GPT-4o and LLaMA 3.1-8B under five prompt variants with progressive structural and security guidance. Evaluated with Bandit and CodeQL on compliance and CWE distributions.

Structured prompting **substantially reduces refusals** (GPT-4o invalid outputs drop from 338/424 to 37–52) but **redistributes** weakness classes rather than uniformly eliminating them. Cyber lab takeaway: security-oriented prompts change the failure surface — measure CWE mix, not only refusal rate. Route cyber brief; no exploit writeups in wiki.

## Snippets

> "Structured prompting substantially reduces refusals … enabling large-scale security analysis, but its effects extend beyond whether detected weaknesses are simply present or absent." [Source: arxiv-2608.24857-prompt-structure-redistributes-not-reduces-an-em.pdf abstract]
