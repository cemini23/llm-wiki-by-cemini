"""Stage 1 — Query taxonomy classifier.

Maps natural-language queries to one of ~10 predefined classes.
For Path B, uses a token-prior prefix constructed from calibration data.
"""

from __future__ import annotations

import json
import logging
import re
from typing import Any

from conductor.api import DeepSeekClient
from conductor.models import Query, TaxonomyClass

logger = logging.getLogger(__name__)


def _extract_json(text: str) -> str:
    """Extract the first JSON object from text that may contain markdown fences."""
    match = re.search(r"\{[^{}]*\}", text, re.DOTALL)
    return match.group(0) if match else text


class TaxonomyClassifier:
    """Classify analyst queries into the Cemini query taxonomy."""

    def __init__(self, config: dict[str, Any], api: DeepSeekClient) -> None:
        self.api = api
        tax_cfg = config["taxonomy"]
        self.classes: list[dict[str, Any]] = tax_cfg["classes"]
        self.fallback_id = "general_question"
        self.confidence_floor = 0.3  # below this → fallback
        self.token_prior = config.get("token_priors", {}).get("taxonomy", "")
        self._system_prompt = self._build_system_prompt()

    def classify(self, query: Query) -> TaxonomyClass:
        """Classify a query. Never raises — falls back to general_question."""
        prompt = self._build_user_prompt(query.text)
        try:
            raw, meta = self.api.classify_json(
                prompt,
                system=self._system_prompt,
                token_prior=self.token_prior or None,
            )
            return self._parse(raw)
        except Exception as exc:
            logger.warning("Taxonomy classification failed: %s", exc)
            return TaxonomyClass(
                name=self.fallback_id,
                confidence=0.0,
                reasoning=f"Classification error: {exc}",
            )

    # -- prompt construction -------------------------------------------------

    def _build_system_prompt(self) -> str:
        lines = [
            "You are a query taxonomy classifier for a financial research system.",
            "Classify the user's query into EXACTLY ONE of these categories:",
            "",
        ]
        for cls in self.classes:
            name = cls["id"]
            desc = cls.get("description", "")
            is_fb = cls.get("is_fallback", False)
            fb = " [FALLBACK — use only if no other class fits]" if is_fb else ""
            lines.append(f"- {name}: {desc}{fb}")
        lines.extend([
            "",
            "Output a JSON object with exactly these keys:",
            '  "class": "<one of the class IDs above>",',
            '  "confidence": <float 0.0-1.0>,',
            '  "reasoning": "<one sentence explaining the classification>"',
        ])
        return "\n".join(lines)

    def _build_user_prompt(self, text: str) -> str:
        return f"Classify this query:\n\n{text}"

    def _parse(self, raw: str) -> TaxonomyClass:
        valid_ids = {c["id"] for c in self.classes}
        try:
            obj = json.loads(_extract_json(raw))
        except json.JSONDecodeError:
            return TaxonomyClass(name=self.fallback_id, confidence=0.0,
                                 reasoning="Failed to parse classifier JSON output")

        class_id = obj.get("class", self.fallback_id)
        confidence = float(obj.get("confidence", 0.0))
        reasoning = str(obj.get("reasoning", ""))

        if class_id not in valid_ids:
            class_id = self.fallback_id
            confidence = min(confidence, 0.2)

        if confidence < self.confidence_floor:
            return TaxonomyClass(
                name=self.fallback_id,
                confidence=confidence,
                reasoning=f"Below confidence floor ({self.confidence_floor}): {reasoning}",
            )

        return TaxonomyClass(name=class_id, confidence=confidence, reasoning=reasoning)
