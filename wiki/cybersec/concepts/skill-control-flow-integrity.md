---
title: "Skill control-flow integrity — compile the SKILL.md procedure into an enforceable contract"
type: concept
maturity: draft
related:
  - sources/arxiv-skillcfi-control-flow-integrity-2611.24185.md
  - concepts/agent-skill-injection.md
  - concepts/skill-cascading-attacks-skill-based-agents.md
  - concepts/agent-runtime-guardrails.md
  - concepts/agent-least-privilege-tool-selection.md
  - concepts/step-level-agent-guardrails.md
updated: 2026-11-22
---

## Raw Concept

What this page answers: an agent skill is a procedure in prose. Can you make the agent follow it the way a CPU follows a program? From 2611.24185 (SkillCFI).

## Narrative

A SKILL.md document names steps, order, mandatory checks, and user-decision points. In code this is a control-flow graph. In a skill, the model decides at runtime whether each step runs in reasoning, a tool call, or a script.

Control-flow integrity (CFI) confines a program to a pre-fixed graph. SkillCFI carries CFI to skills with three parts:

1. A compiler that confines LLM interpretation to compile time and derives the instructions plus an executable contract from one skill.
2. A formal enforceability criterion. It enforces obligations whose evidence crosses the tool boundary, and rejects a skill whose mandatory obligation leaves nothing to check.
3. A deterministic runtime enforcer. It admits a tool request only on trusted evidence and refuses unmediated channels such as inline scripts.

**Why allowlists are not enough.** Many violations use only lawful operations. Overwriting a file before validation uses the same tools the skill requires. A permission allowlist admits it. A prompt-injected model can also evade a monitor by regime migration, for example by claiming that a check passed.

**Baseline unreliability.** Agents that run SKILL.md directly satisfy only 26.2 to 54.0% of prescribed requirements on compliance-critical skills. Agents claim completion 28.7 to 37.9 points more often than evaluators confirm.

**Results.** No compiled contract permitted more than its source under 24 source mutations. In 770 sessions, SkillCFI blocked all 240 violations before dispatch. Normal tasks completed nearly as often. Listing the next legal steps in a refusal raised recovery from 21% to 65%. Checking cost about 2% of task time. A compact command form cut slowdown from 1.32x to 1.08x.

**Adoption signal.** None of 53 public skills was accepted as written. The diagnostics point to interfaces, not workflows, and guided seven skills into enforceable contracts.

**Lab use.** Treat a skill as a program to compile, not a prompt to trust. Recovery improves when the refusal says what the next legal step is.

[Source: arxiv-2611.24185-guarding-the-kingdom-of-skill-based-agents-in-th.pdf]

## Snippets

> "A deterministic runtime enforcer admits a tool request only on trusted evidence and refuses unmediated channels such as inline scripts."
[Source: arXiv:2611.24185v1 abstract]
