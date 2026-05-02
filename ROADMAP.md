# Roadmap

Companion to: `CLAUDE.md` (schema), `wiki/log.md` (backward-looking log), `LESSONS.md` (meta-lessons).

---

## Vision

CeminiSuite ships to an institutional buyer with a **verifiable execution-security architecture** (K19+K20+K22+K23), a **research-grounded market-making edge** (K24 ParlayMarket + Kalshi), and a **24/7 librarian MCP** serving the deployed brain. Each K-series deep-read adds one reusable architectural primitive. The wiki is the IP catalog.

## Active — this session (2026-05-02)

- **K25 Conductor sweep** — 7 papers ingested: ToolOrchestra, MMGRPO, Training-Free GRPO (×2), GiGPO, MasRouter, StR, Meta-Router. `concepts/conductor-orchestrator.md` synthesis page + architecture diagram + dual deployment paths (A: Trained, B: Token-Prior).
- **K26 ToolOrchestra deep-read** — 8B orchestrator beats GPT-5 on HLE (37.1% vs 35.1%) at 2.5× efficiency. Backlinks + `concepts/llm-agent-systems.md` Relations entries. `conductor-orchestrator.md` promoted draft → validated.
- **Cross-doc dedup Pass 3** — H3-heading fuzzy matching. 0 new content duplicates found beyond Pass 1; infrastructure in place for future ingest.
- **Stale NEEDS-VERIFICATION sweep** — 17 tags resolved across 4 pages: `oracle-networks.md` (7 → CONFIRMED via Exa), `crypto-asset-taxonomy.md` (5 → CONFIRMED against ticker pages, 1 → TENTATIVE), `deepseek-api.md` (3 → date-bumped with server-side blocker notes), `publishers-exclusion.md` (1 → removed).
- **Conductor in-house decision** — finalized. ROADMAP updated, memory saved. Research flag: papers enabling multi-module GRPO, token-prior optimization, compound-AI training.
- **Wiki-tooling smoke test re-run** — llmwiki v0.6.0, nested-path bug confirmed (slug resolver strips `/`). kb-server remains serving layer.
- **SafeHarness backlinks** — 3 bidirectional gaps closed (openclaw-security-taxonomy, reasoning-safety-monitor, sae-execution-contract).
- **tsag dangling ref** — `concepts/deepseek-models.md` stub created + index entry.

## Next — queued

| Item | Notes |
|---|---|
| **Gap-detector pass** | Run `wiki_gap_detect.py` for Type-A (cited-unread stubs) and Type-E (thin concept pages) candidates. |
| **Tier 2 arXiv sweep** | Last sweep 2026-05-01. Session-start ritual prompts if >7 days. |
| **ROADMAP Eventually** | Storage compaction (disk 88% full), bootstrap PDF content index, test suite for scripts. |
| **DeepSeek model IDs** | Confirm `deepseek-chat` vs `deepseek-v4-flash` model IDs against current API docs. Non-blocking documentation task. |

## Decisions — open

### Which LLM brain?

DeepSeek hosted API is the operative path. Local options hardware-gated (7 GB RAM).

### Which conductor? (Fugu vs Trinity vs Conductor) ✅ DECIDED 2026-05-02

**In-house Conductor build.** GRPO maintains policy stability; Training-Free GRPO path enables API-only deployment (no weight access needed). 7 papers already ingested. Flag relevant ICLR/NeurIPS/ACL/EMNLP 2026 papers during sweeps.

### Wiki tooling

**Serving layer: kb-server** — deployed on librarian CPX21, active, 397 docs indexed. llm-wiki-compiler retained on disk for potential future compile-mode use (nested-path bug blocks query/serve). Full analysis: `concepts/wiki-tooling-evaluation.md`.

### Librarian server — remaining phases

| Phase | Item | Status |
|---|---|---|
| 0–3.5 | Provision, sync, kb-server, allowlist, cron | Done |
| 4 | Wire production brain → librarian MCP | Server-stack, next concrete step |
| 5 | Sync cron | Done (folded into 3.5) |
| 6 | Monitoring + tuning | Done (workspace-side); brief shipped to cemini-prod |

## Eventually

- **Storage compaction** — disk 88% full. Market dataset → Parquet; research corpus → SQLite FTS index.
- **Bootstrap full PDF content index** — 230 stubs done. Full deep-read at K-series pace (~12 months).
- **Cited-unread backlog** — 133 stubs. Organic reduction via K-series.
- **Periodic lint as session-start ritual** — low friction, high signal.
- **Workspace ↔ server reconciliation rhythm** — compare page counts / slug parity periodically.
- **Test suite for scripts** — `wiki_lint.py` / `bootstrap_inbox.py` have no coverage.
- **Tier 2.5 `/autoresearch` loop** — Steal-from from claude-obsidian. Port multi-round Exa loop into Path 2.
- **Cross-doc duplicate detection** — hash H2 titles across link-aggregate docs.
- **MCP-tool inventory consolidation** — 130 tools discovered (vs 22 documented). Single canonical inventory.

## Gap detection (3-tier)

| Tier | Status |
|---|---|
| **0** — pre-ingest dup check (`preingest_check.py`) | Done |
| **1** — gap-detection lint (`wiki_gap_detect.py`) | Done |
| **2** — proactive Exa sweeps (user-gated) | Active (Path 1: session-driven) |
| **3** — fully autonomous outbound ingest | Rejected |

## Done — 2026-05-02 session

- **Stash episodic memory deployed** — alash3al/stash v0.2.9 on `cemini-librarian` (5.161.179.207). Postgres 16 + pgvector, Ollama-backed embeddings (nomic-embed-text) + reasoning (qwen2.5:0.5b). Two-layer memory architecture: kb-server (static wiki RAG) + stash (dynamic episodic memory). MCP SSE :8080, HTTP :9090, systemd-managed. Wave 5 Phase 7 complete.

## Done — 2026-05-01 session

- **Phase 4 — brain → librarian MCP** — Audit trail deployed on cemini-prod. E2E verified: fetch_wiki_context("BTC-USD") → 3 sources, 777 chars, ~126ms. KB_HOST hardened.
- **K24** — ParlayMarket deep-read + `concepts/parlay-market-making.md` + kalshi.md extension
- **K23** — Nomotic AI deep-read + nomotic-ai.md primary-source confirmation + six principles
- **K22** — Reasoning Safety Monitor deep-read + `concepts/reasoning-safety-monitor.md`
- **K21** — STOCKBENCH deep-read + stockbench.md correction
- **K20** — OpenClaw deep-read + `concepts/openclaw-security-taxonomy.md`
- **K19** — SAE deep-read + `concepts/sae-execution-contract.md`
- **Cross-cluster synthesis** — `concepts/agent-authorization-stack.md` + `briefs/2026-05-01_execution-security-architecture.md`
- **Infra** — gitignore Node.js, preingest_check.py arXiv scoping fix, ROADMAP Trinity/Conductor K13 update

## Done — prior sessions (highlights)

- **Librarian server** — CPX21 provisioned, kb-server on :3838, 397 docs indexed, sync cron active. Phases 0–3.5 shipped.
- **Wiki tooling evaluation** — `concepts/wiki-tooling-evaluation.md`, 6 source pages, llm-wiki-compiler adoption recommendation.
- **Wave 5** — 4 Adopt (polymarket-mcp, claude-obsidian, alash3al/stash, Kronos tokenizer). 10 source pages. 2 Cemini-prod briefs.
- **K8–K18** — Cemini-internal queue exhausted. K8 strongest stale-snapshot find (128 GB → 7 GB). K13 ES-vs-GRPO evidence. Trinity + Fugu + Conductor lineage closed.
- **CI/CD** — `lint.yml` (push + weekly), `links.yml` (monthly), pre-commit hook (blocks secrets/IPs).
