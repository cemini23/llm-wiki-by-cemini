#!/usr/bin/env bash
# OSINT K278 Phase-1 verify. 0 product Integrate GO. FILE and HITL only.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"
echo "=== K278 Phase-1 verify ==="
python3 scripts/wire_ledger_check.py
test -f .cursor/rules/osint-phase1-adopt-wires.mdc
grep -q "OSINT K278" .cursor/rules/osint-phase1-adopt-wires.mdc
if grep -q "git clone" scripts/adopt-waves/adopt_k278_phase0.sh scripts/adopt_k278_phase0.sh; then
  echo "phase0 must not clone"
  exit 1
fi
for f in \
  wiki/sources/arxiv-2610.00340-barrier-option-2026-10-02.md \
  wiki/sources/arxiv-2610.00633-genealogy-db-constraints-2026-10-02.md \
  wiki/sources/arxiv-2610.01187-american-slsv-2026-10-02.md \
  wiki/sources/arxiv-2610.01955-dyor-forecasting-2026-10-02.md \
  wiki/sources/arxiv-2610.02036-global-coherence-2026-10-02.md \
  wiki/sources/arxiv-2610.02072-pypottery-2026-10-02.md \
  wiki/sources/arxiv-2610.02200-vista-2026-10-02.md \
  wiki/sources/arxiv-2610.02206-kalibench-2026-10-02.md \
  wiki/sources/eval-repo-revenue-2026-10-02.md \
  wiki/sources/newsletter-rss-latent-space-2026-10-02-pi-durable-2026-10-02.md \
  wiki/sources/newsletter-rss-latent-space-2026-10-02-rlm-zhang-2026-10-02.md \
  wiki/sources/substack-rss-event-horizon-2026-10-02-sponsored-pm-data-2026-10-02.md \
  wiki/sources/substack-rss-klement-2026-10-02-smoke-this-study-2026-10-02.md \
  wiki/concepts/k278-atto-htr-wave.md \
  wiki/concepts/k278-gambling-pm-wave.md \
  wiki/concepts/k278-harness-wave.md \
  wiki/concepts/k278-ood-stub-wave.md \
  wiki/concepts/k278-security-wave.md \
  wiki/concepts/k278-vol-quant-wave.md \
  briefs/2026-10-02_k278-atto.md \
  briefs/2026-10-02_k278-guruwatcher.md \
  briefs/2026-10-02_k278-ceminidfs.md \
  briefs/2026-10-02_k278-ceminiparlays.md \
  briefs/2026-10-02_k278-ccc-harness.md \
  briefs/2026-10-02_k278-cyber-lab.md \
  briefs/2026-10-02_k278-gambling.md \
  briefs/2026-10-02_k278-seo.md
 do test -f "$f" || { echo "MISSING $f"; exit 1; }; done
grep -q "FILE" wiki/concepts/k278-harness-wave.md
grep -q "policy_wired" wiki/concepts/k278-harness-wave.md
grep -q "Transkribus stays" wiki/concepts/k278-atto-htr-wave.md
grep -q "No PoC" wiki/concepts/k278-security-wave.md
grep -q "OSINT K278" wiki/index.md
grep -q "K278 wave" wiki/log.md
grep -q "K278" ROADMAP.md
lines=$(wc -l < wiki/log.md | tr -d ' ')
if [ "$lines" -le 10000 ]; then
  echo "log line count $lines is not above 10000"
  exit 1
fi
for d in \
  .local/adopts/SimdPaddleOCR \
  .local/adopts/context-mode \
  .local/adopts/caveman \
  .local/adopts/PyPottery \
  .local/adopts/VISTA
 do test ! -d "$d" || { echo "CLONE DIR PRESENT $d"; exit 1; }; done
echo "0 product Integrate GO. FILE and HITL only. Do not swap /route."
echo "=== DONE ==="
