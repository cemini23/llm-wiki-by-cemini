---
title: "SHE — Trajectory-driven Safety Harness Evolution for LLM Agents"
type: source
tags: [arxiv, k232, ccc, cyber]
keywords: [2608.09885, safety-harness, harness-evolution, rule-bank, tool-policy, agent-safety]
related:
  - entities/tools/she-safety-harness.md
  - concepts/ralph-autonomous-agent-pattern.md
maturity: draft
created: 2026-08-11
updated: 2026-08-11
read_status: skimmed
---

## Relations
- @ccc-wiki/briefs/2026-08-11_2026-08-11_k232-she-harness-wave.md  (cross-wiki brief)

- @entities/tools/she-safety-harness.md
- @concepts/ralph-autonomous-agent-pattern.md

## Raw Concept

| Field | Value |
|-------|--------|
| arXiv | 2608.09885 |
| sha256 | `146578c6c93ae4b9527852ffaad32004a90cd0c49f7a1f0726f748047afd4181` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.09885-she-trajectory-driven-safety-harness-evolution-f.pdf` |
| retrieved | 2026-08-11 |

## Narrative

SHE (Shanghai AI Laboratory AgentDoG team; Qu, Mao et al., 15 pp) treats the agent safety harness as an **evolvable object** rather than a fixed deployment artifact. It decouples the harness into four editable artifacts — **System Prompt**, **Rule Bank**, **Safety Memory**, **Tool Policy** — each with an explicit safety responsibility. An attribution-guided evolution loop converts trajectory failures into structured diagnoses, routes each to the smallest responsible artifact, proposes bounded edits, and retains only harnesses that pass safety–utility validation (holding the base LLM, environment, and evaluation protocol fixed).

On Agent-SafetyBench: ASR 8.6%→5.5% (vs static SafeHarness 17.1%→5.5%, a 3.1× reduction), clean UBR 25.7%→19.8%, UA 33.5%→47.6%. The evolved harness generalizes to held-out AgentHarm (Harm Score 19.8%→9.8%; Harm Refusal 78.4%→86.4%) and transfers across agent models without re-evolution. Repo `github.com/RainbowQTT/SHE` (Apache-2.0) cloned at `.local/adopts/SHE` (~5.1MB) — **GO Extract** as a reference for CCC + local-abliterated-lab harness work; do not auto-mutate prod harness without HITL.

[Source: arXiv:2608.09885]
