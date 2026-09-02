# Super audit — Cemini federation AI harness

**Date:** 2026-09-02  
**Mode:** config-infra + workflow  
**Auditors:** 5 (3 Cursor + 2 OpenRouter) — Ollama slot skipped (down)  
**Tier:** default-5-model  
**Pack:** `reports/audit/pack-ai-harness-20260902`

| Slot | Channel | Role | Model | Verdict |
|------|---------|------|-------|---------|
| 1 | Cursor | config-semantics | Fable 5.1 | REWORK |
| 2 | Cursor | workflow/subscriptions | Grok 4.6 | REWORK |
| 3 | Cursor | adversarial | Grok 4.5 | REWORK |
| 4 | API | api-adversarial | openrouter/fusion | *(pending / slow)* |
| 5 | API | api-deep-reasoning | moonshotai/kimi-k2.5 | *(pending / slow)* |

## Overall: **REWORK** (not REJECT)

The stack is capable but over-built for daily use. ~47% of rule tokens are byte-identical duplicates. Phase-0/Phase-1/`policy_wired` vocabulary confuses operators while executable controls are thin.

---

## Consensus (≥3 auditors)

1. **Demote the 770-line `cemini-phase1-policy-wires.mdc`** from alwaysApply; replace with ≤40-line invariants + wiki as canon.
2. **Stop double-loading rules** — global `~/.cursor/rules/` + per-project copies from `sync_federation_cursor_skills.sh`.
3. **Simplify ingest vocabulary** to three verbs: **FILE** (wiki) · **KEEP** (adopt clone) · **WIRE** (executable change only).
4. **Key by arXiv/slug, not bare K#** — dual-ID footnotes are a symptom, not a fix.
5. **Keep route chain** OpenRouter free → OpenCode Zen → DeepSeek Flash; do **not** replace Flash with OpenCode.
6. **Grok issue is usage/auth**, not just "login" — wiki-ingester fails with 402; fix quota or disable Tier-3 ingest agent.
7. **145 `policy_wired` pages ≠ 145 skills** — skill the six daily-use tools; archive wave hubs as wiki-only.

---

## Top 10 fixes (ranked)

| # | Fix | Impact | Effort |
|---|-----|--------|--------|
| 1 | Sync script: global-only federation rules; prune project copies | ~950 lines/turn saved | Medium |
| 2 | Add `cemini-invariants.mdc` (~40 lines alwaysApply); demote phase1 catalog | ~730 lines/turn | Medium |
| 3 | Promote OSINT hard gates (`osint-phase1-adopt-wires` PII/GW/AGPL) to alwaysApply; demote K246–K253 index | Safety ↑ | Low |
| 4 | Collapse GuruWatcher 53 rules → invariants + optional levels file | ~2100 lines in GW | Medium |
| 5 | `wire-ledger.yaml` + `wire_ledger_check.py`; retire per-wave adopt scripts over time | Clarity ↑ | Medium |
| 6 | Fix/disable failing LaunchAgents (wiki-ingester 402, claude-mem zod) | Log noise ↓ | Low |
| 7 | `grok login` + verify `/usage`; do not attach 22 MCP servers to Grok CLI | Unlock SuperGrok $ | Operator |
| 8 | Start Ollama + Qwen → free 6th super-audit slot + local drafts | $0 utility ↑ | Operator |
| 9 | Federation-sync `cemini-wiki-ingest` + `notebooklm-osint-bridge` | David sees ingest | Low |
| 10 | OpenRouter ranker: prefer Qwen/GLM/Kimi coding models over Nemotron 550B on easy | Quality ↑ | Medium |

---

## Simplify Phase-0 / Phase-1 (operator card)

| Old | New |
|-----|-----|
| Phase-0 audit | **KEEP** — one `adopt.sh --manifest` when cloning |
| Phase-1 wire | **WIRE** — only when a script/skill/hook/rule/MCP changes |
| `policy_wired` | **FILEd** — the wiki page *is* the policy |
| `wont_wire` / `watch` | **FILEd** or **rejected** |
| `runtime_wired` | **wired** with path in ledger |
| K# as ID | Batch label in log only; rules use arXiv/slug |
| "Phase-1 leftover" | Forbidden — session ends FILEd or wired |

**Daily flow:** digest → triage → FILE pages → KEEP if clone worth it → WIRE if executable changed → one `log.md` line.

---

## Subscription matrix

| Service | Verdict |
|---------|---------|
| Cursor Pro | KEEP |
| Claude Max | KEEP |
| SuperGrok | KEEP (fix usage first) |
| DeepSeek API | KEEP |
| OpenRouter | KEEP |
| OpenCode Zen | KEEP (sidecar) |
| Exa | KEEP (cap; arXiv-only digest) |
| Brave | KEEP (free tier) |
| Ollama local | ENABLE (free) |
| ChatGPT Plus / Perplexity / SuperGrok Heavy | DO NOT ADD |

---

## Free utility at same monthly cost

1. Grok login + `/usage` working  
2. Ollama + Qwen 3.5  
3. `/free-audit` for triage (save Cursor Task spend)  
4. Fix OpenRouter free model ranker  
5. File audit `SYNTHESIS.md` → wiki after each council  
6. Six wiki→skills: eval-first-rubric, last30days, pii-redact, claim-ledger, vault-dedupe, osint-catalog  

---

## Patch backlog (Fable plan targets)

- [ ] CCC: `cemini-invariants.mdc` + sync script global-only rules  
- [ ] OSINT: flip alwaysApply on hard gates vs index  
- [ ] CCC: concept page `file-keep-wire-harness.md`  
- [ ] `wiki/meta/wire-ledger.yaml` stub + check script  
- [ ] ROADMAP: Grok 402 vs login clarification  
- [ ] Federation sync ingest + notebooklm skills  
- [ ] GuruWatcher rule collapse (phase 2)  
- [ ] LaunchAgent health doc + disable wiki-ingester until HITL  

---

## Conflicts

- Slot 1 wants delete project rule copies immediately; Slot 3 wants flip alwaysApply before delete — **order: invariants first, then prune copies**.
- API slots 4–5 did not finish in session; Cursor consensus stands without API dissent.
