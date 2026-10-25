---
title: "Tool Evaluation Analysis Metaplan.docx — 81 URL game-dev / DFS / poker eval (2026-06-24)"
type: source
tags: [tool-evaluation, license-compliance, game-dev, dfs, poker, cemini-internal, k128]
keywords: [metaplan-tool-eval, BBMOD, pydfs-lineup-optimizer, yuspec-gamedev-ai, fanduel-api, LongShu-GameDev]
related:
  - concepts/cemini-license-posture.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/active-project-research-routing.md
  - entities/tools/bbmod.md
  - sources/cemini-tool-evaluation-plan-62url-2026-06-23.md
  - sources/github-nfl-repo-eval-cemini-2026-06-21.md
  - concepts/polymarket-bot-architecture.md
  - entities/tools/draftfast.md
  - sources/eval-github-repo-plan-dfs-marl-poker-osint-2026-07-01.md
  - sources/eval-url-cemini-research-2026-06-25.md
maturity: draft
read_status: deep-read
created: 2026-06-24
updated: 2026-10-25
---

## Relations

- @concepts/cemini-license-posture.md — eval docx license claims require `gh api` override
- @entities/tools/bbmod.md — sole Adopt row (MIT confirmed Phase-0)
- @sources/cemini-tool-evaluation-plan-62url-2026-06-23.md — prior K127 NFL/PM eval batch

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Comprehensive Ecosystem Evaluation and Architectural Alignment Report |
| **Author** | Gemini Deep Research (Metaplan user-supplied URLs — Hugging Face + GitHub) |
| **Type** | DOCX (`Tool Evaluation Analysis Metaplan.docx`) |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/Tool Evaluation Analysis Metaplan.docx` |
| **Retrieved** | 2026-06-24 |
| **sha256** | `1c825138874c8e22fbbeaadc908ebea5a89a5c11dc8efc2c96edb8c7a423b80e` |
| **Read status** | deep-read (tier aggregation + Adopt license spot-check) |

## Narrative

Multi-wiki eval mapping **game-dev HF models**, **DFS optimizers**, **poker arena repos**, and **scraping utilities** against co-primary surfaces (castle-sim, CeminiDFS, poker-arena, pm-kalshi). Standard 8-section template with synthesis sections on DFS convergence, adversarial scraping, and license poisoning.

### Recommendation distribution

| Tier | Count | Notes |
|------|-------|-------|
| **Reject** | ~45 | UNAVAILABLE HF endpoints, NO LICENSE scrapes, FLUX NC, GPL-3.0 fanduel-api fork, poker_arena.py noise |
| **Reference-only** | 8 | phi-3-gamedev (stale), stackexchange GGUF (unlicensed), NBA-DFS-Tools, sports-betting mockups |
| **Steal-from** | 4 | yuspec-gamedev-ai, bcanfield/southpaw, Live-Sports-Arbitrage-Bet-Finder, Setfive/fanduel-api — methodology only where NO LICENSE |
| **Defer** | 3 | LongShu GameDev MLX models — experimental, unverified HF licenses |
| **Adopt** | 1 | blueburncz/BBMOD |

### License spot-check overrides (Phase-0, 2026-06-24)

| URL | Docx claim | `gh api` | Posture |
|-----|------------|----------|---------|
| blueburncz/BBMOD | MIT Adopt | **MIT**, 118★, pushed 2026-05-30 | **Adopt** → @game-dev-wiki (GameMaker 3D); **NO-GO** castle-sim (Godot) |
| DimaKudosh/pydfs-lineup-optimizer | Reference (duplicate) | **MIT**, 443★, stale 2024-02 | Reference-only — duplicates CeminiDFS stages 2–3 |
| fovane/yuspec-gamedev-ai | Steal-from MIT | **MIT**, 0★ | Steal-from — Godot/Unity/Unreal instruction-data builders |
| Setfive/fanduel-api | Steal-from MIT | **MIT**, 52★ | Steal-from — WebSocket lobby telemetry pattern (not PM CLOB) |
| fal/3D-Game-Assets-Kontext-Dev-LoRA | Reject | flux1-dev-non-commercial | **Reject** — poison pill |
| RK-GEEKSDOBYTE/fanduel-api | Reject | GPL-3.0 | **Reject** — copyleft contamination |

### Active-project routing

| Cluster | Brief target |
|---------|--------------|
| BBMOD (MIT, GameMaker) | @game-dev-wiki brief — 3D rendering reference; not castle-sim install |
| pydfs / draftfast / NBA-DFS-Tools | Wiki-only — CeminiDFS pipeline supersedes |
| Setfive/fanduel-api WebSocket | CCC-wiki steal — local agent telemetry pattern |
| LongShu MLX GameDev models | Defer — unverified HF license + experimental |

### Rejects aggregated (no per-URL stubs)

Unreachable HF spam, unlicensed huggingtweets, poker_arena.py wrappers, FanDuel phishing repos (journal-m-fanduel cluster), GPL/NC poison pills.

## Snippets

> "Adopt: 1 — blueburncz/BBMOD — MIT — 3D graphics rendering library for GameMaker." [Source: Tool Evaluation Analysis Metaplan.docx (retrieved 2026-06-24); license confirmed via `gh api`]

> "CeminiDFS duplicates (Reference-only): 5 (chanzer0/NBA-DFS-Tools, DimaKudosh/pydfs-lineup-optimizer, BenBrostoff/draftfast, WolverineSportsAnalytics/basketball, davehensley/fanduel-nba-optimizer)" [Source: Tool Evaluation Analysis Metaplan.docx shipped-stack overlap summary (retrieved 2026-06-24)]

> "The integration of any artifact carrying a PolyForm Noncommercial or restricted commercial clause would fundamentally poison the codebase." [Source: Tool Evaluation Analysis Metaplan.docx §Architectural Contamination (retrieved 2026-06-24)]
