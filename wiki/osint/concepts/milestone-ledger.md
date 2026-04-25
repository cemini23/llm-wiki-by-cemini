---
title: Milestone ledger
type: concept
tags: [concept, cemini-internal, product-management]
keywords: []
related:
  - sources/3-9-pm-research.md
  - sources/roadmap.md
  - sources/3-10-algorithmic-trading-ip-sale-audit.md
  - sources/3-19-compliance-research.md
  - concepts/ip-sale-readiness.md
  - concepts/cryptographic-audit-trail.md
maturity: retracted
created: 2026-04-23
updated: 2026-04-24
---

## Relations

- @sources/3-9-pm-research.md
- @sources/roadmap.md
- @sources/3-10-algorithmic-trading-ip-sale-audit.md
- @sources/3-19-compliance-research.md
- @concepts/ip-sale-readiness.md
- @concepts/cryptographic-audit-trail.md

## Raw Concept

Synthesized across 4 source(s) in the Cemini research corpus that reference this concept directly or by equivalent terminology.

## Narrative

**[RETRACTED — 2026-04-24 Track C audit]** The milestone ledger **does not exist in any form**. Probes:
- `docker exec postgres psql -U admin -d qdb -c "\dt milestone*"` → `Did not find any relation named "milestone*"`.
- `grep -rln --include="*.py" --exclude-dir=".worktrees" "milestone_ledger\|ledger_entry" .` → 0 hits.
- `ls docs/MILESTONES* docs/milestones*` → no files.
- `docs/ROADMAP.md` exists (auto-updated per `CLAUDE.md`) — this is a **markdown step list**, not a cryptographically-anchored ledger with schema versions + SBOM hashes + Merkle roots.

**Meta-gap**: the milestone ledger is *itself* the first missing milestone. Ticket (**P0**): *Ship milestone-ledger table + append-only writer + ROADMAP → ledger backfill* — single most-load-bearing artifact for the acquirer narrative; without it, due diligence devolves into git-log archeology. Depends on SBOM ticket (see @concepts/sbom.md) for meaningful rows. Gap memo: `briefs/track-c-walk-results.md`.

Original claimed narrative retained below as retracted-claim-of-record.

---

The **milestone ledger** is Cemini's append-only record of shipped
features keyed to an explicit milestone-ID. Each entry carries the
git-commit range, the Pydantic-v2 schema version, the SBOM hash, the
Merkle-root snapshot, and a short natural-language summary.

### Why it exists
In the IP-sale negotiation playbook, the milestone ledger is the
**linear narrative** an acquirer's diligence team reads from initial
commit to the current code. Without it, due diligence degrades into
archeological commit-log spelunking — which increases time-on-deal
and gives the acquirer ammunition to haircut the price on
"complexity risk".

### What it connects
- **Cryptographic audit trail** — each milestone's Merkle snapshot
  is anchored via OpenTimestamps.
- **IP-sale-readiness** — the milestone ledger IS the readiness
  narrative in the APA (Asset Purchase Agreement) schedule.
- **Deal-killer ledger** — each potentially-problematic dependency
  or license is linked to the milestone at which it was introduced
  and (if resolved) retired.

## Snippets

*(populate as source stubs are deep-read.)*
