#!/usr/bin/env bash
# OSINT K268 Phase-1 verify — pages + mdc. No clones, no network.
# Dual-ID: OSINT K268. 0 product Integrate GO. FILE only.
# Do not swap /route. No xsp/pm scp. No LIVE Discord. Never npx github.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"

echo "=== K268 Phase-1 verify ==="
python3 scripts/wire_ledger_check.py

test -f .cursor/rules/osint-phase1-adopt-wires.mdc
grep -q "OSINT K268" .cursor/rules/osint-phase1-adopt-wires.mdc

# 18 source pages
test -f wiki/sources/jev-trading-research-paper-2026-09-21.md
test -f wiki/sources/arxiv-2609.21177-craft-frb-polarimetry-2026-09-21.md
test -f wiki/sources/arxiv-2609.21291-ou-stoch-vol-options-2026-09-21.md
test -f wiki/sources/arxiv-2609.21301-operator-splitting-sv-2026-09-21.md
test -f wiki/sources/arxiv-2609.21554-mirage-creative-reasoning-2026-09-21.md
test -f wiki/sources/arxiv-2609.21684-hmm-equilibrium-prices-2026-09-21.md
test -f wiki/sources/arxiv-2609.21942-failing-robot-ask-2026-09-21.md
test -f wiki/sources/arxiv-2609.22000-recreationworld-2026-09-21.md
test -f wiki/sources/arxiv-2609.22068-codemidas-2026-09-21.md
test -f wiki/sources/substack-rss-capital-flows-2026-09-20-credit-fueled-growth-2026-09-21.md
test -f wiki/sources/substack-rss-event-horizon-2026-09-21-ep33-prediction-markets-2026-09-21.md
test -f wiki/sources/substack-rss-glitchspx-2026-09-20-talon-weekly-sep21-2026-09-21.md
test -f wiki/sources/substack-rss-klement-2026-09-21-heating-hammer-2026-09-21.md
test -f wiki/sources/substack-rss-moontower-2026-09-20-blindsided-2026-09-21.md
test -f wiki/sources/substack-rss-moontower-2026-09-20-end-behavior-2026-09-21.md
test -f wiki/sources/substack-rss-moontower-2026-09-20-moontower-328-2026-09-21.md
test -f wiki/sources/substack-rss-outlier-weekly-2026-09-21-parlay-submit-screen-2026-09-21.md
test -f wiki/sources/substack-rss-wublock-2026-09-21-weekly-outlook-2026-09-21.md

# 8 hubs
test -f wiki/concepts/k268-vol-quant-wave.md
test -f wiki/concepts/k268-harness-evolution-wave.md
test -f wiki/concepts/k268-ood-stub-wave.md
test -f wiki/concepts/k268-game-dev-wave.md
test -f wiki/concepts/k268-newsletter-macro-wave.md
test -f wiki/concepts/k268-gambling-pm-wave.md
test -f wiki/concepts/k268-xsp-signal-wave.md
test -f wiki/concepts/k268-cybersec-wave.md

# Entities
test -f wiki/entities/tools/codemidas.md
test -f wiki/entities/tools/recreationworld.md

# Index / log
grep -q "K268 ingest (2026-09-21)" wiki/index.md
grep -q "K268 wave" wiki/log.md

# Briefs
test -f briefs/2026-09-21_k268-atto.md
test -f briefs/2026-09-21_k268-guruwatcher.md
test -f briefs/2026-09-21_k268-ceminidfs.md
test -f briefs/2026-09-21_k268-ceminiparlays.md
test -f briefs/2026-09-21_k268-ccc-harness.md
test -f briefs/2026-09-21_k268-cyber-lab.md
test -f briefs/2026-09-21_k268-gambling.md
test -f briefs/xsp-k268-glitchspx-talon-sep21.md

# Jev brief add
grep -q "K268 add" briefs/2026-09-19_jev-atto.md
grep -q "K268 add" briefs/2026-09-19_jev-guruwatcher.md
grep -q "K268 add" briefs/2026-09-19_jev-ceminidfs.md
grep -q "K268 add" briefs/2026-09-19_jev-ceminiparlays.md

# Trap checks
grep -q "unread-stub" wiki/sources/jev-trading-research-paper-2026-09-21.md
grep -qi "FRB\|fast radio" wiki/sources/arxiv-2609.21177-craft-frb-polarimetry-2026-09-21.md
grep -qi "NOT.*Atto HTR\|NOT.*handwriting" wiki/sources/arxiv-2609.21177-craft-frb-polarimetry-2026-09-21.md

echo "0 product Integrate GO. FILE only. jev-mcp laptop WIRE unchanged. Do not swap /route."
echo "Transkribus sole HTR. No xsp/pm scp. No LIVE Discord. Never npx github. Never auto-arm."
echo "=== DONE ==="
