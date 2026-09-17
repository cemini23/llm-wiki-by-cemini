# Product + CSV rules

## Atto

- Site `https://youratto.com` (never atto.com).
- Local-first Italian civil-record packet organizer. Not a law firm. Not legal advice. Not eligibility.
- Kit ~$299 pay once. Complements counsel. Sign `Claudio Barone` then `youratto.com`.
- 4–7 short sentences. One fact from `site_detail` only.
- Every body (including form rows) must contain this exact URL on its own line, above the signature: `https://youratto.com/?utm_source=email&utm_medium=outreach&utm_campaign=atto`

## GuruWatcher

- Site `https://guruwatcher.com`.
- Self-hosted Discord buzzer for newsletter price/level claims. ~$99. BYO Gmail folder + webhook.
- Alert-only. No orders. No republishing paid text. Do not ask them to forward paid issues. Do not scrape their list.
- Sign `Claudio Barone` then `guruwatcher.com`.
- 4–7 short sentences. One fact from `detail` only.
- Every body (including form rows) must contain this exact URL on its own line, above the signature: `https://guruwatcher.com/?utm_source=email&utm_medium=outreach&utm_campaign=gw`

## Gate (scripts/gate.py)

Fails a **sendable** row if any:

- `contact` / `public_email` is an email AND body lacks the campaign domain
- sendable body lacks the campaign tracked URL (`utm_source=email&utm_medium=outreach&utm_campaign=atto` or `…=gw`)
- `atto.com` as a domain (`youratto.com` allowed)
- phrases: legal advice, I am an attorney, you qualify, forward (your) paid, scrape your list, place orders
- missing `Claudio Barone`
- duplicate body vs another sendable row in the same file
- address already in send-log or suppress.json

Form rows (URL, no email) must be `status=form` and are not sent.

## From

| Campaign | From |
|----------|------|
| atto | Claudio Barone `<claudio@youratto.com>` |
| gw | Claudio Barone `<claudio@guruwatcher.com>` |
