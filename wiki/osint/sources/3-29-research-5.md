---
title: "Targeted Extraction Audit: Cemini Financial Suite — Options Pricing & SDE Sensitivities"
type: source
tags: [docx, rl-marl, llm-agents, portfolio-strategy, options-derivatives, market-microstructure, ml-methods, cemini-internal, curved-greeks, finns, dml-0dte, traderbench, qmc, asr, sde-diff]
clusters: [rl-marl, llm-agents, portfolio-strategy, options-derivatives, market-microstructure, ml-methods, cemini-internal]
related:
  - concepts/rl-marl-research.md
maturity: validated
created: 2026-04-23
updated: 2026-04-26
---

## Relations

- @concepts/rl-marl-research.md — cluster hub for RL/MARL research in the Cemini corpus

## Raw Concept

- **Original title**: Targeted Extraction Audit: Cemini Financial Suite (options-pricing / SDE-sensitivities batch)
- **Author(s)**: Cemini internal research (no attributed author)
- **Type**: DOCX (internal extraction audit)
- **Location**: research for cemini/3_29 research 5.docx
- **Length**: ~6025 words, 177 paragraphs
- **Retrieved**: 2026-04-23 (filename date 2026-03-29)
- **Read status**: read-skim
- **Primary cluster**: options-derivatives
- **All clusters**: rl-marl, llm-agents, portfolio-strategy, options-derivatives, market-microstructure, ml-methods, cemini-internal

## Narrative

Second-batch extraction audit (sibling to `3-29-research-3.md`) surveying six external sources on options pricing and stochastic-sensitivities and distilling each into the same seven-slot template: WHAT IT IS / ARCHITECTURE PATTERNS TO EXTRACT / CODE LOGIC TO STUDY / DEV WORKFLOW / LLM AUTOMATION PATTERNS / VERDICT / WHAT'S NOT USEFUL. Sources covered:

1. **Curved Greeks (Pérez Velasco, Lu, Arrieta)** — adopts the induced-liquidity-metric tensor as an explicit feature in the 28-dim MAPPO observation space (forces execution-aware policies, closes the reality gap during paper trading). Rejects manual affine-connection calibration (let MAPPO learn it). TimescaleDB continuous aggregates bucket the impact matrix every 15 min.
2. **Feynman-Kac FINNs (Mott)** — extracts AD-based zero-marginal-cost Greeks via `torch.autograd` in single forward pass; state-dependent volatility capping σ(x,t) ≤ σ_max in Polars pipeline to prevent gradient explosions. Cross-sectional random-state sampling over sequential time-series paths. Rejects training full FINNs on CPU (infeasible under 128GB RAM).
3. **Differential Machine Learning for 0DTE (stochastic-vol jump-diffusion)** — twin-network maturity-gated variance correction (vanishes as T→0); compensated-jump-term numerical proxy as a Polars-engineered feature; hard-cutoff drop of deep-OTM Greek targets below ε to prevent gradient noise. Arbitrage-validator agent checks convexity / delta bounds / vega monotonicity via squared positive-part penalties exposed as FastMCP tool.
4. **TraderBench** — two-agent A2A evaluator/candidate architecture across 6 specialized MCP servers (SEC EDGAR, Sandbox, Options, Trading Sim, Risk, Yahoo Finance) — maps to Cemini's FastMCP + LangGraph; adopts temporally-locked servers to prove no lookahead data leakage for IP-sale credibility. Three-stage adversarial data transforms (Gaussian noise + volume spikes → trend injection + false breakouts → coordinated false MACD/RSI) as curriculum for MAPPO. Diagnoses the "competence mirage" — frontier LLMs off by 54 points on Greeks vs strategy selection → enforce "Math Delegation" prompt pattern (agents output JSON parameter requests, never compute numerics).
5. **Quasi-Monte Carlo + GSA (Sobol sequences)** — swap `numpy.random` for `scipy.stats.qmc.Sobol` with Brownian-bridge discretization; QMC + central FD for Greeks is the solo-dev-optimal alternative to AAD (equivalent accuracy, fraction of code). GSA Sobol indices exposed as Analytics-Agent FastMCP tool for autonomous risk-driver explanation.
6. **ASR deep hedging (Optimized Certainty Equivalent)** — OCE-wrapped P&L (Expected Shortfall) as TorchRL reward instead of Sharpe-based reward; continuous-confidence-score soft-stopping with dynamic threshold (avoids every-tick trading). Bespoke ASR bang-bang strategy explicitly rejected.
7. **Differentiating through SDEs: A Primer (Leburu/Nurbekyan/Ruthotto)** — validates discretize-then-optimize; state-augmentation for joint extraction of state gradients and Greeks; pytest harness comparing autograd output against closed-form BSM Greeks as CI/CD gate. "Optimization Agent" using gradients to autonomously gradient-descent portfolio weights via Redis `intel:*` bus.

Relevant to Cemini as the definitive external-sources digest for the options-pricing + SDE-sensitivities layer of the stack. Honest limits: (a) same consulting-style "WHAT IT IS / WHAT'S NOT USEFUL" verdict framing as 3-29-research-3, with effort estimates ("4 hours", "2 hours", "3 hours") ungrounded; (b) document leans into IP-sale narrative ("credibility during IP sale", "41-page site") which biases every recommendation toward demonstrable-architecture-over-measurable-alpha; (c) TraderBench's "54-point gap" claim is repeated but uncited; (d) Curved Greeks and SDE primer sections partially duplicate content from primary source pages (greeks-2-3-29, greeks-8-3-29), so this doc should be treated as prescriptive layer on top of those.

## Key findings

- Curved Greeks liquidity metric → feature in 28-dim MAPPO observation; continuous aggregate every 15 min in TimescaleDB.
- FINN AD Greeks via `torch.autograd` in single forward pass; reject full FINN training on CPU.
- 0DTE DML maturity-gating + compensated-jump proxy feature + hard-cutoff drop of deep-OTM Greeks.
- Arbitrage-validator agent enforces convexity / delta-bounds / vega-monotonicity as squared positive-part penalties via FastMCP tool.
- TraderBench two-agent A2A + 6 specialized MCP servers pattern → adopt as temporally-locked FastMCP layout for lookahead-free backtest credibility.
- TraderBench-style 3-stage adversarial data transforms as curriculum for MAPPO robustness training.
- "Competence mirage" → Math Delegation prompt pattern: agents never compute numerics; FastMCP backend owns arithmetic.
- `scipy.stats.qmc.Sobol` + Brownian bridge + central FD beats AAD for solo-dev Greeks; GSA Sobol indices as risk-driver explainer.
- OCE / Expected Shortfall TorchRL reward over Sharpe.
- Discretize-then-optimize validated; state augmentation yields joint state-gradient + Greek extraction.
- pytest CI gate: autograd output vs closed-form BSM Greeks on every refactor.

## Snippets

- **Curved Greeks extraction** — "By injecting the induced liquidity metric as an explicit, dense feature in the 28-feature observation space, the Multi-Agent Proximal Policy Optimization (MAPPO) algorithm will be forced to learn execution-aware policies that naturally avoid geometrically expensive factor directions."
- **FINN extraction** — "the pattern of using torch.autograd to extract exact, zero-marginal-cost Greeks during a single forward pass is highly valuable… Shifting to an AD-based sensitivity extraction within the existing PyTorch graph will reduce computation cycles and eliminate truncation errors."
- **0DTE DML** — "maturity-gated variance correction… scales the network output by a deterministic function so that the learned variance correction naturally vanishes as the time to expiration approaches zero."
- **TraderBench competence mirage** — "a massive 54-point gap in frontier models' ability to calculate Greeks versus selecting high-level strategies… Prompts must forcefully restrict the 5-agent debate from generating numerical targets directly."
- **QMC** — "for a small number of Greeks, QMC+FD achieves equivalent accuracy to AAD with a fraction of the code complexity."
- **ASR / OCE** — "By wrapping the P&L outputs in an OCE risk measure like Expected Shortfall… the reinforcement learning agent learns to balance maximum extraction against catastrophic tail risks. This provides a vastly more sophisticated and robust training target than standard Sharpe-ratio-based rewards."
- **SDE primer** — "creating a suite of deterministic unit tests using pytest that compare the output of the automated differentiation engine against closed-form Black-Scholes Greeks for vanilla instruments."
