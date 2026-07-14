"""K163 message-DAG trace store — O(n) refs vs O(n²) full-history copies.

Prime Intellect verifiers v1 logging shape only. Do not install PI stack.
Pairs with K161 hierarchical memory caps.
"""
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable, Literal

Layer = Literal["taskset", "harness", "runtime"]
_VALID_LAYERS = frozenset({"taskset", "harness", "runtime"})


def _content_hash(role: str, content: str) -> str:
    digest = hashlib.sha256(f"{role}\n{content}".encode("utf-8")).hexdigest()
    return f"m_{digest[:16]}"


@dataclass
class MessageDag:
    """Store messages once; nodes reference message_ids + parent_ids."""

    schema: str = "devfun.message_dag.v1"
    messages: dict[str, dict[str, Any]] = field(default_factory=dict)
    nodes: list[dict[str, Any]] = field(default_factory=list)
    _node_index: dict[str, dict[str, Any]] = field(default_factory=dict, repr=False)

    def add_message(
        self,
        content: str,
        *,
        role: str = "user",
        message_id: str | None = None,
        meta: dict[str, Any] | None = None,
    ) -> str:
        mid = message_id or _content_hash(role, content)
        if mid not in self.messages:
            entry: dict[str, Any] = {"role": role, "content": content}
            if meta:
                entry["meta"] = meta
            self.messages[mid] = entry
        return mid

    def add_node(
        self,
        message_ids: Iterable[str],
        *,
        parent_ids: Iterable[str] | None = None,
        layer: Layer = "harness",
        node_id: str | None = None,
        meta: dict[str, Any] | None = None,
    ) -> str:
        if layer not in _VALID_LAYERS:
            raise ValueError(f"layer must be one of {sorted(_VALID_LAYERS)}")
        mids = list(message_ids)
        for mid in mids:
            if mid not in self.messages:
                raise KeyError(f"unknown message_id: {mid}")
        parents = list(parent_ids or [])
        for pid in parents:
            if pid not in self._node_index:
                raise KeyError(f"unknown parent node_id: {pid}")
        nid = node_id or f"n{len(self.nodes)}"
        if nid in self._node_index:
            raise ValueError(f"duplicate node_id: {nid}")
        node: dict[str, Any] = {
            "id": nid,
            "message_ids": mids,
            "parent_ids": parents,
            "layer": layer,
        }
        if meta:
            node["meta"] = meta
        self.nodes.append(node)
        self._node_index[nid] = node
        return nid

    def materialize_node_history(self, node_id: str) -> list[dict[str, Any]]:
        """Reconstruct message list along ancestor chain (oldest first)."""
        if node_id not in self._node_index:
            raise KeyError(f"unknown node_id: {node_id}")
        ordered_ids: list[str] = []
        seen: set[str] = set()

        def _walk(nid: str) -> None:
            if nid in seen:
                return
            seen.add(nid)
            node = self._node_index[nid]
            for pid in node.get("parent_ids") or []:
                _walk(pid)
            ordered_ids.append(nid)

        _walk(node_id)
        out: list[dict[str, Any]] = []
        for nid in ordered_ids:
            node = self._node_index[nid]
            for mid in node.get("message_ids") or []:
                msg = dict(self.messages[mid])
                msg["id"] = mid
                msg["node_id"] = nid
                out.append(msg)
        return out

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema": self.schema,
            "messages": self.messages,
            "nodes": self.nodes,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> MessageDag:
        dag = cls(schema=str(data.get("schema") or "devfun.message_dag.v1"))
        msgs = data.get("messages") or {}
        if not isinstance(msgs, dict):
            raise ValueError("messages must be an object")
        dag.messages = {str(k): dict(v) for k, v in msgs.items()}
        for node in data.get("nodes") or []:
            nid = str(node["id"])
            entry = {
                "id": nid,
                "message_ids": list(node.get("message_ids") or []),
                "parent_ids": list(node.get("parent_ids") or []),
                "layer": node.get("layer") or "harness",
            }
            if node.get("meta"):
                entry["meta"] = dict(node["meta"])
            dag.nodes.append(entry)
            dag._node_index[nid] = entry
        return dag

    def save(self, path: str | Path) -> Path:
        out = Path(path)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(self.to_dict(), indent=2) + "\n", encoding="utf-8")
        return out

    @classmethod
    def load(cls, path: str | Path) -> MessageDag:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise ValueError("DAG file must be a JSON object")
        return cls.from_dict(data)


def build_hl_failure_dag(
    turns: list[dict[str, Any]],
    *,
    layer: Layer = "harness",
) -> MessageDag:
    """Build a DAG from analyze/HL turn dicts.

    Each turn: {role?, content, parent_index?} where parent_index defaults to
    previous turn. Shared content is stored once (content-hash id).
    """
    dag = MessageDag()
    node_ids: list[str] = []
    for i, turn in enumerate(turns):
        role = str(turn.get("role") or "user")
        content = str(turn.get("content") or "")
        mid = dag.add_message(content, role=role, meta=turn.get("meta"))
        parent_ids: list[str] = []
        if "parent_index" in turn and turn["parent_index"] is not None:
            pi = int(turn["parent_index"])
            parent_ids = [node_ids[pi]]
        elif i > 0:
            parent_ids = [node_ids[i - 1]]
        nid = dag.add_node(
            [mid],
            parent_ids=parent_ids,
            layer=layer,
            meta={"turn": i, **({} if not turn.get("tag") else {"tag": turn["tag"]})},
        )
        node_ids.append(nid)
    return dag


def estimate_naive_vs_dag_bytes(dag: MessageDag) -> dict[str, int]:
    """Compare DAG size vs naive per-node full-history copies."""
    dag_bytes = len(json.dumps(dag.to_dict()).encode("utf-8"))
    naive = 0
    for node in dag.nodes:
        hist = dag.materialize_node_history(node["id"])
        naive += len(json.dumps(hist).encode("utf-8"))
    return {"dag_bytes": dag_bytes, "naive_full_history_bytes": naive}
