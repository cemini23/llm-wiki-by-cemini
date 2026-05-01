---
title: OneManCompany — From Skills to Talent (Yu et al, Huawei Noah's Ark + UCL + U Liverpool, 2026)
type: source
tags: [llm-agents, ai-organisation-design, multi-agent, agent-orchestration, talent-container, e2r-tree-search, dag-execution, fsm, self-evolution, prdbench, huawei]
keywords: [omc, one-man-company, talent, container, employee, ceo, hr, coo, ea, e2r, mcts, dag, fsm, talent-market, skillsmp, agency-agents, prdbench, dynamic-agentic-workflow, self-evolution, sop, pip, organisational-interfaces]
related:
  - sources/gemini-dr-link-eval-2026-04-28.md
  - concepts/ai-organisation-design.md
  - concepts/llm-agent-systems.md
  - concepts/scatter-gather-topology.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/skill-vetting.md
  - sources/sakana-trinity-llm-coordinator.md
  - sources/sakana-conductor-rl-orchestration.md
  - entities/frameworks/langgraph.md
  - entities/frameworks/autoagent.md
  - entities/infrastructure/deepseek-api.md
maturity: validated
read_status: deep-read
created: 2026-04-28
updated: 2026-04-28
clusters: [llm-agents, agent-orchestration]
---

## Relations

- @sources/gemini-dr-link-eval-2026-04-28.md — sibling source, ingested in the same 2026-04-28 indexing pass; OMC was dropped alongside the Gemini DR report but is an independent arXiv paper, not a Gemini DR finding
- @concepts/ai-organisation-design.md — concept page synthesizing OMC's organisational paradigm (Talent+Container+E²R+self-evolution+HR pipeline) into reusable patterns; this paper is the canonical source for that concept page
- @concepts/llm-agent-systems.md — OMC slots into the corpus index as a top-tier 2026 organisation-level paper; complements the existing scatter-gather + Trinity + autoagent / AutoGen / CrewAI / MetaGPT entries
- @concepts/scatter-gather-topology.md — scatter-gather is one specific *coordination topology* (LangGraph, deterministic, sibling-parallel); OMC's E²R tree search is a *strategy-search* layer ABOVE coordination (decompose dynamically + AND-tree completion + bottom-up review). Complementary, not competing
- @concepts/wiki-tooling-evaluation.md — OMC's Type-2 Talent sourcing (prompt persona + skill assembly via SkillsMP) and Type-3 (dynamic skill assembly) directly cite `agency-agents` (covered in WTE Wave 2 Reference-only tier) and `SkillsMP` skill marketplace; OMC is the canonical source connecting those references
- @concepts/skill-vetting.md — OMC formalises a community-validated skill marketplace (3 sourcing types: curated repo, prompt+skill, dynamic). Reinforces the skill-vetting concept's argument that adoptable agent capabilities need provenance + benchmark validation
- @sources/sakana-trinity-llm-coordinator.md — sibling 2026 paper on LLM-driven agent coordination; Sakana's Trinity coordinates 3 LLMs in a hierarchical pattern with a coordinator. OMC scales to N agents with formal organisational lifecycle. Different scope; cite both in concept pages
- @sources/sakana-conductor-rl-orchestration.md — sibling 2026 paper using RL for orchestration. OMC explicitly notes "RL-based orchestration" as a cited related-work direction (refs [48, 49]) but takes the human-in-the-loop external-oracle path instead. Position-contrast worth recording
- @entities/frameworks/langgraph.md — OMC's Container abstraction names LangGraph as one of three reference Container backends (alongside Claude Code session and script-based executor). LangGraph's role in OMC is "one Container family" rather than "the orchestrator" — significant framing shift
- @entities/frameworks/autoagent.md — OMC's related-work table puts OMC in opposition to AutoGen/CrewAI/MetaGPT/AgentScope on the "agent contract" axis: OMC has 6 typed organisational interfaces; existing systems have implicit prompts/SOPs/callbacks. Architectural differentiator worth quoting
- @entities/infrastructure/deepseek-api.md — OMC's PRDBench evaluation cites Claude Code Sonnet 4.6 + Gemini 3.1 Flash Lite Preview as the LLM brains; DeepSeek is mentioned only as a comparison baseline (62% on minimal mode). For Cemini's downstream adoption, the OMC pattern is LLM-agnostic — could be wired to DeepSeek via the Container abstraction

## Raw Concept

- **Original title**: "From Skills to Talent: Organising Heterogeneous Agents as a Real-World Company"
- **Authors**: Zhengxu Yu*, Yu Fu* (co-first authors), Zhiyuan He, Yuxuan Huang, Lee Ka Yiu, Meng Fang, Weilin Luo, Jun Wang
- **Affiliations**: HUAWEI Noah's Ark Lab; University College London; University Liverpool
- **Type**: arXiv preprint (cs.AI)
- **arXiv ID**: 2604.22446v1
- **Submitted**: 24 April 2026
- **Project homepage**: https://one-man-company.com
- **Repository**: https://1mancompany.github.io/OneManCompany
- **Talent Market**: https://one-man-company.com/market
- **Location**: `research to be indexed/From Skills to Talent- Organising Heterogeneous Agents as a Real-World Company.pdf` (8.7 MB, 33 pages including 6-page appendix) → moved to `research for cemini/`
- **Retrieved**: 2026-04-28
- **Pages / length**: 33 pages (24 main + 9 appendix); references [1]–[57]
- **Read status**: deep-read (full 33-page ingest 2026-04-28)

The paper introduces a third abstraction layer above existing multi-agent systems: where **skills** are capability-level (within one agent) and **multi-agent systems** are interaction-level (how agents communicate), **AI organisations** are organisation-level (how a workforce is structured, managed, and improved). The paper is dropped alongside the Gemini DR report 2026-04-28 but is an independent ingest — the user explicitly framed it as "a new paper" separate from the report.

## Narrative

### Why this matters for Cemini and the wiki

OMC is a 2026 paper that tackles a specific architectural problem the Cemini stack will eventually face: **how to organise heterogeneous AI agents that span Claude Code (anthropic-specific), LangGraph reactive agents (Python-specific), and script-based executors (anything) under a uniform contract**. The wiki has been collecting agent-orchestration sources (Sakana Trinity, Sakana Conductor, autoagent, AutoGen, CrewAI, MetaGPT) but none of those provide a *substitutable contract* between agent identity (prompts, skills, tools) and execution runtime. OMC formalises this separation as Talent + Container = Employee.

For the workspace librarian, OMC's Talent Market design is also significant: it formalises three sourcing channels (curated repo / prompt + skill assembly / dynamic skill synthesis) for adopting community-validated agent packages. Two of those channels directly cite repos that surfaced in WTE Wave 2 (`agency-agents`, `SkillsMP`) — OMC retroactively validates the wiki's earlier evaluation of those as Reference-only and Skill-vetting candidates.

### The three pillars

**Pillar 1: Talent–Container Architecture (Section 2.1)**

- **Talent** = portable cognitive identity (prompts, role, skills, tools, working principles); deployable across runtimes
- **Container** = execution runtime (LangGraph, Claude CLI, script-based) wrapping the Talent and exposing 6 typed organisational interfaces
- **Employee** = Talent + Container; managed lifecycle from hire → evaluate → offboard
- **6 typed organisational interfaces** map to OS kernel subsystems (canonical Tanenbaum/Silberschatz):
  - `Execution` → Process management (dispatch task, return result)
  - `Task` → Process scheduling (per-employee queue, mutual exclusion `|running(e)| ≤ 1`)
  - `Event` → IPC (publish/subscribe organisational event bus)
  - `Storage` → File system (persistent memory short/medium-term)
  - `Context` → Memory management (assemble execution prompt from role + guidance + memory)
  - `Lifecycle` → Security & audit (pre/post hooks for validation, guardrails, self-improvement)
- **Talent Market** sourcing types (Section 2.1.2 + Appendix D):
  - **Type 1 — curated repository agents**: distilled from established open-source repos with community-adoption and benchmark performance gates
  - **Type 2 — prompt-sourced + skill assembly**: starts from `agency-agents` (147 personas) → SkillsMP marketplace skill query → composed Talent package
  - **Type 3 — dynamic skill assembly**: HR provides job description → semantic search over SkillsMP → mutual-compatibility filter → ranked synthesis
  - 80/20 ratio in CEO recommendation shortlist (80% Type 1+2, 20% Type 3) — reflects channel maturity, not intrinsic quality
- **Founding Team**: HR, EA, COO, CSO bootstrap each OMC instance

**Pillar 2: E²R Tree Search (Section 2.2)**

- Decomposes organisational decision into three stages: **Explore** (select decomposition + assignment) → **Execute** (agents do the work) → **Review** (quality signals propagate bottom-up)
- Inspired by Monte Carlo Tree Search (MCTS) but with key differences: real execution (not simulated rollouts), explicit-supervisor evaluation (not UCB-based reward backprop)
- Search tree T = (V, E_tree, E_dep) with two edge types:
  - **Decomposition edges** (E_tree): "parent p was decomposed into child v'"
  - **Dependency edges** (E_dep): "v cannot begin until u is accepted"
- **5 action types**: A_decompose, A_assign, A_recruit, A_review, A_iterate
- **Bounded rationality circuit breakers**: review-round limit (k_rev=3 default), task timeout (T_max=3600s default), cost budget (sum c_v > B → pause)
- **External oracle** (CEO + external customer): policy override, requirement injection, iteration triggering — frames the human-in-the-loop as a meta-level controller applying domain-informed optimal stopping (Russell & Wefald 1991)

**Pillar 3: DAG-based Task Decomposition + FSM (Section 2.2.4)**

- AND-tree augmented with dependency edges: a node is **resolved** iff (leaf with status ∈ {accepted, finished}) OR (∀ children resolved)
- Per-node FSM: `pending → processing → completed → accepted → finished` (happy path); `processing → holding`, `processing → failed → processing` retry, `failed → cancelled` escalation
- **Critical design choice**: `completed → accepted` requires explicit supervisor review — prevents hallucinated/incorrect results from unblocking dependent tasks
- 7 formal invariants: DAG, mutual exclusion, schedule idempotency, review termination (≤k_rev), cascade completeness, dependency completeness, recovery correctness (crash → re-pending → reschedule)

**Pillar 4: Self-evolution (Section 2.3) — agents and organisations both learn over time**

- **Individual-level**: post-CEO-1-on-1 reflection + post-task review → working principles updated → reflected in workforce state W → subsequent calls to π(T) see improved profiles
  - Crucially: updates the *Talent artefacts* (text prompts, principles), NOT the foundation model weights — continuous improvement without retraining
- **Organisation-level**: project retrospectives → SOP updates → injected into future agent contexts
- **HR pipeline**: every-3-projects periodic review → 3 consecutive failures → PIP (Performance Improvement Plan) → 1 more failure → automated offboarding (Container deprovisioned, capability gap flagged for re-recruitment)
- The paper claims this is the first work to apply structured HR protocols (perf review, PIP, offboarding) to AI agent lifecycle management

### Empirical results

- **PRDBench** (Fu et al 2025, 50 project-level software dev tasks across 20+ domains): OMC achieves 84.67% success rate, +15.48 percentage points over best baseline
  - vs Minimal Claude-4.5: 69.19%
  - vs Minimal GPT-5.2: 62.49%
  - vs Commercial Claude Code: 56.65%
  - vs Commercial CodeX: 62.09%
  - vs Minimal DeepSeek-V3.2: 40.11%
  - Total cost across 50 tasks: $345.59 (~$6.91/task) — multi-agent overhead acknowledged
- **Claude Code Sonnet 4.6 + Gemini 3.1 Flash Lite Preview** is the production-LLM combination tested; founding agent uses Gemini 2.1 Flash Lite Preview
- 4 cross-domain case studies validate generality (not just coding):
  - **Content generation**: GPT-4o (Researcher) + Claude Sonnet 4 (Writer) → GitHub trend report emailed; ~$4.49 total
  - **Game development**: Claude Sonnet 4 (Game Dev) + Gemini 2.5 + NanoBanana (Art Designer); demonstrates *human-in-the-loop iteration via re-decomposition* with new skill creation when sprite-sheet segmentation failed
  - **Audiobook**: Claude Sonnet 4 (Novel Writer) + Gemini 3.1 Pro (AV Producer) → 16 illustrated scenes + voice-over + final video; $1.57
  - **Research survey**: Claude Sonnet 4.6 (Research Scientist) + self-hosted AI Engineer → 17 documents + ~70-node mind map + 3 novel research ideas (HiTeWM, PhysWM, MAWM) on world models for embodied AI; $16.26 total

### Architectural axis-comparisons (Table 4 in paper)

OMC vs existing systems on 7 axes:

| System | Design paradigm | Exec model | Agent contract | State mgmt | Multi-runtime | Agent source | Self-evol | Org evol |
|---|---|---|---|---|---|---|---|---|
| **OMC** | Organisation | On-demand | 6 typed interfaces | Disk | ✓ | Talent Market | ✓ | ✓ |
| MetaGPT/ChatDev | SOP pipeline | Sequential | Implicit (SOP) | In-memory | ✗ | Prompt-defined | ✗ | ✗ |
| AutoGen/LangGraph | Message graph | Event/Graph | Callbacks | Checkpoints | ✗ | Developer-defined | ✗ | ✗ |
| CrewAI/Agno | Role framework | Seq/parallel | Class inherit | App-defined | ✗ | Developer-defined | ✗ | ✗ |
| OpenHands | Sandbox | Agent loop | Built-in runtime | Sandboxed | ✗ | Built-in | ✗ | ✗ |
| AIOS | OS kernel | Scheduled | OS syscalls | OS-managed | ✗ | Registry | ✗ | ✗ |
| AgentScope | Distributed actors | Distributed | Partial | App-defined | ✗ | Developer-defined | ✗ | ✗ |
| Paperclip | Orchestrator | Ticket-based | Strategic director | App-defined | ✓ | Prompt-defined | ✗ | ✗ |

OMC is the **only** system in this comparison with both individual self-evolution AND organisation-level evolution. The 6-typed-interface contract and Talent Market are also unique (Paperclip has multi-runtime but no Talent Market; AIOS has OS-kernel framing but a registry rather than a marketplace).

### Limitations the paper acknowledges

1. Quantitative evaluation is PRDBench-only (50 software dev tasks). Case studies show cross-domain generality but no systematic non-coding benchmarks.
2. Self-evolution mechanisms (1-on-1, retrospectives, perf review) are deployed but not yet quantitatively ablated — isolating each mechanism's contribution requires longitudinal studies across many projects.
3. Cost overhead ~$6.91/task is justified for project-level tasks but inappropriate for simple single-turn queries. Adaptive dispatch mode added: CEO can route simple tasks to a single agent.

### Implications for Cemini

1. **The orchestrator question is ALMOST resolvable as "all of the above"** — Cemini currently leans LangGraph (per scatter-gather-topology). OMC reframes LangGraph as *one Container family* (alongside Claude Code session + script). If Cemini adopts the Talent+Container paradigm, the orchestrator question becomes: which Containers do we host? rather than: which orchestrator do we pick? This changes the open ROADMAP question from "which conductor" to "do we adopt OMC's organisational layer."
2. **PRDBench-style evaluation pattern is reusable** — the 50-task project-level benchmark with PRDs + automated evaluation scripts is a template for evaluating the Cemini brain's autonomous research-and-strategy generation pipelines. Worth ingesting separately if the Fu et al 2025 PRDBench paper (ref [12]: arXiv 2510.24358) is dropped.
3. **The HR + PIP + offboarding pipeline is novel and underexplored elsewhere** — for any future Cemini multi-agent deployment with persistent agents (vs ephemeral per-request), structured performance management is the right framing. Worth borrowing the per-3-projects-review cadence.
4. **The 6-typed-interface contract is strict** — the Container/Talent boundary is enforceable at code-review time the way scatter-gather's StateGraph node boundary is. If Cemini ships an OMC-style abstraction, every new agent backend (LocalAI, DeepSeek, future Ollama-based) must implement the 6 interfaces. This is more discipline than the existing FastMCP @mcp.tool surface.
5. **The Talent Market sourcing types validate WTE Wave 2's `agency-agents` Reference-only tier** — OMC explicitly cites `agency-agents` (ref [57]) as the canonical Type-2 prompt source. The wiki's evaluation of `agency-agents` as Reference-only (not Adopt) was correct: OMC uses it as a *raw input* to a more elaborate skill-assembly pipeline, not as a deployable artefact. This is exactly the "study, don't install" recommendation the wiki had on the page.

### What this DOES NOT do for Cemini

- **Doesn't solve the local-LLM brain question** — OMC is LLM-agnostic; the case studies use API-hosted Claude Sonnet 4.6 + Gemini Pro. The "which local LLM" ROADMAP question is orthogonal.
- **Doesn't solve the librarian server question** — WTE Wave 1 already decided llm-wiki-compiler. OMC could *use* the librarian as a knowledge source for its Research Scientist Talents (case study 4 generated 17 docs into the workspace) but doesn't replace it.
- **Doesn't ship code** — homepage exists, repo is at https://1mancompany.github.io/OneManCompany. As of paper submission (24 Apr 2026), the production code maturity is unverified. Spot-check if Cemini ever moves to adopt: confirm code is real, license is acceptable, runtime dependencies are tractable.

## Snippets

> "We argue that this reflects a deeper absence: a principled organisational layer that governs how a workforce of agents is assembled, governed, and improved over time, decoupled from what individual agents know. To fill this gap, we introduce OneManCompany (OMC), a framework that elevates multi-agent systems to the organisational level." [Source: From Skills to Talent, p.1 abstract]

> "Skills are capability-level abstractions, reusable within an agent but agnostic to coordination. Multi-agent systems are interaction-level abstractions, specifying how agents communicate but not how they are organised, managed, or improved. In contrast, an AI organisation is an organisation-level abstraction: it governs how agents are assembled into teams, how work is decomposed and executed, and how the system evolves over time. In other words, skills answer 'what can an agent do?', multi-agent systems answer 'how do agents interact?', while AI organisations answer 'how should a workforce of agents be structured and managed to achieve complex goals?'" [Source: p.2 §1]

> "Definition 1 (AI Organisation). a self-governing system of heterogeneous agents with structured coordination, managed lifecycles, and experience-driven evolution." [Source: p.2 §1]

> "We observe that the six interfaces mirror the canonical subsystems of an OS kernel (process management, memory, file system, I/O, IPC, security)" [Source: p.6 §2.1.1]

> "An employee who fails three consecutive reviews enters a formal Performance Improvement Plan (PIP), receiving targeted coaching, adjusted task assignments, and closer supervision. If the employee fails one additional review under PIP, the system triggers automated offboarding: the agent's Container is deprovisioned, its desk is freed, and the capability gap is flagged for re-recruitment from the Talent Market. … We are not aware of prior work that applies structured HR protocols (performance reviews, PIP, formal offboarding) to AI agent lifecycle management." [Source: p.13 §2.3.2]

> "OMC achieves the highest success rate of 84.67% (+15.48%) across all systems, surpassing all baselines. The total cost of $345.59 across 50 tasks (approximately $6.91 per task) reflects the overhead of multi-agent coordination" [Source: p.13 §3.2]

> "Two design choices are critical (Figure 5). First, COMPLETED→ACCEPTED requires explicit supervisor review, which prevents hallucinated or incorrect results from unblocking dependent tasks. Second, the FAILED→PROCESSING retry path is bounded by a maximum retry count k_retry; exceeding this limit triggers escalation, guaranteeing that no node cycles indefinitely." [Source: p.11 §2.2.4]

> "Talents elevate the unit of reuse from individual tools to complete agent identities with managed lifecycles. … Skills improve what a single agent can do. Talents organise multiple agents into a workforce that can be built, managed, and improved over time." [Source: Table 1, p.4]

> "We follow the official DEV mode setting, in which each system receives the PRD as a one-shot input and must complete the task without iterative feedback or external intervention, with final outputs directly evaluated by automated scripts." [Source: p.13 §3.1]
