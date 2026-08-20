---
title: "Eval — Multi-Repo Revenue 2026-08-20 (20-URL, OSINT K243)"
type: source
tags: [eval, phase-0, k243, atto, cyber, ccc]
keywords: [whisperlivekit, legal-templates, openbot, dnsglobe, nullframe, purple]
related:
  - entities/tools/whisperlivekit.md
  - entities/tools/legal-templates.md
  - entities/tools/openbot.md
  - entities/tools/dnsglobe.md
  - entities/tools/nullframe.md
  - sources/eval-repository-revenue-2026-08-20.md
  - concepts/cemini-license-posture.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/atto-genealogy-agent-kit.md
  - concepts/local-abliterated-llm-pentest-stack.md
  - concepts/agent-harness-verification-bottleneck.md
  - sources/arxiv-2608.19197-spade-2026-08-20.md
maturity: draft
created: 2026-08-20
updated: 2026-08-20
read_status: read
---

## Relations

- @entities/tools/whisperlivekit.md — Apache-2.0 Extract STT; not Transkribus HTR
- @entities/tools/legal-templates.md — CC0-1.0 Extract; HITL lawyer review
- @entities/tools/openbot.md — MIT Extract CEL pre-action; no CopilotKit cloud
- @entities/tools/dnsglobe.md — MIT Extract
- @entities/tools/nullframe.md — MIT Extract
- @sources/eval-repository-revenue-2026-08-20.md — same-day OSINT K243 eval
- @concepts/cemini-license-posture.md — never trust eval SPDX
- @concepts/wiki-tooling-evaluation.md
- @concepts/atto-genealogy-agent-kit.md — Whisper STT + legal-templates HITL
- @concepts/local-abliterated-llm-pentest-stack.md — openbot CEL; AGPL/GPL no vendor
- @concepts/agent-harness-verification-bottleneck.md — Dual-ID: this ingest is **OSINT K243**, not ACEM / CCC K243

## Raw Concept

| Field | Value |
|-------|--------|
| File | `Multi-Repo Revenue Opportunity Analysis.docx` |
| sha256 | `204749322f25ee73c1c8355907ca0f313e84eb4539e7081b2d9ada9cbe882da3` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/Multi-Repo Revenue Opportunity Analysis.docx` |
| retrieved | 2026-08-20 |
| URLs evaluated | 20 |
| Theme | STT, legal templates, CEL agents, DNS/infra, MCP, AGPL/GPL traps |
| License report | `.local/reports/license-k243-2026-08-20.md` |
| Dual-ID | **OSINT K243** = this inbox (20 Aug 2026). Do not collapse onto ACEM / CCC K243. |

## Narrative

20-URL multi-wiki revenue evaluation. **Docx license claims were never trusted.** **0 new runtime Integrate GO** after `gh api` SPDX. Docx **Integrate** on `erickochen/purple` is overridden to Extract/Watch HITL — MCP-to-prod-SSH stays HOLD. Pass/Context/Rejects fold onto this page (no reject-stub farm).

### Verdict aggregate (license-corrected)

| Tier | Count | URLs |
|------|-------|------|
| Integrate (new GO) | **0** | purple Integrate overridden |
| Extract clone | 5 | **WhisperLiveKit** Apache-2.0; **legal-templates** CC0-1.0; **openbot** MIT; **dnsglobe** MIT; **nullframe** MIT |
| Extract-only, no clone | 2 | **dory** GPL-3.0; **picosnitch** GPL-3.0 |
| Watch no-clone | 5 | purple MIT HITL; MemMachine Apache Watch skip; OpenOutreach NOASSERTION; openwolf AGPL; Router.com non-git |
| SIZE-SKIP | 1 | vstorm-co/full-stack-ai-agent-template MIT ~255MB + Stripe HITL |
| Context no-clone | 6 | cap-table MIT; druk MIT; social-auto-upload MIT; dgit MIT; taffy MIT; Clone-Wars AGPL |
| Pass | 1 | FluxER GPL-3.0 |

### License re-verification (gh api)

| Repo / URL | Docx tier | gh SPDX | Action |
|------------|-----------|---------|--------|
| QuentinFuxa/WhisperLiveKit | Extract | **Apache-2.0** | **CLONE Extract** (~43MB). Oral-history STT ≠ Transkribus HTR. No Barone audio in git. |
| General-Legal/legal-templates | Extract | **CC0-1.0** | **CLONE Extract** (~0.6MB). HITL lawyer review before any Atto ToS ship. |
| CopilotKit/openbot | Extract | **MIT** | **CLONE Extract** (~1MB). CEL pre-action; no CopilotKit cloud. |
| 514-labs/dnsglobe | Extract | **MIT** | **CLONE Extract** (~10MB) |
| m1ckc3s/nullframe | Extract | **MIT** | **CLONE Extract** (~60KB) |
| erickochen/purple | **Integrate** | **MIT** | **Override → Extract/Watch.** MCP to prod SSH is HITL HOLD. No runtime Integrate GO. |
| eracle/OpenOutreach | Extract | **NOASSERTION** | **no clone** |
| Augani/dory | Extract | **GPL-3.0** | Extract-only, no clone |
| elesiuta/picosnitch | Extract | **GPL-3.0** | Extract-only, no clone |
| cytostack/openwolf | Extract | **AGPL-3.0** | AGPL Watch, no clone |
| GorvGoyl/Clone-Wars | Context | **AGPL-3.0** | AGPL no clone |
| vstorm-co/full-stack-ai-agent-template | Extract | **MIT** | **SIZE-SKIP** (~255MB) + Stripe HITL |
| MemMachine/MemMachine | Watch | **Apache-2.0** | Watch, skip clone (~35MB) |
| 0n1cOn3/FluxER | Pass | **GPL-3.0** | Pass |
| 1984vc/cap-table | Context | **MIT** | Context, no clone |
| letstri/druk | Context | **MIT** | Context, no clone |
| dreammis/social-auto-upload | Context | **MIT** | Context, no clone |
| littledivy/dgit | Context | **MIT** | Context, no clone |
| DioxusLabs/taffy | Context | **MIT** | Context, no clone |
| Router.com | Watch | n/a | Watch (non-git) |

[Source: `.local/reports/license-k243-2026-08-20.md`]

**Concrete steal `[TENTATIVE]`:** WhisperLiveKit is streaming speech-to-text for oral-history capture, not handwriting recognition. Atto keeps Transkribus as sole product HTR; any STT path stays local and never stores family audio in git.

## Snippets

> Never trust eval docx SPDX. Source: `gh api repos/:owner/:repo --jq .license.spdx_id`. Dual-ID: **OSINT K243** = this inbox. [Source: `.local/reports/license-k243-2026-08-20.md`]
