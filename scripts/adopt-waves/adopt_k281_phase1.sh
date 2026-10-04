#!/usr/bin/env bash
# OSINT K281 Phase-1 verify. 0 product Integrate GO. FILE and HITL only.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"
echo "=== K281 Phase-1 verify ==="
python3 scripts/wire_ledger_check.py
test -f .cursor/rules/osint-phase1-adopt-wires.mdc
grep -q "OSINT K281" .cursor/rules/osint-phase1-adopt-wires.mdc
grep -q "NEW PROJECT — Basgiath" .cursor/rules/osint-phase1-adopt-wires.mdc
if grep -q "git clone" scripts/adopt-waves/adopt_k281_phase0.sh scripts/adopt_k281_phase0.sh; then
  echo "phase0 must not clone"; exit 1
fi
for f in \
  wiki/sources/eval-minecraft-bedrock-protocol-2026-10-04.md \
  wiki/sources/eval-minecraft-modding-2026-10-04.md \
  wiki/sources/substack-rss-moontower-2026-10-04-330.md \
  wiki/sources/substack-rss-moontower-2026-10-04-academic-acceleration.md \
  wiki/sources/substack-rss-moontower-2026-10-04-option-ideas.md \
  wiki/sources/substack-rss-wublock-2026-10-04-asia-top10.md \
  wiki/sources/universal-modder-2026-10-04.md \
  wiki/concepts/k281-basgiath-wave.md \
  wiki/concepts/k281-harness-wave.md \
  wiki/concepts/k281-ood-stub-wave.md \
  wiki/concepts/k281-vol-quant-wave.md \
  briefs/2026-10-04_k281-basgiath.md \
  briefs/2026-10-04_k281-ccc-harness.md \
  briefs/2026-10-04_k281-guruwatcher.md \
  briefs/2026-10-04_k281-atto.md
 do test -f "$f" || { echo "MISSING $f"; exit 1; }; done
grep -q "Basgiath" wiki/concepts/k281-basgiath-wave.md
grep -q "universal-modder" wiki/concepts/k281-harness-wave.md
grep -q "INTC" wiki/concepts/k281-vol-quant-wave.md
grep -q "OSINT K281" wiki/index.md
grep -q "K281 wave" wiki/log.md
grep -q "K281" ROADMAP.md
lines=$(wc -l < wiki/log.md | tr -d ' ')
if [ "$lines" -le 10000 ]; then echo "log line count $lines is not above 10000"; exit 1; fi
echo "0 product Integrate GO. FILE and HITL only."
echo "=== DONE ==="
