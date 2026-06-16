---
title: "Claw-SWE-Bench — OpenClaw-style harness evaluation on coding tasks (arXiv 2606.12344)"
type: source
tags: [source, arxiv, llm-agents, benchmark, openclaw, harness, k119]
keywords: [2606.12344, claw-swe-bench, swe-bench, harness-attribution, pass-at-1, api-cost]
related:
  - concepts/claw-swe-bench-harness-evaluation.md
  - entities/tools/claw-swe-bench.md
  - concepts/code-as-agent-harness.md
  - concepts/openclaw-security-taxonomy.md
  - concepts/mcp-tool-calling-eval-scaffold.md
  - concepts/llm-agent-systems.md
maturity: draft
read_status: read
created: 2026-06-16
updated: 2026-06-16
clusters: [llm-agents, agent-harness]
---

## Relations

- @concepts/claw-swe-bench-harness-evaluation.md — K119 synthesis
- @entities/tools/claw-swe-bench.md — MIT benchmark repo
- @concepts/code-as-agent-harness.md — harness-as-variable cluster
- @concepts/openclaw-security-taxonomy.md — OpenClaw threat model context
- @concepts/mcp-tool-calling-eval-scaffold.md — eval discipline sibling

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Claw-SWE-Bench: A Benchmark for Evaluating OpenClaw-style Agent Harnesses on Coding Tasks |
| **Authors** | Zheng et al. (TokenRhythm, Infinigence, PKU, THU, …) |
| **arXiv** | 2606.12344 |
| **sha256** | `c50bf4e5fd1a588236fcc1e62764e8518d8e87ecf040018f94b4f3c389b926a1` |
| **Repo** | https://github.com/opensquilla/claw-swe-bench (MIT, ~25★ 2026-06-16) |
| **Dataset** | https://huggingface.co/datasets/TokenRhythm/Claw-SWE-Bench |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2606.12344-tier2-sweep.pdf` |
| **Retrieved** | 2026-06-16 (Tier-2 sweep Q1) |
| **Read status** | read (abstract + §1–2 + headline sweeps) |

## Narrative

**Problem:** SWE-bench scores conflate **model**, **harness**, and **task set**. General-purpose claws (OpenClaw, NanoBot, ZeroClaw, …) cannot enter SWE-bench without adapter glue (Docker workspace, patch contract, prediction file).

**Claw-SWE-Bench** fixes base protocol (prompt, timeout, patch extraction, evaluator) and swaps **harness slot** via shared adapter lifecycle API. **350** instances (8 languages, 43 repos); **Lite-80** cost-aware subset (~23% full-run cost, ~0.4pp Pass@1 parity).

**Headline results (paper claims):**

| Axis | Spread |
|------|--------|
| OpenClaw minimal vs full adapter (GLM 5.1) | 19.1% → 73.4% Pass@1 |
| Model choice (fixed harness) | up to **29.4pp** |
| Harness choice (fixed model) | up to **27.4pp** |
| Cost vs accuracy | Pareto frontier — same Pass@1, very different API $ |

**Cemini posture:** **REFERENCE** + **CONDITIONAL-GO** laptop smoke on Lite-80 only. Steal **harness attribution discipline** for conductor/Cursor eval — never report agent coding scores without naming harness + budget + cost. Phase-0: `adopt_k119_phase0.sh`.

## Snippets

> "The resulting resolved rate therefore conflates three causally distinct factors: the evaluated LLM, the harness that turns the LLM into an agent, and the task instances being solved." [Source: arxiv-2606.12344-tier2-sweep.pdf §1]

> "Harness choice is a first-order factor… 27.4pp on Qwen 3.6-flash." [Source: arxiv-2606.12344-tier2-sweep.pdf §1]
