---
title: cua (trycua) — QEMU sandbox API for LLM payloads (Adopt-tier)
type: entity
tags: [tool, sandbox, qemu, isolation, llm-execution, adopt-tier, cybersec-cross-route, workflow, agent-safety]
keywords: [cua, trycua, qemu, sandbox, isolated execution, llm payloads, malware analysis]
related:
  - sources/evaluating-urls-cemini-project-2026-05-13.md
  - concepts/tool-evaluation-framework.md
  - concepts/reviewer-agent-inference-time-feedback.md
maturity: draft
created: 2026-05-13
updated: 2026-05-13
---

## Relations

- `@sources/evaluating-urls-cemini-project-2026-05-13.md` — origin source (Doc 1, K42), Adopt-tier
- `@concepts/tool-evaluation-framework.md` — methodology
- `@concepts/reviewer-agent-inference-time-feedback.md` — agent-safety stack; cua is a possible isolation primitive for autonomous Conductor execution

## Raw Concept

Stub from Doc 1 K42 eval (2026-05-13). Adopt-tier; cross-routed to Cybersec-wiki (LLM-generated malware execution + analysis) + Workflow (laptop-side agent sandboxing).

## Narrative

- **Eval claim**: QEMU sandbox API for executing and analyzing LLM-generated payloads in isolation.
- **Cemini relevance**: alternative or complement to Frona-style OCI sandboxing for autonomous agent execution. K41 weather-bot Phase-0 brief identified the need for execution-isolation primitives — cua is a candidate.

### Phase-0 audit (PENDING)

Compare against Frona (BSL 1.1 rejected) for OCI-vs-QEMU sandboxing tradeoffs. Verify cua license (eval did not explicitly state).

[NEEDS VERIFICATION 2026-05-13]

[Source: Evaluating URLs for Cemini Project.docx (retrieved 2026-05-13)]
