---
title: "Multi-Wiki Tool Evaluation — Strategic Tool-Evaluation & Cross-Wiki Routing Assessment (36-repo batch, May 2026)"
type: source
tags: [source, tool-evaluation, phase-0-audit, multi-wiki-routing, license-audit, ip-sale, k51]
keywords: [multi-wiki-tool-eval, 36-repo-batch, ip-sale-risk, no-license-epidemic, copyleft-poison-pill, cross-wiki-routing, zero-adopt, llm-generated-eval]
related:
  - entities/tools/ml-from-scratch.md
  - entities/tools/osiris.md
  - entities/tools/indicator-go-ta.md
  - entities/tools/mlfinlab.md
  - concepts/cemini-license-posture.md
  - sources/multi-wiki-tool-eval-ipsale-risk-2026-05-17.md
maturity: validated
read_status: deep-read
created: 2026-05-18
updated: 2026-05-18
clusters: [tool-evaluation]
---

## Relations

- @entities/tools/ml-from-scratch.md — Reference-only, OSINT-primary (NumPy ML reference implementations)
- @entities/tools/osiris.md — Reject (no-license), OSINT-primary (real-time OSINT dashboard, "Palantir alternative")
- @entities/tools/indicator-go-ta.md — Defer, Cemini-financial primary (Go technical-analysis library)
- @entities/tools/mlfinlab.md — Reject (license unverified), Cemini-financial primary (Hudson & Thames ML-finance toolbox)
- @concepts/cemini-license-posture.md — the IP-sale copyleft / no-license posture this eval enforces
- @sources/multi-wiki-tool-eval-ipsale-risk-2026-05-17.md — immediately-prior multi-wiki tool-eval batch (K50, 56 repos); this is the successor batch
- @cybersecurity-wiki/briefs/2026-05-18_multi-wiki-tool-eval-k51-cybersec.md — cross-routed brief: 14 cybersec-primary tools
- @ccc-wiki/briefs/2026-05-18_multi-wiki-tool-eval-k51-ccc.md — cross-routed brief: 10 CCC-primary tools
- @image-gen-wiki/briefs/2026-05-18_multi-wiki-tool-eval-k51-imagegen.md — cross-routed brief: 2 image-gen-primary items
- @seo-wiki/briefs/2026-05-18_multi-wiki-tool-eval-k51-seo.md — cross-routed brief: 2 SEO-primary items

## Raw Concept

- **Title**: Strategic Tool-Evaluation and Cross-Wiki Routing Assessment
- **Type**: LLM-generated multi-wiki tool-evaluation report (Gemini Deep Research style). Filename says "Prompt" but the artifact is the evaluation *report*, not a prompt.
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/multi-wiki-tool-eval-prompt-2026-05-18.docx`
- **Retrieved**: 2026-05-18 (dropped into `research to be indexed/` as `Multi-Wiki Tool Evaluation Prompt.docx`)
- **sha256**: `8e035696c2cc67a2...` · **size**: 3,089,848 bytes · **Preingest verdict**: NEW
- **Scope**: 36 candidate repositories / web resources evaluated across 7 surfaces (Cemini-financial / OSINT / Cybersec / Image-gen / SEO / 3D-printing / CCC) against operational utility + IP-sale licensing compliance.

Doc-level evaluation — verdicts derive from the report's own research, not from a Cemini Phase-0 source audit. Phase-0 clone audits remain owed before any code lands on a production surface. Successor to the K50 "56-repo IP-Sale Risk Assessment" batch (`@sources/multi-wiki-tool-eval-ipsale-risk-2026-05-17.md`).

## Narrative

### Headline — zero Adopt, and the no-license epidemic continues

**Nothing in this batch is adoptable.** All 36 items land at Steal-from or below. The dominant cause is the same licensing-hygiene crisis K50 surfaced: of 36 repos, **24 have NO LICENSE FOUND** and **9 are UNVERIFIED** — 33 of 36 cannot be cleared for an IP-sale-bound stack. Only **1 repo (Project-Ideas-And-Resources) has a clean, verified MIT license** — and it is content-only (Reference-only). One AGPL-3.0 poison pill caught (`videoeditor`, `LICENSE-AGPL3.md` in root → terminal reject).

### Verdict ledger (36 items)

| Tier | Count | Items |
|------|-------|-------|
| **Adopt** | **0** | — |
| Steal-from | 8 | openai/skills, raptor, mimeo, playwright-computer-use, Codeman, md2html, Citadel, agent-toolkit |
| Defer | 5 | indicator, opendrop, Shells-X, AgentGym-RL, Grafana-Final-Scanner |
| Reference-only | 5 | Project-Ideas-And-Resources, frontend-challenges, ML-From-Scratch, wan_22_remix (Reddit), awesome-cli-coding-agents |
| Reject | 17 | ParseStudio, nellavio, GarudRecon, videoeditor (AGPL), relay_bypass_server, netgoat, ssh-ai-chat, safeline, NetAlertX, buddyme, fd, Google-Maps-Scrapper, Poc, osiris, mlfinlab, litellm-agent-platform, mantishack |
| Unavailable | 1 | b589174b-… (opensourceprojects.dev — no data retrieved) |

> The doc's own aggregate summary miscounts (claims "Steal-from: 9 / Reference-only: 4"). The per-URL `Tier:` lines — the authoritative count — give **8 Steal-from / 5 Reference-only**. The summary also omits `awesome-cli-coding-agents` from its Reference list. Counts above are the reconciled per-URL figures.

### Primary-fit distribution — this batch is barely an OSINT doc

| Surface | Primary-fit count |
|---------|-------------------|
| Cybersec wiki | 14 |
| CCC wiki | 10 |
| OSINT wiki | 5 |
| Cemini financial | 2 |
| Image-gen wiki | 2 |
| SEO wiki | 2 |
| 3D-printing wiki | 0 |
| None | 1 |

~83% of the batch is non-OSINT. The OSINT workspace keeps only the 4 OSINT/Cemini-financial-primary items as entity stubs; everything else is cross-routed (see Relations → the four destination-wiki briefs).

### OSINT / Cemini-financial-relevant items (kept as stubs)

- **ML-From-Scratch** (`eriklindernoren/ML-From-Scratch`) — Reference-only, OSINT-primary. Bare-bones NumPy implementations of ML models; finalized educational reference (no updates since 2023). No license → read-for-understanding only.
- **osiris** (`simplifaisoul/osiris`) — Reject (no license), OSINT-primary. Real-time OSINT dashboard self-billed as a "Palantir alternative" — aggregates aircraft / satellite / GDELT conflict feeds onto a 60fps WebGL map. Genuinely on-target for OSINT visualization; rejected purely on the missing-license IP risk. Worth re-evaluating if a license appears.
- **indicator** (`cinar/indicator`) — eval said Defer; **license check flips it to Reject** (AGPL-3.0 — see follow-up below). Go TA library: 80+ indicators + backtesting, 852★.
- **mlfinlab** (`hudson-and-thames/mlfinlab`) — Reject, Cemini-financial. Hudson & Thames ML-for-finance toolbox, 4.7k★. Reject **confirmed** by license check (non-OSS license — see below).

### License-check follow-up (2026-05-18)

The eval flags many verdicts as license-unverified. A targeted GitHub-API license check was run on the four items where verification could change the verdict:

| Tool | Eval verdict | Verified license | Corrected verdict |
|------|-------------|------------------|-------------------|
| `fd` (`sharkdp/fd`) | Reject (no-license) | **MIT + Apache-2.0** dual (both `LICENSE-*` files present) | Clean — the Reject was a retrieval-data artifact; `fd` is fully adoptable. Cybersec-primary. |
| `indicator` (`cinar/indicator`) | Defer | **AGPL-3.0** (`LICENSE.md` = GNU AGPL v3) | **Hard Reject** — license-drift: the v2.x.x relicense the eval noticed *was* the move to AGPL. Network-copyleft poison pill. |
| `osiris` (`simplifaisoul/osiris`) | Reject (no-license) | `license: null`, no `LICENSE`/`COPYING` file anywhere | Reject **confirmed** — genuinely unlicensed (verified, not an artifact). |
| `mlfinlab` (`hudson-and-thames/mlfinlab`) | Reject (license unverified) | `LICENSE.txt` = "Other" / `NOASSERTION` (non-OSS) | Reject **confirmed** — custom commercial license, not permissive. |

Net effect: 1 verdict softened (`fd` is clean, though it routes to the cybersec wiki, not OSINT) and 1 verdict hardened (`indicator` Defer → Reject, an AGPL poison pill the Defer label understated). `osiris` and `mlfinlab` rejects stand on verified grounds. The pattern holds — the eval's conservative license posture was right to gate; verification mostly confirms rejection and occasionally catches a worse problem (AGPL) than "unknown."

### Cross-wiki routing

Four destination briefs created via `cross_wiki_route.py` (see Relations):
- **Cybersec (14)** — GarudRecon, relay_bypass_server, raptor, netgoat, ssh-ai-chat, safeline, NetAlertX, opendrop, Shells-X, AgentGym-RL, fd, Poc, Grafana-Final-Scanner, mantishack.
- **CCC (10)** — openai/skills, mimeo, playwright-computer-use, Codeman, md2html, Citadel, agent-toolkit, buddyme, litellm-agent-platform, awesome-cli-coding-agents. Notable Steal-from: Citadel (Claude Code orchestration OS — four-tier `/do` routing, campaign persistence, lifecycle hooks) and agent-toolkit (17.6k Claude-marketplace installs).
- **Image-gen (2)** — videoeditor (AGPL reject; Vibe AI assistant architecture noted), wan_22_remix Reddit thread (uncensored-video model pointer).
- **SEO (2)** — nellavio (Next.js dashboard boilerplate, reject no-license), frontend-challenges + Project-Ideas-And-Resources (web-template references).

### Takeaway

A zero-yield batch for the OSINT workspace and for Cemini's production stack. Its value is almost entirely (a) a continued license-hygiene datapoint — the no-license default is now the single biggest blocker across these LLM-sourced batches — and (b) cross-wiki intelligence for the Cybersec and CCC wikis. No Phase-0 audits are triggered (nothing reached Adopt). `indicator` and `osiris` are the two items worth a re-look if their licenses are ever clarified.

## Snippets

> "Where no explicit license is found in the available documentation, the asset receives a mandatory classification to preempt inadvertent IP contamination." [Source: multi-wiki-tool-eval-prompt-2026-05-18.docx]

> "License pattern summary — NO LICENSE FOUND: 24 · Poison-pill licenses caught: 1 (AGPL-3.0 in videoeditor) · Clean MIT / Apache / BSD: 1 · UNVERIFIED: 9" [Source: multi-wiki-tool-eval-prompt-2026-05-18.docx]

> "osiris ... boldly positioned as a production-grade, real-time OSINT dashboard and a direct Palantir alternative, intelligently aggregating vast global intelligence feeds — including aircraft, satellites, and GDELT conflict events — onto a single, 60fps WebGL map interface." [Source: multi-wiki-tool-eval-prompt-2026-05-18.docx]

## Dead Ends

- **Treating the doc's aggregate-summary counts as authoritative** — the summary miscounts Steal-from (9 vs actual 8) and Reference-only (4 vs actual 5). The per-URL `Tier:` fields are the source of truth.
- **The eval's `fd` reject was a data artifact** — `fd` (43k★ Rust `find` replacement) was rejected for "no license found", but the license check (2026-05-18) confirms a clean **MIT + Apache-2.0 dual license**. The lesson is not "trust the eval's rejects" — it is that no-license rejects specifically warrant a one-call verification, because the eval cannot tell "genuinely unlicensed" from "license present but not retrieved." Verification resolved both ways here: `fd` cleared, `osiris` confirmed genuinely unlicensed.
