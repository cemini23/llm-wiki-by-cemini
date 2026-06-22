#!/usr/bin/env bash
# K126 Kuhn poker SFT reference analysis (reference-only, offline by default).
#
# Builds a summary report from local fixtures using the Worker A reference
# module and writes reports/kuhn-sft-reference/summary.json.
# Optional --live flag augments the summary with one datasets-server row per
# Hugging Face dataset for manual inspection.
#
# Usage:
#   ./scripts/run_kuhn_sft_reference_analysis.sh
#   ./scripts/run_kuhn_sft_reference_analysis.sh --live
set -euo pipefail
cd "$(dirname "$0")/.."

LIVE=0
EXTRA_ARGS=()

while [[ $# -gt 0 ]]; do
  case "$1" in
    --live)
      LIVE=1
      shift
      ;;
    *)
      EXTRA_ARGS+=("$1")
      shift
      ;;
  esac
done

if [[ ${#EXTRA_ARGS[@]} -gt 0 ]]; then
  echo "Unknown args: ${EXTRA_ARGS[*]}" >&2
  exit 2
fi

mkdir -p reports/kuhn-sft-reference

echo "==> Kuhn SFT reference analysis"
if [[ "$LIVE" == "1" ]]; then
  echo "==> Live mode enabled (datasets-server first-row preview)"
fi

UV_LIVE_FLAG="$LIVE" uv run python -c '
from __future__ import annotations

import json
import os
import sys
import urllib.parse
import urllib.request
from pathlib import Path

REPO_ROOT = Path.cwd()
MODULE_PATH = REPO_ROOT / "examples" / "kuhn_sft_format_reference.py"
FIXTURE_PATH = REPO_ROOT / "tests" / "fixtures" / "kuhn_sft_samples.json"
OUTPUT_PATH = REPO_ROOT / "reports" / "kuhn-sft-reference" / "summary.json"
LIVE = os.environ.get("UV_LIVE_FLAG") == "1"

if not MODULE_PATH.exists():
    raise SystemExit(
        "Missing Worker A module: examples/kuhn_sft_format_reference.py"
    )
if not FIXTURE_PATH.exists():
    raise SystemExit(
        "Missing Worker A fixture: tests/fixtures/kuhn_sft_samples.json"
    )

sys.path.insert(0, str(REPO_ROOT / "examples"))
import kuhn_sft_format_reference as ref  # type: ignore


def _fetch_json(url: str) -> dict:
    with urllib.request.urlopen(url, timeout=20) as response:
        return json.loads(response.read().decode("utf-8"))


def _fetch_first_row(dataset_id: str) -> dict:
    encoded = urllib.parse.quote(dataset_id, safe="")
    splits_url = (
        "https://datasets-server.huggingface.co/splits?dataset=" + encoded
    )
    splits_payload = _fetch_json(splits_url)
    splits = splits_payload.get("splits") or []
    if not splits:
        return {"dataset": dataset_id, "error": "no splits returned"}
    first = splits[0]
    config = first.get("config")
    split = first.get("split")
    if not config or not split:
        return {
            "dataset": dataset_id,
            "error": "missing config/split in datasets-server response",
        }
    params = urllib.parse.urlencode(
        {"dataset": dataset_id, "config": config, "split": split, "length": 1}
    )
    rows_url = "https://datasets-server.huggingface.co/first-rows?" + params
    rows_payload = _fetch_json(rows_url)
    rows = rows_payload.get("rows") or []
    return {
        "dataset": dataset_id,
        "config": config,
        "split": split,
        "row_count": len(rows),
        "row": rows[0] if rows else None,
    }


with FIXTURE_PATH.open("r", encoding="utf-8") as handle:
    samples = json.load(handle)

report = ref.build_reference_report(samples)
if not isinstance(report, dict):
    raise SystemExit("build_reference_report(samples) did not return a dict")

report["report_kind"] = "kuhn_sft_reference"
report["source"] = "fixtures"
report["fixture_path"] = str(FIXTURE_PATH.relative_to(REPO_ROOT))
report["module_path"] = str(MODULE_PATH.relative_to(REPO_ROOT))

if LIVE:
    datasets = getattr(ref, "KUHN_SFT_DATASETS", [])
    live_preview = []
    for dataset in datasets:
        if isinstance(dataset, dict):
            dataset_id = dataset.get("id")
        else:
            dataset_id = getattr(dataset, "id", None)
        if not dataset_id:
            live_preview.append({"error": "dataset entry missing id", "raw": str(dataset)})
            continue
        try:
            preview = _fetch_first_row(dataset_id)
            row = preview.get("row")
            if isinstance(row, dict) and isinstance(row.get("row"), dict):
                messages = row["row"].get("messages") or []
                for msg in messages:
                    if isinstance(msg, dict) and isinstance(msg.get("content"), str):
                        if len(msg["content"]) > 1200:
                            msg["content"] = msg["content"][:1200] + "…"
            live_preview.append(preview)
        except Exception as exc:  # noqa: BLE001
            live_preview.append({"dataset": dataset_id, "error": str(exc)})
    report["live_preview"] = live_preview

OUTPUT_PATH.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")

summary = {
    "dataset_count": report.get("dataset_count"),
    "steal_candidates": report.get("steal_candidates"),
    "live_preview_count": len(report.get("live_preview", [])) if LIVE else 0,
    "output": str(OUTPUT_PATH.relative_to(REPO_ROOT)),
}
print(json.dumps(summary, indent=2, sort_keys=True))
'

echo "Kuhn SFT reference summary written to reports/kuhn-sft-reference/summary.json"
