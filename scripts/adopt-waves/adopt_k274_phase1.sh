#!/usr/bin/env bash
# OSINT K274 Phase-1 verify. 0 product Integrate GO. FILE and HITL only.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"
echo "=== K274 Phase-1 verify ==="
python3 scripts/wire_ledger_check.py
test -f .cursor/rules/osint-phase1-adopt-wires.mdc
grep -q "OSINT K274" .cursor/rules/osint-phase1-adopt-wires.mdc
if grep -q "git clone" scripts/adopt-waves/adopt_k274_phase0.sh scripts/adopt_k274_phase0.sh; then
  echo "phase0 must not clone"
  exit 1
fi
for f in \
  wiki/sources/eval-sports-analytics-revenue-2026-09-27.md \
  wiki/sources/eval-nfl-data-revenue-2026-09-27.md \
  wiki/sources/outlier-voyg-profit-paper-2026-09-27.md \
  wiki/sources/substack-rss-glitchspx-2026-09-27-talon-weekly.md \
  wiki/sources/substack-rss-wublock-2026-09-26-magic-eden.md \
  wiki/sources/substack-rss-wublock-2026-09-27-asia-top10.md \
  wiki/concepts/k274-harness-evolution-wave.md \
  wiki/concepts/k274-vol-quant-wave.md \
  wiki/concepts/k274-newsletter-macro-wave.md \
  wiki/concepts/k274-gambling-pm-wave.md \
  wiki/concepts/k274-ood-stub-wave.md \
  briefs/2026-09-27_k274-atto.md \
  briefs/2026-09-27_k274-guruwatcher.md \
  briefs/2026-09-27_k274-ceminidfs.md \
  briefs/2026-09-27_k274-ceminiparlays.md \
  briefs/2026-09-27_k274-ccc-harness.md \
  briefs/2026-09-27_k274-cyber-lab.md \
  briefs/2026-09-27_k274-gambling.md \
  briefs/2026-09-27_k274-seo.md
 do test -f "$f" || { echo "MISSING $f"; exit 1; }; done
grep -q "null" wiki/sources/eval-sports-analytics-revenue-2026-09-27.md
grep -q "pattern" wiki/sources/eval-sports-analytics-revenue-2026-09-27.md
grep -q "parquet" wiki/sources/eval-sports-analytics-revenue-2026-09-27.md
grep -q "null" wiki/concepts/k274-gambling-pm-wave.md
grep -q "FILE" wiki/concepts/k274-harness-evolution-wave.md
grep -q "policy_wired" wiki/concepts/k274-harness-evolution-wave.md
grep -q "OSINT K274" wiki/index.md
grep -q "K274 wave" wiki/log.md
grep -q "K274" ROADMAP.md
lines=$(wc -l < wiki/log.md | tr -d ' ')
if [ "$lines" -le 10000 ]; then
  echo "log line count $lines is not above 10000"
  exit 1
fi
for d in \
  .local/adopts/cfbfastR-cfb-data \
  .local/adopts/cfbfastR-data \
  .local/adopts/nfl-closing-speed-csoe \
  .local/adopts/weathernfl \
  .local/adopts/nfldata \
  .local/adopts/nfl-betting-data \
  .local/adopts/porra-mundial-nanos-2026 \
  .local/adopts/football \
  .local/adopts/open-data \
  .local/adopts/football-odds-scanner \
  .local/adopts/on3-recruit-scraper \
  .local/adopts/Real-Time-NFL-Stats
 do test ! -d "$d" || { echo "CLONE DIR PRESENT $d"; exit 1; }; done
echo "0 product Integrate GO. FILE and HITL only. Do not swap /route."
echo "No product install. No skill install. No LIVE Discord. No xsp/pm scp."
echo "A null SPDX on a sports row still records the pattern. No tree is cloned."
echo "=== DONE ==="
