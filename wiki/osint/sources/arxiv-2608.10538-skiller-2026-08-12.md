---
title: "SKILLER — Language-Level RL for Reusable Skill Extraction in Small LMs"
type: source
tags: [arxiv, k233, ccc, agent-skills, rl]
keywords: [2608.10538, skill-extraction, reinforcement-learning, small-language-model, agent-skills, qwen]
related:
  - entities/tools/skiller.md
  - concepts/agent-skill-rl-extraction.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-08-12
updated: 2026-08-12
read_status: skimmed
---

## Relations

- @entities/tools/skiller.md — Phase-0 NO-GO clone (NOASSERTION SPDX), research-reference only
- @concepts/agent-skill-rl-extraction.md
- @concepts/cemini-license-posture.md
- @ccc-wiki/briefs/2026-08-12_k233-skiller-rollout-scheduling.md (cross-wiki brief)

## Raw Concept

| Field | Value |
|-------|--------|
| arXiv | 2608.10538 |
| sha256 | `80fa5ef0ef8feb8025da244afda2b7a821d8da90dba196e4a16733e76fda201f` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.10538-skiller-language-level-reinforcement-learning-fo.pdf` |
| retrieved | 2026-08-12 |
| authors | Chenhao Dang, Siyuan Xiong, Conghui He, Weijia Li (SJTU, Shanghai AI Lab, HIT-Shenzhen, Tsinghua) |

## Narrative

SKILLER treats agent skills as a **standardized packaging format for procedural knowledge and tool-use conventions** that constrains an LM's behavior space for repeatable high-quality task execution. The motivating gap: strong closed-source models are expensive for skill execution, while open small models need executor-specific skills that naive prompt-writing doesn't produce.

The framework is a natural-language-driven RL loop: a **strong model serves as actor and critic**, the **small-model agent system is the environment**, and all RL signals propagate through natural language (no gradient flow). This is notable because it decouples skill acquisition from model internals — the skill artifact itself is language.

Results on Qwen3.5-9B and Qwen3.5-4B across five benchmarks: absolute gains of 4.3–20.4pp (9B) and 1.8–13.3pp (4B) over three open-source and one closed-source skill generation/evolution baseline; matches strong closed-source models on single-skill tasks in SkillsBench. Repo: `github.com/DANG-ai/SKILLER`.

**Phase-0 verdict: NO-GO clone** — `DANG-ai/SKILLER` reports `NOASSERTION` SPDX (no LICENSE file detectable via gh api), 1 star, ~1.5MB. Research-reference only for CCC `/route` and Atto skill-harness methodology; do not adopt binary/weights. Pattern steal: RL-via-natural-language as a skill-authoring loop is directly reusable for generating `/route`-style skills for small local models.

[Source: arXiv:2608.10538]
