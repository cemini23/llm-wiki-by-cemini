"""Path B calibration — logging and token-prior construction.

Log every routing decision to Stash. Periodically rebuild token priors
from accumulated data using RecursiveLink-inspired residual composition:

1. Residual alignment: prior = base + delta (not full rewrite)
2. Distribution-shift-only: only drifted stages get updated
3. Stage-attributed credit: each decision blames/credits a specific stage
4. Joint optimization: bottleneck analysis on failed routes

Training-Free GRPO: the token prior is a prefix string that biases
P(y|x) toward desired routing behavior without modifying model weights.
"""

from __future__ import annotations

import json
import logging
from typing import Any

from conductor.mcp_client import StashClient
from conductor.models import RoutingDecision
from conductor.recursive_priors import PRIOR_VERSION_KEY, ResidualPriorBuilder

logger = logging.getLogger(__name__)


class CalibrationLogger:
    """Log routing decisions and build token priors from accumulated data.

    Dual-store: Stash for semantic recall, local JSONL for structured analysis.
    Token priors are built via ResidualPriorBuilder — recursive composition
    that preserves stable knowledge in a base branch and captures distribution
    shifts in delta branches.
    """

    _LOG_PATH = "/opt/cemini/logs/routing.jsonl"

    def __init__(
        self,
        config: dict[str, Any],
        stash: StashClient,
        api=None,
    ) -> None:
        self._stash = stash
        self.config = config
        self._api = api
        self._priors = ResidualPriorBuilder(api) if api else None
        self._namespace = config.get("infrastructure", {}).get("stash", {}).get(
            "namespace", "/cemini/conductor"
        )

    # -- logging -------------------------------------------------------------

    def log(self, routing: RoutingDecision) -> None:
        """Store a routing decision to JSONL log + Stash (best-effort).

        Each record now includes alignment_score and prior_version for
        residual prior composition — the delta branch uses only recent,
        high-alignment decisions to capture distribution shifts.
        """
        if not routing.cascade_path:
            return

        # Compute alignment score if we have a prior builder
        alignment_score = None
        if self._priors:
            try:
                # Build a lightweight decision dict for scoring
                decision_snapshot = {
                    "query": routing.query.text,
                    "taxonomy_class": routing.taxonomy.name,
                    "taxonomy_confidence": routing.taxonomy.confidence,
                    "final_model": routing.final_model,
                    "cascade_path": routing.cascade_path,
                    "tool_calls": routing.tool_calls,
                    "outcome": routing.outcome,
                }
                alignment_score = self._priors.score_alignment(decision_snapshot)
            except Exception:
                pass

        # Get current prior version from config
        prior_version = 0
        tp = self.config.get("token_priors", {})
        for key in tp.values():
            if isinstance(key, str) and PRIOR_VERSION_KEY in key:
                import re
                m = re.search(rf"{PRIOR_VERSION_KEY}:(\d+)", key)
                if m and int(m.group(1)) > prior_version:
                    prior_version = int(m.group(1))
                break

        record = {
            "type": "routing_decision",
            "query": routing.query.text,
            "taxonomy_class": routing.taxonomy.name,
            "taxonomy_confidence": routing.taxonomy.confidence,
            "selected_model": routing.selected_model,
            "cascade_path": routing.cascade_path,
            "confidence_scores": routing.confidence_scores,
            "tool_calls": routing.tool_calls,
            "final_model": routing.final_model,
            "outcome": routing.outcome,
            "cost_estimate": routing.cost_estimate,
            "latency_ms": routing.latency_ms,
            "timestamp": routing.query.timestamp.isoformat(),
            "session_id": routing.query.session_id,
            "alignment_score": alignment_score,
            "prior_version": prior_version,
        }

        # Local JSONL — authoritative structured store
        try:
            import os as _os
            _os.makedirs(_os.path.dirname(self._LOG_PATH), exist_ok=True)
            with open(self._LOG_PATH, "a") as f:
                f.write(json.dumps(record) + "\n")
        except Exception as exc:
            logger.warning("Failed to write routing log: %s", exc)

        # Stash — semantic recall (best-effort)
        try:
            summary = (
                f"Query '{routing.query.text[:100]}' classified as "
                f"{routing.taxonomy.name}, routed to {routing.final_model}, "
                f"outcome={routing.outcome}, cost=${routing.cost_estimate:.6f}"
            )
            self._stash.store_episode(summary)
        except Exception as exc:
            logger.warning("Stash log failed: %s", exc)

    # -- token-prior construction --------------------------------------------

    def build_token_priors(self) -> dict[str, str]:
        """Rebuild token priors via ResidualPriorBuilder.

        First run: bootstrap from scratch (base branch only).
        Subsequent runs: extract base, compute delta from recent high-alignment
        decisions, compose as BASE + RESIDUAL DELTA v{N}.
        """
        if self._priors is None:
            logger.warning("No prior builder available (API not provided)")
            return {"taxonomy": "", "cascade_judge": "", "tool_routing": ""}

        decisions = self._load_log()
        if not decisions:
            logger.warning("No calibration data found in %s", self._LOG_PATH)
            return {"taxonomy": "", "cascade_judge": "", "tool_routing": ""}

        # Annotate recent decisions with alignment scores if not already scored
        for d in decisions:
            if "alignment_score" not in d:
                try:
                    d["alignment_score"] = self._priors.score_alignment(d)
                except Exception:
                    d["alignment_score"] = 0.5

        previous = self.config.get("token_priors", {})
        priors = self._priors.build(decisions, previous)

        # Tag priors with version for tracking
        import re
        prior_version = 0
        for key in priors:
            versions = re.findall(r"v(\d+)", priors[key])
            for v in versions:
                prior_version = max(prior_version, int(v))

        # Store version in config for next build
        self.config.setdefault("_meta", {})["prior_version"] = prior_version
        logger.info(
            "Built token priors v%d from %d decisions (residual mode)",
            prior_version, len(decisions),
        )

        return priors

    def _load_log(self) -> list[dict[str, Any]]:
        decisions: list[dict[str, Any]] = []
        try:
            with open(self._LOG_PATH) as f:
                for line in f:
                    line = line.strip()
                    if line:
                        obj = json.loads(line)
                        if obj.get("type") == "routing_decision":
                            decisions.append(obj)
        except FileNotFoundError:
            pass
        return decisions

    # -- stage attribution (for bottleneck analysis) -------------------------

    def get_bottleneck_analysis(self) -> dict[str, Any]:
        """Analyze which pipeline stage is the primary failure bottleneck.

        Uses stage attribution from recursive_priors to identify where
        routing breaks down most often. Returns counts and percentages.
        """
        if self._priors is None:
            return {"error": "no prior builder"}

        decisions = self._load_log()
        if not decisions:
            return {"error": "no decisions"}

        attribution = self._priors.attribute_stages(decisions)
        total = len(decisions)

        analysis: dict[str, Any] = {"total": total, "stages": {}}
        for stage, stage_decisions in attribution.items():
            failures = sum(1 for d in stage_decisions if d.get("outcome") != "accepted")
            analysis["stages"][stage] = {
                "decisions": len(stage_decisions),
                "pct_total": round(len(stage_decisions) / total * 100, 1) if total else 0,
                "failures": failures,
                "failure_rate": round(failures / len(stage_decisions) * 100, 1) if stage_decisions else 0,
            }

        return analysis
