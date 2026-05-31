#!/usr/bin/env bash
# SkillSpector static supply-chain scan wrapper (K88 Phase-0).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

if [[ -x "$ROOT/.local/skillspector-venv/bin/skillspector" ]]; then
  export SKILLSPECTOR_BIN="$ROOT/.local/skillspector-venv/bin/skillspector"
fi

exec python3 scripts/skill_supply_scan.py "$@"
