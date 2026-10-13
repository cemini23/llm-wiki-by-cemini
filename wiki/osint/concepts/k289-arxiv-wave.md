---
title: K289 arXiv Wave — vol hedging, agent orchestration, MCP fuzzing (Oct 2026)
type: source-hub
tags: [k289, arxiv, options, quant, agents, orchestration, security, mcp]
keywords: [k289, flex-options, rough-heston, attention-mlp, tofu, mcp-fuzzing, porchestra, hma, a-saw, margos]
related:
  - concepts/k289-feeds-wave.md
  - concepts/k288-arxiv-wave.md
  - concepts/agent-authorization-stack.md
  - sources/arxiv-2610.13044-fomo-flex-options-2026-10-12.md
  - sources/arxiv-2610.13078-attention-mlp-refusal-2026-10-12.md
  - sources/arxiv-2610.13485-proactive-agentic-orchestration-2026-10-12.md
  - sources/arxiv-2610.13494-humanize-mle-agents-2026-10-12.md
  - sources/arxiv-2610.13543-three-options-rough-heston-2026-10-12.md
  - sources/arxiv-2610.13647-a-saw-agentic-software-architecture-2026-10-12.md
  - sources/arxiv-2610.13651-tofu-orchestrator-fuzzing-2026-10-12.md
  - sources/arxiv-2610.13772-margos-2026-10-12.md
  - concepts/k290-arxiv-wave.md
  - sources/arxiv-2610.12813-vepa-verified-evolving-guardrails-2026-10-13.md
  - sources/arxiv-2610.12758-distressbench-2026-10-13.md
maturity: draft
created: 2026-10-12
updated: 2026-10-12
harness_verb: FILE
wire_status: policy_wired
---

## Relations

- @concepts/k289-feeds-wave.md
- @concepts/k288-arxiv-wave.md
- @concepts/agent-authorization-stack.md
- @sources/arxiv-2610.13044-fomo-flex-options-2026-10-12.md
- @sources/arxiv-2610.13078-attention-mlp-refusal-2026-10-12.md
- @sources/arxiv-2610.13485-proactive-agentic-orchestration-2026-10-12.md
- @sources/arxiv-2610.13494-humanize-mle-agents-2026-10-12.md
- @sources/arxiv-2610.13543-three-options-rough-heston-2026-10-12.md
- @sources/arxiv-2610.13647-a-saw-agentic-software-architecture-2026-10-12.md
- @sources/arxiv-2610.13651-tofu-orchestrator-fuzzing-2026-10-12.md
- @sources/arxiv-2610.13772-margos-2026-10-12.md
- @concepts/k290-arxiv-wave.md
- @sources/arxiv-2610.12813-vepa-verified-evolving-guardrails-2026-10-13.md
- @sources/arxiv-2610.12758-distressbench-2026-10-13.md

## Raw Concept

K289 arXiv cluster hub. **8 papers.** Dual-ID **OSINT K289**. Split: **2 quant**, **4 agent orchestration/eval**, **1 safety**, **1 tooling**.

## Narrative

### The two quant papers

- **`2610.13044` FOMO — FLEX options.** The first direct event study of whether **single-name FLEX option activity leaks a footprint** into listed options and equities. Matched-control DiD: post-event **listed-option OI rises** (β=0.3061, p=0.0042); selection into high IV (β=0.1235); the **IV−RV spread predicts short-straddle P&L** (β=0.0366); a short-lived equity CAR effect (−0.85%). **The honest read: FLEX is a marker of institutional vol demand, not a directional predictor.**
- **`2610.13543` Three options are roughly enough.** In the **rough Heston** model, semi-static variance-optimal hedging of a variance swap via the **Galtchouk–Kunita–Watanabe** decomposition: **three static vanillas cut the hedging error by >95%** vs a purely dynamic hedge, across H ∈ {0.1, 0.3, 0.5}. **The strike choice depends on the Hurst index.**

**Both are desk-relevant. No trade. No scp.**

### The agent-orchestration cluster (4)

- **`2610.13485` POrchestra.** **Sub-agents proactively interrupt the orchestrator** to request harness adjustments; **OPOD** attributes each revision request to the preceding orchestration decision (process supervision). **+9.1% success**; +10.0% for a small orchestrator.
- **`2610.13494` Humanize MLE Agents.** Names **long-horizon deceleration** and **harness staleness**; fixes them with **context-reset session alternation** (CR-SMDP). **MLE-bench SOTA 78.2%** — +8.0 pts over the best open-source baseline **at ¼ the budget**.
- **`2610.13647` A-SAW.** An IDE agent drafts **architecture documentation** from a C4 model behind a **mandatory review gate**. **Author variance collapses SD 19.2 → 3.8**; **11/13 practitioners rejected unreviewed output.**
- **`2610.13772` MARGoS.** Reproducibility discipline for ARGoS/MARL — config hashing, seed propagation, frozen configs, exportable bundles. **Weakest fit; the checklist transfers.**

### Safety and security

- **`2610.13078` Attention sees, MLP refuses.** **Perception and decision are separate stages**: attention carries harmfulness, MLP writes refusal. Joint P–D conditional routing beats single-signal routing. **A model can recognise harm and not refuse.**
- **`2610.13651` ToFu (the headline).** Tool arguments from an LLM are **untrusted**. The **Repeat-After-Me** attack: feed tool-call-shaped text, ask the model to repeat it, the orchestrator dispatches it. **ToFu** fuzzes with semantics-aware oracles derived from tool metadata — **253 verified bugs across 343 tools in 118 servers** (of 273 MCP servers / 3,405 tools). **~42% server hit rate. No PoC.**

### The through-line

Two threads, both already in the wiki: **the harness is the part that ages** (harness staleness, HMA; harness transfer, K288 CoTrace), and **the oracle must come from semantics, not a model** (ToFu's sanitizer corpus, NOMOS's static RESOLVE).

### Boundary

**FILE only. No install. No clone.** ToFu and the safety paper carry **no PoC**. The quant papers carry **no trade**.

### Distribution

- Quant (FLEX, rough Heston) → xsp lane awareness; **no xsp scp**.
- Orchestration (POrchestra, HMA, A-SAW) + MARGoS → `../Cemini claude code CCC/briefs/2026-10-12_k289-agent-orchestration.md`
- ToFu + attention/MLP → `../Cybersecurity wiki/briefs/2026-10-12_k289-mcp-trust-boundary.md`
