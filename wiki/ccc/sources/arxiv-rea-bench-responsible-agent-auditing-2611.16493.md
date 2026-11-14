---
title: "ReA-Bench — six diagnostic tiers for auditing responsible agent behaviour"
type: source
related:
  - concepts/trajectory-audit-diagnostic-tiers.md
  - concepts/trajectory-driven-safety-harness-evolution.md
  - concepts/agent-trace-tampering-audit-gap.md
updated: 2026-11-14
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | ReA-Bench: Benchmarking Responsible Agent Auditing |
| Author | Zipeng Ye, Shenyu Dai, Yong Xie, Kun Wang, Jiyang Guan, Zhikai Chen, Jiaqi Weng, Jialing Tao, Hui Xue (Alibaba AAIG) |
| Type | arXiv preprint (cs.AI), 2611.16493; dated 2026-11-06 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2611.16493-rea-bench-benchmarking-responsible-agent-auditin.pdf` |
| Retrieved | 2026-11-14 |
| Pages | 50 |
| Read status | read |

## Narrative

ReA-Bench grades the **auditor**, not the agent. An auditor reads a recorded execution trajectory and reports risky steps. The paper argues that overall recall hides which risks are missed and whether higher recall costs more false positives on legitimate behaviour.

Six tiers organise the audit challenge:

| Tier | What the auditor must do |
|------|--------------------------|
| L1 | Know the harm from the action and its context |
| L2 | Find contradictions inside the trajectory |
| L3 | Retrieve evidence from a long context (evidence dilution) |
| L4 | Check provenance of sources and the logic of the conclusion |
| L5 | Recognise indirect steering |
| L6 | Work with information the trajectory never recorded |

The benchmark holds 587 trajectories: 304 risky, 177 benign, 106 control versions. Most samples come from production and red-team data, adapted with LLM assistance, human review, and code checks. L1 alone covers 38 risk types across six domains.

The design adds two contrasts. **Hard benign cases** look like risky actions but satisfy task and authorisation conditions. **Paired versions** shorten a trajectory or supply the missing information, so the same judgement can be compared across evidence conditions.

Results are diagnostic. A proposed global-summary-assisted (GSA) method raises recall on four configurations, for example Grok-low from 69.6% to 87.5%. False-positive rate also rises, and GPT-luna goes from 49.2% to 74.0%. Shortening trajectories moves few judgements: 87.1%–89.2% of paired decisions stay on the same side of the threshold. Many risks stay missed even when the evidence is easier to find.

The paper's operational point for Cemini: a single recall number cannot decide the audit design. A post-hoc reviewer can accept cost for recall. A runtime blocker must protect the false-positive budget.

## Snippets

> "In ReA-Bench, most samples are derived from real production trajectories, with high-quality scenarios manually selected and adapted." [Source: arxiv-2611.16493-rea-bench-benchmarking-responsible-agent-auditin.pdf p.1]

> "Shortening the input and highlighting the evidence still do not resolve every judgment error." [Source: arxiv-2611.16493-rea-bench-benchmarking-responsible-agent-auditin.pdf p.19]
