---
title: "Persona-hat Claude Code SDLC — five roles, MCP vs skills, parallel subagents"
type: concept
tags: [concept, claude-code, sdlc, gcp, k238]
keywords: [persona hat, plan mode, Cloud Run, Firestore, security review, subagents, Vertex ADC]
related:
  - sources/x-clayul-ivan-nardini-claude-gcp-2026-08-13.md
  - concepts/role-specialization-model-rsm.md
  - concepts/claude-code-skills-md-workflow.md
  - concepts/code-as-agent-harness.md
  - entities/tools/google-skills.md
  - entities/people/ivan-nardini.md
maturity: draft
created: 2026-08-15
updated: 2026-08-15
---

## Relations

- @sources/x-clayul-ivan-nardini-claude-gcp-2026-08-13.md — Code w/ Claude 2026 live build (X clip + official YT)
- @concepts/role-specialization-model-rsm.md — paper RSM vs this demo (hats without hard scope lock)
- @concepts/claude-code-skills-md-workflow.md — skills as per-block deploy recipes
- @concepts/code-as-agent-harness.md
- @entities/tools/google-skills.md — packing-repo Context; different artifact from GCP Claude Code skills
- @entities/people/ivan-nardini.md

## Raw Concept

What this page answers: how does a single operator use Claude Code as a **role-switching SDLC** (five hats) without pretending 26 minutes is production? Synthesized from Ivan Nardini's Code w/ Claude 2026 GCP live build (X clip 2026-08-13; session 2026-05-06).

## Narrative

Nardini's demo is a **persona-hat loop**, not a five-agent org chart. One human switches hats; Claude Code + GCP MCP/skills fill the role's tools.

| Hat | Prompt posture | Harness piece |
|-----|----------------|---------------|
| **PM** | Idea → wireframe from a sketch | Direct generate (no plan mode in the sketch step) |
| **UI/UX** | Landing + thanks + live dashboard | **Plan mode** (propose before code); optional Figma MCP / design doc |
| **SWE** | Cloud-native backend without prior GCP knowledge | Knowledge-API **MCP** (architecture) + **skills** (Cloud Run, Firestore wiring) + **3 subagents** (API / ingest / dashboard) |
| **Security** | OWASP + service-account least privilege | Pre-built security-review skill; auto-fix then deploy — **demo conflates reviewer and deployer** |
| **Data / growth** | Live session scores → insight | Firestore → BigQuery; Looker / BigQuery MCP |

**Steal (CCC / Cursor):**

1. **MCP designs; skills implement.** Docs MCP answers "what architecture"; a Cloud Run skill answers "how this block ships." Do not dump both into one SKILL.md.
2. **Plan mode before UI code** — change the plan, not a pile of generated CSS.
3. **Fan-out by component**, not by vibe: API vs ingest vs dashboard as separate subagents / worktrees.
4. **Security review is a required check**, not a hat you skip. Keep reviewer ≠ deployer (K239 / HITL) even though the demo merged them.
5. **Vertex ADC** is an enterprise auth story (in-project data, no key in env) — pairs K254 hardware-keystore; not a `/route` swap.

**Caveats:** Auto-captions garble "Claude Code" as "Cloud Code" / "CoCode." The X caption overclaims "weeks → 26 minutes"; a reply notes a basic GCP app is often a day, and another flags missing CI/CD, monitoring, maintenance. Pair with RSM: hats without **scope boundaries** will let the "security engineer" also ship.

## Snippets

> "if with the MCP server you will be able to design the architecture, with the skills you will be able to cover the single blocks" [Source: YouTube SqHsS737CeA auto-captions]

> "this is just a demo so we have this degree of freedom" (security hat also deploys) [Source: YouTube SqHsS737CeA auto-captions]
