---

title: "Microsoft Agent Governance Toolkit"
type: entity
tags: [tool, extract, mit, k198, atto, ccc]
keywords: [agent-governance-toolkit, Microsoft, MIT, AGM]
related:
  - sources/eval-revenue-stack-url-evaluation-2026-07-28.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/verifier-deployment-gap.md
  - entities/tools/agent-governance-manifest.md
  - entities/tools/aisuite.md
maturity: draft
created: 2026-07-28
updated: 2026-07-31
phase_0_verdict: EXTRACT — K198 MIT shallow adopt
harness_verb: FILE
wire_note: large REFERENCE; use manifest patterns only
---

## Relations

- @sources/eval-revenue-stack-url-evaluation-2026-07-28.md
- @concepts/wiki-tooling-evaluation.md
- @concepts/verifier-deployment-gap.md
- @entities/tools/agent-governance-manifest.md — distinct AGM paper/repo
- @entities/tools/aisuite.md — combo Extract

## Raw Concept

| Field | Value |
|-------|-------|
| **Repo** | https://github.com/microsoft/agent-governance-toolkit |
| **License** | MIT `[CONFIRMED]` |
| **Local** | `.local/adopts/agent-governance-toolkit` (~85MB) |
| **Stars** | ~5k (2026-07-28) |

## Narrative

Microsoft toolkit for agent governance patterns (policy/guardrails). **Extract** for Atto MCP allowlist + CCC harness — do not confuse with `agent-governance-manifest` (AGM paper prototype). Pair with aisuite for provider failover under governed calls.
