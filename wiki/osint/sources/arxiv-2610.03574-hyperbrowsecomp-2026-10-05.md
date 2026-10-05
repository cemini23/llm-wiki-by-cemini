---
title: "HyperBrowseComp — multilingual and multimodal stress test for web-browsing agents"
type: source
tags: [arxiv, browsing-agents, benchmark, multilingual]
keywords: [2610.03574, hyperbrowsecomp, web-search, multimodal, exa]
related:
  - concepts/k282-agent-eval-wave.md
maturity: draft
created: 2026-10-05
updated: 2026-10-05
---

## Relations

- @concepts/k282-agent-eval-wave.md

## Raw Concept

| Field | Value |
|-------|--------|
| Title | HyperBrowseComp: A Multilingual and Multimodal Stress Test for Web-Browsing Agents |
| Authors | Alham Fikri Aji, Faiz Rizki Ramadhan, Zayd M. K. Zuhri, Seung Hun Eddie Han, Ryandito Diandaru, and others (MBZUAI; Mila; Inception AI; Alibaba; AI Singapore) |
| Type | arXiv paper |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.03574-hyperbrowsecomp-a-multilingual-and-multimodal-st.pdf` |
| Retrieved | 2026-10-05 |
| arXiv | 2610.03574 |
| read-status | read |

## Narrative

The paper introduces HyperBrowseComp, a multilingual and multimodal browsing
benchmark. It holds 423 manually authored, human-validated questions across 13
languages, written by native or highly proficient speakers. Each question has a
short, publicly verifiable answer. To find it, an agent must locate obscure
evidence, follow multi-step clue chains, or read heterogeneous sources such as
videos, scanned documents, images, and maps. Easier questions were removed with a
no-internet audit: 77 questions were excluded, leaving 423.

The authors evaluate five frontier models (Gemini 3.1 Pro Preview, Gemini 3.7
Flash, GPT-5.6 Terra, GPT-5.6 Luna, GPT-5.6 Sol) across three search settings:
provider-native search, Exa, and OWL. The strongest configuration reaches 31.68%
accuracy. About 57.68% of questions (244 of 423) get no correct answer from any of
the five native-search models. Video/YouTube is the most common source category
(39.0%), then PDF/book/OCR (29.8%) and image (18.4%). In a human evaluation on 30
questions, participants scored 15 of 30, with a mean time of 89.5 minutes. Human and
model difficulty do not fully overlap. The dataset is released in encoded form to
limit contamination.

For this workspace: this is a direct web-browsing agent evaluation, and it includes
Exa, which is the workspace's canonical external-research path. The multilingual and
multimodal axes stress the harness, not just the model. It is a useful yardstick for
any local browsing or deep-research agent.

[Source: arXiv:2610.03574]

## Snippets

> "We introduce HYPERBROWSECOMP, a multilingual and multimodal browsing benchmark comprising 423 manually authored and human-validated questions across 13 languages, written by native or highly proficient speakers."
[Source: arxiv-2610.03574-hyperbrowsecomp-a-multilingual-and-multimodal-st.pdf p.1]

> "The strongest evaluated configuration achieves 31.68% accuracy, while about 57.68% of questions receive no correct answer from any of the five models evaluated with native search."
[Source: arxiv-2610.03574-hyperbrowsecomp-a-multilingual-and-multimodal-st.pdf p.9]

> "We evaluated 5 web-search enabled frontier LLMs and benchmarked three search integration methods (built-in, Exa, and OWL) to analyze accuracy, cost, and failure cases."
[Source: arxiv-2610.03574-hyperbrowsecomp-a-multilingual-and-multimodal-st.pdf p.3]

> "Video/YouTube is the most frequent source category (39.0%), followed by PDF/book/OCR (29.8%) and Image (18.4%)."
[Source: arxiv-2610.03574-hyperbrowsecomp-a-multilingual-and-multimodal-st.pdf p.6]
