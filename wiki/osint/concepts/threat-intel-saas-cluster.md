---
title: "Threat-Intel SaaS Cluster — 9 Commercial CTI Platforms (Reject, Methodology-Extractable)"
type: concept
tags: [concept, threat-intelligence, cti, saas, reject-tier, cybersec-cross-route, methodology-reference, k42]
keywords: [shodan, fullhunt, onyphe, socradar, pulsedive, intelx, hunter, publicwww, coalitioninc, threat intel saas, commercial cti, ctem]
related:
  - sources/tool-evaluation-wiki-fit-2026-05-13.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
  - concepts/paradigm-vs-license-inverse-correlation.md
maturity: draft
created: 2026-05-13
updated: 2026-05-13
---

## Relations

- `@sources/tool-evaluation-wiki-fit-2026-05-13.md` — Doc 3 K42 origin batch (9 SaaS Rejects)
- `@concepts/tool-evaluation-framework.md` — methodology framework that triaged these as Reject
- `@concepts/cemini-license-posture.md` — closed-source SaaS fails IP-sale gate categorically
- `@concepts/paradigm-vs-license-inverse-correlation.md` — separate cluster (these are *commercial SaaS*, not "license-as-moat OSS")

## Raw Concept

K42 Doc 3 (`Tool Evaluation and Wiki Fit`) surfaced 9 commercial threat-intelligence SaaS platforms in one batch. All Reject-tier for codebase integration (closed-source + no OSS publication), but their CTI workflows, query DSLs, and exposure-management methodologies are real and battle-tested — value-extractable as **methodology references for the cybersec wiki**, never as Cemini-stack dependencies.

## Narrative

### The cluster

| Tool | Primary capability | Why Reject (Cemini posture) | Methodology value (cybersec-wiki) |
|---|---|---|---|
| **Shodan** | Internet-wide port/service scanning + banner grabbing | Closed-source SaaS, paid API, no on-prem | CTI dorking patterns, ICS/IoT exposure inventories |
| **FullHunt** | External attack-surface management (EASM) | Closed-source SaaS | Asset-discovery + CVE-correlation workflow reference |
| **ONYPHE** | Cyber-defense search engine (IPs / domains / certs / leaks) | Closed-source SaaS | Pivot-graph reasoning across heterogeneous CTI sources |
| **SOCRadar** | Extended threat intelligence (ETI) + dark-web monitoring | Closed-source SaaS | CTEM (Continuous Threat Exposure Management) framework |
| **Pulsedive** | Free-tier CTI lookup + threat-graph | Closed-source SaaS, API rate-limited | Indicator-correlation heuristics |
| **IntelX** | Leaked-credential + breach-data search | Closed-source SaaS, paid tiers | Breach-correlation tradecraft for OSINT investigations |
| **Hunter.io** | Email-discovery + verification | Closed-source SaaS | Email-pattern enumeration for HR / sales / OSINT enrichment |
| **PublicWWW** | Source-code search across crawled web | Closed-source SaaS | Tracking-script / API-key / fingerprint searches |
| **Coalitioninc** | Cyber-insurance + EASM hybrid | Closed-source SaaS, insurance-bundled | Insurance-loss-data → control-prioritization framework |

### Why grouped as a cluster

Three structural commonalities:

1. **Closed-source SaaS** — no on-prem, no OSS publication. Categorical Reject regardless of feature set.
2. **CTI / EASM / OSINT enrichment** — all serve external attack-surface or threat-intelligence workflows. Adjacent to cybersec-wiki red-team, blue-team, and OSINT methodology pages.
3. **API access available** — even though codebases are closed, all 9 expose paid APIs for query-time enrichment. Cemini *could* call them at runtime via API contract, but this introduces external SaaS dependency that contradicts IP-sale posture (clean-room integration would require API replacement at sale time).

### Cemini posture — categorical Reject, three reasons

1. **License gate**: closed-source fails the OSS-licensing prerequisite. No quarantine path. No 2029-conversion calendar (unlike BSL).
2. **IP-sale gate**: runtime API dependency creates a non-portable external coupling. Sale buyer inherits a vendor-lock that must be unwound.
3. **Cost gate**: paid tiers compound at scale. Cemini's research operations (single-operator OSINT) can lean on free-tier query budgets, but production systems can't.

### Methodology value — three extraction patterns

**Pattern 1 — Query DSL inheritance.** Shodan's filter syntax (`country:`, `port:`, `org:`, `vuln:`) and ONYPHE's IQL are templates for designing internal CTI query languages. If Cemini ever needs internal exposure-management tooling, the DSL ergonomics are documented prior art worth referencing.

**Pattern 2 — CTEM framework adoption (SOCRadar).** Continuous Threat Exposure Management is a Gartner-blessed methodology (Scoping → Discovery → Prioritization → Validation → Mobilization). The framework itself is methodology, not product; document in `@cybersecurity-wiki/concepts/ctem-framework.md` for blue-team reference.

**Pattern 3 — Pivot-graph reasoning (ONYPHE, IntelX).** These platforms encode investigator workflows where one indicator (IP / cert / email) expands across heterogeneous data sources. The pivot logic is methodology-portable; the underlying data is not.

### Where this fits in the K42 evaluation pipeline

Doc 3's executive synthesis explicitly frames these as a *cluster* rather than 9 independent evaluations, justifying batch-Reject without per-tool deep-read. This pattern — **batch-rejection of categorically-incompatible tool families** — is itself an efficiency lever for future link-evaluation cycles:

- Closed-source SaaS → batch Reject (cluster-level)
- BSL 1.1 → individual eval (2029 conversion calendar matters)
- AGPL-3.0 → individual eval (single-maintainer governance + relicensing potential matters)
- MIT / Apache-2.0 → individual eval (per-tool architectural fit matters)

Codify this triage hierarchy in `@concepts/tool-evaluation-framework.md` to speed up future evaluation throughput.

### Cross-routing decision

**Primary route**: `@cybersecurity-wiki/` — stubs for each of the 9 SaaS tools under `cybersec-wiki/entities/threat-intel-saas/` with methodology snapshots. Their CTI workflows belong in the cybersec corpus, not the OSINT-financial corpus.

**Secondary touchpoint**: OSINT-wiki retains this concept page as the *meta-decision* (why these 9 were batch-Rejected) but does not maintain individual tool pages — those live in cybersec-wiki.

### Open questions

- Hunter.io has obvious overlap with OSINT investigation tradecraft (email-pattern enumeration). Worth a dedicated page in `@cybersecurity-wiki/concepts/email-enum-tradecraft.md` rather than just a SaaS stub.
- Coalition's insurance-loss data could feed an `@concepts/insurance-loss-as-control-prioritization.md` page if Cemini ever extends into cyber-insurance modeling.
- Shodan + ONYPHE could be Phase-0-audited for *free-tier query budget viability* against Cemini's actual CTI needs. Currently Reject is categorical; if free-tier suffices, a methodology-only API-call wrapper might re-enter consideration as a closed dependency outside `/opt/cemini`.

[Sources: tool-evaluation-wiki-fit-2026-05-13.md]
