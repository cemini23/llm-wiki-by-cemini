---
title: "SkillLens — Visual Skill Cards for Retrieval-Augmented GUI Action Prediction"
type: source
tags: [arxiv, k233, ccc, gui-agents, vlms]
keywords: [2608.10775, visual-skill-cards, gui-agents, computer-using-agents, distill, vlm, procedural-memory]
related:
  - entities/tools/skilllens.md
  - concepts/gui-procedural-memory.md
maturity: draft
created: 2026-08-12
updated: 2026-08-12
read_status: skimmed
---

## Relations

- @entities/tools/skilllens.md
- @concepts/gui-procedural-memory.md
- @ccc-wiki/briefs/2026-08-12_k233-skiller-rollout-scheduling.md (cross-wiki brief — skill representation family)

## Raw Concept

| Field | Value |
|-------|--------|
| arXiv | 2608.10775 |
| sha256 | `40cb648eba3d0e802402d06cd075f3c16e70722798d81a4bac1e52b75fbf0be2` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.10775-skilllens-visual-skill-cards-for-retrieval-augme.pdf` |
| retrieved | 2026-08-12 |
| authors | Zhou Liu, Ligang Huang, et al. (Peking Univ., ByteDance, SJTU) |

## Narrative

Computer-using agents (CUAs) perceive rich GUI state but lack **visual procedural memory** — they recognize controls without knowing which workflow is active, which control matters next, or what evidence confirms progress. Text-only skills omit the visual state that makes a procedure applicable.

**Visual Skill Cards (VSCs)** are a state-conditioned memory representation binding reusable procedures with (a) applicability cues, (b) visual evidence, and (c) verification signals. SkillLens builds VSCs from heterogeneous interaction traces (Trace-to-Visual-Skill-Card), then at inference retrieves relevant cards and selectively expands only the evidence a fixed VLM executor needs. **CardDistill** uses VSC evidence as privileged teacher context to train a student that acts *without* runtime card retrieval.

Results: SkillLens improves frozen GPT-5.4-mini executor by +11.6 Step SR (Multimodal-Mind2Web) and +2.9 Overall (WebLINX-BrowserGym); CardDistill improves Qwen3-VL-2B student-only metrics by +12.0 / +3.2.

Relevance: (1) CCC skill-harness family — VSC ≈ a *visual* counterpart to text agent skills (SKILLER/K233 sibling); (2) Atto/GUI automation angle — Antenati/portal cassette workflows are GUI-heavy; a distilled student could click through archives locally. No public repo at Phase-0 check — pattern-only.

[Source: arXiv:2608.10775]
