---
title: "World Action Agent: VLMs for Robot Manipulation"
type: source
tags: [arxiv, source, k272, ood, robotics]
keywords: [k272, World-Action-Agent, VLM, robot, not-a-product]
related:
  - concepts/k272-ood-stub-wave.md
maturity: validated
created: 2026-09-25
updated: 2026-09-25
read_status: deep-read
---

## Relations

- @concepts/k272-ood-stub-wave.md

## Raw Concept

| Paper | arXiv:2609.29964 |
| File | `arxiv-2609.29964-world-action-agent-harnessing-vlms-for-robot-man.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2609.29964-world-action-agent-harnessing-vlms-for-robot-man.pdf` |
| Archive | egress-fi 2026-09-25 |
| Authors | Yehang Zhang and co-authors (HKUST(GZ); CUHK; Knowin AI) |
| Retrieved | 2026-09-25 |
| Pages | 29 |
| Dual-ID | **OSINT K272** |
| sha256 | `c5eb945bc6c5a370bcabd202daa864925a8ddebce46992db4d9cbf953cfb5d3f` |
| Code | No GitHub repo in the PDF |

## Narrative

World Action Agent is a multi-agent harness for a robot. Vision-language models pilot the robot with basic tools inside a visual workspace. Contact views show the scene around the current interaction. Action rehearsal turns a move into a proposal that the agent can preview before execution. The workspace has three properties: contact views selected automatically for the current interaction, action rehearsal that lets the agent test actions before execution, and in-view correction that closes the loop between observation, rehearsal, and low-level execution. A Skill Agent evolves multimodal skills from expert videos and human teaching under evidence-based review. Interaction traces train smaller VLMs to pilot the same harness. On LIBERO-Pro, WAA with skills evolved only from LIBERO-90 reaches a state-of-the-art 75.6% average success, outperforming end-to-end VLAs, code-as-policy agents, and a visual-harness baseline with the same backbone; the same skills remain effective on robosuite without further learning. Fine-tuning Qwen3.5-9B on harness traces raises its out-of-domain success from 1.7% to 43.3%. No repo is in the PDF. This is **not a product**. No robotics install.

**Cemini posture:** FILE. OOD. **0 product Integrate GO.**

## Snippets

> "We present World Action Agent (WAA), a multi-agent embodied harness in which agents observe the scene, construct actions, and drive the robot through basic tools alone, build and retrieve multimodal skills, and make every decision within a single visual action workspace." [Source: https://arxiv.org/html/2609.29964 (retrieved 2026-09-25)]

> "WAA achieves a state-of-the-art 75.6% average success on LIBERO-Pro and transfers to robosuite without further learning." [Source: https://arxiv.org/html/2609.29964 (retrieved 2026-09-25)]