---
title: Ziva — GPT-5.6 Godot Flappy Bird agent benchmark — 2026-07-10
type: source
tags: [source, ziva, godot, benchmark, digest, gpt-5.6]
keywords: [ziva, gpt-5.6, godot, benchmark, playtest, flappy-bird]
related:
  - entities/tools/ziva-godot-agent.md
  - sources/ziva-godot-agent-phase-0-audit-2026-06-21.md
  - concepts/ai-game-dev-tool-stack-2026.md
  - concepts/agent-harness-castle-project.md
  - concepts/godot-stagehand-ci-smoke-plan.md
  - sources/inbox-arxiv-reject-batch-2026-07-11.md
  - meta/cross-wiki-routing.md
read_status: read
source_type: news-digest
source_url: https://ziva.sh/blogs/gpt-5-6-benchmark-godot
maturity: validated
created: 2026-07-11
updated: 2026-07-11
---

## Raw Concept

Digest pick (2026-07-10): **Ziva** benchmarked **GPT-5.6** (Luna/Terra/Sol) building a complete Flappy Bird in Godot via in-editor agent tools (file writes, scene tree, playtest frame). All three variants scored 10/10 rubric (~4/5 stars vs anchors); Luna cheapest at **$0.17** / 26 tool calls.

## Narrative

### Benchmark protocol [CONFIRMED — Ziva blog]

| Turn | Task |
|------|------|
| 1 | Flappy Bird: gravity, flap, scrolling pipes, collision game-over |
| 2 | Score counter + playtest-and-fix |
| 3 | Game Over overlay + restart |

Scoring: tool reliability, code correctness, core loop, follow-up fidelity, visuals (0–2 each). Verified via GDScript read, engine error log, three playtests per build.

### Harness lessons for castle-sim [TENTATIVE]

| Extract | Skip |
|---------|------|
| **Runtime playtest loop** validates agentic Godot work better than static lint | Adopting Ziva proprietary stack for public harness |
| **Default reasoning effort** beat xhigh for Sol ($1.59 vs $11.69) — agent loop is the intelligence | Model-picker churn in castle-sim stories without regression gate |
| Muse Spark failed on “test and fix” spiral — cap-aware executor policy | Flappy Bird as castle-sim acceptance proxy |

**Verdict:** **NOTE** — update @entities/tools/ziva-godot-agent.md; reinforces W2 smoke/playtest gate (@concepts/godot-stagehand-ci-smoke-plan.md). **No Phase-0 change** (existing CONDITIONAL-GO); **no new brief** — castle-sim harness stays Cursor + MIT tools.

## Dead Ends

- Switching castle-sim executor default to GPT-5.6 Luna based on Flappy Bird benchmark alone
