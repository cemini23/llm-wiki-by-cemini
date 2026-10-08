---
title: K285 arXiv Wave — harness co-evolution, safety repair, historical OCR (Oct 2026)
type: concept
tags: [k285, arxiv, agents, harness, safety, ocr, robotics, game-theory]
keywords: [k285, risk-averse-mfg, inscriptionocr, patchbench, task-progress-distillation, sldr, cotrace, base-model-screening, embodiedrsi]
related:
  - concepts/k285-eval-wave.md
  - concepts/k285-feeds-wave.md
  - concepts/agent-tool-use-verification.md
  - sources/arxiv-2610.09244-risk-averse-mp-mfg-2026-10-08.md
  - sources/arxiv-2610.09439-inscriptionocr-2026-10-08.md
  - sources/arxiv-2610.10276-patchbench-2026-10-08.md
  - sources/arxiv-2610.10332-task-progress-distillation-2026-10-08.md
  - sources/arxiv-2610.10345-sldr-2026-10-08.md
  - sources/arxiv-2610.10426-cotrace-2026-10-08.md
  - sources/arxiv-2610.10478-base-model-screening-2026-10-08.md
  - sources/arxiv-2610.10498-embodiedrsi-2026-10-08.md
maturity: draft
created: 2026-10-08
updated: 2026-10-08
harness_verb: FILE
wire_status: policy_wired
---

## Relations

- @concepts/k285-eval-wave.md
- @concepts/k285-feeds-wave.md
- @concepts/agent-tool-use-verification.md
- @sources/arxiv-2610.09244-risk-averse-mp-mfg-2026-10-08.md
- @sources/arxiv-2610.09439-inscriptionocr-2026-10-08.md
- @sources/arxiv-2610.10276-patchbench-2026-10-08.md
- @sources/arxiv-2610.10332-task-progress-distillation-2026-10-08.md
- @sources/arxiv-2610.10345-sldr-2026-10-08.md
- @sources/arxiv-2610.10426-cotrace-2026-10-08.md
- @sources/arxiv-2610.10478-base-model-screening-2026-10-08.md
- @sources/arxiv-2610.10498-embodiedrsi-2026-10-08.md

## Raw Concept

K285 arXiv cluster hub. **8 papers**, Dual-ID **OSINT K285**. Split: **1 quant**, **3 safety/eval**, **3 agent-harness**, **1 robotics**.

## Narrative

### The two recurring themes

**Theme A — harness–model co-evolution (papers 4, 6, 8).**

- **`2610.10426` CoTrace** — a trajectory's training value **depends on the harness that made it**. Pooling trajectories across harnesses disconnects training from the deployed runtime. CoTrace routes trajectories with a **harness fingerprint**. Qwen3.5-9B on Tmax: **78 → 90**, at **30–50 trajectories/iteration** vs 149–308. **OOD caveat: gains vanish under a foreign runtime.**
- **`2610.10332` TPD (Task-Progress Distillation)** — label each action with a task **stage**, then **score** stage–action pairs instead of imitating traces. **At 200 demos: 67.7% vs 48.0% (+19.7 pp)** on ALFWorld.
- **`2610.10498` EmbodiedRSI** — a robotics harness that picks the next experiment by **Value-of-Information**. **RoboCasa365 Composite-Unseen 71.3% vs 40.1%**; zero-shot sim-to-real **46% → 71%**.

**Theme B — measuring and repairing model behaviour (papers 3, 5, 7).**

- **`2610.10276` PatchBench** — activation patching can be **broad suppression**, not repair. MMLU can be **flat** while local regression is severe (**−26.3 BNPS** for −0.07 MMLU). Aggregate metrics are blind to local damage.
- **`2610.10345` SLDR** — malicious fine-tuning defence: layer safety sensitivity is **signed**; repair only the **two extreme layers** and route only malicious queries. **Harmful Score 11.54 → 0.08** near-losslessly.
- **`2610.10478` Before They Can Solve** — screen a base model by its **decisive step** (Decisive-Action BPB **ρ = 0.964**). **Bounded benchmarks anti-correlate** (HumanEval ρ = **−0.394**).

### The odd two out

- **`2610.09244` Risk-averse multi-population MFGs** — the only quant hook: AI-vs-human trader populations, risk averse to distributional ambiguity (reward 136.65 → 130.56, sensitivity 25.21 → 22.09). **No trade, no scp.**
- **`2610.09439` InscriptionOCR** — Ashokan **Brahmi** inscription OCR + Prakrit→English NMT (ResNet-50 100%; M2M-100 BLEU 56.4). **CC BY-NC 4.0.** Wrong script for Atto, right *pipeline shape*.

### The through-line

**Five of eight papers say the same thing from different angles: the harness, the runtime, and the local metric matter more than the headline number.** CoTrace (harness transfer), PatchBench (local vs aggregate), Before-They-Can-Solve (bounded benchmarks anti-correlate), TPD (stage-scored over trace-imitated), EmbodiedRSI (experiment where uncertainty is). This is the same doctrine the wiki's audit gates run on.

### Boundary

**FILE only. No install. No clone.** Safety papers carry **no PoC**. Quant paper carries **no trade**. `InscriptionOCR` is **CC BY-NC** — research only.

### Distribution

- Harness co-evolution (CoTrace, TPD, EmbodiedRSI) → `../Cemini claude code CCC/briefs/2026-10-08_k285-harness-coevolution.md`
- Safety repair (PatchBench, SLDR) → `../Cybersecurity wiki/briefs/2026-10-08_k285-model-repair-eval.md`
- Before-They-Can-Solve → CCC (base-model screening).
- InscriptionOCR → family-history research awareness.
- Risk-averse MFG → wiki-only (no xsp scp).
