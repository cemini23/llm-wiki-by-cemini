"""Stage 3 — Cascade router with confidence gate.

Tries models from the pool in cost order, escalating when a confidence
judge says the output is unreliable. Based on StR's multi-judge gating
and Meta-Router's evaluation framework.
"""

from __future__ import annotations

import json
import logging
import re
import time
from typing import Any

from conductor.api import DeepSeekClient
from conductor.models import ModelPool, Query, RoutingDecision, TaxonomyClass

logger = logging.getLogger(__name__)


def _extract_json(text: str) -> str:
    match = re.search(r"\{[^{}]*\}", text, re.DOTALL)
    return match.group(0) if match else text


class CascadeRouter:
    """Try cheapest model, judge output, escalate if needed."""

    def __init__(self, config: dict[str, Any], api: DeepSeekClient) -> None:
        self.api = api
        cascade_cfg = config["cascade"]
        self.confidence_threshold = float(cascade_cfg["confidence_threshold"])
        self.max_escalations = int(cascade_cfg["max_escalations"])
        judge_cfg = cascade_cfg.get("judge", {})
        self._tax_weight = float(judge_cfg.get("taxonomy_judge_weight", 0.6))
        self._gen_weight = float(judge_cfg.get("general_judge_weight", 0.4))
        self.token_prior = config.get("token_priors", {}).get("cascade_judge", "")

    def route(
        self,
        query: Query,
        pool: ModelPool,
    ) -> tuple[RoutingDecision, str, dict[str, Any]]:
        """Run the cascade: try models in order, escalate on low confidence.

        Returns (routing_decision, content, metadata) so the orchestrator
        can use the winning model's output without a redundant API call.
        """
        decision = RoutingDecision(
            query=query,
            taxonomy=TaxonomyClass(name=pool.taxonomy_class, confidence=0.0),
            selected_model=pool.models[0] if pool.models else pool.default_model,
            cascade_path=[],
            confidence_scores=[],
            final_model="",
            outcome="rejected",
        )

        models = pool.models[: self.max_escalations + 1]
        if not models:
            models = [pool.default_model]

        start = time.monotonic()
        last_content = ""
        last_meta: dict[str, Any] = {}

        for i, model in enumerate(models):
            decision.cascade_path.append(model)

            content, meta = self.api.complete(
                query.text,
                model=model,
                temperature=0.0,
            )
            last_content = content
            last_meta = meta

            # Skip judge for terminal model — nothing to escalate to
            is_terminal = i == len(models) - 1
            if is_terminal:
                decision.final_model = model
                decision.outcome = "accepted" if i == 0 else "escalated"
                decision.cost_estimate = float(meta.get("cost_usd", 0.0))
                decision.latency_ms = (time.monotonic() - start) * 1000
                decision.confidence_scores.append(1.0)  # implicit trust
                return decision, last_content, last_meta

            score = self.judge_confidence(query, content, decision.taxonomy)
            decision.confidence_scores.append(score)

            if score >= self.confidence_threshold:
                decision.final_model = model
                decision.outcome = "accepted" if i == 0 else "escalated"
                decision.cost_estimate = float(meta.get("cost_usd", 0.0))
                decision.latency_ms = (time.monotonic() - start) * 1000
                return decision, last_content, last_meta

        # All models failed confidence threshold — use the last one anyway
        decision.final_model = models[-1]
        decision.outcome = "escalated"
        decision.cost_estimate = float(last_meta.get("cost_usd", 0.0))
        decision.latency_ms = (time.monotonic() - start) * 1000
        return decision, last_content, last_meta

    # -- confidence judging --------------------------------------------------

    def judge_confidence(
        self, query: Query, response: str, taxonomy: TaxonomyClass
    ) -> float:
        """Multi-judge confidence: taxonomy-specific + general quality. Returns 0.0-1.0."""
        tax_score = self._judge_taxonomy(query, response, taxonomy)
        gen_score = self._judge_general(query, response)
        return round(self._tax_weight * tax_score + self._gen_weight * gen_score, 3)

    def _judge_taxonomy(
        self, query: Query, response: str, taxonomy: TaxonomyClass
    ) -> float:
        prompt = (
            f"The query was classified as '{taxonomy.name}'.\n\n"
            f"Query: {query.text}\n\n"
            f"Response: {response[:1500]}\n\n"
            "Does this response correctly and completely answer the query for this "
            "domain? Score from 0.0 (wrong/irrelevant) to 1.0 (perfect). "
            'Output JSON: {"score": <float>, "reasoning": "<one sentence>"}'
        )
        return self._judge_call(prompt)

    def _judge_general(self, query: Query, response: str) -> float:
        prompt = (
            f"Query: {query.text}\n\n"
            f"Response: {response[:1500]}\n\n"
            "Evaluate overall quality: is the response factually correct, coherent, "
            "and free of hallucination? Score from 0.0 to 1.0. "
            'Output JSON: {"score": <float>, "reasoning": "<one sentence>"}'
        )
        return self._judge_call(prompt)

    def _judge_call(self, prompt: str) -> float:
        try:
            raw, _ = self.api.classify_json(
                prompt,
                model="deepseek-chat",
                system="You are a response quality evaluator. Output JSON only.",
                token_prior=self.token_prior or None,
            )
            obj = json.loads(_extract_json(raw))
            return max(0.0, min(1.0, float(obj.get("score", 0.5))))
        except Exception as exc:
            logger.warning("Confidence judge failed: %s", exc)
            return 0.5  # neutral on judge failure
