---
title: "Runtime pattern relationships decay under routine operations"
type: concept
related:
  - sources/arxiv-routine-operations-break-patterns-2611.09088.md
  - concepts/hooks-for-automation.md
  - concepts/truncate-only-long-horizon-compaction.md
  - concepts/harness-security-axis-comparison.md
updated: 2026-11-10
---

## Raw Concept

Question this page answers: if a guardrail plugin is installed and enabled, did it run?

Synthesised from `@sources/arxiv-routine-operations-break-patterns-2611.09088.md`.

## Narrative

The paper studies five required relationships across three architectural patterns: Guardrail Enforcement Point, Autonomy Controller, and Blackboard. It examines five released harnesses and fourteen independently written plugins.

Two **carriers** hold a relationship in place:

- **Runtime order** — which callback runs first, and whether it passes the call on.
- **Retained state** — saved rules, cached provenance, or an instance field.

Normal operations change the carrier without changing any code: reapplying a plugin, saving a preference, re-registering after a mode switch, or compacting history.

### Two documented failures

**DeepSeek Harness.** Policy ran first in observe mode. Switching to enforce mode re-registered the policy callback behind the approval plugin. The operator approved a prohibited edit and it executed with no policy decision. Re-enabling the approval plugin restored the order and the check.

**OpenCode 2.2.5.** An earlier "always allow" reply saved a rule. The permission stage then treated a prohibited edit as already allowed. The policy reviewer abstained, because its trigger was "requests needing approval" and none was pending. The edit executed.

A third case: compaction replaced an earlier conversation interval with a summary while keeping the tail verbatim. A source label attached to untrusted content could be removed by compaction, contrary to the provider promise.

### The rule

**A pattern relationship is a property of the running system and its history.** It is not a configuration value.

### Application to Cemini hooks

Cemini runs `PreToolUse` and `PostToolUse` hooks, `step-gate`, and policy wires in `.cursor/rules/`. The failure modes map directly:

- Install order is not execution order after any settings reload.
- A saved allow rule can silence a later policy check.
- Compaction can drop a provenance label that a guardrail depends on.

Practical checks:

1. After any settings or hook change, run one known-bad action and confirm it was **blocked with a record**. Do not infer from the hook file.
2. Give every guardrail a record independent of the tool result, such as a log line, so that "not exercised" is visible.
3. Treat compaction as an operation that can remove labels, and re-attach them after compaction.

## Snippets

> "After a policy plugin was reapplied or an edit allow rule was saved, a prohibited edit executed without policy evaluation even though the participating plugins were active." [Source: arxiv-2611.09088-when-routine-operations-break-architectural-patt.pdf p.1]
