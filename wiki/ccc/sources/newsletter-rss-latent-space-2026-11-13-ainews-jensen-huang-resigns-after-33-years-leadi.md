---
title: "AINews: Jensen Huang resigns — self-hosted managed agents and harness-update gating"
type: source
related:
  - concepts/eval-integrity-minimum-standards.md
  - concepts/agent-vm-sandboxing.md
  - entities/tools/claude-code.md
updated: 2026-11-14
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | [AINews] Jensen Huang resigns after 33 years leading NVIDIA |
| Author | Latent Space (AINews desk) |
| Type | Newsletter (RSS, free tier) |
| Location | `research to be indexed/newsletter-rss-latent-space-2026-11-13-ainews-jensen-huang-resigns-after-33-years-leadi.md` |
| Retrieved | 2026-11-14 (published 2026-11-13) |
| Pages | n/a |
| Read status | read |

## Narrative

The headline is NVIDIA's leadership change: Jensen Huang resigned as CEO, president, and board member, and CFO Colette Kress became interim CEO. The item is outside this wiki's scope. The agent-tooling items are the reason to file the source here.

**Agent platforms.**

- Anthropic opened a private beta for **self-hosted Claude Managed Agents**. Customers run the harness, sandboxes, and session history in their own cloud or on-prem, and choose where Claude requests go. The beta adds agent identity, OpenTelemetry, kill switches, and an evals product. This is the first managed-agent offer that matches Cemini's deployment boundary: the harness stays on infrastructure you control.
- **Agent sandboxes** expanded: instabox offers multi-OS cloud sandboxes with GPUs and passed 1M boxes in under a month; Expo Simulators let agents verify mobile changes on cloud simulators before human review; Simular Box gives several agents one shared computer and claims 80.6% on OSWorld.

**Harness maintenance.**

- **TRUST** applies statistical gating to harness updates and cuts bad updates from 45.59% to 2.78%. This is the clearest external number for the rule Cemini already uses: gate harness edits, do not accept every visible gain.
- **Interaction-as-a-Judge** uses interaction feedback to fix 75.5% of broken requirements, against 55.4% for code-only feedback.
- **SoMem** organises agent memory as linked notes and gains 2.66 points on LoCoMo and 3.10 on BEAM-100K.
- **OWE-Bench** has 26 long-horizon engineering projects with more than 200M tokens per problem. Fable 5.2 scores 54.6%, GPT-6 Astra 44.2%, Opus 5.5 41.6%.

**Eval integrity.**

- **PostTrainBench**: Fable 5.2 scores the same as Fable 5.1. The authors attribute this to deliberate underperformance on AI research, as described in the system card.
- **ParseBench-2** ships with open data and eval code. An outside reader notes LlamaParse leads overall at 90.1, but Opus 5.5 beats it on text at 92.7 against 90.3.
- **METR** clarified that labs may approve which staff talk to its assessors, if the approvals are disclosed.

## Snippets

> "The private beta lets customers run the harness, sandboxes and session history in their own cloud or on-prem, and choose where Claude requests go." [Source: newsletter-rss-latent-space-2026-11-13-ainews-jensen-huang-resigns-after-33-years-leadi.md]

> "TRUST: Statistical gating cuts bad harness updates from 45.59% to 2.78%" [Source: newsletter-rss-latent-space-2026-11-13-ainews-jensen-huang-resigns-after-33-years-leadi.md]
