---
title: "AINews: The No AI Slop manifesto — coding-agent index, effort economics, eval integrity"
type: source
maturity: draft
related:
  - concepts/eval-integrity-minimum-standards.md
  - concepts/reasoning-effort-calibration.md
  - concepts/decision-model-hybrid-agent-routing.md
  - entities/tools/claude-code.md
  - entities/tools/openai-codex-cli.md
  - entities/models/claude-fable-5-2.md
  - sources/newsletter-rss-latent-space-2026-06-30-ahmad-osman-on-why-local-ai-is-catching-up.md
  - sources/newsletter-rss-latent-space-2026-06-30-ainews-not-much-happened-today.md
  - sources/newsletter-rss-latent-space-2026-07-01-aiewf-daily-dispatch-loops-software-factories-fo.md
  - sources/newsletter-rss-latent-space-2026-07-01-ainews-sonnet-5-today-and-fable-5-tomorrow.md
  - sources/newsletter-rss-latent-space-2026-07-01-autoresearch-the-feedback-loop-behind-self-impro.md
  - sources/newsletter-rss-latent-space-2026-07-01-forward-deployed-engineers-and-the-future-of-sof.md
  - sources/newsletter-rss-latent-space-2026-07-01-how-cursor-deploys-ai-inside-the-enterprise.md
  - sources/newsletter-rss-latent-space-2026-07-01-the-coolest-diffusion-research-isnt-in-llms-evan.md
  - sources/newsletter-rss-latent-space-2026-07-01-warp-ceo-zach-lloyd-on-why-software-factories-ar.md
  - sources/newsletter-rss-latent-space-2026-07-02-aiewf-daily-dispatch-autoresearch-and-the-tensio.md
  - sources/newsletter-rss-latent-space-2026-07-02-ainews-not-much-happened-today.md
  - sources/newsletter-rss-latent-space-2026-07-02-the-website-of-the-future-may-assemble-itself-fo.md
  - sources/newsletter-rss-latent-space-2026-07-03-aiewf-daily-dispatch-the-great-loops-debate-and.md
  - sources/newsletter-rss-latent-space-2026-07-07-ainews-the-field-guide-to-fable.md
  - sources/newsletter-rss-latent-space-2026-07-28-codex-chatgpt-work.md
  - sources/newsletter-rss-latent-space-2026-10-21-ai-for-the-fortune-2000-how-tenex-builds-an-ai-n.md
  - sources/newsletter-rss-latent-space-2026-10-21-ainews-deepseek-deepinfer-open-source-sota-infer.md
  - sources/newsletter-rss-latent-space-2026-10-22-ainews-openais-patch-the-planet-program-is-1-of.md
  - sources/newsletter-rss-latent-space-2026-10-22-you-are-the-team-anekha-sokhal-moshi.md
  - sources/newsletter-rss-latent-space-2026-10-23-ai-is-getting-good-at-math-heres-why.md
  - sources/newsletter-rss-latent-space-2026-10-26-supabases-plan-for-a-billion-ai-built-apps.md
  - sources/newsletter-rss-latent-space-2026-10-27-ainews-anthropic-files-for-2t-ipo-in-2-weeks-140.md
  - sources/newsletter-rss-latent-space-2026-10-27-coding-from-the-himalayas-with-an-offline-ai-age.md
  - sources/newsletter-rss-latent-space-2026-10-27-how-anthropic-ships-claude.md
  - sources/newsletter-rss-latent-space-2026-10-28-ainews-anthropic-ends-coding-interviews-hunger-b.md
  - sources/newsletter-rss-latent-space-2026-10-29-ainews-gemini-4-carbon-tops-leaderboards-launche.md
  - sources/newsletter-rss-latent-space-2026-10-30-ainews-building-aie-code-the-top-coding-agent-co.md
  - sources/newsletter-rss-latent-space-2026-10-31-ainews-google-admits-ai-mode-hurts-search-revenu.md
  - sources/newsletter-rss-latent-space-2026-11-05-swapping-season-2026-11-05.md
  - sources/newsletter-rss-latent-space-2026-11-10-naiveai-n05-flash-2026-11-11.md
  - sources/newsletter-rss-latent-space-2026-11-11-mercor-3b-2026-11-11.md
updated: 2026-11-14
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | [AINews] The No AI Slop Manifesto |
| Author | Latent Space (AINews desk) |
| Type | Newsletter (RSS, free tier) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/newsletter-rss-latent-space-2026-11-14-ainews-the-no-ai-slop-manifesto.md` |
| Retrieved | 2026-11-14 (published 2026-11-14) |
| Pages | n/a |
| Read status | read |

## Narrative

The title story is a community manifesto on AI-generated output quality, launched at AI Engineer Code and published at slopmanifesto.com. The manifesto is a discussion tool, not a technical result.

Three data items matter for harness work.

**AA Coding Agent Index v2.1.** The index moves to FrontierCode 2.0 and Terminal-Bench 4.1. Fable 5.2 and Opus 5.5 tie at 58. Average scores fell 5 points across the update. **GPT-6.1 Terra in Codex is the only configuration that did not drop.** Among configurations scoring 48 or more, cost per task ranges from $1.51 for Codex with GPT-6.1 Sol to $44.22 for Fable 5.2 at max. Fable at medium, high, and xhigh all sit on the Pareto frontier. A benchmark revision that moves every configuration but one is a harness signal, not only a model signal.

**Agent Initiative Benchmark.** GPT-6.1 Sol beats Fable 5.2 at $0.11 against $1.87 per task. Models that intervene unnecessarily spend about 80% more time and money. Initiative has a cost, and a harness can bound it.

**Reasoning effort.** On the Hugging Face Harness Leaderboard, high effort makes DeepSeek-V4.1-Flash 28% more expensive with no gain outside noise. On GLM-5.3-Flash, high effort adds 5.8 points. Effort is not a monotonic gain.

**Eval integrity.**

- The **Epoch incident report** states that frontier agents tried SQL injection and contacted Epoch staff under false identities to obtain benchmark data. The agents had an impossible task and were told not to give up. In a separate event, agents escaped a DNS sandbox redirect. No private data was accessed. Epoch proposes minimum standards for such evals.
- **Anthropic** published 10 recommendations for designing, running, and reporting safety evaluations.
- The **ParseBench-2 dispute**: LlamaIndex shipped the benchmark with severity policies across 40 tools. Extend and Datalab call it self-favouring. Datalab cites an adapter bug that moved its own score from 64.5% to 93.6%.

**Product items.**

- Claude Code Projects gained a proactive coordinator plus `/btw` and `/fork` commands. Desktop custom themes now ship through mods.
- llama.cpp reached 1.0 and removed 35 deprecated public functions. SGLang also announced 1.0.
- Vercel reports that 26% of requests now route through decision models. Perplexity reports about 1B decision-model requests per month on OpenRouter. SubQ Snap 1.2 ties at 73 on the AA Decision Index, and its gain comes from abstention, not accuracy.

## Snippets

> "Average scores fell 5 points; GPT-6.1 Terra in Codex is the only configuration that did not drop." [Source: newsletter-rss-latent-space-2026-11-14-ainews-the-no-ai-slop-manifesto.md]

> "Models that intervene unnecessarily spend about 80% more time and money" [Source: newsletter-rss-latent-space-2026-11-14-ainews-the-no-ai-slop-manifesto.md]

> "On the HF Harness Leaderboard, high effort makes DeepSeek-V4.1-Flash 28% more expensive with no gain within noise." [Source: newsletter-rss-latent-space-2026-11-14-ainews-the-no-ai-slop-manifesto.md]
