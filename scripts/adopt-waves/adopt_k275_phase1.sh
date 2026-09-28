#!/usr/bin/env bash
# OSINT K275 Phase-1 verify. 0 product Integrate GO. FILE and HITL only.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"
echo "=== K275 Phase-1 verify ==="
python3 scripts/wire_ledger_check.py
test -f .cursor/rules/osint-phase1-adopt-wires.mdc
grep -q "OSINT K275" .cursor/rules/osint-phase1-adopt-wires.mdc
if grep -q "git clone" scripts/adopt-waves/adopt_k275_phase0.sh scripts/adopt_k275_phase0.sh; then
  echo "phase0 must not clone"
  exit 1
fi
for f in \
  wiki/sources/eval-systems-revenue-stack-2026-09-28.md \
  wiki/sources/arxiv-2609.31047-dynbranch-2026-09-28.md \
  wiki/sources/arxiv-2609.31255-pia-2026-09-28.md \
  wiki/sources/arxiv-2609.31263-option-factor-zoo-2026-09-28.md \
  wiki/sources/arxiv-2609.31418-cognitivereality-2026-09-28.md \
  wiki/sources/arxiv-2609.31490-authority-commit-2026-09-28.md \
  wiki/sources/arxiv-2609.31511-muslim-voice-2026-09-28.md \
  wiki/sources/arxiv-2609.31524-cvs-assessment-2026-09-28.md \
  wiki/sources/arxiv-2609.31570-rough-vol-2026-09-28.md \
  wiki/sources/substack-rss-apricitas-2026-09-27-creative-class.md \
  wiki/sources/substack-rss-event-horizon-2026-09-28-episode-34.md \
  wiki/sources/substack-rss-klement-2026-09-28-kfw-climate.md \
  wiki/sources/substack-rss-moontower-2026-09-27-329.md \
  wiki/sources/substack-rss-moontower-2026-09-27-soulcraft.md \
  wiki/sources/substack-rss-moontower-2026-09-27-taylor-cheatsheet.md \
  wiki/sources/substack-rss-wublock-2026-09-28-payrolls-outlook.md \
  wiki/concepts/k275-harness-evolution-wave.md \
  wiki/concepts/k275-vol-quant-wave.md \
  wiki/concepts/k275-newsletter-macro-wave.md \
  wiki/concepts/k275-gambling-pm-wave.md \
  wiki/concepts/k275-ood-stub-wave.md \
  briefs/2026-09-28_k275-atto.md \
  briefs/2026-09-28_k275-guruwatcher.md \
  briefs/2026-09-28_k275-ceminidfs.md \
  briefs/2026-09-28_k275-ceminiparlays.md \
  briefs/2026-09-28_k275-ccc-harness.md \
  briefs/2026-09-28_k275-cyber-lab.md \
  briefs/2026-09-28_k275-gambling.md \
  briefs/2026-09-28_k275-seo.md
 do test -f "$f" || { echo "MISSING $f"; exit 1; }; done
grep -q "FILE" wiki/concepts/k275-harness-evolution-wave.md
grep -q "policy_wired" wiki/concepts/k275-harness-evolution-wave.md
grep -q "OSINT K275" wiki/index.md
grep -q "K275 wave" wiki/log.md
grep -q "K275" ROADMAP.md
lines=$(wc -l < wiki/log.md | tr -d ' ')
if [ "$lines" -le 10000 ]; then
  echo "log line count $lines is not above 10000"
  exit 1
fi
for d in \
  .local/adopts/changedetection.io \
  .local/adopts/openrig \
  .local/adopts/notebooklm-py \
  .local/adopts/llama.cpp \
  .local/adopts/iLEAPP \
  .local/adopts/PLFM_RADAR \
  .local/adopts/mimalloc-pprof
 do test ! -d "$d" || { echo "CLONE DIR PRESENT $d"; exit 1; }; done
echo "0 product Integrate GO. FILE and HITL only. Do not swap /route."
echo "=== DONE ==="
