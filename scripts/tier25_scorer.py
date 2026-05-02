#!/usr/bin/env python3
"""Tier 2.5 candidate scorer — applies the rubric from tier25_config.yaml.

Usage:
    python3 scripts/tier25_scorer.py --config scripts/tier25_config.yaml --candidates tmp/candidates.json

The scorer reads a JSON array of candidate papers (one per search hit) and
outputs a scored+ranked JSON array. It does NOT call Exa — the LLM or a
separate script handles search; this module only scores results.

Candidate JSON format (input):
    {
      "title": "Paper Title",
      "url": "https://arxiv.org/abs/2603.xxxxx",
      "cluster": "llm-agents",
      "snippet": "Exa highlight text...",
      "published_date": "2026-04-15",
      "authors": ["Author One", "Author Two"],
      "has_code": true,
      "license": "MIT",
      "source": "arxiv"
    }

Output format:
    {
      "candidates": [...scored and ranked...],
      "summary": {
        "total_hits": N,
        "passed_filters": N,
        "ingest_candidates": N (score >= quality_threshold_ingest),
        "strong_candidates": N (score >= quality_threshold_strong),
        "skipped": N
      }
    }
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

import yaml  # type: ignore


def load_config(config_path: str) -> dict:
    with open(config_path) as f:
        return yaml.safe_load(f)


def parse_date(d: str | None) -> datetime | None:
    if not d:
        return None
    for fmt in ("%Y-%m-%d", "%Y-%m-%dT%H:%M:%SZ"):
        try:
            return datetime.strptime(d, fmt)
        except ValueError:
            continue
    return None


# ---------------------------------------------------------------------------
# Hard filters
# ---------------------------------------------------------------------------

def check_recency(
    published_date: str | None,
    recency_window_days: int,
) -> tuple[bool, str]:
    if not published_date:
        return True, "no date — pass (can't check recency)"
    dt = parse_date(published_date)
    if dt is None:
        return True, "unparseable date — pass"
    cutoff = datetime.now() - timedelta(days=recency_window_days)
    if dt >= cutoff:
        return True, f"published {published_date} — within {recency_window_days}d window"
    return False, f"published {published_date} — outside {recency_window_days}d window"


def check_cemini_domain(
    cluster: str,
    snippet: str,
    title: str,
    cemini_clusters: list[str],
) -> tuple[bool, str]:
    # The cluster tag from the query tells us which Cemini domain it matched.
    # This is a first-pass signal; deeper domain check requires reading the
    # abstract/full text during the LLM scoring pass.
    if cluster in cemini_clusters:
        return True, f"cluster={cluster} matches Cemini domain"
    return False, f"cluster={cluster} not in Cemini domain list"


# ---------------------------------------------------------------------------
# Quality signal scoring (LLM-assisted — the script provides the framework)
# ---------------------------------------------------------------------------

def score_quality(candidate: dict, signals: list[dict]) -> dict:
    """Score quality signals from candidate metadata. Each signal marked
    as 'detected', 'not-detected', or 'needs-llm' (requires reading the
    paper abstract/full text to determine)."""
    scores: dict[str, str | None] = {}
    for sig in signals:
        sid = sig["id"]
        # Auto-detectable signals
        if sid == "code_release" and candidate.get("has_code"):
            scores[sid] = "detected"
        elif sid == "code_release":
            scores[sid] = "not-detected"
        # Everything else requires LLM reading of the abstract/full text
        else:
            scores[sid] = "needs-llm"
    return scores


# ---------------------------------------------------------------------------
# Negative signal check
# ---------------------------------------------------------------------------

def check_negative(candidate: dict, signals: list[dict]) -> list[dict]:
    hits = []
    license_str = (candidate.get("license") or "").upper()
    for sig in signals:
        sid = sig["id"]
        if sid == "license_poison" and any(
            p in license_str for p in ("GPL-3", "AGPL-3", "SSPL", "ELV2")
        ):
            hits.append({"signal": sid, "action": sig["action"], "detail": license_str})
        elif sid == "unauthorized_derivative" and "NOASSERTION" in license_str:
            hits.append({"signal": sid, "action": sig["action"], "detail": license_str})
        # Remaining negative signals require LLM reading
    return hits


# ---------------------------------------------------------------------------
# Main scoring pipeline
# ---------------------------------------------------------------------------

def score_candidates(
    candidates: list[dict],
    config: dict,
) -> dict:
    scoring = config["scoring"]
    loop_cfg = config["loop"]
    cemini_clusters = [q["cluster"] for q in config["queries"]]

    results = []
    skipped = []
    total = len(candidates)

    for cand in candidates:
        # Hard filter 2: recency
        passed_recency, recency_msg = check_recency(
            cand.get("published_date"), loop_cfg["recency_window_days"]
        )
        # Hard filter 3: Cemini domain
        passed_domain, domain_msg = check_cemini_domain(
            cand.get("cluster", ""), cand.get("snippet", ""), cand.get("title", ""),
            cemini_clusters,
        )

        # Hard filter 1: format — always passes at search-result stage
        # (Exa returns papers/docs; format check is LLM-driven on deep read)

        hard_filters = [
            ("format", True, "search-result — pass (LLM verifies on deep read)"),
            ("recency", passed_recency, recency_msg),
            ("cemini_domain", passed_domain, domain_msg),
        ]

        failed = [(fid, msg) for fid, ok, msg in hard_filters if not ok]

        if failed:
            skipped.append({
                "title": cand.get("title", "?"),
                "url": cand.get("url", ""),
                "cluster": cand.get("cluster", ""),
                "reasons": [f"{fid}: {msg}" for fid, msg in failed],
            })
            continue

        # Quality scoring (auto-detectable portion)
        qmap = {s["id"]: s for s in scoring["quality_signals"]}
        quality = score_quality(cand, scoring["quality_signals"])
        quality_detected = sum(
            qmap.get(sid, {}).get("weight", 1)
            for sid, status in quality.items()
            if status == "detected"
        )

        # Negative check (auto-detectable portion)
        negatives = check_negative(cand, scoring["negative_signals"])
        rejected = any(n["action"] == "reject" for n in negatives)

        if rejected:
            skipped.append({
                "title": cand.get("title", "?"),
                "url": cand.get("url", ""),
                "cluster": cand.get("cluster", ""),
                "reasons": [f"negative:{n['signal']}: {n['detail']}" for n in negatives],
            })
            continue

        results.append({
            "title": cand.get("title", "?"),
            "url": cand.get("url", ""),
            "cluster": cand.get("cluster", ""),
            "published": cand.get("published_date", ""),
            "authors": cand.get("authors", []),
            "snippet": cand.get("snippet", "")[:300],
            "auto_quality": quality,
            "auto_negatives": negatives,
            "auto_score": quality_detected,
            "needs_llm_review": any(
                v == "needs-llm" for v in quality.values()
            ),
        })

    # Sort by auto_score descending
    results.sort(key=lambda r: r["auto_score"], reverse=True)

    return {
        "candidates": results,
        "skipped": skipped,
        "summary": {
            "total_hits": total,
            "passed_filters": len(results),
            "needs_llm_review": sum(1 for r in results if r["needs_llm_review"]),
            "skipped": len(skipped),
            "threshold_ingest": scoring["quality_threshold_ingest"],
            "threshold_strong": scoring["quality_threshold_strong"],
        },
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Tier 2.5 candidate scorer — apply rubric to search hits"
    )
    parser.add_argument(
        "--config", default="scripts/tier25_config.yaml",
        help="Path to tier25_config.yaml"
    )
    parser.add_argument(
        "--candidates", required=True,
        help="Path to candidates JSON file (array of search hits)"
    )
    parser.add_argument(
        "--output", "-o",
        help="Output path for scored JSON (default: stdout)"
    )
    parser.add_argument(
        "--summary-only", action="store_true",
        help="Print summary only, not full candidate list"
    )
    args = parser.parse_args()

    config = load_config(args.config)

    with open(args.candidates) as f:
        candidates = json.load(f)

    scored = score_candidates(candidates, config)

    if args.summary_only:
        print(json.dumps(scored["summary"], indent=2))
    elif args.output:
        Path(args.output).parent.mkdir(parents=True, exist_ok=True)
        with open(args.output, "w") as f:
            json.dump(scored, f, indent=2, default=str)
        print(f"Scored {scored['summary']['total_hits']} candidates → {args.output}")
    else:
        print(json.dumps(scored, indent=2, default=str))


if __name__ == "__main__":
    main()
