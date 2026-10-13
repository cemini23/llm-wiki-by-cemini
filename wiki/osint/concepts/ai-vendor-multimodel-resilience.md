---
title: AI vendor resilience — multimodel routing, cost transparency, vendor review cadence
type: concept
tags: [engineering, reliability, ai-vendors, cost, model-routing]
keywords: [vendor-resilience, multimodel, multivendor, graceful-degradation, cost-transparency, evals, observability, model-drift]
related:
  - sources/newsletter-rss-pragmatic-engineer-2026-10-13-resilient-ai-systems.md
  - concepts/agent-cost-routing-model-orchestra.md
  - concepts/disaster-recovery-patterns.md
  - concepts/deepseek-models.md
  - concepts/ai-industry-trends-2026.md
maturity: draft
created: 2026-10-13
updated: 2026-10-13
---

## Relations

- @sources/newsletter-rss-pragmatic-engineer-2026-10-13-resilient-ai-systems.md
- @concepts/agent-cost-routing-model-orchestra.md
- @concepts/disaster-recovery-patterns.md
- @concepts/deepseek-models.md
- @concepts/ai-industry-trends-2026.md

## Raw Concept

**The question this page answers:** what does treating a model provider as a *vendor* — rather than as a utility — require of a system that depends on it?

Source: Sam Newman, *Building Resilient Distributed Systems* (O'Reilly, 2026), excerpts in The Pragmatic Engineer, 2026-10-13.

## Narrative

### 1. Model providers are unreliable third parties

Newman states it plainly: **OpenAI and Anthropic have a poor availability track record compared with other managed service providers** such as cloud vendors. Two mitigations:

- **Graceful degradation** — degrade functionality when the model is unavailable, rate-limited, or out of tokens.
- **Backup vendors** — **OpenAI models via Azure**; **Anthropic models via Google's Gemini Enterprise Agent Platform**. Expect a lag before the newest models appear there.

### 2. Multivendor has a cost, not just a benefit

The counterintuitive part, and the reason this page exists:

- **Mixing models from different vendors inside a single flow increases the failure surface** — every model in the flow must be available and behaving.
- **Prompts are not portable.** A prompt tuned against one model must be **re-evaluated** on another, even within the same vendor.
- **Vendor dependence is transitive.** A vendor wholly dependent on one model provider inherits that provider's volatility and pricing. **Cursor had to pass a large 2025 cost increase to customers** because it depended on Anthropic.

So **multimodel is a portfolio decision with a correlation penalty** — the same shape as position concentration.

### 3. Model drift demands evals, not just tests

- LLMs are **nondeterministic** by construction.
- **Vendors have shipped silent behaviour changes.**
- A **version bump can change how existing prompts are handled.**

Required: **functional tests plus AI evals.** *"You want to make sure … you are the ones who get surprised first, rather than your users."*

### 4. Observability when latency is user-shaped

LLM latency varies from **provider load, rate limiting, prompt length, and user-supplied prompts**. Two techniques: **timeouts scaled to expected output tokens**, and **monitoring streaming output** to detect response start instead of waiting for a full completion.

### 5. Cost transparency as an operating practice

- **Publish spend** (Nordhealth publishes **per-person** spend).
- High spend is **not automatically waste** — one QA engineer at **€1,000 in a week on Claude Code** more than **doubled his productivity** once the spend was reviewed.
- **Uber burned its entire annual AI budget in four months.** Microsoft reportedly pulled Claude licences over cost. An **unsubstantiated Axios report** claims one enterprise spent **$500M on Claude licences** with no cost controls.

### 6. Review AI vendors more often than normal vendors

Check whether each vendor is **itself dependent on a single provider**; keep **threat models current**; increase review frequency in AI-heavy areas.

### Applied to this workspace

The `cemini-*` stack and the DeepSeek / Anthropic / Grok / Codex lanes have exactly the dependency shape Newman warns about, and `@concepts/agent-cost-routing-model-orchestra.md` already treats model choice as a routing decision. The new constraint from this source: **do not assume adding a vendor inside a flow is free.** Prefer **vendor-level failover between whole flows** over **vendor-mixing inside one flow**.

## Snippets

> Foundation model providers OpenAI and Anthropic don't have a great track record in terms of providing high levels of availability for their services … having a potentially flaky third party in the mix of your critical functionality can be an issue. [Source: https://newsletter.pragmaticengineer.com/p/building-resilient-systems (retrieved 2026-10-13)]

> mixing models from different vendors in a single flow can exacerbate issues … All those models have to be available and functioning correctly at the time the flow is executed. [Source: https://newsletter.pragmaticengineer.com/p/building-resilient-systems (retrieved 2026-10-13)]

> Make sure you aren't wholly dependent on a single model or AI platform. [Source: https://newsletter.pragmaticengineer.com/p/building-resilient-systems (retrieved 2026-10-13)]
