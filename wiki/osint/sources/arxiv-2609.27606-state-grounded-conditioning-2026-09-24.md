---
title: "State-Grounded Conditioning for User-Facing LLM Agents"
type: source
tags: [arxiv, source, k271, harness]
keywords: [k271, SGC, live-state, wrappers, direction-drift]
related:
  - concepts/k271-harness-evolution-wave.md
maturity: draft
created: 2026-09-24
updated: 2026-09-24
read_status: skimmed
---

## Relations

- @concepts/k271-harness-evolution-wave.md

## Raw Concept

| Paper | arXiv:2609.27606 |
| File | `arxiv-2609.27606-state-grounded-conditioning-wrapping-user-facing.pdf` |
| Location | `research to be indexed/arxiv-2609.27606-state-grounded-conditioning-wrapping-user-facing.pdf` |
| Archive | pending |
| Authors | Qi Liu and co-authors (Tencent) |
| Retrieved | 2026-09-24 |
| Pages | 18 |
| Dual-ID | **OSINT K271** |
| sha256 | `9699ce249f7cf0b31394687f95ced4864c4612a622eb59f1d4e3ea9dbb937c99` |
| Code | No repo in the PDF |

## Narrative

State-Grounded Conditioning (SGC) is a design claim for user-facing agents whose next step depends on live state. The paper names a failure it calls direction drift: the reply is task-complete, but the chosen direction does not match the current state. SGC moves that control into wrappers over structured inputs. The three wrappers are Perception, Grounding, and Interaction.

The paper reports a 200-session benchmark (about 1,000 assistant turns) from an in-game coaching agent. It reports that the Perception wrapper holds mean first-token latency at 1.5 seconds, against 6.1 seconds for a cited baseline inside a tool-use harness. It reports that all three wrappers lift turn-level grounded accuracy from 61.1% / 69.8% to 96.7%.

**Cemini posture:** live-state wrapper pattern only. **FILE. No repo to clone. 0 product Integrate GO. Do not swap `/route`.**
