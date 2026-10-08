---
title: "The Pragmatic Engineer — Building resilient systems with Sam Newman (2026-10-07)"
type: source
tags: [source, k285, engineering, resilience, architecture, ccc, ai-risk]
keywords: [sam-newman, microservices, distributed-systems, idempotency, resilience, cognitive-debt, cognitive-surrender, module-boundaries, llm-causality]
related:
  - concepts/k285-feeds-wave.md
  - concepts/agentic-code-quality-gates.md
maturity: draft
created: 2026-10-08
updated: 2026-10-08
read_status: read
---

## Relations

- @concepts/k285-feeds-wave.md
- @concepts/agentic-code-quality-gates.md

## Raw Concept

| Title | Building resilient systems with Sam Newman |
| Source | The Pragmatic Engineer podcast (Substack) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/newsletter-rss-pragmatic-engineer-2026-10-07-building-resilient-systems-with-sam-newman.md` |
| Retrieved | 2026-10-07 |
| URL | https://newsletter.pragmaticengineer.com/p/building-resilient-systems-with-sam |
| Tier | free (RSS) |
| cross-wiki | ccc-wiki |
| read-status | read |

## Narrative

Sam Newman (*Building Microservices*; new book *Building Resilient Distributed Systems*, out 2026-10-07) on distributed systems and how AI changes them. It lands two hard points relevant to the agent lanes.

### The three rules of distributed systems

Newman collapses the eight fallacies to three:
1. **Information takes time to travel** (speed of light).
2. **Sometimes the thing you want is not there** (resources go offline).
3. **Resources are not infinite** (CPU, memory, storage, bandwidth run out).

Most outages he has seen come from **#3 — resource pools running out.** Also: **idempotency** via keys (clean but hard to retrofit) vs **fingerprints** (easy to retrofit but can reject legitimate requests — a Danish payment system rejected same-value purchases within 5 minutes).

### Four concepts of resilience

**Robustness** · **Rebound** (recovery speed) · **Extensibility** · **Adaptability**. A caveat worth keeping: **robustness adds complexity, and complexity adds failure modes.**

### The AI points (why this page matters)

- **Hedge the vendors.** Which AI companies survive is unknown, so design **multi-vendor, multi-model**, and consider **replacing LLM functionality with deterministic code** where it is faster and cheaper.
- **Resist "cognitive surrender."** More AI use can mean **less** critical thinking, more context switching, longer hours. He used NotebookLM for research but **manually checked every link** it surfaced.
- **Modules first.** Think carefully about module boundaries, then let the AI roam **freely but only inside that structure.**
- **The sharpest point — LLMs are not world models.** "Why did the LLM delete my database? Because it has no concept of causality … LLMs are not world models." He argues **guardrails are not the right long-term solution** because of this. The article pairs it with an incident: **Opus 5.5 formatted a dev's C: drive under `--dangerously-skip-permissions`.**

### Why it matters here

The **"LLMs have no concept of causality, so guardrails are not the long-term answer"** argument is the strongest framing yet for the wiki's **deterministic-gate** doctrine — prefer hard gates and sandboxes to prompt-level guardrails. Pairs with `agentic-code-quality-gates` and the K284 code-review-theater finding. Route: CCC. **No `/route` swap.**

## Snippets

> "Why did the LLM delete my database? Well, because it has no concept of causality. They have no concept that if I do A, B happens." [Source: newsletter-rss-pragmatic-engineer-2026-10-07-building-resilient-systems-with-sam-newman.md]

> "We must resist 'cognitive surrender' to AI … much of our current use of AI is not freeing us up from critical thinking! It's causing more context switching and leaving less time for thinking." [Source: newsletter-rss-pragmatic-engineer-2026-10-07-building-resilient-systems-with-sam-newman.md]

> "When you use AI, allow it to roam freely, but only inside the module structure that you have designed." [Source: newsletter-rss-pragmatic-engineer-2026-10-07-building-resilient-systems-with-sam-newman.md]
