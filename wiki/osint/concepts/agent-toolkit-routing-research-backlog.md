---
title: Agent-Toolkit Routing Research Backlog
type: concept
hub: true
tags: [concept, routing, llm, infra, backlog, k233]
keywords: [routing, failover, kv-capacity, workload-aware, provider-proxy, backlog]
related:
  - sources/arxiv-2608.11152-mixed-rl-rollouts-2026-08-12.md
  - sources/newsletter-pragmatic-engineer-optiver-2026-08-11.md
  - sources/newsletter-pragmatic-engineer-charity-majors-ai-2026-08-12.md
  - concepts/agent-harness-verification-bottleneck.md
  - entities/tools/opencodex.md
  - entities/tools/opencode.md
  - entities/tools/reasonix.md
  - entities/tools/quotio.md
  - entities/tools/reasoning-bank.md
  - concepts/llm-routing-deepseek-openrouter-failover.md
  - concepts/prop-trading-engineering-2026.md
  - entities/tools/codex-self-improving-loop.md
  - entities/tools/sentrux.md
  - sources/arxiv-2608.11683-frontierfinance-2026-08-13.md
  - sources/newsletter-rss-latent-space-2026-08-13-grok-46.md
  - concepts/role-specialization-model-rsm.md
  - concepts/socratic-answer-withholding-contract.md
  - concepts/agentic-legacy-code-modernization.md
  - entities/tools/vakra.md
  - entities/tools/claude-task-viewer.md
  - sources/arxiv-2608.12282-vakra-tool-policies-2026-08-13.md
  - sources/arxiv-2608.12311-rsm-role-specialization-2026-08-13.md
  - entities/tools/qwengyre.md
tags: [concept, routing, llm, infra, backlog, k233, k234]
updated: 2026-08-12
---

## Relations

- @sources/arxiv-2608.11152-mixed-rl-rollouts-2026-08-12.md — MISA-T
- @sources/newsletter-pragmatic-engineer-optiver-2026-08-11.md — AI gateway + MCP hosting platform
- @sources/newsletter-pragmatic-engineer-charity-majors-ai-2026-08-12.md — harness > model; verification bottleneck (K234)
- @concepts/agent-harness-verification-bottleneck.md
- @entities/tools/opencodex.md — GO Integrate provider proxy
- @entities/tools/opencode.md — coding agent Phase-0 (name collision with opencodex); NO-GO mid swap
- @entities/tools/reasonix.md — DeepSeek-native CLI Phase-0; NO-GO mid swap
- @entities/tools/quotio.md — quota-aware failover
- @entities/tools/reasoning-bank.md — WATCH
- @concepts/llm-routing-deepseek-openrouter-failover.md
- @concepts/prop-trading-engineering-2026.md
- @entities/tools/codex-self-improving-loop.md
- @entities/tools/sentrux.md
- @sources/arxiv-2608.11683-frontierfinance-2026-08-13.md — finance-agent benchmark; harness > model (K235)
- @sources/newsletter-rss-latent-space-2026-08-13-grok-46.md — Grok 4.6 SFT-from-harness-trajectories (K235)
- @concepts/role-specialization-model-rsm.md — role scope boundaries (K235)
- @concepts/socratic-answer-withholding-contract.md — deterministic policy core recipe (K235)
- @concepts/agentic-legacy-code-modernization.md — verification-oracle boundary (K235)
- @entities/tools/vakra.md — tool-policy benchmark, reference-only (K235)
- @entities/tools/claude-task-viewer.md — observability surface (K235)
- @sources/arxiv-2608.12282-vakra-tool-policies-2026-08-13.md
- @sources/arxiv-2608.12311-rsm-role-specialization-2026-08-13.md
- @entities/tools/qwengyre.md

## Raw Concept

What this page answers: what routing-related research/patterns the agent-toolkit lane (llm-routing-deepseek-openrouter-failover) should track next. Accumulated from K233–K235 sources.

## Narrative

**Backlog bump (K233):**

1. **MISA-T (arXiv 2608.11152)** — workload-aware KV-capacity + residency-time-aware admission for mixed RL rollout serving (+53.3% throughput over sweep-tuned vLLM router). Research relevance: heterogeneous agentic sessions competing for KV/capacity need priority/weight-aware admission, not just latency/cache optimization. Not a prod wiring — RL-post-training infra.
2. **opencodex (K233 GO Integrate)** — universal provider proxy unifying Codex/Claude Code/Grok lanes across Anthropic/Gemini/Grok/DeepSeek/Ollama; candidate to consolidate the DeepSeek/OpenRouter failover surface.
3. **Quotio (K233 Extract)** — quota-aware round-robin/fill-first failover pattern for stall-proof token-heavy sessions.
4. **Optiver AI gateway + MCP hosting platform** — industry blueprint of the "models-as-a-service + agent tool layer" pattern this workspace approximates with conductor + MCP tools; validates the direction.

**Backlog bump (K234):**

5. **Charity Majors / harness verification** — harness infrastructure and post-generate verification beat model-chasing; maps to `/route` SIP Verify gate. See `@concepts/agent-harness-verification-bottleneck.md`.

**Backlog bump (2026-08-12 claude-ds refresh):**

6. **OpenCode / Reasonix** — Phase-0 complete. Keep isolated `claude-ds` (Claude Code 2.1.222). Neither is a `/route` mid drop-in. See `@entities/tools/opencode.md`, `@entities/tools/reasonix.md`. `opencodex` (K233) remains the provider-**proxy** candidate, not a coding loop.
7. **Flash vs Pro (wired 2026-08-12)** — V4 Pro GA is the Grok CLI usage-out stand-in inside the same `claude-ds` process. Do not add a second harness. Watch for official DeepSeek Harness; keep adapter slot.

**Backlog bump (K235):**

8. **Grok 4.6 harness notes** — SFT trajectories regenerated by Grok 4.5 across *agent harnesses* + agentic RL (coding/knowledge-work/kernel/CAD) is the frontier recipe for long-running agents; maps to `/route` execute-stage quality. See `@sources/newsletter-rss-latent-space-2026-08-13-grok-46.md`.
9. **VAKRA tool-policy gap** — multi-hop + policy-constrained tool use is where agents break (best 50–51% compositional; 2.4% on unanswerable queries); failures concentrate at language-mediated reasoning (entity disambiguation, cross-source grounding), not tool mechanics. CC BY-NC-SA → methodology reference only. See `@entities/tools/vakra.md`.
10. **RSM role specialization** — role-scope boundaries + negative-constraint prompt hardening + rule-file bloat caution (over-detailed rule files *reduce* success rates). See `@concepts/role-specialization-model-rsm.md`.
11. **Tutor withhold contract** — deterministic policy core + detector + LLM judge + persona-driven measure–diagnose–fix loop as the reusable "refuse a capability you have" recipe. See `@concepts/socratic-answer-withholding-contract.md`.
12. **HPC modernization oracle** — delegate only where a domain verification oracle sees; bit-for-bit goldens caught a bug that survived agents + compiler. See `@concepts/agentic-legacy-code-modernization.md`.
13. **FrontierFinance (Samaya)** — 220-query finance-agent benchmark; harness > model (56.0% in-house vs 49.2% best frontier under open harness); Kimi K3 46.4% at 4.5× lower cost. Eval reference only — no XSP/LEAPS hook, no prod dump. See `@sources/arxiv-2608.11683-frontierfinance-2026-08-13.md`.
14. **claude-task-viewer (K235 GO Integrate)** — MIT verified, cloned `.local/adopts/claude-task-viewer`; read-only Kanban for `~/.claude/tasks/` as the harness observability surface (pairs optionally with quotio quota board).

Any of these being wired to prod requires a separate `/phase1` proposal — this page is the tracking surface, not a wire.

[Source: arXiv 2608.11152; Pragmatic Engineer 2026-08-11 + 2026-08-12; K233 + K235 evals]
