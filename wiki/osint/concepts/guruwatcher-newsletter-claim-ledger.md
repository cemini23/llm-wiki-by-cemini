---

title: GuruWatcher — newsletter claim ledger → Discord (alert-only)
type: concept
tags: [concept, guruwatcher, discord, macro, k200, core-candidate]
keywords: [claim ledger, most-recent-wins, sustain, verbatim guards, Macro Charts]
related:
  - entities/tools/weathernext.md
  - entities/tools/flights-rpc.md
  - sources/eval-url-batch-agentic-edge-security-2026-08-05.md
  - sources/substack-rss-klement-2026-08-05-data-centre-reality-check.md
  - entities/tools/cloudflare-os.md
  - entities/tools/cloudflare-temp-email.md
  - entities/tools/ai-surface.md
  - entities/tools/jumpcutter.md
  - sources/guruwatcher-pricing-strategy-research-2026-08-04.md
  - sources/macro-charts-paid-forward-2026-08-05-spx-sox-gdx-yields.md
  - sources/macro-charts-paid-forward-2026-08-04-smh-tech-chat.md
  - sources/macro-charts-paid-forward-2026-08-03-everything-is-about-to-change.md
  - sources/eval-github-revenue-evaluation-docuscan-reader-2026-08-03.md
  - entities/tools/llm-reader.md
  - sources/substack-rss-wublock-2026-08-02-asia-top10.md
  - sources/substack-rss-wublock-2026-08-03-mining-july.md
  - entities/tools/jobseek.md
  - sources/substack-rss-outlier-weekly-2026-07-28-guruwatcher-discord.md
  - entities/tools/guruwatcher.md
  - concepts/macro-charts-regime-signals.md
  - concepts/active-project-research-routing.md
  - sources/macro-charts-paid-forward-2026-07-28-korea-wti-fomc.md
  - sources/macro-charts-paid-forward-2026-07-30-korea-semis.md
  - sources/substack-rss-wublock-2026-07-30-hidden-price-of-treasuries.md
  - sources/macro-charts-paid-forward-2026-07-31-situational-awareness-kospi.md
  - sources/macro-charts-paid-forward-2026-08-06.md
  - entities/tools/mubeng.md
  - sources/substack-rss-capital-flows-2026-08-18-next-stage-macro.md
  - entities/tools/llm-as-a-verifier.md
  - sources/guruwatcher-production-readiness-audit-2026-09-03.md
  - concepts/k267-newsletter-macro-wave.md
  - entities/tools/winnow.md
  - entities/tools/openjev-razorback.md
maturity: draft
created: 2026-07-28
updated: 2026-09-20
---

## Relations

- @concepts/k267-newsletter-macro-wave.md
- @entities/tools/winnow.md
- @entities/tools/openjev-razorback.md
- @sources/guruwatcher-production-readiness-audit-2026-09-03.md — 3 Sep NO-GO; GW-05 discards published_at; GW-06 strips `<`; GW-07 binds the wrong symbol
- @entities/tools/weathernext.md — K230
- @entities/tools/flights-rpc.md — K229 flights Extract

- @sources/macro-charts-paid-forward-2026-08-06.md

- @entities/tools/jumpcutter.md

- @sources/guruwatcher-pricing-strategy-research-2026-08-04.md

- @sources/macro-charts-paid-forward-2026-08-05-spx-sox-gdx-yields.md

- @sources/macro-charts-paid-forward-2026-08-04-smh-tech-chat.md

- @sources/macro-charts-paid-forward-2026-08-03-everything-is-about-to-change.md — K221 paid forward
- @sources/eval-github-revenue-evaluation-docuscan-reader-2026-08-03.md — K221 llm-reader
- @entities/tools/llm-reader.md
- @sources/macro-charts-paid-forward-2026-07-31-situational-awareness-kospi.md — K215

- @sources/substack-rss-wublock-2026-07-30-hidden-price-of-treasuries.md — K214

- @sources/macro-charts-paid-forward-2026-07-30-korea-semis.md — Jul 30 Korea/Semis chat

- @sources/substack-rss-outlier-weekly-2026-07-28-guruwatcher-discord.md — public methodology post
- @entities/tools/guruwatcher.md
- @concepts/macro-charts-regime-signals.md — levels come from regime letters
- @concepts/active-project-research-routing.md — Priority #2 brief home
- @sources/macro-charts-paid-forward-2026-07-28-korea-wti-fomc.md

## Raw Concept

How do paid regime newsletters become reliable Discord level alerts without becoming an order bot?

## Narrative

**GuruWatcher** (Priority #2) turns newsletter **stated numbers** into armed watches. 3 Sep production audit is **NO-GO**: `published_at` is discarded (GW-05), HTML cleanup deletes `<`/`>` (GW-06), and DOTALL extract can bind a level to the wrong symbol (GW-07). Do not promote 0.1.7 until those High findings have tests.


| Rule | Meaning |
|------|---------|
| Alert-only | Discord webhook; never orders / CeminiSuite executor |
| Claim ledger | `(symbol, op, level, verbatim, published_at)` |
| Most-recent-wins | New issue updates mentioned symbols only; others persist |
| Verbatim guards | Snippet must appear; level in snippet; instrument near level; band sanity; reject year-truncation (`2026` ≠ VIX 20) |
| Soft lists / chart-only | Unarmed — no invented numbers |
| Sustain | Default 2×15min polls ≈ 30 min before fire |
| Prod owns state | Laptop extract → sync **claims**; do not wholesale replace watches.json |

Ops: dedicated Discord webhook; fail closed if missing; UW OHLC + yfinance fallback. Code: `~/Projects/GuruWatcher` · inbox hook `scripts/guru_watcher_inbox_hook.sh` · OSINT `scripts/macro_charts_watch.py` cousin.
