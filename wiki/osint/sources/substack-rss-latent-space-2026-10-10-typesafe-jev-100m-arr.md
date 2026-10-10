---
title: "Latent Space — TypeSafe/Jev at >$100M ARR, $7.5B valuation; decision models become a category (2026-10-10)"
type: source
tags: [source, k288, agents, decisions, jev, typesafe, ccc, model-routing]
keywords: [typesafe, jev, decision-models, openai-decisions-api, perplexity-decider, cloudflare-clef, unsloth, semantic-router, diogo-almeida]
related:
  - concepts/k288-feeds-wave.md
  - concepts/typed-judgement-desk-pattern.md
  - entities/tools/jev-mcp.md
maturity: draft
created: 2026-10-10
updated: 2026-10-10
read_status: read
---

## Relations

- @concepts/k288-feeds-wave.md
- @concepts/typed-judgement-desk-pattern.md
- @entities/tools/jev-mcp.md

## Raw Concept

| Title | [AINews] TypeSafe/Jev at >$100M ARR, $7.5B valuation 3 weeks after launch |
| Source | Latent Space (AINews), Substack |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/newsletter-rss-latent-space-2026-10-10-ainews-typesafejev-at-100m-arr-75b-valuation-3-w.md` |
| Retrieved | 2026-10-10 |
| URL | https://www.latent.space/p/ainews-typesafejev-at-100m-arr-75b |
| Tier | free (RSS teaser) |
| cross-wiki | ccc-wiki |
| read-status | read |

## Narrative

**The typed-judgement pattern from K286 became an industry category in two days.** This is the strongest signal yet that the pattern is correct.

### TypeSafe / Jev

**>$100M ARR and a $7.5B valuation three weeks after launch** (Sequoia reportedly leaked the ARR; "Series AI" announced). The category creator.

### Decision models became a product category — same week

- **OpenAI Decisions API** — three request types (probability a condition is true / pick from a list / score against levels); text + images; GPT-6 Luna; **$0.10/M input, no output charge**; "up to 10× faster" by OpenAI's figure.
- **Microsoft-Decision-1** — for LLM judges and hypothesis screening. An early evaluator notes decision models **still struggle on consistency and complex decisions**.
- **Perplexity `pplx-decider-v1.1-27b`** — claims 94.5% on Decision Bench over 1,071 cases, **$0.017 per 1K decisions**.
- **Cloudflare `clef`** — `clef-flash` is **cheaper than Jev**; clef ~2× faster; weights on Hugging Face.
- **Liquid `d1`**, **vLLM Semantic Router Decision 2.0** (multiple questions, per-option probabilities, one pass), **LangSmith** (Jev as judge returning separate typed answers for difficulty and correctness per trace).

### Train your own

**Unsloth** released a free notebook turning **Qwen3.5-4B into a decision model on 8GB VRAM**; a Qwen3.5-0.8B walkthrough reports **37% → 65% accuracy in 60 steps (~10 min on 4GB)**.

### Why harnesses want this

- **LangChain: routing each task to the cheapest adequate model cut median Open SWE cost per task by 64%.**
- **Apple/CMU SSR** (Selection-based Structured Reasoning) applies the same idea inside agents: six strategies scored by length-normalised log-likelihood in **one batched forward pass sharing the KV cache** — per-turn reasoning latency **−90%**, end-to-end only **−28–54%**.

### Also in the issue

- **Claude Managed Agents dynamic workflows** (public beta): a lead agent writes a phased plan and fans out to **up to 1,000 agents per run**. **Anthropic itself warns** token use can be high.
- **Do agent teams pay off?** (Vals AI) — teams cost **1.8–5.1× more**; only Sol at medium effort improved significantly (**+7.3**). Opus ran sequential waves (~6.8 subagents) with **no significant gain**.
- **Prime Agent rewrote itself in Rust**: 2,000+ agents, 10K+ sandboxes, 200B+ GLM-5.3 tokens — **~13× faster to usable input, 83% less startup memory**.
- **Qwen-Image-2.1-Turbo**, **StepFun Step 5** (600B/27B, 1M ctx), **Gemini 4 Argon** (77.9% DeepSWE v1.1 vs Opus 5.5 74.2%), **Haiku 5.5** (#30 WebDev, 6 pts above Luna at the same price).
- Multi-turn image editing: **Ideogram 4.5 / FLUX 3 leave 95%+ untouched** on small edits; **GPT Image 2.5 Sunburst re-renders most of the frame (~20% unchanged) and drifts**.

### Why it matters here

**This validates K286's typed-judgement desk analysis and sharpens the answer to "are we using our Grok Bots to the full potential?"** The industry has moved: the judge is a **cheap typed call**, and the routing decision is now a first-class product. The **-64% cost** figure and the **Unsloth 4B/8GB** recipe are both directly usable. **No `/route` swap.**

## Snippets

> "TypeSafe announced their 'Series AI' and Sequoia 'leaked' that they crossed 100M ARR in their first week." [Source: substack-rss-latent-space-2026-10-10-typesafe-jev-100m-arr.md]

> "routing each task to the cheapest adequate model cut median Open SWE cost per task by 64%." [Source: substack-rss-latent-space-2026-10-10-typesafe-jev-100m-arr.md]

> "Only Sol at medium effort improved significantly, by 7.3 points … Opus ran sequential waves … with no significant gain." [Source: substack-rss-latent-space-2026-10-10-typesafe-jev-100m-arr.md]
