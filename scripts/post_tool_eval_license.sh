#!/usr/bin/env bash
# post_tool_eval_license.sh — gh api license batch for tool-eval drops (K84).
#
# Usage:
#   ./scripts/post_tool_eval_license.sh path/to/tool-eval.md
#   ./scripts/post_tool_eval_license.sh "research to be indexed/Tool Evaluation.docx"
#
# For docx: extracts text via extract_docx.py then runs license_spot_check.

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
INPUT="${1:-}"

if [[ -z "$INPUT" ]]; then
  echo "Usage: $0 <tool-eval.md|docx>" >&2
  exit 1
fi

if [[ ! -f "$INPUT" ]]; then
  echo "ERROR: file not found: $INPUT" >&2
  exit 1
fi

OUT="$ROOT/.local/reports/license-spot-check-$(date +%Y-%m-%d-%H%M).txt"
mkdir -p "$(dirname "$OUT")"

case "$INPUT" in
  *.docx)
    TMP=$(mktemp)
    python3 "$ROOT/scripts/extract_docx.py" "$INPUT" > "$TMP" 2>/dev/null || {
      echo "WARN: extract_docx failed — try manual md export" >&2
      exit 1
    }
    bash "$ROOT/scripts/license_spot_check.sh" "$TMP" | tee "$OUT"
    rm -f "$TMP"
    ;;
  *)
    bash "$ROOT/scripts/license_spot_check.sh" "$INPUT" | tee "$OUT"
    ;;
esac

echo "Saved: $OUT"
