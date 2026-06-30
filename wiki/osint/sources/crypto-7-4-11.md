---
title: 'Execution Is the New Attack Surface: Survivability-Aware Agentic Crypto Trading with OpenClaw-Style Local Executors'
type: source
tags: [pdf, deep-read, llm-agents, quant-finance, agent-security, execution-safety, cemini-internal-cross-ref]
keywords: [SAE, survivability-aware-execution, delegation-gap, DG, OpenClaw, skills.sh, execution-contract, trust-state, projection-enforcement, cooldown, crypto-perpetuals, Binance-replay, agentic-trading, prompt-injection, skill-supply-chain, attack-surface]
related:
  - concepts/llm-agent-systems.md
  - concepts/quant-finance.md
  - concepts/scatter-gather-topology.md
  - concepts/cryptographic-audit-trail.md
  - concepts/sae-execution-contract.md
  - concepts/defend-trade-secrets-act.md
  - sources/3-17-agent-research.md
  - sources/3-25-git-research.md
  - sources/git-3-5-pt3.md
  - sources/4-5-links.md
  - entities/frameworks/langgraph.md
  - sources/ai-2-4-3.md
  - concepts/openclaw-security-taxonomy.md
  - entities/tools/openclaw.md
  - sources/openclaw-ios-node-2026-06-29.md
  - concepts/agent-authorization-stack.md
maturity: validated
read_status: deep-read
created: 2026-04-23
updated: 2026-06-29
clusters:
  - llm-agents
  - quant-finance
  - agent-security
---

## Relations

- @concepts/llm-agent-systems.md — cluster hub for LLM agent-systems research
- @concepts/quant-finance.md — Quantitative Finance corpus-index hub
- @concepts/scatter-gather-topology.md — SAE as middleware in the execution topology; complements Send-API / Generator-Evaluator / Fractals orchestrator variants
- @concepts/cryptographic-audit-trail.md — SAE audit record emission (M6) as fourth execution-layer in the provenance chain
- @concepts/sae-execution-contract.md — promoted concept page: SAE as reusable architectural primitive
- @concepts/defend-trade-secrets-act.md — IP-sale relevance (execution-layer constraint as trade-secret boundary)
- @sources/3-17-agent-research.md — K16: both treat LLM output as untrusted; SAE provides the enforcement layer K16 implies
- @sources/3-25-git-research.md — K17: agentic decision anchoring + debate-cycle complements execution enforcement
- @sources/git-3-5-pt3.md — K18: ToxicSkills threat vector, ABAC guardrails; SAE operationalizes both at execution boundary
- @sources/4-5-links.md — K8: sibling resource-evaluation format; both survey external tools/patterns for Cemini adoption
- @sources/ai-2-4-3.md — K20 deep-read 2026-05-01; OpenClaw 190-advisory security taxonomy — the structured threat model SAE defends against. K19 = defense, K20 = threat model
- @concepts/openclaw-security-taxonomy.md — K20 promotion 2026-05-01; two-axis taxonomy + Context Manipulation kill chain + three structural conditions validate SAE's "assume compromise" baseline
- @entities/frameworks/langgraph.md — OpenClaw-style tool interception is a LangGraph-adjacent orchestration pattern
- @concepts/agent-authorization-stack.md — K19 canonical source for SAE; Layer 3 of the four-layer authorization architecture.

## Raw Concept

- **Original title**: Execution Is the New Attack Surface: Survivability-Aware Agentic Crypto Trading with OpenClaw-Style Local Executors
- **Author(s)**: Ailiya Borjigin, Igor Stadnyk, Ben Bilski (True Trading); Serhii Hovorov, Sofiia Pidturkina (Inc4.net)
- **Type**: PDF — academic paper, arXiv:2603.10092v1 [cs.CR], 10 Mar 2026
- **Location**: cemini-librarian:/opt/cemini-bulk/research/crypto 7 4:11.pdf
- **Retrieved**: 2026-04-23
- **Length**: 26 pages
- **Read status**: deep-read
- **Primary cluster**: llm-agents
- **All clusters**: llm-agents, quant-finance, agent-security

## Narrative

### Paper framing

This paper argues that the dominant safety failure mode for agentic systems has shifted from "wrong answers" to **execution-induced loss**: untrusted prompts, compromised skills, or narrative manipulation can translate into real trades and irreversible side effects. Two structural trends drive this: (i) OpenClaw-style stacks that route language through tool interception into privileged local execution, and (ii) skills.sh-style marketplaces that make capability acquisition a supply-chain event. The paper proposes **Survivability-Aware Execution (SAE)** — execution-layer middleware that treats upstream intent as structurally untrusted and enforces non-bypassable constraints at the last mile.

### Key contributions

1. **Delegation Gap (DG)** — formal metric: expected loss from actions executable but outside intended scope. Operationalized via a structured Intended Policy Spec (tool/venue allowlists, risk budgets, market-state constraints, user/account constraints) that yields deterministic out-of-scope labeling. DG decomposes into DG rate (fraction of out-of-scope actions) and DG loss (loss contribution of out-of-scope actions).

2. **SAE execution contract** — standardized API: `ExecutionRequest` → `ExecutionContext` → `ExecutionDecision` (ALLOW/LIMIT/BLOCK). Designed as middleware between strategy engine and exchange executor. Non-bypassable: even if upstream intent is manipulated, only SAE-approved actions reach the executor.

3. **Four-layer model** beyond conventional OMS: Layer 0 (Static OMS baseline — fixed caps, stop-losses, rate limits), Layer 1 (trust-state conditioned budgeting — provenance, capability risk, injection alerts tighten exposure), Layer 2 (supply-chain and scope enforcement — Intended Policy Spec + hard out-of-scope rules), Layer 3 (attack-aware evaluation — AttackSuccess, FalseBlock, DG metrics as system-level robustness measures).

4. **Trust-state conditioned budgeting**: z_t = (provenance score, capability risk, injection alert). Budget vector B_t = B_0 · g(market) · h(account) · q(z_t). Low provenance, high capability risk, or active injection alerts reduce exposure budgets even if the strategy requests more.

5. **Projection-based enforcement with theoretical bound**: requested actions are projected into the feasible budget region via convex optimization (generalizes heuristic clamping). Formal bound: if loss is L-Lipschitz and SAE enforces ∥e_t∥ ≤ B_t, then ℓ_t(e_t) − ℓ_t(0) ≤ LB_t — linking projection to worst-case loss reduction without assuming return dynamics.

6. **Six mitigations as enforceable invariants** (M1–M6): intended-policy spec + hard OOS rules, trust-state tightening, projection enforcement, temporal invariants (cooldown/rate limits), slippage bounds + staged execution, auditability + incident response.

7. **skills.sh integration**: SAE packaged as installable `sae-policy-guard` skill — `npx skills add https://skills.sh/true-ai-labs/sae-policy-guard/sae-policy-guard`. Treats skill installation as a supply-chain event — the same ecosystem SAE is designed to protect against.

### Empirical results (Binance USD-M replay)

Reproducible offline replay on BTCUSDT/ETHUSDT perpetuals, 15m bars, 2025-09-01–2025-12-01, including funding. Five SAE variants compared: NoSAE (pass-through), StaticOMS (fixed caps + stop-loss + rate limits), Budget (projection + state tightening), Budget+Cooldown (+ temporal invariants), Full (+ trust-conditioned tightening).

| Metric | NoSAE | StaticOMS | Budget | Budget+Cooldown | Full |
|--------|-------|-----------|--------|-----------------|------|
| MDD | 0.4643 | 0.1184 | 0.0325 | 0.0363 | 0.0319 |
| CVaR 0.99 | −4.025×10⁻³ | −5.62×10⁻⁴ | −1.01×10⁻⁴ | −1.03×10⁻⁴ | −1.02×10⁻⁴ |
| DG loss | 0.647 | 0.119 | 0.021 | 0.026 | 0.019 |
| AttackSuccess | 1.000 | 0.885 | 0.760 | 0.759 | 0.728 |
| FalseBlock | 0.000 | 0.011 | 0.000 | 0.000 | 0.000 |

- **MDD**: 93.1% reduction (NoSAE→Full)
- **CVaR 0.99**: ~97.5% reduction in tail-loss magnitude
- **DG loss**: ~97.0% reduction (out-of-scope executions no longer dominate loss)
- **AttackSuccess**: 1.00→0.728 (27.2pp reduction) with zero FalseBlock
- **Statistical significance**: block-bootstrap CIs well-separated, Wilcoxon p=0.0113, two-proportion test on AttackSuccess p=1.76×10⁻⁸

### Cemini relevance

SAE is the **highest-intersection academic paper in the K-series** with Cemini's architecture. It directly addresses gaps identified across four prior K-series docs:

- **K14 (OpenClaw Tier C rejection; K135 Tier A carve-out)** — SAE is the OpenClaw-compatible execution contract K14's analysis implied was missing. Tier A personal gateway still requires execution-boundary enforcement; prod trading integration unchanged NO-GO (@entities/tools/openclaw.md).
- **K16 (sandboxed observer)** — SAE provides the enforcement layer K16's observation-only pipeline needs at the boundary
- **K17 (agentic decision anchoring)** — SAE's ExecutionDecision (ALLOW/LIMIT/BLOCK) complements K17's debate-cycle anchoring with execution-level enforcement
- **K18 (ToxicSkills + ABAC guardrails)** — SAE's trust-state conditioned budgeting (z_t) operationalizes both ToxicSkills threat detection and ABAC-style attribute-based access control at the execution boundary

SAE's architecture maps cleanly onto Cemini's scatter-gather topology: SAE middleware sits at the terminal leaf of the execution graph, downstream of the orchestrator (Send-API / Generator-Evaluator / Fractals) and upstream of the exchange executor. The Intended Policy Spec (St) is a natural YAML configuration artifact — consistent with Cemini's existing config-driven approach (K18's SDD, K8's YAML-defined topology).

### Limitation notes

- Replay fidelity: offline evaluation with configurable simulator; liquidation tiers, fees, and market impact are approximated
- Skill supply-chain realism: trust state models provenance risk but doesn't yet integrate SBOM metadata, signatures, or transitive trust
- Adaptive adversaries: current attack suite is deterministic; adaptive multi-step adversaries that probe gate behavior are future work
- Single exchange (Binance USD-M), two symbols (BTCUSDT, ETHUSDT), one 3-month window

### Promotion decision: 1 new concept page

SAE execution contract promoted to `concepts/sae-execution-contract.md`. It is a **reusable architectural primitive** — an explicit, standardized API contract for execution-layer safety that composes with existing orchestrator topologies. The Delegation Gap metric, trust-state conditioned budgeting, and projection-based enforcement are novel contributions not captured by existing concept pages.

Extensions to 2 existing concept pages (scatter-gather-topology, cryptographic-audit-trail) + 2 cluster-hub frontmatter additions (llm-agent-systems, quant-finance). 11 bidirectional backlinks.

## Snippets

**Delegation Gap formal definition (p.3)**:
"DG ≜ E[ℓ(a_t) · 1{a_t ∉ A_intended(S_t)}], a_t ∼ P_π(·) over A_actual, where ℓ(·) is a fixed loss functional (e.g., realized PnL loss, liquidation indicator/proxy, or security loss proxy), and S_t is an explicit Intended Policy Spec."

**Intended Policy Spec structure (p.4)**:
"S_t = (T_t, R_t, M_t, U_t) with: (i) Allowed action/tool set T_t — permitted action types and tools, plus permitted venues/symbols/accounts; (ii) Risk budgets R_t — hard caps on leverage, notional, order rate, slippage, holding time, concurrent positions; (iii) Market-state constraints M_t — state-triggered tightening based on volatility/liquidity/funding extremes; (iv) User/account constraints U_t — margin ratio, drawdown/PnL state, cooldown timers, exposure concentration."

**SAE execution contract (p.6)**:
"ExecutionRequest: symbol, venue, timestamp_ms, intent, side, requested notional, requested leverage, order type, max slippage_bps, strategy_id. ExecutionContext: account state (equity, drawdown, positions, recent trades, margin ratio), market state (realized volatility, funding, liquidity proxy, regime label), and a first-class trust state z_t. ExecutionDecision: decision ∈ {ALLOW, LIMIT, BLOCK} plus enforced constraints: leverage cap, notional cap, order-rate cap, slippage cap, cooldown, staging plan, and structured audit fields."

**Trust state definition (p.10)**:
"z_t = (p_prov_t, r_cap_t, I_inj_t), where p_prov_t ∈ [0,1] scores provenance of the active skill/toolchain, r_cap_t scores capability risk (privilege and side-effect surface), and I_inj_t ∈ {0,1} is an injection-alert flag from safety monitors."

**Budget tightening factorization (p.10)**:
"B_t = B_0 · g(σ_t, λ_t, f_t) · h(m_t, DD_t) · q(z_t), where B_0 is the default budget, g(·) tightens under volatile/illiquid/funding-extreme regimes, h(·) tightens under constrained accounts, and q(·) tightens when provenance is weak, capability risk is high, or injection alerts trigger."

**Execution contract concrete example (p.8–9)**:
"Strategy asks: leverage=5.0, notional_fraction=0.50, slippage_bps=80. SAE returns: decision=LIMIT, effective_leverage=1.0, effective_notional_fraction=0.20, effective_slippage_bps=30, cooldown_sec=120, reason='extreme regime + low skill provenance'."

**Projection-based enforcement bound (p.7–8)**:
"Let e_t denote the exposure vector induced by an execution action. Assume per-step loss ℓ_t(e) is L-Lipschitz. If SAE enforces ∥e_t∥ ≤ B_t, then ℓ_t(e_t) − ℓ_t(0) ≤ L∥e_t∥ ≤ LB_t. Under projection e_eff_t = Π_F(B_t)(e_req_t): ℓ_t(e_eff_t) − ℓ_t(e_req_t) ≤ L · dist(e_req_t, F(B_t))."

**Why NoSAE is the realistic baseline (p.7)**:
"While human discretionary traders often rely on stop-losses and broker-side controls, many deployed agentic bots connect directly from strategy logic to the executor with no intermediate gating layer. In such systems, the strategy output is effectively the action."

**Why skills.sh makes untrusted intent unavoidable (p.23)**:
"Skill marketplaces such as skills.sh turn capability acquisition into an operational workflow. From a security perspective, installing a skill is a supply-chain event: it can modify which tools are called, how parameters are chosen, and how external content is trusted. Therefore, upstream intent is not merely 'noisy'—it is structurally untrusted in the presence of third-party skills."

**SAE vs. OMS distinction (p.6)**:
"Our position is not that SAE replaces OMS, but that SAE includes a standard OMS baseline and then adds three layers that become necessary in agentic, skills-enabled execution: Layer 1 (trust-state conditioned budgeting), Layer 2 (supply-chain and scope enforcement), Layer 3 (attack-aware evaluation)."

**Moltbook incident as assume-compromise rationale (p.2)**:
"Reuters reported that Moltbook—a Reddit-like social site marketed for AI agents—suffered a major exposure due to a basic security flaw, leaking private agent messages, thousands of owner emails, and a large volume of credentials. The lesson is structural: fast-growing agent ecosystems can externalize sensitive data at scale through simple misconfigurations."
