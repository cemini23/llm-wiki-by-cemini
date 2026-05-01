---
title: MCP Tool Marketplace — Cemini's MCP-Server Adoption Pattern
type: concept
tags: [concept, mcp, model-context-protocol, llm-tooling, marketplace-dynamics, adoption-rubric, applied-during-evaluation, cemini-stack-design]
keywords: [mcp, model-context-protocol, mcp-server, mcp-marketplace, cemini-mcp-inventory, fork-and-pin-pattern, single-day-dev-bus-factor, vendor-backend-dependency, mit-license-dominance, family-c-tos-conflict, claude-code-skill-vs-mcp-server, fastmcp, dune-analytics-mcp, polymarket-predictions-mcp, tradingview-mcp, context7, vibe-trading, sentrux, playwright-mcp, atomicmemory-llm-wiki-compiler, willynikes2-knowledge-base-server, mcp-server-ccxt, mcp-etherscan-server]
related:
  - concepts/high-signal-paper-patterns.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/ip-sale-readiness.md
  - concepts/llm-agent-systems.md
  - concepts/librarian-server-architecture.md
  - sources/vibe-trading-hkuds.md
  - sources/sentrux-ast-sensor.md
  - sources/playwright-mcp-microsoft.md
  - sources/atomicmemory-llm-wiki-compiler.md
  - sources/willynikes2-knowledge-base-server.md
  - sources/dune-analytics-mcp.md
  - sources/polymarket-predictions-mcp.md
  - sources/tradesdontlie-tradingview-mcp.md
  - sources/upstash-context7.md
  - sources/mercurialsolo-claudectl.md
  - sources/7onez-cti-expert.md
  - sources/last30days-skill-mvanhorn.md
  - sources/agentmemory-rohitg00-cpr-impl.md
  - entities/frameworks/fastmcp.md
  - sources/wave-5-1-link-eval-stacks.md
  - sources/gemini-dr-wave5b-osint-2026-04-30.md
  - sources/caiovicentino-polymarket-mcp-server.md
  - sources/agriciDaniel-claude-obsidian.md
  - sources/alash3al-stash.md
  - sources/3-28-links-2.md
  - sources/wave-5-1-link-eval-even-more.md
created: 2026-04-30
updated: 2026-04-30
maturity: validated
---

## Relations

- @concepts/high-signal-paper-patterns.md — sibling rubric; that one is for *papers* (research findings); this one is for *MCP servers / Claude Code skills* (operational tools). Both are ingest decision rubrics.
- @concepts/wiki-tooling-evaluation.md — the wiki-side adoption parent; many MCP-server Adopts also touch the librarian's serving layer (atomicmemory llm-wiki-compiler, willynikes2 kb-server)
- @concepts/ip-sale-readiness.md — license-poison-pill ledger directly applies; this concept page surfaces Family C (TOS-conflict) as a recurring MCP-server-specific risk
- @concepts/llm-agent-systems.md — cluster hub; MCP servers are the *tool surface* of LLM agent systems
- @concepts/librarian-server-architecture.md — the librarian's deployed MCP layer (kb-server) is one of the MCP servers in Cemini's inventory
- @entities/frameworks/fastmcp.md — Cemini's Python MCP framework; the integration substrate for any Adopt-Cemini-stack MCP server. All Cemini-stack MCP integrations attach to FastMCP via `@mcp.tool` decorators.
- @sources/wave-5-1-link-eval-even-more.md — Wave 5.1 infra evaluation; 4-stage extraction pipeline (crawl4ai → trafilatura → unstructured → files-to-prompt) surfaces MCP-as-data-ingestion-surface pattern
- (and 13 individual MCP-server source pages — see frontmatter)

## Raw Concept

**What prompted this page**: by 2026-04-30 the wiki has accumulated ~13 MCP-server source pages and ~5 Claude-Code-skill source pages across Waves 2, 3, and 4. The MCP-as-tool-surface pattern is the dominant LLM-agent integration substrate for Cemini's stack. The accumulation of source pages without cross-cutting synthesis was creating evaluation friction: every new MCP-server Adopt triggered a fresh "wait, is this like vibe-trading or like dune-analytics-mcp?" comparison loop. This page makes the cross-cutting patterns explicit so future MCP-server evaluations can reference a stable rubric.

The page is **applied during evaluation**: when a new MCP server appears (in a Tier-2 sweep, a Gemini DR brief, or a user drop), the LLM consults this rubric explicitly during scoring before recommending Adopt / Defer / Steal-from / Reject.

## Narrative

### Cemini's MCP-server inventory (by purpose)

| Category | Source page | Status | Notes |
|---|---|---|---|
| **Librarian/wiki tooling** | `@sources/atomicmemory-llm-wiki-compiler.md` | Reference (ramped down in favor of kb-server) | Wave 1 Adopt; later replaced by kb-server for the librarian |
|  | `@sources/willynikes2-knowledge-base-server.md` | **Deployed** as `kb-server` on cemini-librarian | Active production |
| **Code-quality / harness** | `@sources/sentrux-ast-sensor.md` | Adopt-Workflow | Tree-sitter AST quality governor; MCP mode for live feedback |
|  | `@sources/agent-browser-vercel-labs.md` | K9 promotion (Wave-3 era) | Browser automation MCP |
| **Browser automation** | `@sources/playwright-mcp-microsoft.md` | Defer-Cemini / Adopt-Workflow | Apache-2.0; memory-leak soak gate before prod |
| **On-chain / crypto** | `@sources/dune-analytics-mcp.md` | Adopt | Wave 4A; small project, fork-and-pin |
|  | (mcp-etherscan-server) | Steal-from candidate | Wave 4A; license unverified |
|  | (mcp-server-ccxt) | Steal-from candidate | Wave 4A; license unverified |
| **Prediction-markets data** | `@sources/polymarket-predictions-mcp.md` | Adopt-with-caveat | Wave 4A; 3-star single-day-dev bus-factor |
| **Prediction-markets trading** | `@sources/caiovicentino-polymarket-mcp-server.md` | **Adopt** | Wave 5B; 395★ / 45 tools / 5 categories; dual-MCP-Polymarket pattern with kukapay's; 1 contributor (fork-and-pin) |
| **Wiki/Obsidian visual layer** | `@sources/agriciDaniel-claude-obsidian.md` | Steal-from | Wave 5B; 3,581★ MIT (Python+Shell); `/wiki` `/save` `/autoresearch` slash commands; 1 contributor |
| **Internal episodic memory** | `@sources/alash3al-stash.md` | Adopt-Workflow | Wave 5A; 8-stage consolidation pipeline; PostgreSQL+pgvector; 1 contributor (fork-and-pin) |
| **Trading data** | `@sources/tradesdontlie-tradingview-mcp.md` | **Defer + Steal-from** ⚠️ | Wave 4A; Family C TOS-conflict |
| **Documentation injection** | `@sources/upstash-context7.md` | Adopt-Workflow only | Wave 4A; vendor-dependency on proprietary backend |
| **Agent-orchestration** | `@sources/vibe-trading-hkuds.md` | Wave 2 Adopt-Cemini → Wave 4 Steal-from | Status downgrade; React frontend non-starter for prod |
|  | `@sources/mercurialsolo-claudectl.md` | Adopt-Workflow | Multi-session Claude Code orchestrator (plugin, not pure MCP server) |
| **Memory** | `@sources/agentmemory-rohitg00-cpr-impl.md` | Steal-from | cpr-pattern; reference impl |
| **OSINT (Claude Code skill, MCP-adjacent)** | `@sources/7onez-cti-expert.md` | Adopt-Workflow | Wave 4B; AEAD methodology + DAG execution |

**Summary**: 10 MCP-server-shaped sources + 5 Claude-Code-skill / orchestrator-shaped adjacent sources + 2 Steal-from candidates with unverified licenses. **Of the production-deployable MCP servers, only `kb-server` (willynikes2) is currently running on Cemini infrastructure**. Everything else is either Workflow-only (laptop) or queued for cemini-prod-side integration via brief.

### Cross-cutting patterns observed

**Pattern 1 — License distribution skews MIT**:
- 9 of 13 MCP-server sources are MIT-licensed
- 1 is Apache-2.0 (playwright-mcp)
- 1 is **NOASSERTION** (tradingview-mcp — file MIT but trademark disclaimers; Family C)
- 2 are **License Other** (cti-expert MIT+Ethical-Use-Addendum; CC BY-SA in some Wave 4B sources)
- 0 are Family A (copyleft) — copyleft-licensed MCP servers haven't appeared yet but the rubric should expect them

**Pattern 2 — Maturity bimodal**:
- **Big-org high-star Adopts** (Microsoft / Upstash / Microsoft-research): qlib (40k★), context7 (53k★), playwright-mcp (31k★) — high-confidence, follow-upstream pattern
- **Solo-author small-star Adopts** (kukapay / mercurialsolo / 7onez / tradesdontlie): 3-78★ stars — fork-and-pin pattern required; bus-factor caveat applies
- **No middle ground** in our inventory — either institutional-scale or single-developer scale

**Pattern 3 — Vendor-dependency is a separate axis from license**:
- `context7` (Upstash backend) — MIT client + proprietary backend. License is clean; service-availability is a single point of failure.
- `tradingview-mcp` — clean MIT but third-party-data-provider TOS-conflict
- `Spaceshift SateAIs API` — fully proprietary vendor SaaS; different shape entirely
- **License axis ≠ deployment-risk axis**. A clean MIT license does not mean clean adoption.

**Pattern 4 — Cemini-stack vs Workflow scope is the operational dichotomy**:
- **Cemini-stack Adopts** (cemini-prod): kb-server (deployed), dune-analytics-mcp (queued), polymarket-predictions-mcp (queued), Spaceshift SateAIs (queued), last30days-skill extraction (queued)
- **Workflow Adopts** (laptop): context7, claudectl, sentrux, last30days-skill, playwright-mcp, cti-expert, kepano-obsidian-skills
- **Both** (rare): last30days-skill (Workflow + Cemini-stack-extract), Spaceshift (both surfaces)

The dichotomy matters: Cemini-prod is headless / 24/7 / latency-sensitive / TOS-rigorous; Workflow is interactive / on-demand / experimentation-friendly. Same MCP server can be Adopt for one and Defer/Reject for the other.

**Pattern 5 — Family C TOS-conflict is a recurring MCP-specific risk**:
MCP servers that bridge to third-party services (TradingView Desktop, vendor APIs) inherit those services' TOS as a deployment risk. The MCP server's own MIT license doesn't shield Cemini from vendor-TOS exposure. **Worked example**: tradingview-mcp. **Pattern probably extends to**: any future MCP server that scrapes / proxies / wraps a vendor service Cemini doesn't have a direct license relationship with.

### Adoption rubric for new MCP servers

When a new MCP server surfaces (in a sweep, brief, or user drop), score against three filters + 4 quality signals:

**Filter 1 — License + TOS posture** *(hard requirement)*

| Required posture | Pass | Fail |
|---|---|---|
| Code license | MIT / Apache-2.0 / BSD / public domain | AGPL-3.0 / SSPL / GPL-3.0 (Family A); NOASSERTION without LICENSE-file inspection (Family B candidate) |
| Third-party-data-TOS | Direct license OR no third-party data dependency | Wraps vendor service Cemini has no direct relationship with (Family C — Defer to Steal-from at minimum) |

**Filter 2 — Cemini-stack vs Workflow fit** *(determines deployment surface)*

| Surface | Headless? | Latency-tolerant? | TOS-rigorous? | Fit |
|---|---|---|---|---|
| cemini-prod | Yes (req'd) | Sub-second | Strict | Cemini-stack Adopt |
| laptop Workflow | No | Multi-second OK | Permissive | Workflow Adopt |
| librarian | Yes | Multi-second OK | Strict | Librarian Adopt |

**Filter 3 — Bus factor** *(determines maintenance pattern)*

| Maintainer profile | Pattern |
|---|---|
| Big-org / 1k+ stars / 10+ contributors / regular release cadence | **Follow upstream**: install latest; auto-upgrade; rely on org maintenance |
| Mid-tier / 100-1k stars / 2-10 contributors / sporadic releases | **Pin a commit, watch periodically**: install pinned version; manual upgrade after review; revisit quarterly |
| Solo-author / <100 stars / 1 contributor | **Fork-and-maintain in-house**: clone, accept that upstream may go stale; Cemini owns the fork going forward |
| Single-day-dev (created+last-pushed same day) | **Skip OR reimplement** — the MCP surface is usually small enough that reimplementation in a Cemini-controlled repo is cheaper than fork-and-maintain. |

**Quality signals** (more = stronger Adopt):
1. **Code release with verifiable license** — file-level LICENSE inspection passed
2. **Reproducibility hooks** — README has install instructions that work; can stand up a smoke test in <30 minutes
3. **Cemini-domain-aligned tool surface** — the exposed MCP tools map to Cemini's actual analyst needs (data access / quality gates / orchestration)
4. **Fits inside FastMCP's Python ecosystem** — easier integration via `@mcp.tool` decorators on `agents/orchestrator.py`'s LangGraph nodes

### Integration architecture (Cemini-stack)

For any Cemini-stack MCP-server Adopt, the integration pattern is:

```
external MCP server  →  cemini-prod's mcp_client/             →  agents/orchestrator.py (LangGraph)
                                  ↓                                          ↑
                       MCP tool registration                  DeepSeek-V4-flash analyst nodes
                                                              (tool-call invocations during reasoning)
```

The MCP server runs either:
- **co-located** on cemini-prod (preferred for latency-sensitive workloads; e.g., the future dune-analytics-mcp + polymarket-predictions-mcp deployments),
- **co-located** on cemini-librarian (for librarian-scope MCPs; e.g., the deployed kb-server),
- or **remote** (tolerated for Workflow-only Adopts; e.g., context7's mcp.context7.com).

Cemini's analyst nodes consult MCP tools via the standard MCP protocol — no custom adapter required if the server is FastMCP-compatible. Non-FastMCP MCP servers (e.g. TypeScript-implemented like context7) require the standard MCP client; latency cost is one network hop locally.

### Failure-mode taxonomy

When an MCP server in Cemini's deployed stack fails, the failure modes cluster:

| Failure mode | Symptom | Root cause | Mitigation |
|---|---|---|---|
| **Upstream service outage** (vendor-dependency MCPs) | All tool calls hang / return 5xx | External service down (Upstash, Spaceshift, Polymarket-API) | Fallback to cached responses; alert; per-MCP-server circuit breakers |
| **Schema drift** (small-project MCPs) | Tool calls return malformed responses | Upstream API changed | Pin commit hash; manual upgrade after review; reimplementation if upstream abandoned |
| **Memory leak under load** (heavy MCPs like playwright) | OOM after multi-day soak | Resource cleanup bug | 14-day soak gate before production; restart cron |
| **TOS-violation alerts** (Family C MCPs) | Vendor blocks Cemini's IP / account | Cemini's automated use exceeded vendor's allowed scope | Don't deploy Family C in cemini-prod; route data through TOS-cleared providers |
| **Token-budget runaway** (heavy-context MCPs like context7) | Per-query cost spikes | LLM consumes large injected context | Per-tool budget caps in claudectl-equivalent observability layer |

### Operational primitives for Cemini

1. **MCP server registry table** — `wiki/entities/components/cemini-mcp-registry.md` (not yet created — roadmap candidate) listing all currently-registered MCP servers in cemini-prod's mcp_client config; per-server schema, status, last-version-pin, escalation contact. Living document maintained alongside production deployments.

2. **Per-server health check** — extending `scripts/librarian_healthcheck.sh` to probe each registered MCP server's health endpoint on the same 5-min cron. Failure modes route to alerting.

3. **Quarterly MCP-server review** — every 90 days, walk the MCP registry. For each: confirm license still passes; confirm upstream still maintained; consider deprecation candidates. Bus-factor caveat servers get a forced re-evaluation each cycle.

### Maintenance

This page is a meta-rubric like `@concepts/high-signal-paper-patterns.md`. Update whenever:
1. A new MCP server gets ingested as a source page (add to inventory table)
2. A new license pattern surfaces (extend Filter 1)
3. A new failure mode is observed in production (extend taxonomy)
4. The integration architecture evolves (e.g., Cemini swaps FastMCP for an alternative)
5. A pattern that was rare becomes common (e.g., if vendor-dependency MCPs go from 1 to 4, the rubric needs to call them out as a category)

## Snippets

> **MCP-as-deployment-surface observation (the load-bearing claim of this page)**:
>
> Across Waves 2/3/4, of the ~30 candidate Adopts evaluated, ~13 were MCP servers. The MCP-as-deployment-surface pattern is firmly established for Cemini's stack. Workflow A's first sweep also surfaced predominantly MCP servers among the Adopts. Future LLM-agent-tooling sweeps will surface MCP servers at high rates; this page makes the cross-cutting patterns explicit so per-evaluation reasoning is faster. [Source: cross-wave synthesis 2026-04-30]

> **The big-org-vs-solo-dev bimodal pattern (per Wave 4 anti-hallucination spot-check 2026-04-29)**:
>
> Anti-hallucination spot-check on 5 Wave 4A Adopts revealed star counts of 53,681 / 40,300 / 40 / 3 / 2,362. The middle range is empty by accident, not by selection bias — solo-developer MCP-server projects with 100-1000 stars are rare in our inventory. Either an institutional team builds it (high stars, follow-upstream pattern) OR a solo developer ships a single-purpose adapter (low stars, fork-and-pin pattern). The integration architecture must support both. [Source: gemini-dr-wave4a-cemini-stack-2026-04-29.md anti-hallucination findings]

> **Family C TOS-conflict precedent (the operational reason this page exists)**:
>
> "Cemini's automated-trading use case directly conflicts with the project's own README warning about TradingView TOS conflict. The MIT LICENSE file is clean; the third-party-data-provider's TOS isn't. Adoption requires legal review or downgrade to Steal-from with a TOS-cleared data source substituted." [Source: tradesdontlie-tradingview-mcp.md → ip-sale-readiness Family C]
