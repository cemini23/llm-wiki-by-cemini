#!/usr/bin/env bash
# OSINT K255 Phase-1 — policy wires (FILE/KEEP; existing harness skills).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"

echo "=== K255 Phase-1 verify ==="
python3 scripts/wire_ledger_check.py
test -f .cursor/skills/safeevolve-harness-audit/SKILL.md && echo "OK safeevolve-harness-audit"
test -f .cursor/skills/harness-eval-gate/SKILL.md && echo "OK harness-eval-gate"
test -f .cursor/skills/step-gate/SKILL.md && echo "OK step-gate"

echo ""
echo "=== Wired surfaces (FILE — no new ledger rows) ==="
echo "OSINT: on-demand osint-phase1-adopt-wires.mdc §K255 harness extract"
echo "CCC:   safeevolve-harness-audit + hook-update awareness (existing skills)"
echo "Cyber: AI-SOC part III fold; CAPTCHA agentic — brief only"
echo "Gambling: EH NFL objectionable bets — awareness"
echo "0 Integrate GO runtime. No xsp/pm scp. No .cursor/skills auto-evolve."
echo "=== DONE ==="
