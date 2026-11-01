---
title: "Latent Space AINews: Building AIE CODE and the 28–29 Oct 2026 agent roundup"
type: source
tags: [source, newsletter, coding-agents, aie-code, harness]
related: []
maturity: draft
read_status: read
created: 2026-11-01
updated: 2026-11-01
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | [AINews] Building AIE CODE: The top Coding Agent Conference |
| Source | Latent Space |
| File | `newsletter-rss-latent-space-2026-10-30-ainews-building-aie-code-the-top-coding-agent-co.md` |
| Retrieved | 2026-11-01 |
| URL | https://latent.space/p/ainews-building-aie-code-the-top-coding-agent-conference/ |
| Read status | read |

## Narrative

Latent Space uses a quiet day for a behind-the-scenes look at AI Engineer. The letter says the site now serves 6M views a month for 1.8M monthly unique viewers. AIE CODE is the last flagship of the year. AIEi Shanghai is next week. AIEi Sydney is a NeurIPS side event in December. CODE is a single-track summit for the top 1000 agentic engineers. The letter says over 100k people tuned into the Software Factories track at WF26. These audience counts appear only in this letter.

The stated goal is to recap the top code themes of 2026 and to preview 2027. The letter names three themes. Scaling without Slop follows last year's call for "No More Slop" and this year's talk about Tokenmaxxing. The letter says that approach has mostly worked and that more work remains. System One models are presented as the largest change in AI engineering, and as a turn away from larger and more costly swarms of coding-agent factories. Increasing Ambition covers rewrites of browsers, the Adobe PhotoShop Suite, and mid-tier B2B SaaS. Jarred Sumner is set to start from the Bun rewrite in Rust and to preview Bun AOT. The letter also names Cursor's next phase as Grok Bot, the internal agent Ramp Inspect, and the failure of Gas Town. A Muse Code speaker is not secured. A couple hundred seats remain. Paid subscribers get a $400 code. The checkout code LS30 takes 30% off.

The AINews block covers 10/28/2026–10/29/2026. The letter says it checked 12 subreddits, 544 Twitters, and no further Discords. Every figure below is a single-source claim in this digest.

Mistral Large 4 ("Le Chonk") is described as open weights for agentic coding and cybersecurity. The letter gives 1.05T total parameters, 52B active parameters, a 1M context, and text plus image input. The listed price is $0.70/$2.10 per 1M input/output tokens, and $0.07 for cached input, about 50% below the Preview. The MEOW license requires a separate commercial license for a model-as-a-service business. FrontierCode 2.0 is 15%, versus 29% for DeepSeek V4.1 Flash 1017 and 22% for GLM-5.3. Terminal-Bench 4.0 is 25%, versus 8% for Muse Spark Open. The Coding Agent Index score is 48 at 8.5M tokens per task, against 49 and 15.9M tokens for GLM-5.3. Artificial Analysis scores the model 26 on Intelligence Index v5, 6 points behind DeepSeek V4.1 Flash 1017 and GLM-5.3. The AA-Omniscience hallucination rate fell from 41% to 28%. Accuracy remains 26%. Unsloth's 1-bit GGUF is 223GB, versus 1.1TB in FP8, and the letter says it retains 91% top-1 accuracy. vLLM support for the FP8 and NVFP4 checkpoints is said to give 1.92–2.23x output throughput.

The same digest matters to a coding-harness reader because it pairs those scores with token cost, monitors, and harness failures. AgentBaton reports that one handoff from a capable model to a cheaper model cuts API cost 65.9%. SwarmChat reports that 16-agent swarms matched single-agent performance 6x faster. OpenAI now monitors all frontier RL runs, evaluations, and internal Codex use. A replay of a Hugging Face incident produced an alert about 30 minutes after the sandbox escape, more than 30 hours before the original breach. Epoch reports that GLM 5.3 built Firefox exploits for six recent versions. Each compromised version cost about $1,000. The fastest attempt took 12 hours of a 48-hour budget. The official Claude Code VS Code extension was reportedly compromised, and a pull during a brief window would have installed an SSH backdoor. One Reddit report says Claude Code use rose from 161M total tokens and $41.17 to 1.306B total tokens and $493.04, and that Anthropic said service-error retries count toward paid limits. Another report reads the harness as about 3.8× less efficient, with output per 1% of the limit falling from 119K to 31K, and points to subagents that reread parent context above about 350K tokens. Gemini 4 Carbon scores 40% on FrontierCode 2.0 at $4.04 per task. GPT-6.1 Sol costs $1.91 per task versus $12.51 for Opus 5.5. OpenAI doubled Codex limits for Pro 100/200/500 and Business Premium and cancelled the planned Pro 200 cut.

## Snippets

> "CODE is the last flagship AIE of the year (there are also 2 partner conferences coming up - AIEi Shanghai takes place next week, and AIEi Sydney is a side event of NeurIPS in December). As a Summit it is meant to be more intimate: single track, invite-only for the top 1000 agentic engineers in the world (over 100k tuned into our Software Factories track at WF26)." [Source: https://latent.space/p/ainews-building-aie-code-the-top-coding-agent-conference/ (retrieved 2026-11-01)]
