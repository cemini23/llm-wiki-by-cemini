---
title: "Cemini Tool Evaluation Plan.docx — 62 URL HF/GitHub eval (2026-06-23)"
type: source
tags: [tool-evaluation, license-compliance, nfl-dfs, polymarket, cemini-internal, k127]
keywords: [cemini-tool-eval-plan, sportsdataverse-py, nflverse, HF datasets, DFS, polymarket-sports-bot]
related:
  - concepts/cemini-license-posture.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/nfl-coherence-risk-features.md
  - entities/tools/sportsdataverse-py.md
  - sources/github-nfl-repo-eval-cemini-2026-06-21.md
  - sources/huggingface-model-evals-74url-2026-06-23.md
  - concepts/active-project-research-routing.md
  - sources/arxiv-agentic-time-machine-2606.21013-2026-06-23.md
  - sources/tool-eval-metaplan-81url-2026-06-24.md
updated: 2026-06-24
---

## Relations

- @concepts/cemini-license-posture.md — eval docx license claims require `gh api` override
- @entities/tools/sportsdataverse-py.md — sole Adopt row (MIT confirmed Phase-0)
- @sources/github-nfl-repo-eval-cemini-2026-06-21.md — prior NFL repo eval (K125)

## Raw Concept

- **Original title**: Comprehensive Evaluation of Open-Source Repositories for the Cemini Ecosystem
- **Author**: Gemini Deep Research (62 user-supplied URLs — Hugging Face + GitHub)
- **Type**: DOCX (`Cemini Tool Evaluation Plan.docx`)
- **Location**: `cemini-egress-fi:/opt/cemini-bulk/research/osint/Cemini Tool Evaluation Plan.docx`
- **Retrieved**: 2026-06-23
- **sha256**: `bd61f70884f3c60d15b777fd582c7d2fcaeb8838f868173003101ac0e8f3cc9f`
- **Read status**: deep-read (tier aggregation + Adopt license spot-check)

## Narrative

Focused eval batch mapping **NFL/DFS datasets**, **vision captioning football models**, and **PM sports bot** repos against CeminiDFS / pm-kalshi / wc-ticket-monitor surfaces. Standard 8-section template.

### Recommendation distribution

| Tier | Count | Notes |
|------|-------|-------|
| **Reject** | 42 | Unreachable HF endpoints, unlicensed scrapes, huggingtweets noise |
| **Reference-only** | 16 | YOLO football detectors, BLIP caption adapters, MicPie Yahoo fantasy QA dataset |
| **Steal-from** | 3 | jjesse/nfl-stats-dashboard, MinaDo7a/yfs-api, thiagocavalheiro/polymarket-sports-trading-bot — **all NO LICENSE in docx** → downgrade to REFERENCE methodology only |
| **Adopt** | 1 | sportsdataverse/sportsdataverse-py |

### License spot-check overrides (Phase-0, 2026-06-23)

| URL | Docx claim | `gh api` | Posture |
|-----|------------|----------|---------|
| sportsdataverse/sportsdataverse-py | MIT | **MIT**, 104★, pushed 2026-06-23 | **Adopt** → CeminiDFS brief |
| sportsdataverse/nfl-data | MIT | not re-checked (data package) | Reference-only — use via sportsdataverse-py |
| thiagocavalheiro/polymarket-sports-trading-bot | Steal-from | NO LICENSE | **Reject** for prod — wiki reference only |
| jjesse/nfl-stats-dashboard | Steal-from | NO LICENSE | Reference-only dashboard UX steal |
| keremberke/yolov5n-nfl | Reference-only | NO LICENSE | Reject install — vision not on CeminiDFS critical path |

### Active-project routing

| Cluster | Brief target |
|---------|--------------|
| sportsdataverse-py (MIT) | CeminiDFS — nflverse-adjacent fetch layer |
| thiagocavalheiro PM sports bot | pm-kalshi wiki-only (no license) |
| Football YOLO/caption HF models | Reject aggregated — no per-URL stubs |

## Snippets

> "Tier: Adopt — sportsdataverse/sportsdataverse-py — MIT — primary Python client for sportsdataverse ecosystem." [Source: Cemini Tool Evaluation Plan.docx (retrieved 2026-06-23); license confirmed via `gh api`]

> "Reject aggregated: unreachable HF spam repos (DFSFSDF/BK, aliali/dfSF) and unlicensed huggingtweets artifacts offer zero mappable code paths." [Source: ingest aggregation 2026-06-23]
