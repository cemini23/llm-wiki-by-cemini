---
title: SAE execution contract
type: concept
tags: [concept, execution-safety, agent-security, architectural-primitive, cemini-internal-cross-ref]
keywords: [SAE, survivability-aware-execution, execution-contract, delegation-gap, DG, trust-state, projection-enforcement, cooldown, allowlist, budget-tightening, OpenClaw, skills.sh, agentic-trading, execution-boundary, last-mile-enforcement]
related:
  - sources/crypto-7-4-11.md
  - concepts/scatter-gather-topology.md
  - concepts/cryptographic-audit-trail.md
  - concepts/llm-agent-systems.md
  - concepts/quant-finance.md
  - sources/3-17-agent-research.md
  - sources/3-25-git-research.md
  - sources/git-3-5-pt3.md
  - concepts/defend-trade-secrets-act.md
  - entities/frameworks/langgraph.md
  - sources/4-5-links.md
  - sources/ai-2-4-3.md
  - concepts/openclaw-security-taxonomy.md
  - entities/tools/openclaw.md
  - sources/openclaw-ios-node-2026-06-29.md
  - sources/3-29-15.md
  - concepts/reasoning-safety-monitor.md
  - concepts/agent-authorization-stack.md
  - sources/safeharness-2604.13630.md
  - concepts/mitre-atlas-taxonomy.md
  - concepts/reviewer-passive-injection-corpus.md
maturity: validated
created: 2026-05-01
updated: 2026-10-25
---

## Relations

- @sources/crypto-7-4-11.md — canonical source: "Execution Is the New Attack Surface," arXiv:2603.10092v1, True Trading / Inc4.net, March 2026
- @concepts/scatter-gather-topology.md — SAE sits at the terminal leaf of the execution graph, downstream of orchestrator and upstream of executor
- @concepts/cryptographic-audit-trail.md — SAE audit record emission (M6) as execution-layer in the provenance chain
- @concepts/llm-agent-systems.md — cluster hub for LLM agent-systems research
- @concepts/quant-finance.md — cluster hub for quantitative finance
- @sources/3-17-agent-research.md — K16: both treat LLM output as untrusted; SAE provides the enforcement layer K16 implies
- @sources/3-25-git-research.md — K17: debate-cycle decision anchoring complements execution enforcement
- @sources/git-3-5-pt3.md — K18: ToxicSkills threat vector + ABAC guardrails operationalized at execution boundary
- @sources/ai-2-4-3.md — K20: OpenClaw security taxonomy (190 advisories) — the structured threat model SAE's six mitigations address; three structural conditions validate SAE's "assume compromise" baseline
- @concepts/openclaw-security-taxonomy.md — K20 promotion: reusable architectural primitive capturing the two-axis taxonomy, Context Manipulation kill chain, and three structural conditions
- @sources/3-29-15.md — K22 deep-read 2026-05-01; reasoning safety monitor provides step-level CoT inspection + interrupt signal — closes K20 §6.6's context-window provenance gap
- @concepts/reasoning-safety-monitor.md — K22 promotion; parallel CoT inspection architecture — feeds reasoning-integrity signals into SAE's trust-state (z_t) as I_reasoning component
- @concepts/agent-authorization-stack.md — K19+K22+K23+K24 cross-cluster synthesis; Layer 3 of the four-layer authorization architecture.
- @sources/safeharness-2604.13630.md — K25 SafeHarness enforces inside the harness lifecycle; SAE enforces at the execution boundary. Different enforcement points, shared authorization posture.

## Raw Concept

Synthesized from `@sources/crypto-7-4-11.md` (Borjigin et al., arXiv:2603.10092v1, March 2026). The SAE execution contract is a reusable architectural primitive for agentic systems where language becomes a control surface for real-world side effects. It standardizes the last-mile boundary between strategy intent and exchange submission as an explicit API contract with non-bypassable enforcement.

## Narrative

### What SAE is

Survivability-Aware Execution (SAE) is **execution-layer middleware** placed between any strategy engine (LLM or non-LLM) and the exchange executor. Its core premise: in agentic settings where skills are installed from third-party marketplaces and prompts may be compromised, **upstream intent is structurally untrusted**. SAE enforces non-bypassable constraints at the last mile — the point where actions become side effects.

SAE does not replace conventional OMS risk checks; it **includes a standard OMS baseline** (fixed leverage/position caps, stop-losses, rate limits) and adds three layers specific to agentic, skills-enabled execution: trust-state conditioned budgeting, supply-chain/scope enforcement, and attack-aware evaluation.

### The execution contract

SAE standardizes three structured types at the execution boundary:

1. **ExecutionRequest**: symbol, venue, timestamp_ms, intent, side, requested notional, requested leverage, order type, max slippage_bps, strategy_id
2. **ExecutionContext**: account state (equity, drawdown, positions, margin ratio), market state (volatility, funding, liquidity proxy, regime label), and a first-class **trust state** z_t
3. **ExecutionDecision**: decision ∈ {ALLOW, LIMIT, BLOCK} plus enforced constraints (leverage cap, notional cap, order-rate cap, slippage cap, cooldown, staging plan) and structured audit fields

A BLOCK decision rejects the action entirely. A LIMIT decision transforms it into a safer executable action — reducing leverage, capping notional, tightening slippage, imposing cooldown — while preserving the intent to trade. ALLOW passes the action through unchanged.

### Delegation Gap (DG)

The Delegation Gap formalizes the distance between what an operator intends to authorize and what the deployed system can actually execute. It is measured as:

**DG ≜ E[ℓ(a_t) · 1{a_t ∉ A_intended(S_t)}]**

where A_intended is induced by a structured **Intended Policy Spec** S_t = (T_t, R_t, M_t, U_t):
- **T_t**: allowed tools, venues, symbols, accounts (allowlists)
- **R_t**: hard risk budgets (leverage cap, notional cap, order-rate cap, slippage cap, max holding time, max concurrent positions)
- **M_t**: market-state triggered tightening rules (volatility/liquidity/funding extremes)
- **U_t**: account-state constraints (margin ratio, drawdown, cooldown timers, exposure concentration)

An action is out-of-scope if it violates any of: cap violation (risk-budget breach), tool/venue violation (capability breach), or state violation (context breach). DG decomposes into DG rate (fraction of actions out-of-scope) and DG loss (loss contribution of out-of-scope actions).

### Trust-state conditioned budgeting

SAE models trust as a first-class input to budget computation:

**z_t = (p_prov_t, r_cap_t, I_inj_t)**

- **p_prov_t** ∈ [0,1]: provenance score of the active skill/toolchain
- **r_cap_t**: capability risk (privilege level and side-effect surface)
- **I_inj_t** ∈ {0,1}: injection alert flag from safety monitors

Budgets are factorized: **B_t = B_0 · g(market) · h(account) · q(z_t)**, where q(·) tightens when provenance is weak, capability risk is high, or injection alerts are active. This makes "untrusted intent" non-optional in the enforcement logic.

### Projection-based enforcement

Rather than binary accept/reject, SAE projects requested actions into the feasible budget region:

**a_eff = arg min_{a ∈ F(B_t)} D(a, a_req)**

This generalizes heuristic clamping. The special case of leverage projection: **L_eff = min(L_req, L_cap)**.

A theoretical bound links projection to worst-case loss reduction: if per-step loss is L-Lipschitz and SAE enforces ∥e_t∥ ≤ B_t, then ℓ_t(e_t) − ℓ_t(0) ≤ LB_t. This bound avoids assuming any particular return dynamics.

### Six mitigations (M1–M6)

1. **M1**: Intended-policy spec + hard out-of-scope rules — deterministic allowlists and state-dependent constraints
2. **M2**: Trust-state conditioned tightening — budgets shrink when trust degrades
3. **M3**: Projection-based enforcement — parameter escalation attacks blocked without semantic understanding
4. **M4**: Temporal invariants — cooldown timers and order-rate caps prevent flooding/churn
5. **M5**: Slippage bounds + staged execution — notional sliced into time-spaced orders under stress
6. **M6**: Auditability — each decision emits matched rule, budgets, effective action, and state snapshot including trust signals

### Four-layer model vs. conventional OMS

| Layer | What it enforces | Why it's needed in agentic settings |
|-------|-----------------|-------------------------------------|
| Layer 0: Static OMS baseline | Fixed caps, stop-losses, rate limits | Market and margin safety (conventional) |
| Layer 1: Trust-state conditioned budgeting | Budgets shrink when provenance/capability/injection signals degrade | Upstream intent is structurally untrusted |
| Layer 2: Supply-chain and scope enforcement | Hard allowlists over tools, venues, symbols, accounts | Skills.sh-style capability acquisition = supply-chain event |
| Layer 3: Attack-aware evaluation | AttackSuccess, FalseBlock, DG metrics as system-level KPIs | Makes robustness claims reproducible and comparable |

### Cemini relevance

SAE directly addresses the execution-boundary gap identified across four K-series docs:

- **K14 (OpenClaw Tier C rejection; K135 Tier A carve-out)**: SAE is the OpenClaw-compatible execution contract K14 implied was missing — it plugs into tool interception and enforces domain-specific constraints. **Personal OpenClaw gateway** (Tier A) still needs SAE-style gates on any trading-adjacent tool path; prod integration remains NO-GO (@entities/tools/openclaw.md).
- **K16 (sandboxed observer)**: SAE provides the enforcement layer K16's observation-only pipeline needs at the boundary where observation becomes action
- **K17 (agentic decision anchoring)**: SAE's ExecutionDecision (ALLOW/LIMIT/BLOCK) complements K17's debate-cycle anchoring with execution-level enforcement — debate produces decisions, SAE gates their execution
- **K18 (ToxicSkills + ABAC guardrails)**: SAE's trust-state conditioned budgeting (z_t) operationalizes both the ToxicSkills threat vector (I_inj flag) and ABAC-style attribute-based access control (provenance + capability risk → budget tightening) at the execution boundary

SAE composes with Cemini's scatter-gather topology: the SAE middleware sits at the terminal leaf of the execution graph, downstream of the orchestrator (Send-API / Generator-Evaluator / Fractals) and upstream of the exchange executor. The Intended Policy Spec is a natural YAML configuration artifact consistent with Cemini's config-driven approach.

### K20 threat-model grounding (OpenClaw security taxonomy)

K20 (@sources/ai-2-4-3.md, @concepts/openclaw-security-taxonomy.md) provides the structured threat model that validates SAE's architectural decisions. The 190-advisory OpenClaw corpus maps onto SAE's six mitigations with high coverage:

| K20 finding | SAE mitigation | Coverage |
|---|---|---|
| Exec allowlist lexical bypasses (line-continuation, busybox multiplexer, GNU abbreviation) | M1 (Intended Policy Spec + hard OOS rules) + M3 (projection enforcement) | Semantic, not lexical — enforces on the executable action, not the command string |
| Gateway RCE chain (SSRF → token exfiltration → exec approval bypass) | M1 + M6 (auditability — full call-path visibility across layers) | Inter-layer composition — SAE observes the full ExecutionRequest→Decision trace |
| yahoofinance supply-chain dropper (context-window execution, bypasses exec policy) | M2 (trust-state conditioned budgeting — provenance score p_prov_t) + M5 (staged execution for low-provenance actions) | Distribution → execution boundary gating |
| Prompt injection (Slack metadata, Sentry headers, inter-session contamination) | M2 (I_inj flag from safety monitors) | Context provenance → budget tightening |
| Docker sandbox escape (bind-mount injection, no validation layer) | M1 (capability allowlists — T_t) + M4 (cooldown/rate limits) | Configuration integrity at creation time |
| Inter-session trust collapse (agent message indistinguishable from user) | M2 (z_t provenance scoring — inter_session < external_user) | Origin-gated trust budgeting |

K20's three structural conditions validate SAE's core design premises:
- **Closed-world assumption** → SAE's "upstream intent is structurally untrusted" baseline (M2: trust-state conditioned budgeting)
- **Absent inter-layer enforcement** → SAE's ExecutionRequest/ExecutionContext/ExecutionDecision typed contract (§6.7's "typed, validated, provenance-carrying request objects" is essentially the SAE API spec)
- **Ungoverned distribution surface** → SAE's provenance score (p_prov_t) for skill/toolchain + staged execution

One gap identified (now closed by K22): K20 §6.6 prescribes a "mandatory provenance tag for every string entering the context window" — a context-assembly-layer control that SAE does not address. SAE enforces at the execution boundary; context-window provenance is an upstream layer that feeds into SAE's trust-state.

### K22 reasoning-safety grounding (Reasoning Safety Monitor)

K22 (@sources/3-29-15.md, @concepts/reasoning-safety-monitor.md) closes the K20 §6.6 gap by providing the missing detection layer at the reasoning boundary. The Reasoning Safety Monitor inspects each CoT step as it's generated, classifies unsafe behaviors into a nine-category taxonomy, and dispatches an interrupt signal BEFORE corrupted reasoning reaches SAE's execution boundary.

| K22 capability | SAE integration point | Mechanism |
|---|---|---|
| Step-level I_inj flag per reasoning step | M2 trust-state (z_t) enrichment | Monitor verdict → z_t downgrade before SAE evaluates ExecutionRequest |
| Error type classification (1a–3c) | Granular budgeting decisions | Cat 3 (adversarial) → hard block; Cat 1-2 (possibly intrinsic) → budget tightening |
| Interrupt signal on unsafe step | SAE ExecutionDecision pre-filter | If monitor dispatched interrupt, SAE rejects without evaluation |
| Attack signature → attack type mapping | M6 audit trail enrichment | Monitor verdict appended to ExecutionDecision for post-hoc forensics |

K19+K20+K22 now form a complete execution-security architecture covering three layers:
- **Reasoning boundary** (K22): detect attacks as they manipulate the CoT — before tool invocation
- **Execution boundary** (K19/SAE): enforce constraints on tool invocations — projection-based, provenance-carrying
- **Threat model** (K20): catalog attack patterns and structural conditions — informs both detection and enforcement

### Known limitations

- Replay is an approximation of live exchange mechanics (liquidation tiers, fees, market impact)
- Trust state does not yet integrate SBOM metadata, signatures, or transitive trust scoring
- Attack suite is deterministic; adaptive adversaries that probe gate behavior are future work
- Evaluated on single exchange, two symbols, one 3-month window
- SAE does not replace key management, 2FA, or exchange-side custody controls

## Snippets

*(See canonical source page `@sources/crypto-7-4-11.md` for full verbatim pulls. Key snippets reproduced here for concept-page readability.)*

**SAE as middleware (p.8)**:
"SAE sits in the last-mile boundary: Strategy Engine → ExecutionRequest → SAE Middleware → Exchange Executor. This placement ensures constraints are non-bypassable: even if upstream intent is manipulated, the executor only receives SAE-approved actions."

**ExecutionDecision example (p.8–9)**:
"Strategy asks: leverage=5.0, notional_fraction=0.50, slippage_bps=80. SAE returns: decision=LIMIT, effective_leverage=1.0, effective_notional_fraction=0.20, effective_slippage_bps=30, cooldown_sec=120, reason='extreme regime + low skill provenance'."

**Why execution is the new attack surface (p.2)**:
"When tool access is permissive, untrusted text can become privileged actions. In finance, the consequences are immediate because side effects are monetized."

**Assume-compromise baseline (p.2)**:
"When agents are both highly connected and highly privileged, 'assume compromise' becomes a reasonable baseline."

**SAE is not an alpha clamp (p.5)**:
"SAE is not 'an alpha clamp'; it is a constraint layer that alters the feasible policy set by restricting execution."
