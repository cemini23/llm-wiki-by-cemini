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
  - sources/fintech-startup-legal-ip-roadmap.md
  - concepts/ip-sale-readiness.md
  - concepts/ip-sale-corporate-structure.md
  - concepts/irc-1235-capital-gains-safe-harbor.md
  - concepts/cryptographic-audit-trail.md
  - concepts/defend-trade-secrets-act.md
maturity: validated
created: 2026-04-23
updated: 2026-04-27
---

## Relations

- @sources/3-9-pm-research.md — primary K5 source (deep-read 2026-04-26); upgrades this page from `[RETRACTED — 2026-04-24 Track C]` to `[RESOLVED — 2026-04-26 K5 deep-read]`
- @sources/roadmap.md
- @sources/3-10-algorithmic-trading-ip-sale-audit.md
- @sources/3-19-compliance-research.md
- @concepts/ip-sale-readiness.md
- @concepts/ip-sale-corporate-structure.md — K6 2026-04-27 — the HoldCo formally owns the milestone-ledger commits; the dual-entity structure is what makes the IP chain-of-title (which the ledger documents) cleanly transferable in the APA
- @concepts/irc-1235-capital-gains-safe-harbor.md — K6 2026-04-27 — Git commit history (the ledger's substrate) is the load-bearing audit artifact for the §1235 personal-efforts test (proves individual-inventor authorship)
- @concepts/cryptographic-audit-trail.md — sibling J-pass page (Track C → RESOLVED) on the same prescribed-vs-deployed pattern
- @sources/fintech-startup-legal-ip-roadmap.md — K7 deep-read 2026-04-27 — third-source corroboration that **Git commit history is the load-bearing trade-secret evidentiary substrate** for the §1235 personal-efforts test (joins 3-10 audit's same finding); K7's IP Protection section explicitly calls Git authorship history the audit artifact under Defend Trade Secrets Act 18 U.S.C. § 1839 + Neural Magic v. Facebook economic-value-from-secrecy burden — the milestone-ledger-as-cryptographically-anchored artifact would be a **tamper-evident superset** of this Git-history substrate
- @concepts/defend-trade-secrets-act.md — K7-tail concept-promotion 2026-04-27 — the milestone ledger / Git commit history is the **load-bearing trade-secret evidentiary substrate** for satisfying DTSA's "reasonable measures to maintain secrecy" element + supporting the *Neural Magic v. Facebook* economic-value-from-secrecy burden; the prescribed Merkle-root-anchored ledger would be a tamper-evident superset that strengthens the secrecy-measure proof in any future DTSA enforcement action

## Raw Concept

`[RESOLVED — 2026-04-26 K5 deep-read]` — Track C found "the milestone ledger does not exist in any form" via direct postgres + filesystem probes (2026-04-24); K5 confirms and contextualizes that finding via the canonical source (`sources/3-9-pm-research.md` v11.0, 2026-03-08). The source itself uses **prescription voice** on the milestone ledger as an artifact (the "VeritasChain Protocol with vcp-core-py SCITT execution logs and Merkle-hashed proofs" framing in para 22 + 85), so the wiki's previous collapse into "the milestone ledger IS Cemini's append-only record" was the same prescription-as-as-built synthesis error documented in J (cryptographic-audit-trail), K (scatter-gather-topology), K3 (telethon), and K4 (hyperliquid). The page is reframed as the **prescribed milestone-ledger build spec + headline-claim verifiability problem**, not as documentation of a deployed artifact.

| Pre-K5 / Track-C state | Server reality / source reality |
|---|---|
| "milestone ledger ... append-only record of shipped features keyed to an explicit milestone-ID" with "git-commit range, Pydantic-v2 schema version, SBOM hash, Merkle-root snapshot" | No `milestone*` postgres table; 0 `milestone_ledger`/`ledger_entry` code refs; no `docs/MILESTONES*` files (Track C audit, 2026-04-24, re-confirmed 2026-04-26 K5). What exists is `docs/ROADMAP.md` — a markdown step-list. |
| "18 of 42 strategic roadmap milestones complete" (asserted as the headline self-assessment in `sources/3-9-pm-research.md` para 2) | Unverifiable against any artifact. Number can only be against the markdown ROADMAP at the time of writing (2026-03-08); no per-milestone evidence anchor (commit range, SBOM hash, Merkle root) exists to validate that any of the 18 actually shipped per their stated acceptance criteria. |
| Implicit framing: "the milestone ledger is the linear narrative an acquirer's diligence team reads" | The ROADMAP markdown can serve a similar function but at much lower trust grade — a markdown file is mutable, history-rewritable, and not cryptographically anchored. The acquirer-narrative function the source describes requires the prescribed VCP/zkCA/EQTY stack which is also unbuilt. |
| Cross-reference: VCP-anchored Merkle snapshots | VCP itself is `[RETRACTED 2026-04-24 Track C]` per @concepts/cryptographic-audit-trail.md. The dependency chain has no concrete artifact at any layer. |

See @sources/3-9-pm-research.md "Prescribed-vs-deployed gap (2026-04-26 K5 deep-read)" for the full evidence trail and the broader pattern: K5 found that the source is **stale-snapshot-style stale**, not pure-prescription-style stale. The "Recommended Tech Stack Upgrades" half of the document has actually largely shipped in the seven weeks since 2026-03-08 (Polars, Pydantic-AI, NautilusTrader, PettingZoo, Schemathesis, Hypothesis, mutmut). The milestone ledger is the one component that's both **claimed-as-deployed** *and* **provably-not-built**.

## Narrative

### Why the ledger matters

The milestone ledger is the **central IP-sale narrative artifact** in the source's framing. The acquirer-side mental model the source assumes:

1. Buyer's diligence team reads the linear ledger from initial commit to current code
2. Each entry has a tamper-evident anchor (Merkle root + SBOM hash + git commit range + Pydantic schema version + natural-language summary)
3. Ledger reads "we shipped X on date Y, Z is the schema version that locks the wire format, here's the SBOM proving no compromised dependency was introduced, here's the Merkle root anchoring the audit trail at this point"
4. Buyer can verify any milestone independently against the cryptographic anchors
5. Total ledger length + density = quantitative IP value signal

Without the ledger:

1. Buyer's diligence team falls back to git-log archeology
2. Time-on-deal lengthens (multiple buyer-side eng days per milestone re-derivation)
3. Buyer gains negotiating leverage on "complexity risk" and "verification overhead"
4. Headline self-assessments (the source's "18 of 42") become untrustworthy
5. The IP gets haircut on the "trust deficit"

### What exists vs. what was prescribed

**Currently exists** (server-verified 2026-04-26):

- `docs/ROADMAP.md` — markdown step-list. Auto-updated per `CLAUDE.md` convention. Mutable, history-rewritable, not cryptographically anchored.
- `LESSONS.md` — meta-lessons file. Captures *how* engineering decisions were made, not *which* milestones shipped.
- Git history on `/opt/cemini/` — the actual primary source of truth, but raw and undifferentiated.

**Prescribed but not shipped** (per `sources/3-9-pm-research.md` Phase 2 + Phase 4):

- `milestone_ledger` postgres table with append-only writer
- VCP SCITT Signed Statements (one per milestone)
- Merkle-tree anchoring of the ledger via OpenTimestamps
- SBOM (CycloneDX via Syft) per milestone — see @concepts/sbom.md for the SBOM piece
- EQTY Lab AI Certificates anchoring trained model weights to Hedera Consensus Service
- Zero-Knowledge Compliance Audit (zkCA) layer attesting to constraint compliance per milestone

### Action ticket (P0)

**Ship milestone-ledger table + append-only writer + ROADMAP → ledger backfill.** Single most load-bearing artifact for the acquirer narrative; without it, due diligence devolves into git-log archeology. Depends on SBOM ticket (see @concepts/sbom.md) for meaningful rows. Sequencing question: build the table-and-writer-and-backfill alone (P0) gets a workable ledger without cryptographic anchoring; deferring the VCP/zkCA layer to P1 lets due diligence start with at least a structured artifact even if the trust-deficit gap remains.

Gap memo: `briefs/track-c-walk-results.md` (Track C audit) + `briefs/2026-04-24_track-c-milestone-ledger-walk.md` (subsequent walk).

### Pattern: the headline-claim-verifiability problem

K5 surfaces a pattern worth naming: **headline claims in IP-sale narrative artifacts have an artifact-backing dependency that is itself often missing**. The "18 of 42 milestones complete" claim depends on a ledger that doesn't exist. Other parallel claims to spot-check in the corpus:

- **Sharpe ratios** depend on cryptographically-tamper-evident trade logs (VCP) — also unbuilt
- **Backtest fidelity** depends on the NautilusTrader↔PettingZoo bridge — partially scaffolded but not validated as research-to-live parity
- **"Zero safety violations"** depends on the SafeOR-Gym CMDP shield — unbuilt
- **"Model lineage"** depends on EQTY Lab AI Certificates anchored to Hedera — unbuilt

Each of these is its own headline claim with its own missing artifact backing. K5 has only resolved the milestone-ledger one; the others remain in their existing `[RETRACTED]` or `prescribed`-flagged states. Future K-style passes might benefit from a per-headline-claim audit grid that explicitly cross-references each claim to its backing artifact's deployment state.

## Snippets

> As of the current development phase (v11.0, documented March 8, 2026), the platform has successfully executed 18 of its 42 strategic roadmap milestones.
>
> *— @sources/3-9-pm-research.md para 2. The headline self-assessment that this concept page exists to address. Unverifiable against any artifact; only against the markdown ROADMAP at time of writing.*

> The platform will integrate the VeritasChain Protocol (VCP), an open standard specification for recording algorithmic trading decisions and execution results in an immutable, cryptographically verifiable format.
>
> *— @sources/3-9-pm-research.md para 22. The source uses **prescription voice** ("will integrate") on VCP — the milestone-ledger artifact's cryptographic anchoring layer. The wiki's prior framing of "milestone ledger IS Cemini's append-only record" inherited the absent artifact along with the prescription. Both VCP and the ledger remain unbuilt.*
