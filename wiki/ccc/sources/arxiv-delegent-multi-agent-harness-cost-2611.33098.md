---
title: "Delegent — multi-agent harness that cuts frontier cost (2611.33098)"
type: source
related:
  - concepts/frontier-led-slm-delegation.md
  - entities/tools/claude-code.md
  - concepts/timeout-cascade-cost-aware-routing.md
  - concepts/decision-model-hybrid-agent-routing.md
  - concepts/subagent-orchestration.md
updated: 2026-11-25
read_status: read
maturity: draft
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Delegent: A Multi-Agent Harness That Reduces Cost without Sacrificing Performance |
| Author | Lingwei Gu, Jimmy Lin (University of Waterloo, David R. Cheriton School) |
| Type | arXiv preprint (cs.AI) |
| ID | 2611.33098v1, 24 Nov 2026 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2611.33098-delegent-a-multi-agent-harness-that-reduces-cost.pdfarxiv-2611.33098-delegent-a-multi-agent-harness-that-reduces-cost.pdf
| Retrieved | 2026-11-25 |
| File | `arxiv-2611.33098-delegent-a-multi-agent-harness-that-reduces-cost.pdf` |
| Pages | 11 |
| Read status | read (abstract, intro, harness section) |
| Code | https://github.com/castorini/delegent |

## Narrative

Delegent is a harness, not a model. It starts from stock **Claude Code** and adds an SLM team member. The frontier model stays in charge of every task. It plans, decides what to delegate, judges what comes back, and writes the final patch or answer. Small-language-model subagents do the legwork in their own tool loops with fresh context.

The mechanism is a relay. The relay speaks the Anthropic Messages API, so Claude Code runs unmodified. It routes each call by the model name in the call: main-loop calls go to the frontier model, subagent and auxiliary-model calls go to the local SLM. Concurrent frontier calls share one prompt-cache key. SLM calls go through vLLM, pinned to one GPU replica per subagent.

For search, Delegent adds a `Delegate` tool. Its subagent borrows prompts and tools from AREX-Turbo, a 4B deep-research agent. The report returns an answer, evidence lines, and a confidence. The harness checks each evidence line against the cited document. The frontier model sees only the final report, never the subagent tool output.

Results with GPT-6.1-Sol at high effort and Qwen3.8-27B-FP8 as SLM:

- DeepSWE coding cost falls to a third, with no loss in resolved tasks.
- Agentic search cost falls to 41% over 694 questions, with the same number of correct answers.
- MiniCPM5-2B, a 2B model that fits on a laptop, also cuts DeepSWE cost to a third.
- With the 27B SLM priced at API rates, total DeepSWE task cost is still 38%.

This is not a cascade and not a router. In a cascade or a router, one model gets the whole task and must solve it alone. Here the frontier model always produces the final answer. No SLM output is accepted without the frontier model reading it first.

**Why it matters for `/route`.** The workspace already runs a frontier-led lane with a cheap implementer. Delegent gives a measured, training-free version of that design inside Claude Code. The cost saving comes from moving tool-heavy legwork to a local SLM, not from routing the whole task down. Delegation adds latency, bounded by local hardware.

All numbers come from one paper. [TENTATIVE]

## Snippets

> "No router or model is trained, so either model can be swapped freely." [Source: `arxiv-2611.33098-delegent-a-multi-agent-harness-that-reduces-cost.pdf` p.1, retrieved 2026-11-25]

> "In Delegent, the frontier model always produces the final answer, and the SLM only does the legwork." [Source: `arxiv-2611.33098-delegent-a-multi-agent-harness-that-reduces-cost.pdf` p.2, retrieved 2026-11-25]
