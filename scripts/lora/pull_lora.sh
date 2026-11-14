#!/bin/bash
# Copy trained LoRA checkpoints back from a RunPod pod.
# Usage: pull_lora.sh <ssh-target> <remote-dir> [<local-dir>]
#   ssh-target   e.g. root@1.2.3.4 -p 22022, or a host alias
#   remote-dir   e.g. /workspace/lora-out
#   local-dir    default ./lora-out

set -euo pipefail

if [ "$#" -lt 2 ] || [ "$#" -gt 3 ]; then
  echo "usage: $(basename "$0") <ssh-target> <remote-dir> [<local-dir>]" >&2
  exit 2
fi

TARGET=$1
REMOTE=$2
LOCAL=${3:-./lora-out}

mkdir -p "$LOCAL"

LIST=$(ssh "$TARGET" "ls -1 '$REMOTE'/*.safetensors 2>/dev/null" || true)

if [ -z "$LIST" ]; then
  echo "error: no .safetensors found in $REMOTE on $TARGET" >&2
  exit 1
fi

echo "found:"
printf '%s\n' "$LIST"

scp -r "$TARGET:$REMOTE/*.safetensors" "$LOCAL/"

for f in "$LOCAL"/*.safetensors; do
  [ -e "$f" ] || continue
  SIZE=$(wc -c < "$f" | tr -d ' ')
  if [ "$SIZE" -lt 50000000 ]; then
    echo "warn: $f is only $SIZE bytes — likely a truncated save, not a real LoRA" >&2
  fi
  echo "pulled: $f ($SIZE bytes)"
done

echo "reminder: terminate the pod, do not merely stop it."
