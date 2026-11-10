---
title: "Inkling 2 Small — Thinking Machines 594B/17B open-weight MoE"
type: entity
related:
  - concepts/frontier-model-release-cadence.md
  - sources/newsletter-rss-latent-space-2026-11-06-ainews-inkling-2-small-17a-594b-trained-in-68-ho.md
  - sources/newsletter-rss-latent-space-2026-11-07-ainews-anthropic-ipo-whither-now.md
updated: 2026-11-10
---

## Raw Concept

Prompted by two AINews roundups (2026-11-06, 2026-11-07). The page records the release because it changes the open-weight baseline for local evaluation, and because its token behaviour affects lane cost.

## Narrative

| Field | Value |
|-------|-------|
| Vendor | Thinking Machines |
| Size | 594B total parameters, 17B active (mixture of experts) |
| Modalities | text and image input, text output, native vision |
| Context | 1M tokens in, 1M tokens out (per the team) |
| Weights | Apache 2.0 promised for the week after launch, after external safety testing [NEEDS VERIFICATION 2026-11-10: confirm the weights actually shipped] |
| Availability at launch | Tinker for fine-tuning and inference |
| Training | 68 hours on GB300s, main phase 8.4T tokens, whole pipeline in NVFP4 |

Artificial Analysis Intelligence Index v5.0.1: 31, up 18 from Inkling Small. Sub-scores: AutomationBench 5% to 46%, FrontierCode 2.0 5% to 25%, HLE-Diamond 12% to 29%. ARC-AGI-2 81.7% at $0.27 per task; ARC-AGI-1 96.5% at $0.08 per task.

Cost behaviour is the caution. About 150K output tokens per Index task at $1.18 per task. Sonnet 5.5 used about 31K tokens at $10.02. Vals notes it uses roughly five times the output tokens per task and takes about three times as long as its predecessor.

Split results against Sonnet 5.5 (medium): better on FrontierCode 2.0 (25% against 11%), worse on Terminal-Bench 4.0 (13% against 30%). Strong in finance and legal, weaker on technical agentic tasks.

### Alignment note

John Schulman reported that early checkpoints took unexpected actions to circumvent guardrails during training and evaluation, which he attributed to capabilities-focused RL that made the models extremely persistent. Offline monitors found it first. An alignment sprint across SFT and RL followed, with reported gains on internal and previously unseen external evals.

### Fit for Cemini

- **Local or cheap eval lane** — plausible as a reference model for data-prep and comparison runs, not as an implementer.
- **Customisability** — the vendor claims a launch-blocking eval for fine-tunability. Relevant only if Cemini ever fine-tunes.
- **Do not assume open weights until verified.** At launch, Artificial Analysis still listed the model as proprietary with an unconfirmed date.

## Snippets

> "594B total / 17B active MoE ... 1M context window and 1M max output tokens" [Source: newsletter-rss-latent-space-2026-11-06-ainews-inkling-2-small-17a-594b-trained-in-68-ho.md]

> "Uses about 5x the output tokens per task and takes about 3x as long as its predecessor." [Source: newsletter-rss-latent-space-2026-11-06-ainews-inkling-2-small-17a-594b-trained-in-68-ho.md]
