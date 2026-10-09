#!/usr/bin/env bash
# OSINT K285 Phase-1 verify. Rapid-MLX CLI is installed. API licence field stays NOASSERTION.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"
echo "=== K285 Phase-1 verify ==="
python3 scripts/wire_ledger_check.py
test -f .cursor/rules/osint-phase1-adopt-wires.mdc
grep -q "OSINT K285" .cursor/rules/osint-phase1-adopt-wires.mdc
grep -q "Rapid-MLX" .cursor/rules/osint-phase1-adopt-wires.mdc
grep -q "REA" .cursor/rules/osint-phase1-adopt-wires.mdc
for f in \
  wiki/sources/eval-github-repository-revenue-2026-10-08.md \
  wiki/sources/substack-rss-moontower-2026-10-07-vibey-vs-discrete-trades.md \
  wiki/sources/newsletter-rss-latent-space-2026-10-07-cloud-native-harness.md \
  wiki/sources/newsletter-rss-pragmatic-engineer-2026-10-07-sam-newman-resilience.md \
  wiki/sources/arxiv-2610.09244-risk-averse-mp-mfg-2026-10-08.md \
  wiki/sources/arxiv-2610.09439-inscriptionocr-2026-10-08.md \
  wiki/sources/arxiv-2610.10276-patchbench-2026-10-08.md \
  wiki/sources/arxiv-2610.10332-task-progress-distillation-2026-10-08.md \
  wiki/sources/arxiv-2610.10345-sldr-2026-10-08.md \
  wiki/sources/arxiv-2610.10426-cotrace-2026-10-08.md \
  wiki/sources/arxiv-2610.10478-base-model-screening-2026-10-08.md \
  wiki/sources/arxiv-2610.10498-embodiedrsi-2026-10-08.md \
  wiki/concepts/k285-eval-wave.md \
  wiki/concepts/k285-arxiv-wave.md \
  wiki/concepts/k285-feeds-wave.md \
  wiki/entities/tools/rapid-mlx.md \
  wiki/entities/tools/rea.md \
  wiki/entities/tools/syntaqlite.md \
  briefs/2026-10-08_k285-atto-local-inference-lint.md \
  briefs/2026-10-08_k285-rea-background-agents.md \
  briefs/2026-10-08_k285-artcraft-clips.md \
  briefs/2026-10-08_k285-worldmonitor-canary.md \
  briefs/2026-10-08_k285-ccc-harness-resilience.md \
  briefs/2026-10-08_k285-ccc-harness-coevolution.md \
  briefs/2026-10-08_k285-cyber-model-repair.md
 do test -f "$f" || { echo "MISSING $f"; exit 1; }; done
grep -q "NOASSERTION" wiki/entities/tools/rapid-mlx.md
grep -q "OSINT K285" wiki/index.md
grep -q "K285" wiki/log.md
grep -q "K285" ROADMAP.md
echo "Rapid-MLX CLI installed (Apache-2.0 file). API field still NOASSERTION. No model pull."
echo "=== DONE ==="
