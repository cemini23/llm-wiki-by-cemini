---
title: "RAPID: Robot Agentic Programming from Demonstrations"
type: source
tags: [arxiv, source, k272, ood, robotics]
keywords: [k272, RAPID, demonstration, robot-program, not-a-product]
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

| Paper | arXiv:2609.30249 |
| File | `arxiv-2609.30249-rapid-robot-agentic-programming-from-demonstrati.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2609.30249-rapid-robot-agentic-programming-from-demonstrati.pdf` |
| Archive | egress-fi 2026-09-25 |
| Authors | Yuyao Liu, Jiayuan Mao, David Hsu, Leslie Pack Kaelbling, Tomás Lozano-Pérez (MIT; NUS; UPenn; NVIDIA) |
| Retrieved | 2026-09-25 |
| Pages | 9 |
| Dual-ID | **OSINT K272** |
| sha256 | `92295be94ca059a4cde83f047f6a9f4ca7e64c3f9506038c4b22300dcefa8dd5` |
| Code | No GitHub repo in the PDF |

## Narrative

RAPID writes a robot program from one visual human demonstration. It infers a testable task specification, action primitives, and an interactive check environment. The program is object-centric. The strategy is not tied to one recorded motion. RAPID segments the demonstration into several phases, infers a subgoal and success predicate for each phase, and performs real-to-sim reconstruction to obtain interactive simulation environments. RAPID further synthesizes feasible scene variants for additional verification. For each phase, the coding agent generates a primitive and iteratively executes, verifies, and revises it across the reconstructed environment and its variants. RAPID then infers the overall task goal and success predicate, composes the primitives into a strategy, and refines the composition through the same loop. The object-centric relational program representation represents manipulation primitives as trajectory-optimization programs that achieve an object-level effect, and composes them through relational constraints that specify the desired effect of each primitive. Evaluated on eight contact-rich nonprehensile manipulation tasks in simulation and on LIBERO-Pro, RAPID demonstrated strong performance with generalization over object pose, shape, material, and environment. Successfully deployed on a real Franka arm. No repo is in the PDF. This is **not a product**.

**Cemini posture:** FILE. OOD. **0 product Integrate GO.**

## Snippets

> "RAPID automatically generates, verifies, and refines robot programs, given a single visual human demonstration." [Source: https://arxiv.org/html/2609.30249 (retrieved 2026-09-25)]

> "The object-centric relational program representation represents manipulation primitives as trajectory-optimization programs and composes them with relational constraints, enabling generalization to novel scenes." [Source: https://arxiv.org/html/2609.30249 (retrieved 2026-09-25)]