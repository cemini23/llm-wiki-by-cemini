---
title: "Latent Space — AINews: Muse Glimmer + Spark open weights, GPT-5.6-Cyber, harness/tool-calling (2026-08-11)"
type: source
tags: [newsletter, latent-space, k231, ai-engineering, agents, llm, open-weights]
keywords: [Muse Glimmer, Muse Spark 1.2, GPT-5.6-Cyber, Apache 2.0, DFlash, programmatic tool calling, RH bound, Sonnet 5 pricing]
related:
  - concepts/code-as-agent-harness.md
  - concepts/harness-optimization-bench.md
  - entities/tools/openai-codex-security.md
  - sources/newsletter-rss-latent-space-2026-08-07-amd-taalas-muse.md
  - sources/eval-url-revenue-opportunity-2026-08-11.md
maturity: draft
created: 2026-08-11
updated: 2026-08-11
read_status: read
---

## Relations

- @concepts/code-as-agent-harness.md
- @concepts/harness-optimization-bench.md
- @entities/tools/openai-codex-security.md — GPT-5.6-Cyber
- @sources/newsletter-rss-latent-space-2026-08-07-amd-taalas-muse.md
- @sources/eval-url-revenue-opportunity-2026-08-11.md — Stagehand v4 / browser-native abstractions noted here

## Raw Concept

| Field | Value |
|-------|--------|
| Title | AINews — Muse Glimmer and Spark: Open Weights return Personal Superintelligence promise |
| URL | https://www.latent.space/p/ainews-muse-glimmer-and-spark-open |
| sha256 | `fb9797ff47d9126480b2dbbab5caaf8fecce5ca6127cfc4a0198aa51c04310cd` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/newsletter-rss-latent-space-2026-08-11-ainews-muse-glimmer-and-spark-open-weights-retur.md` |
| retrieved | 2026-08-11 |
| read_status | read |

RSS feed body (free tier). Promotes prior `source-stub`. Cross-wiki: CCC + cyber.

## Narrative

**Muse Glimmer (Meta):** 30B dense multimodal agent-focused LLM under **Apache 2.0**; Muse Spark 1.2 weights promised "soon". Optimized for always-on local agents: quantization brings LM under 20GB on 24–32GB systems (KV cache + perception encoder + DFlash speculative drafter); 128K context, ~60GB BF16 / ~18GB 4-bit. Artificial Analysis: Intelligence Index 35 (Qwen3.6-27B 38, Kimi K2.5 36), Openness 44. Weakness: hallucination/knowledge calibration; strong on Tau3-Banking tool-use follow-up. Zuck "Personal Superintelligence" essay: personal agents, creation tools, tutors, scientific advance; risks incl. recursive self-improvement compute allocation.

**Frontier:** Anthropic research Claude improved RH-related lower bound (zeta zeros on critical line 41.6%→67.2%) via 31M-token exploration — AI-assisted theorem search, not solved. OpenAI **GPT-5.6-Cyber** (restricted, approved defenders; Daybreak cyber initiative; found bugs in open-source + Chrome V8). Claude Sonnet 5 intro pricing made permanent $2/M in / $10/M out.

**Harness/tool-calling:** Composio benchmark ran DeepSeek V4 Flash through 4 harnesses over 30 agentic tasks → Pi Agent cheapest + best-performing. Programmatic tool calling (typed Python stubs) ≥ native JSON tool calling in 11/14 models; GPT-5.6 +10.6% over JSON on BFCL v4. Browser Use + Stagehand v4 signal shift to thinner, browser-native agent abstractions. LiteParse: 4ms/200 pages heuristic extraction before OCR/VLM fallback.

**Cross-wiki:** CCC (Muse Glimmer harness value, PTC tool-calling, Stagehand v4, smart-ralph) + cyber (GPT-5.6-Cyber, LLMVault OWASP LLM range context).

## Snippets

> "Meta released Muse Glimmer, a 30B dense, multimodal, agent-focused model under Apache 2.0, plus the promise to release Muse Spark 1.2 weights 'soon.'" [Source: https://www.latent.space/p/ainews-muse-glimmer-and-spark-open (retrieved 2026-08-11)]
