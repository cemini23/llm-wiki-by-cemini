#!/usr/bin/env bash
# OSINT K269 Phase-1 verify. 0 product Integrate GO. FILE only.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"
echo "=== K269 Phase-1 verify ==="
python3 scripts/wire_ledger_check.py
test -f .cursor/rules/osint-phase1-adopt-wires.mdc
grep -q "OSINT K269" .cursor/rules/osint-phase1-adopt-wires.mdc
for f in \
  wiki/sources/eval-multi-wiki-url-revenue-2026-09-22.md \
  wiki/sources/eval-repository-revenue-2026-09-22.md \
  wiki/sources/arxiv-2609.24972-rrsi-harness-2026-09-22.md \
  wiki/sources/arxiv-2609.24974-harness-zero-2026-09-22.md \
  wiki/sources/newsletter-rss-latent-space-2026-09-21-jev-diogo-2026-09-22.md \
  wiki/concepts/k269-eval-github-wave.md \
  wiki/concepts/k269-harness-evolution-wave.md \
  wiki/concepts/k269-jev-system-one-wave.md \
  wiki/concepts/k269-vol-quant-wave.md \
  wiki/concepts/k269-newsletter-macro-wave.md \
  wiki/concepts/k269-gambling-pm-wave.md \
  wiki/concepts/k269-ood-stub-wave.md \
  wiki/entities/tools/jev-lexer.md \
  wiki/entities/tools/jev-test-filter.md \
  wiki/entities/tools/open-jev-typed-decision-engine.md \
  wiki/entities/tools/jev-search.md \
  wiki/entities/tools/harness-zero.md
 do test -f "$f" || { echo "MISSING $f"; exit 1; }; done
grep -q "K269 ingest" wiki/index.md
grep -q "K269 wave" wiki/log.md
test -d .local/adopts/jev-lexer
test -d .local/adopts/jev-test-filter
test -d .local/adopts/open-jev-typed-decision-engine
test -d .local/adopts/jev-search
echo "0 product Integrate GO. jev-mcp WIRE unchanged. Transkribus sole HTR."
echo "No skill evolve. No LIVE Discord. No xsp/pm scp. Do not swap /route."
echo "=== DONE ==="
