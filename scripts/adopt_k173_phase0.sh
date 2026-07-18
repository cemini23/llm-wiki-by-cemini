#!/usr/bin/env bash
# K173 Phase-0 local adopts — shallow clones only.
# Size posture (raised 2026-07-18): soft cap 2GB/clone, 8GB total under .local/adopts.
# Still skip PostHog monorepo (~5.7GB) and foundation model weights.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ADOPTS="${ROOT}/.local/adopts"
PER_CLONE_CAP_MB="${ADOPT_PER_CLONE_CAP_MB:-2048}"
mkdir -p "$ADOPTS"
cd "$ADOPTS"

clone_shallow() {
  local repo="$1"
  local dir="$2"
  if [[ -d "$dir/.git" ]]; then
    echo "exists: $dir"
    return 0
  fi
  echo "clone: $repo -> $dir"
  git clone --depth 1 --single-branch "https://github.com/${repo}.git" "$dir"
  du -sh "$dir"
  mb="$(du -sm "$dir" | awk '{print $1}')"
  if (( mb > PER_CLONE_CAP_MB )); then
    echo "FAIL: $dir is ${mb}MB > per-clone cap ${PER_CLONE_CAP_MB}MB" >&2
    exit 1
  fi
}

# Extract / Watch under size gate
clone_shallow "ibelick/ui-skills" "ui-skills"
clone_shallow "MoonshotAI/kimi-cli" "kimi-cli"
clone_shallow "lyogavin/airllm" "airllm"
clone_shallow "kvcache-ai/ktransformers" "ktransformers"
clone_shallow "antins-labs/SearchOS" "SearchOS"
clone_shallow "apache/ossie" "ossie"

# Explicitly NOT cloned (size or license):
# - PostHog/posthog (~5.7GB) — SaaS Integrate only
# - KnockOutEZ/wigolo — AGPL-3.0 Pass
# - elder-plinius/G0DM0D3 — AGPL-3.0 Watch
# - Moonshot Kimi K3 weights — Watch, no download

echo "=== K173 adopt sizes ==="
du -sh ui-skills kimi-cli airllm ktransformers SearchOS ossie 2>/dev/null || true
echo "OK adopt_k173_phase0"
