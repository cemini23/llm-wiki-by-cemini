---
title: K288 Feeds Wave — decision models as a category, reliable execution, Polymarket V2 (Oct 2026)
type: concept
tags: [k288, feeds, decisions, jev, typesafe, robotics, prediction-markets, crypto]
keywords: [k288, typesafe, jev, decision-models, openai-decisions, unsloth, standard-bots, alphafold, polymarket-v2, pyth-exa]
related:
  - concepts/k288-eval-wave.md
  - concepts/k288-arxiv-wave.md
  - concepts/typed-judgement-desk-pattern.md
  - concepts/ai-industry-trends-2026.md
  - concepts/prediction-market-regulation-2026.md
  - sources/substack-rss-latent-space-2026-10-10-typesafe-jev-100m-arr.md
  - sources/newsletter-rss-latent-space-2026-10-10-standard-bots-reliable-execution.md
  - sources/newsletter-rss-latent-space-2026-10-10-alphafold-bitter-lesson.md
  - sources/substack-rss-wublock-2026-10-10-weekly-project-updates.md
  - concepts/k289-feeds-wave.md
  - sources/newsletter-rss-latent-space-2026-10-12-anthropic-dynamic-workflows.md
maturity: draft
created: 2026-10-10
updated: 2026-10-25
harness_verb: FILE
wire_status: policy_wired
---

## Relations

- @concepts/k288-eval-wave.md
- @concepts/k288-arxiv-wave.md
- @concepts/typed-judgement-desk-pattern.md
- @concepts/ai-industry-trends-2026.md
- @concepts/prediction-market-regulation-2026.md

## Raw Concept

K288 feeds cluster hub. **4 feeds:** Latent Space ×3, WuBlock. Dual-ID **OSINT K288**.

## Narrative

### The headline — the typed-judgement pattern became a category

**TypeSafe/Jev: >$100M ARR, $7.5B valuation, three weeks after launch.** And in the same week, **OpenAI** shipped a **Decisions API**, **Microsoft** shipped Decision-1, **Perplexity** shipped `pplx-decider-v1.1-27b` (94.5% Decision Bench, $0.017/1K), **Cloudflare** shipped `clef` (`clef-flash` cheaper than Jev), and **vLLM** shipped Semantic Router Decision 2.0.

Two numbers to keep: **unsloth turns Qwen3.5-4B into a decision model on 8GB VRAM** (a 0.8B walkthrough: 37% → 65% in 60 steps on 4GB), and **routing each task to the cheapest adequate model cut median Open SWE cost per task by 64%** (LangChain).

This **validates the K286 analysis** (@concepts/typed-judgement-desk-pattern.md) — the pattern was not idiosyncratic; it is where the industry went.

**Also:** agent teams cost **1.8–5.1× more** with little gain (Vals AI); Claude Managed Agents fans out to **1,000 agents/run** with Anthropic's own cost warning; **Prime Agent** rewrote itself with 2,000+ agents.

### Reliable execution — the physical-AI twin

**Standard Bots** ($200M, $1B valuation): **perception is learned, motion and cell logic are conventional code**; short-horizon tasks; **inference on-prem**; data quality over volume ("a few dozen examples" fix an edge case); full-stack co-optimisation. Same doctrine as the typed-judgement desk, from robotics.

### The scaling counterweight

**Pushmeet Kohli (DeepMind) & Sal Candido (Biohub):** the bitter lesson is not enough for biology; find the **right scaling law**; AlphaFold used a **handcrafted architecture** and **did not solve protein folding** (dynamics and disorder remain); **trustworthiness and uncertainty calibration matter more than full interpretability**.

### Crypto

**Polymarket Protocol V2** — full CTF rebuild, ERC-1155 positions, **pUSD** collateral, unified exchange, **OracleAggregator (UMA + Chainlink)**, cross-chain bridge; **mainnet migration Nov 2**. **Pyth** posts ARR $11.49M (+86.5% QoQ) and adopts a **100% buyback rule** — and **partners with Exa to deliver structured market data to AI agents via MCP**, the item most relevant to our tooling. Also: Robinhood Chain tx **−42%**, Aptos reward cut, Starknet mulls an **independent L1**, Orca+Loopscale → **Formation** (defense assets), **Abstract shuts down Dec 15**.

### Distribution

- Decision models → `../Cemini claude code CCC/briefs/2026-10-10_k288-decision-models.md`
- Pyth/Exa MCP → wiki-only + CCC awareness.
- Polymarket V2 → `../Gambling wiki/briefs/2026-10-10_k288-polymarket-v2.md` (**no pm scp**).
- Standard Bots / AlphaFold → CCC awareness.
