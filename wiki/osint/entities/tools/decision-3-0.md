---
title: Decision 3.0 (d3) — open multimodal decision models
type: entity
tags: [models, tools, decision-models, open-weights, llama-cpp, calibrated-probabilities]
keywords: [decision-3-0, vllm-semantic-router, d3, jev-decision-index, calibrated-probabilities, gguf, apache-2-0, perception-test]
related:
  - sources/newsletter-rss-latent-space-2026-10-13-ainews-meta-muse-wonder.md
  - concepts/k290-feeds-wave.md
  - entities/tools/omlx.md
maturity: draft
created: 2026-10-13
updated: 2026-10-13
---

## Relations

- @sources/newsletter-rss-latent-space-2026-10-13-ainews-meta-muse-wonder.md
- @concepts/k290-feeds-wave.md
- @entities/tools/omlx.md

## Raw Concept

**What prompted this page:** the Latent Space AINews issue for 2026-10-10 to 2026-10-12. Released by **vLLM Semantic Router**; Apache-2.0.

## Narrative

A family of **open multimodal decision models** from **0.6B to 27B**, on **Qwen3.5 / Qwen3.8 backbones**. The defining property: they **do not generate free-form text**. They **output calibrated probabilities** for **choice, yes/no, and score** tasks.

**Reported results:** **d3-27B 64.7 text / 71.6 vision**, ranked **#1 on both Jev Decision Index boards**. Zero-shot video on **19,140** Perception Test validation questions: **77.4** (27B) and **70.3** (4B).

**Ecosystem fit is unusually fast:** **llama.cpp integration merged in about 2 hours** (PRs #30378, #30383) with **GGUF builds published** across the size range — `nano`, `mini`, `lite`, `base`, `flash`, `edge` — so local and edge deployment paths exist immediately.

**Open question raised by the community:** whether **sub-4B and sub-1B** decision models can approach 20B+ accuracy, which would unlock **low-latency edge control**. Latency is the deployment metric, not just index rank — compared against Microsoft's **Decision-1 ~85 ms**.

**Why it matters here:** a **decision model that returns a calibrated probability rather than prose** is a different primitive from a chat model. It matches the **typed-judgement** shape this wiki already tracks — a fixed option set with a calibrated score is much easier to **gate, log, and verify** than free text. It also **commoditises** what proprietary decision-model vendors sell; commenters questioned the reported **$7.5B** valuation of Typesafe AI/Jev given open models matching or exceeding its benchmark.

## Snippets

> Decision 3.0: open, multimodal decision models from 0.6B to 27B. Ranks #1 on both Jev Decision Index boards [Source: https://www.latent.space/p/ainews-meta-muse-wonder-and-wonder (retrieved 2026-10-13)]
