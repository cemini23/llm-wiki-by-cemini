---
title: "Low-Cost Assays for Model Behavior Across Vendors"
type: source
tags: [arxiv, source, k272, harness]
keywords: [k272, behavior-assays, coding-atlas, modelun, cross-vendor]
related:
  - concepts/k272-harness-evolution-wave.md
  - entities/tools/modelun.md
maturity: validated
created: 2026-09-25
updated: 2026-09-25
read_status: deep-read
---

## Relations

- @concepts/k272-harness-evolution-wave.md
- @entities/tools/modelun.md

## Raw Concept

| Paper | arXiv:2609.30012 |
| File | `arxiv-2609.30012-low-cost-assays-for-measuring-model-behavior-acr.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2609.30012-low-cost-assays-for-measuring-model-behavior-acr.pdf` |
| Archive | egress-fi 2026-09-25 |
| Authors | Tapan Parikh (Cornell Tech) |
| Retrieved | 2026-09-25 |
| Pages | 6 |
| Dual-ID | **OSINT K272** |
| sha256 | `94463b28bfd2611d95d7a7bb5603bb72589630b83ce1ef61bc544c950e8d41bc` |
| Code | coding-atlas SPDX null; modelun MIT SIZE-SKIP |

## Narrative

The paper runs one frozen public stimulus on a cross-vendor panel. The stated cost is a few dollars per model. Each study reads the transcripts in one of three ways: an exact match on a clamped reply, a codebook applied by LLM judges whose agreement with a human coder is reported per code, and an instrumented environment that records what an agent did independently of what it said. Run across four years of model releases from both frontier and open-source labs, these instruments find four things. Convergence: asked to pick a word, 27 of 44 models answer serendipity at least once in four tries. Resistance: a trailing "right?" moves endorsement by up to 32 points, and the sign flips from sycophantic to resistant as generations advance, keyed to the tag's surface form. House: whether a model holds a position under pressure tracks its generation, and how it holds tracks the lab that built it. Account: told to do something the documentation in their repository contradicts, some coding agents never went along silently and others always did, and the same model can change with the harness it runs in. The coding atlas gives a coding agent a small repository and a one-line instruction. Each repository holds a right thing to do, a shortcut that looks finished, and a hidden check the agent never sees. Fourteen configurations ran six scenarios three times each in full-auto mode: Claude Code, Codex CLI and Gemini CLI as products, and eleven models in the OpenCode harness. The harness is part of the behavior: Gemini 3.5 Flash went along silently in three of six replies in Gemini CLI and six of six in OpenCode. Re-run on every release, batteries like these track how behavior is changing across vendors and over time. Stimuli, transcripts, scores and scripts are public at the modelun and coding-atlas GitHub repos.

| Repo | gh api 2026-09-25 | Verdict |
|------|-------------------|---------|
| tap2k/coding-atlas | SPDX null, 7401 KB | **NO-CLONE** |
| tap2k/modelun | MIT, 21956 KB | **SIZE-SKIP.** Size still blocks the clone. `wont_wire` stays |

No clone this wave. The 2026-09-23 SPDX-null note on modelun is superseded by this gh api read. The size block does not change.

**Cemini posture:** FILE. Never auto-evolve skills. **0 product Integrate GO.**

## Snippets

> "Each battery is a frozen stimulus that puts a model in a situation where behavior matters, sent identically to every model on a cross-vendor panel." [Source: https://arxiv.org/html/2609.30012 (retrieved 2026-09-25)]

> "A study at this price is closer in scale to a small experiment with human participants than to a benchmark: one person can run it, repeat it on the next release, and point it at a new question the week after." [Source: https://arxiv.org/html/2609.30012 (retrieved 2026-09-25)]