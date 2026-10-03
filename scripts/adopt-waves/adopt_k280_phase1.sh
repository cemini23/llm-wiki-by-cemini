#!/usr/bin/env bash
# OSINT K280 Phase-1 verify. 0 product Integrate GO. FILE and HITL only.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"
echo "=== K280 Phase-1 verify ==="
python3 scripts/wire_ledger_check.py
test -f .cursor/rules/osint-phase1-adopt-wires.mdc
grep -q "OSINT K280" .cursor/rules/osint-phase1-adopt-wires.mdc
grep -q "POSTURE CHANGE" .cursor/rules/osint-phase1-adopt-wires.mdc
if grep -q "git clone" scripts/adopt-waves/adopt_k280_phase0.sh scripts/adopt_k280_phase0.sh; then
  echo "phase0 must not clone"
  exit 1
fi
for f in \
  wiki/sources/eval-htr-repos-2026-10-03.md \
  wiki/sources/eval-monte-carlo-repos-2026-10-03.md \
  wiki/concepts/k280-atto-htr-wave.md \
  wiki/concepts/k280-dfs-wave.md \
  wiki/concepts/k280-ood-stub-wave.md \
  briefs/2026-10-03_k280-atto-htr-decision.md \
  briefs/2026-10-03_k280-ceminidfs.md
 do test -f "$f" || { echo "MISSING $f"; exit 1; }; done
grep -q "kraken" wiki/concepts/k280-atto-htr-wave.md
grep -q "CATMuS" wiki/concepts/k280-atto-htr-wave.md
grep -q "particle" wiki/concepts/k280-dfs-wave.md
grep -q "OSINT K280" wiki/index.md
grep -q "K280 wave" wiki/log.md
grep -q "K280" ROADMAP.md
lines=$(wc -l < wiki/log.md | tr -d ' ')
if [ "$lines" -le 10000 ]; then
  echo "log line count $lines is not above 10000"
  exit 1
fi
echo "0 product Integrate GO. FILE and HITL only."
echo "=== DONE ==="
