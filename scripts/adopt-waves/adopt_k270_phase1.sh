#!/usr/bin/env bash
# OSINT K270 Phase-1 verify. 0 product Integrate GO. FILE only.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"
echo "=== K270 Phase-1 verify ==="
python3 scripts/wire_ledger_check.py
test -f .cursor/rules/osint-phase1-adopt-wires.mdc
grep -q "OSINT K270" .cursor/rules/osint-phase1-adopt-wires.mdc
for f in \
  wiki/sources/arxiv-2609.25447-conduct-under-pressure-2026-09-23.md \
  wiki/sources/arxiv-2609.25518-matryoshka-attribution-2026-09-23.md \
  wiki/sources/arxiv-2609.25686-task-state-influence-2026-09-23.md \
  wiki/sources/arxiv-2609.26499-local-coding-agent-manipulation-2026-09-23.md \
  wiki/sources/arxiv-2609.26606-option-rebate-design-2026-09-23.md \
  wiki/sources/arxiv-2609.26760-grow-the-harness-2026-09-23.md \
  wiki/sources/arxiv-2609.26779-cliffcompaction-2026-09-23.md \
  wiki/sources/arxiv-2609.26781-agensh-2026-09-23.md \
  wiki/sources/newsletter-rss-latent-space-2026-09-22-john-platt.md \
  wiki/sources/newsletter-rss-latent-space-2026-09-23-opus-55.md \
  wiki/sources/newsletter-rss-latent-space-2026-09-23-bio-security.md \
  wiki/sources/newsletter-rss-pragmatic-engineer-2026-09-22-windows-ai.md \
  wiki/sources/newsletter-rss-pragmatic-engineer-2026-09-23-appleton.md \
  wiki/sources/newsletter-rss-sparktoro-2026-09-23-algorithms.md \
  wiki/sources/substack-rss-capital-flows-2026-09-22-kospi.md \
  wiki/sources/substack-rss-event-horizon-2026-09-23-cftc-mention-markets.md \
  wiki/sources/substack-rss-klement-2026-09-23-who-forecasts.md \
  wiki/sources/substack-rss-wublock-2026-09-23-bstocks.md \
  wiki/sources/newsletter-rss-sterling-sky-2026-09-22-gbp-batch.md \
  wiki/concepts/k270-harness-evolution-wave.md \
  wiki/concepts/k270-vol-quant-wave.md \
  wiki/concepts/k270-newsletter-macro-wave.md \
  wiki/concepts/k270-gambling-pm-wave.md \
  wiki/concepts/k270-ood-stub-wave.md \
  wiki/entities/tools/cliffcompaction.md \
  wiki/entities/tools/modelun.md \
  wiki/entities/tools/agensh.md
 do test -f "$f" || { echo "MISSING $f"; exit 1; }; done
grep -q "K270 ingest" wiki/index.md
grep -q "K270 wave" wiki/log.md
test -d .local/adopts/cliffcompaction
test ! -d .local/adopts/modelun
test ! -d .local/adopts/agensh
echo "0 product Integrate GO. FILE only. Do not swap /route."
echo "No skill evolve. No LIVE Discord. No xsp/pm scp. Never npx github:."
echo "=== DONE ==="
