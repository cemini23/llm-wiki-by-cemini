---
title: "Multi-Wiki Link Evaluation.docx — OpenClaw ecosystem batch (2026-06-30)"
type: source
tags: [tool-evaluation, openclaw, agent-harness, k137, docx]
keywords: [openclaw, clawhub, DeepSpec, OpenClaw-RL, mission-control, zero-token, gemini-deep-research-v9]
related:
  - concepts/wiki-tooling-evaluation.md
  - concepts/openclaw-security-taxonomy.md
  - entities/tools/openclaw.md
  - entities/tools/deepspec.md
  - entities/tools/openclaw-rl.md
  - entities/tools/clawhub.md
  - entities/tools/open-im-server.md
  - entities/tools/openclaw-mission-control.md
  - entities/tools/openclaw-zero-token.md
  - sources/eval-github-batch-unusualwhales-2026-06-28.md
  - sources/openclaw-ios-node-2026-06-29.md
  - concepts/rl-marl-research.md
  - sources/eval-multi-wiki-agent-harness-v2-2026-07-03.md
maturity: draft
read_status: read
created: 2026-06-30
updated: 2026-10-25
clusters: [agent-harness, wiki-tooling]
---

## Relations

- @entities/tools/openclaw.md — gateway entity; Tier A/C posture unchanged
- @entities/tools/deepspec.md — K137 Adopt (MIT)
- @entities/tools/openclaw-rl.md — K137 Adopt (Apache-2.0)
- @entities/tools/clawhub.md — K137 Steal-from (official skill registry)
- @concepts/openclaw-security-taxonomy.md — ClawHub supply-chain context (K20)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Multi-Wiki Link Evaluation (Gemini Deep Research RUNTIME v9) |
| **Type** | DOCX |
| **sha256** | `6080f49f1a8ef2527fff6696a3532686ea7b03278b0df6006bd1008878f2af78` |
| **Batch theme** | OpenClaw ecosystem extensions, local inference, multi-agent ops |
| **URLs** | 20 |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/Multi-Wiki Link Evaluation.docx` |
| **Retrieved** | 2026-06-30 |
| **Read status** | read (`gh api` on GitHub rows) |

## Narrative

K137 batch — **20 URLs** (8 HuggingFace OpenClaw adapters + 12 GitHub ecosystem repos).

### Tier distribution (docx + gh spot-check 2026-06-30)

| Tier | Count | Items |
|------|-------|-------|
| **Adopt** | 2 | Gen-Verse/OpenClaw-RL (Apache-2.0), deepseek-ai/DeepSpec (MIT) |
| **Steal-from** | 5 | sunkencity/qwen25-3b-openclaw (HF), openimsdk/open-im-server, openclaw/clawhub, linuxhsj/openclaw-zero-token, abhi1693/openclaw-mission-control |
| **Reference-only** | 5 | JetLM/OpenClaw-macOS (HF), cloud8443/Gemma-4-31B (HF), VoltAgent/awesome-openclaw-skills, hesamsheikh/awesome-openclaw-usecases, TianyiDataScience/openclaw-control-center |
| **Reject** | 4 | Crazyrouter guide, Ishant06 continuous-pretraining, sulpikar2 Qwen mash, mengjian-github/openclaw101 |
| **UNAVAILABLE** | 4 | williamKang112/multi-agent-openclaw (HF), GarryKouyu/openclaw-offline (HF), NOIRAgentic qwopus adapters ×2 |

### gh api corrections vs docx

| Repo | Docx license | Verified 2026-06-30 |
|------|--------------|---------------------|
| TianyiDataScience/openclaw-control-center | NOT FOUND | **MIT** — reference-only (UX patterns) |
| mengjian-github/openclaw101 | MIT | **NOASSERTION/null** — Reject stands (tutorial front-end only) |

### HuggingFace cluster

Most HF rows: **NO LICENSE** on model cards → Reject/UNAVAILABLE/Reference only. Exception: **qwen25-3b-openclaw** steal tool-call JSON tag patterns (assume Qwen weights terms; no SPDX on card).

### Cross-wiki routing

| Wiki | Steals |
|------|--------|
| **OSINT** | DeepSpec latency, OpenClaw-RL self-improvement, open-im-server transport, zero-token CDP scraping patterns, mission-control fleet audit |
| **CCC** | clawhub skill-format + static scan, awesome-* catalogs as harness design refs |
| **TipDrop** | clawhub YAML/skill validation for ingest compliance |
| **Prod (brief)** | DeepSpec → xsp-killer inference; mission-control → PM/XSP fleet observability |

**OpenClaw Tier C prod NO-GO unchanged** — ecosystem tools do not lift cemini-prod trading integration bar (@entities/tools/openclaw.md).

## Snippets

> "DeepSpec introduces semi-autoregressive speculative decoding … slashing inference latency by an estimated 60–85%." [Source: eval docx URL 20, 2026-06-30; gh MIT verified]

> "clawhub … defines rigorous schemas and frontmatter parsing logic necessary to execute third-party agent skills safely." [Source: eval docx URL 15, 2026-06-30; openclaw/clawhub MIT]

## Dead Ends

- HF adapter mashups without license metadata — do not download weights into prod.
- openclaw101 — consumer tutorial site; no backend steal despite docx MIT claim (gh license null).
