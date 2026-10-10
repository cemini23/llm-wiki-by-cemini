#!/usr/bin/env bash
# OSINT K288 Phase-1 verify. FILE and HITL only. 0 Integrate GO.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"
echo "=== K288 Phase-1 verify ==="
python3 scripts/wire_ledger_check.py
test -f .cursor/rules/osint-phase1-adopt-wires.mdc
grep -q "OSINT K288" .cursor/rules/osint-phase1-adopt-wires.mdc
grep -q "reachability layer is broken" .cursor/rules/osint-phase1-adopt-wires.mdc
grep -q "licence weight is lowered" .cursor/rules/osint-phase1-adopt-wires.mdc
for f in \
  wiki/sources/eval-dfs-betting-repositories-2026-10-10.md \
  wiki/sources/swarmer-sourced-dossier-2026-10-08.md \
  wiki/sources/swarmer-ratel-revenue-check-2026-10-08.md \
  wiki/sources/x-post-rubio-trade-framing-2026-10-08.md \
  wiki/sources/x-post-russia-escalation-2026-10-08.md \
  wiki/sources/arxiv-2610.11030-nomos-2026-10-10.md \
  wiki/sources/arxiv-2610.11669-co-speech-gesture-benchmark-2026-10-10.md \
  wiki/sources/substack-rss-latent-space-2026-10-10-typesafe-jev-100m-arr.md \
  wiki/sources/newsletter-rss-latent-space-2026-10-10-standard-bots-reliable-execution.md \
  wiki/sources/newsletter-rss-latent-space-2026-10-10-alphafold-bitter-lesson.md \
  wiki/sources/substack-rss-wublock-2026-10-10-weekly-project-updates.md \
  wiki/concepts/k288-eval-wave.md \
  wiki/concepts/k288-arxiv-wave.md \
  wiki/concepts/k288-feeds-wave.md \
  briefs/2026-10-10_k288-dfs-repositories.md \
  briefs/2026-10-10_k288-parlays-repositories.md \
  briefs/2026-10-10_k288-decision-models.md \
  briefs/2026-10-10_k288-nomos-toolcall-gates.md \
  briefs/2026-10-10_k288-polymarket-v2.md \
  briefs/2026-10-10_k288-gesture-eval.md
 do test -f "$f" || { echo "MISSING $f"; exit 1; }; done
grep -q "false negative" wiki/sources/eval-dfs-betting-repositories-2026-10-10.md
grep -q "AUDITED" wiki/sources/swarmer-ratel-revenue-check-2026-10-08.md
grep -q "OSINT K288" wiki/index.md
grep -q "K288" wiki/log.md
grep -q "K288" ROADMAP.md
echo "0 Integrate GO. FILE and HITL only. No install. No scrape. No auto-submit."
echo "=== DONE ==="
