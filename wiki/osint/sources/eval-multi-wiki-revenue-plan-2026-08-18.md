---
title: "Eval — Multi-Wiki Revenue Plan 2026-08-18 (20-URL, K241)"
type: source
tags: [eval, phase-0, k241, atto, ccc, cyber]
keywords: [google-sam, llm-as-a-verifier, diagram-design, bbot, OSINT4ALL, AGPL]
related:
  - entities/tools/google-sam.md
  - entities/tools/llm-as-a-verifier.md
  - entities/tools/diagram-design.md
  - entities/tools/bbot.md
  - entities/tools/osint4all.md
  - concepts/sovereign-agent-mesh-biscuit.md
  - concepts/cemini-license-posture.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/atto-genealogy-agent-kit.md
  - concepts/skill-misevolution.md
  - sources/eval-multi-wiki-url-revenue-2026-08-18.md
  - sources/osint4all-startme-2026-08-18.md
maturity: draft
created: 2026-08-18
updated: 2026-08-18
read_status: read
---

## Relations

- @entities/tools/google-sam.md — Apache-2.0 Extract (Sovereign Agent Mesh)
- @entities/tools/llm-as-a-verifier.md — MIT Extract (self-verification)
- @entities/tools/diagram-design.md — MIT Extract + HITL skill-vetting (docx Integrate overridden)
- @entities/tools/bbot.md — **AGPL-3.0** Extract-only (docx said GPL — wrong)
- @entities/tools/osint4all.md — catalog hub; no stub farm
- @concepts/sovereign-agent-mesh-biscuit.md — libp2p MCP sidecar + Biscuit tokens
- @concepts/cemini-license-posture.md — never trust eval SPDX
- @concepts/wiki-tooling-evaluation.md
- @concepts/atto-genealogy-agent-kit.md — SAM biscuit scopes + PII-safe verifier
- @concepts/skill-misevolution.md — do not silent-copy diagram-design into `~/.cursor/skills`
- @sources/eval-multi-wiki-url-revenue-2026-08-18.md — same-day K241 URL eval
- @sources/osint4all-startme-2026-08-18.md — OSINT4ALL Context → catalog hub

## Raw Concept

| Field | Value |
|-------|--------|
| File | `Multi-Wiki Revenue Evaluation Plan.docx` |
| sha256 | `5d166291ce416229dd668d1863ccd884878f9ee818b0a4cae76c01c8b23f5b35` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/Multi-Wiki Revenue Evaluation Plan.docx` |
| retrieved | 2026-08-18 |
| URLs evaluated | 20 |
| Theme | GitHub / C2 / OSINT / agent-mesh / diagram skill |
| License report | `.local/reports/license-k241-2026-08-18.md` |
| Dual-ID | **OSINT K241** = this inbox (18 Aug 2026). Resolve by file+wiki, not bare K#. |

## Narrative

20-URL multi-wiki revenue-plan evaluation. **Docx license claims were never trusted.** **0 new runtime Integrate GO** after `gh api` SPDX. Docx Integrate on `cathrynlavery/diagram-design` is overridden to **Extract + HITL skill-vetting** (misevolution; no silent `~/.cursor/skills` copy). CyberChef Integrate attempt lives on the same-day URL eval and is also overridden (already K149 Context).

### Verdict aggregate (license-corrected)

| Tier | Count | URLs |
|------|-------|------|
| Integrate (new GO) | **0** | diagram-design Integrate overridden |
| Extract clone | 3 | **google/sam** Apache-2.0; **llm-as-a-verifier** MIT; **diagram-design** MIT (HITL) |
| Extract-only clone (AGPL) | 1 | **bbot** AGPL-3.0 — isolate; no Atto vendor |
| Already Context (do not re-tier) | 1 | CyberChef (K149; URL eval) |
| Watch NOASSERTION no-clone | 3 | PageLM; multica; DeepSeek-V4-J-Space |
| Watch AGPL no-clone | 1 | ssh-ai-chat |
| Keep prior NOASSERTION | 1 | usertour (K240) |
| Context no-clone | 6 | PrivFu (BSD-3 PoC); QUIC C2 article; movfuscator; plugandpwn; HTB (null SPDX); OSINT4ALL (hub, not farm) |
| Context archived | 1 | codex-plusplus (MIT, archived Electron) |
| SIZE-SKIP | 1 | traceway MIT ~514MB |
| Pass | 2 | rakazo (Apache-2.0, portfolio SaaS miss); liquid.trade |

### License re-verification (gh api)

| Repo / URL | Docx claim | gh SPDX | Size | Action |
|------------|-----------|---------|------|--------|
| google/sam | Apache-2.0 / Extract | **Apache-2.0** | ~34MB API / 44MB clone | **CLONE Extract** |
| llm-as-a-verifier/llm-as-a-verifier | MIT / Extract | **MIT** | ~67MB API / **411MB** clone | **CLONE Extract** (under 500MB) |
| cathrynlavery/diagram-design | OSS / **Integrate** | **MIT** | ~6–11MB | **CLONE Extract + HITL** |
| blacklanternsecurity/bbot | GPL-3.0 / Extract | **AGPL-3.0** | ~16MB clone | **CLONE Extract-only**. Docx GPL **wrong** |
| CaviraOSS/PageLM | OSS / Watch | **NOASSERTION** | 29MB | **no clone** |
| multica-ai/multica | Apache-2.0 / Watch | **NOASSERTION** | 121MB | **no clone** |
| miantiao-me/ssh-ai-chat | MIT / Watch | **AGPL-3.0** | 0.3MB | **no clone** — Watch |
| b-nnett/codex-plusplus | MIT / Context | MIT archived | 89MB | Context; no clone |
| Tiger3807861189/DeepSeek-V4-J-Space… | NOT FOUND / Context | **NOASSERTION** | 91KB | Context; no clone |
| elie222/rakazo | MIT / Pass | **Apache-2.0** | 11MB | Pass |
| daem0nc0re/PrivFu | NOT FOUND / Extract | **BSD-3-Clause** | 16MB | **Context — no clone** (token-steal PoC) |
| xoreaxeaxeax/movfuscator | BSD / Context | **NOASSERTION** | 12MB | Context; no clone |
| usertour/usertour | (K240) | **NOASSERTION** | 30MB | keep K240; no clone |
| tracewayapp/traceway | AGPL / Pass | **MIT** | **514MB** | SIZE-SKIP |
| Fr6ey/HackTheBox-All-Cheatsheets | OSS / Extract | **null SPDX** | 14MB | Context; no payloads |
| AccentuSoft/LinkScope_Client | n/a | **AGPL-3.0** | 3MB | catalog Context; no clone |
| OSINT4ALL start.me | n/a / Context | n/a | n/a | **catalog hub** |
| liquid.trade | proprietary / Pass | n/a | n/a | Pass |
| QUIC C2 article / plugandpwn | n/a / Context | n/a | n/a | Context; no PoC |

**Pattern:** bbot GPL → **AGPL-3.0**; diagram-design Integrate → Extract + HITL; PageLM/multica claimed OSS/Apache → NOASSERTION; ssh-ai-chat MIT → AGPL. Same "never trust eval SPDX" as K231/K237/K239/K240.

### Phase-0 clone log (this eval)

| Repo | Verdict | Clone? | Size |
|------|---------|--------|------|
| google/sam | Apache-2.0 Extract | HAVE (44MB) | 44MB |
| llm-as-a-verifier | MIT Extract | ✓ NEW | 411MB |
| diagram-design | MIT Extract + HITL | HAVE | 11MB |
| bbot | AGPL-3.0 Extract-only | HAVE | 16MB |

### Pass / Context / Rejects (folded here — no reject-stub farm)

- **Pass:** rakazo (portfolio SaaS miss); liquid.trade.
- **Context:** PrivFu / QUIC C2 / plugandpwn / movfuscator / HTB / LinkScope / OSINT4ALL / DeepSeek-V4-J-Space / codex-plusplus. Offensive rows are **awareness only** — no PoC, no implant writeup, no cheatsheet payloads.
- **NO-GO clone:** PageLM, multica, usertour (NOASSERTION); ssh-ai-chat (AGPL Watch); traceway SIZE-SKIP.
- **Do not vendor AGPL** (`bbot`, `ssh-ai-chat`, LinkScope) into proprietary Atto kits.

### Routing notes

- **Atto (#1):** SAM biscuit least-privilege scopes + llm-as-a-verifier claim-ledger pattern + diagram-design HITL visuals. **No Barone PII** in fixtures. Do not silent-install the diagram skill.
- **CCC:** ClawGym / HarnessEval / cursor-route live on other K241 sources; this eval does not swap `/route`.
- **Cyber:** bbot Extract-only on **authorized targets**. PrivFu/HTB/C2 Context-no-PoC.
- **xsp/pm:** none from this eval.

## Snippets

> bbot: claimed GPL-3.0 Extract → **AGPL-3.0**. diagram-design: claimed Integrate → **Extract + HITL skill-vetting**. [Source: `.local/reports/license-k241-2026-08-18.md`]

> 0 new runtime Integrate GO. [Source: `.local/reports/license-k241-2026-08-18.md`]
