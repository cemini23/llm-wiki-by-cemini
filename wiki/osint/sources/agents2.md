---
title: "Natural-Language Agent Harnesses"
type: source
tags: [pdf, llm-agents, k49]
clusters: [llm-agents]
related:
  - concepts/llm-agent-systems.md
maturity: validated
read_status: deep-read
created: 2026-04-23
updated: 2026-05-16
---

## Relations

- @concepts/llm-agent-systems.md — cluster hub for LLM agent-systems research in the Cemini corpus

## Raw Concept

- **Original title**: Natural-Language Agent Harnesses
- **Author(s)**: Linyue Pan, Shuo Guo, Jingchen Ni, Hai-Tao Zheng (Shenzhen International Graduate School, Tsinghua University); Lexiao Zou (Harbin Institute of Technology, Shenzhen)
- **Type**: PDF (arXiv preprint 2603.25723v1, 26 Mar 2026)
- **Location**: cemini-librarian:/opt/cemini-bulk/research/agents2.pdf
- **Retrieved**: 2026-04-23 (filename date reflects download date, not publication)
- **Length**: 18p
- **Read status**: deep-read
- **Primary cluster**: llm-agents
- **All clusters**: llm-agents

## Narrative

This paper argues that agent performance increasingly depends on **harness engineering** — the control stack governing multi-step reasoning, tool use, memory, delegation, and stopping — yet harness logic is normally scattered across controller code, framework defaults, and tool adapters, making it impossible to transfer, compare, or ablate cleanly. The proposal: externalize the harness design-pattern layer as an editable, executable artifact. The authors introduce **Natural-Language Agent Harnesses (NLAHs)** — harness control expressed in structured natural language with explicit contracts (required I/O, validation gates, retry/stop rules), roles (solver/verifier/researcher/orchestrator), stage structure, deterministic adapters/scripts, state semantics, and a failure taxonomy — and the **Intelligent Harness Runtime (IHR)**, an in-loop LLM that interprets an NLAH against current state plus a fixed "runtime charter," cleanly separating shared runtime policy from task-family logic. An optional file-backed state module externalizes durable state into path-addressable, compaction-stable artifacts.

Evaluation (Codex CLI 0.114.0, GPT-5.4, xhigh reasoning) covers SWE-bench Verified (125-sample subset) and OSWorld (36-sample subset). Three findings: (RQ1) the runtime charter and harness logic are behaviorally real — process metrics (tokens, tool calls, runtime) move sharply, ~90% of usage occurring in delegated child agents — while resolved rate stays in a narrow band; >110/125 SWE instances do not flip, so differences concentrate on a small component-sensitive frontier. (RQ2) modular ablation shows "more structure" is not uniformly better: self-evolution helps (+4.8 SWE) via a disciplined acceptance-gated loop, file-backed state and evidence-backed answering give mild process gains, while verifier (−0.8 SWE, −8.4 OSWorld) and multi-candidate search (−2.4 SWE) can hurt. (RQ3) a paired code-to-text migration of OS-Symphony reaches 47.2 vs 30.4 for the native code harness, with control re-centering from brittle screenshot-grounded GUI repair onto file-backed, artifact-verified closure.

**Cemini relevance**: NLAH/IHR is directly analogous to Cemini's conductor architecture and the CCC meta-wiki's treatment of harnesses, skills, and subagent orchestration as first-class objects — it provides a vocabulary (contracts, roles, charter vs. harness logic, file-backed state) and an empirical caution that adding harness modules only helps when they tighten the path to the evaluator's acceptance condition.

## Snippets

> "We ask whether the high-level control logic of an agent harness can instead be externalized as a portable executable artifact. We introduce Natural-Language Agent Harnesses (NLAHs), which express harness behavior in editable natural language." [Source: agents2.pdf p.1]

> "RQ2 does not support a simple 'more structure is always better' story. The stronger interpretation is that explicit modules help when they tighten the path from intermediate behavior to the evaluator's acceptance condition." [Source: agents2.pdf p.6]

> "Long-horizon autonomy fails in practice when critical state remains implicit or ephemeral ... the module enforces three properties: externalized, path-addressable, and compaction-stable." [Source: agents2.pdf p.4]
