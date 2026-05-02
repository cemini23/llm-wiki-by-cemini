---
title: Nomotic AI — Pre-Action Authorization Architecture
type: concept
tags: [concept, nomotic-ai, agent-governance, execution-gate, deterministic-validation, cemini-stack-design]
keywords: [nomotic, pre-action authorization, trade intent payload, pydantic gate, governance-as-architecture, delegated-authority, fail-by-default, execution-safety]
related:
  - sources/ai-7-4-6.md
  - sources/4-6-links.md
  - sources/4-4-link-re-2.md
  - sources/3-26-b.md
  - concepts/algorithmic-stopping-conditions.md
  - concepts/llm-agent-systems.md
  - concepts/cryptographic-audit-trail.md
  - concepts/ip-sale-readiness.md
  - sources/3-29-15.md
  - concepts/agent-authorization-stack.md
maturity: validated
created: 2026-04-30
updated: 2026-05-01
---

## Relations

- @sources/ai-7-4-6.md — **K23 deep-read; primary source.** Chris Hood (Jan 2026). The paper that introduced the term "Nomotic AI" — confirms every core claim in this concept page.
- @sources/4-6-links.md — K12 deep-read; secondary-source evaluation that first surfaced the Nomotic AI concept into the wiki.
- @sources/4-4-link-re-2.md — K12 deep-read; Sovereign-OS YAML Charter + asymmetric TrustScore + legal-action masking — convergent patterns.
- @sources/3-26-b.md — K10 deep-read; LangGraph interrupt()/Command(resume=...) — the brain-side mechanism that the Nomotic gate controls.
- @concepts/llm-agent-systems.md — cluster hub; Nomotic AI is the governance dimension of LLM agent systems.
- @concepts/cryptographic-audit-trail.md — every Nomotic gate decision (pass/fail + payload hash) is immutably logged.
- @concepts/ip-sale-readiness.md — Nomotic AI is the single strongest IP-sale narrative weapon: mathematically provable LLM containment.
- @concepts/agent-authorization-stack.md — K19+K22+K23+K24 cross-cluster synthesis; Layer 1 of the four-layer authorization architecture.

## Raw Concept

Synthesized originally from three converging K12 secondary sources. **K23 (2026-05-01): confirmed against the primary paper** — Chris Hood, "Nomotic AI: The Governance Counterpart to Agentic AI" (Jan 2026, 26p, independent). The paper introduces Nomotic AI as a conceptual category, not an implementation guide. The K12 secondary sources faithfully transmitted the core ideas; this concept page adds Cemini-specific architectural application that the paper does not contain. The paper's six formal principles (Governance as Architecture, Pre-Action Authorization, Explicit Authority Boundaries, Verifiable Trust, Ethical Justification, Accountable Governance) are now incorporated below. [CONFIRMED]

## Narrative

### Definition

Nomotic AI is the governance counterpart to Agentic AI. Where agentic systems focus on capabilities and executing workflows, Nomotic AI establishes the laws, boundaries, and constraints dictating what a system is permitted to do. The core architectural principle: **AI authority is delegated, never inherent. Every action requires explicit pre-action authorization. Actions outside defined boundaries fail by default.**

### Etymology

From Greek *nomos* (νόμος) — law, rule, custom, governance. In classical Greek thought, *nomos* was humanly constructed and deliberately established, distinct from *physis* (nature). The etymology is deliberate: AI governance is a human responsibility. The rules don't emerge from the technology. [Source: ai 7 4:6.pdf pp.8–9]

### The agentic-nomotic duality (from primary paper)

| Dimension | Agentic AI | Nomotic AI |
|-----------|-----------|-----------|
| Focus | Capability | Accountability |
| Core Question | What can this system do? | What should this system do? |
| Characteristic Verbs | Perceive, Reason, Plan, Act | Govern, Authorize, Trust, Evaluate |
| Function | Integration Layer | Governance Layer |
| Based On | Actions | Directives (Laws) |
| Risk When Absent | Inert governance | Ungoverned capabilities |
| Temporal Emphasis | Runtime execution | Pre-action authorization |

"Actions without laws are chaos. Laws without actions are inert." [Source: ai 7 4:6.pdf pp.16–17, Table 1]

### Intent vs. authority

A key distinction from the primary paper: **intent** originates with users (it lives in the prompt, the instruction, the goal). **Authority** lives in the governance layer (it answers: is this action permitted?). A user may intend for an AI system to perform an action that the system is not authorized to perform. The nomotic layer governs whether the agentic layer may act. This reframes AI failures: most are not failures of action but failures of authorization — the governance was inadequate, not the system. [Source: ai 7 4:6.pdf pp.13–15]

### Six formal principles (Hood 2026)

1. **Governance as Architecture** — Governance is an architectural decision, not a compliance layer. Designed in from the beginning, not retrofitted. When architectural, responsible behavior is the default.

2. **Pre-Action Authorization** — Authorization must be verified before execution, not reviewed after. Post-hoc review is insufficient: by the time review occurs, harm is done.

3. **Explicit Authority Boundaries** — AI systems possess only the authority deliberately delegated to them. Implicit authority is dangerous. Actions outside explicit boundaries fail or escalate, never proceed by default.

4. **Verifiable Trust** — Trust is earned through evidence and verified through observation. Not assumed from capability. Trust is specific to actions, conditions, and contexts; calibrated and adjusted over time.

5. **Ethical Justification** — AI actions must be justifiable, not merely executable. Explainability is a precondition: if an action cannot be explained, it cannot be justified. Ethics is woven throughout governance, not a separate constraint.

6. **Accountable Governance** — AI systems cannot be accountable; they are tools. Accountability rests with humans who define rules, grant authorities, and set ethical standards. Every rule has an owner; every authorization traces to a responsible party.

[Source: ai 7 4:6.pdf pp.16–20, §5]

### Cemini application of the six principles

1. **Delegated authority (Principle 3)** — The LLM brain possesses zero inherent authority. It cannot directly call any broker API. All it can do is emit a "Trade Intent Payload" — a structured proposal that must pass deterministic validation before execution.

2. **Pre-action authorization (Principle 2)** — Every trade intent is validated by a pure-Python Nomotic Execution Service before reaching any broker interface (Kalshi, Alpaca, OANDA). Validation is deterministic: Pydantic v2 models with `@field_validator` decorators enforce margin requirements, exposure limits, position sizing, and venue-specific rules.

3. **Fail-by-default (Principle 3 corollary)** — If validation fails for any reason, the trade is rejected. There is no fallback, no "ask the LLM to try again," no soft degradation path. The gate is binary: pass through or block.

4. **Governance-as-architecture (Principle 1)** — Constraints are embedded in the execution layer, not prompt-engineered. The MAPPO policy network's outputs are clamped via tensor operations during RL training. Runtime constraints are Pydantic validators, not system-prompt instructions.

### Architecture

```
LangGraph Brain (5-agent ensemble)
        ↓
   Trade Intent Payload (Pydantic v2 model)
        ↓
   Nomotic Execution Service
   ├── Margin validation (account.available >= intent.margin_required)
   ├── Exposure validation (position + intent.size <= limits.max_exposure)
   ├── Venue validation (intent.venue in authorized_venues)
   ├── Rate-limit validation (intents_last_60s < venue.max_rate)
   └── Compliance validation (no wash-trade, no spoofing patterns)
        ↓
   ┌─ PASS → Multi-broker EMS → broker API
   └─ FAIL → rejected + audit trail entry
```

The brain never sees the broker API. It sees only the Trade Intent Payload schema and the pass/fail response. This is not a soft guideline — it's a hard architectural boundary enforced by Docker network policies (the brain container cannot reach the broker API network).

### Trade Intent Payload schema

```python
from pydantic import BaseModel, field_validator
from datetime import datetime

class TradeIntent(BaseModel):
    venue: str  # "kalshi" | "alpaca" | "oanda"
    symbol: str
    direction: str  # "long" | "short"
    size: float
    limit_price: float | None = None
    stop_loss: float | None = None
    take_profit: float | None = None
    agent_id: str  # which agent proposed this
    debate_round: int  # which debate round produced this
    confidence: float  # MAPPO confidence score [0, 1]
    feature_vector_hash: str  # SHA-256 of the 34-dim feature vector at decision time

    @field_validator("venue")
    @classmethod
    def venue_authorized(cls, v):
        if v not in ("kalshi", "alpaca", "oanda"):
            raise ValueError(f"Unauthorized venue: {v}")
        return v

    @field_validator("size")
    @classmethod
    def size_positive(cls, v):
        if v <= 0:
            raise ValueError("Size must be positive")
        return v

    @field_validator("confidence")
    @classmethod
    def confidence_bounded(cls, v):
        if not 0 <= v <= 1:
            raise ValueError("Confidence must be in [0, 1]")
        return v
```

### Relationship to other Cemini patterns

- **Cryptographic audit trail**: Every Nomotic gate decision is immutably logged — the Trade Intent Payload, the Pydantic validation result (pass/fail + which validator failed), the timestamp, and the SHA-256 chain entry. This provides forensic-grade traceability for every rejected trade.

- **Algorithmic stopping conditions**: The Nomotic gate enforces a hard debate-round cap (max 3) as part of its validation. If `debate_round > 3`, the payload is rejected regardless of content. This mechanically prevents agreement-spiral API burn.

- **Sovereign-OS Charter**: The YAML-declarative approach from @sources/4-4-link-re-2.md can serve as the human-readable configuration layer for Nomotic boundaries. Charter rules compile to Pydantic validators.

- **MAPPO retrain window**: During RL training, the same Nomotic boundaries are enforced as tensor masks over the action space. This ensures the policy never learns to propose trades that would be rejected at runtime — governance is embedded in the neural architecture, not just the execution layer.

### What Nomotic AI is NOT

- **Not a prompt engineering pattern** — "Trade safely" in a system prompt is not Nomotic. The constraints must be mechanically enforced.
- **Not a post-hoc audit** — Reviewing trades after execution is not Nomotic. Authorization must be pre-action.
- **Not a human-in-the-loop gate** — Nomotic validation is deterministic and automated. Human review is too slow for the execution path (though it can supplement for anomalous patterns).

### IP-sale relevance

This is the single strongest IP-sale narrative weapon in the Cemini arsenal. Institutional acquirers (hedge funds, banks) are paralyzed by compliance risk around autonomous AI trading systems. The Nomotic architecture provides a mathematically verifiable answer: the LLM brain is completely sequestered behind deterministic, auditable authority boundaries. Every trade can be traced: which agent proposed it, which validators approved it, which feature vector informed it. This directly neutralizes the "black box AI" due diligence objection.

### Sources and convergence

- @sources/4-6-links.md §Nomotic AI — primary source. "AI authority is delegated, never inherent; every action requires pre-action authorization; actions outside defined boundaries fail by default."
- @sources/4-4-link-re-2.md §Target Domain 1 — Sovereign-OS YAML Charter with asymmetric TrustScore (+5/−15). §Target Domain 4 — legal-action masking as binary mask over action space before policy softmax.
- @sources/3-26-b.md §Q1 — LangGraph interrupt()/Command(resume=...) as the brain-side mechanism the Nomotic gate controls.
- @sources/4-6-links.md §AI Agency — "Tool-Gating to Prevent Hallucination: before an agent can evaluate a trade, the system must assert via Pydantic validation that the agent has successfully executed the necessary data-retrieval tools."

## Snippets

> "Nomotic AI: the governance counterpart to Agentic AI. Agentic = what a system CAN do; Nomotic = what a system SHOULD do. AI authority is delegated, never inherent; every action requires pre-action authorization; actions outside defined boundaries fail by default." [Source: 4_6 links.docx §Nomotic AI]

> "Pre-action Authorization and Explicit Authority Boundaries constitute the ultimate architectural defense mechanism for autonomous systems. The LangGraph brain must possess zero inherent authority or direct API access to execute a trade. Instead, it must generate a Trade Intent Payload passed to a strict, deterministic Nomotic Execution Service." [Source: 4_6 links.docx §Nomotic AI]

> "Governance as Architecture demands that oversight mechanisms operate at the execution speed of the agentic system. For the 62K parameter PyTorch MAPPO model, this means constraints on the outputs must be enforced mathematically via tensor clamping or reward penalization during the RL retrain window." [Source: 4_6 links.docx §Nomotic AI]

> "Legal-action masking: constraining RL action spaces to legally permissible trades only. Binary mask over action space before policy softmax — computationally free." [Source: 4_4 link re 2.docx §Target Domain 4]

> "Sovereign-OS: Declarative agent governance via YAML Charter. Asymmetric TrustScore: +5 for compliant actions, −15 for violations — 3:1 penalty ratio makes violations cumulatively disqualifying." [Source: 4_4 link re 2.docx §Target Domain 1]
