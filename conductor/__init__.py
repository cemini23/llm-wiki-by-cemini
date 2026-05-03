"""Cemini Conductor — lightweight multi-model orchestrator.

Path B (Token-Prior): API-only deployment, no model training required.
Routes analyst queries to the right model+tool combination, cascading
only when confidence is low. Optimized via Training-Free GRPO.
"""

__version__ = "0.1.0"
