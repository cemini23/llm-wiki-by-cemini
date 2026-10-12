#!/usr/bin/env bash
# OSINT K289 Phase-1 verify. FILE and HITL only. 0 Integrate GO. No eval docx this wave.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"
echo "=== K289 Phase-1 verify ==="
python3 scripts/wire_ledger_check.py
test -f .cursor/rules/osint-phase1-adopt-wires.mdc
grep -q "OSINT K289" .cursor/rules/osint-phase1-adopt-wires.mdc
grep -q "Repeat-After-Me" .cursor/rules/osint-phase1-adopt-wires.mdc
grep -q "dynamic workflows" .cursor/rules/osint-phase1-adopt-wires.mdc
for f in \
  wiki/sources/arxiv-2610.13044-fomo-flex-options-2026-10-12.md \
  wiki/sources/arxiv-2610.13078-attention-mlp-refusal-2026-10-12.md \
  wiki/sources/arxiv-2610.13485-proactive-agentic-orchestration-2026-10-12.md \
  wiki/sources/arxiv-2610.13494-humanize-mle-agents-2026-10-12.md \
  wiki/sources/arxiv-2610.13543-three-options-rough-heston-2026-10-12.md \
  wiki/sources/arxiv-2610.13647-a-saw-agentic-software-architecture-2026-10-12.md \
  wiki/sources/arxiv-2610.13651-tofu-orchestrator-fuzzing-2026-10-12.md \
  wiki/sources/arxiv-2610.13772-margos-2026-10-12.md \
  wiki/sources/substack-rss-moontower-2026-10-11-iron-condor-destroyer.md \
  wiki/sources/substack-rss-moontower-2026-10-11-farmers-almanac-for-investing.md \
  wiki/sources/substack-rss-moontower-2026-10-11-moontower-331.md \
  wiki/sources/substack-rss-glitchspx-2026-10-11-talon-weekly-oct-12-16.md \
  wiki/sources/substack-rss-capital-flows-2026-10-11-sovereign-debt-volatility.md \
  wiki/sources/substack-rss-event-horizon-2026-10-12-ep36-verifact.md \
  wiki/sources/newsletter-rss-latent-space-2026-10-12-anthropic-dynamic-workflows.md \
  wiki/sources/substack-rss-outlier-weekly-2026-10-12-swarmer-revenue.md \
  wiki/sources/substack-rss-klement-2026-10-12-emissions-trading-schemes.md \
  wiki/sources/substack-rss-wublock-2026-10-11-asia-top10.md \
  wiki/sources/substack-rss-wublock-2026-10-12-weekly-outlook.md \
  wiki/sources/newsletter-rss-sparktoro-2026-10-12-pokemon-pokopia.md \
  wiki/concepts/k289-arxiv-wave.md \
  wiki/concepts/k289-feeds-wave.md \
  briefs/2026-10-12_k289-agent-orchestration.md \
  briefs/2026-10-12_k289-mcp-trust-boundary.md \
  briefs/2026-10-12_k289-xsp-talon-and-almanac.md \
  briefs/2026-10-12_k289-sovereign-debt-vol.md \
  briefs/2026-10-12_k289-cftc-swap-rules.md \
  briefs/2026-10-12_k289-human-made-premium.md
 do test -f "$f" || { echo "MISSING $f"; exit 1; }; done
grep -q "253 verified bugs" wiki/sources/arxiv-2610.13651-tofu-orchestrator-fuzzing-2026-10-12.md
grep -q "95%" wiki/sources/arxiv-2610.13543-three-options-rough-heston-2026-10-12.md
grep -q "OSINT K289" wiki/index.md
grep -q "K289" wiki/log.md
grep -q "K289" ROADMAP.md
echo "0 Integrate GO. FILE and HITL only. No install. No scrape. No auto-submit."
echo "=== DONE ==="
