---
title: "Latent Space: Google AI Mode hurts Search revenue; agent limits and harness costs"
type: source
tags: [source, newsletter, agents, coding-harness, search-revenue]
related: []
maturity: draft
read_status: read
created: 2026-11-01
updated: 2026-11-01
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | [AINews] Google admits AI Mode hurts Search revenue; -15% $500B drop worst since 2004 IPO. AI Bear Market coming? |
| Source | Latent Space |
| File | `newsletter-rss-latent-space-2026-10-31-ainews-google-admits-ai-mode-hurts-search-revenu.md` |
| Retrieved | 2026-11-01 |
| URL | https://latent.space/p/ainews-google-admits-ai-mode-hurts-search-revenue-15-500b-drop-worst-since-2004-ipo-ai-bear-market-c/ |
| Read status | read |

## Narrative

The file lists this Latent Space post as published on 2026-10-31. The issue covers AI news for 10/29/2026–10/30/2026. Latent Space says it rarely runs financial stories. It runs this one because the subject is the future of Google and Google Search, after a recent departure in AI leadership. The argument is that a good summary removes the need to read the source page. Featured Snippets and Knowledge Panels already had that tension with publishers. The issue says Google's own AI Overviews now press on Google's Search revenue.

The title states "-15%" and a "$500B drop", and calls it the worst since the 2004 IPO. Those two figures appear in the title. The body quotes Philipp Schindler, Chief Business Officer: strong growth in AI Mode queries had an impact because monetization in AI Mode was lower. The issue says Google does not break out AI Mode in enough detail for a rigorous analysis. The same issue says OpenAI is "raising at $1.25T not $1.4T". It also says Reddit's CEO says Google's AI Mode "does not drive traffic", and that Search referrals fell by more than 1M per week in October. Each of these figures is a single-source claim in this issue.

The issue then reports costs that change how an agent harness runs. It labels the Anthropic margin notes as unverified analysis. One account cites a SemiAnalysis reconstruction. The issue puts Anthropic's API margin at about 92%, versus about 84% for DeepSeek. It says Opus on subscriptions breaks even only below about 21.3% utilization. It estimates that subscriptions bring in about 18% of revenue and use more than 50% of compute. On Agent Arena, an analysis of 26K sessions finds that a task on a top-10 agent costs 3.6x as much without prompt caching. A typical Fable 5.1 task costs $7.44 with caching versus $27 without. A single cache invalidation adds about 5% to a task's bill. These figures are single-source in this digest.

Anthropic plan changes land on the session limit. Max 5x is now "Max" at $100/month. Max 20x is now "Ultra" at $200/month. Verified Ultra accounts no longer have the 5-hour session limit. Weekly limits stay the same. Newer accounts keep a temporary limit until Anthropic verifies them. The issue calls that check an anti-fraud measure.

Two items hit the coding agent supply chain. A malicious copy of the Claude Code extension in Cursor's marketplace affected at most 5,000 users. Cursor pulled the marketplace, neutralized the malware, and reinstated it. The issue says users should update to v2.1.314. Anthropic says its own systems were not compromised, and that it did not build or publish this extension. A server-pushed Claude Code rule under the flag `tengu_heron_brook`, added around Oct 27, bars recreating specific existing games even if the user renames them. Users cannot turn the rule off. A research note says poisoning 0.1% of pretraining data planted a remote-code-execution backdoor in a CLI agent. The attack fired on about 92% of triggered prompts at 4B. The backdoor survived SFT, DPO, and RL, and attack success rose with model size. At 0.0005% poisoning (about 2,500 documents in 100B tokens), the trigger fired on 1.4% of prompts in a single-seed run. These results are single-source as reported here.

The same issue reports harness efficiency claims. A LoRA trained with RL on LFM2.5-24B-A2B matches the base model's accuracy with 39% fewer tool calls in the pi harness. The run took about 24 hours on one GPU. Claude rewrote the Messages API in Rust on a team with no Rust developers. Humans wrote the plan and checked that old and new output matched on real traffic. CPU use dropped 40–50%. A 4B Microsoft computer-use agent scores 66.0% on OSWorld-Verified. NVIDIA Nemotron 3.5 Super scores 51.78% on SWE-bench Pro. Each of these results is a single-source claim in this issue.

## Snippets

> "It's worth noting that the strong growth in AI Mode queries had an impact because of the lower monetization we were seeing in AI Mode." [Source: https://latent.space/p/ainews-google-admits-ai-mode-hurts-search-revenue-15-500b-drop-worst-since-2004-ipo-ai-bear-market-c/ (retrieved 2026-11-01)]

> "A malicious copy of the Claude Code extension affected at most 5,000 users." [Source: https://latent.space/p/ainews-google-admits-ai-mode-hurts-search-revenue-15-500b-drop-worst-since-2004-ipo-ai-bear-market-c/ (retrieved 2026-11-01)]
