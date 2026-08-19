---
title: "Latent Space — Glean model routing (2026-08-18)"
type: source
tags: [newsletter, ccc, k242, routing]
keywords: [glean, model-routing, openrouter, stripe]
related:
  - concepts/llm-routing-deepseek-openrouter-failover.md
  - entities/tools/easy-agent.md
  - entities/tools/cursor-route.md
  - sources/newsletter-rss-latent-space-2026-08-17-stripe-openrouter.md
  - sources/newsletter-rss-latent-space-2026-08-19-memory-prices.md
  - sources/newsletter-rss-pragmatic-engineer-2026-08-18-eng-leader-exit.md
  - sources/substack-rss-klement-2026-08-19-hyperscalers-slm.md
maturity: draft
created: 2026-08-19
updated: 2026-08-19
read_status: read
---

## Relations

- @concepts/llm-routing-deepseek-openrouter-failover.md — enterprise routing demand ≠ new `/route` worker
- @entities/tools/easy-agent.md — harness/routing Extract
- @entities/tools/cursor-route.md — public MIT CLI; do not swap `/route`
- @sources/newsletter-rss-latent-space-2026-08-17-stripe-openrouter.md — Stripe/OpenRouter $7B already K241
- @sources/newsletter-rss-latent-space-2026-08-19-memory-prices.md — same-week DRAM spike
- @sources/newsletter-rss-pragmatic-engineer-2026-08-18-eng-leader-exit.md — operator attention scarce
- @sources/substack-rss-klement-2026-08-19-hyperscalers-slm.md — SLM vs cloud cost

## Raw Concept

| Field | Value |
|-------|--------|
| File | `newsletter-rss-latent-space-2026-08-18-frontier-model-cost-and-open-weights-popularity.md` |
| sha256 | `5793d0a62cd0e9cd1bde47ccbd789f3babc37d9c1f0d2d06c5551f4910aefc4f` |
| URL | https://www.latent.space/p/glean-model-routing |
| retrieved | 2026-08-18 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/newsletter-rss-latent-space-2026-08-18-frontier-model-cost-and-open-weights-popularity.md` |

## Narrative

Frontier cost plus open-weight popularity is turning **model routing** into a product. Stripe/OpenRouter $7B is already K241 — this piece adds **Glean** as an enterprise meta-harness: $7.2B last round, **$300M ARR** (3× in 15 months). Steal: Glean's job is to pick a model **per task, or skip the LLM** (Jain: don't use an LLM to add two numbers). Three selection layers — user pick, admin limits, automatic mode — and customers pick automatic **mostly for cost**. Gentilcore: Glean claims **~$0.45/task vs $1.84 Claude Cowork** (4×). Per-token price-ups plus longer tasks can 10–20× per-user spend vs last year. **Do not swap Cemini `/route` or PATH `claude-ds`** because Glean exists; treat this as CCC backlog that routing is a product surface, not a reason to fork the worker. [TENTATIVE] Glean cost claims are vendor-sourced.

[Source: https://www.latent.space/p/glean-model-routing (retrieved 2026-08-18)]
