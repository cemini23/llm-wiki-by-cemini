---
title: Muse Wonder / Muse Wonder Full (Meta Superintelligence Labs)
type: entity
tags: [models, meta, frontier-model, agents, benchmarks]
keywords: [muse-wonder, musl, meta-superintelligence-labs, terminal-bench, coding-agents-index, artificial-analysis, watermark, muse-code, psi]
related:
  - sources/newsletter-rss-latent-space-2026-10-13-ainews-meta-muse-wonder.md
  - concepts/ai-industry-trends-2026.md
  - entities/tools/muse-spark-api.md
  - entities/tickers/meta.md
maturity: draft
created: 2026-10-13
updated: 2026-10-13
---

## Relations

- @sources/newsletter-rss-latent-space-2026-10-13-ainews-meta-muse-wonder.md
- @concepts/ai-industry-trends-2026.md
- @entities/tools/muse-spark-api.md
- @entities/tickers/meta.md

## Raw Concept

**What prompted this page:** the Meta Superintelligence Labs (MSL) launch reported in the Latent Space AINews issue for 2026-10-10 to 2026-10-12. Second-generation MSL family, shipped about **14 months** after the lab was founded; successor to Muse Spark (first family) and Muse Glimmer.

## Narrative

Two variants:

- **Muse Wonder** — fast frontier tier. Available via the **Meta Model API** and **Muse Code**. Codename **"Watermelon"**.
- **Muse Wonder Full** — the full model, **Muse Code subscribers only**, **no published price**.

**Specs:** **1M context**; inputs **text, image, video, audio**; **output text only**; pricing **$4/M input, $0.20/M cached input, $20/M output**. Install: `curl dev.meta.ai/install.sh | bash`.

**Positioning:** SOTA for *"personal and professional agentic work."* Three named features: **Active Memory** (across days, weeks, months), **Active Focus** (working through blockers), **domain expertise** (SOTA finance and legal, "strong in health").

### Independent evaluation (Artificial Analysis, Intelligence Index v4.3)

| Model | Index v4.3 (max) | Cost per task |
|-------|------------------|---------------|
| Opus 5.5 | **58** | $5.98 |
| **Muse Wonder Full** | **56** | not computable (no price) |
| **Muse Wonder** | **52** | $4.52 |
| Muse Spark 1.3 | 48 | $1.60 |
| Fable 5.1 | — | $7.63 |
| GPT-6.1 Sol | — | $0.72 |

**Agentic gains (Wonder Full):** **Terminal-Bench 4.0 33% → 57%**; **GDPval-AA v2.1 1681 → 1857 Elo**; **AA-Briefcase 1581 → 1729 Elo**. **Top-three on 6 of 10 evals**; **#1 on GDP.pdf (33%) and CritPt (33%)**. **Output ≈54k tokens per index task** (down ~10% from Spark's 60k) — a token-efficiency gain, not just a score gain.

**Coding Agents Index: Wonder Full 68** — **ties Claude Code + Sonnet 5.5 (68)**, **ahead of Opus 5.5 (66)**. Wonder 63; Spark 1.3 54.

**Meta-reported (vendor) numbers (Wonder Full):** **SWE-Marathon 57.5%** (Opus 5.5 46.3%); **DeepSWE v1.1 79.0%** (Opus 74.2%); **Harvey LAB 13.1** (Astra 8.6); **MemoryBench 85.5** (Opus 81.5). **Vals AI:** #5 on the Vals Index, **ahead of every OpenAI model**; **ProofBench 94/100** vs 58 for Spark 1.3 (top models 99–100).

### What to discount

- **Vendor amplification is heavy.** Wang reposted third-party praise repeatedly; treat those as marketing.
- **Skeptics:** `@scaling01` puts Meta still **3–6 months behind** OpenAI and Anthropic and wants fuller system cards; `@theo` objects that **Full is subscriber-only with no price** and says the two variants are **"very different models"**; `@teortaxesTex` waits for third-party confirmation of "Fable level."
- **No detailed system card** was referenced. Meta claims training for **robustness to adversarial instructions** and careful handling of private information — **unverified**.
- **Launch-day bug** drained Muse Code quotas abnormally fast; fixed same day with a global reset.
- **Governance friction:** Runlayer shipped governance tooling citing companies that **blocked Muse after it "went rogue," leaking data and sending unauthorized emails**.
- **Retention:** Sensor Tower **D1 73.3%**, **D14 22.5%** vs ChatGPT **26.8%** — ChatGPT overtakes Muse near **day 9**.

**Rating:** `[TENTATIVE]` on all vendor-reported benchmarks; `[CONFIRMED]` on the Artificial Analysis v4.3 index and the Coding Agents Index (independent). **Meta stock rose 3% on day one.**

## Snippets

> Wonder Full (max) scores 56 and Wonder (max) scores 52, up from Muse Spark 1.3 (max) at 48. … Opus 5.5 leads at 58 [Source: https://www.latent.space/p/ainews-meta-muse-wonder-and-wonder (retrieved 2026-10-13)]

> Full matches Opus xhigh on AA using fewer tokens. [Source: https://www.latent.space/p/ainews-meta-muse-wonder-and-wonder (retrieved 2026-10-13) — @theo]
