"""Path B calibration — logging and token-prior construction.

Log every routing decision to Stash. Periodically rebuild token priors
from accumulated data by identifying model/tool patterns that produced
high-confidence, low-cost outcomes.

Training-Free GRPO: the token prior is a prefix string that biases
P(y|x) toward desired routing behavior without modifying model weights.
"""

from __future__ import annotations

import json
import logging
from typing import Any

from conductor.mcp_client import StashClient
from conductor.models import RoutingDecision

logger = logging.getLogger(__name__)


class CalibrationLogger:
    """Log routing decisions and build token priors from accumulated data.

    Dual-store: Stash for semantic recall, local JSONL for structured analysis.
    Token priors are built from the JSONL log (Stash consolidation loses structure).
    """

    _LOG_PATH = "/opt/cemini/logs/routing.jsonl"

    def __init__(self, config: dict[str, Any], stash: StashClient) -> None:
        self._stash = stash
        self.config = config
        self._namespace = config.get("infrastructure", {}).get("stash", {}).get(
            "namespace", "/cemini/conductor"
        )

    # -- logging -------------------------------------------------------------

    def log(self, routing: RoutingDecision) -> None:
        """Store a routing decision to JSONL log + Stash (best-effort)."""
        if not routing.cascade_path:
            return

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
        """Rebuild token priors from the local JSONL routing log."""
        decisions = self._load_log()
        if not decisions:
            logger.warning("No calibration data found in %s", self._LOG_PATH)
            return {"taxonomy": "", "cascade_judge": "", "tool_routing": ""}

        return {
            "taxonomy": self._build_taxonomy_prior(decisions),
            "cascade_judge": self._build_cascade_prior(decisions),
            "tool_routing": self._build_tool_prior(decisions),
        }

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

    def _build_taxonomy_prior(self, decisions: list[dict[str, Any]]) -> str:
        """Build a taxonomy classification prior from historical patterns."""
        # Count classification frequency
        class_counts: dict[str, int] = {}
        class_avg_conf: dict[str, list[float]] = {}
        for d in decisions:
            tc = d.get("taxonomy_class", "general_question")
            class_counts[tc] = class_counts.get(tc, 0) + 1
            conf = d.get("taxonomy_confidence", 0.0)
            class_avg_conf.setdefault(tc, []).append(float(conf))

        if not class_counts:
            return ""

        # Top classes by frequency
        total = sum(class_counts.values())
        top = sorted(class_counts.items(), key=lambda x: -x[1])[:5]

        lines = [
            "[ROUTING PRIOR — built from calibration data]",
            f"Based on {total} historical queries, the most common query types are:",
        ]
        for cls, count in top:
            pct = count / total * 100
            avg_c = (
                sum(class_avg_conf.get(cls, [0])) / len(class_avg_conf.get(cls, [1]))
                if class_avg_conf.get(cls)
                else 0.0
            )
            lines.append(f"  {cls}: {count} queries ({pct:.0f}%, avg confidence {avg_c:.2f})")
        lines.append("Prefer the most specific applicable class. Default to ticker_lookup "
                      "for symbol queries, not general_question.")
        return " ".join(lines)

    def _build_cascade_prior(self, decisions: list[dict[str, Any]]) -> str:
        """Build a cascade confidence judge prior from escalation patterns."""
        if not decisions:
            return ""

        accepted = sum(1 for d in decisions if d.get("outcome") == "accepted")
        escalated = sum(1 for d in decisions if d.get("outcome") == "escalated")
        total = len(decisions)

        escalations = [d for d in decisions if d.get("outcome") == "escalated"]
        model_counts: dict[str, int] = {}
        for d in escalations:
            fm = d.get("final_model", "unknown")
            model_counts[fm] = model_counts.get(fm, 0) + 1

        return (
            f"[JUDGE PRIOR — built from {total} evaluations] "
            f"First model accepted {accepted}/{total} queries ({accepted/total*100:.0f}%). "
            f"When escalation was needed ({escalated} cases), final model distribution: "
            + ", ".join(f"{m}: {c}" for m, c in model_counts.items())
            + ". Prefer accepting responses that are factually grounded and cite sources. "
            "Be more strict for options_analysis and quantitative_methods queries."
        )

    def _build_tool_prior(self, decisions: list[dict[str, Any]]) -> str:
        """Build a tool routing prior from tool usage patterns."""
        if not decisions:
            return ""

        tool_benefit: dict[str, list[float]] = {}
        for d in decisions:
            tools = d.get("tool_calls", [])
            outcome = d.get("outcome", "")
            for t in tools:
                tool_benefit.setdefault(t, []).append(
                    1.0 if outcome == "accepted" else 0.5
                )

        lines = [
            "[TOOL PRIOR — built from calibration data]",
            "Tool effectiveness from historical routing:",
        ]
        for tool, scores in sorted(tool_benefit.items()):
            avg = sum(scores) / len(scores)
            lines.append(f"  {tool}: effectiveness {avg:.2f} ({len(scores)} uses)")
        lines.append("Use kb_search for factual lookups and ticker queries. "
                      "Use stash_recall for research synthesis and options analysis "
                      "where prior context helps.")
        return " ".join(lines)
