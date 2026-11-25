---
title: "Deep Research link evaluation — game engine, media verification, container ops (2026-11-16)"
type: source
related:
  - concepts/agent-link-evaluation-gates-v1013.md
  - sources/2026-11-16-deep-research-link-eval-agentic-harnesses.md
  - "@game-dev-wiki/entities/tools/ffmpeg-skill.md"
  - "@game-dev-wiki/entities/tools/estella.md"
updated: 2026-11-16
read_status: read
maturity: draft
---

## Raw Concept

- **Title:** Cemini Multi-Wiki Link Evaluation (batch B)
- **Author:** Deep Research evaluation run, operator-supplied rubric v10.13
- **Type:** vendor-link evaluation report (DOCX)
- **Location:** `cemini-egress-fi:/opt/cemini-bulk/research/osint/Cemini Multi-Wiki Link Evaluation (1).docx`
- **Retrieved:** 2026-11-16
- **Pages:** 20 URL records
- **Read status:** read

Batch theme: game engine ECS and playable-ad architecture, deterministic FFmpeg media
verification, equity trading agent workflows, self-hosted container operations, and
DSH tooling.

## Narrative

This batch honoured its own budget. Two URLs cleared the bar, both graded Extract, and
both route to game-time. All other eighteen defaulted to Context or Pass.

### Graded outcomes

| Tier | Count | Items |
|------|-------|-------|
| Extract | 2 | `ffmpeg-skill`, `estella` |
| Context | 12 | `decky-lsfg-vk`, `plannotator` (repeat), `claude-trading-skills`, `arcane`, `paper-orchestra`, `svelte`, `tatami`, `phonebox`, `cc-switch-cli`, `archify`, `dsh-our-free-model`, `open-code-review` |
| Pass | 6 | `swamp`, `deepseek-ai/chat-demo`, `lazydsh` (repeat), `code.claude.com/sub-agents` (repeat), `aitmpl/fable-5-2-advisor`, `copybook.page` |

### Why the two winners hold

**`ffmpeg-skill`** — MIT, 6.6k stars, pushed the same day as the evaluation. It gives a
coding agent 42 FFmpeg operations behind a machine-readable interface. game-time has no
`ffmpeg` reference anywhere in `packages/`, so the media-verification gap is real.
[CONFIRMED — local repository check 2026-11-16]

**`estella`** — Apache-2.0, 938 stars, TypeScript SDK over a C++/WebAssembly core. It
is a 2D and 3D engine with an ECS shape close to the castle-sim and game-time slice
work. Extract here means the architecture notes, not a dependency swap.

### Items the batch correctly refused

- **`decky-lsfg-vk`** — requires the proprietary Steam Lossless Scaling application and
  its `Lossless.dll`. The repository licence is `NOASSERTION` on the tracker snapshot.
  A paid proprietary binary cannot enter a shipped stack. Context only.
- **`open-code-review`** — the Workstation Harness Freeze blocks a new review runner
  locally while `code-review` and `simplify` already cover the ground.
- **`claude-trading-skills`** — routes to the retired poker and TipDrop posture; the
  CeminiSuite lane is not a target this cycle.

### Overlap with batch A

`plannotator`, `lazydsh`, `code.claude.com/docs/en/sub-agents`, `aitmpl`, and
`copybook.page` appear in both batches with different tiers. Batch A graded
`plannotator` Integrate; batch B graded it Context. Batch A is the later reading and it
matches our Phase-0, so batch A's grade stands. The duplicate grading is a report
artifact, not new evidence.

## Snippets

> Actionable budget: Max 2 URLs total across this batch may earn Integrate or Extract.
> [Source: Cemini Multi-Wiki Link Evaluation (1).docx, research plan]

> decky-lsfg-vk requires a proprietary Windows Lossless.dll binary purchased from
> Steam. [Source: Cemini Multi-Wiki Link Evaluation (1).docx, URL 1]

## Dead Ends

- **Bundling a wrapper around a paid proprietary DLL.** `decky-lsfg-vk` cannot ship;
  only its frame-pacing tuning notes are usable, and they belong to QA, not to code.
- **Re-running a URL that an earlier batch already settled.** Five URLs repeat across
  the two files. The tiers disagree, which costs a reconciliation pass for no new
  information.
