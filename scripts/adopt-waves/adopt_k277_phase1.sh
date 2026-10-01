#!/usr/bin/env bash
# OSINT K277 Phase-1 verify. 0 product Integrate GO. FILE and HITL only.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"
echo "=== K277 Phase-1 verify ==="
python3 scripts/wire_ledger_check.py
test -f .cursor/rules/osint-phase1-adopt-wires.mdc
grep -q "OSINT K277" .cursor/rules/osint-phase1-adopt-wires.mdc
if grep -q "git clone" scripts/adopt-waves/adopt_k277_phase0.sh scripts/adopt_k277_phase0.sh; then
  echo "phase0 must not clone"
  exit 1
fi
for f in \
  wiki/sources/arxiv-2609.39256-sk-calibration-2026-10-01.md \
  wiki/sources/arxiv-2609.39684-distributed-document-analysis-2026-10-01.md \
  wiki/sources/arxiv-2609.39902-codemimicry-2026-10-01.md \
  wiki/sources/arxiv-2609.40169-scholarevolve-2026-10-01.md \
  wiki/sources/arxiv-2609.40303-minimal-harness-2026-10-01.md \
  wiki/sources/arxiv-2609.40306-dynaharness-2026-10-01.md \
  wiki/sources/arxiv-2609.40324-cogentic-2026-10-01.md \
  wiki/sources/arxiv-2609.40330-turbo-harness-2026-10-01.md \
  wiki/sources/newsletter-rss-latent-space-2026-09-30-why-dwarkesh-is-wrong-about-computer-use-how-ope.md \
  wiki/sources/newsletter-rss-latent-space-2026-10-01-ainews-gemini-4-argon-gdms-answer-to-astrafable.md \
  wiki/sources/newsletter-rss-sterling-sky-2026-09-29-the-1-checklist-to-optimize-your-google-business.md \
  wiki/sources/newsletter-rss-tldrsec-2026-10-01-tldr-sec-348---googles-pagebreak-scanner-perplex.md \
  wiki/sources/substack-rss-event-horizon-2026-10-01-polymarket-adds-responsible-trading-tools.md \
  wiki/sources/substack-rss-klement-2026-10-01-flippin-heck.md \
  wiki/sources/substack-rss-wublock-2026-10-01-september-vc-report-crypto-vc-funding-rises-more.md \
  wiki/concepts/k277-atto-htr-wave.md \
  wiki/concepts/k277-gambling-pm-wave.md \
  wiki/concepts/k277-harness-evolution-wave.md \
  wiki/concepts/k277-ood-stub-wave.md \
  wiki/concepts/k277-security-wave.md \
  wiki/concepts/k277-vol-quant-wave.md \
  briefs/2026-10-01_k277-atto.md \
  briefs/2026-10-01_k277-guruwatcher.md \
  briefs/2026-10-01_k277-ceminidfs.md \
  briefs/2026-10-01_k277-ceminiparlays.md \
  briefs/2026-10-01_k277-ccc-harness.md \
  briefs/2026-10-01_k277-cyber-lab.md \
  briefs/2026-10-01_k277-gambling.md \
  briefs/2026-10-01_k277-seo.md
 do test -f "$f" || { echo "MISSING $f"; exit 1; }; done
grep -q "FILE" wiki/concepts/k277-harness-evolution-wave.md
grep -q "policy_wired" wiki/concepts/k277-harness-evolution-wave.md
grep -q "Transkribus stays" wiki/concepts/k277-atto-htr-wave.md
grep -q "No PoC" wiki/concepts/k277-security-wave.md
grep -q "OSINT K277" wiki/index.md
grep -q "K277 wave" wiki/log.md
grep -q "K277" ROADMAP.md
lines=$(wc -l < wiki/log.md | tr -d ' ')
if [ "$lines" -le 10000 ]; then
  echo "log line count $lines is not above 10000"
  exit 1
fi
for d in \
  .local/adopts/turbo-harness \
  .local/adopts/ScholarEvolve \
  .local/adopts/CodeMimicry
 do test ! -d "$d" || { echo "CLONE DIR PRESENT $d"; exit 1; }; done
echo "0 product Integrate GO. FILE and HITL only. Do not swap /route."
echo "=== DONE ==="
