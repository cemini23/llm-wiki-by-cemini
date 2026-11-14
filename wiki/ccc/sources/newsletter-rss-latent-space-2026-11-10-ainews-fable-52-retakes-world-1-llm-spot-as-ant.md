---
title: "Latent Space AINews — Fable 5.2 retakes the top LLM spot"
type: source
related:
  - entities/models/claude-fable-5-2.md
  - concepts/frontier-model-release-cadence.md
  - concepts/token-economics-and-prompt-caching.md
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | [AINews] Fable 5.2 retakes World #1 LLM spot as $ANT IPO roadshow begins |
| Author | Latent Space (AINews roundup) |
| Type | newsletter (RSS) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/newsletter-rss-latent-space-2026-11-10-ainews-fable-52-retakes-world-1-llm-spot-as-ant.md` |
| Retrieved | 2026-11-10 |
| Published | 2026-11-10 |
| Read status | read |

## Narrative

Anthropic shipped **Claude Fable 5.2** and **Claude Mythos 5.2** on the day its IPO roadshow began. Independent leaderboards put Fable 5.2 first.

Specification:

- $8 per million input tokens and $40 per million output tokens. That is 20% below Fable 5.1 at $10/$50.
- Cache writes cost $10 (5-minute TTL) or $16 (1-hour TTL). Cache reads cost $0.20.
- 1M-token context, text and image input.
- Five effort levels: low, medium, high, xhigh, max. Medium is the default in the Claude apps and Claude Code.

The operational point is that the cheaper token price does not lower the task cost. SemiAnalysis measured $88.15 per task on GDPx, up from $67.16, despite the 20% price cut. The run logs explain it. Where Opus 5.5 and Fable 5.1 tried about 20 test cases, 5.2 wrote hundreds or thousands and spawned subagents to check its work. It took first place at 16.4%. **You pay for the checks either way.**

Effort guidance from the vendor: on FrontierCode 2.0, Fable 5.2 at High matched Opus 5.5 at Max for about half the cost per task. At Xhigh it was the top released model. The newsletter advises starting at the default rather than carrying over 5.1 settings, because effort levels behave differently.

Independent results:

- Artificial Analysis Intelligence Index v5: first at 65. Gemini 4 Carbon 60, Opus 5.5 59, GPT-6 Astra 57, Fable 5.1 49.
- New records: HLE-Diamond 80% (previous 69%), AA-Omniscience 67 (previous 54), Terminal-Bench-Science 73% (previous 65%), CritPt v2 hard 77%, FrontierCode 2.0 49%.
- ARC-AGI-3 standard harness 81.2% at $21.9K total cost; provider adapter harness 97.7% at $18.6K. That harness gap is itself a finding.
- Epoch Capabilities Index 174, a record.
- Weaker spots: AA-Briefcase 1785 Elo, GDP.pdf 24% all-pass against 26% for Opus 5.5, Terminal-Bench 4.0 60%.

Efficiency: at high and xhigh it scores 62 using about 98K output tokens per task, against 173K for Opus 5.5 at max. At max, cost is about $26.5 per task, roughly 2.6 times Opus 5.5 and 2 times Fable 5.1.

Long-horizon demonstrations: 1,000 Fable 5.2 agents formalised the existing proof of Fermat's Last Theorem in 30 hours (Opus 5.5 reached 26% in 18 hours). Over 8 days, 1,000+ subagents built an OS from an empty folder with its own kernel, drivers, windowing, login, installer, and a built-in Claude.

Access restrictions are part of the release: subscription resets scale with tenure, Fable may consume only 50% of a weekly limit, and data retention is required by default so safety classifiers can run.

## Snippets

> "Where Opus 5.5 and Fable 5.1 would try about 20 test cases, 5.2 sometimes wrote hundreds or thousands and spun up subagents to check its work independently. ... You pay for the checks either way." [Source: newsletter-rss-latent-space-2026-11-10-ainews-fable-52-retakes-world-1-llm-spot-as-ant.md]

> "Fable 5.1 cost $10 per million input tokens and $50 per million output tokens. Fable 5.2 costs $8 and $40. Yet on GDPx ... SemiAnalysis paid $88.15 per task, up from $67.16." [Source: newsletter-rss-latent-space-2026-11-10-ainews-fable-52-retakes-world-1-llm-spot-as-ant.md]
