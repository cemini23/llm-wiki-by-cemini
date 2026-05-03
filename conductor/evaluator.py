"""Meta-Router style evaluation framework.

Tier 1: LLM-as-judge (95% of evaluations) — cheap, automated.
Tier 2: Gold-standard calibration (5%) — corrects judge bias via CATE.

Evaluates: correctness, routing_quality, cost_efficiency, tool_appropriateness.
"""

from __future__ import annotations

import json
import logging
import re
from typing import Any

from conductor.api import DeepSeekClient
from conductor.models import EvalReport, EvalScores

logger = logging.getLogger(__name__)


def _extract_json(text: str) -> str:
    match = re.search(r"\{[^{}]*\}", text, re.DOTALL)
    return match.group(0) if match else text


class RoutingEvaluator:
    """LLM-as-judge evaluation with periodic gold-standard calibration."""

    def __init__(self, config: dict[str, Any], api: DeepSeekClient) -> None:
        self.api = api
        eval_cfg = config.get("evaluation", {})
        self.judge_model = eval_cfg.get("judge_model", "deepseek-chat")
        self.gold_ratio = float(eval_cfg.get("gold_standard_ratio", 0.05))
        self.dimensions: list[str] = eval_cfg.get("dimensions", [
            "correctness", "routing_quality", "cost_efficiency", "tool_appropriateness",
        ])
        self.thresholds: dict[str, float] = eval_cfg.get("thresholds", {})

    # -- tier 1: LLM-as-judge -----------------------------------------------

    def evaluate_decision(self, decision: dict[str, Any]) -> EvalScores:
        """Score a single routing decision using LLM-as-judge."""
        prompt = self._build_eval_prompt(decision)
        try:
            raw, _ = self.api.classify_json(
                prompt,
                model=self.judge_model,
                system="You are a routing quality evaluator. Output JSON only. Be honest.",
            )
            return self._parse_scores(raw)
        except Exception as exc:
            logger.warning("Evaluation failed: %s", exc)
            return EvalScores(
                correctness=0.5, routing_quality=0.5,
                cost_efficiency=0.5, tool_appropriateness=0.5,
                reasoning=f"Eval error: {exc}",
            )

    def _build_eval_prompt(self, d: dict[str, Any]) -> str:
        query = d.get("query", d.get("query_text", ""))
        taxonomy = d.get("taxonomy_class", d.get("taxonomy", {}).get("name", "unknown"))
        model = d.get("final_model", "unknown")
        path = d.get("cascade_path", [])
        tools = d.get("tool_calls", [])
        cost = d.get("cost_estimate", 0.0)
        outcome = d.get("outcome", "unknown")

        return (
            "Evaluate this routing decision:\n\n"
            f"Query: {query}\n"
            f"Taxonomy class: {taxonomy}\n"
            f"Model used: {model}\n"
            f"Cascade path: {path}\n"
            f"Outcome: {outcome}\n"
            f"Tools invoked: {tools}\n"
            f"Estimated cost: ${cost:.6f}\n\n"
            "Score each dimension 0.0-1.0:\n"
            "1. correctness: Was the taxonomy classification appropriate for this query?\n"
            "2. routing_quality: Was the right model chosen? Could a cheaper model have worked?\n"
            "3. cost_efficiency: Was this the most cost-effective path to a correct answer?\n"
            "4. tool_appropriateness: Were the right tools invoked for this query type?\n\n"
            'Output JSON: {"correctness": float, "routing_quality": float, '
            '"cost_efficiency": float, "tool_appropriateness": float, '
            '"reasoning": "<one sentence>"}'
        )

    def _parse_scores(self, raw: str) -> EvalScores:
        try:
            obj = json.loads(_extract_json(raw))
        except json.JSONDecodeError:
            return EvalScores(0.5, 0.5, 0.5, 0.5, "JSON parse failure")

        def _clamp(key: str) -> float:
            return max(0.0, min(1.0, float(obj.get(key, 0.5))))

        return EvalScores(
            correctness=_clamp("correctness"),
            routing_quality=_clamp("routing_quality"),
            cost_efficiency=_clamp("cost_efficiency"),
            tool_appropriateness=_clamp("tool_appropriateness"),
            reasoning=str(obj.get("reasoning", "")),
        )

    # -- tier 2: gold-standard calibration -----------------------------------

    def calibrate_judge(
        self, gold_labels: list[dict[str, Any]]
    ) -> dict[str, float]:
        """Compare judge scores against gold-standard labels. Compute bias correction.

        Each gold label: {"decision": {...}, "gold_scores": {"correctness": 0.9, ...}}
        Returns per-dimension bias correction factors (CATE from Meta-Router).
        """
        corrections: dict[str, list[float]] = {d: [] for d in self.dimensions}
        for item in gold_labels:
            decision = item["decision"]
            gold = item["gold_scores"]
            judge = self.evaluate_decision(decision)
            for dim in self.dimensions:
                judge_val = getattr(judge, dim, 0.5)
                gold_val = float(gold.get(dim, 0.5))
                corrections[dim].append(gold_val - judge_val)

        bias: dict[str, float] = {}
        for dim, deltas in corrections.items():
            if deltas:
                bias[dim] = round(sum(deltas) / len(deltas), 4)
            else:
                bias[dim] = 0.0
        return bias

    # -- report generation ---------------------------------------------------

    def build_report(
        self,
        scores: list[EvalScores],
        decisions: list[dict[str, Any]] | None = None,
        bias_correction: dict[str, float] | None = None,
    ) -> EvalReport | None:
        """Build an evaluation report from a batch of scored decisions."""
        if not scores:
            return None

        n = len(scores)
        dims = self.dimensions

        means: dict[str, dict[str, float]] = {}
        for dim in dims:
            vals = [getattr(s, dim, 0.5) for s in scores]
            mean = sum(vals) / len(vals)
            variance = sum((v - mean) ** 2 for v in vals) / len(vals)
            means[dim] = {"mean": round(mean, 3), "std": round(variance ** 0.5, 3)}

        decisions_list = decisions or []
        escalation_count = sum(
            1 for d in decisions_list if d.get("outcome") == "escalated"
        )
        escalation_rate = escalation_count / n if n > 0 else 0.0

        total_cost = sum(
            float(d.get("cost_estimate", 0.0)) for d in decisions_list
        )
        avg_cost = total_cost / n if n > 0 else 0.0

        # Baseline: always reasoner
        baseline_cost = 0.00219  # deepseek-reasoner avg cost per query
        cost_savings = (1 - avg_cost / baseline_cost) * 100 if baseline_cost > 0 else 0.0

        gold_n = max(1, int(n * self.gold_ratio))

        return EvalReport(
            period_start=(
                decisions_list[0].get("timestamp", "") if decisions_list else ""
            ),
            period_end=(
                decisions_list[-1].get("timestamp", "") if decisions_list else ""
            ),
            total_decisions=n,
            evaluated=n,
            gold_standard_sample=gold_n,
            scores=means,
            judge_bias_correction=bias_correction or {},
            escalation_rate=round(escalation_rate, 3),
            avg_cost_per_query=round(avg_cost, 6),
            baseline_cost_per_query=baseline_cost,
            cost_savings_pct=round(cost_savings, 1),
        )
