---
title: Cemini License Posture — Dependency Obligations & IP Status
type: concept
tags: [license-compliance, audit-security, cemini-internal, ip-sale-readiness]
keywords: [AGPL-3.0, GPL-3.0, MIT, Apache-2.0, derivative-work, network-copyleft, default-copyright]
related:
  - concepts/ip-sale-readiness.md
  - sources/more-links-5-2-arch-eval.md
  - sources/4-3-link-re-2.md
  - sources/4-4-link-re-2.md
  - concepts/cemini-deployment.md
  - entities/infrastructure/cemini-stack.md
maturity: draft
created: 2026-05-03
updated: 2026-05-03
---

## Relations

- @concepts/ip-sale-readiness.md — license posture is a prerequisite for any IP-sale or partial-license transaction
- @sources/more-links-5-2-arch-eval.md — K27 surfaced AGPL-3.0 Docker-defeat pattern + GPL-3.0 LLM-agent derivative-work risk + missing-license default-copyright pattern (three license-compliance failure modes)
- @sources/4-3-link-re-2.md — Moirai (CC-BY-NC-4.0) + Firecrawl (AGPL-3.0) rejections recorded in K14 deep-read
- @sources/4-4-link-re-2.md — AGPL-3.0 contamination warnings (OpenViking, SAMEP) recorded in K12 deep-read

## Raw Concept

This page audits the license obligations attached to the Cemini stack — what Cemini's own code carries, what its dependencies require, and where the exposure points are.

Originated from the user's 2026-05-03 question on whether the wiki needs a license page. Confirmed scope: Cemini is **private** (not intended for open-source release at this time), so the goal is to track license obligations *as a constraint* on what can be deployed and a *prerequisite* for any future IP-sale or licensing transaction. See @concepts/ip-sale-readiness.md.

## Narrative

### Cemini's own license

Cemini source code is **proprietary, all rights reserved by default** [NEEDS VERIFICATION 2026-05-03] — there is no `LICENSE` file at `/opt/cemini/` on the production host, which means default copyright applies. This is fine for a private deployment, but **not** equivalent to having an explicit license. For IP-sale readiness, the recommended fix is to add an internal `LICENSE` file declaring "Proprietary — All Rights Reserved" or a custom proprietary license clarifying ownership transfer terms.

The same applies to the librarian (`/opt/cemini-wiki/`) and to this OSINT workspace.

### Dependency license categories

Cemini's deployed dependencies fall into four risk buckets:

**Safe (no operational restrictions)** — MIT, Apache-2.0, BSD-3-Clause, ISC.
- Examples in stack: Redis (BSD-3-Clause), pgvector (PostgreSQL License — BSD-style), Polars (MIT), most Python ecosystem libs.
- Obligation: attribution in distributed binaries. For private SaaS deployments not distributing the binary, attribution is best-practice but not strictly required.

**Conditional (network-copyleft / strong copyleft)** — AGPL-3.0, GPL-3.0.
- **AGPL-3.0**: any user interacting with the software over a network must be able to receive the source. Docker isolation does *not* defeat this — the AGPL network clause was specifically drafted to close that loophole [Source: K27 / @sources/more-links-5-2-arch-eval.md].
  - Implication: any AGPL-3.0 dependency in the prod stack means Cemini's modifications + integration glue around that dependency must be source-available to users hitting it over the network.
  - Examples to watch (K12/K14 rejections): Firecrawl, OpenViking, SAMEP, NautilusTrader (LGPL transitive taint per K27).
- **GPL-3.0**: derivative works inherit GPL. K27 surfaced a non-obvious risk: **LLM agents reading GPL-licensed source code and emitting code based on that reading may produce derivative works** [Source: @sources/more-links-5-2-arch-eval.md]. This affects Cemini's autonomous-coding workflows if pointed at GPL repos.

**Restricted (non-commercial / research-only)** — CC-BY-NC-*, custom restrictive.
- Example: Moirai (CC-BY-NC-4.0) — rejected for Cemini deployment per K14.
- Implication: cannot be deployed in a revenue-generating context.

**Unknown (no LICENSE file)** — falls back to **default copyright = all rights reserved by upstream author** [Source: K27 missing-license pattern].
- Common failure mode: a GitHub repo with no LICENSE looks "free" but legally is not. K27 flagged this as a recurring blind spot in tool evaluations.
- Audit rule: if a candidate dependency has no `LICENSE`, no `package.json` `license` field, and no `pyproject.toml` license metadata, treat as **REJECT pending upstream clarification**.

### Cemini's adopted license-evaluation policy

Codified across K12/K14/K25/K27 deep-reads (see @sources/more-links-5-2-arch-eval.md, @sources/4-3-link-re-2.md, @sources/4-4-link-re-2.md):

1. Every Adopt/Defer/Reject decision in a Gemini-DR sweep must record the dependency's license explicitly.
2. AGPL-3.0 dependencies are **default-Reject** for production deployment; allowable only as Reference/Steal-from (read-the-code-but-don't-link-the-binary pattern).
3. GPL-3.0 dependencies require dual licensing or replacement before deployment.
4. CC-BY-NC and other commercial-restrictive licenses are categorically Reject for production.
5. Missing-license repos are Reject pending upstream LICENSE clarification.

This policy is *operational*, not aspirational — license findings have triggered concrete rejections across the K-series deep-reads.

### Risk surface for IP-sale or commercial license

When the IP is eventually transferred or licensed (see @concepts/ip-sale-readiness.md):

- **Buyer due-diligence scope**: full SBOM with license-per-component, including transitive dependencies. Tooling: `cyclonedx-bom`, `pip-licenses`, `npm-license-checker`. [NEEDS VERIFICATION 2026-05-03] — SBOM tooling not yet wired into Cemini CI.
- **Highest-risk findings**: any AGPL-3.0 dependency in prod (network-clause obligation transfers to buyer); any LLM-agent-generated code derived from GPL-3.0 sources (derivative-work claim risk).
- **Cleanest deliverable**: explicit Cemini LICENSE file + clean SBOM + recorded license-evaluation history (the K-series record is itself an asset here).

## Snippets

*(populate as license findings accrue.)*

## Dead Ends

*(none yet — license posture is newly tracked as of 2026-05-03.)*
