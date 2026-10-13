---
title: "Pragmatic Engineer — building resilient AI-powered software (Sam Newman excerpt)"
type: source
tags: [source, k290, engineering, reliability, disaster-recovery, ai-vendors, feeds]
keywords: [pragmatic-engineer, sam-newman, rpo, rto, pilot-light, warm-failover, active-active, multi-model, cost-transparency, k290]
related:
  - concepts/k290-feeds-wave.md
  - concepts/ai-vendor-multimodel-resilience.md
  - concepts/disaster-recovery-patterns.md
  - concepts/agent-cost-routing-model-orchestra.md
maturity: draft
created: 2026-10-13
updated: 2026-10-13
read_status: read
---

## Relations

- @concepts/k290-feeds-wave.md
- @concepts/ai-vendor-multimodel-resilience.md
- @concepts/disaster-recovery-patterns.md
- @concepts/agent-cost-routing-model-orchestra.md

## Raw Concept

| Title | Building resilient AI-powered software, and planning for when things go wrong |
| Author | Gergely Orosz (The Pragmatic Engineer); excerpts from Sam Newman, *Building Resilient Distributed Systems* (O'Reilly, 2026) |
| Type | Newsletter (free RSS) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/newsletter-rss-pragmatic-engineer-2026-10-13-building-resilient-ai-powered-software-and-plann.md` |
| URL | https://newsletter.pragmaticengineer.com/p/building-resilient-systems |
| Retrieved | 2026-10-13 |
| Published | 2026-10-13T16:03:33Z |
| read-status | read |

## Narrative

Two book chapters (10: Disaster Recovery; 7: Resiliency and AI) plus Orosz's framing. **The framing claim is the news:** outages are rising, and **much of the increase is more code deploy churn from AI agents** — more software, more bugs, more incidents.

### DR fundamentals (Chapter 10)

**RPO (recovery point objective)** = maximum tolerable data loss (how far back the last backup is). **RTO (recovery time objective)** = maximum tolerable unavailability. **You cannot have RPO 0 / RTO 0** — cost and complexity rise steeply as either shrinks. **Different services need different RPO/RTO** (a bank's payments path vs its sign-up flow). **RPO/RTO do not fit neatly into SLOs** — disasters are too rare to accumulate useful SLIs; you can only measure proxies, such as replication speed.

**Four DR patterns, in increasing cost and improving RPO/RTO:**

| Pattern | Data | Infrastructure | Notes |
|---------|------|----------------|-------|
| Backup and restore | periodic backups to a second site | provisioned on demand | simplest; longest RTO (minutes→weeks if hardware must be bought) |
| Pilot light | continuous replication | provisioned after failover | short RPO; cost saving only makes sense on public cloud |
| Warm failover | continuous replication | partially provisioned, reserved for critical services | lower RTO for top-priority functions only |
| Multisite active-active | replication between 2+ sites, writes to any | always on | best RPO/RTO; highest cost and complexity |

**Infrastructure availability is now a DR constraint.** **GPU and memory costs spiked in 2025–2026**, and clients report **failing to secure capacity for ordinary (non-AI) workloads**. Options: **reserve capacity** (AWS EC2 reservations; not possible for Lambda), **prioritize critical services** (needs per-service RPO/RTO), or **run fully redundant infrastructure**. Reuse idle DR capacity (load-test pool) to offset cost.

### AI-specific resilience (Chapter 7)

**Model provider resilience.** Newman states **OpenAI and Anthropic have a poor availability track record versus cloud vendors.** Mitigations: **graceful degradation** when the model is unavailable or rate-limited, and **backup vendors** — e.g. **OpenAI models via Azure**, **Anthropic models via Google's Gemini Enterprise Agent Platform**.

**Model changes.** LLM behaviour is **nondeterministic**, and **small version changes alter behaviour**; vendors have shipped **silent behaviour changes**. Therefore **functional tests plus evals** are mandatory: *"you want to make sure … you are the ones who get surprised first, rather than your users."*

**Observability.** Agent and LLM latency **varies unpredictably** (provider load, rate limits, prompt length, user-supplied prompts). Techniques: **timeouts scaled to expected output tokens**, and **watching streaming output** to detect a response start rather than waiting for the whole completion.

**Handling uncertainty — three concrete practices:**
1. **Multimodel, multivendor.** Mixing vendors inside one flow **increases** the failure surface — every model in the flow must be up. **Prompts do not port cleanly between models.** Vendor dependence also matters: **Cursor had to pass a large cost increase to customers in 2025** after Anthropic changed pricing.
2. **Cost transparency.** Nordhealth's CTO **publishes spend per person**; a QA engineer burning **€1,000 in a week on Claude Code** more than **doubled his productivity** once paired and understood. **Uber burned its entire annual AI budget in four months.** Microsoft reportedly pulled Claude licences over cost. An **unsubstantiated Axios report** claims one enterprise spent **$500M on Claude licences** without cost controls.
3. **More frequent vendor analysis.** Review **AI vendors more often than normal vendors**; check whether each vendor is **itself dependent on a single provider**; keep **threat models current**.

**Orosz's closing read:** an **autonomous AI SRE is far off**; humans stay in the loop. **Consistency of behaviour** is a big part of resilience, and LLMs are the opposite of consistent.

### Why it matters here
This is the best **operational** frame this wiki has picked up for the AI-vendor question. Two direct applications: (a) **`@concepts/agent-cost-routing-model-orchestra.md`** — multi-vendor routing is a **cost and resilience** control, and the new warning is that **mixing vendors inside one flow raises the failure surface**; (b) **our own stack** — `cemini-*` hosts and the DeepSeek/Anthropic/Grok lanes are exactly the "vendor dependent on one provider" pattern Newman warns about.

## Snippets

> Foundation model providers OpenAI and Anthropic don't have a great track record in terms of providing high levels of availability for their services … having a potentially flaky third party in the mix of your critical functionality can be an issue. [Source: https://newsletter.pragmaticengineer.com/p/building-resilient-systems (retrieved 2026-10-13)]

> You want to make sure that when the unexpected occurs, you are ones who get surprised first, rather than your users. [Source: https://newsletter.pragmaticengineer.com/p/building-resilient-systems (retrieved 2026-10-13)]

> Cursor was forced to pass on a significant cost increase to its customers in 2025, as it relied on the use of Anthropic's services, and Anthropic changed its pricing structure. [Source: https://newsletter.pragmaticengineer.com/p/building-resilient-systems (retrieved 2026-10-13)]

> Uber recently revealed that it had burned through its entire annual AI budget in just the first four months of the year. [Source: https://newsletter.pragmaticengineer.com/p/building-resilient-systems (retrieved 2026-10-13)]
