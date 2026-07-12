---
title: Fable-advisor prod-touch gate (K159)
type: meta
tags: [k159, fable-advisor, xsp, prod-gate, cross-vendor]
keywords: [prod-touch, grok-implementer, codex-implementer, skill_audit, rollback]
related:
  - entities/tools/fable-advisor.md
  - concepts/xsp-lane-trading-framework.md
maturity: draft
created: 2026-07-12
updated: 2026-07-12
---

## Relations

- @entities/tools/fable-advisor.md
- @concepts/xsp-lane-trading-framework.md

## Narrative

Cross-vendor review checklist before merging any **prod-touching** diff to `cemini-prod`. Fail any item → do not merge.

- [ ] **Implementer lane** — change was written by `grok-implementer` or `codex-implementer` (not architect session bulk code)
- [ ] **Fable review pass** — architect/`fable-advisor` reviewed the diff for correctness, blast radius, and fit
- [ ] **skill_audit (if brief)** — when shipping via `briefs/`, `python3 scripts/skill_audit.py briefs/<file>.md` is PASS (or WARN with explicit accept)
- [ ] **No secrets** — no credentials, keys, tokens, or `.local`/server secrets in the diff or commit message
- [ ] **Scope boundary** — only intended paths under `/opt/cemini` (or agreed paths); no drive-by config/CLAUDE.md edits
- [ ] **Rollback plan** — revert commit/tag or known restore path documented before merge
- [ ] **Evidence** — verification commands/tests recorded; operator can re-run them post-deploy
