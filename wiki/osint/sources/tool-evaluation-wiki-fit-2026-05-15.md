---
title: "Tool Evaluation and Wiki Fit — 52-URL multi-wiki eval (2026-05-15)"
type: source
tags: [docx, tool-evaluation, multi-wiki, license-audit, ip-sale, cemini-internal, phase-0, k47]
keywords: [tool-evaluation, 52-url-audit, license-audit, agpl-poison-pill, adopt-tier, steal-from, cross-wiki-routing, fingerprint-suite, leann, llm-generated-eval]
related:
  - concepts/ip-sale-readiness.md
  - concepts/multi-wiki-eval-doc-level-vs-phase-0.md
  - concepts/paradigm-vs-license-inverse-correlation.md
  - entities/tools/fingerprint-suite.md
  - entities/tools/leann.md
  - entities/tools/website-downloader.md
  - concepts/kb-server-retrieval-scaling.md
  - sources/tool-eval-wiki-fit-v3-iteration-2026-05-16.md
maturity: validated
read_status: deep-read
created: 2026-05-15
updated: 2026-05-16
clusters: [eval, multi-wiki-routing, k47]
---

## Relations
- @cybersecurity-wiki/briefs/2026-05-15_osint-tool-eval-routing-2026-05-15.md  (cross-wiki brief)
- @seo-wiki/briefs/2026-05-15_osint-tool-eval-routing-2026-05-15.md  (cross-wiki brief)
- @image-gen-wiki/briefs/2026-05-15_osint-tool-eval-routing-2026-05-15.md  (cross-wiki brief)
- @ccc-wiki/briefs/2026-05-15_osint-tool-eval-routing-2026-05-15.md  (cross-wiki brief)

- @concepts/ip-sale-readiness.md — the report applies the IP-sale license gate (AGPL / non-commercial / no-license = reject)
- @concepts/multi-wiki-eval-doc-level-vs-phase-0.md — doc-level eval only; all Adopt verdicts still require a Phase-0 source audit before real adoption
- @concepts/paradigm-vs-license-inverse-correlation.md — Shadowbroker (most capable OSINT tool in the batch) is AGPL-3.0, reconfirming the pattern
- @entities/tools/fingerprint-suite.md — Adopt-tier, OSINT primary fit; locally adopted from this eval
- @sources/tool-eval-wiki-fit-v3-iteration-2026-05-16.md — successor batch: the K49 v3-iteration 46-repo eval
- @entities/tools/leann.md — Adopt-tier, cross-routed to OSINT (vector indexing for the librarian); locally adopted from this eval
- @concepts/kb-server-retrieval-scaling.md — K47 benchmark of the two Adopt-tier vector indexes against kb-server's brute-force search
- @entities/tools/website-downloader.md — re-evaluated here (Defer); already cataloged 2026-05-12 as Reference-only

## Raw Concept

- **Title**: Cemini Multi-Wiki Link Evaluation Report (v3) — "Tool Evaluation and Wiki Fit"
- **Type**: Internal evaluation document (.docx, LLM-generated)
- **Retrieved**: 2026-05-15
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/Tool Evaluation and Wiki Fit.docx`
- **Scope**: 52 URLs evaluated across all 6 Cemini wikis + /opt/cemini financial stack
- **Read status**: deep-read

This is a distinct 52-URL batch despite the report's "(v3)" self-label — the `v3` tag has been reused across several non-overlapping eval docs (see `sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md` (28-URL) and `sources/multi-wiki-tool-evaluation-v3.md` (26-tool)). No URL overlap with those batches. `preingest_check.py` verdict: NEW (unseen sha256).

## Narrative

A 52-URL doc-level evaluation against the standard two-gate protocol: (1) **license safety** — AGPL-3.0 / custom non-commercial / no-license = automatic reject for any IP-sale-bearing surface; (2) **architectural fit** — primary-wiki routing + cross-wiki routing.

### Tier distribution (52 total)

| Tier | Count | Members |
|------|-------|---------|
| Adopt | 8 | nano-banana-pro-prompts-recommend-skill, pm-claude-skills, defenseclaw, fingerprint-suite, Arcforge, LEANN, Awesome-finance-skills, DeepZero |
| Steal-from | 2 | oransim, evilcharts |
| Defer | 3 | Website-downloader, lytenyte, OpenAgents |
| Reference-only | 12 | bridge.surf, x-algorithm, kling.ai, elevenlabs.io, runwayml.com, viggle.ai, leonardo.ai, synthesia.io, fliki.ai, invideo.io, scispace.com, beautiful.ai |
| Reject | 9 | llm_engineering, live-trade-bench, Shadowbroker, GHOST-osint-crm, Reverse-Engineering, Awesome-LLM4Cybersecurity, checkmygit, WordListeXplorer, agents-towards-production |
| UNAVAILABLE | 18 | retrieval-failed URLs (no analysis possible) |

### OSINT-wiki primary-fit entries (5) + 1 cross-routed in

| Tool | Tier | Verdict / disposition |
|------|------|----------------------|
| `apify/fingerprint-suite` | Adopt | OSINT primary. Apache-2.0. **Locally adopted** → `entities/tools/fingerprint-suite.md` |
| `BigBodyCobain/Shadowbroker` | Reject | OSINT primary, but **AGPL-3.0 poison pill** — tactically perfect (60+ intel feeds, ADS-B/AIS/satellite) yet uninstallable on IP-sale grounds. Recorded here, no entity page |
| `AhmadIbrahiim/Website-downloader` | Defer | Already cataloged 2026-05-12 (Reference-only). Commodity wget wrapper, stale >2yr; we use `mcp__exa__crawling_exa`. No change |
| `elm1nst3r/GHOST-osint-crm` | Reject | OSINT primary, but **custom non-commercial license** — investigation-management CRM, exact fit yet blocked. Recorded here, no entity page |
| `scispace.com` | Reference-only | Proprietary SaaS (280M+ paper RAG agent). Architectural benchmark for the librarian's RAG orchestration; no codebase to adopt |
| `yichuan-w/LEANN` | Adopt | CCC primary, **cross-routed to OSINT** — 97% smaller vector index (60M chunks in 6GB). MIT, 11k★. **Locally adopted** → `entities/tools/leann.md` |

### Routed out of OSINT (cross-wiki briefs filed)

- **CCC wiki** — defenseclaw, Arcforge, Awesome-finance-skills, DeepZero, lytenyte, OpenAgents, nano-banana, pm-claude-skills, bridge.surf (agent/skill architecture references)
- **Image-gen wiki** — nano-banana-pro-prompts-recommend-skill (Adopt) + the proprietary video/avatar SaaS cluster (kling, elevenlabs, runwayml, viggle, leonardo, synthesia, fliki, invideo — all Reference-only)
- **SEO wiki** — pm-claude-skills, evilcharts (Steal-from), oransim (Steal-from), lytenyte, beautiful.ai
- **Cybersec wiki** — defenseclaw (Adopt), DeepZero (Adopt), fingerprint-suite (cross-route, fingerprint evasion), plus rejects Shadowbroker / WordListeXplorer / Reverse-Engineering / Awesome-LLM4Cybersecurity

### Adoption outcomes

- **Local adoptions (laptop)**: `fingerprint-suite`, `LEANN` — see respective entity pages.
- **Server adoption briefs (→ /opt/cemini/briefs/)**: `Awesome-finance-skills` (Cemini-financial — alphaear news/sentiment/predictor skill modules) and `pm-claude-skills` (Cemini-financial cross-route — financial-audit SKILL.md templates). Staged for server-Claude review/execution.

### Data-quality flags (report is LLM-generated; verify before trust)

- **18 of 52 URLs UNAVAILABLE** — over a third returned no retrievable data. Not failures of the tools; failures of the report's retrieval pass.
- **Arcforge license error**: report claims MIT; GitHub API returns `NOASSERTION` (unrecognized/custom license). Adopt verdict is **not safe** until the LICENSE file is verified — treat as Defer.
- **nano-banana license error**: report's aggregate "Clean MIT/Apache/BSD" line lists it, but its own per-URL entry says "NO LICENSE FOUND" and GitHub confirms no license. Not IP-safe; downgrade to Defer pending licensing.
- Prose is hyperbolic throughout ("phenomenally advanced", "fiercely optimized") — characteristic of LLM generation; star/commit figures cross-checked against GitHub API on ingest and broadly matched (fingerprint-suite 2,214★, LEANN 11,031★, Awesome-finance-skills 2,172★, pm-claude-skills 346★, defenseclaw 654★, DeepZero 425★, Shadowbroker 6,286★).

## Snippets

> "Adopt: 8 (nano-banana-pro-prompts-recommend-skill, pm-claude-skills, defenseclaw, fingerprint-suite, Arcforge, LEANN, Awesome-finance-skills, DeepZero) [...] Poison-pill licenses caught: 3 (AGPL-3.0 strictly located in Shadowbroker; Custom Non-commercial variants aggressively located in GHOST-osint-crm and agents-towards-production)"
> — [Source: Tool Evaluation and Wiki Fit.docx, Aggregate summary]

> "Shadowbroker offers an unprecedented [...] decentralized intelligence aggregation interface, simultaneously tracking ADS-B aircraft, AIS maritime vessels, and military recon satellites [...] However, the codebase is explicitly licensed under the virally restrictive AGPL-3.0 license, which acts as a definitive hard poison pill for any IP-sale-bearing surface."
> — [Source: Tool Evaluation and Wiki Fit.docx, URL 10]

## Dead Ends

- **Shadowbroker** — best-fit OSINT tool in the batch (geospatial intel aggregation, HMAC-signed AI co-analyst channel), rejected purely on AGPL-3.0. The capability is worth re-examining only if it ever relicenses or if a permissively-licensed equivalent surfaces.
- **GHOST-osint-crm** — investigation-management CRM is a genuine OSINT-workflow gap, but the custom non-commercial license is terminal. Gap remains open; a permissive alternative would be worth a Tier-1 search.
