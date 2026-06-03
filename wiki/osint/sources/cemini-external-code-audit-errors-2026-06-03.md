---
title: CeminiSuite external code audit — execution & security errors (2026-06-03)
type: source
tags: [source, cemini-prod, security, ems, audit, k96]
keywords: [kalshi-bypass, position-gate, rbac-fail-open, deploy-ci, debate-prometheus, archive-logs]
related:
  - concepts/ems-execution-security-gaps.md
  - concepts/production-trading-blind-spots.md
  - concepts/cemini-knowledge-application-architecture.md
  - sources/arxiv-sandboxed-coding-agents-omni-mod-2606-00579-2026-06-03.md
read_status: deep-read
maturity: validated
created: 2026-06-03
updated: 2026-06-03
---

## Relations

- @concepts/ems-execution-security-gaps.md — synthesized failure catalog + fixes
- @concepts/production-trading-blind-spots.md — parent blind-spot taxonomy
- @briefs/2026-06-03_cemini-external-audit-remediation-cemini-prod.md — prod handoff (gitignored briefs/)

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Errors in code |
| Author | External reviewer (friend / third-party audit) |
| Type | docx |
| Location | `cemini-librarian:/opt/cemini-bulk/research/Errors in code .docx` |
| Retrieved | 2026-06-03 |
| sha256 | `50e4ea0c3473a2b3…` |
| read_status | deep-read |

Third-party static review of CeminiSuite repo run 2026-06-03. Findings verified against local clone `/Users/claudiobarone/Desktop/projects/CeminiSuite` — all seven issues reproduce as described. Reviewer note: `py_compile` + guardrail scripts passed; full pytest/ruff blocked locally (Python 3.11 tooling gap on reviewer machine).

## Narrative

Seven findings — **3 High**, **4 Medium** — clustered around **EMS gate bypass**, **fail-open security**, and **CI/archive hygiene**.

| # | Severity | Finding | Verified path |
|---|----------|---------|---------------|
| 1 | **High** | Kalshi Redis listener calls `kalshi_v2.place_order()` directly — skips `ems.execute()` gate stack (exposure, SAE, CVaR, PositionGate, TrustGate, LLM gating) | `ems/main.py` ~141–154 |
| 2 | **High** | PositionGate emits `outcome="error"` when adapter returns `None`; router only blocks `outcome=="block"` — live Kalshi/Coinbase adapters return `None` → shorts pass with `SHORT_ENABLED=false` | `core/ems/position_gate.py` ~84–92; `core/ems/router.py` ~396–409 |
| 3 | **High** | RBAC middleware fail-open on any token-validation exception → `{"allowed": True}` | `services/rbac/middleware.py` ~76–79 |
| 4 | Medium | Deploy CI runs only `pytest tests/` — package tests under `cemini_mcp/tests`, `logit_pricing/tests`, etc. not in gate | `.github/workflows/deploy.yml` ~361 |
| 5 | Medium | Debate state machine: Byzantine import guarded but `_pipeline_violations` / `_hitl_gate_triggers` use `_REGISTRY`/`_Counter` unconditionally → `NameError` without prometheus_client | `debate_protocol/state_machine.py` ~152–159, ~237–239 |
| 6 | Medium | `RBAC_BYPASS_LOCALHOST=true` documented in `.env.example` + ROADMAP but never read by middleware | `.env.example` ~242; `services/rbac/middleware.py` |
| 7 | Medium | `archive_logs.py` writes CSV then DELETEs Postgres rows — no txn, checksum, or restore verification | `scripts/archive_logs.py` ~26–40 |

## Snippets

> Kalshi execution bypasses EMS risk gates. The Redis EMS listener special-cases Kalshi and calls KalshiRESTv2.place_order() directly.

> With RBAC_ENABLED=true, any exception during token validation returns {"allowed": True}.

[Source: Errors in code .docx, retrieved 2026-06-03]
