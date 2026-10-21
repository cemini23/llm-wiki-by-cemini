---
title: K293 osint wave — options-agent loss limits, IV surfaces, and the inbox fan-out (Oct 2026)
type: concept
related:
  - sources/arxiv-addmart-iv-surface-2610.25671-2026-10-20.md
  - sources/arxiv-options-agent-safeguards-2610.24289-2026-10-20.md
  - sources/arxiv-abf-bench-2610.23656-2026-10-20.md
  - sources/k293-osint-feeds-2026-10-20.md
  - sources/arxiv-k293-skipped-no-lane-2026-10-20.md
  - concepts/options-agent-order-boundary.md
  - concepts/kalshi-retail-lp.md
maturity: draft
updated: 2026-10-20
---

## Raw Concept

OSINT K293, 2026-10-20. Full inbox pass. 83 files, 37 distinct PDFs, 18 newsletters at the inbox root. Most PDFs were byte-identical copies of papers already filed. The digest fan-out from K292 is still open. No install. No trade. No scrape. No xsp or pm scp. No `/route` swap.

## Narrative

Three osint claims change a decision. The rest are filed so the arXiv ids stop coming back as new.

1. **Loss limits sit outside the model.** @sources/arxiv-options-agent-safeguards-2610.24289-2026-10-20.md and @concepts/options-agent-order-boundary.md. Of 26 shipped options agents, 13 can reach unbounded loss, including 6 of 8 broker interfaces. None authenticate their text sources.
2. **Build the IV surface as a martingale.** @sources/arxiv-addmart-iv-surface-2610.25671-2026-10-20.md. Static no-arbitrage by construction, not by a penalty. No trade.
3. **Cite the ledger row you retrieved.** @sources/arxiv-abf-bench-2610.23656-2026-10-20.md. A forensics harness at 75% edge recall against 10% for Claude Code, which cites records it never retrieved.

Feeds are in @sources/k293-osint-feeds-2026-10-20.md. Kalshi trailing seven-day volume on 18 Oct is **$21.5bn**, parlays **70.7%** of Sunday's $4.11bn. Muse Spark Open leads US open weights on one index and ranks last of the top nine on agentic evals. **No `/route` swap.**

Skipped, with the ids in Raw Concept so preingest marks them duplicate next time: `2610.18802`, `2610.20896` (pure math, third inbox appearance), `2610.23419` (mmWave handwriting). See @sources/arxiv-k293-skipped-no-lane-2026-10-20.md.

Safety, harness, visual-tool, and functional-CAD papers from this same drop are filed under cybersec, ccc, image-gen, and 3d-printing. This page does not repeat them.
