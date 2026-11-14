---
title: "Provider-outage control verification"
type: concept
related:
  - sources/substack-rss-secpro-2026-11-13-the-microsoft-outrage-bumper-issue.md
  - concepts/soc-operations.md
  - concepts/incident-response.md
  - concepts/software-maintenance-institutional-insecurity.md
  - concepts/siem.md
updated: 2026-11-14
---

## Raw Concept

Question: **what must a SOC verify when a SaaS provider it depends on fails?** From Packt SecPro's analysis of the Microsoft 365 outage, 12–13 November 2026.

## Narrative

A SaaS outage is not only an availability incident. It is a period when security controls may be degraded, blind, or unable to act. The provider restores the service. The tenant must establish what its own controls actually did during the gap.

### Four steps between an event and a response

Every detection path has four steps. An outage can break any one of them, and each break has a different remedy.

| Step | Failure symptom | Remedy |
|---|---|---|
| Sensor generates the event | Endpoint silent | Check the agent, not the portal |
| Event reaches the service | Queue or connector stalled | Check the upstream route |
| Team can see it | Portal page or tab fails | Use a second data path |
| Response action applies | Action submitted, unconfirmed | Verify effect independently |

A blank portal proves a failure at step three only. It says nothing about steps one and two. This distinction prevents two errors: assuming detection was blind when it was not, and assuming containment ran when it did not.

### The measurement that matters: message receipt

"Message sent" is not "message received." This rule covers mail, alerts and tickets alike.

For every important event, record three times:

1. when the event happened,
2. when the provider ingested it,
3. when a person read it.

The gap between 1 and 3 is the time the team worked blind. A SIEM with a healthy collector and stale data reports green during that gap.

### Verification checklist for the next provider incident

- Send a harmless test message in both directions, internal and external, and confirm **receipt**.
- Confirm a test event reaches both the primary alert queue and the backup destination.
- Test device enrolment and the compliance status used for an access decision.
- Note the last known good time for each path, plus who will re-check it.
- Include shared inboxes and ticketing connectors, because they carry operational work.
- Test one action that policy should allow and one it should block.

### Continuity rules

1. Move incident command off the affected services. Publish the fallback through a channel that does not depend on the provider.
2. Use emergency administrator accounts only for their designed purpose, with a named operator and a use log.
3. Keep MFA, Conditional Access and data handling in force. For any exception, name an approver, limit scope, set an expiry, and confirm restoration.
4. Preserve records and timestamps in a restricted location while the console is degraded.

### Reconciliation after recovery

The outage leaves a working set that no dashboard shows: delayed messages, unconfirmed actions, and workarounds that moved data outside the normal path.

- Compare gateway records, provider traces and application logs. Classify each item as accepted, deferred, delivered or rejected.
- Match resubmitted requests against the originals before paying, releasing or replaying.
- Rerun the searches when indexing resumes. Reconcile them with independently collected evidence.
- Record copies that staff made to keep working. A document sent to a personal account is a different event from a delayed export.
- Close recovery only when priority controls and workflows are demonstrated, pending actions are accounted for, and each evidence gap has an owner.

### Rehearsal

Run the exercise with work mail unavailable and the security portal unreachable. The analyst receives a harmless alert, reaches the duty manager, retrieves the runbook, and records a containment decision on the fallback path. A second person confirms the decision. Measure the elapsed time.

If the first failure is that the analyst cannot find the duty manager's number without opening mail, the exercise has already paid for itself.

### Abuse during an outage

The realistic threat is opportunistic fraud, not a technical campaign. Outage-themed phishing rose during the July 2024 CrowdStrike incident. The defences are procedural: verify changed payment details through a number already known, and never share MFA codes with a caller who claims to be support.

## Snippets

> "It's quite possible for a portal to go blank while an endpoint keeps generating events." [Source: substack-rss-secpro-2026-11-13-the-microsoft-outrage-bumper-issue.md]

> "A SIEM that reads a delayed Microsoft feed can show a healthy collector and stale data at the same time." [Source: substack-rss-secpro-2026-11-13-the-microsoft-outrage-bumper-issue.md]

> "An alert generated at 18:00 can be processed, delivered and read at three quite different times." [Source: substack-rss-secpro-2026-11-13-the-microsoft-outrage-bumper-issue.md]
