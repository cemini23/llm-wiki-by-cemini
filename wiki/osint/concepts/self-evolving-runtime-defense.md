---

title: "Self-evolving runtime defense (HARD) — harness-based autonomous defense evolution"
type: concept
tags: [concept, agent-safety, defense-evolution, cyber, harness, k237]
keywords: [HARD, harness-based defense, security policy, execution gate, AgentCanary, AgentHazard, runtime defense]
related:
  - sources/arxiv-2608.12977-self-evolving-security-2026-08-14.md
  - concepts/skill-misevolution.md
  - concepts/agent-setup-instruction-supply-chain.md
  - entities/tools/cyberscraper-2077.md
  - sources/arxiv-2608.13560-autodesign-2026-08-14.md
  - sources/arxiv-2608.26008-self-evolving-jailbreak-defense-2026-08-29.md
  - concepts/k249-cyber-agent-safety-wave.md
maturity: draft
created: 2026-08-14
updated: 2026-08-29

---

## Relations

- @sources/arxiv-2608.12977-self-evolving-security-2026-08-14.md — primary source
- @concepts/skill-misevolution.md — offensive mirror
- @concepts/agent-setup-instruction-supply-chain.md — setup-instruction risk sibling
- @sources/arxiv-2608.26008-self-evolving-jailbreak-defense-2026-08-29.md — K249 black-box method-level rule memory (no weight updates)
- @concepts/k249-cyber-agent-safety-wave.md — K249 cluster

## Raw Concept

What this page answers: static handcrafted runtime defenses can't keep pace with an open-ended adaptive attack space — how does a deployed LLM agent's defense improve itself from observed failure traces? Synthesized from HARD (2608.12977).

## Narrative

HARD = **Harness-based Autonomous Runtime Defense Evolution**. Model the agent as A=(Mθ, H) with harness H=(ϕH, ψH): **context construction ϕH** (what the model sees) and **action interpretation ψH** (how outputs become actions). Runtime defense = optimize over harnesses: argmax E[J_safe + λ·J_util].

### The loop

1. Sample attack tasks → collect trajectories under current harness.
2. Identify failures (J_safe < δs or J_util < δu).
3. LLM trace router classifies each failure to a defense slot (**policy** = context side, or **gate** = action side).
4. Each evolver updates its artifact (minimize Δ(H, H′) subject to resolving failures).
5. Reassemble + redeploy; re-test on held-out split.

### Key findings

- HARD-Both: DPI 12.1%, IPI 1.3%, MC 13.9%, SP 7.4% ASR, BU 91.0–97.0%; beats handcrafted (13–66% ASR, attack-specific). *(Table vs main-text numbers differ — `[NEEDS VERIFICATION 2026-08-29]`. K249 did not re-measure.)*
- Under multi-turn adaptive attacks **policy-only can beat joint** — the two artifacts are not uniformly additive.
- **Gate rules memorize attacks, generalize poorly** (0→97 rules, test split 28.9→26.5). Literal patterns rot — push for anti-obfuscation/cumulative-intent abstractions.
- Over-restriction is a failure mode: GPT-5.5 backbone "succeeded" at correction while wrecking utility (UA 7.2).

### Guardrails to port (cyber lab / operator stack)

Deterministic train/test splits; evolve per attack category; conservative routing (gate only high-confidence, low-FP, pre-execution-matchable patterns; <0.55 confidence → policy); batch failures (8 traces) for shared-structure repair; gate rules match **dangerous action shape** never staging paths; module-specific views to prevent benchmark memorization; temp 0; separate `security_awareness` diagnostic (recognized-but-executed vs never-recognized need different repair surfaces).

**Offense-side lessons**: defense exemptions gated on framing/self-asserted auth are exploitable; variable-splicing/cross-turn obfuscation defeats literal gate predicates — both ready-made red-team techniques.

### K249 sibling (black-box rule memory)

2608.26008 is a **test-time** self-evolving defense that stores wrapper-level rules in external memory (no parameter updates). HARD evolves harness policy/gate from traces. Use both as policy: method-level wrappers in memory; do not grow literal gate rules that memorize attacks. No clone this wave.
