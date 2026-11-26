---
title: "ZeroHero — training sub-50M-parameter language agents from scratch (arXiv:2611.34635)"
type: source
related:
  - concepts/process-verified-agentic-search-geo.md
updated: 2026-11-26
read_status: skimmed
maturity: draft
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | ZeroHero: Training Small Language Agents From Scratch |
| Authors | Nikita Sorokin, Zoya Volovikova, Alexey Skrynnik, Aleksandr Panov — Cognitive AI Systems Lab and Moscow Independent Research Institute of AI |
| Type | arXiv preprint |
| arXiv | 2611.34635 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2611.34635-zerohero-training-small-language-agents-from-scr.pdf` |
| Retrieved | 2026-11-26 |
| Read status | skimmed — abstract and introduction read, results not verified |

## Narrative

The question the paper asks is the interesting part: **how much model capacity does a specialised language agent actually need?** ZeroHero trains small language agents from scratch. In each environment a large model acts as the expert and its successful trajectories are collected. Sub-50-million-parameter models are pretrained to predict the expert's responses given the interaction history, then post-trained with PPO on their own interactions. Reasoning alignment adds expert supervision on the language the agent emits alongside its actions.

The paper's own framing cites prior work using 2- to 6-million-parameter models for multi-agent pathfinding, and asks whether fewer than 10 million parameters suffices for an agent policy.

**Relevance to this wiki: not SEO, but real elsewhere.** Nothing here concerns search visibility. The transferable claim is a cost argument for agent lanes: if a task is narrow enough, a very small distilled policy may replace a frontier model call entirely.

That belongs to the `/route` and agent-toolkit lanes, not to this domain. Recorded here because the file arrived in the `seo/` inbox; the routing line below names the real consumer.

`[TENTATIVE]` — the size claims are the authors' and the results were not verified.

## Dead Ends

- Reading this as GEO evidence. A small agent policy has no bearing on whether an engine cites a page.
