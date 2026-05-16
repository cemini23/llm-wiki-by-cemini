---
title: "Is Grep All You Need? How Agent Harnesses Reshape Agentic Search (arXiv:2605.15184)"
type: source
tags: [source, arxiv, agent-harness, agentic-search, retrieval, grep-vs-vector, rag, k48]
keywords: [grep-vs-vector-retrieval, agent-harness, agentic-search, longmemeval, rag, tool-calling-paradigm, chronos-harness, retrieval-strategy]
related:
  - concepts/kb-server-retrieval-scaling.md
maturity: validated
read_status: skimmed
created: 2026-05-15
updated: 2026-05-15
---

## Relations

- @concepts/kb-server-retrieval-scaling.md — this paper's central finding (grep ≥ vector retrieval in agentic search) independently corroborates the K47 decision to keep kb-server on brute-force/grep-style retrieval rather than wire in a vector index

## Raw Concept

- **Title**: Is Grep All You Need? How Agent Harnesses Reshape Agentic Search
- **Authors**: Sahil Sen, Akhil Kasturi, Elias Lumer, Anmol Gulati, Vamse Kumar Subbiah (PwC, per the 2026-05-15 sweep)
- **Type**: arXiv preprint — arXiv:2605.15184
- **Submitted**: 2026-05-14
- **Retrieved**: 2026-05-15 (Tier-2 arXiv sweep `@sweeps/2026-05-15.md`, Q1 #1)
- **Read status**: skimmed (abstract-level)

## Narrative

An empirical study comparing retrieval strategies inside LLM agent harnesses. Two experiments:

- **Experiment 1** — grep vs. vector retrieval on a 116-question LongMemEval sample, across a custom harness (Chronos) and provider-native CLI harnesses (Claude Code, Codex, Gemini CLI), testing both inline and file-based tool-result presentation.
- **Experiment 2** — grep-only vs. vector-only retrieval as progressively more unrelated conversation history is mixed in (a distraction-robustness test).

**Headline finding**: across harnesses, **grep generally beats vector retrieval** on accuracy — but overall scores depend strongly on *which harness* and *tool-calling style* is used, even on identical underlying data. Harness architecture is a first-order variable, not a detail.

**Why it matters here**: this is direct external corroboration of the K47 `@concepts/kb-server-retrieval-scaling.md` decision. kb-server retrieves over ~943 documents with brute-force cosine; the benchmark there showed a vector index (turbovec/LEANN) bought nothing at that scale. This paper generalizes the point — at agentic-search scale, grep-style retrieval is competitive with or better than vector retrieval, and the harness matters more than the index.

## Snippets

> "Across Chronos and the provider CLIs, grep generally yields higher accuracy than vector retrieval in our comparisons in experiment 1; at the same time, overall scores still depend strongly on which harness and tool-calling style is used, even when the underlying conversation data are the same."
> — [Source: https://arxiv.org/abs/2605.15184 (retrieved 2026-05-15)]
