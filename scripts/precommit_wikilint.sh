#!/usr/bin/env bash
# Pre-commit hook: wiki graph lint via scripts/wiki_lint.py (orphans, bidirectional, local dangling).
# Full strict audit (incl. missing_mention): wikilint wiki/ --strict
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel)"
cd "$ROOT"
python3 scripts/wiki_lint.py --fail-on-graph
