---
title: "A Self-Evolving Multi-Agent Framework Defense against LLM Jailbreak Attacks (arXiv 2608.26008)"
type: source
tags: [arxiv, agent-safety, jailbreak-defense, cyber, k249]
keywords: [rule-memory, method-level-wrapper, test-time-defense, AutoDefense, AegisLLM, XSTest]
related:
  - concepts/k249-cyber-agent-safety-wave.md
  - concepts/self-evolving-runtime-defense.md
maturity: draft
created: 2026-08-29
updated: 2026-08-29
read_status: read
---

## Relations

- @concepts/k249-cyber-agent-safety-wave.md — K249 cyber cluster
- @concepts/self-evolving-runtime-defense.md — HARD harness-evolution sibling (black-box rule memory vs policy/gate evolvers)

## Raw Concept

| Field | Value |
|-------|--------|
| Paper | arXiv:2608.26008, "A Self-Evolving Multi-Agent Framework Defense against LLM Jailbreak Attacks" |
| Authors | Tongyan Hu, Bryan Hooi (NUS) |
| Retrieved | 2026-08-29 |
| File | `arxiv-2608.26008-a-self-evolving-multi-agent-framework-defense-ag.pdf` |
| sha256 | `ab006fa81b4d6e483c624f3a533188fe0b766311b40fb4582c4af2642ab89a58` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.26008-a-self-evolving-multi-agent-framework-defense-ag.pdf` |
| License | CC BY 4.0 (arXiv) |
| Type | cs.CR preprint, 16pp |
| Dual-ID | **OSINT K249** = this inbox |

## Narrative

Black-box **test-time** defense. When a jailbreak succeeds, the system abstracts the **structural attack wrapper** (nested role-play, code obfuscation) into a reusable method-level rule. Rules live in external memory. No parameter updates. Works on open-weight and API models.

Four prompted modules implement the memory loop: rule trigger (A1), policy decision (A2: ALLOW / SOFT_REFUSE / HARD_REFUSE), response generation (A3), self-reflection (A4). The paper says the contribution is the **persistent rule memory**, not the agent split.

### Results (Table 1, ASR-rej / ASR-gpt)

On DeepInception / CodeChameleon / ReNeLLM / FlipAttack vs Qwen2.5-7B, Llama3.1-8B, Gemini-3-Flash-Preview, "Ours" drops ASR well below AutoDefense / Self-reminder / DefensePrompt. Example: CodeChameleon Qwen 98.0/57.0 (NoDefense) → 4.5/1.4 (Ours). MMLU / GSM8K utility stays close to the undefended baseline.

XSTest over-refusal (Qwen2.5-7B, Table 2): empty memory 3.6% → accumulated four-family memory 9.6%. Residual is classifier mislabel of homonym traps ("kill a process"). `[TENTATIVE]` — single-paper numbers.

No public GitHub in the PDF. **No clone. No jailbreak PoC in this wiki.** Phase-0: none (paper, not Adopt/GO repo).

### Steal (cyber lab / CCC policy)

Store **wrapper-level** refusal rules, not topic keywords. Trigger at most K=2 rules. Gate hard-refuse on executable harm / hidden-intent decrypt. Do **not** unattended-evolve skills from these traces (`@concepts/skill-misevolution.md`). Pairs HARD: HARD evolves harness policy/gate from traces; this paper evolves an external method-level memory with no weight updates.

## Snippets

> "the contribution is the memory-based adaptation mechanism, not the module decomposition." [Source: arxiv-2608.26008.pdf p.1]

> "each rule captures the structural attack wrapper … rather than the harmful topic, so a single rule induced from one instance generalizes across an entire attack family" [Source: arxiv-2608.26008.pdf p.2]
