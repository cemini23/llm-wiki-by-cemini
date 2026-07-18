---
title: "Revenue Opportunity URL Evaluation (2026-07-18)"
type: source
tags: [source, tool-eval, k173]
keywords: [k173, posthog, ui-skills, kimi-cli, airllm, searchos, wigolo]
related:
  - concepts/wiki-tooling-evaluation.md
  - concepts/cemini-license-posture.md
  - entities/tools/ui-skills.md
  - entities/tools/kimi-cli.md
  - entities/tools/airllm.md
  - entities/tools/searchos.md
  - entities/tools/posthog.md
  - entities/tools/ossie.md
  - entities/tools/ktransformers.md
  - entities/tools/wigolo.md
  - entities/tools/g0dm0d3.md
maturity: draft
read_status: read
created: 2026-07-18
updated: 2026-07-18
clusters: [k173-ingest]
---

## Relations

- @concepts/wiki-tooling-evaluation.md
- @concepts/cemini-license-posture.md
- @entities/tools/ui-skills.md · @entities/tools/kimi-cli.md · @entities/tools/airllm.md
- @entities/tools/searchos.md · @entities/tools/posthog.md · @entities/tools/ossie.md
- @entities/tools/ktransformers.md · @entities/tools/wigolo.md · @entities/tools/g0dm0d3.md

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Revenue Opportunity URL Evaluation |
| **Type** | Gemini tool-eval docx (v5 tiers) |
| **sha256** | `a4263db80317f7d3c9c4e82427d8e9eb02a79ab01887a0740038cbd63f48bab1` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/Revenue Opportunity URL Evaluation.docx` |
| **retrieved** | 2026-07-18 |

## Narrative

19-URL eval. **Verified licenses via `gh api` (never trust docx claims).**

| Tier | Item | Verified license | Cemini decision |
|------|------|------------------|-----------------|
| Extract | ibelick/ui-skills | MIT | TipDrop/David UI skill pack |
| Extract | MoonshotAI/kimi-cli | Apache-2.0 | CCC CLI substrate |
| Extract | lyogavin/airllm | Apache-2.0 | PM LP canary — layer-wise inference |
| Extract | kvcache-ai/ktransformers | Apache-2.0 | PM/local MoE serve patterns |
| Extract | unsloth Gemma-4 docs | Apache-2.0 base | Watch docs only — **no weight download** |
| Integrate | PostHog/posthog | MIT + ee/ proprietary split | TipDrop SaaS analytics — **no full clone** (~5.7GB) |
| Integrate→**Pass** | KnockOutEZ/wigolo | **AGPL-3.0** | Eval said Integrate; AGPL blocks TipDrop/XSP SaaS embed |
| Integrate→**Watch** | elder-plinius/G0DM0D3 | **AGPL-3.0** (eval claimed MIT) | Jailbreak/prompt research only |
| Watch | apache/ossie | Apache-2.0 | CCC OSS intelligence |
| Watch | paste.trade | NOT FOUND | XSP flow UI — license TBD |
| Watch | Kimi K3 blog / weights | N/A | No weight download (<500MB gate) |
| Pass | bat / mu-repo / thefuck / eza | various | Already-covered CLI niceties |
| Context | build-your-own-x / tailspin / macos27 | CC0/MIT | Learning refs |

SearchOS (arxiv 2607.15257) handled as separate arXiv source + entity.
