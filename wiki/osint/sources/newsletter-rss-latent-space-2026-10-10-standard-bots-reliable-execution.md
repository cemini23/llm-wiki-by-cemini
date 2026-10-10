---
title: "Latent Space — Building AI for reliable execution: lessons from industrial robotics (2026-10-10)"
type: source
tags: [source, k288, robotics, reliability, agents, ccc]
keywords: [standard-bots, industrial-robotics, on-prem-inference, data-quality, co-optimization, short-horizon, conventional-programming]
related:
  - concepts/k288-feeds-wave.md
maturity: draft
created: 2026-10-10
updated: 2026-10-10
read_status: read
---

## Relations

- @concepts/k288-feeds-wave.md

## Raw Concept

| Title | Building AI for Reliable Execution: Lessons From Industrial Robotics |
| Source | Latent Space (Substack) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/newsletter-rss-latent-space-2026-10-10-building-ai-for-reliable-execution-lessons-from.md` |
| Retrieved | 2026-10-10 |
| URL | https://www.latent.space/p/standard-bots |
| Tier | free (RSS teaser) |
| cross-wiki | ccc-wiki |
| read-status | read |

## Narrative

An interview with **Standard Bots** (co-founder/CEO Evan Beard; Head of AI Leif Jentoft) — "America's largest AI-native industrial robot manufacturer", recently **$200M at a $1B valuation**, customers including **NASA, Amazon, Lockheed Martin**.

### The architecture

- **Perception is learned; motion and cell logic are conventional code.** "The model handles perception — locating and identifying the parts — while conventional programming handles the motion and the cell logic around it."
- **Short-horizon tasks.** To meet cycle-time and reliability requirements, the model does only what needs learning.
- **Inference runs on-premise.** Training in the cloud; inference at the factory. For the core customers, on-prem is a hard requirement.
- **One base model, adapted per task** by demonstration and fine-tune. The largest model is **low-billions of parameters** — not frontier-scale.
- **Data quality over volume.** "In-situ interventions can fix an edge case with a few dozen examples." The largest model is trained on **>1 billion images** for perception.
- **Full-stack co-optimisation.** They own the arm, end effector, and control system: "no model today is truly hardware-agnostic, and co-optimizing low-level control and higher-level functions is a major advantage."

### Why it matters here

The same doctrine as the wiki's K285/K286 threads, from the physical-AI side: **learn what needs learning, keep everything else deterministic, run inference where the data lives, and value targeted data over volume.** It is the industrial-robotics twin of "code fetches, the model judges, code decides". The on-prem inference point also echoes the local-inference lane (`Strata`, `Rapid-MLX`).

## Snippets

> "The model handles perception — locating and identifying the parts — while conventional programming handles the motion and the cell logic around it." [Source: newsletter-rss-latent-space-2026-10-10-building-ai-for-reliable-execution-lessons-from.md]

> "In-situ interventions can fix an edge case with a few dozen examples." [Source: newsletter-rss-latent-space-2026-10-10-building-ai-for-reliable-execution-lessons-from.md]
