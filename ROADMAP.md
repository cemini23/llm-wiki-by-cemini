# Roadmap

Companion to: `CLAUDE.md` (schema), `wiki/log.md` (backward-looking log), `LESSONS.md` (meta-lessons).

---

## Vision

CeminiSuite ships to an institutional buyer with a **verifiable execution-security architecture** (K19+K20+K22+K23), a **research-grounded market-making edge** (K24 ParlayMarket + Kalshi), and a **24/7 librarian MCP** serving the deployed brain. Each K-series deep-read adds one reusable architectural primitive. The wiki is the IP catalog.

## Active — this session (2026-05-01)

- **K19–K24 shipped** — six academic deep-reads. SAE (K19), OpenClaw taxonomy (K20), STOCKBENCH (K21), Reasoning Safety Monitor (K22), Nomotic AI (K23), ParlayMarket (K24).
- **Cross-cluster synthesis shipped** — `concepts/agent-authorization-stack.md` (four-layer architecture: Nomotic → Reasoning Monitor → SAE → ParlayMarket). `briefs/2026-05-01_execution-security-architecture.md` (IP-sale artifact).
- **Infra fixes shipped** — gitignore Node.js cruft, preingest_check.py arXiv-ID scoping fix, Trinity/Conductor ROADMAP update with K13 ES-vs-GRPO evidence.
- **Next:** K25 academic-stub routing, or user-directed pivot.

## Next — queued

| Item | Notes |
|---|---|
| **K25 deep-read** | Academic-stub routing by cited-unread density × cluster relevance × recency. 14 remaining Type-A candidates at 2 inbound each. |
| **Phase 4 — brain → librarian MCP** | Server-stack scope. Code shipped; audit-trail + e2e verification remaining. Brief at `briefs/2026-04-30_brain-librarian-mcp-wiring.md`. |
| **Stale NEEDS-VERIFICATION sweep** | All `[NEEDS VERIFICATION]` flags ≥21 days old. K11 fixed the RAM figure; broader sweep queued. |
| **Tier 2 arXiv sweep** | Session-start ritual prompts if last sweep >7 days. Next check: next session. |

## Decisions — open

### Which LLM brain?

DeepSeek hosted API is the operative path. Local options hardware-gated (7 GB RAM). Full analysis: `## Open questions` in prior revisions.

### Which conductor? (Fugu vs Trinity vs Conductor)

| Option | Verdict | Why |
|---|---|---|
| **Fugu beta** | NEEDS VERIFICATION | Closed-beta gate + pricing unknown. If free + acceptable data-egress → dominates. |
| **Trinity (in-house)** | ⚠️ K13 risk | sep-CMA-ES → catastrophic forgetting under sequential cross-asset learning. |
| **Conductor (in-house)** | ✅ K13 advantage | GRPO maintains policy stability. Higher build cost but mathematically safer. |
| **Status quo** | Operative | Linear scatter-gather. P1 ticket on `concepts/scatter-gather-topology.md`. |

**Action:** sign up for Fugu waitlist. Decision gate: Fugu free-tier question first. K13 adds training-stability axis tilting Trinity-vs-Conductor toward Conductor.

### Wiki tooling

Recommendation: adopt `llm-wiki-compiler` (MIT, 7/10 Karpathy ops). Smoke test queued (~30 min). Full analysis: `concepts/wiki-tooling-evaluation.md`.

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
- **`alash3al/stash` episodic memory** — Postgres + pgvector. Phase 7+ candidate.
- **Cross-doc duplicate detection** — hash H2 titles across link-aggregate docs.
- **MCP-tool inventory consolidation** — 130 tools discovered (vs 22 documented). Single canonical inventory.

## Gap detection (3-tier)

| Tier | Status |
|---|---|
| **0** — pre-ingest dup check (`preingest_check.py`) | Done |
| **1** — gap-detection lint (`wiki_gap_detect.py`) | Done |
| **2** — proactive Exa sweeps (user-gated) | Active (Path 1: session-driven) |
| **3** — fully autonomous outbound ingest | Rejected |

## Done — 2026-05-01 session

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
