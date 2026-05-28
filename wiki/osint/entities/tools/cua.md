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
updated: 2026-05-28
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

### Phase-0 audit (2026-05-28)

Repo: `trycua/cua` — **MIT** (`LICENSE.md`), ~17k★, active, large test surface.

**Verdict: CONDITIONAL-GO (steal-from)** — viable QEMU/computer-use sandbox primitive for agent isolation pilots; compare against existing OCI sandbox posture before prod-adjacent use.

[Source: Evaluating URLs for Cemini Project.docx (retrieved 2026-05-13)]
