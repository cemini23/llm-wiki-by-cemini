---
title: Cemini License Posture — Dependency Obligations & IP Status
type: concept
tags: [license-compliance, audit-security, cemini-internal, ip-sale-readiness]
keywords: [AGPL-3.0, GPL-3.0, EUPL-1.2, MIT, Apache-2.0, BSD-3-Clause, CC-BY-NC-SA, derivative-work, network-copyleft, default-copyright, dual-license-ambiguity, namespace-confusion]
related:
  - concepts/ip-sale-readiness.md
  - sources/more-links-5-2-arch-eval.md
  - sources/4-3-link-re-2.md
  - sources/4-4-link-re-2.md
  - sources/5-4-links-tool-eval.md
  - sources/links-2-5-4-tool-eval.md
  - sources/5-6-links-eval-batch.md
  - sources/evaluating-project-links-stacks.md
  - concepts/cemini-deployment.md
  - entities/infrastructure/cemini-stack.md
  - entities/tools/klaassen-magnus-elo.md
  - entities/tools/loki-mode.md
  - entities/tools/pybroker.md
  - entities/tools/gitnexus.md
  - entities/tools/deepteam.md
  - entities/tools/taranis-ai.md
  - concepts/mitre-atlas-taxonomy.md
  - entities/tools/blade-github.md
  - concepts/regime-conditioned-evaluation.md
  - sources/odini-air-gap-magnetic-field.md
  - concepts/rlhf-critic-bias.md
  - sources/rlhf-critic-bias-al-zawahreh-2026.md
  - concepts/hedge-fund-open-source-tooling.md
  - entities/tools/arcticdb.md
maturity: draft
hub: true
created: 2026-05-03
updated: 2026-05-18
---

## Relations

- @concepts/ip-sale-readiness.md — license posture is a prerequisite for any IP-sale or partial-license transaction
- @sources/more-links-5-2-arch-eval.md — K27 surfaced AGPL-3.0 Docker-defeat pattern + GPL-3.0 LLM-agent derivative-work risk + missing-license default-copyright pattern (three license-compliance failure modes)
- @sources/4-3-link-re-2.md — Moirai (CC-BY-NC-4.0) + Firecrawl (AGPL-3.0) rejections recorded in K14 deep-read
- @sources/4-4-link-re-2.md — AGPL-3.0 contamination warnings (OpenViking, SAMEP) recorded in K12 deep-read
- @sources/5-4-links-tool-eval.md — 2026-05-04 ingest surfaced two new license patterns: **CC-BY-NC training-data contamination** (tennis_atp dataset → tennis_match_prediction MIT code becomes NC-bound) + **namespace confusion risk** (1weiho/open-slide vs CMU's openslide.org medical library)
- @sources/links-3-5-4-tool-eval.md — 2026-05-04 ingest surfaced **Elastic License v2 (ELv2)** as 9th license-pattern (source-available with use-restrictions): Context Mode tool. Reject for production; reference-only.
- @sources/links-2-5-4-tool-eval.md — 2026-05-04 ingest surfaced **dual-license MIT-vs-GPL ambiguity** pattern (Lumibot README claims MIT, core repo files labeled GPL-3.0)
- @sources/5-6-links-eval-batch.md — 2026-05-06 K32 ingest surfaced **License Drift** as 10th license-pattern (MIT→BUSL-1.1 transition w/ stale third-party aggregator misreport): asklokesh/loki-mode. Operational lesson: NEVER trust aggregators in M&A diligence; always check canonical repo's current `LICENSE` + recent commits.
- @sources/evaluating-project-links-stacks.md — 2026-05-11 K39 ingest surfaced **EUPL-1.2 IP-sale poison pill** as 11th license-pattern: taranis-ai. EU Public License v1.2 has AGPL-3.0-equivalent network-copyleft behavior + explicit Article 5/14 IP-sale obligations (mandatory source disclosure to acquirers).
- @entities/tools/taranis-ai.md — EUPL-1.2 exemplar (catalog mode #11). Also 3rd `read_status=no-LICENSE`-pattern-adjacent finding (after K36 finance-skills + K38 AI-Trader).
- @entities/tools/loki-mode.md — License Drift exemplar (catalog mode #10)
- @entities/tools/pybroker.md — Commons Clause poison pill (catalog mode #5-family — Apache+restrictive-amendment)
- @entities/tools/gitnexus.md — PolyForm Noncommercial 1.0.0 (catalog mode #9 family — source-available with use-restrictions)
- @entities/tools/deepteam.md — Apache+commercial-vendor-pull-up (informal pattern; not yet a catalog mode unless it generalizes)
- @entities/tools/klaassen-magnus-elo.md — exemplar of pattern #4 (CC-BY-NC training-data contamination): MIT code, NC-bound data dependency, requires retraining-on-commercial-feeds before production deployment
- @concepts/mitre-atlas-taxonomy.md — recorded 2026-05-04 license correction: ATLAS data feed is Apache-2.0 (not CC BY 4.0 as K28 eval claimed); website-presented content has separate MITRE terms; **eval-time-detected license claims should be verified against canonical LICENSE file in upstream repos before recording**
- @concepts/rlhf-critic-bias.md — **parallel pattern catalog** (K40). This page systematizes the structural moves of *license-claim mischaracterization* (now at 11 modes). The RLHF Critic Bias 6-category Rhetorical Catalog systematizes the structural moves of *LLM-generated critique*. Both convert recurring patterns into checklist-style audit aids. The structural argument also explains *why* eval-brief mischaracterization is recurring (mirror asymmetric-penalty: "I said adopt and it was unfit" < "I said skip and it was useful").
- @sources/rlhf-critic-bias-al-zawahreh-2026.md — RLHF Critic Bias source (Al-Zawahreh April 2026, draft maturity, Reference/Steal-from)
- @concepts/hedge-fund-open-source-tooling.md — K52 hedge-fund OSS catalog; 21 of 22 repos are MIT/Apache/BSD, the lone exception is a **BSL** repo (ArcticDB) — a clean data point on the open/closed-firm split
- @entities/tools/arcticdb.md — **Business Source License (BSL)** exemplar: source-available, free for non-production, paid license required for commercial deployment. Same family as ELv2 (#9) / License-Drift-to-BUSL (#10) — a capable tool gated entirely on a non-OSI license

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

**Conditional (network-copyleft / strong copyleft)** — AGPL-3.0, GPL-3.0, EUPL-1.2.
- **AGPL-3.0**: any user interacting with the software over a network must be able to receive the source. Docker isolation does *not* defeat this — the AGPL network clause was specifically drafted to close that loophole [Source: K27 / @sources/more-links-5-2-arch-eval.md].
  - Implication: any AGPL-3.0 dependency in the prod stack means Cemini's modifications + integration glue around that dependency must be source-available to users hitting it over the network.
  - Examples to watch (K12/K14 rejections): Firecrawl, OpenViking, SAMEP, NautilusTrader (LGPL transitive taint per K27).
- **GPL-3.0**: derivative works inherit GPL. K27 surfaced a non-obvious risk: **LLM agents reading GPL-licensed source code and emitting code based on that reading may produce derivative works** [Source: @sources/more-links-5-2-arch-eval.md]. This affects Cemini's autonomous-coding workflows if pointed at GPL repos.
- **EUPL-1.2** (added K39 2026-05-11 from `@entities/tools/taranis-ai.md`): European Union Public Licence v1.2 is **functionally AGPL-3.0-equivalent for network deployments + explicit IP-sale poison pill**. Article 5 requires source disclosure for derivative works distributed by any means including network. Article 14.3 binds successors-in-interest, meaning a future IP-sale acquirer inherits the source-disclosure obligation. The EUPL is explicitly compatible-with-AGPL/GPL via its Article 5 compatibility list — once a derivative chains through any of those, the strongest license dominates.
  - Implication: **default-Reject for production**; allowable only as Reference (read-the-code, don't link). Treat exactly as AGPL-3.0 for prod stack decisions.
  - Examples: taranis-ai (K39 Reject 2026-05-11).

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
6. **(Added 2026-05-04 from `@sources/5-4-links-tool-eval.md`)** CC-BY-NC training-data contamination — MIT code coupled to NC-licensed datasets propagates NC restriction to derivative model weights and feature pipelines. Algorithm extraction is safe; deployment requires retraining on commercially-licensed data with full provenance documentation.
7. **(Added 2026-05-04 from `@sources/links-2-5-4-tool-eval.md`)** Dual-license MIT-vs-GPL ambiguity — when a repository's README claims one license but core files carry another, treat as REJECT pending file-by-file legal audit. Importing modules under false license assumptions is a forced-disclosure risk.
8. **(Added 2026-05-04 from `@sources/5-4-links-tool-eval.md`)** Namespace confusion — repositories sharing names with established libraries (e.g., 1weiho/open-slide vs CMU's openslide.org medical library) trigger false-positive SCA scanner flags during M&A diligence. Document explicit distinction in any adoption decision.
9. **(Added 2026-05-11 from `@sources/evaluating-project-links-stacks.md` K39)** EUPL-1.2 = AGPL-3.0-equivalent for prod + IP-sale poison pill — Article 5 = strong copyleft (network-distribution = source release); Article 14.3 binds successors-in-interest, so any future Cemini IP-sale inherits source-disclosure to acquirer. Default-Reject for production; Reference-only.

This policy is *operational*, not aspirational — license findings have triggered concrete rejections across the K-series deep-reads.

### License-pattern catalog (ten failure modes)

| # | Pattern | First seen | Mitigation |
|---|---------|------------|------------|
| 1 | NO LICENSE → default copyright (8+ occurrences: K27 multiple, K36 Anthropic finance-skills, K38 HKUDS/AI-Trader, K38 Readme.skill, K39 virattt/ai-hedge-fund 58.6k★, K39 19PINE-AI/ikp, K39 Phase-0 meridian, K39 Phase-0 mac-code, K39 Steal-from gabagool) | K27 (multiple) | Audit rule: REJECT until upstream LICENSE clarified. **Star count does NOT confer derivative right** — 58k-star repos can still be `NOLICENSE`. Canonical verification: `gh api repos/<owner>/<repo> --jq '.license.spdx_id'` returns `null` → blocked. **README badges/footers claiming MIT must not be trusted in isolation** — K39 Phase-0 audit confirmed meridian + mac-code + gabagool all return `null` despite README MIT claims. README claim and repo reality routinely disagree. |
| 2 | AGPL network-clause Docker-defeat | K27 (SocratiCode) | Reject for any networked deployment; allow only as static reference reading |
| 3 | GPL-3.0 LLM-agent derivative-work | K27 (freqtrade, qb-core) | Quarantine agents — never feed GPL source to coding agents writing into Cemini |
| 4 | **CC-BY-NC training-data contamination** | **5_4-links (tennis_atp + tennis_match_prediction)** | Extract algorithm only; retrain against commercially-licensed data |
| 5 | **Dual-license MIT-vs-GPL ambiguity** | **links-2-5_4 (Lumibot)** | File-by-file legal audit before any import; default-Reject pending clarification |
| 6 | **Namespace confusion** | **5_4-links (1weiho/open-slide vs openslide.org)** | Document explicit distinction in adoption decision; document for SCA scanners |
| 7 | LGPL dynamic-linking ambiguity (PyO3) | links-2-5_4 (nautilus_trader) | Defer pending acquirer legal counsel review of dynamic linking vs derivative-work boundary |
| 8 | Dual-licensing enterprise-tier gating | links-2-5_4 (shannon, repowise) | Reference-only; enterprise tier extracts critical features behind paywall, OSS Lite is intentionally degraded |
| 9 | **Source-available with use-restrictions** (Elastic License v2 / SSPL family) | **K30 links-3-5_4 (Context Mode, ELv2)** | Reject for production deployment (ELv2 forbids hosting-as-service + circumvention). Allow only as architectural-reference reading. Does NOT meet OSI open-source definition.
| 10 | **License Drift — repository-aggregator metadata staleness** (MIT→BUSL-1.1, MIT→PolyForm, etc.) | **K32 5_6-links (asklokesh/loki-mode)** | Always read canonical repo's CURRENT `LICENSE` file + recent commits + any `LICENSE-CHANGE-NOTICE.md`. NEVER trust libraries.io / SourceForge mirrors / search-result snippets / `pip-licenses` aggregators alone — they sync at a point in time and may report stale licenses for weeks/months after upstream change. M&A-grade diligence requires canonical-source verification. |
| 11 | **EUPL-1.2 IP-sale poison pill** (AGPL-3.0-equivalent + Article 14.3 binds successors) | **K39 evaluating-project-links-stacks (taranis-ai)** | Default-Reject for production deployment exactly like AGPL-3.0. Article 5 network-distribution = source-disclosure obligation; Article 14.3 binds successors-in-interest = future Cemini IP-sale acquirer inherits source-disclosure. Reference-only adoption allowed (read-the-code, don't link to it). |

**Apache + commercial vendor pull-up** (deepteam / Confident AI) is a related but distinct pattern: license is genuinely Apache-2.0 clean, but project actively channels users to a SaaS upgrade path. Not a license-rejection per se; cost/lock-in axis to flag during operational decision. Captured here informally; not a separate catalog mode unless it generalizes beyond confident-ai.

### Risk surface for IP-sale or commercial license

When the IP is eventually transferred or licensed (see @concepts/ip-sale-readiness.md):

- **Buyer due-diligence scope**: full SBOM with license-per-component, including transitive dependencies. Tooling: `cyclonedx-bom`, `pip-licenses`, `npm-license-checker`. [NEEDS VERIFICATION 2026-05-03] — SBOM tooling not yet wired into Cemini CI.
- **Highest-risk findings**: any AGPL-3.0 dependency in prod (network-clause obligation transfers to buyer); any LLM-agent-generated code derived from GPL-3.0 sources (derivative-work claim risk).
- **Cleanest deliverable**: explicit Cemini LICENSE file + clean SBOM + recorded license-evaluation history (the K-series record is itself an asset here).

## Snippets

### License Drift exemplar (loki-mode BUSL transition, K32 catalog mode #10)

> "The foremost risk is License Drift. The project transitioned from the permissive MIT license to the restrictive BUSL-1.1 recently. However, online aggregators and older documentation still falsely report it as MIT. Trusting third-party aggregators over the actual repository's commit history in an M&A context leads to catastrophic due-diligence failure." [Source: 5_6 links.docx URL 14, K32 Gemini DR eval batch]

### NO-LICENSE-popular-repo recurrence (K39 batch closeout, 2026-05-11)

> Of 14 license-pending repos resolved via `gh api` SPDX lookup in the K39 wave-4 batch: 9 returned clean SPDX IDs (MIT, Apache-2.0), 2 returned `NOLICENSE`, 3 returned `NOASSERTION` (LICENSE present but non-standard). **The 2 NOLICENSE findings include `virattt/ai-hedge-fund` at 58.6k stars and `19PINE-AI/ikp` at 69 stars.** This brings the catalog-mode-#1 occurrence count to 5+: K27 (multiple), K36 (Anthropic finance-skills), K38 (HKUDS/AI-Trader), K39 (virattt + 19PINE-AI). The 58.6k-star case is the most operationally telling — high social-proof signal coexists with full no-derivative-right blocker. Tooling lesson: `gh api repos/<owner>/<repo> --jq '.license.spdx_id'` is canonical for this check, faster + more reliable than `crawling_exa` against the LICENSE file URL because it returns `null` for missing-LICENSE in one call rather than requiring a 404 inference.

### K39 Phase-0 audit batch addendum (2026-05-12) — 2 more no-LICENSE catches

> K39 RED-FLAG queue Phase-0 batch (5 tools audited 2026-05-12) surfaced 2 additional catalog-mode-#1 occurrences: **`rynfar/meridian` (1,221★, README badge claims MIT)** and **`walter-grace/mac-code` (975★, README claims MIT)** both return `gh api license.spdx_id = null`. Total occurrence count now **7+**. K39 alone surfaces **4 of the 7** (virattt + 19PINE-AI + meridian + mac-code) — a single eval-brief ingest produced more catalog-#1 catches than the prior 2 K-cycles combined. Mechanism: Phase-0 audit discipline (cf. CLAUDE.md "Phase-0 audit pattern") catches what eval-brief intake misses. README license claims continue to be wrong roughly 1-in-15 against `gh api` ground truth across the K-series sample. **Operational consequence**: every K-series intake should run `gh api license.spdx_id` against every Adopt/Steal-from URL upfront, not at Phase-0 — the cost is one API call per URL.

### K39 Steal-from batch addendum (2026-05-12) — gabagool = 8th no-LICENSE catch + Steal-from pattern duplication

> K39 Steal-from Phase-0 (2 tools, 2026-05-12) surfaced **1 additional GO** (`NVIDIA/OpenShell`, Apache-2.0 verified, policy schemas standalone-portable for FastMCP hardening) **and 1 additional no-LICENSE catch**: `strongca22-cpu/gabagool` (180★, README claims MIT, `gh api license.spdx_id` = null). **8th occurrence**; K39 alone now accounts for **5 of 8** (virattt + 19PINE-AI + meridian + mac-code + gabagool). Beyond the license blocker, gabagool's risk/arbitrage math is a subset re-implementation of K38-certified CloddsBot — Cemini's Kalshi adapter should extract from CloddsBot (MIT, 254★, 5-factor risk decomposition, already Kalshi-aware via `PLATFORM_RISK_SCORES`) and skip gabagool entirely. **New observation**: Steal-from intent ≠ license-bypass. Pattern extraction still requires a clean upstream license for IP-sale-readiness; the no-LICENSE blocker applies symmetrically to Adopt and Steal-from paths.

## Dead Ends

*(none yet — license posture is newly tracked as of 2026-05-03.)*
