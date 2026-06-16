---
title: "HarnessFix — trace-guided harness diagnosis and repair (arXiv 2606.06324)"
type: source
tags: [source, arxiv, llm-agents, harness, reliability, k119]
keywords: [2606.06324, harnessfix, htir, etclovg, trace-repair, regression-aware]
related:
  - "@ccc-wiki/concepts/failed-trajectory-harness-repair.md"
  - "@ccc-wiki/sources/arxiv-failed-trajectory-harness-repair-2606.06324-2026-06-05.md"
  - concepts/code-as-agent-harness.md
  - concepts/agent-memory-cross-scenario-generality.md
  - concepts/mcp-tool-calling-eval-scaffold.md
  - concepts/llm-agent-systems.md
maturity: draft
read_status: read
created: 2026-06-16
updated: 2026-06-16
clusters: [llm-agents, agent-harness]
cross-wiki-source: "@ccc-wiki/sources/arxiv-failed-trajectory-harness-repair-2606.06324-2026-06-05.md"
---

## Relations

- @ccc-wiki/concepts/failed-trajectory-harness-repair.md — CCC validated deep-read (2026-06-05)
- @ccc-wiki/sources/arxiv-failed-trajectory-harness-repair-2606.06324-2026-06-05.md — CCC canonical source page
- @concepts/code-as-agent-harness.md — harness engineering cluster
- @concepts/agent-memory-cross-scenario-generality.md — outcome-only vs diagnosis-driven contrast
- @concepts/mcp-tool-calling-eval-scaffold.md — trajectory eval discipline

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | From Failed Trajectories to Reliable LLM Agents: Diagnosing and Repairing Harness Flaws |
| **Authors** | Chen, Wang et al. (CAS / ISCAS) |
| **arXiv** | 2606.06324 |
| **sha256** | `00a4236ba8ab24925e3b0409b4c003bd22c57d76faabc888f20734fba5e4cafd` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2606.06324-tier2-sweep.pdf` |
| **Retrieved** | 2026-06-16 (Tier-2 sweep Q1) |
| **Read status** | read (abstract + §I–III overview) |

## Narrative

**HarnessFix** — four-agent loop: trace abstraction → diagnosis → scoped repair → regression-bounded validation.

| Artifact | Role |
|----------|------|
| **HTIR** | Harness-aware Trace IR — TraceSteps + temporal / input-provenance / control-flow links |
| **ETCLOVG layers** | Execution, Tooling, Context, Lifecycle, Observability, Verification, Governance |
| **Flaw records** | Merged recurring diagnoses before patching |
| **Repair operators** | Layer-scoped edits (not free-form self-edit) |

**Reported gains:** +15.2%–50.0% held-out on SWE-Bench Verified, Terminal-Bench 2.0, GAIA, AppWorld vs initial harnesses [TENTATIVE].

**Cemini posture:** **REFERENCE** — no public code repo at ingest. Steal **diagnosis-before-patch** + **regression acceptance** for MCP/conductor harness iteration. CCC owns operator vocabulary (`@ccc-wiki/concepts/etclovg-harness-layers.md`). OSINT prod brief stages trace-grounded repair discipline.

## Snippets

> "HARNESSFIX compiles raw execution traces and harness code into a Harness-aware Trace Intermediate Representation (HTIR)." [Source: arxiv-2606.06324-tier2-sweep.pdf abstract]

> "Existing self-improving agents… often fail to diagnose where the responsible evidence lies in failed trajectories and which harness layer causes the unreliable behavior." [Source: arxiv-2606.06324-tier2-sweep.pdf §I]
