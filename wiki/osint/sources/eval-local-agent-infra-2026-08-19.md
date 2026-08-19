---
title: "Eval — Local agent infra URL 2026-08-19 (20-URL, K242)"
type: source
tags: [eval, phase-0, k242, atto, cyber, ccc]
keywords: [mdflux, easy-agent, bloodbash, vphone-cli, cua, omlx]
related:
  - entities/tools/mdflux.md
  - entities/tools/easy-agent.md
  - entities/tools/bloodbash.md
  - entities/tools/vphone-cli.md
  - entities/tools/ai-memory.md
  - entities/tools/omlx.md
  - sources/eval-project-revenue-url-2026-08-19.md
  - concepts/cemini-license-posture.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/atto-genealogy-agent-kit.md
  - concepts/local-abliterated-llm-pentest-stack.md
  - concepts/agent-harness-verification-bottleneck.md
maturity: draft
created: 2026-08-19
updated: 2026-08-19
read_status: read
---

## Relations

- @entities/tools/mdflux.md — MIT Extract Atto local OCR wrapper; Transkribus sole HTR
- @entities/tools/easy-agent.md — MIT Extract 5-layer harness
- @entities/tools/bloodbash.md — MIT Extract-only authorized AD JSON
- @entities/tools/vphone-cli.md — MIT Extract REFERENCE; no jailbreak writeup
- @entities/tools/ai-memory.md — MIT Extract; reconstruct-before-inject
- @entities/tools/omlx.md — Apache-2.0 already K182 `wont_wire`; K242 bump, skip clone
- @sources/eval-project-revenue-url-2026-08-19.md — same-day K242 Project Revenue eval
- @concepts/cemini-license-posture.md
- @concepts/wiki-tooling-evaluation.md
- @concepts/atto-genealogy-agent-kit.md
- @concepts/local-abliterated-llm-pentest-stack.md
- @concepts/agent-harness-verification-bottleneck.md — Dual-ID OSINT K242 ≠ Trajectory Sentinel K242

## Raw Concept

| Field | Value |
|-------|--------|
| File | `Untitled document.docx` |
| sha256 | `71ef013622ef8b14ef8d9c98196651ed4875faf105310e8c80c928dd51ef27df` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/Untitled document.docx` |
| retrieved | 2026-08-19 |
| URLs evaluated | 20 |
| Theme | Local agent infra, offline cyber, digitization, OS automation |
| License report | `.local/reports/license-k242-2026-08-19.md` |
| Dual-ID | **OSINT K242** = this inbox (19 Aug 2026). |

## Narrative

20-URL local-infra evaluation. **0 new runtime Integrate GO.** Docx Integrate on BloodBash and cua is overridden (Extract-only / SIZE-SKIP). Transkribus remains sole product HTR — mdflux is a RapidOCR wrapper, not a replacement.

### Verdict aggregate (license-corrected)

| Tier | Count | URLs |
|------|-------|------|
| Integrate (new GO) | **0** | BloodBash / cua Integrate overridden |
| Extract clone | 5 | **mdflux**; **easy-agent**; **vphone-cli**; **ai-memory**; **BloodBash** (Extract-only) |
| Already wiki skip-clone | 1 | **omlx** K182 `wont_wire` |
| Watch / SIZE-SKIP | 2 | cua MIT ~313MB (+ optional AGPL omni); treg NOASSERTION |
| Context no-clone | 8 | WireTapper; H.I.V.E; botdirectory; text-to-cad; unbound-dashboard; Google style; herdrm DRM; repowise AGPL; J-Space; munder-difflin |
| Pass | 2 | EasyCopy; elasticsearch (ELv2/SSPL SIZE-SKIP) |

### License re-verification (gh api)

| Repo | Docx claim | gh SPDX | Action |
|------|-----------|---------|--------|
| ibrahimqureshae/mdflux | MIT / Extract | **MIT** | **CLONE Extract** (~38MB) |
| ConardLi/easy-agent | MIT / Extract | **MIT** | **CLONE Extract** (~4.7MB) |
| SquidSec/BloodBash | MIT / **Integrate** | **MIT** | **CLONE Extract-only** (~104MB). Authorized SharpHound JSON only. No PoC. |
| Lakr233/vphone-cli | Extract | **MIT** | **CLONE Extract REFERENCE** (~5.9MB). No AMFI/jailbreak writeup. |
| akitaonrails/ai-memory | Extract | **MIT** | **CLONE Extract** (~18MB) |
| trycua/cua | MIT / **Integrate** | **MIT** | SIZE-SKIP ~313MB; AGPL omni isolate |
| jundot/omlx | Extract | **Apache-2.0** | Skip clone; keep `wont_wire` |
| superdesigndev/treg | Extract | **NOASSERTION** | Watch, no clone |
| elastic/elasticsearch | Pass | ELv2/SSPL | SIZE-SKIP |

[Source: `.local/reports/license-k242-2026-08-19.md`]
