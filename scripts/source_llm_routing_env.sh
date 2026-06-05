#!/usr/bin/env bash
# Source Cemini LLM routing env (DeepSeek + OpenRouter fallback).
# Usage:  source scripts/source_llm_routing_env.sh
set -euo pipefail

_SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" && pwd)"
_REPO_ROOT="$(cd "$_SCRIPT_DIR/.." && pwd)"

_candidates=(
  "${CEMINI_LLM_ROUTING_ENV:-}"
  "$HOME/.cemini/llm-routing.env"
  "$_REPO_ROOT/.env"
  "$_REPO_ROOT/config/llm-routing.env"
)

_loaded=""
for _f in "${_candidates[@]}"; do
  [[ -n "$_f" && -f "$_f" ]] || continue
  # shellcheck disable=SC1090
  set -a
  source "$_f"
  set +a
  _loaded="$_f"
  break
done

if [[ -z "$_loaded" ]]; then
  echo "llm-routing: no env file found. Copy config/llm-routing.env.example to ~/.cemini/llm-routing.env" >&2
  return 1 2>/dev/null || exit 1
fi

# Wire world-cup-bot ADVISOR_* when unset (prefers OpenRouter when OR key present).
if [[ -z "${ADVISOR_BASE_URL:-}" ]] && [[ -n "${OPENROUTER_API_KEY:-}" ]]; then
  export ADVISOR_BASE_URL="${OPENROUTER_BASE_URL:-https://openrouter.ai/api/v1}"
  export ADVISOR_API_KEY="$OPENROUTER_API_KEY"
  export ADVISOR_MODEL="${LLM_FALLBACK_MODEL_ADVISOR:-google/gemini-2.5-flash}"
elif [[ -z "${ADVISOR_BASE_URL:-}" ]] && [[ -n "${DEEPSEEK_API_KEY:-}" ]]; then
  export ADVISOR_BASE_URL="${DEEPSEEK_BASE_URL:-https://api.deepseek.com/v1}"
  export ADVISOR_API_KEY="$DEEPSEEK_API_KEY"
  export ADVISOR_MODEL="${DEEPSEEK_MODEL:-deepseek-v4-flash}"
fi

echo "llm-routing: loaded $_loaded" >&2
