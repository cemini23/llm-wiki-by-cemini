---
title: "Eval — GitHub Repository Stack 2026-08-16 (20-URL dsh/RPC, K240)"
type: source
tags: [eval, phase-0, k240, ccc, cyber, dsh]
keywords: [dshackle, dsh-vision-toolkit, dsh-agent-teams, deepseek-harness, filekey-not-this-eval, dual-id]
related:
  - entities/tools/dshackle.md
  - entities/tools/dsh-vision-toolkit.md
  - concepts/cemini-license-posture.md
  - concepts/llm-routing-deepseek-openrouter-failover.md
  - sources/eval-url-revenue-opportunity-2026-08-17.md
maturity: draft
created: 2026-08-17
updated: 2026-08-17
read_status: read
---

## Relations

- @entities/tools/dshackle.md — Apache-2.0 GO Extract REFERENCE (not prod RPC)
- @entities/tools/dsh-vision-toolkit.md — MIT GO Extract; do not replace PATH `claude-ds`
- @concepts/cemini-license-posture.md — gh SPDX overrides docx
- @concepts/llm-routing-deepseek-openrouter-failover.md — official dsh stays behind `claude-ds`
- @sources/eval-url-revenue-opportunity-2026-08-17.md — same-day K240 URL eval

## Raw Concept

| Field | Value |
|-------|--------|
| File | `GitHub Repository Stack Evaluation.docx` |
| sha256 | `19c68331f67526b1e7deef62f1e938b2dada098eeaa59fb4109f14a1cc73f2d5` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/GitHub Repository Stack Evaluation.docx` |
| retrieved | 2026-08-16 |
| URLs evaluated | 20 |
| Theme | DeepSeek Harness ecosystem, blockchain RPC load balancing, network forensics |
| License report | `.local/reports/license-k240-2026-08-17.md` |
| Dual-ID | **OSINT K240** = this inbox (17 Aug 2026). **CCC K240** = MixedComplementarityProblems.jl robotics solver (old). Resolve by file+wiki, not bare K#. |

## Narrative

20-URL GitHub-stack evaluation. **Docx license claims were never trusted.** Every Extract/Integrate verdict re-verified via `gh api repos/{owner}/{repo}` (SPDX + size). **0 new Integrate GO.** `emeraldpay/dshackle` was the only docx Integrate with a matching SPDX — it is **Extract REFERENCE**, not a cemini-prod RPC deploy.

### Verdict aggregate (license-corrected)

| Tier | Count | URLs |
|------|-------|------|
| Integrate (new GO) | **0** | Docx listed dshackle Integrate; overridden to Extract REFERENCE |
| Extract | 2 | **dshackle** (Apache-2.0 ✓), **dsh-vision-toolkit** (MIT ✓) |
| Watch / clone REFERENCE | 1 | **dsh-agent-teams** (MIT ✓) |
| Extract-blocked | 2 | dsh-anchored-standard (**NOASSERTION**); dsh-routing-suite (**null SPDX**) |
| Context | 6 | awesome-dsh-plugin, awesome-deepseek-harness, dsh-web-ui, dsh-market, DShield (GPL-2.0 isolate), Dshell (NOASSERTION, stale 2019) |
| Pass | 8 | DSharpPlus, dsh-desktop, DShotRMT, helloagents, dsh-deep-whale, dsh_desktop, DSH_tensorflow, working-activity |
| Do-not-replace | 1 | anywhere-labs/deepseek-harness-desktop (MIT) — **not** a `claude-ds` swap |

### License re-verification (gh api)

| Repo | Docx claim | gh api SPDX | Size | Action |
|------|-----------|-------------|------|--------|
| emeraldpay/dshackle | Apache-2.0 / **Integrate** | Apache-2.0 | 8MB | cloned REFERENCE 5.6MB; **not** prod |
| Anionex/dsh-vision-toolkit | CLAIMED unverified / Extract | **MIT** | 9MB | cloned 17MB Extract |
| NanmiCoder/dsh-agent-teams | NOT FOUND / Watch | **MIT** | 8MB | cloned 3.5MB Watch REFERENCE |
| xiaobright/dsh-anchored-standard | CLAIMED unverified / Extract | **NOASSERTION** | <1MB | **no clone** |
| yjh051108/dsh-routing-suite | NOT FOUND / Watch | **null** | — | **no clone** |
| anywhere-labs/deepseek-harness-desktop | CLAIMED unverified / Context | MIT | — | Context; do not replace `claude-ds` |
| 0xsline/awesome-deepseek-harness | CC0 / Context | CC0-1.0 | — | Context catalog |
| awesome-dsh-plugin/awesome-dsh-plugin | CC0 / Context | CC0-1.0 | — | Context catalog |
| zhu1090093659/dsh-web-ui | Apache-2.0 / Context | Apache-2.0 | — | Context |
| dsh-market/dsh-market | MIT / Context | MIT | — | Context |
| DShield-ISC/dshield | GPL-2.0 / Context | **GPL-2.0** | — | Context; GPL isolate |
| USArmyResearchLab/Dshell | US Gov PD / Context | **NOASSERTION** | stale 2019 | Context; no clone |
| DSharpPlus/DSharpPlus | NOT FOUND / Pass | MIT | — | Pass (.NET Discord — stack miss) |
| dataelement/dsh-desktop | NOT FOUND / Pass | MIT | — | Pass (Electron wrapper) |
| derdoktor667/DShotRMT | NOT FOUND / Pass | MIT | — | Pass (ESP32 DShot — OOD) |
| hellowind777/helloagents | NOT FOUND / Pass | **NOASSERTION** | — | Pass |
| Small-tailqwq/dsh-deep-whale | NOT FOUND / Pass | **null** | — | Pass |
| myYangyunfan/dsh_desktop | NOT FOUND / Pass | MIT | — | Pass |
| yg33717/DSH_tensorflow | NOT FOUND / Pass | **null** | — | Pass (name collision) |
| ccch1mneyyy/working-activity | MIT / Pass | MIT | — | Pass |

**Pattern:** docx invented Integrate on an RPC proxy that Cemini must not auto-deploy, and left MIT unverified on the two useful dsh Extract repos. Reproduces K53/K54/K231/K237/K239 "never trust eval SPDX."

### Phase-0 clone log (this eval)

| Repo | Verdict | Clone? | Size |
|------|---------|--------|------|
| dshackle | GO Extract REFERENCE | ✓ NEW | 5.6MB |
| dsh-vision-toolkit | GO Extract | ✓ NEW | 17MB |
| dsh-agent-teams | Watch REFERENCE | ✓ NEW | 3.5MB |
| dsh-anchored-standard / dsh-routing-suite | null / NOASSERTION | skip | — |
| Dshell / DShield | Context | skip (stale / GPL isolate) | — |

### Pass / Context aggregate (no reject-stub farm)

- **Pass:** DSharpPlus (.NET Discord — GuruWatcher is Python webhooks), dsh-desktop / dsh_desktop (Electron wrappers around dsh — do not replace PATH `claude-ds`), DShotRMT (ESP32 motor protocol — OOD), helloagents / dsh-deep-whale / DSH_tensorflow / working-activity (name-collision or no stack hook).
- **Context:** awesome-dsh-plugin + awesome-deepseek-harness (catalogs; third-party plugins execute arbitrary install code), dsh-web-ui (operator UX, not a steal), dsh-market (marketplace), DShield (GPL-2.0 isolate), Dshell (NOASSERTION, last push 2019).
- **Do-not-replace:** any dsh-desktop / awesome-dsh fork. Official DeepSeek Harness stays behind PATH `claude-ds`.

### Routing notes

- **CCC:** dsh-vision-toolkit + dsh-agent-teams = Extract for the dsh ecosystem. Do **not** swap `/route` mid.
- **Cyber:** DShield/Dshell stay Context. No GPL vendor into Atto kits.
- **Prod:** dshackle is a PM/RPC **pattern** only. HITL before any cemini-prod proxy. **Not** a default deploy.
- **Atto / GuruWatcher / xsp / pm:** none from this eval.

## Snippets

> Batch theme: DeepSeek Harness ecosystem, blockchain RPC load balancing, network forensics, threat intelligence, and multimodal agent tooling. [Source: GitHub Repository Stack Evaluation.docx]

> Docx Integrate list starts with dshackle — license+ops override leaves **zero** new Integrate GO. [Source: `.local/reports/license-k240-2026-08-17.md`]
