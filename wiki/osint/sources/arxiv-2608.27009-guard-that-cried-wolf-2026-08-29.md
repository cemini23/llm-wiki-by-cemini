---
title: "The Guard That Cried Wolf — name-superstition over-safety (arXiv 2608.27009)"
type: source
tags: [arxiv, agent-safety, over-refusal, guardrails, cyber, atto, k249]
keywords: [CautiousBench, name-superstition, over-safety, authorization-policy, AgentDoG, TS-Guard]
related:
  - concepts/k249-cyber-agent-safety-wave.md
  - concepts/intent-not-form-refusal.md
  - concepts/agent-runtime-identity-adr.md
maturity: draft
created: 2026-08-29
updated: 2026-08-29
read_status: read
---

## Relations

- @concepts/k249-cyber-agent-safety-wave.md — K249 cyber cluster
- @concepts/intent-not-form-refusal.md — refuse intent + authorization, not surface form
- @concepts/agent-runtime-identity-adr.md — tool-layer allow/refuse must read policy, not the object name

## Raw Concept

| Field | Value |
|-------|--------|
| Paper | arXiv:2608.27009, "The Guard That Cried Wolf: How Scary Words Make Agent Guardrails Refuse Legitimate Actions" |
| Authors | Yingjie Zhang, Yuanbo Xie, Kai Chen (IIE CAS / UCAS) |
| Retrieved | 2026-08-29 |
| File | `arxiv-2608.27009-the-guard-that-cried-wolf-how-scary-words-make-a.pdf` |
| sha256 | `d32c4907f890ea093995ec347ea1d487f74b50727e3d3096f2588e8fcb509660` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.27009-the-guard-that-cried-wolf-how-scary-words-make-a.pdf` |
| License | CC BY-NC-SA 4.0 (arXiv). Generator claimed "open license" in the PDF — **do not clone** until `gh api` SPDX is confirmed. NC/SA blocks proprietary Atto/Cemini copy. |
| Type | cs.CR preprint, 9pp |
| Dual-ID | **OSINT K249** = this inbox |

## Narrative

**Over-safety** for agent guardrails is a false positive: the action was authorized, but the guard refuses because the surface looks dangerous. Content-safety (is the *output* harmful?) is a different question.

**Cautious Bench** is a constructed (not harvested) over-safety benchmark. Each cell is a benign/twin pair under a stated authorization policy Π. Labels derive from Π at build time. 756 Decidable pairs × 3 name grades (as-authored / innocent / scary) = 2,268 measured pairs, plus 40 Undecidable pairs.

### Name-superstition (Table 1, FP / twin-detect %)

Execution-safety guards over-refuse more under a scary resource name than an innocent one, with authorization held fixed:

| Guard | innocent | as-authored | scary |
|-------|----------|-------------|-------|
| AgentDoG-Qwen | 63/83 | 70/91 | 82/93 |
| TS-Guard | 34/37 | 35/38 | 66/68 |
| ToolEmu | 32/82 | 36/89 | 45/85 |

PIGuard (injection classifier) and LlamaGuard (content-safety floor, ~1%) stay flat. Four of five designs also raise refusal on **authorized removal** under a scary name. `[TENTATIVE]` — single-paper; rates are point estimates.

`gh search` 2026-08-29 found **no public CautiousBench repository**. Paper license is **CC BY-NC-SA 4.0**. Phase-0: **NO-GO clone**. Wiki method only. **No PoC. No benchmark corpus in this repo.**

### Steal

- Key refuse/allow on **authorization** (role, scope, consent, precondition, provenance), not the resource name.
- Atto concierge: an authorized civil-record download must not fail because the register is named death / homicide. That is a product bug, not a safety win.
- CCC / cyber: scary CVE-looking filenames on owned lab paths are not an auto-refuse if the policy already authorizes the action.
- Report over-refusal **with** twin-detection. A lone FP number is not interpretable.

## Snippets

> "the execution-safety guards over-refuse an authorized action more often under a scary-looking object name than an innocent one. Since only the object name varies across the measured grades, the deviation is the name's doing." [Source: arxiv-2608.27009.pdf p.1]

> "We release the generator, the authorization policy Π, the gate, and the recipes under an open license" [Source: arxiv-2608.27009.pdf p.7] — **no GitHub URL in the PDF; NC-SA paper license; do not clone.**
