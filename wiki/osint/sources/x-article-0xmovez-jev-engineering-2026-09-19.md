---
title: "Jev Engineering: fastest AI Agent Brain in 10 Steps (@0xMovez)"
type: source
tags: [source, k266, ccc, jev, harness, cost]
keywords: [k266, Jev, System One, Jevons paradox, compaction, confidence, guardrails]
related:
  - concepts/k266-ccc-jev-x-wave.md
  - sources/x-article-sydneyrunkle-harness-jev-2026-09-19.md
  - entities/tools/jev-mcp.md
  - entities/tools/openjev.md
  - sources/x-article-shreyanshpatni-agent-harness-2026-09-19.md
  - sources/x-article-borjafat-internal-linking-2026-09-19.md
  - sources/x-article-buildwithpublic-0dte-2026-09-19.md
  - sources/x-post-parcadei-jev-skill-classify-2026-09-19.md
maturity: draft
created: 2026-09-19
updated: 2026-09-19
read_status: read
---

## Relations

- @sources/x-post-parcadei-jev-skill-classify-2026-09-19.md
- @sources/x-article-buildwithpublic-0dte-2026-09-19.md
- @sources/x-article-borjafat-internal-linking-2026-09-19.md
- @sources/x-article-shreyanshpatni-agent-harness-2026-09-19.md
- @concepts/k266-ccc-jev-x-wave.md
- @sources/x-article-sydneyrunkle-harness-jev-2026-09-19.md
- @entities/tools/jev-mcp.md
- @entities/tools/openjev.md

## Raw Concept

| File | `x-article-0xmovez-jev-engineering-10-steps-2026-09-19.md` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/x-article-0xmovez-jev-engineering-10-steps-2026-09-19.md` |
| Retrieved | 2026-09-19 |
| Dual-ID | **OSINT K266** |
| Author | @0xMovez — post id `2101007482919227841` |
| Kind | X Article — *Jev Engineering: how to build the fastest AI Agent Brain in 10 Steps (Full-Setup)* |
| Metrics | 285 likes · 500 bookmarks · 49,777 impressions (X MCP 2026-09-19) |
| sha256 | `e3e7e0b28f8838bb23ecfc00058252fc9605b4c83284d7e4afd4c7fd8d4bce71` |

## Narrative

Practitioner build guide for a Jev decision layer. Ten steps plus a five-use-case deploy section. **CCC FILE. Do not swap `/route`.**

**Framing — Jevons paradox.** The 1865 rule: a more efficient steam engine raises total coal consumption rather than lowering it. The post applies it to AI: tokens get cheaper each quarter, usage explodes, the bill stays flat or grows. Jev is positioned as the break — System One receives state plus predefined questions and returns typed answers with probabilities. No text generation, no chat, no autoregressive loop.

**The ten steps, compressed.**

| # | Step | Core claim |
|---|------|------------|
| 01 | **Split** gen from decide | "If the operation creates text, it stays with the LLM. If it picks an option, scores a value, or answers yes/no, it goes to Jev." Exact rules (stop after ten actions) stay in code. |
| 02 | **Playground** before code | Test one question in the TypeSafe Playground, then swap the state and compare the decision. |
| 03 | **SDK** | TypeSafe account with API key; Python 3.12+ or Node; TypeSafe's official skill installs integration instructions. |
| 04 | **Handoff** as local JSON queues | `chief.py` writes request, progress, Jev's choice, confidence, destination into `queue/research`, `queue/write`, `queue/review`. Threshold set to **0.85**. |
| 05 | **Questions** | Choice / Score / Noul. Jev does not see the question ID — a field named `safe_to_publish` carries no instruction. |
| 06 | **Dynamic menu** | Rebuild options every turn from what exists now. Browser Use rebuilds the observed control list each click; an LLM generates text only to fill an input. |
| 07 | **Parallel** | Batch questions that inspect the same state. Speculative branches supported. |
| 08 | **Guardrails** | Action limit, spend limit, saved progress. Browser Use checks the outcome **separately** after Jev selects DONE. |
| 09 | **Cost** | Jev 1.13 at **$0.042 per MTok input, no output-token charge.** 10,000 decisions at 1,000 billed input tokens each = $0.42. |
| 10 | **Deploy** | Five production use cases (below). |

**Cost detail worth keeping.** The flight demo's reported **$0.0039** covers 90,558 Jev input tokens plus a text helper's charge. Browser costs sit outside it. The ~**7-second** clock starts after the initial page observation and excludes post-run verification. It finds flights; **it does not book tickets**.

**The 10-step confidence caveat is explicit:** confidence is not an accuracy percentage. Use labeled examples from your own workflow to set the threshold.

**Five deploy cases.**

| Case | Builder | Reported result |
|------|---------|-----------------|
| Control a browser | Browser Use | Flights found in 7s for $0.0039. Jev selects action and page element. |
| Classify research | **Hassan** | **1,018 AI research papers for $0.08**, 256ms median end-to-end latency per paper. |
| Triage inbox | **Riley Brown** | **500 emails classified for 3.5¢.** Options: reply / research / wait / review. |
| Route tasks between models | LangChain | Simple → fast model; complex → reasoning model. |
| Instant context compaction | **Tamara** / **Alex Volkov** | Volkov measured **1 second to compact a Claude session from nearly 1M tokens to 86K**. Scored every tool call, dropped irrelevant ones — a relevance filter, not a summarization pass. |

**Harness-over-model claim.** The post asserts the harness is the difference between 78% and 42% on the same model — same weights, different loop engineering. Present this as the author's claim; the number is not sourced in the article.

**Two safety/performance data points.** Vercel's **fx** team reported roughly **5–18x faster safety classification than GPT-5.6-Luna**, with improved accuracy — that compares the classifier, not a full agent run. Browser Use's optimized runtime cut median browser protocol calls from **1,092 to 101** while median task time fell 25% across three matched pairs, same models.

**Cemini reading.** FILE. Compaction is already **K264** (`fast-jev-compaction`) — do not re-open. The email-triage and paper-classification analogs map to Atto (redacted type) and CeminiDFS (review CSV citation) as **FILE patterns only**. **200x / 400x / 78%-vs-42% are vendor or author claims** — cite them as claims, never as Cemini measurements. **0 product Integrate GO.**

## Snippets

> "If the operation creates text, it stays with the LLM. If the operation picks an option from a list, scores a value, or answers yes/no, it goes to Jev." [Source: x-article-0xmovez-jev-engineering-10-steps-2026-09-19.md]

> "The confidence threshold is set to 0.85. Adjust it using labeled examples from your workflow. Confidence is not an accuracy percentage." [Source: x-article-0xmovez-jev-engineering-10-steps-2026-09-19.md]

> "Hassan used Jev to classify 1,018 AI research papers. The entire classification cost $0.08, with 256ms median end-to-end latency per paper." [Source: x-article-0xmovez-jev-engineering-10-steps-2026-09-19.md]

> "Alex Volkov tested it: 1 second to compact a Claude session from nearly 1M tokens to 86K." [Source: x-article-0xmovez-jev-engineering-10-steps-2026-09-19.md]

> "The harness is the difference between 78% and 42% on the same model. Same weights. Different loop engineering." [Source: x-article-0xmovez-jev-engineering-10-steps-2026-09-19.md] — author claim, unsourced.
