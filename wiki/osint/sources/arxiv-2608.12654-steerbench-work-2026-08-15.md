---
title: "SteerBench-Work — agent steering at action boundaries (arXiv 2608.12654, K239)"
type: source
tags: [arxiv, agent-safety, hitl, ccc, k239]
keywords: [SteerBench-Work, action-boundary, proceed-or-hold, over-refusal, under-refusal, HITL, steerbench.com]
related:
  - concepts/agent-steering-action-boundary.md
  - concepts/practical-loop-engineering.md
  - sources/arxiv-2608.13304-wifa-intent-not-form-2026-08-15.md
  - sources/arxiv-2608.12821-hiroute-2026-08-15.md
  - sources/substack-rss-addy-osmani-2026-08-14-practical-loop-engineering.md
maturity: draft
created: 2026-08-15
updated: 2026-08-15
read_status: read
---

## Relations

- @concepts/agent-steering-action-boundary.md — synthesized proceed/hold gate
- @concepts/practical-loop-engineering.md — /goal /loop stop-conditions pair with the gate
- @sources/arxiv-2608.13304-wifa-intent-not-form-2026-08-15.md — refuse intent not wrapper form
- @sources/arxiv-2608.12821-hiroute-2026-08-15.md — routed safety prompts at the same boundary
- @sources/substack-rss-addy-osmani-2026-08-14-practical-loop-engineering.md — HITL / don't delegate judgment

## Raw Concept

| Field | Value |
|-------|--------|
| Paper | arXiv:2608.12654, "SteerBench-Work: A Benchmark for Agent Steering at Action Boundaries" |
| Author | Oguz Serdar, Cuneyt Mertayak (AgentDock) |
| Retrieved | 2026-08-15 |
| File | `arxiv-2608.12654-steerbench-work-a-benchmark-for-agent-steering-a.pdf` |
| sha256 | `071af41df7e2f06cb0c5cff9d4e37b3ae1261d81e5155b95c35c3e01b4f5fd50` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.12654-steerbench-work-a-benchmark-for-agent-steering-a.pdf` |
| Type | cs.AI preprint, 18pp, Aug 2026 |
| Leaderboard | https://steerbench.com |

## Narrative

Workplace agents fail at the **pre-commit action boundary**: the last decision before a tool call changes external state (send email, merge PR, wire payment). SteerBench-Work scores a binary **proceed vs hold** given the trace, the candidate action, and the evidence on hand.

Release v2026-05: **106 incident-anchored scenarios** across developer ops, CS, finance, legal, medical, HR, security. Labels split nearly evenly proceed/hold. Paired **evidence-reversed mirrors** test whether the gate follows evidence or the famous-incident prior.

### Headline result `[TENTATIVE]` (single paper)

Across 30 model conditions, errors run one way: **over-refusal 28.1%** (hold authorized, evidence-cleared work) vs **under-refusal 1.0%** (allow unsafe work). Sensitivity: drop 17 derived-risk-flag rows → 19.4% / 1.25%; three-rater majority relabel → 41.1% / 0.36%. Hardest slice is **risk-resolved commits** (signed evidence already cleared a real trigger). Models score **63.8%** on evidence-reversed mirrors of famous incidents vs **98.5%** on the incidents themselves.

Capability ≠ calibration: stronger models over-refuse at the commit boundary. Extra reasoning can repair a weak gate while leaving a calibrated gate flat or slightly worse.

### Cemini steal (CCC /route + OSINT K239 HITL)

- Wire a **proceed/hold gate** at state-changing tool calls (`scp` to prod, Discord LIVE, watch-file writes, skill auto-evolve). Default: **HITL hold**.
- Do **not** treat "the model is smarter" as a reason to drop the gate.
- Dual-ID: **OSINT K239** = this SteerBench ingest. **CCC K239** = Datumpont / execution-fidelity. Resolve by file+wiki, not bare K#.
- **No unattended auto-evolve** of `.cursor/skills/*` (pairs skill-misevolution K237).

**Brief:** `../Cemini claude code CCC/briefs/2026-08-15_k239-ccc-steerbench-flue-loop.md`.

## Snippets

> "The steering decision is the pre-commit choice at that boundary: proceed, or hold for human or policy review." [Source: arxiv-2608.12654 p.1]

> "The failures run almost entirely in one direction: models wrongly hold authorized, evidence-cleared work on 28.1% of opportunities and wrongly allow unsafe work on 1.0%." [Source: arxiv-2608.12654 abstract]
