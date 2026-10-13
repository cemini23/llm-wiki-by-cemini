#!/usr/bin/env bash
# OSINT K290 Phase-1 verify. FILE and HITL only. 0 Integrate GO until Phase-0 runs.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"
echo "=== K290 Phase-1 verify ==="
python3 scripts/wire_ledger_check.py
test -f .cursor/rules/osint-phase1-adopt-wires.mdc
grep -q "OSINT K290" .cursor/rules/osint-phase1-adopt-wires.mdc
grep -q "No-Verifier" .cursor/rules/osint-phase1-adopt-wires.mdc
grep -q "typed symbolic rules" .cursor/rules/osint-phase1-adopt-wires.mdc
grep -q "recognition–action gap" .cursor/rules/osint-phase1-adopt-wires.mdc
grep -q "Muse Wonder" .cursor/rules/osint-phase1-adopt-wires.mdc
for f in \
  wiki/sources/arxiv-2610.12813-vepa-verified-evolving-guardrails-2026-10-13.md \
  wiki/sources/arxiv-2610.12758-distressbench-2026-10-13.md \
  wiki/sources/eval-url-revenue-opportunity-2026-10-13.md \
  wiki/sources/newsletter-rss-latent-space-2026-10-13-ainews-meta-muse-wonder.md \
  wiki/sources/newsletter-rss-pragmatic-engineer-2026-10-13-resilient-ai-systems.md \
  wiki/sources/substack-rss-event-horizon-2026-10-13-gambling-redefinition.md \
  wiki/sources/substack-rss-klement-2026-10-13-ai-productivity-lower-debt.md \
  wiki/sources/substack-rss-wublock-2026-10-13-september-spot-volume.md \
  wiki/concepts/k290-arxiv-wave.md \
  wiki/concepts/k290-eval-wave.md \
  wiki/concepts/k290-feeds-wave.md \
  wiki/concepts/ai-productivity-fiscal-debt.md \
  wiki/concepts/ai-vendor-multimodel-resilience.md \
  wiki/concepts/disaster-recovery-patterns.md \
  wiki/concepts/crypto-exchange-spot-volume.md \
  wiki/entities/models/muse-wonder.md \
  wiki/entities/tools/context-mode.md \
  wiki/entities/tools/vercel-skills.md \
  wiki/entities/tools/decision-3-0.md \
  wiki/entities/tools/claude-show-your-work.md \
  wiki/entities/tools/qwengyre.md \
  wiki/entities/tools/takumi.md \
  wiki/entities/tools/openmed.md \
  briefs/2026-10-13_k290-vepa-and-sandbox-credential-abuse.md \
  briefs/2026-10-13_k290-muse-wonder-and-agent-rl.md \
  briefs/2026-10-13_k290-ai-vendor-resilience-and-debt-watch.md \
  briefs/2026-10-13_k290-gambling-definition-and-parlay-mix.md \
  briefs/2026-10-13_k290-pm-xsp-context-no-scp.md \
  briefs/2026-10-13_k290-atto-pii-pdf-and-diagrams.md \
  briefs/2026-10-13_k290-basgiath-promo-media-tooling.md \
  scripts/adopt_k290_phase0.sh \
  scripts/adopt-waves/adopt_k290_phase0.sh ; do
  [ -f "$f" ] || { echo "MISSING: $f"; exit 1; }
done
echo "OK — all K290 pages, hubs, briefs, and scripts present."
echo "0 Integrate GO. No install. No scrape. No auto-submit."
echo "No xsp/pm scp. Never auto-arm. No watches.json write."
