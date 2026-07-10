#!/usr/bin/env bash
# build_reviewer_context.sh — compile K37 reviewer passive-injection bundle.
#
# Usage:
#   bash scripts/build_reviewer_context.sh
#
# Output: conductor/reviewer/corpus/context_bundle.md
# Manifest: conductor/reviewer/corpus/manifest.yaml

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
python3 "$ROOT/conductor/reviewer/corpus/build_context_bundle.py"
