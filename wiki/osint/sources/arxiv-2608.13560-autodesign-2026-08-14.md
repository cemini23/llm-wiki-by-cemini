---

title: "AutoDesign: Meta-Harness Optimization for Long-Horizon Agentic Design (arXiv 2608.13560)"
type: source
tags: [arxiv, agent-harness, meta-optimization, ccc, autodesign, k237]
keywords: [AutoDesign, DesignHarness, meta-harness, harness optimization, PosterBench, five components, acceptance gate]
related:
  - concepts/agent-harness-verification-bottleneck.md
  - concepts/skill-misevolution.md
  - concepts/self-evolving-runtime-defense.md
  - sources/arxiv-2608.13522-vero-2026-08-14.md
  - sources/arxiv-2608.12851-skill-misevolution-2026-08-14.md
  - sources/arxiv-2608.12977-self-evolving-security-2026-08-14.md
  - sources/newsletter-rss-latent-space-2026-08-14-gemini-37-flash.md
maturity: draft
created: 2026-08-14
updated: 2026-08-14
read_status: read

---

## Relations

- @concepts/agent-harness-verification-bottleneck.md — harness-vs-model framing
- @concepts/skill-misevolution.md — skill/harness evolution risk sibling
- @concepts/self-evolving-runtime-defense.md — harness evolution defense side
- @sources/arxiv-2608.13522-vero-2026-08-14.md — Vero sibling (repository-scale verified-codegen)

## Raw Concept

| Field | Value |
|-------|--------|
| Paper | arXiv:2608.13560, "AutoDesign: Meta-Harness Optimization for Long-Horizon Agentic Design" |
| Authors | Yaxin Luo, Haobin Jiang, ..., Xiaotong Li (Meituan, MBZUAI, HUST, PKU, Tsinghua, CUHK, SJTU) |
| Retrieved | 2026-08-14 |
| File | `arxiv-2608.13560-autodesign-meta-harness-optimization-for-long-ho.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/` |
| Type | cs.CV preprint, 29pp |

## Narrative

Meta-harness optimization: an **outer loop recursively improves a "design harness"** (the system around a fixed LLM) from rollout feedback; an inner loop (the harness) generates and revises artifacts. Instantiated for paper-to-poster generation with **PosterBench** (100-paper Main Track) and a seven-dimensional rubric. Key claim: **optimize the harness, not model weights.**

### Architecture

- **Five functional components** of a design harness: Context & Memory, Tools & Specs, Execution Runtime, Orchestration, Evaluation & Feedback.
- Meta-objective H\* = argmax_H E[R_meta(y,x,c)], model fixed throughout.
- Outer loop: rollout → evaluation → update proposal → **acceptance gate** (Accept(H') ⇔ J_train(H') > J_train(H) ∧ J_dev(H') ≥ J_dev(H)) — dev set never exposed to the optimizer P. Planner dispatches parallel subagents to inspect trajectories, synthesizes recurrent-failure evidence, changes **exactly one component per iteration** (credit assignment). Optimization record L persists as optimizer context.
- **Human-in-the-loop**: NL guidance can redirect the planner; evaluator revision requires explicit human input.

### Key results

- PosterBench Main Track: AutoDesign (Claude Code + Claude 4.8) = **78.32**, beating Claude Design (70.87) by 7.45 and OpenDesign (69.45) by 8.87.
- Harness-attachment ablation across 7 model/configs: **+12.40 points average** (+5.01 to +19.56; DeepSeek V4 Pro +19.56).
- Fully autonomous run: **253 tool calls, 11 editing turns, 40 minutes, <$3**. Pareto: LongCat $0.27/55.13 → Claude 4.8 $7.63/74.56 → GPT-5.5 $10.02/81.46. **Harness quality can substitute for model quality.**
- Meta-harness scale: 224 subagents, ≥123 recursive iterations, 54 harness updates over 7 days. Trajectory 49.00 → 80.88 autonomous plateau → **88.39 with human redirection**.
- Human study: AutoDesign Bradley–Terry preference 64.0%; per-poster benchmark-human alignment r=0.34.

### Steal-for-CCC / /route backlog

- **Five-component harness decomposition** as a clean audit taxonomy for a Claude Code agent harness (map skills/hooks/MCP/session loop onto it).
- **Meta-harness optimization loop** transfers to improving Claude Code skills/commands: train task set + hidden dev set, one bounded update per iteration, promote only when train improves AND dev doesn't regress. The optimization record (checkpoint + evidence per iteration) as persistent optimizer context is directly reusable.
- **Planner + code-editor split** with parallel trajectory-inspection subagents; **one-component-per-iteration** credit assignment.
- **HITL redirection on plateau**: autonomous stalls at 80.88, NL nudge → 88.39. Anti-overfitting acceptance gate = harness-level held-out split.
- DesignHarness inner loop: provenance-aware ingestion → editable artifact → deterministic **blocking validator** + VLM critic → localized repair → finalize best valid candidate (K=12 attempt budget).

**Briefs:** CCC `/route` backlog (meta-harness canon). Tier: `[TENTATIVE]` — preprint; concrete, reusable protocol.
