---
title: fable-advisor (DannyMac180)
type: entity
tags: [tool, claude-code, orchestration, xsp, ceminidfs, k159, integrate]
keywords: [Fable, subagent routing, cross-vendor review, API cost, MIT]
related:
  - sources/eval-multi-wiki-repo-evaluation-strategy-2026-07-11.md
  - concepts/coding-agent-substrate-steerability.md
  - concepts/xsp-lane-trading-framework.md
  - entities/tools/muse-spark-api.md
  - meta/fable-advisor-prod-touch-gate.md
maturity: draft
created: 2026-07-11
updated: 2026-07-12
---

## Relations

- @sources/eval-multi-wiki-repo-evaluation-strategy-2026-07-11.md — K159 Integrate
- @concepts/xsp-lane-trading-framework.md — prod harness cost discipline
- @meta/fable-advisor-prod-touch-gate.md — K159 prod-touch checklist

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | [DannyMac180/fable-advisor](https://github.com/DannyMac180/fable-advisor) |
| **License** | MIT (~432★) [CONFIRMED Phase-0; eval said NOT FOUND] |
| **Verdict** | **Integrate** — architect/implementer split for Claude Code (Fable judges; Grok/GPT-5.6 implement) |
| **Routing** | xsp-killer prod brief (**scp**); CCC orchestration doctrine; CeminiDFS pipeline cost pattern |

Requires Claude Code ≥2.1.170. Five-part spec contract + cross-vendor review loop. **Friction:** Grok lane needs xAI CLI headless; subagent routing tied to Anthropic CLI changes. [NEEDS VERIFICATION 2026-07-11] empirical token savings on XSP generation run.

### Local adopt (2026-07-11)

| Check | Status |
|-------|--------|
| Plugin `fable-advisor@fable-advisor` v3.1.0 | **enabled** (user scope) |
| Claude Code | **2.1.207** — meets plugin floor ≥2.1.170 (upgraded 2026-07-12) |
| Grok CLI | **installed** (`grok` 0.2.93) — verify with `grok models`; headless needs `--allow "Bash(*)"` |
| Codex CLI | **installed** — `codex-implementer` lane available if GPT-5.6 auth OK |
| Install ritual | `bash scripts/adopt_k159_local.sh` |
| Report | `.local/reports/k159-fable-advisor-local-adopt.md` |

Use `/model fable` in Claude Code sessions on this workspace; architect doctrine in root `CLAUDE.md` § Agent orchestration.

### K159 token spike (2026-07-12)

| Check | Result |
|-------|--------|
| Claude Code | **2.1.207** — floor cleared |
| Grok implementer | **PASS** — 17s wall; `wiki/meta/fable-advisor-prod-touch-gate.md` (29 lines) |
| Fable-only baseline | **Pending** — operator CC session token readout for ≥30% adopt gate |
| Prod-touch gate | `@meta/fable-advisor-prod-touch-gate.md` |

Ritual: `bash scripts/run_k159_fable_token_spike.sh` · report `.local/reports/k159-fable-advisor-token-spike.md`

## Snippets

> "Implementation mechanics constitute approximately 90% of a coding session's token volume" [Source: eval docx URL 1 — paraphrase]
