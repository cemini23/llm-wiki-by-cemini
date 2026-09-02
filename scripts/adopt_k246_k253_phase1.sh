#!/usr/bin/env bash
# OSINT K246-K253 Phase-1 backlog verify (wired 2026-09-02).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

echo "=== K246-K253 Phase-1 verify ==="
test -f .cursor/rules/osint-k246-k253-phase1-wires.mdc
CCC="../Cemini claude code CCC"
CYBER="../Cybersecurity wiki"
GAMBLE="../Gambling wiki"
GW="../GuruWatcher"
test -f "$CCC/.cursor/rules/ccc-k246-k253-phase1-wires.mdc"
test -f "$CYBER/.cursor/rules/cyber-k246-k253-phase1-wires.mdc"
test -f "$GAMBLE/.cursor/rules/gambling-k246-k253-phase1-wires.mdc"
test -f "$GW/.cursor/rules/guruwatcher-k249-phase1-wires.mdc"
test -f "$GW/.cursor/rules/guruwatcher-k251-phase1-wires.mdc"
test -f "$GW/.cursor/rules/guruwatcher-k252-phase1-wires.mdc"
test -f "$GW/.cursor/rules/guruwatcher-k253-phase1-wires.mdc"
test -f "$GW/.cursor/rules/guruwatcher-k250-k253-phase1-wires.mdc"
python3 scripts/harness_eval_checklist.py selftest
python3 scripts/spdx_watch_k254_eval.py selftest

echo ""
echo "=== Wired surfaces ==="
echo "OSINT:     .cursor/rules/osint-k246-k253-phase1-wires.mdc (alwaysApply)"
echo "CCC:       .cursor/rules/ccc-k246-k253-phase1-wires.mdc"
echo "Cyber:     .cursor/rules/cyber-k246-k253-phase1-wires.mdc"
echo "Gambling:  .cursor/rules/gambling-k246-k253-phase1-wires.mdc"
echo "GW:        k246-k248 existing + k249/k251/k252/k253 + k250 canary fix"
echo "K254:      adopt_k254_phase1.sh"
echo "=== DONE ==="
