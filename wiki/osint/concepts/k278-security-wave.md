---
title: K278 Security Wave (Oct 2026)
type: concept
tags: [security, benchmark, k278, agents]
keywords: [k278, kalibench, cli, verifiable-reward, no-poc]
related:
  - concepts/k279-security-wave.md
  - concepts/k277-security-wave.md
  - sources/arxiv-2610.02206-kalibench-2026-10-02.md
maturity: draft
created: 2026-10-02
updated: 2026-10-03
harness_verb: FILE
wire_status: policy_wired
---

## Relations

- @concepts/k279-security-wave.md
- @concepts/k277-security-wave.md
- @sources/arxiv-2610.02206-kalibench-2026-10-02.md

## Raw Concept

K278 cluster hub. Dual-ID **OSINT K278**. Prior @concepts/k277-security-wave.md.

## Narrative

One paper. A benchmark, not an exploit. **No PoC.**

KaliBench measures whether a model can turn plain language into an **exact, executable** command for a real security tool. 8,504 query-command pairs, 1,642 tools, 23 capability dimensions, five phases. Scoring is runtime-free, using canonicalisation plus alias-aware matching.

The finding that transfers beyond security:

| Setting | Result |
|---------|--------|
| Best open-weight, unrestricted | 41.3% exact |
| Best proprietary, unrestricted | 61.68% exact |
| Tool selection, unrestricted to restricted | 72.0% to 95.2% |
| Optional-argument F1, unrestricted to hinted | 45.1% to 87.8% |
| Exact-correct, unrestricted to hinted | 22.3% to 73.1% |

**Tool choice is not the bottleneck; arguments are.** Narrow the candidate set or supply the docs and tool selection nearly resolves. Exactness does not, until the arguments are pinned down.

The second transferable idea is the **runtime-free verifiable reward**. Canonicalisation plus alias-aware matching gives a deterministic score without executing anything. That is the same principle as the K276 trace finding and the K277 confirm-before-report rule: score against a fixed reference, not against a model's own account of what it did.

The authors admit the ground truth comes from manuals captured at build time, so upstream changes can outdate items, and the manuals themselves contain inconsistencies. Single-turn only.

The dataset licence is claimed as CC BY-NC 4.0 — a docx-style claim. Verify with `gh api` before any use. No dataset download. No clone.

**Cemini posture:** FILE. **No PoC. No exploit steps. No command list.** Defensive framing only. **0 product Integrate GO.**
