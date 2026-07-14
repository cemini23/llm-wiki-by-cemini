"""K163 message-DAG trace tests."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))

from message_dag_trace import (  # noqa: E402
    MessageDag,
    build_hl_failure_dag,
    estimate_naive_vs_dag_bytes,
)


def test_shared_message_stored_once():
    dag = MessageDag()
    mid_a = dag.add_message("fold trash", role="system")
    mid_b = dag.add_message("fold trash", role="system")
    assert mid_a == mid_b
    assert len(dag.messages) == 1
    n0 = dag.add_node([mid_a], layer="harness")
    n1 = dag.add_node([mid_b], parent_ids=[n0], layer="harness")
    hist = dag.materialize_node_history(n1)
    assert len(hist) == 2
    assert hist[0]["content"] == "fold trash"
    assert hist[1]["content"] == "fold trash"


def test_layer_split_and_roundtrip(tmp_path: Path):
    dag = MessageDag()
    m_task = dag.add_message("spot:R3", role="system")
    m_harn = dag.add_message("decide→fold", role="assistant")
    m_rt = dag.add_message("POST /action ok", role="tool")
    n0 = dag.add_node([m_task], layer="taskset")
    n1 = dag.add_node([m_harn], parent_ids=[n0], layer="harness")
    n2 = dag.add_node([m_rt], parent_ids=[n1], layer="runtime")
    path = tmp_path / "dag.json"
    dag.save(path)
    loaded = MessageDag.load(path)
    assert loaded.to_dict()["schema"] == "devfun.message_dag.v1"
    assert len(loaded.materialize_node_history(n2)) == 3
    assert json.loads(path.read_text())["nodes"][-1]["layer"] == "runtime"


def test_build_hl_failure_dag_linear_chain():
    turns = [
        {"role": "system", "content": "analyze BB bleed"},
        {"role": "user", "content": "worst: 99 BB -840"},
        {"role": "assistant", "content": "patch trash-fold"},
    ]
    dag = build_hl_failure_dag(turns)
    assert len(dag.nodes) == 3
    assert len(dag.messages) == 3
    sizes = estimate_naive_vs_dag_bytes(dag)
    assert sizes["dag_bytes"] > 0
    assert sizes["naive_full_history_bytes"] > 0


def test_dag_beats_naive_with_reuse_and_depth():
    """Repeated system prompt + deep chain → DAG smaller than naive copies."""
    dag = MessageDag()
    sys_id = dag.add_message("HL analyst rules " * 20, role="system")
    parent = None
    for i in range(12):
        mid = dag.add_message(f"turn-{i} analyze row", role="user")
        parent = dag.add_node(
            [sys_id, mid],
            parent_ids=[parent] if parent else [],
            layer="harness",
        )
    sizes = estimate_naive_vs_dag_bytes(dag)
    assert sizes["naive_full_history_bytes"] > sizes["dag_bytes"]
    assert len(dag.messages) == 13  # 1 system + 12 turns
