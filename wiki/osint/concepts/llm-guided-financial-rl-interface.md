---
title: LLM-guided financial RL — state-reward interface design
type: concept
tags: [concept, financial-rl, llm, reward-shaping, low-snr, portfolio]
keywords: [gift, fpqc-sac, financial-entropy-trap, state-reward-interface, ppo, sac, low-snr]
related:
  - sources/arxiv-gift-llm-state-reward-2606.08450-2026-06-11.md
  - sources/arxiv-fpqc-sac-quantum-finrl-2606.10448-2026-06-11.md
  - concepts/llm-agent-systems.md
  - entities/tools/gift-finrl.md
  - entities/tools/fpqc-sac.md
  - entities/tools/pandaai.md
  - sources/arxiv-pandaai-neuro-symbolic-quant-2606.06823-2026-06-12.md
maturity: draft
created: 2026-06-11
updated: 2026-06-11
---

## Relations

- @sources/arxiv-gift-llm-state-reward-2606.08450-2026-06-11.md — GIFT guided LLM interface design
- @sources/arxiv-fpqc-sac-quantum-finrl-2606.10448-2026-06-11.md — representation-bottleneck stabilization
- @concepts/llm-agent-systems.md — constrained LLM roles (design vs execute)
- @entities/tools/gift-finrl.md — NO-GO adoption
- @entities/tools/fpqc-sac.md — NO-GO adoption

## Raw Concept

K111 ingest cluster: financial markets as **low-SNR** sequential decision problems where raw OHLCV + short-horizon return under-specifies learning. Two complementary stabilization axes from Jun 2026 papers.

## Narrative

| Axis | Paper | Mechanism | Cemini posture |
|------|-------|-----------|----------------|
| Interface design | GIFT (2606.08450) | LLM builds factor + risk-rule features and aux rewards; DGR from PPO diagnostics | REFERENCE — offline env design; repo NO-GO |
| Representation | FPQC-SAC (2606.10448) | PQC front-end before SAC actor/critic; mitigates Financial Entropy Trap | REFERENCE — skeptical on quantum prod path; repo NO-GO |

**Shared lesson:** stabilize **before** Bellman bootstrapping — either via guided state/reward engineering (GIFT) or representation constraints (FPQC). Output-side Q clipping alone is late intervention.

Not a prod adoption track for CeminiSuite equity/PM stacks in K111 — informs research briefs and future FinRL env experiments only.

## Snippets

> "The effectiveness of this learning process depends critically on the state-reward interface provided to the agent."

> — [Source: arxiv-2606.08450-gift-llm-guided-state-reward-interface-for-finan.pdf, retrieved 2026-06-11]
