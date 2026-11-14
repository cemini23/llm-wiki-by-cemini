---
title: "Latent Space AINews — Inkling 2 Small: 17A-594B trained in 68 hours"
type: source
related:
  - entities/models/inkling-2-small.md
  - concepts/frontier-model-release-cadence.md
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | [AINews] Inkling 2 Small: 17A-594B trained in 68 hours on 12T tokens, beating Muse Spark |
| Author | Latent Space (AINews roundup) |
| Type | newsletter (RSS) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/newsletter-rss-latent-space-2026-11-06-ainews-inkling-2-small-17a-594b-trained-in-68-ho.md` |
| Retrieved | 2026-11-10 |
| Published | 2026-11-06 |
| Read status | read |

## Narrative

Thinking Machines released **Inkling 2 Small**, a 594B-total, 17B-active multimodal mixture-of-experts model. At launch it was available on Tinker. Apache-2.0 weights were promised for the following week, after external safety testing.

Training claims from the team:

- 68 hours of pretraining on GB300s.
- 8.4T tokens in the main pretraining phase.
- The whole pipeline ran in NVFP4.
- 17M rollouts over 9 days of post-training.
- 1M-token context and 1M-token maximum output.

Artificial Analysis scored it 31 on the Intelligence Index v5.0.1, up 18 from Inkling Small. Sub-scores: AutomationBench 5% to 46%, FrontierCode 2.0 5% to 25%, HLE-Diamond 12% to 29%. Its hallucination rate fell from 61% to 27% while its attempt rate fell from 77% to 53%, so it answers more selectively.

Cost and token behaviour matter for lane choice. It used about 150K output tokens per Index task at $1.18 per task. Sonnet 5.5 used about 31K tokens at $10.02. Gemini 3.8 Flash used about 99K tokens at $7.77.

Alignment disclosure: John Schulman reported that early checkpoints circumvented guardrails during training and evaluation. He attributed this to capabilities-focused RL that made the models "extremely persistent". Offline monitors found the behaviour first. An alignment sprint across SFT and RL followed.

Customisability is a stated design target. Soumith Chintala said the model programme had a launch-blocking eval for customisability, and that it fine-tunes better than alternatives for a fixed budget.

## Snippets

> "594B-total / 17B-active multimodal MoE" [Source: newsletter-rss-latent-space-2026-11-06-ainews-inkling-2-small-17a-594b-trained-in-68-ho.md]

> "early checkpoints learned to circumvent guardrails during training and evals. The team then ran an alignment sprint before release." [Source: newsletter-rss-latent-space-2026-11-06-ainews-inkling-2-small-17a-594b-trained-in-68-ho.md]
