---
title: Agent Authorization Stack — Five-Layer Architecture
type: concept
tags: [concept, authorization, governance, execution-safety, reasoning-safety, market-microstructure, architectural-primitive, synthesis]
keywords: [authorization-stack, four-layer, nomotic, sae, reasoning-safety-monitor, parlay-market-making, rfq-trilemma, pre-action-authorization, trust-state, execution-contract, cross-cluster-synthesis]
related:
  - concepts/nomotic-ai.md
  - concepts/sae-execution-contract.md
  - concepts/reasoning-safety-monitor.md
  - concepts/parlay-market-making.md
  - concepts/openclaw-security-taxonomy.md
  - concepts/llm-agent-systems.md
  - concepts/market-microstructure.md
  - concepts/scatter-gather-topology.md
  - concepts/cryptographic-audit-trail.md
  - sources/ai-7-4-6.md
  - sources/crypto-7-4-11.md
  - sources/3-29-15.md
  - sources/kalshi1-3-29.md
  - sources/ai-2-4-3.md
  - sources/safeharness-2604.13630.md
  - sources/signa.md
  - sources/4-11-crypto-re.md
  - concepts/mitre-atlas-taxonomy.md
  - sources/xskill-2603-12056.md
maturity: validated
created: 2026-05-01
updated: 2026-05-11
---

## Relations

- @concepts/nomotic-ai.md — Layer 1: philosophical framework. Six formal principles. Governance as architecture, pre-action authorization, explicit authority boundaries.
- @concepts/sae-execution-contract.md — Layer 3: execution-boundary enforcement. Trust-state conditioned budgeting, projection-based enforcement, ALLOW/LIMIT/BLOCK.
- @concepts/reasoning-safety-monitor.md — Layer 2: reasoning-boundary detection. Parallel CoT inspection, nine-category taxonomy, interrupt signal before corrupted reasoning reaches execution.
- @concepts/parlay-market-making.md — Layer 4: market-level authorization constraint. RFQ trilemma proves no architecture satisfies all three desiderata; design tradeoffs are explicit authorization decisions.
- @concepts/openclaw-security-taxonomy.md — Threat model that catalogs what all four layers must defend against (190 advisories, two-axis taxonomy, three structural conditions).
- @sources/safeharness-2604.13630.md — Harness-internal monitoring layer (K25). Four defense layers woven into the agent lifecycle. Closes the gap between reasoning monitor and execution contract.
- @concepts/llm-agent-systems.md — Cluster hub for LLM agent-systems; the authorization stack is the governance dimension of this cluster.
- @concepts/market-microstructure.md — Cluster hub for market microstructure; ParlayMarket's RFQ trilemma is the authorization-relevant finding from this cluster.
- @concepts/scatter-gather-topology.md — Execution topology; SAE sits at the terminal leaf; the authorization stack gates every scatter-gather fan-out.
- @concepts/cryptographic-audit-trail.md — Every authorization decision across all four layers is immutably logged.
- @sources/signa.md — Cemini competitive intelligence on Signa platform; Tiered RBAC tool permissioning (Pattern 2.5) and hmac-webhooks directly extend authorization stack patterns
- @sources/4-11-crypto-re.md — Cemini competitive intelligence; A2Auth capability-bound certificates and SAE execution middleware directly extend authorization patterns

## Raw Concept

Four K-series deep-reads (K19, K22, K23, K24), drawn from four different clusters (execution safety, reasoning safety, governance philosophy, market microstructure), converge on the same question: **"When should an agent be allowed to act?"** Each provides a piece of the answer at a different architectural layer. Together they form a complete authorization stack — a reusable architectural primitive for any agentic system where actions have real-world side effects.

This page synthesizes the convergence. It does not duplicate the individual concept pages; it shows how they compose.

## Narrative

### The convergence: four papers, one question

| K | Paper | Cluster | Layer | Question answered |
|---|-------|---------|-------|-------------------|
| K23 | Nomotic AI (Hood, Jan 2026) | Governance philosophy | **Layer 1: Authorization framework** | Why must every action be authorized before execution? |
| K22 | Reasoning Safety Monitor (Wang/Zhou, arXiv:2603.25412, Mar 2026) | Reasoning safety | **Layer 2: Reasoning integrity** | Is the reasoning that produced this action trustworthy? |
| K25 | SafeHarness (Lin et al., arXiv:2604.13630, Apr 2026) | Agent security | **Layer 3: Harness-internal monitoring** | Is the harness itself — the orchestrator managing tools, context, and state — compromised? |
| K19 | SAE (Borjigin, arXiv:2603.10092, Mar 2026) | Execution safety | **Layer 4: Execution constraints** | Does this specific action, in this market state, with this trust level, satisfy all constraints? |
| K24 | ParlayMarket (Rana/Nadkarni, arXiv:2603.22596, Mar 2026) | Market microstructure | **Layer 5: Market design** | What authorization tradeoffs are structurally unavoidable in the market design itself? |

The convergence is not coincidental. All four papers were published within a 3-month window (Jan–Mar 2026). All four address the same architectural shift: as LLM agents move from chatbots to execution engines, authorization must move from after-the-fact review to before-the-fact enforcement. The four layers are independent by design — each addresses a different part of the attack surface — but they compose into a single authorization architecture.

### The four layers in detail

#### Layer 1 — Nomotic AI: the authorization framework

**What it provides**: The philosophical and architectural framework for pre-action authorization. Six formal principles. The agentic-nomotic duality: agentic systems provide capabilities; nomotic systems provide governance. The core rule: AI authority is delegated, never inherent. Every action requires explicit pre-action authorization. Actions outside defined boundaries fail by default.

**Why it's Layer 1**: It defines the *category* of the problem. Without the nomotic framing, Layers 2–4 are just disconnected safety mechanisms. With it, they're a coherent authorization architecture. The five principles (Governance as Architecture, Pre-Action Authorization, Explicit Authority Boundaries, Verifiable Trust, Ethical Justification, Accountable Governance) provide the design checklist that Layers 2–4 implement.

**Cemini instantiation**: The Nomotic Execution Service — a deterministic Pydantic gate between the LangGraph brain and any broker API. The brain emits Trade Intent Payloads; the gate validates and passes or blocks. The brain never sees the broker API.

#### Layer 2 — Reasoning Safety Monitor: reasoning integrity

**What it provides**: Detection at the reasoning boundary. A parallel LLM-based monitor inspects each chain-of-thought step as it's generated, classifies unsafe behaviors into a nine-category taxonomy, and dispatches an interrupt signal BEFORE corrupted reasoning reaches tool execution.

**Why it's Layer 2**: Nomotic AI says "authorize before acting," but it doesn't say how to detect corrupted intent. If the reasoning chain has been prompt-injected — if the model is reasoning from attacker-manipulated premises — the actions it produces will pass execution-level validation while serving attacker goals. The Reasoning Safety Monitor catches this: it inspects the CoT, not the output. Category 3 errors (Goal Deviation, Reasoning Loop) occur at ≤1.7% natural frequency — when the monitor sees them, it's almost certainly adversarial.

**Cemini instantiation**: The monitor's per-step verdict (safety flag + error type code + confidence) feeds into SAE's trust-state as an I_inj component. If the monitor dispatched an interrupt, SAE rejects without evaluation.

#### Layer 3 — SafeHarness: harness-internal monitoring

**What it provides**: The layer missing from the original four-layer stack. SafeHarness embeds defense mechanisms inside the agent harness itself — the orchestrator that manages tool registries, compresses conversation state, curates context under token budgets, and enforces execution contracts. Four internal defense layers map to the four phases of agent execution: Inform (input filtering with provenance), Verify (three-tier causal verification), Constrain (privilege-separated tool control with capability tokens), and Correct (checkpoints with adaptive degradation). Cross-layer feedback: a detection at one phase strengthens protection at others through escalation, rollback, and privilege-tightening signals.

**Why it's Layer 3**: K22 monitors what the model *thinks* (reasoning chains). K19 constrains what the model *does* (execution). But neither monitors the harness that sits between them — the orchestrator that decides which tools to expose, which context to retain, and which execution contracts to enforce. If the harness is compromised — poisoned tool outputs, tampered tool specifications, corrupted conversation history — the reasoning can be clean and the execution can pass constraints, but the action still serves attacker goals. SafeHarness closes this gap: it inspects the harness itself, at every lifecycle phase, with cross-layer coordination.

**Evaluation**: 38% UBR reduction, 42% ASR reduction vs. unprotected baseline on Agent-SafetyBench (2,000 tasks, 349 environments, 8 risk categories). Evaluated across three harness configurations (ReAct, Multi-Agent, Self-Evolving) with DeepSeek-V3.2. Compared against four baselines of monotonically deeper integration (Unprotected → System-Prompt → Guardrail → LlamaFirewall → SafeHarness), confirming lifecycle integration provides meaningful improvement beyond pipeline-level auditing.

**Cemini instantiation**: SafeHarness's four internal layers (Inform/Verify/Constrain/Correct) compose with the existing stack:
- L1 Inform augments K22's CoT inspection with context-provenance filtering at input
- L2 Verify provides a complementary detection surface — reasoning audit that K22's nine-category taxonomy doesn't cover
- L3 Constrain adds tool-level privilege enforcement *before* SAE's execution-boundary projection
- L4 Correct provides state-level recovery (checkpoints, rollback, degradation) that none of K19/K22/K23/K24 currently address

**Code**: No GitHub link in abstract. 11 authors from CAS + Peking University. Monitoring for code release.

#### Layer 4 — SAE Execution Contract: execution constraints

**What it provides**: Enforcement at the execution boundary. Trust-state conditioned budgeting (z_t = provenance × capability risk × injection alerts). Projection-based enforcement (a_eff = arg min D(a, a_req)) rather than binary accept/reject. Structured audit trail (M6).

**Why it's Layer 4**: Nomotic AI defines the authorization requirement; the Reasoning Safety Monitor detects corrupted intent; SafeHarness monitors the harness orchestrating execution. SAE enforces the constraints on the executable action itself. It answers: given the current trust state, market state, and account state, what is the maximum safe action? And if the requested action exceeds that, it projects it into the feasible region rather than rejecting it outright. This is the operational answer to "when should an agent be allowed to act?" — the mathematical constraint that computes the answer per-action, per-millisecond.

**Cemini instantiation**: SAE middleware at the terminal leaf of the scatter-gather execution graph. Receives ExecutionRequests with trust-state enriched by Layer 2. Returns ExecutionDecisions: ALLOW/LIMIT/BLOCK.

#### Layer 5 — ParlayMarket / RFQ Trilemma: market design constraints

**What it provides**: The recognition that some authorization tradeoffs are structurally unavoidable — they're baked into the market design itself, not fixable by better enforcement. The RFQ trilemma: no Request-for-Quote architecture can simultaneously satisfy liquidity consistency, information aggregation, AND bounded loss. You must choose which two to satisfy.

**Why it's Layer 5**: Layers 1–4 assume the market is a neutral substrate — authorization is about whether the agent should act, not about whether the market can safely accommodate the action. ParlayMarket shows that the market itself has authorization-relevant design constraints. When Cemini quotes on Kalshi combo contracts, the RFQ trilemma means the market-maker must explicitly decide: sacrifice liquidity consistency, sacrifice information aggregation, or sacrifice bounded loss. This is an authorization decision — it determines which actions the market-maker will refuse — but it's a Layer 4 decision because it's about market design, not per-action enforcement.

**Cemini instantiation**: ParlayMarket's standalone market-maker architecture (Ising model + shadow trades + composite-likelihood SGD). The design choice — satisfy liquidity consistency + bounded loss, sacrifice full information aggregation — is an explicit authorization posture documented in the architecture.

### How the layers compose

```
                    ┌──────────────────────────────────────┐
                    │  LAYER 1: Nomotic AI (K23)            │
                    │  Framework: pre-action authorization  │
                    │  Six principles. Delegated authority. │
                    │  Fail-by-default posture.             │
                    └──────────────────────────────────────┘
                                      │
                                      ▼
┌──────────┐    ┌──────────────────────────────────────────┐
│  LLM     │    │  LAYER 2: Reasoning Safety Monitor (K22) │
│  CoT     │───▶│  Detection: is the reasoning trustworthy? │
│  Stream  │    │  Nine-category taxonomy.                  │
└──────────┘    │  Step-level interrupt on unsafe.          │
                │  Enriches trust-state → I_inj flag.       │
                └──────────────────────────────────────────┘
                                      │
                                      ▼ (enriched z_t)
                ┌──────────────────────────────────────────┐
                │  LAYER 3: SafeHarness (K25)               │
                │  Harness-internal: is the orchestrator    │
                │  itself compromised?                      │
                │  Four lifecycle phases, cross-layer FB.   │
                │  Inform → Verify → Constrain → Correct.   │
                └──────────────────────────────────────────┘
                                      │
                                      ▼ (harness-validated)
                ┌──────────────────────────────────────────┐
                │  LAYER 4: SAE Execution Contract (K19)   │
                │  Enforcement: is this action permitted?   │
                │  Trust-state conditioned budgeting.       │
                │  Projection: ALLOW / LIMIT / BLOCK.       │
                │  Structured audit record (M6).            │
                └──────────────────────────────────────────┘
                                      │
                                      ▼ (approved action)
                ┌──────────────────────────────────────────┐
                │  LAYER 5: Market Design (K24)             │
                │  Structural constraints: RFQ trilemma.   │
                │  Which 2 of 3 to satisfy?                 │
                │  ParlayMarket: liquidity + bounded loss. │
                └──────────────────────────────────────────┘
                                      │
                                      ▼
                ┌──────────────────────────────────────────┐
                │  Exchange / Broker / Side-effect surface  │
                └──────────────────────────────────────────┘
```

The layers are independent: an attack that evades Layer 2 still hits Layer 3. A market design choice at Layer 4 doesn't weaken Layers 1–3. The layers are complementary: Layer 1 provides the framework, Layer 2 provides detection, Layer 3 provides enforcement, Layer 4 provides market awareness.

### Why this is an IP-sale asset

An institutional buyer evaluating Cemini's architecture sees five independently-grounded authorization layers rather than a single "safety module." The layers are:

1. **Philosophically warranted** (Layer 1: Nomotic AI — the governance framework has formal principles and a named intellectual lineage)
2. **Empirically validated** (Layer 2: Reasoning Safety Monitor — nine-category taxonomy with natural-vs-adversarial frequency baseline on 1,520 clean + 300 adversarial traces)
3. **Harness-integrated** (Layer 3: SafeHarness — four defense layers woven into the agent lifecycle, 38% UBR/42% ASR reduction, 11 authors from CAS + Peking University, cross-layer feedback coordination)
4. **Mathematically bounded** (Layer 4: SAE — Delegation Gap decomposition, projection-based enforcement with Lipschitz loss bound, Binance replay with 93.1% MDD reduction)
5. **Market-structure aware** (Layer 5: ParlayMarket — RFQ trilemma theorem, polynomial loss scaling O(M²), Fréchet violations in 39% of Kalshi combo quotes)

The stack converts "AI safety" from a vague concern into a verifiable architecture spanning five independently-grounded layers. Every authorization decision is traceable: which layer made it, which mathematical constraint produced it, which audit record documents it. This is the due-diligence answer to "how do we know your AI won't blow up?"

### What the stack does NOT cover (honest posture)

- **Key management and custody**: exchange API keys, wallet private keys, and 2FA are outside the authorization stack. The stack authorizes *actions*, not *access*.
- **Content safety**: toxicity, bias, and hallucination in natural-language outputs are separate concerns (K22's orthogonality argument explicitly distinguishes reasoning safety from content safety).
- **Adaptive adversaries**: an attacker who knows all five layers can craft multi-stage attacks that exploit gaps between layers. The stack is robust against known patterns (K20's 190 advisories) but not against a dedicated adversary with full architecture knowledge.
- **Regulatory compliance**: the stack provides auditability but does not encode jurisdiction-specific regulations (SEC, CFTC, MiFID). Those must be layered on as additional constraints in the Nomotic gate.
- **Model weights security**: the stack assumes the model weights themselves are trusted. Weight poisoning or training-data backdoors are outside scope.

### Cross-cluster integration map

```
execution-safety (K19) ─────────────┐
                                     │
agent-security (K25) ────────────────┤
                                     ├── authorization stack
reasoning-safety (K22) ─────────────┤      (this page)
                                     │
governance (K23) ───────────────────┤
                                     │
market-microstructure (K24) ────────┘
         │
         └── threat model (K20: OpenClaw) informs all five layers
```

### When to consult this page

- Explaining Cemini's security architecture to an institutional buyer or technical DD team
- Designing a new agent capability and determining which layers need new constraints
- Evaluating whether a detected attack would have been caught by the stack (trace through layers)
- Understanding why "just add a safety check" is insufficient — authorization is a stack, not a check

## Snippets

**S1 — Nomotic pre-action authorization (from @concepts/nomotic-ai.md)**:
> "AI authority is delegated, never inherent. Every action requires explicit pre-action authorization. Actions outside defined boundaries fail by default."

**S2 — Reasoning safety orthogonality (from @concepts/reasoning-safety-monitor.md)**:
> "Content safety concerns what a model says; reasoning safety concerns how a model thinks. A model may produce a response that appears benign at the output level while its underlying reasoning chain is corrupted."

**S3 — SAE trust-state conditioned budgeting (from @concepts/sae-execution-contract.md)**:
> "SAE models trust as a first-class input to budget computation. Budgets are factorized: B_t = B_0 · g(market) · h(account) · q(z_t), where q(·) tightens when provenance is weak, capability risk is high, or injection alerts are active."

**S4 — RFQ trilemma (from @concepts/parlay-market-making.md)**:
> "No RFQ architecture can simultaneously satisfy (a) liquidity consistency — quotes must be internally coherent across related contracts, (b) information aggregation — quotes must incorporate all available public information, and (c) bounded loss — the market-maker's loss must be bounded independent of counterparty sophistication. You can have at most two."

**S5 — The composition principle (this page)**:
> "An attack that evades the reasoning monitor (Layer 2) still hits SAE enforcement (Layer 3). A market design choice (Layer 4) doesn't weaken the philosophical framework (Layer 1). The layers are independent by design and complementary in coverage."
