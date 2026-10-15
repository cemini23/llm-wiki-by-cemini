---
title: "Receiver Decides — Agent-to-Agent Negotiations"
type: source
tags: [arxiv, agents, negotiation, evaluation]
keywords: [agent negotiation, holder role, endowment, refusal rate, persuasion fine-tuning, role-based evaluation]
related:
  - concepts/k291-game-dev-wave.md
maturity: draft
read_status: read
created: 2026-10-14
updated: 2026-10-14
---

## Relations

- @concepts/k291-game-dev-wave.md — K291 game-dev wave hub

## Raw Concept

Title: Receiver Decides — Agent-to-Agent Negotiations
Authors: Fardeen Sadab, Alif Hasnain, Afsana Shehrin, Md. Azam Hossain, Abu Raihan Mostofa Kamal (Islamic University of Technology)
Type: arXiv preprint (2610.18424)
Location: `research to be indexed/game-dev/arxiv-2610.18424-receiver-decides-agent-to-agent-negotiations.pdf`
Retrieved: 2026-10-14
Read status: read

## Narrative

**1,049 negotiations, fifteen agents.** A REQUESTER raises money from a HOLDER given a $100 endowment.

| Variance in amount transferred | Share |
|---|---|
| Which agent **holds** | **47%** |
| Which agent **asks** | **2%** |
| After dropping extremes | 22% vs 4% |

Frame changes what requesters *write* but not what transfers. **Holders that refuse the opening request lose least**, ranked by turn-1 refusal rate (ρ = −0.73). Fine-tuning Qwen3-8B on a low-refusal persuasion corpus raised holder give-away from **12% to 84%**; distilling two never-losing holders into a 4B student cut losses **95% → 1%**.

**The lesson:** evaluate resource-holding agents **in the holder role**.

## Snippets

> "Knowing which agent holds the money explains 47% of the variance in the amount transferred; knowing which agent asks explains 2%." [Source: arxiv-2610.18424 p.1]

> "Evaluations of agents that hold resources should test them in the holder role, including after persuasion fine-tuning." [Source: arxiv-2610.18424 p.1]

## Dead Ends

- Evaluating only the asker. The paper finds the holder explains ~24× more of the outcome variance.
