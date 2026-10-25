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
  - sources/eval-multi-wiki-link-revenue-v10.9-2026-10-25.md
maturity: draft
created: 2026-09-16
updated: 2026-10-25
phase_0_verdict: GO — Integrate (operator ruling 2026-10-25)
harness_verb: INTEGRATE
wire_status: installed
wire_note: Supersedes the K262 FILE verdict. Verdict Integrate; first run DEFERRED — Atlas (Atto's newest repo) is under active development. Static-first when it does run; dynamic validation needs an OS-enforced sandbox with networking off.
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

### Conflict with the K262 verdict — RESOLVED 2026-10-25

This page carried a K262 Phase-0 verdict of **GO REFERENCE / FILE / 0 Integrate GO** (2026-09-16). The v10.9 evaluation scores it **Integrate**.

**Operator ruled Integrate on 2026-10-25.** The K262 FILE reading was about not copying the skill into Cursor's skill directory unattended. The Integrate reading is about running the workflow as a tool against Atto. Both hold together: installed, run only on request, never written into the target repo's tree.

Frontmatter and verdict reflect the ruling. The K262 row above is kept as history.

### Installed and first run — 2026-10-25

Installed globally with `npx skills add https://github.com/cloudflare/security-audit-skill --skill security-audit -g -y`. Registration confirmed: the skill is available as `security-audit` in the session.

**First run: `comuni-atlas`, guidance mode.** The deferral above said to wait for a stable Atlas checkpoint and to audit a named commit, not a dirty worktree. Atlas is now committed and live, so the condition is met, and it was audited **before** Atto because it is MIT, small (`cli/`, `lib/`, `web/`, `scripts/`), public-facing, and holds no family PII.

Findings: no confirmed vulnerability. Details under `## Audit — comuni-atlas` below.

**Still owed:** a full six-phase run against Atto. That is the higher-stakes target — it holds the family tree, the Stato Civile requests, and the citizenship packet.

### First run deferred — 2026-10-25 (superseded)

**Do not audit Atto or Atlas yet.** Atlas is the newest repository and work is in flight there. A six-phase audit of a tree being actively rewritten produces findings against code that will not exist by the time anyone reads them.

Resume when Atlas reaches a stable checkpoint. At that point run against a named commit, not a dirty worktree — the skill's own setup rule requires a recorded source ref and a note on whether the worktree is dirty.

The install was interrupted before completing. Nothing is registered in `~/.claude/skills/` or `~/.agents/skills/`. Install is still owed.

### Why the 6-phase split matters

The failure it fixes is real: one agent invents a finding and then confirms it. Separating coverage-ledger hunters from fresh adversarial verifiers, and emitting `confirmed` / `needs_validation` / `rejected` to `findings.json` outside the target repo, breaks that loop.

### Guard

Dynamic validation needs an OS-enforced sandbox with networking off and writes restricted to scratch. Without one, the skill degrades to static tracing and marks dynamic leads `needs_validation` — correct behaviour, not a failure.
