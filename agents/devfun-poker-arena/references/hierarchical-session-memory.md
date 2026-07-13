# Hierarchical session memory (K161)

Operator spec from arXiv **2607.07666** (Ensemble QSP hierarchical memory).
Config: `config/hu_hierarchical_memory.json`. Code: `examples/hierarchical_session_state.py`.

## Three tiers

| Tier | Contents | Cap |
|------|----------|-----|
| **Short-term** | Last N hand summaries + scratchpad facts (stack_bb, HUD tags) | `max_hands` / `max_scratchpad_facts` |
| **Mid-term** | Active goals, last 3 session summaries, recent jobs | Evict `status: completed` drills |
| **Long-term** | Strategy handbook / yardstick docs in `references/` | Doc pointers only — never inlined into decide |

## O(1) slice for decide / HL

`build_memory_slice_for_decide()` returns a **bounded** dict under `slice_max_chars`.
Lobby injects it as `research_context["hierarchical_memory_slice"]`.

**Never** dump:

- Full `selfplay_trajectory.jsonl` / Arena exports
- Raw `reasoning` blobs or full `action_history`
- Complete session transcripts

## Eviction

`evict_completed()` removes mid-term goals/jobs marked `completed` so token budget
stays ~O(1) across multi-hour lobby sessions. Competition scope change resets mid-term
(same pattern as `session_villain_memory` reset in `run_cemini_lobby.py`).

## Compose with existing villain memory

`session_memory.py` (villain aggression / showdown HUD) stays intact. Hierarchical
slice sits **alongside** `session_villain_memory` — do not replace exploit_from_memory.

## Advisory

`compute_hierarchical_memory_advisory()` echoes char budget — **not** a submit gate.

## Related

- `references/deepsearch-trajectory-filter.md` (K161 P1)
- `references/expert-yardstick-pool.md` (long-term)
- `briefs/2026-07-13_k161-hierarchical-memory-deepsearch-steal.md`
