---
title: "NOMOS: compiling written policies into statically verified tool-call gates (arXiv 2610.11030)"
type: source
tags: [source, k288, arxiv, agents, safety, policy, tool-call-gating, security]
keywords: [nomos, tool-call-gate, policy-compiler, static-verification, agentdojo, tau2-bench, asr, deterministic-gate]
related:
  - concepts/k288-arxiv-wave.md
  - concepts/agent-safety-executable-evaluation.md
  - concepts/agent-authorization-stack.md
maturity: draft
created: 2026-10-10
updated: 2026-10-10
read_status: read
---

## Relations

- @concepts/k288-arxiv-wave.md
- @concepts/agent-safety-executable-evaluation.md
- @concepts/agent-authorization-stack.md

## Raw Concept

| Title | NOMOS: Compiling Written Policies into Statically Verified Tool-Call Gates for LLM Agents |
| Authors | Min-Young Yu, Tony Kim, Jang Won Choi (Corners Co., Ltd.) |
| Type | arXiv preprint (cs.CR) — IEEE submission |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.11030-nomos-compiling-written-policies-into-statically.pdf` |
| Retrieved | 2026-10-10 |
| arXiv | 2610.11030v1 |
| Code | **implementation proprietary, not released.** Artifact on Zenodo: doi:10.5281/zenodo.22123419 |
| read-status | read |

## Narrative

**The deterministic-gate answer to the guardrail problem.** A four-pass compiler turns a **natural-language agent policy** into a **runtime tool-call gate that uses no LLM**.

### The four passes

**PARSE → EXTRACT** (the **only** LLM pass; N=5 majority vote) **→ RESOLVE** (deterministic static checks: self-blocking reachability, argument–signature consistency, domain satisfiability, state contradictions, write-scope correctness) **→ MATERIALIZE**.

The runtime gate evaluates each proposed call against **facts taken only from real tool results and user turns** (structural fact provenance) and returns allow/block in **microseconds, with no LLM**. A **zero-LLM behavioural preflight** replays the rules over undefended transcripts.

### Results

- Policy violations among state-changing calls: **66.3% → 2.6%** (airline, 234/353 → 3/116) and **30.8% → 6.9%** (retail, 188/611 → 40/582) — **26×** and **4.5×**.
- **AgentDojo banking ASR: 0.0%** (288 pairs) vs **46.5% undefended** (a tool filter leaves 11.8%).
- RESOLVE **repairs 37% / rejects 13%** of candidate rules — the static pass catches bad generated policy.
- Airline pass^5 / pass^1: **0.51 → 0.67** (a policy that does not break the agent).
- Cost: a PolicyGuard reimplementation costs **+74% wall-clock and 347 LLM calls** vs **3 µs/call and zero calls**. Reproduces on **Llama-3.3-70B** (86.9% → 7.1%). The compiler runs **on-premise** on gemma-4-26B.

### Why it matters here

This is the **strongest published counter to "guardrails are prompt-level"** (Sam Newman, K285): compile the policy once, verify it statically, then enforce it **in code**, deterministically. It is also the same shape as the wiki's **typed-judgement / deterministic-gate** thread and as `agent-authorization-stack`.

**The 37% repair rate is the caution**: generated policy is wrong about a third of the time — an LLM-extracted rule set must be **statically verified**, not trusted. **Implementation not released**; the artifact DOI is on Zenodo.

## Snippets

> "Cuts policy violations among state-changing calls from 66.3%→2.6% (airline) and 30.8%→6.9% (retail) — 26× and 4.5×." [Source: arxiv-2610.11030-nomos-compiling-written-policies-into-statically.pdf]

> "RESOLVE repairs/rejects 37%/13% of candidates." [Source: arxiv-2610.11030-nomos-compiling-written-policies-into-statically.pdf]

> "AgentDojo banking ASR 0.0% (288 pairs) vs undefended 46.5%." [Source: arxiv-2610.11030-nomos-compiling-written-policies-into-statically.pdf]
