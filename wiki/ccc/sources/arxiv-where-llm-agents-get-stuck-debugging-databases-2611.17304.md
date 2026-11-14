---
title: "Where LLM agents get stuck debugging databases — access, more than reasoning"
type: source
related:
  - concepts/production-state-access-bottleneck.md
  - concepts/failed-trajectory-harness-repair.md
  - concepts/agent-trace-tampering-audit-gap.md
  - concepts/agent-completion-verification-gates.md
updated: 2026-11-14
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Where LLM Agents Get Stuck Debugging Databases: Access More Than Reasoning |
| Author | Gustavo Pinto (Federal University of Pará, UFPA) |
| Type | arXiv preprint, 2611.17304 |
| Location | `research to be indexed/ccc/arxiv-2611.17304-where-llm-agents-get-stuck-debugging-databases-a.pdf` |
| Retrieved | 2026-11-14 |
| Pages | 12 |
| Read status | read |

## Narrative

This is a field observation, not a benchmark. The author follows **Claude Code** as it diagnoses eight database incidents in a production message-dispatch engine over ten days.

The behaviour pattern is repeated self-correction. The agent announces a cause, ships a fix, and later walks the fix back. Each wrong guess costs a deploy-and-observe cycle. Across the eight incidents the agent shipped 22 fix commits. All five incidents whose root cause depended on runtime concurrency began with a false start. The throughput incident alone burned six hypotheses before a configuration value, the retry-sweep cap, was found.

The central finding is about **access**, not model skill. An access gap was present in all five concurrency-dependent incidents: alone in one, and combined with a reasoning error in four. No incident was limited by reasoning alone.

Missing access took four forms:

- A live `pg_locks` view.
- An untruncated deadlock `DETAIL` record.
- Read-only SQL execution against production.
- An explicit statement of the environment context.

The three incidents that did not depend on concurrency needed nothing beyond what the agent already had. Where reasoning did fail, it failed next to an access gap that shaped the error: anchoring on an early cause, not inspecting the configuration, or misreading transaction semantics.

The proposed remedy is a **forensics layer** inside existing security controls. It has three parts: a safe interrogation API, a lock-and-deadlock flight recorder, and a production replay harness. The paper states the implication directly. In this setting the instrumentation was at least as binding as the model.

A useful caution: the agent ran mostly on an efficient open-weights model, with a frontier model as a minority. The study did not attribute each hypothesis to a model, so it neither supports nor undermines the access thesis.

## Snippets

> "In every incident whose root cause depended on runtime concurrency, the agent announced a cause, shipped a fix, and later walked it back, and each wrong guess cost a deploy-and-observe cycle." [Source: arxiv-2611.17304-where-llm-agents-get-stuck-debugging-databases-a.pdf p.1]

> "in our observation, access to production state was the most pervasive limit on the agent's diagnosis" [Source: arxiv-2611.17304-where-llm-agents-get-stuck-debugging-databases-a.pdf p.8]
