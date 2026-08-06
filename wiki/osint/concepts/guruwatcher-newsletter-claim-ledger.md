---

title: GuruWatcher — newsletter claim ledger → Discord (alert-only)
type: concept
tags: [concept, guruwatcher, discord, macro, k200, core-candidate]
keywords: [claim ledger, most-recent-wins, sustain, verbatim guards, Macro Charts]
related:
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
maturity: draft
created: 2026-07-28
updated: 2026-08-06
---

## Relations

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

**GuruWatcher** (Priority #2) turns newsletter **stated numbers** into armed watches:

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
