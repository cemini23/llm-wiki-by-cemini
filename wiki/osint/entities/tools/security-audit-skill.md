---
title: security-audit-skill — Cloudflare audit skill (MIT)
type: entity
tags: [tool, k262, ccc, cyber, mit]
keywords: [security-audit-skill, Cloudflare, FILE]
related:
  - concepts/k262-eval-github-wave.md
  - concepts/k262-ccc-harness-wave.md
  - concepts/k262-cybersec-wave.md
  - sources/eval-repository-revenue-2026-09-16.md
maturity: draft
created: 2026-09-16
updated: 2026-09-16
phase_0_verdict: GO REFERENCE
harness_verb: FILE
wire_status: wont_wire
wire_note: REFERENCE clone. Do not copy into Cursor skills. Ask before skill install.
---

## Relations

- @concepts/k262-eval-github-wave.md
- @concepts/k262-ccc-harness-wave.md
- @concepts/k262-cybersec-wave.md
- @sources/eval-repository-revenue-2026-09-16.md

## Raw Concept

K262 Phase-0 on [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill).

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | https://github.com/cloudflare/security-audit-skill |
| **License** | MIT `[CONFIRMED]` gh api 2026-09-16 |
| **Local** | `.local/adopts/security-audit-skill` |
| **Stars** | 5670 (2026-09-16) |
| **Size** | ~0.14MB git |
| **Verdict** | **GO REFERENCE** FILE. Eval Integrate OVERRIDE to FILE. **0 Integrate GO.** |

Cyber/CCC FILE. Do not copy into Cursor skills. Ask before skill install. No skill auto-evolve.

## Phase-0 re-audit — 2026-10-25

Re-evaluated as URL 6 of @sources/eval-multi-wiki-link-revenue-v10.9-2026-10-25.md, tier **Integrate** (atto high, local-abliterated-lab high).

| Field | Value |
|-------|-------|
| **License** | MIT `[CONFIRMED]` by clone 2026-10-25 |
| **Last commit** | **2026-09-14** |
| **Size** | 588 KB / 22 files |
| **Verdict** | **GO** for install; retains the FILE boundary above |

Structural check: `skills/security-audit/` holds `SKILL.md` plus **11** domain documents — AI-AND-LLM, WEB-PROTOCOL-AND-AUTH, MEMORY-SAFETY-AND-BINARY, SUPPLY-CHAIN-AND-RELEASE, CLOUD-AND-DEPLOYMENT, DATA-ISOLATION-AND-LIFECYCLE, RESOURCE-EXHAUSTION-AND-AVAILABILITY, RECONNAISSANCE, VALIDATION-AND-REPORTING, CLIENT-SIDE, and one more.

**Two corrections to the report.** It names only five domain documents; there are eleven, so coverage is broader than stated. It also gives the last commit as 2026-10-17; the clone shows **2026-09-14**.

### Conflict with the K262 verdict — `[NEEDS VERIFICATION 2026-10-25]`

This page carries a K262 Phase-0 verdict of **GO REFERENCE / FILE / 0 Integrate GO** (2026-09-16). The v10.9 evaluation scores it **Integrate**.

Both cannot hold. The K262 decision read it as "reference only, do not copy into Cursor skills"; the new evaluation argues the 6-phase hunter/disprover split is directly usable against Atto. Nothing in the repo changed between the two — last commit 2026-09-14 predates both reads.

Unresolved. Treat as FILE until the operator rules. Do not install on the strength of the newer report alone.

### Why the 6-phase split matters

The failure it fixes is real: one agent invents a finding and then confirms it. Separating coverage-ledger hunters from fresh adversarial verifiers, and emitting `confirmed` / `needs_validation` / `rejected` to `findings.json` outside the target repo, breaks that loop.

### Guard

Dynamic validation needs an OS-enforced sandbox with networking off and writes restricted to scratch. Without one, the skill degrades to static tracing and marks dynamic leads `needs_validation` — correct behaviour, not a failure.
