---
title: "CAPTA: identifying the LLM behind an AI agent"
type: source
related:
  - concepts/ai-agent-traffic-identification.md
  - concepts/generative-engine-optimization.md
  - concepts/agent-ready-website-local-bm.md
updated: 2026-11-25
---

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | CAPTA: Identifying LLMs Behind AI Agents |
| **Author** | Kailun Yan, Yue Huang, Sisi Duan (Tsinghua University) |
| **Type** | arXiv preprint (cs.AI) |
| **arXiv ID** | 2611.32686 |
| **Location** | `research to be indexed/seo/arxiv-2611.32686-capta-identifying-llms-behind-ai-agents.pdf` |
| **Retrieved** | 2026-11-25 |
| **Pages** | 18 |
| **Read status** | read |

## Narrative

**Relevance: indirect but real.** The paper is a security method. It matters to GEO in two ways. First, a server can identify which model sits behind an AI agent. Second, the paper names AI-targeted **cloaking** as the reason a server would want to. Both touch how AI-engine traffic is measured.

**The problem.** An agent reaches a remote service through tools, often by API. The service never talks to the backend model. It only sees responses. A service may want to know the backend model to deliver model-specific prompts, or to deliver different content to the agent than to a human.

**The method.** CAPTA borrows the CAPTCHA format. When an agent hits a challenge, the service serves multiple-choice questions instead. Different models pick different options on the same question. Two examples from the paper: in 20 trials of a "pick a rainbow colour" question, DeepSeek-V4-Flash and Qwen-3.7-Flash picked red 20 of 20 times. GPT-5.6-Luna and Claude-Sonnet-5 picked blue 20 of 20 times.

Questions are chosen by how much the candidate options differ across models. An LLM-guided search then tunes each option set to widen that gap.

**Results.**

| Setting | Result |
|---------|--------|
| 25 LLMs from 10 families | 99.0% mean identification accuracy with 10 probes |
| Same set, 21 probes | At least 99% for every candidate model |
| 4 agents × 7 LLMs = 28 combinations | 99.7% mean accuracy with 30 submitted answers |

**The traffic numbers it cites.** AI agent traffic exceeded 6.6 billion requests in a single month in Q2 2026, per DataDome. Agents made an average of 3.64 external requests per session on information-retrieval tasks [TENTATIVE — secondary citations inside the paper].

**What a publisher should take from it.** Two points, both framed as risk rather than tactic.

1. **Segment AI traffic by model, if you measure it.** A site that already challenges agents can, in principle, label visits by backend model. That would let a GEO audit separate ChatGPT, Claude, and Perplexity crawls. This wiki has not tested it, and the paper does not present a website-side deployment.
2. **AI-targeted cloaking is now cheap.** If a service can tell the model, it can serve that model different content. The paper's own example is a shopping site showing AI agents fake promotions while humans see the real page. A citation read from a cloaked response is not evidence about the page. Any GEO measurement that trusts agent-side answers inherits that risk.

**What it does not do.** The paper explicitly does not attack the identified models. It is an identification study. It does not measure citation behaviour, rankings, or retrieval quality.

**Boundary.** Do not read this as advice to cloak. It is a threat model. See @concepts/ai-agent-traffic-identification.md for the wiki's standing on that line.

## Snippets

> "a service could selectively deliver manipulated content to AI agents while showing the original content to human visitors. This technique is known as cloaking." [Source: arxiv-2611.32686-capta-identifying-llms-behind-ai-agents.pdf p.1]

> "CAPTA achieves 99.0% mean identification accuracy with only 10 questions across 25 LLMs from 10 model families." [Source: arxiv-2611.32686-capta-identifying-llms-behind-ai-agents.pdf p.1]
