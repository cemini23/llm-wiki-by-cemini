#!/usr/bin/env bash
# OSINT K271 Phase-1 verify. 0 product Integrate GO. FILE and HITL only.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"
echo "=== K271 Phase-1 verify ==="
python3 scripts/wire_ledger_check.py
test -f .cursor/rules/osint-phase1-adopt-wires.mdc
grep -q "OSINT K271" .cursor/rules/osint-phase1-adopt-wires.mdc
for f in \
  wiki/sources/eval-multi-wiki-url-revenue-2026-09-24.md \
  wiki/sources/arxiv-2609.27138-commodity-sv-2026-09-24.md \
  wiki/sources/arxiv-2609.27542-control-token-2026-09-24.md \
  wiki/sources/arxiv-2609.27606-state-grounded-conditioning-2026-09-24.md \
  wiki/sources/arxiv-2609.27612-regenharness-2026-09-24.md \
  wiki/sources/arxiv-2609.27620-inguard-2026-09-24.md \
  wiki/sources/arxiv-2609.27639-echo-chambers-2026-09-24.md \
  wiki/sources/arxiv-2609.27717-skillgym-2026-09-24.md \
  wiki/sources/arxiv-2609.27720-corelnav-2026-09-24.md \
  wiki/sources/newsletter-rss-latent-space-2026-09-24-meta-connect.md \
  wiki/sources/substack-rss-event-horizon-2026-09-24-wc-broadcasts.md \
  wiki/sources/substack-rss-klement-2026-09-24-ai-debt.md \
  wiki/sources/substack-rss-klement-2026-09-24-acquisitions.md \
  wiki/concepts/k271-harness-evolution-wave.md \
  wiki/concepts/k271-vol-quant-wave.md \
  wiki/concepts/k271-newsletter-macro-wave.md \
  wiki/concepts/k271-gambling-pm-wave.md \
  wiki/concepts/k271-ood-stub-wave.md \
  wiki/entities/tools/jev-curate.md \
  wiki/entities/tools/canny.md
 do test -f "$f" || { echo "MISSING $f"; exit 1; }; done
grep -q "K271 ingest" wiki/index.md
grep -q "K271 wave" wiki/log.md
test -d .local/adopts/jev-curate
test -d .local/adopts/canny
test ! -d .local/adopts/deleting-the-trace
test ! -d .local/adopts/skillgym
test ! -d .local/adopts/inguard
echo "0 product Integrate GO. FILE and HITL only. Do not swap /route."
echo "No product install. No skill evolve. No LIVE Discord. No xsp/pm scp."
echo "Keep the live jev path. Never npx github:."
echo "=== DONE ==="
