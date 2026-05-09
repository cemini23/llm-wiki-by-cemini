# Hot — session-state cache

Ephemeral curator working memory. Read first on session start; rewritten at session end. Gitignored.

## Position (end of 2026-05-08 session, K33 regime-disclosure gate SHIPPED)

- **K-series**: K33 complete (BLADE listwise alignment + Regime-Conditioned BO evaluation, 2026-05-07). Regime-disclosure gate shipped 2026-05-08.
- **Latest commit**: TBD (regime-disclosure gate commit pending).
- **Wiki**: 555 pages indexed (550 + 5 K33 pages), license-pattern catalog stable at 10 modes.
- **skill_audit.py v0.2**: regime-disclosure gate shipped — 7 checks (0.25/0.15/0.15/0.10/0.10/0.05/0.10 weights). All 4 test briefs PASS. No false positives on K28-K30 adoption briefs.

## Monetization-priority directive (2026-05-06)

User: "license its going to be a bit before we sell but i need to start making money here with this soon so we need to do what we need to do."

Effects: license auto-rejects soften for non-prod-codebase use. Phase-0 audit rigor unchanged. Saved as project memory `monetization_priority_2026.md`. Re-confirm 2027+.

## Current state — workspace idle, ready for next K

K33 closed. Regime-disclosure gate shipped and verified.

### Shipped workspace-laptop briefs

| Brief | Status |
|-------|--------|
| `briefs/2026-05-06_obsidian-llm-wiki-local-steal-from.md` | Phase 1 ✓ / Phase 2 deferred (bundles with brief-audit-upgrade sprint) |
| `briefs/2026-05-07_regime-disclosure-brief-audit-gate.md` | **SHIPPED 2026-05-08** — `scripts/skill_audit.py` v0.2 with regime-disclosure veto gate, all tests PASS |

skill_audit v0.2: 7 checks, regime-disclosure is a veto gate (Scientific Integrity). Static score weights rebalanced: required_sections 0.25, crosslinks 0.15, citations 0.15, needs_verification 0.10, prose_quality 0.10, frontmatter 0.05, regime_disclosure 0.10.

### Bundled brief-audit upgrade sprint (NOT YET DRAFTED)

K32+K33 surfaced 4 STEAL-FROM/concept-driven upgrades that all touch `scripts/skill_audit.py`:
- `academic-paper-skills` 35-point peer-review framework (K32, highest priority — 4-6 hr port)
- `research-paper-writing-skills` claim-evidence + abstract synthesis (K32, 2-3 hr port)
- `codex-startup-pressure-test-skill` adversarial review prompts (K32, 1-2 hr port)
- **Regime-disclosure gate** (K33, SHIPPED 2026-05-08) — 1-2 hr, independent-shippable
- **Plus `_llm_retry.py` helper** (Phase 2 of obsidian brief) — bundles with sprint

Decision pending: bundle as one combined `brief-audit-upgrade-sprint.md` (~13 hr) OR ship sequentially.

### 9 active prod briefs at `cemini-prod:/opt/cemini/briefs/` awaiting prod-side execution

| Brief | What it ships |
|-------|---------------|
| `2026-05-04_klaassen-magnus-elo-cemini-fastmcp.md` | Tennis Elo math + commercial-data sourcing |
| `2026-05-04_quant-libs-fastmcp-integration.md` | Riskfolio-Lib + FinanceToolkit + FinanceDatabase (K30-updated) |
| `2026-05-04_probablyprofit-pattern-extraction.md` | Kelly + ensemble + kill-switch |
| `2026-05-05_polymarket-stack-adoption.md` | Polymarket Agents + python-order-utils + py-clob-client + polymarket-mcp-server |
| `2026-05-05_pykalashi-adoption.md` | pykalashi replaces bloated official Kalshi SDK |
| `2026-05-05_conductor-audit-trail-phase1.md` | Conductor fitness function + audit JSONL + git-tracked config commits |
| `2026-05-06_hftbacktest-adoption.md` (K31) | Microsecond-tick HFT backtester |
| `2026-05-06_guidance-ai-adoption.md` (K31) | Microsoft structured-generation library |
| `2026-05-06_ttok-prod-install.md` (K31) | ttok Pipfile addition + pre-call audit hook |

### 2 deferred-with-triggers prod briefs (unchanged)

| Brief | Trigger |
|-------|---------|
| `2026-05-04_autoresearch-conductor-evolution.md` (Phases 2-6) | traffic ≥ 3,500 Conductor decisions/week sustained ≥ 2 weeks AND explicit buyer/research signal |
| `2026-05-04_xskill-cross-rollout-critique-conductor.md` | same |

## Open follow-ups

- **Brief-audit upgrade sprint decision** — bundle vs sequential. Regime-disclosure gate (K33) already shipped standalone; remaining 3 STEAL-FROMs + `_llm_retry.py` await decision.
- **Phase 4 of obsidian-llm-wiki-local** — `wiki_lint.py --fix-bidirectional` mode is standalone-shippable (~30 min). Low priority.
- **Cemini-prod ttok install** — staged; awaits prod-side execution (single Pipfile addition).
- **hftbacktest Phase 0 audit** — GO (MIT license, Production/Stable v2.4.4, wheel install on Hetzner confirmed). Brief `2026-05-06_hftbacktest-adoption.md` updated and ready for prod staging. Phase 1 sandbox replication is next.
- **Sakana 2026-04-27 NV tags Exa-resolution** — 12 stale `[NEEDS VERIFICATION 2026-04-27]` tags pending focused Exa-cross-check pass.
- **Tier 2 arXiv sweep** — last 2026-05-01; due ~2026-05-08 per 7-day cadence.
- **Storage compaction** — disk 88% full; market-dataset Parquet conversion + research-corpus SQLite FTS index.

## Key file locations (end of 2026-05-08)

- ROADMAP: `/Users/claudiobarone/Desktop/OSINT WORKSPACE/ROADMAP.md`
- log: `/Users/claudiobarone/Desktop/OSINT WORKSPACE/wiki/log.md`
- index: `/Users/claudiobarone/Desktop/OSINT WORKSPACE/wiki/index.md`
- license catalog: `/Users/claudiobarone/Desktop/OSINT WORKSPACE/wiki/concepts/cemini-license-posture.md`
- staged brief: `briefs/2026-05-07_regime-disclosure-brief-audit-gate.md` (SHIPPED)
- scripts: `scripts/skill_audit.py` v0.2 (regime-disclosure gate shipped)
- raw source: `cemini-librarian:/opt/cemini-bulk/research/5_6 links.docx`
- prod ccd-cli: `cemini-prod:/root/.claude/remote/ccd-cli/{2.1.111,2.1.128}`
- rewind config: stored in rewind's own keystore; `rewind config show` to see redacted state
- laptop `.env`: contains `DEEPSEEK_API_KEY`, `LIBRARIAN_API_KEY`, `GROQ_API_KEY`, `GEMINI_API_KEY`

## Session-start ritual reminders

1. Read this file
2. Check `wiki/sweeps/*.md` mtime — sweep due ~2026-05-08
3. Check `research to be indexed/` for new sources (currently empty)
4. If prod desktop-app fails on first message after a Claude Code update: verify `ssh cemini-prod 'env | grep IS_SANDBOX'` returns `IS_SANDBOX=1`.
