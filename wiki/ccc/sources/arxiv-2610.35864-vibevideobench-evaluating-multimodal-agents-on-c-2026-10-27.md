---
title: "VibeVideoBench: Evaluating Multimodal Agents on Code-Driven Video Generation"
type: source
tags: [source, arxiv, agent-benchmark, video-generation]
related: []
maturity: draft
read_status: skimmed
created: 2026-10-27
updated: 2026-10-27
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | VibeVideoBench: Evaluating Multimodal Agents on Code-Driven Video Generation |
| Authors | Muxi Diao, Wenbin Xu, Lele Yang, Xuyang Ma, Yuzhe Chen, Jiankang Chen, Kaiyu Jiang et al. (Beijing University of Posts and Telecommunications; Zhongguancun Academy; Peking University; Jilin University; Kling Team) |
| arXiv | 2610.35864 |
| File | `arxiv-2610.35864-vibevideobench-evaluating-multimodal-agents-on-c.pdf` |
| Retrieved | 2026-10-27 |
| URL | https://arxiv.org/abs/2610.35864 |
| Read status | skimmed (abstract + intro) |

## Narrative

Diffusion video models produce striking clips but cannot follow a long, exact specification. **VibeVideoBench** instead asks a multimodal agent to turn a self-contained specification into a finished MP4, using only code.

The task spans 239 items in 12 categories, in English and Chinese, with target runtimes from 8 seconds to 15 minutes. Agents render with three.js, Canvas, SVG, or cairo, add TTS voice, synthesise music and sound effects, and mux with ffmpeg — all inside a sandbox within one hour.

Grading combines three layers: program checks, an average of 54 task-specific rubric checks, and five quality dimensions judged by three audio-visual judge panels.

Models named in the sampler include Kimi K3, DeepSeek-V4.1-Flash, Gemini 4, GPT-6 Astra, GPT-5.6 Sol, Claude Opus 5.5, GLM-5.3-Flash, and Claude Sonnet 5.5.

**Why it matters.** Two points for a workspace that exposes image and video generation. First, code-driven generation is a distinct capability from diffusion generation, and it is measurable. Second, the emphasis on rubrics over a single score matches the same lesson the rules paper makes: many small mechanical checks beat one holistic judgement.

## Snippets

> "VibeVideoBench asks a multimodal agent to turn a self-contained specification into a finished MP4 with sound, using only code." [Source: `arxiv-2610.35864-vibevideobench-evaluating-multimodal-agents-on-c.pdf` p.1 (arXiv 2610.35864), retrieved 2026-10-27]
