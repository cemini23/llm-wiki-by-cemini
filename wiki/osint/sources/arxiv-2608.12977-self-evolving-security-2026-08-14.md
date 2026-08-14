---
title: "Beyond Handcrafted Security: Towards Self-Evolving Defense for LLM Agents (arXiv 2608.12977)"
type: source
tags: [arxiv, agent-safety, self-evolving-defense, cyber, harness, k237]
keywords: [HARD, harness-based defense evolution, AgentCanary, AgentHazard, runtime defense, security policy, execution gate]
related:
  - concepts/self-evolving-runtime-defense.md
  - concepts/skill-misevolution.md
  - sources/arxiv-2608.12851-skill-misevolution-2026-08-14.md
  - sources/arxiv-2608.13560-autodesign-2026-08-14.md
maturity: draft
created: 2026-08-14
updated: 2026-08-14
read_status: read
---

## Relations

- @concepts/self-evolving-runtime-defense.md — the HARD loop + guardrails
- @concepts/skill-misevolution.md — offensive mirror (same harness-evolution territory)
- @sources/arxiv-2608.12851-skill-misevolution-2026-08-14.md — offense/defense pair
- @sources/arxiv-2608.13560-autodesign-2026-08-14.md — meta-harness optimization family

## Raw Concept

| Field | Value |
|-------|--------|
| Paper | arXiv:2608.12977, "Beyond Handcrafted Security: Towards Self-Evolving Defense for LLM Agents" |
| Authors | Jiajun Ruan, Peiyang Li, Yukun Chen, Fengting Li, Chao Feng (U. Minnesota; Ant Group; Tsinghua; Zhejiang U.) |
| Retrieved | 2026-08-14 |
| File | `arxiv-2608.12977-beyond-handcrafted-security-towards-self-evolvin.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/` |
| Type | cs.CR preprint, 18pp |

## Narrative

**HARD (Harness-based Autonomous Runtime Defense Evolution)** — a framework that lets a deployed agent's defense improve itself from observed failure traces. Harness-centric formulation: agent A=(Mθ, H), harness H=(ϕH, ψH) with **context construction ϕH** (what the model sees) and **action interpretation ψH** (how outputs become actions). Runtime defense = argmax over harnesses of E[J_safe + λ·J_util]. Evolves two artifacts: a context-side **security policy** and an action-side **execution gate**, with LLM failure-trace routing + per-artifact evolvers. Three variants: HARD-Policy / HARD-Gate / HARD-Both.

### Key results (Table 1)

- HARD-Both ASR: DPI 12.1%, IPI 1.3%, MC 13.9%, SP 7.4%; BU 91.0–97.0%; UA MC 85.9%, SP 95.1%. *(Table vs main-text numbers differ — flag `[NEEDS VERIFICATION]`.)*
- Handcrafted defenses range ~13–66% ASR and are attack-specific (SecureClaw leaves DPI essentially unmitigated at 66.3%).
- Adaptive attacks: DAE — HARD-Both 26.5% vs strongest handcrafted 30.1%; LPA — HARD-Policy 4.8% vs 24.1%.
- Under multi-turn adaptive attacks **HARD-Policy can beat HARD-Both** — joint evolution not uniformly additive.
- Backbone ablation (MC): No-Evolution 63.9 ASR; GLM-5.2 13.9; Claude Opus-4.6 7.7/96.2 BU; GPT-5.5 20.3/94.9 BU but **UA 7.2** — over-restriction "success" that wrecks utility.
- Gate rules memorize observed attacks, generalize poorly (HARD-Gate grows 0→97 rules, test split only 28.9→26.5).
- IPI remains hard for every defense (UA <25% all cells).

### Steal-for-cyber-lab (concrete self-evolving defense loop)

1. Run attack tasks against harnessed agent → judge each trajectory (outcome ≤0.5 = attack success; keep `security_awareness` as diagnostic to separate recognized-but-executed from never-recognized → different repair surface: gate vs policy).
2. Route failures to a semantic-policy evolver or a tool-gate evolver → redeploy → re-test on held-out split.
3. Guardrails: deterministic train/test splits; evolve per attack category; conservative routing (gate only high-confidence, low-FP, pre-execution-matchable; <0.55 confidence → policy); batch failures (8 traces) for shared-structure repair; gate rules match **dangerous action shape** (`rm\s+.*\.so`, `curl\b.*-d\s+.*https?://`, `cat\s+.*~/.ssh/id_`) never staging paths; module-specific views to prevent benchmark memorization; temp 0.

### Steal-for-CCC / skill-engineering

Two-surface harness model (context construction vs action interpretation) maps onto Claude Code skill/agent engineering. Policy-evolver discipline: produce the **smallest set of general security invariants**, merge/generalize rather than append per-scenario refusals, never memorize task artifacts, scope every invariant to preserve benign utility (gate on authorization/provenance/consent, not blanket capability refusal). Case studies are ready-made red-team techniques: defense exemptions gated on framing/self-asserted auth, variable-splicing/cross-turn obfuscation that defeats literal gate predicates.

**Briefs:** cyber (self-evolving defense loop). Tier: `[TENTATIVE]` — numeric table/text discrepancy flagged; method concrete and independently checkable.
