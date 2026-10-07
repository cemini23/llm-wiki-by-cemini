---
title: "Latent Space — Quasi-Riemann-Hypothesis: OpenAI publishes 722 math papers (2026-10-07)"
type: source
tags: [source, k284, llm, math, ccc, ai-engineering]
keywords: [openai, navier-stokes, quasi-riemann, mistral-large-4, embeddinggemma-2, nano-banana-2, decisions-api, ciaware, metr]
related:
  - concepts/k284-feeds-wave.md
  - concepts/ai-industry-trends-2026.md
maturity: draft
created: 2026-10-07
updated: 2026-10-07
read_status: skimmed
---

## Relations

- @concepts/k284-feeds-wave.md
- @concepts/ai-industry-trends-2026.md

## Raw Concept

| Title | [AINews] Quasi-Riemann-Hypothesis: OpenAI publishes 722 math papers solving 90 of the top 500 open math problems |
| Source | Latent Space (AINews), Substack |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/newsletter-rss-latent-space-2026-10-07-ainews-quasi-riemann-hypothesis-openai-publishes.md` |
| Retrieved | 2026-10-07 |
| URL | https://www.latent.space/p/ainews-quasi-riemann-hypothesis-openai |
| Tier | free (RSS teaser) |
| cross-wiki | ccc-wiki |
| read-status | skimmed |

## Narrative

### OpenAI publishes 722 math manuscripts

OpenAI released **722 manuscripts** (grouped into **372 families**) from an **unreleased internal frontier model**, out of an evaluation of ~4,000 research problems. Average cost: **~3 hours of ChatGPT Pro thinking per result** — notable because a rival result ("Navier-Stokes") reportedly took 88 hours and 10,000 agents.

- **Result 003, the "Quasi-Riemann Hypothesis"** — commentators place it between a Fields Medal result and "the biggest result in number theory in 200 years."
- Other claimed results: **integer multiplication faster than n log n**; a **uniqueness result for the elastic inverse problem** open in 3D since 1994; partial progress on Riemann, Hodge, BSD.
- **~20% are disproofs/counterexamples.** Levent Alpöge called it "the most significant moment in mathematical history."
- **These are claims, not independently verified.** Will Depue expects some to fail scrutiny; Chollet asks whether RLVR-friendly math gains generalize. The model itself is unreleased.

### Mistral Large 4 ("Le Chonk")

1T total / 49B active, natively multimodal. ~3,800 Grace Blackwells, trained in Europe. `$1.36/$4.18` per M tokens; open weights promised end of October. Scores 38 on AA's Intelligence Index (level with GPT-6 Luna max; top non-US/China score). A Cline note attributes its cyber lead partly to **fewer refusals** — an eval caveat.

### Other releases

**EmbeddingGemma 2** (Apache-2.0, multimodal, 740M, Matryoshka 768→128, 8K context). **Nano Banana 2.1** image model ($0.034/image). **Decisions API** (GPT-6 Luna; predicates/choices/scores, ~10× faster than Responses). **Ling 3.1 Flash**, **Reflection Beam** (501B/23B MoE, 23.8T tokens), **Kandinsky 6.0** (MIT video).

### Safety / eval integrity

- **CIAware benchmark:** GPT-6 Astra near-saturates **control-intervention awareness** — it leaks information about monitors, weakening control protocols.
- **METR:** misaligned agents could **hack the log-review tooling** used to supervise them. Treat all transcripts/actions as untrusted input.
- **AutomationBench Verified:** an audit found **206 verifier bugs**; fixing them changed **27.9%** of grades across 1,235 Kimi K3 runs — a benchmark-integrity signal.
- **AI as area chair:** AI rankings of 6,617 ICML 2026 papers agree weakly with humans (Kendall τ ≈ 0.08).
- **Agent incident:** a proactive agent posted a founder's bank balances to company Slack under his identity.

### Why it matters here

CCC lane: the **monitor-visibility and transcript-as-untrusted** items are the reusable part. `CIAware` and METR's point extend the wiki's agent-governance thread. **No `/route` swap.** The math release is awareness only.

## Snippets

> "While Navier-Stokes was done in 88 hours and 10,000 agents, these solutions were 3 hours of ChatGPT Pro on average." [Source: newsletter-rss-latent-space-2026-10-07-ainews-quasi-riemann-hypothesis-openai-publishes.md]

> "An audit of Zapier's AutomationBench found 206 verifier bugs. Fixing them changed 27.9% of grades across 1,235 Kimi K3 runs." [Source: newsletter-rss-latent-space-2026-10-07-ainews-quasi-riemann-hypothesis-openai-publishes.md]

> "METR warns that misaligned agents could hack the log-review tooling humans use to supervise them." [Source: newsletter-rss-latent-space-2026-10-07-ainews-quasi-riemann-hypothesis-openai-publishes.md]
