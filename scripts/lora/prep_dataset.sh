#!/bin/bash
# Convert photos to 1024-long-edge JPEG, strip EXIF, write kohya captions.
# Usage: prep_dataset.sh <src-dir> <out-dir> <trigger>
# The source directory is read-only: nothing in it is moved, renamed or deleted.

set -euo pipefail

usage() {
  echo "usage: $(basename "$0") <src-dir> <out-dir> <trigger>" >&2
  echo "  Converts HEIC/JPG/PNG to 1024px JPEG, strips EXIF," >&2
  echo "  and writes one .txt caption per image for kohya training." >&2
  exit 2
}

[ "$#" -eq 3 ] || usage

SRC=$1
OUT=$2
TRIGGER=$3

[ -n "$TRIGGER" ] || usage
[ -d "$SRC" ] || { echo "error: not a directory: $SRC" >&2; exit 1; }

SRC_ABS=$(cd "$SRC" && pwd -P)
mkdir -p "$OUT"
OUT_ABS=$(cd "$OUT" && pwd -P)

if [ "$SRC_ABS" = "$OUT_ABS" ]; then
  echo "error: output directory must differ from source directory" >&2
  exit 1
fi

LIST="$OUT_ABS/.prep_list.$$"
trap 'rm -f "$LIST"' EXIT

find "$SRC_ABS" -maxdepth 1 -type f \
  \( -iname '*.heic' -o -iname '*.jpg' -o -iname '*.jpeg' -o -iname '*.png' \) \
  -print | sort > "$LIST"

COUNT=$(wc -l < "$LIST" | tr -d ' ')

if [ "$COUNT" -eq 0 ]; then
  echo "error: no HEIC/JPG/PNG files found in $SRC_ABS" >&2
  exit 1
fi

if [ "$COUNT" -lt 5 ]; then
  echo "warn: only $COUNT image(s). Five is the practical floor for a usable LoRA." >&2
fi

if [ "$COUNT" -gt 40 ]; then
  echo "warn: $COUNT images. Past about 30, outfit bake-in rises faster than fidelity." >&2
fi

i=0
while IFS= read -r f; do
  i=$((i + 1))
  n=$(printf '%02d' "$i")
  base="img_$n"
  outjpg="$OUT_ABS/$base.jpg"

  if ! sips -Z 1024 -s format jpeg --out "$outjpg" "$f" >/dev/null 2>&1; then
    echo "error: sips could not convert: $f" >&2
    rm -f "$outjpg"
    exit 1
  fi

  # sips re-encodes, which drops the EXIF block. Verify rather than assume.
  if sips -g all "$outjpg" 2>/dev/null | grep -Eiq '(gps|serial|make|model|camera)'; then
    echo "warn: metadata may remain in $outjpg — check with: sips -g all \"$outjpg\"" >&2
  fi

  printf '%s\n' "$TRIGGER, a photo of $TRIGGER, [outfit: describe], [pose: describe], [background: describe], [lighting: describe]" \
    > "$OUT_ABS/$base.txt"
done < "$LIST"

echo "images processed: $COUNT"
echo "output directory: $OUT_ABS"
echo "captions that still need an edit:"
grep -l '\[' "$OUT_ABS"/*.txt 2>/dev/null || echo "  none"
