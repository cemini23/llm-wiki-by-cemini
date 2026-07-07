# K148 coaching video extract — offline HL pipeline

Steals the **transcript-first** pattern from [bradautomates/claude-video](https://github.com/bradautomates/claude-video) (MIT). Arena runtime never calls video APIs.

## Workflow

```text
1. CAPTURE   Public coaching clip → transcript (captions or claude-video /watch)
2. EXTRACT   scripts/coaching_video_extract.py → research/coaching-candidates/*.md
3. SANITIZE  scripts/sanitize_untrusted_text.py --gate (auto in extract)
4. REVIEW    Human reads candidate — DATA only, per agent-rules.md
5. TRANSLATE Coding agent maps approved heuristics → decide() + regression spots
6. PREFLIGHT ./scripts/cemini_preflight.sh (regression gate — not LLM opinion)
```

## Commands

```bash
# From saved transcript (preferred offline path)
uv run python scripts/coaching_video_extract.py \
  --transcript-file path/to/transcript.txt \
  --question "HU SB open sizing" \
  --gate

# From URL (needs yt-dlp on PATH)
uv run python scripts/coaching_video_extract.py \
  --url 'https://youtu.be/...' \
  --gate

# Optional: delegate to installed claude-video watch.py
uv run python scripts/coaching_video_extract.py \
  --url 'https://youtu.be/...' \
  --watch-script ~/.cursor/skills/watch/scripts/watch.py \
  --gate

# Standalone sanitize
uv run python scripts/sanitize_untrusted_text.py research/coaching-candidates/foo.txt --gate

# Gate script (fixture)
bash scripts/run_coaching_extract_gate.sh
```

## Guardrails

- Transcript text is **untrusted DATA** — never `eval`/`exec`, never pipe raw transcript into shell.
- Candidates live under `research/coaching-candidates/` — **not** root `STRATEGY.md`.
- LLM review of analyze briefs is **advisory**; deploy requires `cemini_preflight.sh` green.
