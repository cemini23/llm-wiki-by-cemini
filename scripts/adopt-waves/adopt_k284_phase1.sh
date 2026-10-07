#!/usr/bin/env bash
# OSINT K284 Phase-1 verify. 0 product Integrate GO — design/tooling leads only. FILE and HITL only.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"
echo "=== K284 Phase-1 verify ==="
python3 scripts/wire_ledger_check.py
test -f .cursor/rules/osint-phase1-adopt-wires.mdc
grep -q "OSINT K284" .cursor/rules/osint-phase1-adopt-wires.mdc
grep -q "storytold" .cursor/rules/osint-phase1-adopt-wires.mdc
grep -q "Strata" .cursor/rules/osint-phase1-adopt-wires.mdc
for f in \
  wiki/sources/eval-developer-resource-2026-10-07.md \
  wiki/sources/eval-url-revenue-opportunity-2026-10-07.md \
  wiki/sources/arxiv-2610.07554-bspline-galerkin-cgmy-2026-10-07.md \
  wiki/sources/arxiv-2610.07686-bluffjax-2026-10-07.md \
  wiki/sources/arxiv-2610.08621-recursive-game-creator-2026-10-07.md \
  wiki/sources/arxiv-2610.08630-in-parameter-memory-survey-2026-10-07.md \
  wiki/sources/arxiv-2610.08720-worldsolver-2026-10-07.md \
  wiki/sources/arxiv-2610.08722-compaction-harm-prediction-2026-10-07.md \
  wiki/sources/arxiv-2610.08761-verifine-2026-10-07.md \
  wiki/sources/arxiv-2610.08768-slow-fictitious-play-2026-10-07.md \
  wiki/sources/substack-rss-latent-space-2026-10-07-quasi-riemann-openai-math.md \
  wiki/sources/substack-rss-pragmatic-engineer-2026-10-06-state-of-tech-2026.md \
  wiki/sources/substack-rss-event-horizon-2026-10-07-kalshi-election-push.md \
  wiki/sources/substack-rss-klement-2026-10-07-ai-labs-profit.md \
  wiki/sources/substack-rss-klement-2026-10-07-europe-war-readiness.md \
  wiki/sources/substack-rss-secpro-2026-10-07-cyber-ai-newsletter.md \
  wiki/sources/substack-rss-wublock-2026-10-07-september-mining.md \
  wiki/concepts/k284-eval-wave.md \
  wiki/concepts/k284-arxiv-wave.md \
  wiki/concepts/k284-feeds-wave.md \
  wiki/entities/tools/strata.md \
  wiki/entities/tools/artcraft-suite.md \
  wiki/entities/tools/treg.md \
  wiki/entities/tools/monid.md \
  wiki/entities/tools/bluffjax.md \
  wiki/entities/tools/refero-styles.md \
  wiki/entities/tools/21st-dev.md \
  briefs/2026-10-07_k284-atto-document-pipeline.md \
  briefs/2026-10-07_k284-strata-local-inference.md \
  briefs/2026-10-07_k284-ccc-design-registries.md \
  briefs/2026-10-07_k284-guruwatcher-monid.md \
  briefs/2026-10-07_k284-pm-cftc-crypto.md \
  briefs/2026-10-07_k284-basgiath-clips.md
 do test -f "$f" || { echo "MISSING $f"; exit 1; }; done
grep -q "pingdotgg/ts-rust" wiki/sources/eval-developer-resource-2026-10-07.md
grep -q "NOASSERTION" wiki/entities/tools/treg.md
grep -q "OSINT K284" wiki/index.md
grep -q "K284" wiki/log.md
grep -q "K284" ROADMAP.md
echo "0 product Integrate GO. FILE and HITL only. No install."
echo "=== DONE ==="
