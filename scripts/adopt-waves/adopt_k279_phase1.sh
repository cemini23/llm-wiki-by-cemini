#!/usr/bin/env bash
# OSINT K279 Phase-1 verify. 0 product Integrate GO. FILE and HITL only.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"
echo "=== K279 Phase-1 verify ==="
python3 scripts/wire_ledger_check.py
test -f .cursor/rules/osint-phase1-adopt-wires.mdc
grep -q "OSINT K279" .cursor/rules/osint-phase1-adopt-wires.mdc
if grep -q "git clone" scripts/adopt-waves/adopt_k279_phase0.sh scripts/adopt_k279_phase0.sh; then
  echo "phase0 must not clone"
  exit 1
fi
for f in \
  wiki/sources/arxiv-2610.01323-trace-2026-10-03.md \
  wiki/sources/arxiv-2610.01349-pace-2026-10-03.md \
  wiki/sources/arxiv-2610.01497-openmtb-2026-10-03.md \
  wiki/sources/arxiv-2610.01769-contra-2026-10-03.md \
  wiki/sources/arxiv-2610.01833-process-eval-2026-10-03.md \
  wiki/sources/eval-multi-repo-revenue-2026-10-03.md \
  wiki/sources/eval-repo-opportunity-2026-10-03.md \
  wiki/sources/newsletter-rss-latent-space-2026-10-02-airbnb-2026-10-03.md \
  wiki/sources/newsletter-rss-latent-space-2026-10-03-ainews-not-much-happened-today.md \
  wiki/sources/substack-rss-secpro-2026-10-02-teamcity-2026-10-03.md \
  wiki/sources/substack-rss-wublock-2026-10-02-weekly-2026-10-03.md \
  wiki/concepts/k279-dfs-parlays-wave.md \
  wiki/concepts/k279-gambling-pm-wave.md \
  wiki/concepts/k279-harness-wave.md \
  wiki/concepts/k279-ood-stub-wave.md \
  wiki/concepts/k279-security-wave.md \
  briefs/2026-10-03_k279-atto.md \
  briefs/2026-10-03_k279-guruwatcher.md \
  briefs/2026-10-03_k279-ceminidfs.md \
  briefs/2026-10-03_k279-ceminiparlays.md \
  briefs/2026-10-03_k279-ccc-harness.md \
  briefs/2026-10-03_k279-cyber-lab.md \
  briefs/2026-10-03_k279-gambling.md \
  briefs/2026-10-03_k279-seo.md
 do test -f "$f" || { echo "MISSING $f"; exit 1; }; done
grep -q "FILE" wiki/concepts/k279-harness-wave.md
grep -q "policy_wired" wiki/concepts/k279-harness-wave.md
grep -q "breakeven" wiki/concepts/k279-dfs-parlays-wave.md
grep -q "No PoC" wiki/concepts/k279-security-wave.md
grep -q "OSINT K279" wiki/index.md
grep -q "K279 wave" wiki/log.md
grep -q "K279" ROADMAP.md
lines=$(wc -l < wiki/log.md | tr -d ' ')
if [ "$lines" -le 10000 ]; then
  echo "log line count $lines is not above 10000"
  exit 1
fi
echo "0 product Integrate GO. FILE and HITL only. Do not swap /route."
echo "=== DONE ==="
