---
title: "Frontier-led SLM delegation — the expensive model keeps the wheel"
type: concept
related:
  - sources/arxiv-delegent-multi-agent-harness-cost-2611.33098.md
  - entities/tools/claude-code.md
  - concepts/subagent-orchestration.md
  - concepts/timeout-cascade-cost-aware-routing.md
  - concepts/decision-model-hybrid-agent-routing.md
updated: 2026-11-25
---

## Raw Concept

Question this page answers: can a local small model cut frontier cost without routing the whole task to it? Synthesised from `@sources/arxiv-delegent-multi-agent-harness-cost-2611.33098.md` (2611.33098).

## Narrative

The dominant cost pattern is cheap-first: run the small model, escalate on failure. That pattern fails when the small model cannot do the task at all, which is usual below about 7B.

**Frontier-led delegation inverts the pattern.** The frontier model keeps the task. It plans, delegates bounded subtasks to a local SLM, checks the returned evidence, and writes the final answer. The SLM does legwork: locate code, reproduce a bug, run tests, search a corpus.

Delegent implements this on stock Claude Code with a relay in front of the model API. The relay routes by model name. Main-loop calls go to the frontier model. Subagent calls go to the SLM. Nothing is trained, so either model can be swapped.

Measured cost, with a 27B local SLM:

- Long-horizon coding: frontier cost falls 67% with no loss in resolved tasks.
- Agentic search: frontier cost falls 59% over 694 questions, same correct count.
- A 2B laptop-class SLM also reaches 66% coding-cost reduction.

Why it works: the expensive model pays for context on every step it takes. Fewer frontier steps mean less context re-read. The SLM absorbs tool output and returns a short report. The frontier model never sees the raw tool chatter.

**Two conditions.** First, the frontier model must read every SLM output before it is used. Unchecked delegation reintroduces the error problem. Second, the delegation brief must be narrow. Broad delegation turns into the SLM doing the task.

**Trade-off.** Delegation adds latency, bounded by the local hardware that serves the SLM. It also adds a moving part: a relay that must route correctly by model name.

**Status.** One paper, one frontier model, two SLMs. Results are self-reported. [TENTATIVE]

## Snippets

> "A small language model running on local hardware can take over the easy subtasks of a frontier model, cutting its cost substantially without hurting task performance, and without any training." [Source: `arxiv-2611.33098-delegent-a-multi-agent-harness-that-reduces-cost.pdf` p.1, retrieved 2026-11-25]
