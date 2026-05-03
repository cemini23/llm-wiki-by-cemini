"""Stage 2 — Model pool selector.

Maps taxonomy class to an ordered list of candidate models (cheapest first).
For Path B, all models are DeepSeek API variants (chat vs reasoner).
"""

from __future__ import annotations

from typing import Any

from conductor.models import ModelPool, TaxonomyClass


class ModelPoolSelector:
    """Look up which models can handle a given taxonomy class."""

    def __init__(self, config: dict[str, Any]) -> None:
        raw = config["model_pool"]
        self._pool: dict[str, ModelPool] = {}
        for class_id, entry in raw.items():
            self._pool[class_id] = ModelPool(
                taxonomy_class=class_id,
                models=list(entry.get("models", [])),
                default_model=entry.get("default", ""),
            )
        self._default_pool = self._pool.get("general_question")

    def select(self, taxonomy: TaxonomyClass) -> ModelPool:
        """Return the model pool for a taxonomy class. Falls back to general_question."""
        pool = self._pool.get(taxonomy.name)
        if pool and pool.models:
            return pool
        if self._default_pool:
            return self._default_pool
        return ModelPool(
            taxonomy_class="general_question",
            models=["deepseek-chat"],
            default_model="deepseek-chat",
        )
