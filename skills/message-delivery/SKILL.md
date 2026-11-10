---
name: message-delivery
description: Work out why a message didn't reach the right person, or reached them late - when it was sent, to whom and how, who was on call at that time, and how they're set up to be reached. Use when someone says they never got a message, got it late, or the wrong person got it.
---

# Trace a message that didn't arrive

## 1. Find the message

- `search_messages` by caller, number or words in the message, or `list_messages` for
  the line and time window.
- `get_message_by_short_code` when the person has the link from a delivered message.
- Don't open it with `get_message` just to trace it: opening a message marks it read,
  which changes the record you're looking into. Work from the list and search results.

If several match, list them briefly and ask which one.

## 2. What happened to it

`list_message_activities` for its history: each delivery attempt, who it went to, how
(call, text, email), when, and whether it was read, picked up or acknowledged.
`list_message_notes` for anything the service or your team added.

## 3. Who should have been reached

1. `list_escalation_levels` for the line.
2. `list_calendar_events` around the message's time, once for each escalation level's
   id. Without the level id the calendar returns the first level only, and backup
   coverage goes missing from the answer.
3. `list_delivery_methods` for the person who was on call: the number, email and method
   on file.

## Report

Say plainly:
- whether it was sent, to whom, how and when, and whether anyone acknowledged it,
- whether that matches who was on call and how they're set up to be reached,
- the likely cause, for example nobody on the schedule, an old number, a method that was
  removed, or a delivery that was sent but never picked up.

Keep what the records show apart from what's likely, and give times in the line's time
zone.

## Fixing it

Offer the fix and use the skill that makes it: `oncall-changes` for the schedule,
`contact-delivery` for a number or method. If the records show the message went to the
right person the right way but never arrived, the answering service needs to look into
delivery: say so, rather than changing settings to test it.
