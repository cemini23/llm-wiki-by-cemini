#!/usr/bin/env bash
# OSINT K273 Phase-1 verify. 0 product Integrate GO. FILE and HITL only.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"
echo "=== K273 Phase-1 verify ==="
python3 scripts/wire_ledger_check.py
test -f .cursor/rules/osint-phase1-adopt-wires.mdc
grep -q "OSINT K273" .cursor/rules/osint-phase1-adopt-wires.mdc
if grep -q "git clone" scripts/adopt-waves/adopt_k273_phase0.sh; then
  echo "phase0 must not clone"
  exit 1
fi
for f in \
  wiki/sources/eval-nfl-dfs-revenue-2026-09-26.md \
  wiki/sources/eval-agent-runtime-revenue-2026-09-26.md \
  wiki/sources/arxiv-2609.29167-indicbankbench-2026-09-26.md \
  wiki/sources/arxiv-2609.29287-aegis-audio-2026-09-26.md \
  wiki/sources/newsletter-rss-latent-space-2026-09-25-openrouter.md \
  wiki/sources/newsletter-rss-sterling-sky-2026-09-24-sterling-virtual-office.md \
  wiki/sources/newsletter-rss-sterling-sky-2026-09-24-sterling-review-gating.md \
  wiki/sources/newsletter-rss-sterling-sky-2026-09-24-sterling-title-length.md \
  wiki/sources/substack-rss-seceng-weekly-2026-09-25-fundamentals.md \
  wiki/sources/substack-rss-secpro-2026-09-25-253-teamcity.md \
  wiki/concepts/k273-harness-evolution-wave.md \
  wiki/concepts/k273-vol-quant-wave.md \
  wiki/concepts/k273-newsletter-macro-wave.md \
  wiki/concepts/k273-gambling-pm-wave.md \
  wiki/concepts/k273-ood-stub-wave.md \
  briefs/2026-09-26_k273-atto.md \
  briefs/2026-09-26_k273-guruwatcher.md \
  briefs/2026-09-26_k273-ceminidfs.md \
  briefs/2026-09-26_k273-ceminiparlays.md \
  briefs/2026-09-26_k273-ccc-harness.md \
  briefs/2026-09-26_k273-cyber-lab.md \
  briefs/2026-09-26_k273-gambling.md \
  briefs/2026-09-26_k273-seo.md
 do test -f "$f" || { echo "MISSING $f"; exit 1; }; done
grep -q "pattern extract" wiki/sources/eval-nfl-dfs-revenue-2026-09-26.md
grep -q "null" wiki/sources/eval-nfl-dfs-revenue-2026-09-26.md
grep -q "showdown" wiki/sources/eval-nfl-dfs-revenue-2026-09-26.md
grep -q "exposure" wiki/sources/eval-nfl-dfs-revenue-2026-09-26.md
grep -q "NOASSERTION" wiki/sources/eval-nfl-dfs-revenue-2026-09-26.md
grep -q "FILE" wiki/concepts/k273-harness-evolution-wave.md
grep -q "policy_wired" wiki/concepts/k273-harness-evolution-wave.md
grep -q "K273" wiki/index.md
grep -q "K273 wave" wiki/log.md
grep -q "K273" ROADMAP.md
test ! -d .local/adopts/draftfast
test ! -d .local/adopts/dfsOptimizer
test ! -d .local/adopts/aegis-audio-defense
echo "0 product Integrate GO. FILE and HITL only. Do not swap /route."
echo "No product install. No skill install. No LIVE Discord. No xsp/pm scp."
echo "Sports pattern extracts stay when SPDX is null. No auto-submit."
echo "=== DONE ==="
