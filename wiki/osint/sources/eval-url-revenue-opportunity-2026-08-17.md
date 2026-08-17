---
title: "Eval — URL Revenue Opportunity 2026-08-17 (20-URL, K240)"
type: source
tags: [eval, phase-0, k240, atto, ccc, cyber]
keywords: [filekey, memvid, usertour, corsair, aiwg, unsloth, qwen-abliterated, claude-cookbooks]
related:
  - entities/tools/filekey.md
  - entities/tools/memvid.md
  - entities/tools/addyosmani-agent-skills.md
  - entities/tools/pi-earendil.md
  - concepts/cemini-license-posture.md
  - concepts/atto-genealogy-agent-kit.md
  - sources/eval-github-repository-stack-2026-08-16.md
  - sources/arxiv-2608.14392-tripwire-2026-08-17.md
  - sources/newsletter-rss-latent-space-2026-08-14-ainews-cursors-60b.md
maturity: draft
created: 2026-08-17
updated: 2026-08-17
read_status: read
---

## Relations

- @entities/tools/filekey.md — GPL-3.0 Extract-only (docx NOT FOUND was wrong)
- @entities/tools/memvid.md — already K219 Integrate; do not re-tier
- @entities/tools/addyosmani-agent-skills.md — already K223 Integrate; related only
- @entities/tools/pi-earendil.md — already K228 Integrate; related only
- @concepts/cemini-license-posture.md
- @concepts/atto-genealogy-agent-kit.md — filekey pattern; Transkribus remains sole HTR
- @sources/eval-github-repository-stack-2026-08-16.md — same-day K240 GitHub eval
- @sources/arxiv-2608.14392-tripwire-2026-08-17.md — Qwen abliterated Watch pairs Tripwire HITL

## Raw Concept

| Field | Value |
|-------|--------|
| File | `URL Revenue Opportunity Evaluation.docx` |
| sha256 | `8b718b3f0071fb37dc9d9e9104d6e98f0f7aff6289addf122efbbaced1862373` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/URL Revenue Opportunity Evaluation.docx` |
| retrieved | 2026-08-17 |
| URLs evaluated | 20 |
| Theme | Agent onboarding, memory, lab weights, cost/cache, credential isolation |
| License report | `.local/reports/license-k240-2026-08-17.md` |
| Dual-ID | **OSINT K240** = this inbox. **CCC K240** = robotics MCP solver (old). Resolve by file+wiki. |

## Narrative

20-URL revenue-opportunity evaluation. **Docx license claims were never trusted.** **0 new Integrate GO** after gh SPDX. Docx listed four Integrates (Qwen GGUF, aiwg, claude-cookbooks, corsair). All overridden: weights skip, K239 Context hold, size/pattern-only, NOASSERTION no-clone.

### Verdict aggregate (license-corrected)

| Tier | Count | URLs |
|------|-------|------|
| Integrate (new GO) | **0** | Four docx Integrates overridden |
| Extract-only (GPL) | 1 | **filekey** (GPL-3.0 ✓) — pattern REFERENCE; no Atto vendor |
| Already Integrate (do not re-tier) | 3 | memvid (K219), addyosmani/agent-skills (K223), earendil-works/pi (K228) |
| Keep Context | 1 | jmagly/aiwg (MIT ✓, K239) |
| Size-hold | 1 | daily_stock_analysis (MIT ✓, K231 ~100MB) |
| Size-skip | 2 | claude-cookbooks (MIT, 210MB — notebook pattern only); traceway (MIT, **511MB**) |
| Skip weights | 2 | Qwen3.8-27B-ABLITERATED-GGUF; Qwen3.8-27B-Uncensored-FP8 |
| Skip HTR | 1 | unsloth (Apache-2.0 ✓, 199MB) — Transkribus remains sole Atto HTR |
| NOASSERTION no-clone | 2 | usertour, corsair |
| Null SPDX no-clone | 1 | HackTheBox-All-Cheatsheets |
| Watch no-clone (budget) | 1 | paperclip (MIT, 190MB) |
| Context | 3 | rete, dune query 8354772, ultramock.io, dreamcut.ai |
| Pass | 1 | vercel.com |

(Context row counts SaaS/SQL with the three listed plus dreamcut.)

### License re-verification (gh api)

| Repo / URL | Docx claim | gh api SPDX | Size | Action |
|------------|-----------|-------------|------|--------|
| RockwellShah/filekey | NOT FOUND / Extract | **GPL-3.0** | <1MB | cloned 1.2MB Extract-only |
| usertour/usertour | MIT CE / Extract | **NOASSERTION** | 29MB | **no clone** |
| corsairdev/corsair | Open Source / **Integrate** | **NOASSERTION** | 52MB | **no clone** |
| memvid/memvid | NOT FOUND / Extract | Apache-2.0 | 29MB | already K219 |
| jmagly/aiwg | MIT / **Integrate** | MIT | 81MB | **keep K239 Context** |
| anthropics/claude-cookbooks | MIT/Apache / **Integrate** | MIT | 210MB | Extract **notebook pattern only** — no full clone |
| unslothai/unsloth | Apache-2.0 / Extract | Apache-2.0 | 199MB | skip; Transkribus sole HTR |
| ZhuLinsen/daily_stock_analysis | Apache/MIT / Extract | **MIT** | 100MB | K231 size-hold |
| addyosmani/agent-skills | MIT / Extract | MIT | <1MB | already K223 |
| earendil-works/pi | NOT FOUND / Pass | MIT | — | already K228 |
| paperclipai/paperclip | MIT / Watch | MIT | 190MB | Watch; no clone this batch |
| tracewayapp/traceway | OSS claimed / Watch | MIT | **511MB** | SIZE-SKIP |
| Fr6ey/HackTheBox-All-Cheatsheets | NOT FOUND / Extract | **null** | — | Context; **no clone**, no payloads |
| Blackfrost-AI/Qwen3.8-27B-ABLITERATED-GGUF | Community / **Integrate** | HF weights | huge | **Watch, no download** |
| orcarouter/Qwen3.8-27B-Uncensored-FP8 | Apache/Qwen / Watch | HF weights | huge | **Watch, no download** |
| retejs/rete | MIT / Context | MIT | — | Context |
| dune.com/queries/8354772 | public SQL / Context | n/a | n/a | Context |
| ultramock.io | proprietary / Context | n/a | n/a | Context (SEO/image-gen) |
| vercel.com | proprietary / Pass | n/a | n/a | Pass |
| dreamcut.ai | proprietary SaaS / Context | n/a | n/a | Context |

**Pattern:** usertour MIT → NOASSERTION; corsair Integrate/OSS → NOASSERTION; filekey NOT FOUND → **GPL-3.0**; Qwen GGUF Integrate → weights skip; aiwg Integrate → keep Context. Same "never trust eval SPDX" as K231/K237/K239.

### Phase-0 clone log (this eval)

| Repo | Verdict | Clone? | Size |
|------|---------|--------|------|
| filekey | GPL-3.0 Extract-only | ✓ NEW | 1.2MB |
| memvid / agent-skills / pi | already adopted | skip re-tier | — |
| usertour / corsair | NOASSERTION | skip | — |
| Qwen GGUF / FP8 | Watch | **no weights** | — |
| claude-cookbooks | pattern only | no full clone | — |
| unsloth / daily_stock / traceway / paperclip | skip / hold | no | — |

### Pass / Context / Rejects (folded here — no reject-stub farm)

- **Pass:** vercel.com (generic edge host; cemini-prod already containerized).
- **Context:** rete (node editor), ultramock (3D mockup SaaS), dreamcut.ai (SEO/image-gen), Dune query 8354772 (public SQL), HTB cheatsheets (null SPDX — authorized-lab intel only, **no payloads in wiki**), paperclip (Watch, budget).
- **NO-GO clone:** usertour, corsair (NOASSERTION).
- **Do not re-tier:** memvid, addyosmani-agent-skills, pi-earendil, aiwg, daily_stock.

### Routing notes

- **Atto (#1):** filekey = passkey/WebAuthn credential-isolation **pattern**. **Do not vendor GPL-3.0** into proprietary Atto kits. unsloth skip (Transkribus sole HTR). claude-cookbooks = prompt-cache notebook pattern only (no 210MB clone).
- **Cyber / local-abliterated lab:** Qwen 27B abliterated GGUF + Uncensored FP8 = **Watch, no weight download**. HTB cheatsheets Context only.
- **CCC:** do not replace `claude-ds`. Skills library already K223.
- **xsp/pm:** none from this eval.

## Snippets

> filekey: claimed NOT FOUND Extract → **GPL-3.0**. usertour: claimed MIT → **NOASSERTION**. corsair: claimed Integrate/OSS → **NOASSERTION**. [Source: `.local/reports/license-k240-2026-08-17.md`]

> Qwen3.8-27B-ABLITERATED-GGUF: claimed Integrate → **weights skip**. [Source: `.local/reports/license-k240-2026-08-17.md`]
