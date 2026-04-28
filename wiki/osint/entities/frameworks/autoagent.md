---
title: AutoAgent (kevinrgu/autoagent) — autonomous harness engineering framework
type: entity
tags: [framework, agent-harness, score-driven-optimization, mit-licensed, k8-promotion]
keywords: [autoagent, harbor, score-driven-hill-climbing, single-file-registry, harness-optimization, third-layer-team]
related:
  - sources/4-5-links.md
  - entities/frameworks/langgraph.md
  - entities/frameworks/fastmcp.md
  - concepts/scatter-gather-topology.md
  - concepts/llm-agent-systems.md
  - concepts/ip-sale-readiness.md
  - concepts/ai-organisation-design.md
  - sources/omc-talent-container-paper.md
maturity: draft
created: 2026-04-28
updated: 2026-04-28
---

## Relations

- @sources/4-5-links.md — K8-canonical source. Para 2–13 evaluation block; "kevinrgu/autoagent" is the **first H2 section** of the doc and gets the deepest substantive Cemini-mapping treatment (Single-File Registry-Driven Harness pattern + Score-Driven Hill Climbing pattern). Highest substantive Cemini-relevance among the 13 repos evaluated; promoted to its own entity page on the K8 deep-read pass.
- @entities/frameworks/langgraph.md — the operative orchestration framework AutoAgent's "Score-Driven Hill Climbing" pattern would integrate against; the doc maps the meta-evaluator's commit/revert decisions onto LangGraph node-execution cycles
- @entities/frameworks/fastmcp.md — the tool layer AutoAgent's "Single-File Registry-Driven Harness" pattern would consolidate; the doc's prescription is to consolidate the (server-confirmed) **130 registered `@mcp.tool` decorators** into a hot-reloadable single-file registry behind a fixed adapter boundary
- @concepts/scatter-gather-topology.md — sibling LangGraph-orchestration concept; AutoAgent's harness-optimization loop is conceptually adjacent to the prescribed scatter-gather Send-API fan-out (different axis of the same orchestration problem: scatter-gather optimizes *runtime topology*; AutoAgent optimizes *harness configuration*)
- @concepts/llm-agent-systems.md — cluster hub for LLM agent-systems research; AutoAgent fits the "agent scaffolding + harness engineering" sub-cluster
- @concepts/ip-sale-readiness.md — the K8 source's "IP sale relevance" subsection on AutoAgent reads: implementing automated, score-driven harness optimization "significantly strengthens the IP sale narrative" by demonstrating self-healing architecture capable of autonomous, weekend-based parameter optimization without manual developer intervention

## Raw Concept

GitHub repository `kevinrgu/autoagent` (Kevin Gu, Third Layer Team), MIT-licensed. Surfaced via K8 deep-read of `sources/4-5-links.md` 2026-04-28 as one of three promoted entities (alongside `concepts/context-compression-resume-pattern.md` and `entities/infrastructure/localai.md`). Page is `draft` maturity at first creation — promoted on the strength of the K8 source's analytical pass, not yet validated against an upstream first-hand read of the repository.

## Narrative

### What AutoAgent is

Per the K8 source (paragraph 2):

> The repository implements an autonomous harness engineering framework designed to iteratively improve an artificial intelligence agent's execution environment without human intervention. Functioning as an automated research loop, the deployed system assigns a meta-agent to modify a target agent's system prompts, tool configurations, and orchestration logic overnight. The system then executes benchmark tasks against Harbor-compatible evaluation containers, calculates a deterministic score, and either commits or reverts the architectural changes based on performance improvements.

It's not a model — it's a **harness optimizer**. The target system being optimized is a separate agent; AutoAgent's job is to mutate that agent's prompts/tools/routing configurations, score the result against benchmark tasks running in Harbor-compatible Docker containers, and accept-or-revert based on the score delta. Hill-climbing search over agent harness configuration space.

### Two named patterns worth stealing (K8 source)

**1. Single-File Registry-Driven Harness pattern**

The full agent execution environment — configurations, tool definitions, routing logic — lives in one `agent.py` file, separated from infrastructure via a fixed adapter boundary. Hot-reloadable. The K8 source maps this directly onto Cemini's FastMCP intelligence server: consolidate the (server-confirmed) **130 registered `@mcp.tool` decorators** into a single, structured, hot-reloadable registry file so the LangGraph orchestrator can swap tool definitions without rebuilding Docker containers.

The 22-tool figure the K8 source assumed (off by ~6×) doesn't change the pattern's value — at 130-tool scale the consolidation is *more* useful, not less. K8 calibration finding.

**2. Score-Driven Hill Climbing pattern**

The meta-agent's accept/revert decision is governed by a deterministic score on benchmark tasks. The K8 source maps this onto the Devil's Advocate debate protocol's offline-window meta-evaluation — during the prescribed (but per K8 server-probe, **not-shipped**) April 14–17 RL retrain window, a meta-evaluator could continuously modify the deterministic scoring rubric and execute backtests against the existing ~5K BTC-USD and ~2.3K SPY accumulated rows, retaining only modifications that improve Sharpe ratio or decrease maximum drawdown.

K8 server-probe finding: the April 14–17 window did not happen as the doc prescribed (git log for that window shows logic-audit + CI cleanup + dead-code deletion + kill-switch placement, zero MAPPO retrain commits). So the AutoAgent integration story is a **forward-looking IP-sale-prep entry** — what the doc *hoped* would land in that window — not an as-built description.

### One named pattern flagged as questionable (K8 source)

**3. Model Empathy Optimization** (paragraph 4): an empirical observation that a meta-agent uses diagnostic failure modes more accurately when optimizing a task agent running on the identical underlying model architecture. The K8 source flags this as theoretically interesting but practically blocked by the CPU-only Hetzner hardware constraint. Real applicability would require quantized local inference (which gates on the retracted DeepSeek-R1-14B local-runtime path) or a future hardware swap.

### What the K8 source flags AutoAgent got wrong

- Steering meta-agent optimization via natural-language `program.md` markdown files. The K8 source flags this as a critical engineering failure for a financial-platform solo-dev: markdown parsing introduces probabilistic execution risks, breaks deterministic typing, and creates untraceable silent failures. **Cemini's translation discipline**: AutoAgent's pattern adopts must convert `program.md`-style steering into strict Pydantic v2 schemas at the FastMCP boundary
- Implicit assumption of cloud-LLM availability (e.g., GPT-4) in the critical execution loop for meta-evaluation — incompatible with the CPU-only hardware constraint and the live-trading low-latency requirement; meta-evaluation is restricted to offline windows

### Cemini integration roadmap (K8 source's verbatim Top-3 Steal-Immediately)

> 1. Isolate the FastMCP tool registry into a single, hot-reloadable file pattern behind a fixed adapter boundary.
> 2. Implement strict Docker container sandboxing for all automated historical backtesting tasks.
> 3. Adopt deterministic score-driven hill climbing for the MAPPO feature vector tuning during offline windows.

K8 server-probe context: the **130 FastMCP tools** are NOT yet consolidated into a single registry file (the doc's prescription is good); the existing 40-container Docker Compose stack already handles container-sandboxing trivially (low-effort lift); the MAPPO retrain window has slipped, so #3 is **deferred-not-cancelled**.

### Status

- **License**: MIT 🟢 — clean, no IP-sale-prep poison flags (contrast with peers in the K8 doc: SocratiCode AGPL-3.0, GitNexus PolyForm Noncommercial, peth AGPL v3)
- **Deployed integration**: none. AutoAgent is **not currently in `/opt/cemini/requirements.txt`**, no AutoAgent containers in the 40-container Docker Compose stack. This is forward-looking architectural prep, not deployed code.
- **Integration effort estimate (K8 source)**: ~4 hours for the Single-File Registry refactor (pattern #1); 1–2-day sprint for the Score-Driven Hill Climbing wiring against PostgreSQL backtest schema (pattern #3). The doc rates pattern #2 (Docker sandboxing) as 🟢 LOW because the docker-compose.yml infrastructure is already established.
- **NEEDS VERIFICATION 2026-04-28**: upstream repo state (commit hash, last-update date, MIT-license verbatim, README structure) — page is built from the K8 doc's secondhand evaluation; first-hand crawl-via-Exa pass is queued for a future deep-read

## Snippets

### Solo-dev filter table (K8 source)

| Finding | Implementation Effort | Justification |
|---|---|---|
| Single-File FastMCP Registry | 🟢 LOW | Consolidating the 22 tools requires under 4 hours of refactoring and eliminates cross-module import complexities. *(K8 calibration: actual is 130 tools, so the lift is larger but the value is amplified)* |
| Docker-Sandboxed Task Evaluation | 🟢 LOW | The docker-compose.yml infrastructure is already established; spinning up isolated containers for backtests requires minimal configuration. |
| Score-Driven Hill Climbing Loop | 🟡 MEDIUM | Requires wiring the LangGraph orchestrator to a dedicated PostgreSQL backtest schema and defining the validation loop parameters over a 1–2 day sprint. |

### Conflicts with the deployed stack (K8 source verbatim)

> The repository implicitly assumes the availability of heavy, cloud-based LLM inference (e.g., GPT-4) within the critical execution loop to perform the meta-evaluation and harness adjustments. Executing continuous LLM-based architectural modifications directly contradicts the low-latency requirements of the Kalshi and Alpaca multi-broker EMS and is computationally incompatible with the CPU-only hardware constraints if attempted during live market hours.

### Top-3 To Explicitly Avoid (K8 source verbatim)

> 1. Do not steer agent behavior or system architectures via unstructured markdown files.
> 2. Do not execute LLM-based meta-evaluation in the critical path of live order routing.
> 3. Do not allow automated agents the permissions to modify their own host environment dependencies (pyproject.toml).
