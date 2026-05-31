#!/usr/bin/env bash
# Install NVIDIA SkillSpector into .local/skillspector-venv (Phase-0 K88).
# Requires Python 3.12+ (skillspector pyproject constraint).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
VENV="$ROOT/.local/skillspector-venv"
SRC="$ROOT/.local/skillspector-src"
REF="${SKILLSPECTOR_REF:-main}"
REPO_URL="${SKILLSPECTOR_REPO:-https://github.com/nvidia/skillspector}"

pick_python() {
  if command -v python3.12 >/dev/null 2>&1; then
    echo python3.12
  elif python3 -c 'import sys; raise SystemExit(0 if sys.version_info >= (3, 12) else 1)' 2>/dev/null; then
    echo python3
  else
    echo "ERROR: Python 3.12+ required for SkillSpector (skillspector requires-python >=3.12)." >&2
    exit 1
  fi
}

PY="$(pick_python)"
echo "Using: $($PY --version 2>&1)"

if [[ ! -d "$SRC/.git" ]]; then
  echo "Cloning $REPO_URL (ref=$REF) → $SRC"
  git clone --depth 1 --branch "$REF" "$REPO_URL" "$SRC"
else
  echo "Source present: $SRC (set SKILLSPECTOR_REF + rm -rf .local/skillspector-src to re-pin)"
fi

if [[ ! -d "$VENV" ]]; then
  "$PY" -m venv "$VENV"
fi

"$VENV/bin/pip" install -q --upgrade pip
"$VENV/bin/pip" install -q -e "$SRC"

echo ""
echo "Installed: $VENV/bin/skillspector"
"$VENV/bin/skillspector" scan --help | head -5
echo ""
echo "Run: python3 scripts/skill_supply_scan.py --repo-skills"
