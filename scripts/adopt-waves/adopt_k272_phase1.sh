#!/usr/bin/env bash
# OSINT K272 Phase-1 verify. 0 product Integrate GO. FILE and HITL only.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"
echo "=== K272 Phase-1 verify ==="
python3 scripts/wire_ledger_check.py
test -f .cursor/rules/osint-phase1-adopt-wires.mdc
grep -q "OSINT K272" .cursor/rules/osint-phase1-adopt-wires.mdc
for f in \
  wiki/sources/eval-github-repo-revenue-2026-09-25.md \
  wiki/sources/arxiv-2609.29016-evotreenad-2026-09-25.md \
  wiki/sources/arxiv-2609.29035-bounded-coalescent-2026-09-25.md \
  wiki/sources/arxiv-2609.29333-llm-graders-2026-09-25.md \
  wiki/sources/arxiv-2609.29964-world-action-agent-2026-09-25.md \
  wiki/sources/arxiv-2609.30012-behavior-assays-2026-09-25.md \
  wiki/sources/arxiv-2609.30219-verified-commissioning-2026-09-25.md \
  wiki/sources/arxiv-2609.30249-rapid-2026-09-25.md \
  wiki/sources/arxiv-2609.30266-trace-tamper-2026-09-25.md \
  wiki/sources/newsletter-rss-latent-space-2026-09-24-foundries-navigators.md \
  wiki/sources/newsletter-rss-latent-space-2026-09-25-future.md \
  wiki/sources/newsletter-rss-latent-space-2026-09-25-worldprompt.md \
  wiki/sources/newsletter-rss-pragmatic-engineer-2026-09-24-pulse.md \
  wiki/sources/newsletter-rss-sterling-sky-2026-09-23-gmb-suspension.md \
  wiki/sources/newsletter-rss-tldrsec-2026-09-24-347.md \
  wiki/sources/substack-rss-capital-flows-2026-09-24-rates.md \
  wiki/sources/substack-rss-event-horizon-2026-09-25-kalshi-curry.md \
  wiki/sources/substack-rss-klement-2026-09-25-artist.md \
  wiki/sources/substack-rss-wublock-2026-09-24-bitget.md \
  wiki/sources/substack-rss-wublock-2026-09-24-vitalik.md \
  wiki/sources/substack-rss-wublock-2026-09-25-weekly.md \
  wiki/concepts/k272-harness-evolution-wave.md \
  wiki/concepts/k272-vol-quant-wave.md \
  wiki/concepts/k272-newsletter-macro-wave.md \
  wiki/concepts/k272-gambling-pm-wave.md \
  wiki/concepts/k272-ood-stub-wave.md \
  wiki/entities/tools/modelun.md
 do test -f "$f" || { echo "MISSING $f"; exit 1; }; done
grep -q "MIT" wiki/entities/tools/modelun.md
grep -q "wont_wire" wiki/entities/tools/modelun.md
grep -q "21956" wiki/entities/tools/modelun.md
grep -q "K272 ingest" wiki/index.md
grep -q "K272 wave" wiki/log.md
test ! -d .local/adopts/modelun
test ! -d .local/adopts/phylodyn
test ! -d .local/adopts/wifite2
test ! -d .local/adopts/search
echo "0 product Integrate GO. FILE and HITL only. Do not swap /route."
echo "No product install. No skill evolve. No LIVE Discord. No xsp/pm scp."
echo "Keep the live jev path. Never npx github:."
echo "=== DONE ==="
