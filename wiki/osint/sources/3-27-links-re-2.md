---
title: "Targeted Extraction Audit: Cemini Financial Suite — 20-source architectural code-pattern audit (3_27 links re 2.docx)"
type: source
tags: [docx, cemini-internal, architecture-audit, extraction-audit, mcp, langgraph, security, ci-cd, multi-topic]
clusters: [llm-agents, quant-finance, prediction-markets, audit-security, infrastructure, cemini-internal]
keywords: [extraction-audit, compound-engineering, agentos, agno, ag2, mpp-directory, temporal-rest, claude-code-hooks, strix, spring-ai-cve, veeam-rce, safetensors, codebase-to-course, ruflo, byzantine-consensus]
related:
  - concepts/llm-agent-systems.md
  - concepts/quant-finance.md
  - sources/4-11-crypto-re.md
  - sources/ssrn-3247865.md
  - concepts/mcp-tool-marketplace.md
  - sources/signa.md
maturity: validated
read_status: deep-read
created: 2026-04-23
updated: 2026-05-11
---

## Relations

- @concepts/llm-agent-systems.md — cluster hub for LLM agent-systems research; this audit evaluates 10+ agent orchestration platforms
- @concepts/quant-finance.md — Quantitative Finance corpus-index hub
- @sources/4-11-crypto-re.md — sibling Cemini intelligence report, same 8-section format, complementary source set
- @sources/ssrn-3247865.md — the one source this audit tried but failed to retrieve (wrong extraction payload)
- @concepts/mcp-tool-marketplace.md — mpp.directory analysis (agentic spend/budget gates for MCP endpoints)

## Raw Concept

- **Original title**: Targeted Extraction Audit: Cemini Financial Suite
- **Author(s)**: Cemini internal (LLM-generated extraction audit)
- **Type**: DOCX (3,079,696 bytes)
- **Location**: cemini-librarian:/opt/cemini-bulk/research/3_27 links re 2.docx
- **Retrieved**: 2026-04-23 (stub); deep-read 2026-05-02 (via `extract_docx.py` after `scp` from librarian)
- **Length**: 612 lines extracted text; 20 source analyses + works cited
- **Read status**: deep-read

## Narrative

This is a Cemini-internal targeted architectural extraction and code-pattern audit. It evaluates 20 technical sources against the rigid Cemini Financial Suite parameters: Python 3.12, 128GB RAM CPU-only VPS, FastAPI, Redis (pub/sub + Streams via `intel:*`), PostgreSQL/TimescaleDB with pgvector, Pydantic v2, FastMCP, LangGraph 5-agent Devil's Advocate debate, TorchRL + PettingZoo MAPPO (28-feature observation space), SHA-256 + Merkle tree + OpenTimestamps audit trail, strict CI/CD + LGTM observability.

Each source analysis follows the same template: (1) What it is, (2) Architecture patterns worth extracting, (3) Code & logic worth studying, (4) Development workflow & tooling, (5) Agent/LLM/automation patterns, (6) Verdict table with Effort/Impact/Action ratings, (7) What's not useful.

### High-impact ADOPT verdicts

| Source | Key finding | Maps to |
|--------|-------------|---------|
| **EveryInc/compound-engineering-plugin** | CLAUDE.md compounding — runtime experiences write back to static repo state; Git worktree isolation for agent code generation | Developer IDE, CI/CD |
| **agentos/Agno/AG2** | Stateless FastAPI wrapper for multi-agent orchestration; Human-in-the-Loop execution gates | FastAPI / LangGraph / Kalshi exec |
| **mpp.directory/v1** | Agentic spend/budget gates; tool-level approval tags | LangGraph / Kalshi API |
| **luongnv89/claude-howto** | Event-driven lifecycle hooks → Redis Streams; headless CI/CD remediation; graph state rewind/branching | Redis Streams / LangGraph / GitHub Actions |
| **Spring AI CVEs** | Parameterized vector filters (anti-SQLi for pgvector); SSRF outbound allowlists; least-privilege DB roles | PostgreSQL / FastAPI / Docker |
| **Veeam RCE (CVE-2025-23120)** | Ban pickle — use safetensors for TorchRL checkpoints; non-root Docker users | TorchRL / Docker Compose |
| **zarazhangrui/codebase-to-course** | 4-phase deterministic agent pipeline; explicit negative constraints in system prompts | LangGraph nodes / prompts |
| **ruvnet/ruflo** | Byzantine Fault Tolerance truth verification (0.95 threshold); Stream-JSON chaining; prompt-enforced TDD | LangGraph debate / Redis / CI/CD |

### Sources that returned nothing useful

- **SSRN 3247865** — wrong extraction payload (returned luongnv89/claude-howto instead of 151 Trading Strategies)
- **background-agents.com/landscape** — inaccessible, no data retrieved
- **Google Docs presentation** — permissions/paywall blocked
- **MediaTek WiFi CVE / LOTP Windows evasion** — C-kernel/assembly domain, irrelevant to Python 3.12 stack

### Cross-cutting themes

The solo-dev filter is applied ruthlessly throughout: anything requiring Java, Node.js, Rust, GPU, Kubernetes, or external cloud dependencies is flagged RED/HIGH and explicitly rejected. SQLite is consistently rejected in favor of PostgreSQL/TimescaleDB for concurrency reasons.

## Snippets

### S1 — Stack constraint preamble

> "The target infrastructure is rigidly defined as a Python 3.12 stack operating on a single virtual private server (VPS) constrained to 128GB of RAM and CPU-only execution. The system utilizes FastAPI, Redis (configured for both pub/sub and Streams via intel:* channels), PostgreSQL and TimescaleDB with pgvector, Pydantic v2, FastMCP, and a LangGraph orchestration layer running a five-agent Devil's Advocate debate architecture."

### S2 — Veeam safetensors verdict (most critical security finding)

> "The system must explicitly and universally ban the use of Python's built-in pickle module (which suffers from the exact same arbitrary object initialization flaws as the .NET BinaryFormatter). All state serialization must utilize strict, whitelisted schemas via Pydantic v2, and tensor weights must exclusively use safetensors rather than torch.load(weights.pt) to mathematically guarantee memory safety during state reloading."

### S3 — compound-engineering CLAUDE.md compounding

> "Instead of the developer manually updating documentation, the system's runtime experiences directly augment the static repository. Over time, the CLAUDE.md file becomes a highly condensed, domain-specific instruction set perfectly tuned to the Cemini Financial Suite's idiosyncrasies."

### S4 — Ruflo Byzantine consensus

> "Without a mathematical consensus threshold, the debate acts merely as a text generator. By forcing a 0.95 verification threshold, the system guarantees that trades are only executed under conditions of overwhelming statistical confidence."

### S5 — Stateless agent orchestration (Agno/AG2)

> "If the VPS experiences a transient memory spike and the Out-Of-Memory (OOM) killer terminates the FastAPI container, a stateful agent would lose the context of an open Kalshi prediction market order. A stateless architecture instantly resumes the workflow from the last TimescaleDB commit upon container restart."
