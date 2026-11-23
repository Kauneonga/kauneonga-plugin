---
name: message-triage
description: Review the messages an answering service took and separate what needs action now from what can wait, then act on them - acknowledge one or several, change status, add notes, read a message's history. Use when catching up on overnight or weekend messages, checking for anything urgent, or working through an unread queue.
---

# Triage answering service messages

Work from what the service actually recorded, not from assumptions about what a caller meant.

## Gather

Pull the window the user asked about with `list_messages` or `list_recent_messages`,
filtering by account when they name one. `search_messages` finds a specific caller or
subject across the retained window, and `get_message_by_short_code` finds one from the
link in a delivered message. Open a message in full with `get_message` only when the user
asks about that one: opening it marks it read.

Read before summarizing. Messages carry callers' personal details and whatever else they
chose to share. Minimize disclosure: report only what the user needs, and do not include
sensitive details in unnecessary tool calls or external messages.

## Sort

Group into three buckets and lead with the first:

**Needs action now:** anything flagged as an emergency, a caller reporting a
situation that gets worse with time, a second call from the same person, or a message whose
delivery has not been acknowledged past its escalation window.

**Needs a reply today:** routine callbacks, scheduling requests, questions with a named
person waiting.

**Informational:** confirmations, vendor calls, resolved items.

Within the first bucket, order by how long the caller has been waiting, not by arrival order.

## Report

Give a short prose summary first, then the urgent items individually with caller name,
what they need, and how long it has been open. Keep the rest as counts unless asked to expand.

Call out patterns worth acting on: repeat callers, a spike from one number, several
messages that should have paged someone but did not.

## Acting on messages

Say which message and what will change, wait for a yes, then read back the result. Act
only on the intended message and account. Never invent success.

| To | How |
|---|---|
| Mark one handled | `acknowledge_message`. It counts the message as picked up and stops it escalating to anyone else on call |
| Mark several handled | `acknowledge_messages`, up to 10 at a time, with one yes for the list. Say which messages first (who called, when). If it isn't in your tool list yet, use `acknowledge_message` for each one, after that same one yes |
| Change status | `update_message`. A message can't go back to new |
| Mark read or unread | `mark_message_read` or `mark_message_unread` |
| Add a message by hand, or a test message | `create_message`. It is delivered to whoever is on call, like a real message, so say that first |
| Follow up later: a text, email or call | `follow-ups` |

## Notes, history and recording

- **History:** `list_message_activities` shows each delivery, read, pickup and status
  change with its time. Present it as a timeline in the line's time zone.
- **Notes:** `list_message_notes` to read them, `create_message_note` to record work
  done, `delete_message_note` to remove one. Others on the account see notes, so show the
  exact text and get a yes before adding or deleting.
- **Recording:** `list_message_call_recording` gives the details of the call linked to a
  message: its time, the caller's number and the line, if the login has call recording
  access. It returns no audio and no transcript, so never offer to play, share or
  summarize the recording itself. Treat the details as sensitive and share only what was
  asked for.
