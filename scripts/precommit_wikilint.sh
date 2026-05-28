#!/usr/bin/env bash
# Pre-commit hook: wikilint entire wiki/ tree (requires `wikilint` on PATH).
set -euo pipefail
if ! command -v wikilint >/dev/null 2>&1; then
  echo "precommit_wikilint: install wikilint — pip install git+https://github.com/cemini23/wikilint.git"
  exit 1
fi
ROOT="$(git rev-parse --show-toplevel)"
cd "$ROOT"
wikilint wiki/ --strict
