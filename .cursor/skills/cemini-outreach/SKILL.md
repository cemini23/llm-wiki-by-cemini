---
name: cemini-outreach
description: >-
  Automates Atto and GuruWatcher cold outreach: ingest scout CSVs, second-model
  human-voice rewrite, mechanical gate, then send from claudio@youratto.com or
  claudio@guruwatcher.com via Cloudflare Email Sending. Use when the operator
  says run outreach, process scout CSV, atto scout, guruwatcher scout, or drops
  a file in .local/outreach/inbox/. Multi-model plus gate replaces a human read
  of each body. Grok Bot.app scouts only — it must not send.
license: MIT
metadata.author: cemini23
metadata.version: "1.1.0"
disable-model-invocation: true
federation: false
---

# Cemini outreach (find → voice → send)

**Verifier (do not rewrite):** `scripts/gate.py` exit 0 on every row that will send. Then `scripts/send.py`. The second-model voice pass is the quality gate. Do **not** ask the operator to read bodies or confirm send after they invoked this skill.

Cap: **15 sends per invocation** unless the operator names a higher number.

## When this runs

Operator says **run outreach** / **process scout CSV** / **atto scout** / **guruwatcher scout**, or points at a CSV.

Grok Bot.app **does not** finish this loop. Local execution on the Bot is off. Bot writes a CSV; operator drops it in `.local/outreach/inbox/` (or pastes a path) and says run outreach. Do not wait for a chat ping of “I found more.”

## Data

All under `.local/outreach/` (gitignored):

| Path | Role |
|------|------|
| `inbox/*.csv` | Scout dumps |
| `suppress.json` | Never-send addresses |
| `send-log.json` | Already sent (dedupe) |
| `*.human.csv` | Voice-pass output |

Campaigns: **atto** (`claudio@youratto.com`) or **gw** (`claudio@guruwatcher.com`). Detect from columns (`site_detail` / `city` → atto; `newsletter` / `public_email` → gw) or filename (`atto-`, `gw-`).

## Workflow

1. **Collect CSV** — inbox, or a path the operator named. If empty and they asked to *find*, search public pages (Exa/web), write `inbox/<campaign>-<YYYYMMDD>.csv` with the schema in [reference.md](reference.md). Do not invent emails.
2. **Voice pass** — skip rows with `status=human|sent|form`. Otherwise dispatch **one** Task subagent:
   - atto → model `gpt-5.6-sol-medium`
   - gw → model `kimi-k3-max` (fallback `kimi-k3` if that slug is missing)
   Prompt: rewrite only `draft_subject` and `draft_body`; set `status=human`; keep other columns byte-stable. Product rules in [reference.md](reference.md). Write `*.human.csv`. Every body must include the campaign tracked URL from reference.md (own line above the signature).
3. **Gate** — run, do not eyeball:

```bash
python3 ".cursor/skills/cemini-outreach/scripts/gate.py" --csv "<human.csv>" --campaign atto
```

Exit ≠ 0 → fix failing rows or mark `status=fail`. Do not send fails.
4. **Send** — no extra confirmation:

```bash
python3 ".cursor/skills/cemini-outreach/scripts/send.py" --csv "<human.csv>" --campaign atto --max 15
```

5. **Report** — counts only: sent / form / skipped_dup / suppressed / fail. No body dump.
6. **Clicks** — after send (and when the operator asks if anyone clicked), query Cloudflare Web Analytics for pageviews whose URL contains `utm_source=email`. Atto vs GW is `utm_campaign=atto` / `utm_campaign=gw`. Also report Email Sending delivered vs failed. Do not invent open/click rates; these are text mails with one tracked URL, not a pixel.

## Grok Bot scout (copy into the Bot)

Keep Atto Scout and GuruWatcher Scout running. They find + first draft only.

```
When you have new leads, export a CSV (do not email anyone).
Atto columns: name,city,url,contact,site_detail,draft_subject,draft_body,status
GW columns: name,newsletter,URL,public_email,detail,draft_subject,draft_body,status
contact/public_email is a real email or a contact-form URL.
status=draft. One site-specific detail per row. No atto.com. No legal advice.
Stop at 15 new rows. Claudio drops the file in outreach inbox; Cursor sends.
```

Do **not** put Cloudflare / wrangler tokens on the Bot computer.

## Never

- From `cjbarone23@gmail.com` or `@atto.com`
- Send contact-form URLs
- Re-send an address already in `send-log.json` or `suppress.json`
- Vendor OpenOutreach (GPLv3) into Atto or this skill
- Ask the operator to approve each email after this skill was invoked
