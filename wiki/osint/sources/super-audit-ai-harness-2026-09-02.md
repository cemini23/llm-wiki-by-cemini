---
title: Super-audit — Cemini federation AI harness (2026-09-02)
type: source
tags: [source, audit, harness, federation, cursor]
keywords: [super-audit, phase-a, file-keep-wire, invariants, rework]
related:
  - concepts/file-keep-wire-harness.md
  - meta/launchagent-health.md
  - concepts/cemini-wiki-ingest-workflow.md
maturity: validated
created: 2026-09-02
updated: 2026-09-02
read_status: read
---

## Relations

@concepts/file-keep-wire-harness.md · @meta/launchagent-health.md · @concepts/cemini-wiki-ingest-workflow.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Super-audit — Cemini federation AI harness |
| Author | 5-auditor council (3 Cursor + 2 OpenRouter) |
| Type | audit synthesis |
| Location | `reports/audit/premium-ai-harness-20260902/SYNTHESIS.md` |
| Retrieved | 2026-09-02 |
| Read status | read |

## Narrative

Five-auditor super-audit of laptop Cursor/Grok/route/MCP/skills/subscriptions across the Cemini federation. **Verdict: REWORK** (not REJECT). Main finding: ~47% duplicate rule tokens from global + per-project federation copies; 770-line alwaysApply catalog drowned hard gates; Phase-0/Phase-1/`policy_wired` vocabulary confused operators.

**Phase A shipped same day:** `cemini-invariants.mdc` (≤45 lines, alwaysApply); federation rules global-only; FILE · KEEP · WIRE concept; `wire-ledger.yaml`; OSINT alwaysApply flips; Grok 402 clarified.

**Phase B (ongoing):** `osint-invariants.mdc`; wiki-ingester unloaded; OpenRouter ranker prefers Qwen/GLM/Kimi; Cybersec overlay retirement; LaunchAgent health doc; GuruWatcher rule collapse (operator).

Full report: `reports/audit/premium-ai-harness-20260902/SYNTHESIS.md` · plan: `IMPLEMENTATION_PLAN.md`.

## Snippets

> Overall: **REWORK** (not REJECT). The stack is capable but over-built for daily use.

[Source: reports/audit/premium-ai-harness-20260902/SYNTHESIS.md]

## Dead Ends

- Installing Ollama on laptop — deferred (storage). Super-audit stays 5-model.
