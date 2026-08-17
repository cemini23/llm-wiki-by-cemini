---
title: "Demystifying Agent Skills: Why They Work—Until They Don't (arXiv 2608.14036)"
type: source
tags: [arxiv, skills, ccc, k240]
keywords: [procedural-anchoring, skill-retrieval, SKILL.md, misevolution, library-cap]
related:
  - concepts/agent-skills-procedural-anchoring.md
  - concepts/skill-misevolution.md
  - sources/arxiv-2608.12851-skill-misevolution-2026-08-14.md
  - entities/tools/addyosmani-agent-skills.md
  - sources/arxiv-2608.13926-never-the-number-2026-08-17.md
maturity: draft
created: 2026-08-17
updated: 2026-08-17
read_status: read
---

## Relations

- @concepts/agent-skills-procedural-anchoring.md — synthesized steal
- @concepts/skill-misevolution.md — three lifecycle gates; no unattended evolve
- @sources/arxiv-2608.12851-skill-misevolution-2026-08-14.md — pair paper (skills get worse with practice)
- @entities/tools/addyosmani-agent-skills.md — already K223; do not re-tier

## Raw Concept

| Field | Value |
|-------|--------|
| Paper | arXiv:2608.14036, "Demystifying Agent Skills: Why They Work—Until They Don't" |
| Authors | Zhiyuan Jiang, Fangrui Huang, Hanwen Xing, Xander Wu, Yipeng Gao, Rui Cao, Mengdi Wang, Shilong Liu, Yijiang Li (Princeton / UCSD / Stanford / USC / JHU) |
| Retrieved | 2026-08-17 |
| File | `arxiv-2608.14036-demystifying-agent-skills-why-they-work-until-th.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.14036-demystifying-agent-skills-why-they-work-until-th.pdf` |
| Type | cs.AI preprint, 28pp |
| Dual-ID | **OSINT K240**. **CCC K240** = robotics solver (old). CCC `/route` owns skill-library ops. |

## Narrative

Skills work when they convert noisy prior trajectories into compact **procedural anchors**, not when they dump facts. Controlled experiments (8,135 trial records; 238 unique labels) isolate representation, outcome annotation, retrieval difficulty, and cross-framework robustness.

### Key results `[TENTATIVE]`

- Skills beat Workflow Memory by **6.06 points** in matched comparisons.
- **Procedural anchoring accounts for 65.7%** of skill-use cases vs **4.5%** for explicit knowledge injection.
- Retrieval is a separate bottleneck: as the candidate pool grows **5 → 100**, actual-use precision falls **29.6% → 3.3%**.
- Confusable distractors impair offline identification; downstream success can still be stable — exact ground-truth invocation is neither sufficient nor necessary.
- Skills fail under brittle assumptions, incompatible contexts, or insufficient adaptation.

### Steal for CCC / OSINT

Treat `SKILL.md` as a procedure (what to do, what to check, what to avoid), not a knowledge wiki. Keep a library cap + retirement (pairs misevolution three gates). **No unattended auto-evolve** of `.cursor/skills/*`. Retrieval precision collapsing with pool size is the operational reason to retire unused skills.

## Snippets

> "Procedural anchoring accounts for 65.7% of skill-use cases, versus 4.5% for explicit knowledge injection, showing that skills stabilize action rather than inject missing facts." [Source: arxiv-2608.14036 abstract]

> "as pools grow from 5 to 100, actual-use precision falls from 29.6% to 3.3%." [Source: arxiv-2608.14036 abstract]
