---
name: message-triage
description: Review the messages an answering service took and separate what needs action now from what can wait. Use when catching up on overnight or weekend messages, checking for anything urgent, or working through an unread queue.
---

# Triage answering service messages

Work from what the service actually recorded, not from assumptions about what a caller meant.

## Gather

Pull the window the user asked about with `list_messages` or `list_recent_messages`,
filtering by account when they name one. `search_messages` finds a specific caller or
subject across the retained window.

Read before summarizing. Messages carry caller PII and, for medical practices, clinical
detail — keep both inside the summary you produce and do not restate more than the user needs.

## Sort

Group into three buckets and lead with the first:

**Needs action now** — anything flagged as an emergency, a caller reporting a symptom or
situation that escalates with time, a second call from the same person, or a message whose
delivery has not been acknowledged past its escalation window.

**Needs a reply today** — routine callbacks, scheduling requests, questions with a named
person waiting.

**Informational** — confirmations, vendor calls, resolved items.

Within the first bucket, order by how long the caller has been waiting, not by arrival order.

## Report

Give a short prose summary first, then the urgent items individually with caller name,
what they need, and how long it has been open. Keep the rest as counts unless asked to expand.

Call out patterns worth acting on: repeat callers, a spike from one number, several
messages that should have paged someone but did not.

## Acting on them

Use `create_message_note` to record work done. A customer with the appropriate
account access can use `create_to_do` or `delete_to_do` for follow-ups. Before
creating a task, verify its account, phone, schedule and recipients, and check
for existing tasks. A task can send real voice calls, email or SMS, so explain
that effect and obtain explicit confirmation.

When authorized, use `create_message`, `update_message`,
`mark_message_read`, `mark_message_unread`, `acknowledge_message`,
and `delete_message_note` for the intended message and account only.
Confirm consequential changes and read back the successful result.
Never invent success or create duplicate follow-ups.

Use `list_message_activities` when a message's history matters — who picked it up, when it
was read, whether it was delivered.
