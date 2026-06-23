---
title: "links.docx — Multi-wiki tool evaluation (146 URLs, 2026-06-22)"
type: source
tags: [tool-evaluation, license-compliance, multi-wiki, huggingface, agent-skills, nfl-dfs, poker, cemini-internal, k126]
keywords: [links-docx, tool-eval-v6, clarusc64-coherence, nvidia-skills, mattpocock-skills, hermes-agent, kuhn-poker-sft, ITBench, SWE-bench-Pro]
related:
  - sources/5-4-links-tool-eval.md
  - sources/5-5-links-tool-eval.md
  - sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md
  - concepts/cemini-license-posture.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/nfl-coherence-risk-features.md
  - entities/tools/nvidia-skills.md
  - entities/tools/mattpocock-skills.md
  - entities/tools/hermes-agent.md
  - concepts/active-project-research-routing.md
  - sources/arxiv-continuum-robots-resilience-2606.20495-2026-06-22.md
  - concepts/castle-sim-pathfinding-steals.md
  - concepts/kuhn-poker-sft-curriculum-reference.md
  - sources/huggingface-model-evals-74url-2026-06-23.md
maturity: validated
read_status: deep-read
created: 2026-06-22
updated: 2026-06-23
---

## Relations

- @sources/5-4-links-tool-eval.md — prior K27/K28 batch; same 8-section eval template lineage
- @sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md — v6 multi-wiki routing rubric predecessor
- @concepts/cemini-license-posture.md — eval docx **systematically mislabels licenses**; Phase-0 `gh api` overrides docx claims
- @concepts/wiki-tooling-evaluation.md — Phase-0 registry updated for K126 Adopt/CONDITIONAL-GO rows
- @concepts/nfl-coherence-risk-features.md — ClarusC64 MIT suite (10 Steal-from URLs) promoted from this batch
- @entities/tools/nvidia-skills.md — URL 61; docx Adopt → **CONDITIONAL-GO** after license re-check (Apache-2.0 + CC-BY-4.0 dual)
- @entities/tools/mattpocock-skills.md — URL 62; Adopt confirmed (MIT)
- @entities/tools/hermes-agent.md — URL 63; Steal-from refresh (MIT, v2026.6.19)
- @concepts/kuhn-poker-sft-curriculum-reference.md — Kuhn/Spiral HF SFT corpora; offline format steal (NO LICENSE)

## Raw Concept

- **Original title**: Tool Evaluation Report: 2026-06-22
- **Author**: Gemini Deep Research (146 user-supplied URLs)
- **Type**: DOCX (`links.docx`)
- **Location**: cemini-egress-fi:/opt/cemini-bulk/research/osint/links.docx
- **Retrieved**: 2026-06-22
- **sha256**: `c0a54833abcceedb…` (preingest LIKELY vs historical `4_6 links.docx` filename — **distinct document**)
- **Read status**: deep-read
- **Format caveat**: Word table columns collapsed during export — wiki-fit matrix (✅/❌ per wiki column) parsed as vertical checkbox lines; tier counts recovered from `Tier:` field per URL block, not from table geometry

## Narrative

Largest single links.docx drop since K90 — **146 URLs** evaluated with the standard Cemini 8-section template (identity, stack, maturity, tier, primary fit, cross-wiki routing, reasoning, license risk). Domains span Hugging Face datasets, GitHub agent-skill repos, cybersec benchmarks, NFL tactical features, poker SFT corpora, and image-gen voice models.

### Recommendation distribution (recovered from collapsed export)

| Tier | Count | Notes |
|------|-------|-------|
| **Reject** | 83 | fineweb-2, unlicensed scraped corpora, off-domain PM/SEO noise |
| **Reference-only** | 42 | ITBench-AA, SWE-bench_Pro, trace inversion sets — study only |
| **Steal-from** | 18 | ClarusC64 NFL coherence suite (10× MIT), hermes-agent, nuwa-skill, Kuhn/Spiral poker SFT |
| **Adopt** | 2 | nvidia/skills (license corrected → CONDITIONAL-GO), mattpocock/skills (MIT confirmed) |
| **Defer** | 1 | context-mode (NO LICENSE) |

### Active-project routing (co-primary briefs staged)

| Cluster | Tier | Brief target |
|---------|------|--------------|
| ClarusC64 NFL coherence-risk (URLs 30–39) + Karmane rest/travel sample | Steal-from | CeminiDFS — stage-2 feature extensions |
| mattpocock/skills + nvidia/skills signing patterns | Adopt / CONDITIONAL-GO | CCC-wiki — skill supply + castle-sim `to-issues` |
| Kuhn / Spiral poker SFT datasets (URLs ~140+) | Steal-from (NO LICENSE on HF) | Poker Arena — HU curriculum reference only |
| hermes-agent v2026.6.19 | Steal-from | CCC — self-improving skill loop patterns (existing entity page) |

### License spot-check overrides (Phase-0, 2026-06-22)

| URL | Docx claim | `gh api` / file read | Posture |
|-----|------------|----------------------|---------|
| nvidia/skills | MIT | **Apache-2.0 AND CC-BY-4.0** (dual LICENSE file) | **CONDITIONAL-GO** — attribution + no static embed without legal review |
| mattpocock/skills | MIT | MIT | **Adopt** |
| NousResearch/hermes-agent | MIT | MIT, ~200k★, pushed 2026-06-22 | Steal-from (runtime too heavy for prod stack) |
| alchaincyf/nuwa-skill | MIT | MIT | Steal-from |
| ClarusC64 NFL suite | MIT (HF snippet) | MIT per dataset card | Steal-from — methodology extract, not HF dependency |
| kuhn-poker / Spiral-Kuhn SFT | NO LICENSE | NO LICENSE | Reference-only — do not train on corpus without license |

### Rejects aggregated (no per-URL stubs)

Unlicensed massive web scrapes (fineweb-2), duplicate nflverse fetch paths, off-domain image/SEO corpora, and PM-bot repos without licenses roll into this source page per `@concepts/wiki-tooling-evaluation.md` reject-stub discipline.

## Snippets

> "The repository isolates advanced coherence risk markers fundamentally missing from the standard nflverse projection stage within CeminiDFS." [Source: links.docx URL 30 — nfl-playcall-defense-coherence-risk-v0.1]

> "This ecosystem actively sets the standard for securely distributing and verifying the SKILL.md format protocol." [Source: links.docx URL 61 — nvidia/skills; license corrected in Phase-0]

> "Delivering uncompromising, battle-tested directives—specifically tools like to-issues and grill-me—the repository significantly accelerates agent precision across fragmented projects." [Source: links.docx URL 62 — mattpocock/skills]

> "Format caveat: Word table columns collapsed during export — tier counts recovered from Tier: field per URL block." [Source: ingest session note 2026-06-22]
