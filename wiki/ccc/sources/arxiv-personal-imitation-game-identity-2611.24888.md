---
title: "The Personal Imitation Game — can an LLM impersonate one specific person?"
type: source
related:
  - concepts/agent-personality-file-hermes-openclaw.md
  - concepts/trajectory-level-privacy-audit.md
updated: 2026-11-22
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Who are you? The Personal Imitation Game |
| Author | Muhammad Rizky Wellyanto, Hajara-Yasmin Isa et al. (UIUC) |
| Type | arXiv paper (HCI), 2611.24888 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2611.24888-who-are-you-the-personal-imitation-game.pdf` |
| Retrieved | 2026-11-22 |
| Pages | 19 |
| Read status | read |

## Narrative

This paper is a weak fit for CCC. It is an HCI study of identity, not a harness study. It is filed here because persona agents are a CCC topic and because the result cautions against reading persona fidelity as a product claim.

The authors propose the **Personal Imitation Game**: not "can a machine pass as human", but "can a machine replicate one specific individual in conversation". Thirty participants give a human baseline and identify the signals interrogators use: stylometric features, personality traits, and biographical facts.

They then build an LLM system for one author, trained on ten years of personal digital communication. In a 20-person deception study, interrogators choose the system over the author's own friends in 7 of 10 rounds, and the author over the system in 13 of 20. At this sample size neither rate is distinguishable from chance.

The honest reading is that the study is underpowered. The null is the result. Do not cite it as evidence that persona cloning works.

## Snippets

> "Interrogators choose our system over the author's own friends in 7 of 10 rounds, and the author over our system in 13 of 20; neither rate is distinguishable from chance at this sample size." [Source: arxiv-2611.24888-who-are-you-the-personal-imitation-game.pdf p.1]
