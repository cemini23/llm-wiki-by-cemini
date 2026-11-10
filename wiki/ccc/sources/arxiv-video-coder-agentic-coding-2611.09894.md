---
title: "Video-Coder — training a coding agent whose code builds the video scene"
type: source
related:
  - concepts/agentic-robotics-harness.md
  - concepts/harness-learning-test-time-adaptation.md
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Video-Coder: Reinforcing Agentic Coding for Video Generation |
| Author | Chaoyang Wang, Sicheng Gao, Junan Hu, and others (UCF, Wurzburg, Microsoft Research, Tsinghua, UNC, UW-Madison) |
| Type | arXiv paper (cs.CV), 2611.09894 |
| Location | `research to be indexed/ccc/arxiv-2611.09894-video-coder-reinforcing-agentic-coding-for-video.pdf` |
| Retrieved | 2026-11-10 |
| Pages | 16 |
| Read status | read |

## Narrative

Direct video generation is weak on exact counts, spatial relations, and physical motion. Code is precise. A short program can state that three spheres fall from different heights.

**Video-Coder** trains an agent that writes and executes code to build a 3D scene. The scene renders to a **draft video**. The draft video then conditions a downstream video generator. Through several turns, the agent reads execution errors and rendered results and revises its code.

The authors built the **Video-Coder Harness**: one environment that integrates code execution, 3D rendering, and execution feedback. They used it both to generate training data and to serve inference. Data: Video-Coder-SFT-6k and Video-Coder-RL-2k.

Training runs in two stages. Supervised fine-tuning teaches scene programming and tool calling. Harness-native agentic RL then improves multi-turn trajectories. Two rewards are used:

- **Execution reward** — does the program run.
- **Video reward** — is the final video correct.

An **annealing schedule** lowers the execution reward over training, so the video reward dominates later. The authors report about 7 points on PhyGenBench and 24 points on VBench-2.0 over MiniMax-H3.

The interesting engineering pattern is general. **Use the harness as the training environment, not a separate simulator.** The same loop that scores a run also generates the training trajectory. The reward schedule is explicit about the handover from "make it run" to "make it good".

## Snippets

> "Video-Coder, the first attempt to train a code-driven video generation agent, which autonomously writes and executes code to construct a dynamic 3D scene (Draft Video) that provides structure and motion signals to downstream video generators." [Source: arxiv-2611.09894-video-coder-reinforcing-agentic-coding-for-video.pdf p.1]

> "we design an annealing training strategy that gradually reduces the execution reward over time, allowing the model to rely more on the video reward in the later training stages." [Source: arxiv-2611.09894-video-coder-reinforcing-agentic-coding-for-video.pdf p.1]
