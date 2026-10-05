---
title: K282 Agent-Eval Wave (Oct 2026)
type: concept
tags: [k282, arxiv, agent-security, agent-eval, harness, benchmark, local-abliterated-lab]
keywords: [k282, evoriskbench, powerbench, jailbreak, moe-router, kinetic-theory, hyperbrowsecomp, finskillsbench]
related:
  - concepts/k282-level-editors-wave.md
  - concepts/k282-feeds-wave.md
  - concepts/active-project-research-routing.md
  - sources/arxiv-2610.03153-evoriskbench-runtime-2026-10-05.md
  - sources/arxiv-2610.02303-powerbench-bias-2026-10-05.md
  - sources/arxiv-2610.02827-mlcommons-jailbreak-2026-10-05.md
  - sources/arxiv-2610.02910-moe-router-gradient-2026-10-05.md
  - sources/arxiv-2610.03243-kinetic-gated-evolution-2026-10-05.md
  - sources/arxiv-2610.03564-finskillsbench-2026-10-05.md
  - sources/arxiv-2610.03574-hyperbrowsecomp-2026-10-05.md
maturity: draft
created: 2026-10-05
updated: 2026-10-05
harness_verb: FILE
wire_status: policy_wired
---

## Relations

- @concepts/k282-level-editors-wave.md
- @concepts/k282-feeds-wave.md
- @concepts/active-project-research-routing.md
- @sources/arxiv-2610.03153-evoriskbench-runtime-2026-10-05.md
- @sources/arxiv-2610.02303-powerbench-bias-2026-10-05.md
- @sources/arxiv-2610.02827-mlcommons-jailbreak-2026-10-05.md
- @sources/arxiv-2610.02910-moe-router-gradient-2026-10-05.md
- @sources/arxiv-2610.03243-kinetic-gated-evolution-2026-10-05.md
- @sources/arxiv-2610.03564-finskillsbench-2026-10-05.md
- @sources/arxiv-2610.03574-hyperbrowsecomp-2026-10-05.md

## Raw Concept

K282 agent-eval cluster. Seven arXiv papers that measure agent safety, refusal, skill gates, and browsing. Dual-ID **OSINT K282** (the same day's eval docx is a separate hub, @concepts/k282-level-editors-wave.md).

## Narrative

Seven papers, one theme: **how to measure an agent**. They split into three lanes.

### Lane 1 — runtime security (the actionable one)

**EvoRiskBench** (@sources/arxiv-2610.03153-evoriskbench-runtime-2026-10-05.md). Nine model × harness configs; injection arrives through **MCP tools, skills, and subagents**. Aggregate attack success **37.46%**; worst config **68.44%** (DeepSeek-V4-Pro-0813 × Codex). **Model spread (54.37 pp) ≫ harness spread (5.41 pp)** — the harness is second-order but still a factor we control. This is the first number we have for indirect-prompt-injection risk across our own harness class. Routed to the cybersec lane and the CCC lane.

### Lane 2 — refusal and jailbreak surfaces

- **PowerBench** (@sources/arxiv-2610.02303-powerbench-bias-2026-10-05.md) — refusal ranks power-grabbing > disempowerment > self-empowerment; average 1.0%–35.1%; refusal **triples** at society scale; AI-agent requesters are refused more than humans.
- **MLCommons Jailbreak Benchmark v1.0** (@sources/arxiv-2610.02827-mlcommons-jailbreak-2026-10-05.md) — unsafe-response rate **11.08% → 18.65%**; average **Resilience Gap 7.57 pp**. The reusable idea is the **paired metric**: attack result measured against a baseline.
- **MoE router gradient** (@sources/arxiv-2610.02910-moe-router-gradient-2026-10-05.md) — router-gradient expert selection cuts refusals more than activation frequency in 24 of 25 conditions; OLMoE **34 → 9 of 100**. A local-abliterated-lab technique, and dual-use.

### Lane 3 — skill gates and browsing agents

- **Kinetic theory of the gated self-evolving agent** (@sources/arxiv-2610.03243-kinetic-gated-evolution-2026-10-05.md) — fluctuation scaling flat at sparse skill density (β = −0.04), **−0.58 at tripled density**; a **separation theorem** keeps the evaluator outside the population. This is the theory under our step gate.
- **HyperBrowseComp** (@sources/arxiv-2610.03574-hyperbrowsecomp-2026-10-05.md) — 423 questions, 13 languages, multimodal; best **31.68%**; **57.68% shared failures**; humans 15/30. It exercises **Exa**, the workspace's external-research path.
- **Financial agent skills** (@sources/arxiv-2610.03564-finskillsbench-2026-10-05.md) — curated skills **+16.2 pts**, self-generated **+0.5**, tools **+19.5**, docs **+5.6** (subadditive); a 9-stage workflow shows **"silent competence"** (optimality 0.934, mandate adherence 0/33). **Curated skills beat self-generated** — the numbers behind our skill-audit discipline.

### Boundary

**FILE only. No install. No clone. No PoC run.** The papers route to cybersec and CCC as briefs. 0 product Integrate GO.

## Snippets

> "Model spread (54.37 pp) ≫ harness spread (5.41 pp)." [Source: arxiv-2610.03153-evoriskbench-runtime-2026-10-05.pdf]

> "Refusal triples when the request is framed at society scale." [Source: arxiv-2610.02303-powerbench-bias-2026-10-05.pdf]

> "Curated skills +16.2 pts; self-generated skills +0.5." [Source: arxiv-2610.03564-finskillsbench-2026-10-05.pdf]
