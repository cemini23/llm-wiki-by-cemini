<!-- bundle_sha256_prefix: e1794a7b9b4d | entries: 15 -->
# Conductor reviewer — passive injection context bundle

> Generated 2026-07-10 from `conductor/reviewer/corpus/manifest.yaml`.
> Do not edit by hand — run `bash scripts/build_reviewer_context.sh`.

This bundle is injected into the K37 reviewer-agent prompt at invocation time.
It is **not** retrieved via kb_search. Sprint 5 prod wiring is DEFERRED.

---

## [trigger_policy] policy.yaml (verbatim)

# Trigger policy for K37 reviewer-agent v2 (selective-trigger gating).
# Primary consumer: XSP killer bot — Robinhood long-call lanes A/B via EMS.
#
# Each tool listed below routes through one of three buckets:
#
#   always-review         Invoke reviewer-agent before every call.
#   skip-review           Dispatch directly without reviewer-agent.
#   review-on-uncertainty Review iff base-agent confidence < uncertainty_threshold.
#
# Tools NOT enumerated default to always-review (safe-default).
#
# PRE-PROD: side-effecting order tools require lane_id — see lane_id_contract.

tools:

  place_order:
    bucket: always-review
    notes: Robinhood XSP options via EMS; requires lane_id + lane hard limits (regime is context, not universal GREEN gate)
  withdraw:
    bucket: always-review
    notes: moves funds off broker; irreversible (rare on XSP path)
  close_position:
    bucket: always-review
    notes: XSP exit; lane_id selects Lane A vs B hard limits
  cancel_order:
    bucket: always-review
    notes: cancels pending Robinhood order
  notify_operator:
    bucket: always-review
    notes: Tier-2 MCP alert (XADD operator_alerts)

  get_price:
    bucket: skip-review
    notes: XSP or underlying quote; lane_id not required
  get_regime_status:
    bucket: skip-review
    notes: intel:playbook_snapshot regime — context for sizing/alerts; not a universal entry block for XSP lanes
  get_playbook_snapshot:
    bucket: skip-review
    notes: full playbook Redis snapshot

# ---------------------------------------------------------------------------
# lane_id contract — PRE-PROD GATE (Sprint 5 / XSP EMS wiring)
# ---------------------------------------------------------------------------
# Base agent MUST attach lane_id on place_order / close_position / cancel_order.
# Reviewer uses lane_id to select rule set; must NOT second-guess strategy.
# Validator: conductor.reviewer.lane_contract.validate_provisional_call
# Hub: wiki/concepts/reviewer-passive-injection-corpus.md

lane_id_contract:
  version: 1

  required_on_tools:
    - place_order
    - close_position
    - cancel_order

  allowed_lane_ids:
    - id: lane_a
      label: "Lane A — 14–60 DTE overnight swing; v1 exit monitor only"
      automation_v1: exit_only
    - id: lane_b
      label: "Lane B — LEAPS core book; v1 alerts + manual entry"
      automation_v1: alerts_only
    - id: lane_c
      label: "Lane C — mid-dated ~10:30 ET; not v1 automated"
      automation_v1: not_automated
    - id: lane_d
      label: "Lane D — weeklies; not v1 automated"
      automation_v1: not_automated
    - id: manual
      label: "Operator confirm-card / discretionary"
      automation_v1: manual_only
    - id: smb_put_credit
      label: "SMB short put-credit — orthogonal to long-call lanes"
      automation_v1: not_automated
    - id: hl_shadow
      label: "Hyperliquid SP500 perp timing shadow — no XSP options"
      automation_v1: not_automated

  reviewer_verdict_mode:
    place_order: refuse_only
    close_position: refuse_only
    cancel_order: refuse_only

  reviewer_mandate:
    # Prebind Assurance (CAGE-1 / K155): prove control before EMS bind —
    # validate_provisional_call runs before LLM reviewer; refuse_only holds
    # action until approved or refused (no silent revise into binding order).
    - "Do not second-guess strategy, edge, or timing."
    - "lane_id selects which hard-limit rule set applies; never cross-apply lanes."
    - "Refuse (do not revise order arguments) on place_order, close_position, cancel_order."
    - "Do NOT refuse place_order solely because regime is not GREEN — Lane B dip accumulation and related variants are designed for YELLOW/RED drawdown windows."
    - "Regime informs sizing caps and operator alerts; lane-specific dip rubrics override portfolio GREEN-only framing."
    - "Refuse automated place_order for lane_c, lane_d, smb_put_credit, hl_shadow until dedicated tracks ship."
    - "Lane A v1: allow close_position per exit rules; refuse automated place_order (entry is manual)."
    - "Lane B v1: refuse automated place_order; alerts and manual entry only."

# ---------------------------------------------------------------------------
# regime_entry_policy — lane-specific (reviewer context; NOT universal GREEN gate)
# ---------------------------------------------------------------------------
# Macro Weather GREEN/YELLOW/RED still gates brain/orchestrator and Kelly sizing.
# XSP long-call lanes may add risk in non-GREEN regimes when dip rubric fires.

regime_entry_policy:
  default_reviewer_posture: context_only  # never refuse solely on non-GREEN

  by_lane:
    lane_a:
      entry_regime: discretionary
      notes: Tactical overnight swing; regime informs sizing — not GREEN-only
    lane_b:
      entry_regime: dip_accumulation
      notes: LEAPS core book — accumulate on dips; YELLOW/RED entries expected
    lane_c:
      entry_regime: lane_specific
      notes: Mid-dated ~10:30 ET rule; not v1 automated
    lane_d:
      entry_regime: lane_specific
      notes: Weeklies; informed-bet tier; not v1 automated
    manual:
      entry_regime: operator_discretion
      notes: Confirm-card path; regime is advisory context only
    smb_put_credit:
      entry_regime: orthogonal
      notes: Short premium track — separate regime YAML when automated
    hl_shadow:
      entry_regime: shadow_only
      notes: HL perp timing shadow — no XSP options entries

---

## [reviewer_rubric] @osint-wiki/concepts/reviewer-agent-inference-time-feedback.md

## Narrative

### The pattern

Standard tool-calling agents loop on `propose_call → execute_tool → observe_result → critique`. Errors caught at the `critique` stage are already side-effecting — money spent, orders placed, irreversible state mutated. The reviewer-agent pattern interposes a second model between `propose_call` and `execute_tool`:

```
base_agent.propose_call(query, context)
  → reviewer_agent.review(provisional_call, query, context)
    → (approve | revise(new_call))
  → execute_tool(approved_call)
```

The reviewer is a **distinct model**, ideally a reasoning-class model (o3-mini-class), with a prompt rubric covering directness/parsimony, completeness across multi-step requests, argument fidelity, threshold inclusivity defaults, units/scales normalization, and explicit error criteria.

### Empirical envelope

From the source paper:

| Axis | Headline |
|------|----------|
| BFCL irrelevance detection | **+5.5%** over baseline |
| τ²-Bench (multi-turn, stateful) | **+7.1%** over baseline |
| BFCL latency (mean) | **6.2× slower** single-turn |
| τ²-Bench duration (mean) | **2.4× slower** multi-turn |
| Reviewer model selection | o3-mini → **3.0:1** benefit:risk; GPT-4o → **2.1:1** |
| GEPA prompt-opt layer | adds **+1.5–2.8%** on top of reviewer |

The Helpfulness-Harmfulness framing is the paper's key methodological contribution:
- **Helpfulness**: fraction of base-agent errors that the reviewer corrects
- **Harmfulness**: fraction of *correct* base outputs that the reviewer degrades

A reviewer is net-positive iff helpfulness > harmfulness, but the *ratio* lets you tune the system (reviewer strictness, model class, prompt) against a single scalar.

### Architectural axes for tuning

Three orthogonal axes, all tunable without retraining the base agent:

1. **Reviewer model class** (reasoning vs non-reasoning). Reasoning models win materially.
2. **Reviewer prompt** (manual rubric vs GEPA-optimized). GEPA compounds on top of model selection.
3. **Reviewer trigger policy** (review every call vs selective gating on high-stakes calls). Paper reviews every call; production deployment will want a trigger filter to avoid the 6.2× single-turn latency hit.

### Cemini application

**Insertion point**: Conductor (Cemini's MCP orchestrator, see `@concepts/conductor-orchestrator.md`) already routes tool calls through an orchestrator node. Slot a reviewer stage between `provisional_tool_call` and `execute_tool`.

**Model assignment**:
- **Reviewer**: DeepSeek-R1 (reasoning-class, already in Cemini's pool) — natural o3-mini analogue
- **Base agent**: DeepSeek-V3 (fast, non-reasoning) — natural GPT-4o analogue

**Latency tolerability**: Cemini trading sessions are predominantly *multi-turn long-horizon* (a Polymarket weather thesis can run 40+ tool calls across 10+ minutes). The paper's 2.4× multi-turn amortization regime applies, not the 6.2× single-turn regime. For single-turn lookups (e.g., one-shot price quote), the reviewer should be **trigger-gated off** — only review on calls with side effects.

**Trigger policy (Cemini-specific)**:
- **Always review**: `place_order`, `withdraw`, `close_position`, `cancel_order`, anything mutating account state
- **Review on uncertainty**: tool calls where the base agent's confidence score is below a configurable threshold
- **Skip review**: read-only queries (`get_price`, `get_orderbook`, `get_news`)

This selective-trigger design recovers most of the single-turn latency floor while preserving the reviewer's gating benefit on the high-stakes minority of calls.

**Lane_id contract (XSP pre-prod)**: side-effecting order tools require `lane_id` on provisional calls so the reviewer applies the correct lane rule set and uses **refuse_only** (no `revise` of order args). Deterministic validation: `conductor.reviewer.lane_contract.validate_provisional_call`. Hub: @concepts/reviewer-passive-injection-corpus.md § Pre-prod gates.

**Prebind Assurance (K155)**: CAGE-1 term for proving control before an action binds — maps directly to `refuse_only` + `validate_provisional_call` before the LLM reviewer. Pair with Addy outer-loop **Verdict** / **Answerability** (`@sources/substack-rss-addy-osmani-2026-07-09-own-the-outer-loop.md`): reviewer is the inner-loop gate; operator owns ship/block and must be able to explain why.

### Open questions

1. **Domain transfer**: does the o3-mini 3:1 benefit:risk hold on Cemini's finance-specific tool surfaces (Kalshi, Polymarket, IBKR)? Needs empirical measurement on Conductor production trajectories before broad rollout.
2. **GEPA fit**: Cemini's `skill_audit.py` v0.5 already uses LLM-as-judge for brief auditing. Can the same infrastructure be reused as the prompt-optimization layer for the reviewer? Reduces engineering surface.
3. **Reviewer cost ceiling**: if the reviewer runs at every high-stakes call, what's the total monthly DeepSeek-R1 cost on a typical Cemini trading load? Need a cost model before commit.
4. **Failure mode**: paper measures harmfulness as % of correct outputs degraded, but doesn't characterize *what kind* of degradation (false negatives vs over-cautious refusals). For finance, over-cautious refusals are particularly costly (missed trades). Need an audit pass on harmful-class trajectories specifically.

### Why this matters for the IP-sale-readiness thesis

Cemini's defensibility is the **stack architecture**, not any individual model. A reviewer-agent layer is exactly the kind of architecturally-distinctive component that strengthens the moat: it produces measurable benefit:risk ratios that are quotable in a sale prospectus, it composes with the existing Conductor design, and it's tunable along three axes without retraining a base model. Phase-0 prototype is ~200-400 LOC.

### Pairing with trajectory triage

This concept is the **inference-time** half of a complete agent-quality stack. Its complement is `@concepts/agent-trajectory-triage-signals.md` — cheap non-LLM signals computed *after* trajectory close-out to triage which trajectories are worth human review or RLHF preference data. Reviewer agent improves trajectories while they happen; signals select which trajectories matter for downstream learning.

## Snippets

> "We move evaluation into the execution loop at inference time: a specialized reviewer agent evaluates provisional tool calls prior to execution, shifting the paradigm from post-hoc recovery to proactive evaluation and error mitigation." [Source: Reinforced Agent.pdf p.1]

> "Our metrics reveal that reviewer model choice is critical: the reasoning model o3-mini achieves a 3:1 benefit-to-risk ratio versus 2.1:1 for GPT-4o." [Source: Reinforced Agent.pdf p.1]

[Sources: @sources/reinforced-agent-tool-calling-feedback.md (arXiv 2604.27233v1)]

---

## [ems_p0_gaps] @osint-wiki/concepts/ems-execution-security-gaps.md

## Narrative

Three **P0** patterns — treat as blockers before expanding live Kalshi or enabling RBAC in production:

### 1. Side-door execution (Kalshi)

`ems/main.py` Redis listener bypasses `core/ems/router.py` for Kalshi signals. Only stale-ticker skip remains; exposure/SAE/CVaR/PositionGate/TrustGate never run.

**Fix:** Route Kalshi through `router.execute()` (or shared `_run_gate_stack()` helper). Delete direct `kalshi_v2.place_order()` except inside adapter after gates pass.

### 2. PositionGate error ≠ block

When `adapter.get_position()` returns `None`, gate returns `outcome="error"`. Router treats only `"block"` as hard stop → **uncovered shorts** on live adapters.

**Fix (choose one):** (a) treat `error` + `short_origination_attempt` as `block` when `SHORT_ENABLED=false`; (b) implement `get_position()` on Kalshi/Coinbase adapters; (c) fail-closed default for live brokers.

### 3. RBAC fail-open

`services/rbac/middleware.py` except block returns `allowed: True`. Postgres outage = open MCP.

**Fix:** Invert default — `except` → `allowed: False` + alert metric. Wire `RBAC_BYPASS_LOCALHOST` or remove from docs.

### Medium (P1–P2)

| Issue | Fix sketch |
|-------|------------|
| CI scope | Add matrix job: `pytest tests/ cemini_mcp/tests logit_pricing/tests …` or `pytest --collect-only` guard |
| Debate prometheus | Guard `_pipeline_violations` / `_hitl_gate_triggers` same as `_byzantine_checks` try/except |
| Archive janitor | Wrap CSV write + DELETE in txn; verify file size/checksum before DELETE; dry-run flag |

Prod brief: `briefs/2026-06-03_cemini-external-audit-remediation-cemini-prod.md` → `/opt/cemini/briefs/`.

---

## [sae_contract] @osint-wiki/concepts/sae-execution-contract.md

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

---

## [mitre_atlas_surface] @osint-wiki/concepts/mitre-atlas-taxonomy.md

## Narrative

### LLM-relevant techniques (Cemini's primary threat surface)

Cemini's threat model is dominated by techniques touching:
1. The **DeepSeek API surface** (LLM brain interactions)
2. The **FastMCP @mcp.tool decorators** (AI agent tool invocation)
3. The **kb-server + stash retrieval layer** (RAG context)
4. The **librarian wiki** (AI Ops infrastructure that lateral-movement targets)

Relevant subset of the 170 ATLAS techniques (out of 53 LLM-tagged + agent-tagged):

| Technique ID | Name | Tactic | Cemini surface affected |
|--------------|------|--------|-------------------------|
| AML.T0051 | LLM Prompt Injection | Execution | DeepSeek API call site (any user/document → prompt path) |
| AML.T0051.001 | Indirect Prompt Injection | Execution | RAG context, document ingest, librarian wiki |
| AML.T0054 | LLM Jailbreak | Privilege Escalation, Defense Evasion | DeepSeek API (boundary on what the brain will do) |
| AML.T0064 | Gather RAG-Indexed Targets | Reconnaissance | librarian wiki contents indexable by adversary |
| AML.T0065 | LLM Prompt Crafting | Resource Development | Adversarial preparation against Cemini-specific prompts |
| AML.T0067 | LLM Trusted Output Components Manipulation | Defense Evasion | Output rendering / structured-output post-processing |
| AML.T0068 | LLM Prompt Obfuscation | Defense Evasion | Bypass our pre-call hooks |
| AML.T0069 | Discover LLM System Information | Discovery | Reveal Cemini's system prompts, model identity |
| AML.T0070 | RAG Poisoning | Persistence | Plant adversarial entries in librarian wiki / kb-server |
| AML.T0071 | False RAG Entry Injection | Defense Evasion | Inject entries that influence retrieval |
| AML.T0080 | AI Agent Context Poisoning | Persistence | Poison stash episodic memory or session state |
| AML.T0081 | Modify AI Agent Configuration | Persistence, Defense Evasion | Touch FastMCP / Conductor config.yaml |
| AML.T0086 | Exfiltration via AI Agent Tool Invocation | Exfiltration | Use a poisoned MCP tool to leak data via tool params |
| AML.T0093 | Prompt Infiltration via Public-Facing Application | Initial Access, Persistence | User-facing input → DeepSeek path |
| AML.T0099 | AI Agent Tool Data Poisoning | Persistence | Tool inputs/outputs tampered to mislead the brain |
| AML.T0100 | AI Agent Clickbait | Execution | Confused-deputy-style agent action triggers |
| AML.T0101 | Data Destruction via AI Agent Tool Invocation | Impact | Tool-mediated destructive ops (DELETE, rm, etc.) |
| AML.T0103 | Deploy AI Agent | Execution | Adversarial deployment of an unauthorized agent |
| AML.T0104 | Publish Poisoned AI Agent Tool | Resource Development | Supply-chain attack on tools we install |
| AML.T0110 | AI Agent Tool Poisoning | Persistence | Modify @mcp.tool decorator behavior |

For full descriptions of any technique above: https://atlas.mitre.org/techniques/<ID> (e.g., https://atlas.mitre.org/techniques/AML.T0051 for LLM Prompt Injection).

### LLM-relevant mitigations

Out of 35 ATLAS mitigations, 11 directly inform Cemini-side defenses:

| Mitigation ID | Name | Cemini implementation locus |
|---------------|------|-----------------------------|
| AML.M0002 | Passive AI Output Obfuscation | Sanitize LLM-emitted text before downstream consumption |
| AML.M0007 | Sanitize Training Data | Vet any external-data ingest path for poison content |
| AML.M0008 | Validate AI Model | Sanity-check model behavior pre-deployment (cross-validate vs known-correct outputs) |
| AML.M0020 | Generative AI Guardrails | Pre-call hooks in `services/llm_analyst/deepseek_client.py`; system-prompt invariants |
| AML.M0026 | Privileged AI Agent Permissions Configuration | Explicit allowlist of MCP tools the brain can invoke |
| AML.M0027 | Single-User AI Agent Permissions Configuration | Per-session token budget; per-user execution context |
| AML.M0028 | AI Agent Tools Permissions Configuration | FastMCP tool registry — what each agent can call |
| AML.M0029 | Human In-the-Loop for AI Agent Actions | Manual confirmation gates for destructive / financially-impactful tool calls |
| AML.M0030 | Restrict AI Agent Tool Invocation on Untrusted Data | Don't let RAG-retrieved content trigger tool calls |
| AML.M0032 | Segmentation of AI Agent Components | Run brain, tools, RAG retrieval in separately-credentialed containers |
| AML.M0033 | Input and Output Validation for AI Agent Components | Schema-validate every tool input/output against a typed contract |

These map cleanly onto the existing Cemini agent-authorization-stack (`@concepts/agent-authorization-stack.md`):
- M0026/M0027/M0028 ⇒ K19 SAE execution contract (`@concepts/sae-execution-contract.md`)
- M0029 ⇒ Human-in-the-loop nodes in the LangGraph orchestrator
- M0030 ⇒ K22 reasoning safety monitor (`@concepts/reasoning-safety-monitor.md`)
- M0032 ⇒ Hetzner container topology + private-network isolation
- M0033 ⇒ FastMCP `@mcp.tool` typed signatures + return-schema validation

---

## [rlhf_critic_guardrail] @osint-wiki/concepts/rlhf-critic-bias.md

## Narrative

### Why this matters for Cemini specifically

Cemini deploys LLMs as **evaluators** in three places that this framework illuminates:

1. **Reviewer-agent (K37 prototype)** — DeepSeek-R1 gates side-effecting tools. Implements Mitigation 3 (evidence-weighted critique) and Mitigation 4 (audit-trail disclosure) in miniature. The framework justifies the reviewer-agent investment: without it, every evaluative LLM call is exposed to the structural negativity bias.

2. **`scripts/skill_audit.py` (laptop-side)** — currently checks brief-completeness, claim-evidence alignment, risk-discipline, phasing, prose-quality, regime-disclosure (v0.5). The 5-tell scorecard + 6-category Rhetorical Catalog are **portable audit primitives** that fit into the same harness. **Follow-up brief candidate**: opt-in `--rlhf-tell-mode` flag. *Deferred until user-gated authorization.*

3. **Tier-2 eval brief processing** — eval briefs feed Cemini's K-cycle adoption decisions. The mirror failure mode applies: when an LLM is prompted "evaluate this project for adoption," the asymmetric penalty for "I said skip and it was useful" exceeds "I said adopt and it was unfit." This is the **structural reason** behind K28+K30+K38's 6 mischaracterization catches. Phase-0 audit discipline is the human-in-the-loop counterweight.

### The 5 output patterns

| # | Pattern | Signature |
|---|---|---|
| 1 | **Interesting But Template** | Diplomatic open → 3-5 structural objections → "more work is needed" terminal |
| 2 | **Credentialing Prior** | Institutional affiliation modulates evaluation severity independent of content |
| 3 | **Unfalsifiable Objection** | Objections that apply to all research equally ("sample size may not generalize", etc.) |
| 4 | **Invention of Flaws** | Fabricated objections that contradict provided evidence |
| 5 | **Double Standard** | Endorsement requires overwhelming evidence; criticism requires only that an objection exists |

### The 4 proposed mitigations

| # | Mitigation | Layer | Cemini status |
|---|---|---|---|
| 1 | **Symmetric Reward Training** | Training | N/A — Cemini does not train models |
| 2 | **Evaluative Stance Disclosure** | Inference | Partial via reviewer-agent audit trail; could extend to skill_audit.py opt-in |
| 3 | **Evidence-Weighted Evaluation** | Architecture | Partial via reviewer-agent gating against artifact; could extend to skill_audit.py `check_claim_evidence` (v0.4) |
| 4 | **Anti-Laundering Watermarks** | Social | Partial via brief-audit footer disclosure conventions |

---

## [inkh_passive_injection] @osint-wiki/concepts/interaction-native-knowledge-harness.md

## Narrative

### Passive vs agent-driven retrieval

Paper argues **passive injection** beats agent-driven wiki-walk when planning overhead dominates irrelevant context `[TENTATIVE]`. Cemini conductor already biases toward **pre-classified tool routes** and kb_search fan-out rather than re-walking the whole vault each turn — compatible direction, not yet a formal InKH buffer.

### Posture

| Scope | Verdict |
|-------|---------|
| **Wiki-as-audit + ingest discipline** | **ALIGNED** — keep; see `@ccc-wiki/concepts/interaction-native-knowledge-harness.md` |
| **Prod trading temporal graph** | **REFERENCE** — no new memory write path on prod until EMS/RBAC + invalidation design reviewed |
| **Copy-trading / PM analysis agents** | **EVALUATE** — map paper workflows to `@concepts/polymarket-copy-trading-strategy.md` and bot state machines |

---

## [prod_blind_spots] @osint-wiki/concepts/production-trading-blind-spots.md

## Narrative

### How to use this page

When headline PnL "doesn't make sense," scan the table **top to bottom** before tuning alpha. Most rows are infrastructure/attribution — not model edge.

| # | Blind spot | Symptom | Early signal | Fix (Cemini prod where applicable) |
|---|------------|---------|--------------|-----|
| 1 | **PnL logic unversioned** | "Was profitable last month" after code change | Win rate shifts exactly at deploy date | @concepts/pnl-attribution-versioning.md — `logic_version` + `--scope current` |
| 2 | **Internal counter ≠ venue truth** | Bot journal WR >> exchange export | Polymarket CSV disagrees with bot stats | Reconcile to venue export; @Gustafssonkotte CSV rule |
| 3 | **Phantom WIN / assume-filled** | Risk gates no-op; ghost profits | "WIN" rows with no matching fill | Poll order status; never infer fill from timeout |
| 4 | **Duplicate fill events** | Double-counted position / 2× PnL | Same `order_id` twice in log window | Dedup in formatter (QuantPython trade-journal pattern) |
| 5 | **Silent fills post-API change** | State drift after CLOB upgrade | Positions wrong but no exceptions | Full reconciliation pass **≥ every 30s** [@0x_Punisher] |
| 6 | **One leg open (hedge break)** | "Market neutral" with directional bleed | Funding PnL OK, price PnL dominates | Treat partial fill as first-class; @concepts/perps-dex-funding-carry-strategy.md |
| 7 | **Broken upstream data** | Modules agree on nonsense | Chainlink vs exchange divergence | Multi-module conflict detector → SKIP |
| 8 | **Over-logging** | Can't find ERROR in GB/day noise | Debugging takes hours despite "full logs" | @concepts/trading-bot-logging-discipline.md |
| 9 | **Wrong profitability question** | Optimizing WR not expectancy | 70% WR at 57¢ entry still loses | Entry-price break-even math in @concepts/polymarket-bot-architecture.md |
| 10 | **UI shows stale/mock** | Dashboard green, prod red | `status: empty` vs `live` ignored | Envelope pattern on `/api/*`; @concepts/trading-dashboard-api-wiring.md |
| 11 | **Fair value change without version bump** | Sleeve attribution shifts | Hold/tactical mix changes after valuation deploy | Bump `brain_equity` in strategy registry |
| 12 | **Mixing Brinson daily attribution with trade PnL** | Two reports disagree | Step 60 portfolio report vs FIFO script | Different tables/questions — don't merge blindly |
| 13 | **Silent zero-trade abort** | Signal fired, nothing sent, no ERROR | Logs show decision but no `trade_aborted` reason | @concepts/zero-trade-edge-signal-diagnostics.md — tag `abort_reason` |
| 14 | **EMS gate bypass (side door)** | Live orders skip exposure/PositionGate | Kalshi fills with gates "enabled" in env | @concepts/ems-execution-security-gaps.md — route all brokers through router |

---

## [xsp_lane_framework] @osint-wiki/concepts/xsp-lane-trading-framework.md

## Narrative

### Lane map

| Lane | Tenor / style | Portfolio role | Automation posture (2026-06-14) |
|------|---------------|----------------|-------------------------------|
| **A** | **14–60 DTE**, overnight 1–2 session swing; non-January | Tactical overlay; nimble, risk-averse | **Prod brief shipped** — exit monitor first |
| **B** | **LEAPS** (>180 DTE); accumulate on dips | **Core book** (mentor: 30–50% risk budget conceptually) | **Prod brief shipped** — inventory + hedge alerts; manual entry |
| **C** | Mid-dated; **~10:30 ET** decision rule | Between A and B | Not v1 |
| **D** | **Weeklies** | Smallest structural role; informed-bet tier | Not v1 |

January expiries route to **Lane B** (LEAPS), not Lane A.

### Shared rules (all lanes)

- **Instrument:** XSP long **calls** on **Robinhood** (prod).
- **Direction:** No puts in long-call lanes (puts appear as **hedges** per @concepts/xsp-hedge-fund-core-book-thesis.md, not as short premium sleeve).
- **Regime (lane-specific — not universal GREEN-only):**

| Lane | Entry vs Macro Weather |
|------|------------------------|
| **A** | Tactical swing; regime informs sizing/alerts — **not** GREEN-only |
| **B** | **Accumulate on dips** — entries may target **YELLOW/RED** drawdown windows per dip rubric |
| **C / D** | Lane-specific rules when automated (not v1) |
| **Reviewer** | Hard limits + automation posture only — **must not refuse solely on non-GREEN regime** |

Portfolio-level Macro Weather still gates brain/orchestrator Kelly sizing; XSP dip lanes are an explicit exception. See @concepts/macro-weather-regime.md § XSP lane exception.
- **HL:** SP500 perp on Hyperliquid — **clock/timing shadow only**; no XSP options on HL.

### Lane A — exit rules (v1 defaults)

| Rule | Default |
|------|---------|
| Hard max loss | **-$75** / contract |
| Morning cut | Red past **10:30 ET** → close |
| Open + 30 min | Still red → close |
| Entry | Manual or confirm-card |

Canonical prod handoff: `briefs/2026-06-14_xsp-lane-a-overnight-swing-monitor-cemini-prod.md` (on `cemini-prod:/opt/cemini/briefs/`).

Canonical prod handoff: `briefs/2026-06-14_xsp-lane-b-leaps-hedge-monitor-cemini-prod.md` (on `cemini-prod:/opt/cemini/briefs/`).

### Lane B — hedge rules (v1 defaults)

| Field | v1 default |
|-------|--------------|
| Target delta band | 0.35–0.55 |
| DTE floor | >180d |
| Put hedge | Long protective puts; roll alert DTE <45, call Δ >0.65 |
| Entry | Manual only |
| Scorecard | Delta-adjusted risk return |

Dip entry rubric and per-add size caps — operator fills in prod YAML when ready.

---

## [xsp_regime_gate] @osint-wiki/concepts/macro-weather-regime.md

## Narrative

**[CONFIRMED — 2026-04-24 Track C audit]** Regime gate is real and enforced at the top of the stack. Evidence:
- `agents/regime_gate.py` — exports `REGIME_THRESHOLDS`, `CATALYST_PATTERNS`, `CATALYST_BONUS`, `_regime_gate`, `_REGIME_FALLBACK`.
- `cemini_contracts/regime.py` — typed Pydantic contract.
- `agents/orchestrator.py:16-22` imports the regime symbols and calls regime evaluation **before** signal processing.
- `intel:playbook_snapshot` Redis key (published by `trading_playbook/runner.py`) carries regime state; consumed by `cemini_mcp/server.py` tool #1 `get_regime_status`, `services/conviction_aggregator.py`, RL training, and regression tests.
- `tests/test_regime_gate.py` — coverage.
- Three-regime threshold structure observable at `regime_gate.py` lines 44–46: BUY/SELL/SHORT thresholds vary per regime.

No ticket required.

The **Macro Weather regime** is Cemini's simple, auditable portfolio-
gate classifier. It uses two signals on SPY — the 21-EMA and the
50-SMA — cross-referenced with a small set of FRED macro series, to
produce one of three regime states:

- **GREEN**: SPY > 21-EMA AND SPY > 50-SMA. Permissive regime. Full
  Kelly fraction allowed; new risk may be added.
- **YELLOW**: price between 21-EMA and 50-SMA (either side). Defensive.
  Kelly fraction halved; no new uncorrelated risk; existing positions
  tightened.
- **RED**: SPY < 21-EMA AND SPY < 50-SMA. Flat-or-hedge-only. All
  directional risk flattened or hedged; only market-making style
  strategies (Kalshi AS-in-logit, forex scalping) continue.

### Why these two moving averages
The trading-playbook research argues, and several RL-based regime
classifiers confirm in ablations, that 21-EMA captures ~1-month trend
and 50-SMA captures ~2.5-month trend; their crossover vs price
together identifies three distinct drawdown-risk regimes without
over-fitting.

### Why it sits at the top of the stack
The regime classifier is evaluated **before** the Kelly/CVaR risk
engine, which is evaluated **before** the strategy-specific signal.
This inverts the usual strategy-first → risk-second ordering and is
framed in the corpus as the **Game of Attrition doctrine**: survive
first, compound second. The regime flag is cheap to compute,
auditable, and caps all downstream risk — which is exactly what an
IP-sale buyer wants to see at the top of the stack.

### XSP lane exception (K37 reviewer / long-call playbook)

Macro Weather still gates **brain/orchestrator** paths and **Kelly fraction**
sizing at the portfolio level. **XSP long-call lanes are not universal
GREEN-only entry:**

| Lane | Regime posture |
|------|----------------|
| **Lane B (LEAPS)** | **Accumulate on dips** — entries may fire in **YELLOW/RED** when dip rubric triggers |
| **Lane A (tactical)** | Regime informs sizing/alerts; not a hard GREEN-only block |
| **K37 reviewer** | Must **not** refuse `place_order` solely because regime ≠ GREEN |

See @concepts/xsp-lane-trading-framework.md and `conductor/reviewer/policy.yaml`
`regime_entry_policy` block. Prod `agents/regime_gate.py` BUY blocks on
YELLOW/RED apply to **orchestrator** paths — XSP EMS manual/dip entries
use lane-specific YAML, not a blanket portfolio gate.

### External overlay — USDJPY yen-strength zone (K155)

Macro Charts Jul 10 chat (`@sources/macro-charts-paid-forward-chat-2026-07-10.md`) flags **USDJPY 162.25–162.50** as the clearest medium-term FX R/R zone amid Japan GPIF domestic-allocation / yen-strength narrative.

| Field | Posture |
|-------|---------|
| **Role** | **Advisory** macro-weather snapshot input — yen-strength / international macro context for **Lane B** dip framing |
| **Not** | A GREEN/YELLOW/RED gate substitute; does not block or permit XSP entries by itself |
| **Operator** | Log zone in `playbook_snapshot` comment block or trade journal when GPIF/yen headlines active |
| **CPI cluster** | Pair with Jul 15 CPI tighten on Lane A overnight size (`@concepts/macro-charts-gold-reversal-thesis-2026-06.md`) |

See also `@concepts/macro-charts-regime-signals.md` § Jul 10 2026.

---

## [cfd_provenance] @osint-wiki/concepts/context-fractured-decomposition-attacks.md

## Narrative

**Provenance gap:** safety monitors assume a contiguous trace; real pipelines split across sessions, tools, and agent instances while **files/logs/caches** persist. Attackers write benign payloads early, trigger harmful composition later via innocuous per-step tool calls.

**CFD vs STAC/backdoor:** intent-bearing pieces never co-occur in one monitor window — single-turn judges fail.

**Cemini mitigations (prescribed-not-built):**

| Layer | Action |
|-------|--------|
| Artifact writes | Lineage tags (source session, tool, trust tier) on `briefs/`, wiki edits, `.local/reports/` |
| MCP tool outputs | Treat cross-session file reads as untrusted until provenance verified |
| Eval | Extend MCP smoke matrix with CFD-style delayed-composition scenarios |

**Posture:** REFERENCE — prod brief for conductor artifact policy; cybersec-wiki handoff for offensive methodology.

## Snippets

> "Risk emerges only under delayed artifact-mediated composition."

> — [Source: arxiv-2606.09084-context-fractured-decomposition-attacks-on-tool.pdf, retrieved 2026-06-12]

---

## [kelly_sizing_caps] @osint-wiki/concepts/kelly-sizing-quarter.md

## Narrative

### When to override

Quarter-Kelly is the default, not the law. Operator overrides:

| Override | When |
|----------|------|
| **Half-Kelly** | High-conviction signal with multiple independent confirmations (e.g., Poisson + KL agree, fat-tail bucket says safe) |
| **Eighth-Kelly** | Unknown new strategy in dry-run / first 30 days live |
| **Full position cap** | Hard cap at N% of bankroll regardless of Kelly output — typically 5% per position |

### Cemini relevance

Cemini's planned Polymarket trading surface should encode quarter-Kelly as a **default**, not a **hardcoded** value:

- Strategy modules read a `kelly_fraction` config (default 0.25)
- Operator can override per-strategy via config
- A separate per-position **hard cap** (5–10% of bankroll) acts as the second safety layer

The hard cap is non-negotiable. Quarter-Kelly mis-sized by 2–3x is recoverable; full-portfolio Kelly mis-sized by 2–3x is a blow-up.

---

## [igac_intent_scope] @cybersec-wiki/concepts/intent-governed-tool-authorization.md

## Narrative

### Authorization gap

| Question | Traditional OAuth/MCP scope | IGAC adds |
|----------|----------------------------|-----------|
| Can credential call tool? | ✓ | — |
| Is call justified by **current user request**? | — | ✓ |

Example: read+export integration authorized statically — user asks for summary only → export tools should be **filtered from manifest** and export payloads rejected.

### Components

1. **Intent certificates** — session-scoped authority ceiling from parsed user goal
2. **Monotone narrowing** — intent can only shrink static grants
3. **Intent-aware manifest filtering** — planner sees reduced tool surface
4. **Intent–tool–payload consistency** — arg-level check before invoke

Mapped to **OpenPort** substrate in paper. Pilot: static auth still allowed **85.71%** of high-risk requests immediately — IGAC layering required.

### prod-mcp positioning

Sits **above** attested admission (2605.24248) and **before** planner:
- Admission: which servers/tools enter catalog
- **IGAC:** which subset matches current user intent
- AIRGuard/ChainCaps: runtime execution/composition

See `briefs/2026-06-24_igac-intent-governed-tool-auth-handoff.md`.

`[TENTATIVE]` — OpenPort pilot; Claude Code / lazy-tool mapping not lab-tested.

---

## [mcp_execution_invariants] @cybersec-wiki/concepts/mcp-execution-control-invariants.md

## Narrative

### Layer model

```
Connection layer (MCP)     → JSON-RPC, transports, tool registry, OAuth
Execution-control layer    → principals, grants, capabilities, data-pipe, audit
```

Wiki admission/DCI/SPI (@concepts/mcp-security-posture.md) gates **what enters the catalog**. Execution invariants gate **what each invocation may do** given catalog contents.

### Eight invariants → prod-mcp mapping [TENTATIVE]

| Invariant | Failure mode without it | prod-mcp / lazy-tool steal |
|-----------|-------------------------|----------------------------|
| **I1 Metadata non-authority** | Tool description becomes hidden invoke | Never parse tool metadata as policy; DCI + SPI |
| **I2 Grant-backed approval** | "Approve all" bypasses scope | Per-tool grants bound to user consent token |
| **I3 Canonical resources** | Path confusion / deputy reads | Stable resource IDs, not string prefixes alone |
| **I4 Principal binding** | Server acts as omnipotent deputy | Attribute every `tools/call` to session principal |
| **I5 Scoped invocation** | Capability creep mid-chain | ChainCaps/AIRGuard narrowing (@entities/tools/chaincaps.md) |
| **I6 Data-flow authorization** | PII from tool A → exfil tool B | Sink-specific budgets + class tags |
| **I7 Deny-path audit** | Silent block, no forensics | Log principal + capability + reason on deny |
| **I8 Protocol state** | Pre-init method dispatch | Strict MCP initialize/version gates |

---

## [agent_guardrail_failure_modes] @cybersec-wiki/concepts/agent-runtime-guardrails.md

## Narrative

### Failure modes (offensive / red-team lens)

| Mode | Mechanism | Source |
|------|-----------|--------|
| **Authority confusion** | Untrusted docs/MCP/skills *inform* reasoning but must not *authorize* writes, sends, or exec | AIRGuard |
| **Permission laundering** | Each tool call passes local ACL; composed workflow exfiltrates (read → summarize → send) | ChainCaps |
| **Sleeper attack** | Payload persists in session/memory/skills; benign later query triggers harm | PLANT |
| **Dual-surface injection** | Same bytes succeed on tool *output* or tool *description* depending on model | Surface paper |
| **Mid-session tool injection (MSTI)** | Third-party JS mutates WebMCP tool registry during task — hijack (race/AbortSignal) or frame via metadata | WebMCP 2606.06387 |
| **Error-path implicit authority** | Tool **error** JSON triggers corrective mode; adversarial recovery steps bypass skepticism | VATS 2606.07992 |
| **Memory poisoning (architectural)** | Single untrusted write to persistent memory corrupts all subsequent reasoning cycles | Containment gap 2606.12797 |
| **Trajectory steering** | Locally plausible fragments accumulate across turns; accepted outputs update persistent context without drift gate | GT-MCP 2606.10322 |
| **Over-privileged tool selection** | Agent picks broader **authorized** tool when narrow sufficient alternative exists; amplified by transient narrow-tool failures | TOOLPRIVBENCH 2606.20023 |
| **System prompt leakage** | Adversarial query exfiltrates hidden system/skill instructions — API keys, tool rules | LLM07 / 2606.18673 |
| **Confident guard misses** | PI detectors assign ~1.0 confidence to missed indirect hijacks | 2606.22659 |
| **Self-evolution persistence** | Attacks embed across evolution cycles; scanners miss evolution path | 2606.23075 MLAS |
| **Cross-tool description poisoning** | Poisoned metadata on tool A steers planner toward tool B; poisoned tool never invoked | Tool-Guard 2606.20922 |
| **Multi-tool threshold poisoning** | Shamir shares across tools; cooperative reconstruction; per-tool review reveals nothing | ShareLock 2606.27027 |
| **Lingering authority** | Subgoal-closed capability still visible in planner manifest | PORTICO 2606.22504 |
| **Intent-scope mismatch** | Static credential authorizes tool call unjustified by current user request | IGAC 2606.22916 |
| **Runtime implementation flaws** | Parser/dispatcher/memory-writer bugs in local agent source | CLAWAUDIT 2606.21071 |
| **Agent-phishing (offensive agent)** | Trojanized target artifact → download+execute without prompt injection | 2606.24496 |
| **Worker→orchestrator escalation** | Compromised worker reaches orchestrator secrets/APIs | 2606.24496 |
| **Tool-environment unreliability** | Clean P₀ tool assumptions break; agent fails to diagnose/recover | ToolBench-X 2606.25819 |
| **Semantic decoupling** | Natural-language intent hides unsafe tool args from LLM-as-Judge guards | ePCA motivation |

These are **not jailbreaks** in the classic sense — the model may comply with user intent while attacker-controlled context steers authorized access off-scope. [CONFIRMED] across AIRGuard + sleeper paper framing.

### Defense paradigms (defensive / blue-team lens)

1. **Formal pre-action verification (ePCA)** — SMT/formal constraints on intended actions before execution; maps unsafe transitions to UNSAT deadlocks. Aims for deterministic lower bound under explicit assumptions. `[TENTATIVE]` — lab validation pending; complements not replaces semantic alignment.

1b. **Probabilistic Datalog + DRO (2606.20510)** — when upstream PII/secret/redaction classifiers are noisy and **correlated**, sound upper bounds on policy-violation probability via distributionally robust optimization over Datalog derivation graphs (Praline/Soufflé). Complements ePCA for imperfect predicates; Phase-0 **Reference** until Google artifact ships. See @concepts/agent-probabilistic-datalog-verification.md.

2. **Runtime authority control (AIRGuard)** — Action-time least privilege: task authority → step authority (narrow-only), source/target trust, side-effect simulation, cross-step audit. Prompt-only policy insufficient in paper ablation.

3. **Composition-safe IFC (ChainCaps)** — MCP proxy; sink-specific capability budgets propagate by intersection (monotonic attenuation). Requires **trusted manifests** — naive manifests block only ~27% of attacks in paper.

4. **Stack with existing wiki tools** — @entities/tools/nvidia-skillspector.md (skill preflight), @entities/tools/defenseclaw.md (enterprise governance), @entities/tools/iron-proxy.md (egress), @concepts/agent-vm-sandboxing.md (substrate isolation).

5. **Layered skill governance (ClawHub study)** — On 67k+ OpenClaw skill versions, VirusTotal, static heuristics, and SkillSpector **disagree** (max pair overlap 10.4%; 81.9% of positives from one scanner only). SkillSpector leads on semantic agentic-risk; VT leads on bundled-code malware. **Do not** treat any single scanner as allow/block. [Source: arXiv:2606.01494] `[TENTATIVE]` — automated registry labels, not human ground truth.

6. **Integration-aware guards (AgentRedBench)** — Enterprise copilots with many SaaS integrations: poison via **read** on one app, harm via **write** on another. Chat-trained guards miss tool-response injections; paper’s AgentRedGuard targets that channel. Compare with AIRGuard authority model before adoption. [Source: arXiv:2606.02240] `[TENTATIVE]` — benchmark scenarios via maintainer channel.

---
