---
title: "Jiang et al. 2026 — Understanding ChatGPT Citations: Evidence from Production Web Search Across Model Generations"
type: source
tags: [seo, geo-aeo, academic-paper, citation-visibility, retrieval, model-generations]
keywords: [GEO, ChatGPT Web, retrieval to citation, query rewriting, SSR traces, Google Search proxy, Responses API]
related:
  - concepts/retrieval-vs-citation-visibility-geo.md
  - concepts/ai-citation-sourcing-geo.md
  - concepts/geo-visibility-measurement.md
  - concepts/competitive-geo-citation-factors.md
  - sources/chen-2026-what-drives-ai-citations.md
maturity: validated
read_status: deep-read
created: 2026-10-14
updated: 2026-10-14
---

## Relations

- @concepts/retrieval-vs-citation-visibility-geo.md — the retrieval-to-citation split this paper instruments
- @concepts/ai-citation-sourcing-geo.md
- @concepts/geo-visibility-measurement.md — the proxies this paper tests are measurement instruments
- @concepts/competitive-geo-citation-factors.md — those gatekeepers act inside the retrieved set this paper measures
- @sources/chen-2026-what-drives-ai-citations.md — companion study; reaches the same retrieval primacy from a different method

## Raw Concept

Title: Understanding ChatGPT Citations: Evidence from Production Web Search Across Model Generations
Authors: Yunxuan Jiang, Shiqi Zhang, Anqi Xing, Xiangyu Chang, Xiaokui Xiao (XJTU, NUS, SGIT AI Lab)
Type: arXiv preprint
Location: `research to be indexed/seo/arxiv-2610.15382-understanding-chatgpt-citations-evidence-from-pr.pdf`
Retrieved: 2026-10-14
Pages: 11
Read status: deep-read

## Narrative

An **observational study of the internal execution** of ChatGPT Web — the step between retrieval and citation — read from **server-sent event (SSE) traces** rather than from final answers. Four settings, **ChatGPT 5.2 → 5.5**, across Instant and Thinking modes, measured at three levels: URL, hostname, and entity.

### Settings behave differently, and not in a straight line

| Setting | Retrieval behaviour |
|---|---|
| GPT-5.2 Instant | More executed queries; mostly single-round |
| GPT-5.3 Instant | Fewer executed queries; mostly single-round |
| GPT-5.4 Thinking | **Frequently multi-round**; narrows the target in later rounds |
| GPT-5.5 Instant | Fewer executed queries; mostly single-round |

**GEO findings do not transfer between settings.** The paper's own conclusion: strategies should be **re-evaluated when the deployed setting or serving environment changes**.

### Retrieval frequency predicts citation

Repeated runs retrieve many different pages. But **candidates that appear more often across runs are also more likely to be cited**. Longer retrieval snippets are a **weaker but consistent** citation signal.

This is the practical consequence: citation share is partly a function of retrieval *stability*, not just retrieval *presence*.

### External proxies are weak at URL level

| Proxy | Coverage | Agreement |
|---|---|---|
| OpenAI Responses API candidates | **Broader** | Closer citation match |
| Google Search | Narrower | Weaker match |

Both proxies agree with ChatGPT Web **better at hostname and entity level than at exact-URL level**. **Combined, they recover only about a quarter of cited URLs.**

A supervised model over the joint external signals reaches **AUC above 0.74** for GPT-5.3 and GPT-5.5 at all three levels — useful, but not a substitute for direct observation.

### The recommendation to practitioners

The paper closes with four instructions, all of which follow from the above:

1. **Distinguish retrieval visibility from citation visibility.** Being retrieved is necessary; it is not sufficient.
2. **Account for rewritten queries** and **run-to-run variation**.
3. **Measure hostname- and entity-level presence**, not only exact URLs.
4. **Re-evaluate** when the model setting or serving environment changes.

## Snippets

> "Generative engines such as ChatGPT Web retrieve webpages to answer user queries, but only a subset are shown as citations." [Source: arxiv-2610.15382 p.1]

> "Repeated runs retrieve many different webpages, but candidates that appear more often across runs are also more likely to be cited." [Source: arxiv-2610.15382 p.1]

> "Both proxies match ChatGPT Web more closely at the hostname and entity levels than at the URL level. ... Even when combined, they recover only about one quarter of cited URLs." [Source: arxiv-2610.15382 p.1]

> "These findings suggest that GEO should distinguish retrieval visibility from citation visibility, account for rewritten queries and run-to-run variation, and consider hostname- and entity-level presence in addition to exact URLs." [Source: arxiv-2610.15382 p.1]

## Dead Ends

- Using Google Search rankings as a proxy for ChatGPT citations. Agreement is weak at URL level, and the two proxies together recover roughly a quarter of cited URLs.
- Treating a previous GEO result as stable. Behavioral differences across the 5.2→5.5 settings mean a result measured on one setting may not hold on another.
