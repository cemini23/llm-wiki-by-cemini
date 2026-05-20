---
title: AI Organisation Design — Talent–Container, E²R, and the Organisational Layer
type: concept
tags: [concept, ai-organisation, agent-orchestration, multi-agent, organisational-layer, decision-pending, llm-agents]
keywords: [omc, talent, container, employee, e2r-tree-search, dag-fsm, self-evolution, hr-pipeline, organisational-interfaces, container-pattern, multi-runtime, talent-market, skill-vetting, sourcing-types]
related:
  - sources/omc-talent-container-paper.md
  - sources/gemini-dr-link-eval-2026-04-28.md
  - sources/sakana-trinity-llm-coordinator.md
  - sources/sakana-conductor-rl-orchestration.md
  - concepts/llm-agent-systems.md
  - concepts/scatter-gather-topology.md
  - concepts/hiring-quant-talent-philosophy.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/skill-vetting.md
  - concepts/librarian-server-architecture.md
  - concepts/context-compression-resume-pattern.md
  - entities/frameworks/langgraph.md
  - entities/frameworks/autoagent.md
  - entities/frameworks/fastmcp.md
  - entities/infrastructure/deepseek-api.md
  - sources/vibe-trading-hkuds.md
  - sources/gemini-dr-wave3-link-eval-2026-04-28.md
maturity: draft
created: 2026-04-28
updated: 2026-04-28
---

## Relations

- @sources/omc-talent-container-paper.md — canonical source (Yu et al, Huawei + UCL + U Liverpool, arXiv 2604.22446v1, 24 Apr 2026); this concept page is the synthesis and Cemini-applicability analysis of that paper
- @sources/gemini-dr-link-eval-2026-04-28.md — sibling source from the same 2026-04-28 indexing pass; multiple URLs in the Gemini wave (Vibe-Trading, AutoHedge) are agent-orchestration projects that could be studied as Containers under the OMC paradigm
- @sources/sakana-trinity-llm-coordinator.md — alternative orchestration paradigm (3-LLM coordinator, Sakana 2026); contrast with OMC's organisational-layer-above-coordination
- @sources/sakana-conductor-rl-orchestration.md — RL-driven orchestrator (Sakana 2026); OMC explicitly contrasts with this in its related-work section
- @concepts/llm-agent-systems.md — corpus index of agent papers; OMC is a top-tier 2026 paper to register here
- @concepts/scatter-gather-topology.md — concrete LangGraph runtime pattern (sibling-parallel coordination); OMC reframes LangGraph as one Container family among three (LangGraph, Claude Code session, script-based). This concept page is the parent abstraction; scatter-gather is one runtime instance under it
- @concepts/wiki-tooling-evaluation.md — WTE Wave 2 evaluated `agency-agents` (Type-2 prompt source for OMC) as Reference-only; this concept page validates that decision via OMC's own use of agency-agents as raw input
- @concepts/skill-vetting.md — OMC's three Talent sourcing types (curated repo / prompt+skill assembly / dynamic skill synthesis) formalise the skill-vetting argument that adoptable agent capabilities need provenance + benchmark validation
- @concepts/librarian-server-architecture.md — sibling 2026-04-28 decision document; if Cemini ever adopts the OMC paradigm, the librarian server is one Storage-interface backend that any Container could read as a knowledge source
- @concepts/context-compression-resume-pattern.md — cpr-pattern (Compress/Preserve/Resume) for individual agent memory; OMC's individual-level self-evolution (post-task review → working principles → workforce state W) is the per-Talent analog; both patterns can co-exist (cpr handles in-session context; OMC handles cross-session principle evolution)
- @entities/frameworks/langgraph.md — LangGraph is one of OMC's three reference Container families (alongside Claude Code session + script-based executor). Significant framing shift: LangGraph as "one Container," not "the orchestrator"
- @entities/frameworks/autoagent.md — autoagent is in OMC's related-work table on the "agent contract" axis. The 6-typed-interface contract is OMC's differentiator vs autoagent / AutoGen / CrewAI / MetaGPT / AgentScope
- @entities/frameworks/fastmcp.md — Cemini's existing FastMCP layer (130+ tools) maps closest to OMC's tool-surface within a Container's Lifecycle/Execution interfaces. If Cemini ever ships an OMC-style abstraction, FastMCP becomes the Cemini-stack-specific Container's tool registry
- @entities/infrastructure/deepseek-api.md — Cemini's current LLM brain; LLM-agnostic in OMC's design (case studies use Claude Sonnet 4.6 + Gemini Pro). DeepSeek would slot into any Container as the underlying model

## Raw Concept

This concept page captures the *AI Organisation Design* paradigm introduced by Yu et al's OneManCompany paper (arXiv 2604.22446v1, 24 Apr 2026). The paradigm posits that multi-agent systems need a third abstraction layer — beyond skills (within-agent) and multi-agent coordination (between-agents) — to govern how a workforce of heterogeneous agents is assembled, managed, and improved over time. The paper claims an 84.67% success rate on PRDBench (+15.48 pp over best baseline), validates 4 cross-domain case studies, and is the first published work to apply structured HR protocols (performance reviews, PIPs, automated offboarding) to AI agent lifecycle management.

The page exists to make these patterns inspectable + actionable for Cemini's downstream architectural decisions, particularly the open ROADMAP question "which conductor / orchestrator do we use?" OMC's reframing of the question — orchestrator as Container family rather than as the architecture — is potentially decision-shifting and warrants an explicit concept page rather than a buried subsection of `scatter-gather-topology.md` or `llm-agent-systems.md`.

## Narrative

### The three abstraction layers (OMC's framing)

| Layer | Question answered | Examples in the wiki |
|---|---|---|
| **Skills** (capability-level) | "What can a single agent do?" | FastMCP @mcp.tool surface, SkillsMP marketplace, Anthropic Skills format |
| **Multi-agent systems** (interaction-level) | "How do agents communicate?" | LangGraph scatter-gather (deterministic), CrewAI roles, AutoGen message graph, Sakana Trinity (3-LLM coord) |
| **AI Organisations** (organisational-level) | "How should a workforce be structured, managed, and improved?" | OMC (Talent+Container+E²R+self-evolution+HR pipeline) |

The argument: existing multi-agent frameworks couple agent identity (who an agent is) to runtime (where it executes). Roles are specified through descriptive prompts rather than executable contracts. Self-improvement is session-bound. The team is fixed before the project starts. **AI Organisations decouple identity from substrate** the way an OS kernel decouples processes from hardware.

### Pattern 1 — Talent + Container = Employee

```
Employee = Talent (cognitive identity) + Container (execution runtime)
                                                      ⬇
                              6 typed organisational interfaces:
                                  • Execution → process management
                                  • Task → scheduling, mutual exclusion
                                  • Event → IPC publish/subscribe
                                  • Storage → file system (short/medium-term memory)
                                  • Context → memory management (prompt assembly)
                                  • Lifecycle → security/audit (pre/post hooks)
```

The same Talent runs on a LangGraph agent OR a Claude CLI session OR a script-based executor, no modification. Adding a new agent runtime requires only a Container implementing the 6 contracts. This is Cemini-relevant because Cemini's current LangGraph-only orchestration could be reframed as "one Container family"; future additions (DeepSeek-direct, Claude Code, ad-hoc Python scripts) become additional Container families under a uniform interface.

**OS kernel analogy is more than rhetorical** (mapped in OMC Appendix B):
- Process Mgmt → Execution + Task interfaces
- Memory Mgmt → Context interface
- File System → Storage interface
- I/O Device Mgmt → Container contract (each Container = one device driver)
- IPC → Event interface
- Security & Audit → Lifecycle interface

### Pattern 2 — Talent Market with three sourcing types

| Type | Source | Example | Cemini-applicability |
|---|---|---|---|
| **Type 1** — Curated repository | Established open-source agent repos (community adoption + benchmark gates) | OMC distills agency-agents and other vetted personas | Cemini could maintain its own internal "Type 1 catalog" for stable agent components |
| **Type 2** — Prompt + skill assembly | Curated persona prompts (e.g., agency-agents 147 personas) + automated skill query → SkillsMP marketplace → composed package | OMC's automated query against SkillsMP using persona descriptors | If Cemini adopts SkillsMP-style cataloging, this is the most generative channel |
| **Type 3** — Dynamic skill synthesis | HR job description → semantic search over skills → mutual-compatibility filter → ranked synthesis | Used for niche/emerging domains; ~20% of CEO shortlist | Cold-start mechanism; less mature than Types 1+2 |

OMC ships an 80/20 (Type1+2 / Type3) shortlist by default. The CEO inspects each candidate's provenance (source repo / source persona + attached skills / constituent skills) before approval. **This validates the WTE Wave 2 evaluation of `agency-agents` as Reference-only** — OMC uses it as raw input, not as deployable artefact.

### Pattern 3 — E²R Tree Search (organisational decision-making)

```
Project directive (CEO)
        ⬇
[Explore: π(T) selects strategy] → decompose + assign + maybe recruit
        ⬇
[Execute: each Employee runs f_e(d_v) → (r_v, c_v)]
        ⬇
[Review: supervisor q_v ∈ {accept, reject}]
        ⬇                              ⬇
   accept → propagate            reject → re-explore (new subtree under same parent)
        ⬇
   bottom-up resolution toward root
```

- Inspired by **MCTS** structurally (tree growth + expansion + evaluation) but DIFFERENT in two ways: real execution (not simulated rollouts), explicit-supervisor evaluation (not UCB-based reward backprop)
- 5 action types: A_decompose, A_assign, A_recruit, A_review, A_iterate
- Search tree T = (V, E_tree, E_dep) — DAG invariant enforced at insertion via DFS cycle detection
- **Bounded rationality circuit breakers**: review-round limit (default 3), task timeout (default 3600s), cost budget cap
- **External oracle pattern** (CEO + customer): policy override, requirement injection, iteration triggering — meta-level controller (Russell & Wefald 1991)

The Cemini-relevant insight: scatter-gather-topology.md describes a deterministic *runtime topology*; E²R describes a *strategy-search* layer ABOVE that topology. They're complementary — E²R could choose a scatter-gather decomposition for one branch and a sequential-pipeline decomposition for another, both backed by the same Container substrate.

### Pattern 4 — DAG + FSM execution semantics

Per-node FSM:

```
                                  Review Pass
pending → processing ────────→ completed ──────→ accepted → finished
              ⬆ retry ↑                ↓
              │       │            Review Fail
              │       ↓                ↓
              │    holding           failed → cancelled (after k_retry)
              ↑       ↓
              └───────┘
```

- **AND-semantics**: a node is resolved iff every child is resolved (or status ∈ {accepted, finished} for leaves)
- **Critical design choice**: `completed → accepted` requires explicit supervisor review — prevents hallucinated/incorrect results from unblocking downstream tasks
- 7 formal invariants:
  1. DAG Invariant: G = (V, E_tree ∪ E_dep) is always acyclic
  2. Mutual Exclusion: |running(e)| ≤ 1 for all employees e
  3. Schedule Idempotency: repeated scheduling is a no-op (crash-safe)
  4. Review Termination: at most k_rev reviews per parent before escalation
  5. Cascade Completeness: cancellation propagates to all transitive dependents
  6. Dependency Completeness: every resolved-state transition triggers forward dependency resolution
  7. Recovery Correctness: after crash, processing nodes reset to pending and reschedule from consistent state

**Cemini relevance**: Cemini's existing LangGraph StateGraph handles state-machine semantics implicitly. If Cemini ever adopts an organisational layer, the FSM + AND-semantics + 7 invariants are the formal contract that LangGraph nodes don't currently provide — particularly the explicit-review gate, which is the strongest hallucination-cascade defence in the design.

### Pattern 5 — Self-evolution at two levels

**Individual-level:**
- Post-CEO-1-on-1 reflection: review feedback, identify expected-vs-actual gaps, update working principles
- Post-task review: review own execution trace, append summary to progress log
- Updates modify the **Talent artefact** (text prompts, principles), NOT the foundation model — continuous improvement without retraining
- Reflected in workforce state W; subsequent calls to π(T) see improved profiles

**Organisation-level:**
- Project retrospectives: COO aggregates per-employee self-assessments + objective signals (retry counts, rejection reasons, cost) → distils into individual feedback + organisational SOPs
- SOPs persisted as workflow documents; auto-injected into relevant agent contexts in subsequent projects

**HR pipeline (the OMC novelty):**
- Every 3 projects: HR auto-initiates periodic review per employee
- 3 consecutive failures → Performance Improvement Plan (PIP) with targeted coaching
- 1 more failure under PIP → automated offboarding (Container deprovisioned, capability gap flagged for re-recruitment)
- The paper claims first application of structured HR protocols to AI agent lifecycle

**Cemini relevance for any future persistent-agent deployment**: if Cemini ever runs agents persistently (vs. ephemeral per-request), the every-3-projects-perf-review cadence is a defensible default. The Container deprovisioning pattern aligns with Hetzner Docker container lifecycle.

### Comparison with sibling agent-orchestration sources

| Source | Scope | What's unique | Where it doesn't go |
|---|---|---|---|
| OMC (this concept page) | Organisation-level (above orchestration) | 6-typed-interface Container contract; Talent Market 3 sourcing types; HR pipeline | Doesn't ship a deterministic runtime topology — relies on the Container family chosen |
| Sakana Trinity (`sakana-trinity-llm-coordinator.md`) | Coordination-level (3-LLM hierarchical) | Coordinator-LLM does meta-decisions over 2 worker LLMs | Limited to 3 agents; no organisation-level abstraction |
| Sakana Conductor (`sakana-conductor-rl-orchestration.md`) | Coordination-level (RL-trained orchestrator) | RL learns orchestration policy | Single-agent RL, no Talent contract, no marketplace |
| autoagent (`entities/frameworks/autoagent.md`) | Agent framework | Score-driven hill climbing + single-file registry-driven harness | No organisation-level abstraction; no multi-runtime |
| LangGraph (`entities/frameworks/langgraph.md`) | Coordination/runtime | Deterministic StateGraph | Single runtime; no Talent contract |
| Scatter-gather (`scatter-gather-topology.md`) | Runtime topology | Sibling-parallel + barrier-join | Specific topology, not organisational |

**OMC's positioning**: above all of these. Any of them could be a Container family.

### Decision points for Cemini

These are decision-pending, not adopted. The paper is fresh (24 Apr 2026, ingested 2026-04-28) and the production code maturity is unverified. The patterns are inspectable but adoption requires verification of the OMC repo and Talent Market.

**Question 1: does Cemini adopt the Talent+Container abstraction?**
- **Pro**: future agent additions (Claude Code session for research, DeepSeek-direct for inference, ad-hoc scripts for backtesting) become uniform Container instances rather than ad-hoc integration points. Library agnostic — outlives any one orchestration framework choice.
- **Con**: discipline cost is high (every Container must implement 6 interfaces). Cemini's current FastMCP @mcp.tool layer is already a partial contract; adding Container would be a re-architecture. The OMC repo is unverified — adopting an unproven framework is risk.
- **Decision gate**: confirm OMC repo exists and is production-grade BEFORE this becomes an adoption candidate. Re-evaluate after spot-checking https://1mancompany.github.io/OneManCompany.

**Question 2: does Cemini adopt the E²R tree-search strategy layer?**
- **Pro**: explicit-supervisor-review gate is a strong hallucination-cascade defence. The 7 formal invariants give Cemini a contract for crash-recovery + cancellation that LangGraph doesn't provide implicitly.
- **Con**: scatter-gather is already deployed. E²R is a higher-level strategy layer ABOVE coordination — Cemini's projects (ticker research, strategy generation) are largely linear and don't yet benefit from dynamic decomposition.
- **Decision gate**: defer until Cemini's research pipelines outgrow scatter-gather. Track in ROADMAP open question "which conductor."

**Question 3: does Cemini adopt the HR + PIP + offboarding pipeline?**
- **Pro**: novel, well-specified, applies cleanly if Cemini ever runs persistent agents. Aligns with Hetzner Docker container lifecycle.
- **Con**: Cemini today runs request-scoped agents (start with task, finish, exit). HR pipeline applies only to persistent-agent deployments. Premature optimisation.
- **Decision gate**: revisit if Cemini ships a persistent-agent product (e.g., a long-running research-Talent that persists across user sessions).

### Patterns to consider stealing (not full adoption)

Even without adopting OMC wholesale, individual patterns are extractable:

1. **The 6-typed-interface contract** — even if Cemini doesn't ship a Container, the 6 categories (Execution / Task / Event / Storage / Context / Lifecycle) are a useful taxonomy for code-organising existing agent integrations.
2. **AND-semantics with explicit-review gate** — could be added to the existing LangGraph StateGraph by inserting a supervisor-review node between completion and downstream-dispatch. Cheap; high hallucination-defence value.
3. **Working-principles-as-text-artefact pattern** — Cemini could add per-agent `principles.md` files that get auto-updated via post-task self-reflection prompts. No model retraining needed.
4. **The `agency-agents` × SkillsMP composition pattern** — if Cemini ever needs a new specialist agent, the OMC Type-2 sourcing approach (start from a curated persona prompt, add skills from a marketplace, compose) is a cleaner generation path than ad-hoc prompt-writing.

## Snippets

> "Skills operate strictly within a single agent. They enhance what an agent can do, but they do not address how multiple agents should work together. As tasks grow in complexity, requiring diverse expertise, long-horizon coordination, and iterative refinement, a single agent, no matter how well equipped with skills, becomes insufficient." [Source: From Skills to Talent, p.2 §1]

> "We argue that the next stage of progress requires a shift in perspective: from agents and their skills to the organisation that governs them." [Source: From Skills to Talent, p.2 §1]

> "Identity–substrate separation: the same Talent can run on a LangGraph agent, a Claude CLI session, or a script-based executor without modification, and conversely the same Container type can host different Talents to produce employees with different roles on the same backend." [Source: From Skills to Talent, p.5–6 §2.1.1]

> "Talents elevate the unit of reuse from individual tools to complete agent identities with managed lifecycles." [Source: From Skills to Talent, Table 1 caption, p.4]

> "Two design choices are critical (Figure 5). First, COMPLETED→ACCEPTED requires explicit supervisor review, which prevents hallucinated or incorrect results from unblocking dependent tasks. Second, the FAILED→PROCESSING retry path is bounded by a maximum retry count k_retry; exceeding this limit triggers escalation, guaranteeing that no node cycles indefinitely." [Source: From Skills to Talent, p.11 §2.2.4]

> "We are not aware of prior work that applies structured HR protocols (performance reviews, PIP, formal offboarding) to AI agent lifecycle management." [Source: From Skills to Talent, p.13 §2.3.2]
