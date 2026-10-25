---
title: EMS execution security gaps — external audit catalog (K96)
type: concept
tags: [concept, cemini-prod, ems, security, rbac, k96]
keywords: [kalshi-bypass, position-gate, rbac-fail-open, gate-bypass, fail-closed]
related:
  - sources/arxiv-cage1-enterprise-governance-2607.03510-2026-07-10.md
  - sources/cemini-external-code-audit-errors-2026-06-03.md
  - concepts/production-trading-blind-spots.md
  - concepts/cemini-knowledge-application-architecture.md
  - concepts/shadow-to-live-transition-engineering.md
  - concepts/seclaw-agent-security-evaluation.md
  - sources/arxiv-seclaw-spec-driven-agent-security-2606-02302-2026-06-04.md
  - concepts/interaction-native-knowledge-harness.md
  - sources/arxiv-interaction-native-knowledge-harness-2606.01886.md
  - concepts/context-fractured-decomposition-attacks.md
  - concepts/reviewer-passive-injection-corpus.md
  - sources/arxiv-context-fractured-decomposition-cfd-2606.09084-2026-06-12.md
maturity: validated
created: 2026-06-03
updated: 2026-07-10
---

## Relations

- @sources/cemini-external-code-audit-errors-2026-06-03.md — provenance (friend audit 2026-06-03)
- @concepts/production-trading-blind-spots.md — operational failure taxonomy
- @cybersecurity-wiki/concepts/agent-runtime-guardrails.md — RBAC / runtime guard patterns
- @concepts/interaction-native-knowledge-harness.md — maturity × action-risk gates before prod memory writes
- @concepts/reviewer-passive-injection-corpus.md — K37 reviewer passive-injection corpus hub
- @sources/arxiv-interaction-native-knowledge-harness-2606.01886.md — InKH governance model (K99)

## Raw Concept

Synthesized from third-party CeminiSuite code review dropped 2026-06-03. All findings `[CONFIRMED]` against local repo clone same day.

## Narrative

Three **P0** patterns — treat as blockers before expanding live Kalshi or enabling RBAC in production:

### 1. Side-door execution (Kalshi)

`ems/main.py` Redis listener bypasses `core/ems/router.py` for Kalshi signals. Only stale-ticker skip remains; exposure/SAE/CVaR/PositionGate/TrustGate never run.

**Fix:** Route Kalshi through `router.execute()` (or shared `_run_gate_stack()` helper). Delete direct `kalshi_v2.place_order()` except inside adapter after gates pass.

### 2. PositionGate error ≠ block

When `adapter.get_position()` returns `None`, gate returns `outcome="error"`. Router treats only `"block"` as hard stop → **uncovered shorts** on live adapters.

**Fix (choose one):** (a) treat `error` + `short_origination_attempt` as `block` when `SHORT_ENABLED=false`; (b) implement `get_position()` on Kalshi/Coinbase adapters; (c) fail-closed default for live brokers.

### 3. RBAC fail-open

`services/rbac/middleware.py` except block returns `allowed: True`. Postgres outage = open MCP.

**Fix:** Invert default — `except` → `allowed: False` + alert metric. Wire `RBAC_BYPASS_LOCALHOST` or remove from docs.

### Medium (P1–P2)

| Issue | Fix sketch |
|-------|------------|
| CI scope | Add matrix job: `pytest tests/ cemini_mcp/tests logit_pricing/tests …` or `pytest --collect-only` guard |
| Debate prometheus | Guard `_pipeline_violations` / `_hitl_gate_triggers` same as `_byzantine_checks` try/except |
| Archive janitor | Wrap CSV write + DELETE in txn; verify file size/checksum before DELETE; dry-run flag |

Prod brief: `briefs/2026-06-03_cemini-external-audit-remediation-cemini-prod.md` → `/opt/cemini/briefs/`.
