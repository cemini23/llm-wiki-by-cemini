---
title: FILE · KEEP · WIRE — three-verb harness ingest vocabulary
type: concept
tags: [concept, workflow, harness, federation, ingest, audit]
keywords: [file-keep-wire, phase-0, phase-1, policy_wired, wire-ledger, super-audit]
related:
  - concepts/cemini-wiki-ingest-workflow.md
  - concepts/multi-wiki-eval-doc-level-vs-phase-0.md
  - concepts/harness-updating-vs-benefit-nonmonotonic.md
  - meta/launchagent-health.md
  - sources/super-audit-ai-harness-2026-09-02.md
maturity: draft
created: 2026-09-02
updated: 2026-09-02
---

## Relations

- @concepts/cemini-wiki-ingest-workflow.md — daily ingest ritual
- @concepts/multi-wiki-eval-doc-level-vs-phase-0.md — eval vs adopt boundary
- @concepts/harness-updating-vs-benefit-nonmonotonic.md — harness edit risk
- @ccc-wiki/concepts/phase1-adopt-wire.md — CCC adopt vocabulary (legacy name)

## Raw Concept

Prompted by super-audit `reports/audit/premium-ai-harness-20260902/SYNTHESIS.md` (5 auditors, verdict REWORK, 2026-09-02). Operators asked to replace Phase-0 / Phase-1 / `policy_wired` prose with a simple mental model.

## Narrative

Three verbs replace the old harness vocabulary:

| Verb | Meaning | Replaces |
|------|---------|----------|
| **FILE** | A wiki page exists with claim + locator. The page *is* the policy. | `policy_wired`, `wont_wire`, `watch`, "Phase-1 leftover" |
| **KEEP** | A clone under `.local/adopts/` with SPDX verified and size recorded. | Phase-0 audit, `extract_only`, `reference` |
| **WIRE** | An executable changed (script, skill, hook, rule, MCP) with a row in `wiki/meta/wire-ledger.yaml`. | Phase-1, `runtime_wired`, `integrate` |

**Daily flow:** digest → triage → FILE pages → KEEP if clone worth it → WIRE only if something executable changed → one line in `wiki/log.md`. A session ends FILEd or wired. "Phase-1 leftover" is forbidden.

**ID rule:** Rules and ledger rows use arXiv id or slug. K# is a batch label in `log.md` and ROADMAP only.

**Rule budget:** `alwaysApply` = invariants only (`cemini-invariants.mdc` ≤45 lines + per-wiki hard gates). Catalogs are on-demand (`alwaysApply: false` + good description). Canon is the wiki page.

**Migration (2026-09-02):** `wire_status` retired → `harness_verb: FILE|KEEP|WIRE`. Run `python3 scripts/migrate_wire_status.py --dry-run` to audit stragglers. `runtime_wired` / `integrate` → WIRE (ledger row required). See `python3 scripts/wire_ledger_check.py`.

## Snippets

```yaml
# wiki/meta/wire-ledger.yaml (example row)
- id: cemini-invariants-rule
  verb: WIRE
  kind: rule
  repo: ccc
  path: .cursor/rules/cemini-invariants.mdc
  wiki_page: "@ccc-wiki/concepts/phase1-adopt-wire.md"
  since: 2026-09-02
```

## Dead Ends

27 duplicate K# ids across federation rules (K237 ×7 meanings) forced dual-ID footnotes — a symptom of keying by batch label instead of slug/arXiv id. Collapsing to FILE/KEEP/WIRE removes the need for most dual-ID prose.
