#!/usr/bin/env bash
# Build the merged federation wiki (migration plan 5.2).
#
# Extends the osint repo: every sibling's `wiki/` tree moves to `wiki/<domain>/`,
# osint's own `wiki/` moves to `wiki/osint/`, and history is preserved in both cases.
#
# Writes ONLY to --out. No live repository is touched.
#
#   osint  -> TARGET mode: --path-rename alone, so scripts/, CLAUDE.md, ROADMAP.md
#             and briefs/ survive. Adding --path wiki/ here would delete them from
#             the tree AND the history (plan 5.2.2).
#   others -> SOURCE mode: --path wiki/ keeps only that wiki's tree.
#
# Usage: bash scripts/merge_build.sh [--out DIR] [--keep-scratch]

set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$HERE")"
MANIFEST="$HERE/wiki_merge_manifest.py"
PROJ="$HOME/Projects"

OUT="${TMPDIR:-/tmp}/cemini-wiki-build"
if [ "${1:-}" = "--out" ]; then
  OUT="$2"
fi

DOMAINS=(osint ccc cybersec seo image-gen gambling game-dev 3d-printing)

dir_for() {
  case "$1" in
    osint)       echo "$PROJ/OSINT WORKSPACE" ;;
    ccc)         echo "$PROJ/Cemini claude code CCC" ;;
    cybersec)    echo "$PROJ/Cybersecurity wiki" ;;
    seo)         echo "$PROJ/SEO:GEO B&M Business" ;;
    image-gen)   echo "$PROJ/Image gen" ;;
    gambling)    echo "$PROJ/Gambling wiki" ;;
    game-dev)    echo "$PROJ/Game Dev wiki" ;;
    3d-printing) echo "$PROJ/3d printing" ;;
  esac
}

if [ -e "$OUT" ]; then
  echo "refusing to overwrite existing $OUT" >&2
  exit 2
fi
mkdir -p "$OUT"

echo "=== 1. import OSINT as the target (keeps non-wiki content) ==="
MERGED="$OUT/target"
python3 -I "$MANIFEST" dryrun --repo "$(dir_for osint)" --domain osint --scratch "$MERGED" --target >/dev/null
echo "  target: $MERGED"
echo "  scripts/ files: $(find "$MERGED/scripts" -type f 2>/dev/null | wc -l | tr -d ' ')"
echo "  CLAUDE.md:      $([ -f "$MERGED/CLAUDE.md" ] && echo present || echo MISSING)"

echo
echo "=== 2. import each sibling (wiki/ only, renamed to wiki/<domain>/) ==="
for dom in "${DOMAINS[@]}"; do
  [ "$dom" = "osint" ] && continue
  src="$(dir_for "$dom")"
  tmp="$OUT/src-$dom"
  python3 -I "$MANIFEST" dryrun --repo "$src" --domain "$dom" --scratch "$tmp" >/dev/null
  echo "  $dom <- $(basename "$src")  ($(find "$tmp/wiki" -type f 2>/dev/null | wc -l | tr -d ' ') files)"
done

echo
echo "=== 3. merge each sibling into the target (unrelated histories) ==="
for dom in "${DOMAINS[@]}"; do
  [ "$dom" = "osint" ] && continue
  tmp="$OUT/src-$dom"
  branch="$(git -C "$tmp" rev-parse --abbrev-ref HEAD)"
  git -C "$MERGED" remote add "$dom" "$tmp" 2>/dev/null || true
  git -C "$MERGED" fetch -q "$dom"
  if git -C "$MERGED" merge -q --allow-unrelated-histories --no-edit "$dom/$branch" >/dev/null 2>&1; then
    echo "  merged $dom"
  else
    echo "  MERGE FAILED: $dom" >&2
    git -C "$MERGED" merge --abort 2>/dev/null || true
    exit 3
  fi
done

echo
echo "=== 4. result ==="
echo "  domains:  $(ls -d "$MERGED"/wiki/*/ 2>/dev/null | wc -l | tr -d ' ')"
echo "  wiki files: $(find "$MERGED/wiki" -type f | wc -l | tr -d ' ')"
echo "  commits:  $(git -C "$MERGED" rev-list --count HEAD)"
echo "  merged repo: $MERGED"
