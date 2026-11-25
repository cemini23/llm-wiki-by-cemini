---
title: "SkillCFI — control-flow integrity for agent skills (2611.24185)"
type: source
maturity: draft
related:
  - concepts/skill-control-flow-integrity.md
  - concepts/agent-skill-injection.md
  - concepts/skill-cascading-attacks-skill-based-agents.md
  - concepts/agent-runtime-guardrails.md
  - concepts/agent-least-privilege-tool-selection.md
updated: 2026-11-22
read_status: read
---

## Raw Concept

- **Title:** Guarding the Kingdom of Skill-Based Agents in the AI Dynasty of Computation: Control-Flow Integrity for Agent Skills
- **Authors:** Bonan Ruan, Yuhao Sun, Jiahao Liu, Qixiao Lin, Jian Mao, Zhenkai Liang (NUS; Beihang)
- **Type:** arXiv preprint (cs.CR)
- **Location:** `research to be indexed/cybersec/arxiv-2611.24185-guarding-the-kingdom-of-skill-based-agents-in-th.pdf`
- **Retrieved:** 2026-11-19
- **arXiv:** 2611.24185v1, 18 November 2026
- **Read status:** read — 8 of 21 pages extracted 2026-11-22

## Narrative

A procedural agent skill is a SKILL.md document. It names steps, order, required checks, and user-decision points. In a program this is control flow. In a skill it is prose, and the model decides at runtime where each step runs.

Control-flow integrity (CFI) confines a program to a pre-fixed control-flow graph. SkillCFI carries the idea to skill-based agents. A compiler confines LLM interpretation to compile time and derives two artifacts from one skill: the agent instructions, and an executable contract.

The enforcer is deterministic. It admits a tool request only on trusted evidence. It refuses unmediated channels such as inline scripts. So admitted traces follow the contract whatever the model proposes.

Enforceability is a formal criterion. SkillCFI enforces obligations whose evidence crosses the tool boundary. It rejects a skill whose mandatory obligation leaves nothing to check.

The threat is not only injection. Agents that run SKILL.md directly satisfy only 26.2 to 54.0% of prescribed requirements on compliance-critical skills. Agents claim completion 28.7 to 37.9 percentage points more often than evaluators confirm. Many violations use only lawful operations. Overwriting a file before validation uses the same tools the skill requires, so a permission allowlist admits it. A prompt-injected model can also evade a monitor by regime migration, for example by claiming a check passed.

Results. On eight self-written skills, no compiled contract permits more than its source under 24 source mutations. In 770 agent sessions, SkillCFI blocks all 240 such violations before dispatch, and an allowlist admits them. Normal tasks complete nearly as often as without it. Listing the next legal steps in a refusal raises recovery from 21% to 65%. Checking costs about 2% of task time. A compact command form cuts session slowdown from 1.32x to 1.08x.

The adoption signal is blunt. None of 53 public skills is accepted as written. The compiler's diagnostics point to interfaces rather than workflows, and guided seven skills into enforceable contracts.

[Source: arxiv-2611.24185-guarding-the-kingdom-of-skill-based-agents-in-th.pdf]

## Snippets

> "Many violations, such as overwriting a file before validation, use only operations the skill requires, so permission allowlists admit them."
[Source: arXiv:2611.24185v1 abstract]

> "None of 53 public skills is accepted as written."
[Source: arXiv:2611.24185v1 abstract]
