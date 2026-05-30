#!/usr/bin/env bash
# license_spot_check.sh — gh api SPDX lookup for GitHub repo URLs (K84 workflow adoption).
#
# Post-run on tool-eval docx extracts or any file listing github.com/owner/repo URLs.
# Implements the manual step prescribed in @concepts/cemini-license-posture.md and
# @sources/tool-eval-50urls-polymarket-kalshi-license-false-negative-2026-05-21.md.
#
# Usage:
#   ./scripts/license_spot_check.sh path/to/eval.md
#   rg -o 'github\.com/[^/]+/[^/\s\)]+' brief.md | ./scripts/license_spot_check.sh -
#   echo 'https://github.com/ranaroussi/quantstats' | ./scripts/license_spot_check.sh -
#
# Requires: gh (authenticated), network.
# Exit: 0 always (informational); non-zero only if gh missing or no URLs found.

set -uo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
INPUT="${1:-}"

if ! command -v gh >/dev/null 2>&1; then
  echo "ERROR: gh CLI not found — install GitHub CLI and auth" >&2
  exit 1
fi

extract_urls() {
  if [[ -z "$INPUT" || "$INPUT" == "-" ]]; then
    cat
  elif [[ -f "$INPUT" ]]; then
    grep -Eo 'https?://github\.com/[^/[:space:])]+/[^/[:space:])]+' "$INPUT" \
      | sed 's/[).,;]*$//' || true
    grep -Eo 'github\.com/[^/[:space:])]+/[^/[:space:])]+' "$INPUT" \
      | sed 's/^/https:\/\//' | sed 's/[).,;]*$//' || true
  else
    echo "ERROR: not a file: $INPUT" >&2
    exit 1
  fi
}

normalize_repo() {
  local url="$1"
  url="${url%.git}"
  url="${url#https://github.com/}"
  url="${url#http://github.com/}"
  url="${url#github.com/}"
  echo "$url" | cut -d/ -f1-2
}

repos=$(
  extract_urls \
    | while read -r line; do
        [[ -z "$line" ]] && continue
        normalize_repo "$line"
      done \
    | sort -u
)

if [[ -z "$repos" ]]; then
  echo "No github.com/owner/repo URLs found" >&2
  exit 1
fi

printf "%-45s %s\n" "REPO" "SPDX"
printf "%-45s %s\n" "----" "----"

while IFS= read -r repo; do
  [[ -z "$repo" ]] && continue
  spdx=$(gh api "repos/${repo}" --jq '.license.spdx_id // "null"' 2>/dev/null || echo "ERROR")
  printf "%-45s %s\n" "$repo" "$spdx"
  sleep 0.15
done <<< "$repos"
