#!/usr/bin/env bash
# OSINT K292 Phase-1 verify. FILE and HITL only. 0 Integrate GO.
#
# K292 was a feeds + eval + arXiv wave. The inbox held a fan-out defect: the same
# 16 arXiv PDFs across all eight domain inboxes, 8 already ingested. This gate
# asserts the wave's pages exist in the right domains, the wires section landed,
# the ledger is clean, and the two no-relevance papers stayed skipped.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
echo "=== K292 Phase-1 verify ==="

echo "1. wire ledger"
python3 scripts/wire_ledger_check.py

echo "2. wires section"
test -f .cursor/rules/osint-phase1-adopt-wires.mdc
grep -q "OSINT K292" .cursor/rules/osint-phase1-adopt-wires.mdc
grep -q "fans out" .cursor/rules/osint-phase1-adopt-wires.mdc
grep -q "leantoken" .cursor/rules/osint-phase1-adopt-wires.mdc

echo "3. pages exist, in the owning domain"
for f in \
  wiki/osint/concepts/k292-osint-wave.md \
  wiki/osint/sources/k292-osint-feeds-2026-10-16.md \
  wiki/osint/sources/eval-url-multi-wiki-repository-2026-10-16.md \
  wiki/osint/sources/arxiv-betinn-2610.19254-2026-10-16.md \
  wiki/osint/sources/arxiv-theophyseval-2610.16733-2026-10-16.md \
  wiki/osint/sources/arxiv-librarian-agents-2610.22273-2026-10-16.md \
  wiki/osint/concepts/anticipatory-workspace-curation.md \
  wiki/ccc/concepts/k292-ccc-wave.md \
  wiki/ccc/sources/arxiv-opengcua-2610.22200-2026-10-16.md \
  wiki/ccc/sources/arxiv-mlexpert-2610.22344-2026-10-16.md \
  wiki/ccc/concepts/computer-use-agent-harness.md \
  wiki/ccc/concepts/execution-window-rl.md \
  wiki/3d-printing/concepts/k292-3d-printing-wave.md \
  wiki/3d-printing/sources/arxiv-3dcodeverse-2610.22341-2026-10-16.md \
  wiki/3d-printing/concepts/executable-3d-verification-harness.md \
  wiki/image-gen/concepts/k292-image-gen-wave.md \
  wiki/image-gen/sources/arxiv-omniverifier-c1-2610.22355-2026-10-16.md \
  wiki/image-gen/concepts/decomposed-graded-verifier.md \
  scripts/adopt_k292_phase0.sh ; do
  [ -f "$f" ] || { echo "MISSING: $f"; exit 1; }
done
echo "   all K292 pages present"

echo "4. the two no-relevance papers stayed skipped"
for id in 2610.18802 2610.20896; do
  if grep -rq "$id" wiki/*/sources/ 2>/dev/null; then
    echo "   UNEXPECTED: $id has a source page. It was assessed as no-relevance."
    exit 1
  fi
done
echo "   confirmed: no source page for 2610.18802 or 2610.20896"

echo "5. the Integrate rows carry their verified licence, and are still not adopted"
EV=wiki/osint/sources/eval-url-multi-wiki-repository-2026-10-16.md
grep -q "leantoken.*Apache-2.0" "$EV" || { echo "   MISSING: leantoken licence reading"; exit 1; }
grep -q "flameox.*MIT" "$EV" || { echo "   MISSING: flameox licence reading"; exit 1; }
grep -q "0 Integrate GO" "$EV" || { echo "   MISSING: the no-GO statement"; exit 1; }
grep -q "Phase-0 status — RUN 2026-10-16" "$EV" || { echo "   MISSING: the Phase-0 result"; exit 1; }
echo "   eval page carries the verified readings and still says 0 Integrate GO"

echo "OK — K292 Phase-1 clean."
echo "0 Integrate GO. No install. No clone committed. No scrape."
echo "No xsp/pm scp. Never auto-arm. No watches.json write."
