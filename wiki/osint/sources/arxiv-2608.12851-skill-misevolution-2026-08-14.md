---
title: "Practice Makes Unsafe: Skill Misevolution in Self-Improving LLM Agents (arXiv 2608.12851)"
type: source
tags: [arxiv, agent-safety, skill-evolution, ccc, cyber, she, k237]
keywords: [skill misevolution, SKILLMISEVO-GYM, SKILLMISEVO-BENCH, SAFEEVOLVE, self-improving agents, skill poisoning, C-ASR]
related:
  - concepts/skill-misevolution.md
  - concepts/agent-skill-rl-extraction.md
  - concepts/agent-setup-instruction-supply-chain.md
  - sources/arxiv-2608.12977-self-evolving-security-2026-08-14.md
  - sources/arxiv-2608.13560-autodesign-2026-08-14.md
maturity: draft
created: 2026-08-14
updated: 2026-08-14
read_status: read
---

## Relations

- @concepts/skill-misevolution.md — the lifecycle-gate framework (authoring/retrieval/execution)
- @concepts/agent-skill-rl-extraction.md — K233 SKILLER sibling (generation vs misevolution)
- @concepts/agent-setup-instruction-supply-chain.md — K236 promptware/setup-instruction risk
- @sources/arxiv-2608.12977-self-evolving-security-2026-08-14.md — defensive mirror (HARD)
- @sources/arxiv-2608.13560-autodesign-2026-08-14.md — self-improving harness context

## Raw Concept

| Field | Value |
|-------|--------|
| Paper | arXiv:2608.12851, "Practice Makes Unsafe: Skill Misevolution in Self-Improving LLM Agents" |
| Authors | Xutao Mao, Liangjie Zhao, Xiang Zheng, Cong Wang (City University of Hong Kong; Adelaide University) |
| Retrieved | 2026-08-14 |
| File | `arxiv-2608.12851-practice-makes-unsafe-skill-misevolution-in-self.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/` |
| Type | cs.AI preprint, 21pp, code `github.com/henrymao2004/misevolve` |

## Narrative

Defines **skill misevolution**: a self-improving agent converts a "successful" trajectory containing an unsafe shortcut into a persistent reusable skill (SKILL.md), which later causes harm in fresh sessions after the original attack input is gone. Delivers three artifacts:

- **SKILLMISEVO-GYM** — lifecycle-aware harness: versions skill state, isolates conversation/workspace/native-memory, replays clean-session reloads.
- **SKILLMISEVO-BENCH** — frozen 21-task benchmark from autoresearch-discovered vulnerability concepts (VC1 label-conditioned unsafe reuse, VC2 dual-use boundary loss, VC3 compositional completion spillover).
- **SAFEEVOLVE** — method-agnostic governance wrapper.

### Key results

- All 21 evolved configurations author unsafe artifacts; 19 retrieve unsafe skills; 19 show contamination; **15 retain fresh-session harm**. No-Evolution stays near zero. This attenuation is the "misevolution signature."
- Coexistence not tradeoff: BU higher than No-Evolution in 15/21 settings, M-ASR higher in 17.
- Exposure sweep: pooled C-ASR rises 16.0% → 35.3% after one 3-malicious-task round, reaching 41.3% at full budget. **Benign updates do not reliably erase learned risk**; early exposure widens the contamination window.
- SAFEEVOLVE (OpenClaw): authored-artifact risk 37.37% → 18.80%; URR 35.33% → 8.67%; C-ASR 21.33% → 4.00%; BU essentially unchanged (58.44 → 58.00). Paired deleter (delete-only repair) is the key component; attribution covers 108/110 harmful outcomes; without retirement, threshold-crossing skills get re-retrieved and URR doubles.

### Drift mechanisms (the "how skills get worse" core)

- **VC1**: unsafe body attaches to a benign label ("monitoring/telemetry/setup"), abstracted as the trigger.
- **VC2**: safety-critical boundary (provenance, data scope, granted capability) dropped while the reusable template is kept.
- **VC3**: full collection→processing→transmission chain packaged as one procedure so later benign work "completes" the omitted harmful steps.
- Every evolution method has a **self-reinforcing in-place-edit path** that accumulates the shortcut. Runtime refusal + utility-only hygiene are insufficient — they neither inspect learned state nor connect it to later outcomes.

### Steal-for-CCC / SHE

This is a direct blueprint for a Claude Code skill library (SKILL.md is literally the artifact under study). Governance belongs at **write and reuse boundaries**: critic-localized delete-only repair (never add guards), lineage on retrieval, retirement on evidenced harm (2 harmful reuses), capacity eviction by utility-minus-risk, library cap. **HITL approval on a skill's write does not check whether later retrieval activates an unsafe span** — need retrieval lineage + retirement. **SHE eval**: skills can get worse with practice → promote/refine under eval-gate with benign-utility + harm judges decoupled.

**Briefs:** CCC `/route` (skill misevolution), cyber (misevolution as offense-side poisoning templates). Tier: `[TENTATIVE]` — fresh preprint, but methodology is concrete and the lifecycle-gate framing is directly actionable.
