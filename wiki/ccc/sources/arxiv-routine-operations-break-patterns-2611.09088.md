---
title: "When routine operations break architectural pattern relationships in agent harnesses"
type: source
related:
  - concepts/runtime-pattern-relationship-decay.md
  - concepts/hooks-for-automation.md
  - concepts/truncate-only-long-horizon-compaction.md
  - concepts/harness-security-axis-comparison.md
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | When Routine Operations Break Architectural Pattern Relationships in LLM Agent Harnesses |
| Author | Boming Xia, Qinghua Lu, Dino Sejdinovic, Liming Zhu (CSIRO, Adelaide University, UNSW) |
| Type | arXiv paper (cs.SE), 2611.09088 |
| Location | `research to be indexed/ccc/arxiv-2611.09088-when-routine-operations-break-architectural-patt.pdf` |
| Retrieved | 2026-11-10 |
| Pages | 12 |
| Read status | read |

## Narrative

An LLM harness spreads tool mediation, state, and guardrails across native services, third-party plugins, and configuration. The paper asks whether the required relationships between those parts survive normal operations. It studies five relationships tied to three patterns: Guardrail Enforcement Point, Autonomy Controller, and Blackboard. It examines five released harnesses and fourteen independently written plugins.

The central finding is a real and reproducible failure. **Plugin callback order is not a stable configuration value; it is a property of runtime history.** In DeepSeek Harness, switching from observe mode to enforce mode re-registered the policy callback behind the approval plugin. The operator then approved a prohibited edit, and it executed with no policy decision. Disabling and re-enabling the approval plugin restored evaluation. The same enabled plugins and the same final settings gave different coverage after different operations.

A second failure used retained state. In OpenCode 2.2.5, an earlier "always allow" reply saved a rule. The permission stage then treated a prohibited edit as already allowed, the policy reviewer abstained because no approval was pending, and the edit executed.

A third case used compaction. Compaction replaced an earlier interval of the conversation with a summary and kept the tail verbatim. A label attached to untrusted content could be removed by compaction, which the provider promise said must not happen.

The authors offer **PatternOps**: derive requirements from the pattern description, the provider documentation, and the deployment profile, then bind each requirement to a provider and a carrier. A carrier is either runtime order or retained state. They also separate three requirement strengths: prevent the prohibited effect, let the designated policy decide, and evaluate every admitted edit.

The lesson for Cemini is direct. A hook or plugin that is installed and enabled is not the same as a hook that ran. Verify by trace, and re-verify after any mode switch, plugin reload, or compaction.

## Snippets

> "The same enabled plugins and final settings thus gave different policy coverage after different operations." [Source: arxiv-2611.09088-when-routine-operations-break-architectural-patt.pdf p.1]

> "In these harnesses, a pattern relationship is a property of the running system and its history." [Source: arxiv-2611.09088-when-routine-operations-break-architectural-patt.pdf p.1]
