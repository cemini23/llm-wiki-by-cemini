---
title: "Cemini Multi-Wiki Link Evaluation Report (v3) — 28-URL eval (May 14 2026)"
type: source
tags: [source, github-audit, eval, multi-wiki-routing, license-audit, phase-0-pending, k44]
keywords: [k44-ingest, 28-url-audit, doc-level-eval, adopt-steal-defer-reject, cross-wiki-routing, ip-sale-readiness, copyleft-poison, llm-generated-eval]
related:
  - entities/tools/aulekator-polymarket-btc-bot.md
  - entities/tools/supavec.md
  - entities/tools/lap-platform.md
  - entities/tools/awesome-polymarket-tools-harish-garg.md
  - entities/tools/citriniresearch-2028-gic.md
  - entities/tools/awesome-osint-arsenal-rawfilejson.md
  - entities/tools/awesome-prediction-market-tools-aarora4.md
  - concepts/cemini-license-posture.md
  - concepts/multi-wiki-eval-doc-level-vs-phase-0.md
maturity: validated
read_status: deep-read
created: 2026-05-14
updated: 2026-05-14
clusters: [eval, multi-wiki-routing, k44]
---

## Relations
- @ccc-wiki/entities/tools/alumnium.md  (cross-wiki stub)
- @ccc-wiki/entities/tools/optillm.md  (cross-wiki stub)
- @ccc-wiki/entities/tools/adamsreview.md  (cross-wiki stub)
- @ccc-wiki/entities/tools/thuki.md  (cross-wiki stub)
- @ccc-wiki/entities/tools/jcode.md  (cross-wiki stub)
- @ccc-wiki/entities/tools/red-run.md  (cross-wiki stub)
- @ccc-wiki/entities/tools/lap-platform.md  (cross-wiki stub)
- @ccc-wiki/entities/tools/gtm-agents.md  (cross-wiki stub)
- @ccc-wiki/entities/tools/gym-anything.md  (cross-wiki stub, DEFER)
- @cybersecurity-wiki/entities/tools/betterleaks.md  (cross-wiki deep entity — pre-IP-sale audit critical)
- @cybersecurity-wiki/entities/tools/ai-infra-guard.md  (cross-wiki stub)
- @cybersecurity-wiki/entities/tools/cariddi.md  (cross-wiki stub)
- @cybersecurity-wiki/entities/tools/czkawka.md  (cross-wiki stub)
- @seo-wiki/entities/tools/geo-seo-claude.md  (pre-existing validated entity, K44 cross-reference appended; reconfirms 2026-05-07 SEO-wiki Phase-0 GO)
- @seo-wiki/entities/tools/gtm-agents.md  (cross-wiki stub)
- @image-gen-wiki/entities/training-tools/czkawka.md  (cross-wiki stub, LoRA dedup)
- @image-gen-wiki/entities/custom-nodes/ai-infra-guard.md  (cross-wiki stub, ComfyUI vuln detection)

- @entities/tools/aulekator-polymarket-btc-bot.md — ADOPT-tier (MIT, NautilusTrader core), direct Cemini-financial fit
- @entities/tools/supavec.md — STEAL-FROM (Apache-2.0, PostgreSQL+Supabase RAG)
- @entities/tools/lap-platform.md — STEAL-FROM (Apache-2.0, OpenAPI→agent-tool compilation)
- @entities/tools/awesome-polymarket-tools-harish-garg.md — REFERENCE-ONLY (CC0-1.0, safe)
- @entities/tools/citriniresearch-2028-gic.md — REFERENCE-ONLY (no license, macro essay)
- @entities/tools/awesome-osint-arsenal-rawfilejson.md — REJECT (no license)
- @entities/tools/awesome-prediction-market-tools-aarora4.md — REJECT (no license)
- @concepts/cemini-license-posture.md — same IP-sale lens applied per verdict
- @concepts/multi-wiki-eval-doc-level-vs-phase-0.md — K43 lesson restated: all ADOPTs here require Phase-0 source audits before actual adoption

## Raw Concept

- **Format**: docx (Cemini-internal eval document; v3 versioning suggests prior iterations)
- **Date**: May 14, 2026
- **Drop location**: `research to be indexed/Tool Evaluation for Cemini Wiki Integration.docx` → librarian
- **sha256**: `8353a99683cb689d...`
- **Size**: 3,068,059 bytes
- **Preingest verdict**: NEW
- **Author**: unknown (LLM-mediated; voice and structure consistent with deep-research synthesis)

**What prompted this page**: A 28-URL evaluation batch — the **largest single-source cross-wiki-routing event documented so far** (exceeds the K43 14-repo audit). Spans all 6 sibling wikis with explicit primary-fit + cross-route assignments. Distinct from K43 in two ways: (a) it explicitly frames the **IP-sale-readiness** of Cemini's commercial suite as the overarching verdict lens; (b) it introduces a "Steal-from" tier with copyleft-isolation discipline (laptop-side only, no compiled binary into shipped product).

## Narrative

### Verdict ladder (extends Cemini convention)

The eval uses a 5-tier ladder structurally identical to the Cemini house convention from K41/K43, with one re-naming:

- **Adopt** — install directly, depend on upstream (=Cemini ADOPT)
- **Steal-from** — patterns only; laptop-side or non-distributed deployment (=Cemini STEAL-FROM)
- **Defer** — recheck in 30-90 days (=Cemini DEFER)
- **Reference-only** — useful as catalog/reference, never code-coupled (=Cemini REFERENCE-ONLY)
- **Reject** — license-fatal or domain-fatal (=Cemini REJECT)
- **UNAVAILABLE** — added category: URL failed retrieval; no evaluation possible

### 28 verdicts at a glance

| # | Asset | License | Stars | Verdict | Primary fit | Cross-routes |
|---|-------|---------|-------|---------|-------------|--------------|
| 1 | 2028 Global Intelligence Crisis (citriniresearch) | NO LICENSE | — | Reference-only | OSINT | none |
| 2 | runablehq/mini-browser | UNVERIFIED | — | UNAVAILABLE | — | — |
| 3 | blacklanternsecurity/red-run | GPL-3.0 | 160 | Steal-from | CCC | Cybersec |
| 4 | Lap-Platform/LAP | Apache-2.0 | 241 | Steal-from | CCC | OSINT |
| 5 | aulekator/Polymarket-BTC-15-Minute-Trading-Bot | MIT | 274 | **Adopt** | Cemini-financial | OSINT |
| 6 | zerotracelab.com/blog/dll-sideloading | UNVERIFIED | — | UNAVAILABLE | — | — |
| 7 | alumnium-hq/alumnium | MIT | 655 | **Adopt** | CCC | Cemini-financial |
| 8 | quiet-node/thuki | Apache-2.0 | 485 | Steal-from | CCC | none |
| 9 | cmu-l3/gym-anything | MIT | 211 | Defer | CCC | none |
| 10 | chrisbanes/skills | Apache-2.0 | 497 | Reject (Android, domain mismatch) | — | none |
| 11 | supavec/supavec | Apache-2.0 | 1100 | Steal-from | OSINT | Cybersec, CCC |
| 12 | cedrickchee/awesome-wireguard | MIT (code) / CC-BY-NC-ND (text) | 1400 | **Reject (NC poison-pill)** | — | none |
| 13 | Google Colab in VS Code | UNVERIFIED | — | UNAVAILABLE | — | — |
| 14 | algorithmicsuperintelligence/optillm | Apache-2.0 | 3800 | **Adopt** | CCC | OSINT |
| 15 | rawfilejson/awesome-osint-arsenal | NO LICENSE | 422 | **Reject (no license)** | — | none |
| 16 | zubair-trabzada/geo-seo-claude | MIT | 7200 | **Adopt** | SEO | CCC |
| 17 | betterleaks/betterleaks | MIT | 934 | **Adopt** | Cybersec | Cemini-financial (pre-IP-sale audit) |
| 18 | Tencent/AI-Infra-Guard | Apache-2.0 (with attribution) | 3700 | Steal-from | Cybersec | Image-gen |
| 19 | aarora4/Awesome-Prediction-Market-Tools | NO LICENSE | 400 | **Reject (no license)** | — | none |
| 20 | harish-garg/Awesome-Polymarket-Tools | CC0-1.0 | 80 | Reference-only | OSINT | Cemini-financial, CCC |
| 21 | YSLAB-ai/scenario-lab | UNVERIFIED | — | UNAVAILABLE | — | — |
| 22 | 1jehuang/jcode | MIT | 6100 | Steal-from | CCC | none |
| 23 | adamjgmiller/adamsreview | MIT | 188 | **Adopt** | CCC | Cemini-financial |
| 24 | edoardottt/cariddi | GPL-3.0 | 3400 | Steal-from | Cybersec | OSINT |
| 25 | eduwass/tmux-palette | UNVERIFIED | — | UNAVAILABLE | — | — |
| 26 | gtmagents/gtm-agents | Apache-2.0 | — | **Adopt** | CCC | SEO |
| 27 | opensourceprojects.dev post | UNVERIFIED | — | UNAVAILABLE | — | — |
| 28 | qarmin/czkawka | MIT (core) / GPL-3.0 (GUI) | 31000 | Steal-from | Cybersec | Image-gen |

### Cross-routing matrix

| Destination wiki | Inbound items | Highest-value |
|------------------|---------------|---------------|
| OSINT (here) | 4 entity pages + source + 2 reject-notes | Polymarket-BTC bot (direct K43 follow-up); supavec (kb-server retrieval optimization) |
| CCC | 9 items (8 stubs + 1 brief candidate) | adamsreview (Claude Code plugin template — overlaps K37); alumnium (MCP testing) |
| Cybersec | 5 items (1 deep brief + 4 stubs) | **betterleaks (pre-IP-sale codebase audit — operationally critical)** |
| Image-gen | 2 items (czkawka for LoRA dedup, AI-Infra-Guard for ComfyUI vuln) | czkawka |
| SEO | 2 items (1 deep brief + 1 stub) | geo-seo-claude (parallel-agent GEO framework, 7.2k stars; **Phase-0-pending**) |
| 3D-printing | 0 | — |

Total wiki touchpoints: ~25-28 pages across 6 wikis.

### Aggregate distribution

- **Adopt: 7** — Polymarket-BTC bot, alumnium, optillm, geo-seo-claude, betterleaks, adamsreview, gtm-agents
- **Steal-from: 7** — red-run, LAP, thuki, supavec, AI-Infra-Guard, jcode, czkawka
- **Defer: 1** — gym-anything (cmu-l3, low maturity)
- **Reference-only: 3** — 2028-GIC, awesome-wireguard (which is then sub-rejected on NC license), Awesome-Polymarket-Tools
- **Reject: 3** — chrisbanes/skills (Android), awesome-osint-arsenal (no license), Awesome-Prediction-Market-Tools (no license)
- **UNAVAILABLE: 7** — mini-browser, dll-sideloading, colab-in-vscode, scenario-lab, tmux-palette, OSS post, (+ awesome-wireguard re-bucketed)

### Doc-level vs Phase-0 — explicit gate stamped on every Adopt

**K43 lesson restated:** the K43 source-doc audit ranked 5-of-5 ADOPTs as MIT-clean; both ML/MCP candidates that progressed to Phase-0 (bukosabino/ta, tradingview-mcp) caught failure modes the doc-level eval missed. That lesson directly applies here. This source page records the **doc-level verdict** for each tool; **Phase-0 source audits are required follow-ups for every Adopt and Steal-from item before any code touches `/opt/cemini`**. See `@concepts/multi-wiki-eval-doc-level-vs-phase-0.md` for the gate definition.

Specific doc-level red flags that warrant elevated Phase-0 scrutiny on K44:

1. **Star-count inflation suspicion**. geo-seo-claude (7,200 stars), jcode (6,100 stars), czkawka (31,000 stars) — czkawka is well-established and plausible; the other two are from less-known maintainers and warrant verification via `gh api`.
2. **LLM-synthesis voice**. The eval document uses "ruthless," "catastrophic," "exceptionally," "absolute compliance" language characteristic of LLM-generated synthesis; "anti-hallucination protocols" self-claim is itself a hallucination tell. Treat all metrics as claims-pending-verification.
3. **Footnote citations** ([1]-[30]) reference unspecified sources — no bibliography. Reduces independent reproducibility.
4. **TradingView-MCP-class TOS gates**: not addressed in this eval for tools that wrap third-party services (e.g., Polymarket-BTC bot wraps Binance + Coinbase — TOS for commercial redistribution unaudited; geo-seo-claude wraps Google Search Console / Maps endpoints — same gate).

### IP-sale lens — primary verdict driver

The eval is explicit that **the impending sale of the Cemini financial suite** is the overarching constraint. Three concrete implications baked into the verdicts:

- **Copyleft (GPL-3.0, AGPL) → Steal-from at best**: red-run, cariddi, czkawka-GUI all bucketed Steal-from on this basis even where the tool is operationally desirable. The Cemini house posture from K41 (`@concepts/cemini-license-posture.md`) is preserved.
- **NC clauses → hard Reject**: awesome-wireguard's CC-BY-NC-ND on the text is treated as fatal even though the code is MIT. This is the strictest interpretation we've seen documented; consistent with Cemini's "no ambiguity in IP transfer" stance.
- **No-license → hard Reject**: three tools rejected purely on missing-LICENSE-file (awesome-osint-arsenal, Awesome-Prediction-Market-Tools); awesome-wireguard sub-rejected; citriniresearch text reference-only-not-extractable. Consistent posture.

### Most operationally critical finding: betterleaks

The eval flags `betterleaks/betterleaks` (MIT, Go, CEL-based secret scanning) with a directive that exceeds the normal Adopt verdict: **"Mandatory execution for pre-IP sale codebase auditing"**. The reasoning is that any hardcoded credentials, API keys, or DB passwords lurking in `/opt/cemini` or historical PostgreSQL dumps must be exterminated before the IP-sale transfer. This is the highest-priority single-tool follow-up from K44 — Phase-0 audit and pre-IP-sale scan job both warrant immediate scheduling.

### Most architecturally interesting finding: adamsreview

`adamjgmiller/adamsreview` (MIT, Python+Bash Claude-Code plugin) is described as a "highly sophisticated Claude Code plugin architecture dedicated to asynchronous code review" with persistent JSON state tracking via `artifact.json` and PEP 723 inline-script shebangs. This is directly relevant to the K37 reviewer-agent v2 work (Sprint 5 currently deferred). May be a usable template or convergent prior art — Phase-0 audit should compare directly against the K37 spec.

### geo-seo-claude — cross-wiki convergence finding

`zubair-trabzada/geo-seo-claude` (MIT, Python+Shell+Playwright, claimed 7,200 stars) — **already Phase-0-audited and adopted by the SEO-wiki on 2026-05-07** (`@seo-wiki/entities/tools/geo-seo-claude.md`, maturity: validated). K44 cross-wiki convergence raises the signal quality of *this specific* doc-level eval finding. The K44 metrics (7,200 stars vs SEO-wiki's ~6,700 stars / 11 open issues / 2026-04-30 last commit) are consistent with a week of continued repo activity, not inflation. No action change; cross-reference appended to the existing SEO-wiki entity page.

## Snippets

> "The evaluation is predicated on a critical overarching directive: maintaining absolute intellectual property (IP) cleanliness for the impending sale of the Cemini financial suite and its associated knowledge bases."
[Source: Tool Evaluation for Cemini Wiki Integration.docx ¶2]

> "Critically, we must Adopt this tool immediately to recursively scan the /opt/cemini algorithmic trading stack and historical PostgreSQL databases, ensuring that absolutely no hardcoded credentials or API keys breach the perimeter prior to our impending financial suite IP sale."
[Source: ibid, betterleaks reasoning ¶205-206]

> "The repository functions under a precarious dual-license model. The core mathematical algorithms (czkawka_core) are MIT-licensed and safe, but the Slint-based GUI frontends (Krokiet, Cedinia) enforce the GPL-3.0 license. Extreme prejudice and rigid build isolation must be utilized to decouple the core library from the GUI to prevent IP-sale poisoning."
[Source: ibid, czkawka license-risk ¶338]

> "OptiLLM functions as an OpenAI API-compatible proxy utilizing LiteLLM to gateway multiple LLM providers, notably supporting complex inference tasks via the Z3 theorem prover for rigid logical reasoning."
[Source: ibid, optillm reasoning ¶169]

## Dead Ends

- **UNAVAILABLE URLs are not Deferrals.** Seven URLs failed retrieval during the evaluation. The eval correctly does not synthesize from cached snippets (mini-browser had 19/6 stars per peripheral search but was marked UNAVAILABLE; same discipline applied elsewhere). For K44 ingest, these are recorded as provenance footnotes only — no entity pages created.
- **Doc-level metrics are claims, not facts.** Star counts, commit dates, and contributor counts from this eval must be independently verified (`gh api repos/<owner>/<repo>`) before any Phase-0 audit upgrade.
- **CC-BY-NC-ND on text content is a poison-pill the K41 license-posture page does not yet enumerate.** awesome-wireguard is the first instance encountered. Worth a follow-up update to `@concepts/cemini-license-posture.md` to add a "mixed-license repos" sub-section enumerating the joint-license posture (text NC + code MIT = reject the whole repo).
