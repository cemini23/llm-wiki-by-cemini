#!/usr/bin/env bash
# OSINT K254 Phase-1 — policy wires landed 2026-09-02 (operator GO implied by ingest directive).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

echo "=== K254 Phase-1 verify ==="
python3 scripts/harness_eval_checklist.py selftest
python3 scripts/spdx_watch_k254_eval.py selftest

echo ""
echo "=== Wired surfaces ==="
echo "OSINT:     .cursor/rules/osint-phase1-adopt-wires.mdc §K254"
echo "GuruWatcher: .cursor/rules/guruwatcher-k254-phase1-wires.mdc"
echo "CCC:       .cursor/rules/ccc-k254-phase1-wires.mdc"
echo "Cyber:     .cursor/rules/cyber-k254-phase1-wires.mdc"
echo "Gambling:  .cursor/rules/gambling-k254-phase1-wires.mdc"
echo "SEO:       .cursor/rules/cemini-phase1-seo-geo-wires.mdc §K254"
echo ""
echo "Helpers: harness_eval_checklist.py, spdx_watch_k254_eval.py"
echo "Skills (existing): harness-eval-gate, scout-tool-search, step-gate, env-harness-wrap"
echo "0 Integrate GO clones. No xsp/pm scp. No .cursor/skills auto-evolve."
echo "=== DONE ==="
