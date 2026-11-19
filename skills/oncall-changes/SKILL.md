---
name: oncall-changes
description: Make day-to-day changes to who is on call - cover someone's time off, swap two shifts, add or move a shift, change a repeating shift, copy a week, or answer "who's on call tonight". Use when you want to change your on-call schedule or check who is covering.
---

# Change the on-call schedule

This skill covers everyday on-call shifts and escalation-level management
where a customer's membership grants Calendar Management access. Changes to
escalation timing or level order can affect real calls. Show the current
configuration, explain the impact, obtain confirmation, and verify the result.

## Who's on call

1. Find the line. If the account has several, ask which one.
2. `list_escalation_levels` for the line, then `list_calendar_events` with the line's
   phone and a start and end around the time asked about. Pass each escalation level's id
   in turn: without it the calendar returns the first level only, so backup coverage goes
   missing from the answer.
3. Answer with names, levels and times in the line's time zone.

## Making a change

Always in this order:

1. **Reference data first.** `list_calendar_event_reference_data` for shifts and
   `list_calendar_contact_reference_data` for people. Use only ids these return; ids
   belong to one phone line and mean nothing on another.
2. **Read the current shifts** for the dates involved, so you change the right one.
3. **Say the change in plain words**: who, which level, from when to when, and whether it
   is one shift or the whole repeating series. Wait for a yes.
4. **Make it**, then read the calendar again for that window and confirm it shows what
   was asked.

| Request | How |
|---|---|
| Cover time off | One date of a repeating shift: change only that date (see below). Otherwise add a shift for the person covering with `create_calendar_event` |
| Swap two shifts | Confirm both changes before making either. If only one succeeds, tell the user immediately and do not imply the swap is complete |
| Change a repeating shift | Ask whether it's only that date or every date, then follow "One date of a repeating shift" below. Never assume the series |
| Copy a week | `copy_calendar_event` |
| Remove shifts | `delete_calendar_event` for one, `delete_calendar_events` for several. Read back exactly what will go |
| Add a person | `create_calendar_contact`, at least one way to reach them (see `contact-delivery`), then give them shifts |
| Add or edit escalation levels | Check `list_escalation_levels`, confirm the plan, then use `create_escalation_level` or `update_escalation_level` where authorized. Read back the level order. Clients can't delete a level: if they want one removed, say their answering service can remove it |

## One date of a repeating shift

"Move Saturday's shift to Dr. Patel" can mean this Saturday or every Saturday. Ask which
before changing anything, unless the person already said ("only this Saturday", "every
Saturday").

- **Only that date:** `create_calendar_event` with action `detach`. `parent_id` is the
  repeating shift, `original_start_date` is that date's start as the calendar shows it
  (for example `2026-11-21 08:00`), and `start_date`, `end_date`, `contact_id` and
  `delivery_method_ids` are what that date becomes. Leave `schedule` out. Every other
  date stays as it was.
- **Take one date off:** `update_calendar_event` with action `delete` and that date's
  start as `start_date`.
- **Every date:** `update_calendar_event` with action `update` on the repeating shift.
  Leave `schedule` out so it keeps repeating. If the tool says `schedule` is missing,
  send the shift's current `schedule` from `get_calendar_event`, unchanged. A repeating
  shift holds only its current and upcoming dates (past ones roll off), so this is also
  "from now on".
- **From a later date on** ("starting December 5"): changing every date would also change
  the dates before it. Say so and ask how to handle those dates; don't pick for them.

`update_calendar_event` on a repeating shift changes every date of it. Never send
`schedule` "null" to change one date: that stops the shift repeating and removes every
later date. Send it only when the person asks for the shift to stop repeating, together
with `stop_repeating` set to true.

## "The wrong person got called"

Escalation-level configuration differs from the delivery sequence for contacts
within a level. Do not change either as a troubleshooting shortcut. Never
delete and re-add a person to change order: removing a contact removes all
their shifts. If calls are not arriving, ask the answering service to
investigate delivery beyond what the portal tools can verify.

## Who can change what

You can change the calendar of lines where your login has Calendar Management access.
Customers with Calendar Management access may edit escalation levels.
Some contact-delivery ordering settings still need the answering service.
If access is refused, explain the required permission; do not bypass it.
