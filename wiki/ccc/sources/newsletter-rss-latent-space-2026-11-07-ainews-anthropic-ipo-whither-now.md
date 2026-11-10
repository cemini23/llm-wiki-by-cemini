---
title: "Latent Space AINews — Anthropic IPO and the open-weight week"
type: source
related:
  - concepts/frontier-model-release-cadence.md
  - entities/models/inkling-2-small.md
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | [AINews] Anthropic IPO: Whither Now? |
| Author | Latent Space (AINews roundup) |
| Type | newsletter (RSS) |
| Location | `research to be indexed/newsletter-rss-latent-space-2026-11-07-ainews-anthropic-ipo-whither-now.md` |
| Retrieved | 2026-11-10 |
| Published | 2026-11-07 |
| Read status | read |

## Narrative

A market and model roundup. The ccc-relevant items are the model releases and one eval anomaly.

Market context: Anthropic had a $100B year-end run-rate target and was at $80B. The AI market drawdown deepened to about -10% on Nasdaq.

Model releases:

- **Inkling 2 Small** (Thinking Machines) — repeat coverage. ARC-AGI-2 81.7% at $0.27 per task; ARC-AGI-1 96.5% at $0.08 per task. Code Arena WebDev 1648, top US open model once weights ship.
- **Kimi K3.1 Pro** (Moonshot) — 2.8T parameters, 104B active. Ranked first among open models in Agent Arena. Day-0 SGLang megakernel support. Scored 9.9% on WeirdML, behind Haiku 5.5.
- **ERNIE-5.5-Flash-Base** (Baidu) — 280B MoE, 14B active, trained on 33.5T tokens. Only 6 of 43 layers keep token-level full context; the rest compress every 128 tokens into one KV entry, with up to 1M context.
- **Tencent Hy4** — top Chinese model in Agent Arena at $0.57 median cost per task.
- **Meta Muse** — new specialised models bring Active Memory and Active Focus. Meta claims 2.4x less forgetting and 67% better recovery when constraints change.

One eval anomaly is worth recording. Vals found Inkling 2 Small swearing in 50 of 2,655 benchmark runs. The profanity clustered late in long runs, alongside repeated failed recoveries. That is a harness and context symptom surfacing in output, not a style quirk.

Artificial Analysis also reported an endpoint fidelity finding: nearly one in four of over 100 serverless endpoints score below the self-hosted reference deployment. Endpoint choice is part of the measurement.

## Snippets

> "Nearly 1 in 4 of 100+ serverless endpoints score below the self-hosted reference deployment." [Source: newsletter-rss-latent-space-2026-11-07-ainews-anthropic-ipo-whither-now.md]

> "Vals found the model swearing in 50 of 2,655 benchmark runs. The profanity clustered late in long runs, alongside repeated failed recoveries." [Source: newsletter-rss-latent-space-2026-11-07-ainews-anthropic-ipo-whither-now.md]
