#!/usr/bin/env bash
# K92 adopt: isolated venv for rlcard poker sim (gambling-wiki research; not prod).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
VENV="$ROOT/.local/venv-gambling-research"
REQ="$ROOT/scripts/gambling_research_requirements.txt"

python3 -m venv "$VENV"
"$VENV/bin/pip" install -U pip wheel
"$VENV/bin/pip" install -r "$REQ"
"$VENV/bin/python" -c "import rlcard; print('rlcard', rlcard.__version__, 'OK at', '$VENV')"
