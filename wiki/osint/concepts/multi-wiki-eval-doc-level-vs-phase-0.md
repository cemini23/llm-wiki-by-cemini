---
title: "Multi-wiki tool evaluation: doc-level verdict vs Phase-0 source audit"
type: concept
tags: [concept, methodology, evaluation, license-audit, phase-0-audit, doc-level-gate, k43, k44]
keywords: [doc-level-eval, phase-0-source-audit, two-gate-pattern, license-claim-verification, star-inflation, llm-eval-skepticism, ip-sale-readiness]
related:
  - sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md
  - sources/eval-github-repos-2026-05-13.md
  - entities/tools/bukosabino-ta.md
  - entities/tools/tradingview-mcp-atilaahmettaner.md
  - entities/tools/aulekator-polymarket-btc-bot.md
  - concepts/cemini-license-posture.md
  - sources/multi-wiki-link-eval-v4-2026-05-15.md
maturity: validated
created: 2026-05-14
updated: 2026-05-15
---

## Relations

- @sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md — K44 (28-URL eval), source-of-formalization
- @sources/eval-github-repos-2026-05-13.md — K43 (14-repo eval), origin lesson
- @entities/tools/bukosabino-ta.md — K43 ADOPT → Phase-0 NO-GO (parallel implementation)
- @entities/tools/tradingview-mcp-atilaahmettaner.md — K43 ADOPT → Phase-0 NO-GO (TOS gate)
- @entities/tools/aulekator-polymarket-btc-bot.md — K44 ADOPT → Phase-0 pending
- @concepts/cemini-license-posture.md — IP-sale lens applied at both gate levels
- @sources/multi-wiki-link-eval-v4-2026-05-15.md — K46 v4 evaluation provides updated tier distribution across 40 URLs, validating the two-gate pattern

## Raw Concept

The Cemini wiki ingest pipeline distinguishes two evaluation gates for third-party tools:

1. **Doc-level eval** — license + maturity-metric + stack-fit screening done from a source document (typically a paid-research deep-research output or LLM-synthesized eval). Cheap; high false-positive rate on Adopt verdicts.
2. **Phase-0 source audit** — clone the repo to `/tmp`, verify license file matches the claim, verify maturity signals via `gh api`, run the tool's most-likely-failure-mode test (per tool class). Costlier; high accuracy.

**Both gates required** before any code is adopted into `/opt/cemini` or any Cemini production wiki. The lesson, formalized in K43 and reconfirmed in K44, is that doc-level eval is necessary but not sufficient.

## Narrative

### Origin (K43, 2026-05-13)

The K43 source-doc eval (`@sources/eval-github-repos-2026-05-13.md`) ranked 5-of-5 ADOPTs as MIT-clean. Two of those (bukosabino/ta, tradingview-mcp) progressed to Phase-0 source audits. **Both Phase-0 audits returned NO-GO** for failure modes the doc-level eval could not see:

- **bukosabino/ta — NO-GO**: parallel-implementation conflict with already-adopted `pandas-ta-classic` (K30) — same 43-indicator set, identical API. Doc-level eval did not have visibility into Cemini's existing adoption state.
- **tradingview-mcp — NO-GO**: TradingView TOS gate — the doc-level eval audited the wrapper's MIT license but not the wrapped service's commercial-redistribution rights. Phase-0 source-read of the dependency chain exposed the gap.

### K44 application

The K44 eval (28 URLs, all 6 wikis) reproduces the doc-level pattern: 7 Adopts + 7 Steal-froms ranked from a single LLM-synthesized document. **Every K44 Adopt is now marked `maturity: adopt-doc-level-pending-phase-0`** until its Phase-0 source audit clears.

One K44 finding bypassed the gate: `geo-seo-claude` was independently Phase-0-audited by SEO-wiki on 2026-05-07 (a week before K44) and shipped GO. K44's doc-level Adopt converges with the prior Phase-0 GO — the convergence elevates the K44 eval's signal-quality for *this specific* finding. All other K44 Adopts remain doc-level-only.

### The two-gate pattern, formalized

| Gate | Inputs | Outputs | Cost | False-positive rate |
|------|--------|---------|------|---------------------|
| Doc-level | Source eval doc (3rd-party LLM, deep-research output, vendor white paper, etc.) | Tier verdict (Adopt / Steal-from / Defer / Reject) | ~5 min per URL | High (~40% on K43 Adopts went on to fail Phase-0) |
| Phase-0 | Doc-level verdict + repo URL + tool class | GO / CONDITIONAL-GO / NO-GO + reconsideration gates | ~30-60 min per URL (Explore subagent) | Low (~5% — gates remaining are operational, not classification) |

### What Phase-0 specifically catches that doc-level cannot

1. **Parallel-implementation conflicts** — doc-level eval doesn't know what's already adopted. Phase-0 cross-references against existing entity pages.
2. **Dependency-chain TOS gates** — doc-level filters the wrapper's license but not the wrapped service's redistribution rights.
3. **Stale-deps compounding** — doc-level reports last-commit but doesn't run dep-tree analysis. Phase-0 catches Python 3.12 / pandas 2.x incompatibility on libraries pinned to older versions.
4. **Star-count inflation** — doc-level cites star counts as claimed. Phase-0 runs `gh api` and checks star/fork ratio + commit cadence + contributor count.
5. **Hardcoded directory layout** — doc-level can't see if a wiki-tooling library has hardcoded directory structure that breaks nested-wiki support.
6. **License-file mismatch** — doc-level reads the eval's license field; Phase-0 reads the actual LICENSE file.

### Implementation discipline

- Every Adopt entity created from a doc-level eval starts at `maturity: adopt-doc-level-pending-phase-0`.
- Phase-0 audits are scheduled via ROADMAP (K-series follow-ups).
- Successful Phase-0 → flip `maturity` to `validated` and add verdict table to the entity page.
- Failed Phase-0 → flip `maturity` to `no-go-phase-0-YYYY-MM-DD`, add Dead Ends entry, document reconsideration gates.

### LLM-generated eval — additional skepticism flags

When a doc-level eval is itself LLM-synthesized (vs human research), apply elevated Phase-0 priority on:

- Star counts >5,000 stars for solo maintainers (high prior for inflation)
- "Anti-hallucination protocols" self-claims (it's itself a hallucination tell)
- Hyperbolic language ("ruthless," "catastrophic," "absolute") — markers of synthesis
- Footnote citations without bibliography — reduces reproducibility
- Convergent verdicts across multiple LLM-generated evals are weak signals (they may share training data); convergent verdicts across one LLM-generated eval and one human Phase-0 audit (e.g., geo-seo-claude) are strong signals.

## Snippets

> "Doc-level ADOPT vs source-level Phase-0: the K43 source-doc audit ranked 5 of 5 ADOPTs as MIT-clean. Both ML/MCP candidates that progressed to Phase-0 caught failure modes the doc-level eval missed."
[Source: hot.md (post-K43), 2026-05-13 lesson capture]

## Dead Ends

- **The two-gate pattern is not unique to Cemini.** Any IP-sale-bound knowledge base that ingests third-party software needs both gates. Documenting this concept page for portability — image-gen-wiki, seo-wiki, ccc-wiki should adopt the same gate discipline (some already do; geo-seo-claude SEO-wiki Phase-0 is an example).
- **Phase-0 budget is the bottleneck.** Each Phase-0 takes ~30-60 min of Explore subagent time. A 14-Adopt batch (K44) is 7-14 hours of audit work — multi-session. Prioritize by IP-sale risk: betterleaks first (pre-IP-sale audit critical), then Polymarket-BTC bot (direct Cemini fit), then the rest by primary-wiki demand.
