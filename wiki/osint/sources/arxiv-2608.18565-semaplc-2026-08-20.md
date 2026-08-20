---
title: "SemaPLC — verification-gated agent harness for PLC code (arXiv 2608.18565)"
type: source
tags: [arxiv, harness, verification, ccc, k243]
keywords: [SemaPLC, PLC, verification-gated, IEC-61131, wont_wire]
related:
  - concepts/agent-harness-verification-bottleneck.md
  - concepts/continual-harness-online-self-improvement.md
  - concepts/cemini-license-posture.md
  - sources/arxiv-2608.19013-harness-continual-learning-2026-08-20.md
  - sources/newsletter-rss-latent-space-2026-08-20-glm53-harness.md
maturity: draft
created: 2026-08-20
updated: 2026-08-20
read_status: read
---

## Relations

- @concepts/agent-harness-verification-bottleneck.md — completion is logged external checks, not self-judge
- @concepts/continual-harness-online-self-improvement.md — guarded commit of harness state
- @concepts/cemini-license-posture.md — `midea-ai/SemaPLC` NOASSERTION; no clone
- @sources/arxiv-2608.19013-harness-continual-learning-2026-08-20.md — HCL proposal/eval/commit
- @sources/newsletter-rss-latent-space-2026-08-20-glm53-harness.md — harness as cost/diff surface

## Raw Concept

| Field | Value |
|-------|--------|
| Paper | arXiv:2608.18565, "SemaPLC: A Project-Grounded, Verification-Gated Agent Harness for PLC Code Generation" |
| Authors | Yanlun Tu et al. (Midea AIRC / KUKA / SJTU / ZJU) |
| Retrieved | 2026-08-20 |
| File | `arxiv-2608.18565-semaplc-a-project-grounded-verification-gated-ag.pdf` |
| sha256 | `7a853702207851b71e61f9e8f62bab4ae433c35804343433a207f2aa0b5553b6` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.18565-semaplc-a-project-grounded-verification-gated-ag.pdf` |
| Repo | https://github.com/midea-ai/SemaPLC — **NOASSERTION, no clone** |
| Dual-ID | **OSINT K243**. CCC OOD `wont_wire` (PLC industrial). |

## Narrative

SemaPLC is a project-grounded agent harness for programmable-logic-controller code. It does not stop when the model judges its own output adequate. Completion requires logged external checks covering specification, compilation, and **live runtime traces**. On 117 independent-POU tasks it reports the highest strict verified pass rate on all seven models (72.6% mean). On a 65-task project-context track, static scores cluster within ~10 points while **dynamic** scores separate baselines (22.4–31.4) from SemaPLC (52.2).

**Concrete claim `[TENTATIVE]`:** execution, not static scoring, is the faithful test of whether generated control logic works. CCC steal: verification-gated harness — worker ≠ verifier. **PLC runtime is OOD.** `wont_wire`. No clone (NOASSERTION). Do not auto-evolve `.cursor/skills/*` from this paper.

## Snippets

> "Rather than stopping when the model judges its own output adequate, SEMAPLC declares a task complete only when logged external checks confirm it." [Source: arxiv-2608.18565 abstract]
