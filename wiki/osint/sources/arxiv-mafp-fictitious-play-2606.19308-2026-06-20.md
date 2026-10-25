---
title: "MAFP — Multi-Agent Fictitious Play for LLM decisions — arXiv 2606.19308"
type: source
tags: [source, arxiv, llm-agents, game-theory, poker, k124]
keywords: [2606.19308, MAFP, fictitious play, stance entanglement, Nash, tournament strength]
related:
  - concepts/multi-agent-fictitious-play-llm.md
  - concepts/poker-arena-multi-axis-cognitive-profile.md
  - concepts/team-zero-sum-games-complexity.md
  - concepts/extensive-form-games-stochastic-action-sets.md
  - concepts/garip-running-average-self-play.md
  - sources/arxiv-garip-self-play-2606.22688-2026-06-23.md
  - sources/arxiv-2608.15258-self-fictitious-play-2026-08-18.md
  - sources/arxiv-emagnet-parameter-space-ema-2606.23995-2026-06-25.md
  - sources/arxiv-equilibrium-internal-transfers-seate-2606.20960-2026-06-25.md
  - sources/arxiv-moral-geometry-nash-kantian-2606.21967-2026-06-25.md
maturity: draft
read_status: read
created: 2026-06-20
updated: 2026-10-25
clusters: [llm-agents, rl-marl]
---

## Relations

- @concepts/multi-agent-fictitious-play-llm.md — K124 synthesis
- @concepts/poker-arena-multi-axis-cognitive-profile.md — poker eval + equilibrium baselines
- @concepts/team-zero-sum-games-complexity.md — equilibrium hardness context

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Enhancing Decision-Making with Large Language Models through Multi-Agent Fictitious Play |
| **Authors** | Leyang Shen, Yang Zhang, Xiaoyan Zhao, Chun Kai Ling, Tat-Seng Chua (NUS) |
| **arXiv** | 2606.19308 (17 Jun 2026) |
| **sha256** | `110811ad6c9bb4228da980278b1ec31c9ce5d58396eb45db690e067f4bfd1ad1` |
| **Repo** | none public at ingest |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2606.19308-pdf-enhancing-decision-making-with-large-languag.pdf` |
| **Retrieved** | 2026-06-20 (daily digest inbox) |
| **Read status** | read (abstract + §1 + evaluation framing) |

## Narrative

Identifies **stance entanglement** — decision complexity where stakeholder choices are mutually dependent — distinct from **execution complexity** addressed by divide-and-conquer MAS.

**MAFP:** decompose stances into agents; iterate **fictitious play** — each agent best-responds to empirical mixture of others' past decisions. Two operators: aggregation (empirical mixture) and best-response (utility-maximizing policy in language space).

**Evaluation:** 13 scenarios (competitive games + negotiation); metrics **tournament strength** (avg payoff vs field) and **robustness** (worst-case vs adaptive adversaries). Outperforms single-round and multi-round baselines on both axes [TENTATIVE — paper claims].

**Cemini posture:** **REFERENCE / steal-from** — poker `decide()` can treat villain archetypes (lag/maniac/rock) as stance agents; offline fictitious-play rounds for preflop chart refinement before Arena submit. No public repo → do not Adopt.

## Snippets

> "We characterize this challenge as stance entanglement, a form of decision complexity distinct from execution complexity." [Source: arXiv:2606.19308 abstract (retrieved 2026-06-20)]

> "MAFP iteratively updates each agent's decision by best responding to the empirical mixture of other agents' past decisions." [Source: arXiv:2606.19308 abstract (retrieved 2026-06-20)]

## Dead Ends

- Open-ended language policies ≠ symbolic poker action space — requires constrained best-response operator.
- No code release — pattern brief only.
