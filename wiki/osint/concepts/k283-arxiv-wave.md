---
title: K283 arXiv Wave — vol decomposition + agent verification (Oct 2026)
type: concept
tags: [k283, arxiv, volatility, options, agents, rag, eval, verification]
keywords: [k283, dpp, vix, uvm, uncertain-volatility, gspo, t-search, clift, conformal, wikidata, bttf, mean-field]
related:
  - concepts/k283-eval-wave.md
  - concepts/k283-feeds-wave.md
  - concepts/xsp-vol-regime-gates.md
  - concepts/agent-tool-use-verification.md
  - entities/tools/t-search.md
  - sources/arxiv-2610.03849-beneath-the-vix-2026-10-06.md
  - sources/arxiv-2610.04530-broadcast-voter-model-2026-10-06.md
  - sources/arxiv-2610.06292-mean-field-fictitious-play-2026-10-06.md
  - sources/arxiv-2610.06495-uncertain-vol-error-bounds-2026-10-06.md
  - sources/arxiv-2610.06650-wikidata-search-traces-2026-10-06.md
  - sources/arxiv-2610.06782-t-search-agentic-retriever-2026-10-06.md
  - sources/arxiv-2610.06790-bttf-eda-agentic-2026-10-06.md
  - sources/arxiv-2610.06829-clift-web-agent-verification-2026-10-06.md
maturity: draft
created: 2026-10-06
updated: 2026-10-06
harness_verb: FILE
wire_status: policy_wired
---

## Relations

- @concepts/k283-eval-wave.md
- @concepts/xsp-vol-regime-gates.md
- @concepts/agent-tool-use-verification.md
- @sources/arxiv-2610.03849-beneath-the-vix-2026-10-06.md
- @sources/arxiv-2610.06829-clift-web-agent-verification-2026-10-06.md

## Raw Concept

K283 arXiv cluster hub. **8 papers**, split cleanly: **4 quant/math**, **4 LLM-agent/tooling**. Dual-ID **OSINT K283**.

## Narrative

### The four quant/math papers

**1. `arXiv 2610.03849` — Beneath the VIX (the useful one).** Splits the VIX into **probability × severity** via a Downside Protection Premium. Severity is 91.5% of the recession premium and its elasticity is 1.032; the probability elasticity is −0.032. DPP–VIX correlation 0.992. The actionable read: **a VIX rise that is severity-led is the one that hurts short-vol positioning.** Feeds `xsp-vol-regime-gates`.

**2. `arXiv 2610.06495` — UVM a posteriori bounds.** In the Uncertain Volatility Model the price is a *range*. This gives computable two-sided bounds from one smooth candidate, using a **cash-gamma** dual and the **Black–Scholes–Barenblatt residual**. Hessian duals beat the martingale dual; second-order Sobolev training tightens them. The reusable part is the dual construction.

**3. `arXiv 2610.06292` — MFG fictitious play.** Convergence proof for learning controls in potential mean-field games. Adjacent to trade-crowding models; no direct hook.

**4. `arXiv 2610.04530` — Broadcast voter model.** Pure probability (math.PR). The dual is a coordinated-coalescing random walk. No hook; ingested for the technique.

### The four agent papers

**5. `arXiv 2610.06829` — CLIFT (the headline result).** Conformal self-verification for web agents. A URL-scoped question bank + a **Mondrian-ACI** conformal certifier produce a judge-free verifier. On OM2W, GPT-5.5 improved **49.7 → 61.0 (+11.3 pp) at K=4 with zero policy training.** The training reward is **additive-only** — the verifier term never subtracts. Directly feeds `agent-tool-use-verification` and `llm-as-a-verifier`. Route to CCC + cyber.

**6. `arXiv 2610.06782` — T-Search.** Open agentic retriever, **Apache-2.0**. Returns ranked evidence **chunks with reasons, not answers**. 56.0 Recall@10 single-rollout, 61.3 fused. Clean license — rare in this batch. Route to CCC.

**7. `arXiv 2610.06650` — Wikidata Search Traces.** 10,235 traces + an RLM harness. Headline: **a persistent-Python-state harness beats stateless tool-calling** (gpt-6-luna 49→61; Qwen3.8-27B 60→74). Same lesson as the wiki's interpreter-over-tool-loop thread.

**8. `arXiv 2610.06790` — BTTF (EDA).** Recasts terabyte waveform dumps into **SQLite**, then lets a multi-agent engine write schema-aware SQL. 95.33% execution accuracy; multi-agent beats single-agent by 17.3%. Transferable idea: **put the data in a relation, let agents write SQL.** (EDA = electronic design automation, not exploratory data analysis.)

### Boundary

**FILE only. No install. No clone.** The two vol papers are the desk-relevant extracts; the four agent papers are CCC/cyber awareness.

### Distribution

- Vol papers → wiki-only (no xsp scp this wave; awareness feeds `xsp-vol-regime-gates`).
- Agent papers (CLIFT, T-Search, Wikidata, BTTF) → `../Cemini claude code CCC/briefs/2026-10-06_k283-agent-harness.md`
- CLIFT + Wikidata → `../Cybersecurity wiki/briefs/2026-10-06_k283-agent-verification.md`
